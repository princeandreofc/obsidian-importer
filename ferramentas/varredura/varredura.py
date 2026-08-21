#!/usr/bin/env python3
"""
Varredura e mapeamento de ambiente — multivolume.

Inventaria um ou mais volumes (Mac interno, MAC Amos, Seagate, qualquer pasta),
cruza o conteúdo entre eles e responde quatro perguntas:

	1. O que existe?            inventário por tipo, tamanho e idade
	2. O que está repetido?     duplicados exatos, por hash, ENTRE volumes
	3. O que é lixo?            .DS_Store, zero byte, temporários, vazios
	4. O que só existe em um    cópia única — risco de perda se aquele disco morrer
	   lugar?

E garimpa: procura por nome os ativos que já se sabe que estão perdidos
(MIX_MASTER_ORIGINALS, acervo MART, DNA AMOZZ, etc.) em todos os volumes.

INVARIANTE: este script NUNCA apaga, move ou renomeia nada. Ele só lê e
relata. As remoções saem num script separado, com TODAS as linhas comentadas,
para revisão humana antes de rodar.

Uso:
	python3 varredura.py ~ --incluir-volumes
	python3 varredura.py ~ "/Volumes/MAC Amos" /Volumes/Seagate
	python3 varredura.py ~ --incluir-volumes --precos --rapido

Sem dependências externas — só a biblioteca padrão.
"""

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from collections import defaultdict
from datetime import datetime, timezone

# ─────────────────────────────────────────────────────────────────────────────
# Configuração
# ─────────────────────────────────────────────────────────────────────────────

# Pastas que nunca valem a pena varrer: pesadas, geradas ou do sistema.
PODAR = {
	'node_modules', '.git', '.next', '.nuxt', '.svelte-kit', 'dist', 'build',
	'out', '.turbo', '.cache', '.parcel-cache', '__pycache__', '.venv', 'venv',
	'env', '.tox', '.mypy_cache', '.pytest_cache', 'Pods', 'DerivedData',
	'.gradle', '.m2', '.cargo', '.rustup', '.npm', '.pnpm-store', '.yarn',
	'.Trash', '.Trashes', '.Spotlight-V100', '.fseventsd', '.TemporaryItems',
	'.DocumentRevisions-V100', '.vol', 'System', 'Applications',
	'.DocumentRevisions', 'com.apple.TimeMachine.localsnapshots',
}

# Lixo reconhecível pelo nome.
LIXO_NOMES = {'.DS_Store', 'Thumbs.db', 'desktop.ini', '.localized', 'Icon\r'}
LIXO_EXT = {'.tmp', '.temp', '.crdownload', '.part', '.partial', '.download'}

# Nomes que denunciam cópia feita à mão.
RE_COPIA = re.compile(
	r'(\scopy(\s\d+)?$|\scópia(\s\d+)?$|\(\d+\)$|\s\d+$|_copy$|_old$|_bkp$|_backup$|-final-final)',
	re.IGNORECASE,
)

# Ativos que o dossiê diz estarem perdidos ou fora de alcance. O garimpo
# procura por estes nomes em TODOS os volumes varridos.
GARIMPO_PADRAO = [
	'MIX_MASTER_ORIGINALS',
	'MART',
	'AMOZZ',
	'De-AI',
	'DeAI',
	'CENTRAL_DE_CONTROLE',
	'TABELA_PRECOS',
	'alilove',
	'ali love',
	'princeandre',
	'prince andre',
	'puressencia',
	'climbex',
	'EPK',
	'Fernando Bento',
	'Eco Music',
	'Cosmic Rave',
]

# Valores da tabela de preço morta (F9/B5). O scan de preços procura por eles
# em arquivos de texto para achar propostas antigas ainda circulando.
PRECOS_MORTOS = ['1.500', '2.800', '4.500', '1500', '2800', '4500']
EXT_TEXTO = {
	'.md', '.txt', '.html', '.htm', '.json', '.js', '.ts', '.tsx', '.jsx',
	'.css', '.csv', '.yml', '.yaml', '.xml', '.svg', '.astro', '.vue', '.py',
}

LEGIVEL = ('B', 'KB', 'MB', 'GB', 'TB')


def humano(n):
	"""Tamanho em bytes -> string legível."""
	f = float(n)
	for u in LEGIVEL:
		if f < 1024 or u == 'TB':
			return f'{f:.0f} {u}' if u == 'B' else f'{f:.1f} {u}'
		f /= 1024
	return f'{f:.1f} TB'


# ─────────────────────────────────────────────────────────────────────────────
# Descoberta de volumes
# ─────────────────────────────────────────────────────────────────────────────

def descobrir_raizes(args):
	"""Resolve a lista de (rótulo, caminho) que será varrida."""
	raizes = []
	for r in args.raizes:
		p = os.path.abspath(os.path.expanduser(r))
		if os.path.isdir(p):
			raizes.append((os.path.basename(p.rstrip('/')) or p, p))
		else:
			print(f'  ! ignorado (não é pasta): {r}', file=sys.stderr)

	if args.incluir_volumes and os.path.isdir('/Volumes'):
		for nome in sorted(os.listdir('/Volumes')):
			p = os.path.join('/Volumes', nome)
			# O volume de boot aparece em /Volumes como link — não varrer duas vezes.
			if os.path.islink(p) or not os.path.isdir(p):
				continue
			if any(os.path.samefile(p, q) for _, q in raizes if os.path.exists(q)):
				continue
			raizes.append((nome, p))

	return raizes


# ─────────────────────────────────────────────────────────────────────────────
# Varredura
# ─────────────────────────────────────────────────────────────────────────────

def varrer(rotulo, raiz, arquivos, projetos, erros):
	"""Percorre uma raiz, coletando arquivos e marcando projetos."""
	vistos = 0
	for pasta, subpastas, nomes in os.walk(raiz, topdown=True, onerror=erros.append):
		base = os.path.basename(pasta)

		# Marca o projeto ANTES de podar, senão .git some da lista.
		if '.git' in subpastas:
			projetos.append(inspecionar_repo(pasta, rotulo))
		if '.vercel' in subpastas:
			projetos.append(inspecionar_vercel(pasta, rotulo))

		subpastas[:] = [s for s in subpastas if s not in PODAR and not s.startswith('.git')]

		for nome in nomes:
			caminho = os.path.join(pasta, nome)
			try:
				st = os.lstat(caminho)
			except OSError as e:
				erros.append(e)
				continue
			if not os.path.isfile(caminho) or os.path.islink(caminho):
				continue

			arquivos.append({
				'caminho': caminho,
				'nome': nome,
				'vol': rotulo,
				'tamanho': st.st_size,
				'mtime': st.st_mtime,
				'ext': os.path.splitext(nome)[1].lower(),
				'pasta': base,
			})
			vistos += 1
			if vistos % 20000 == 0:
				print(f'  … {rotulo}: {vistos} arquivos', file=sys.stderr)

	return vistos


def inspecionar_repo(caminho, vol):
	"""Lê branch, remote e estado sujo de um repositório git."""
	def g(*a):
		try:
			return subprocess.run(
				['git', '-C', caminho, *a],
				capture_output=True, text=True, timeout=15,
			).stdout.strip()
		except Exception:
			return ''

	sujo = g('status', '--porcelain')
	return {
		'tipo': 'git',
		'vol': vol,
		'caminho': caminho,
		'branch': g('rev-parse', '--abbrev-ref', 'HEAD'),
		'remote': g('remote', 'get-url', 'origin'),
		'ultimo_commit': g('log', '-1', '--format=%h %ad %s', '--date=short'),
		'sujo': len([l for l in sujo.splitlines() if l.strip()]),
	}


def inspecionar_vercel(caminho, vol):
	"""Lê o nome do projeto Vercel de .vercel/project.json."""
	alvo = os.path.join(caminho, '.vercel', 'project.json')
	dados = {}
	try:
		with open(alvo, encoding='utf-8') as f:
			dados = json.load(f)
	except Exception:
		pass
	return {
		'tipo': 'vercel',
		'vol': vol,
		'caminho': caminho,
		'projeto': dados.get('projectName') or dados.get('projectId', '?'),
		'org': dados.get('orgId', ''),
	}


# ─────────────────────────────────────────────────────────────────────────────
# Duplicados
# ─────────────────────────────────────────────────────────────────────────────

def hash_rapido(caminho, tamanho):
	"""Assinatura barata: começo + fim do arquivo. Descarta a maioria dos falsos."""
	h = hashlib.blake2b(digest_size=16)
	try:
		with open(caminho, 'rb') as f:
			h.update(f.read(65536))
			if tamanho > 131072:
				f.seek(-65536, os.SEEK_END)
				h.update(f.read(65536))
	except OSError:
		return None
	return h.hexdigest()


def hash_completo(caminho):
	h = hashlib.sha256()
	try:
		with open(caminho, 'rb') as f:
			for bloco in iter(lambda: f.read(1024 * 1024), b''):
				h.update(bloco)
	except OSError:
		return None
	return h.hexdigest()


def achar_duplicados(arquivos, max_hash_bytes, rapido):
	"""
	Três passadas, da mais barata para a mais cara:
	tamanho -> hash das pontas -> sha256 completo.

	Cada passada só pode DIVIDIR os grupos da anterior, nunca fundi-los —
	senão arquivos já provados diferentes voltariam a cair juntos. Por isso a
	passada 3 refina cada grupo isoladamente, em vez de rechavear tudo num
	dicionário só.

	Devolve [{'itens': [...], 'exato': bool}]. 'exato' é False quando o grupo
	foi fechado pelo hash das pontas, sem sha256 completo — provável, não provado.
	"""
	por_tamanho = defaultdict(list)
	for a in arquivos:
		if a['tamanho'] > 0:
			por_tamanho[a['tamanho']].append(a)
	candidatos = [g for g in por_tamanho.values() if len(g) > 1]
	print(f'  … {sum(len(g) for g in candidatos)} arquivos com tamanho repetido', file=sys.stderr)

	por_pontas = defaultdict(list)
	for grupo in candidatos:
		for a in grupo:
			hp = hash_rapido(a['caminho'], a['tamanho'])
			if hp:
				por_pontas[(a['tamanho'], hp)].append(a)
	# Cada grupo aqui tem o MESMO tamanho e o MESMO hash das pontas.
	candidatos = [g for g in por_pontas.values() if len(g) > 1]

	if rapido:
		return [{'itens': g, 'exato': False} for g in candidatos]

	resultado = []
	for grupo in candidatos:
		if grupo[0]['tamanho'] > max_hash_bytes:
			# Grande demais para sha256: mantém o grupo como está, marcado
			# como provável. Não se mistura com nenhum outro grupo.
			resultado.append({'itens': grupo, 'exato': False})
			continue
		por_hash = defaultdict(list)
		for a in grupo:
			hc = hash_completo(a['caminho'])
			if hc:
				por_hash[hc].append(a)
		resultado += [{'itens': g, 'exato': True} for g in por_hash.values() if len(g) > 1]
	return resultado


# ─────────────────────────────────────────────────────────────────────────────
# Análises
# ─────────────────────────────────────────────────────────────────────────────

def garimpar(arquivos, padroes):
	"""Procura ativos conhecidos por nome, em todos os volumes."""
	achados = defaultdict(list)
	baixos = [(p, p.lower()) for p in padroes]
	for a in arquivos:
		alvo = a['caminho'].lower()
		for original, p in baixos:
			if p in alvo:
				achados[original].append(a)
	return achados


def escanear_precos(arquivos, limite_bytes=2_000_000):
	"""Procura os valores da tabela morta dentro de arquivos de texto."""
	ocorrencias = []
	for a in arquivos:
		if a['ext'] not in EXT_TEXTO or a['tamanho'] > limite_bytes:
			continue
		try:
			with open(a['caminho'], encoding='utf-8', errors='ignore') as f:
				texto = f.read()
		except OSError:
			continue
		batidas = sorted({v for v in PRECOS_MORTOS if v in texto})
		if len(batidas) >= 2:  # dois ou mais valores = provável tabela, não coincidência
			ocorrencias.append({**a, 'valores': batidas})
	return ocorrencias


def classificar(arquivos, grupos_dup, dias_frio):
	"""Separa lixo, cópias-únicas e arquivos frios."""
	agora = datetime.now(timezone.utc).timestamp()
	frio_s = dias_frio * 86400

	em_grupo = set()
	for g in grupos_dup:
		for a in g['itens']:
			em_grupo.add(a['caminho'])

	lixo, frios, so_um_lugar = [], [], []
	for a in arquivos:
		nome, ext = a['nome'], a['ext']
		if nome in LIXO_NOMES or ext in LIXO_EXT or a['tamanho'] == 0:
			lixo.append(a)
			continue
		if 'download' in a['caminho'].lower() and (agora - a['mtime']) > frio_s:
			frios.append(a)
		# Cópia única: não aparece em nenhum grupo de duplicados.
		if a['caminho'] not in em_grupo and a['tamanho'] > 1_000_000:
			so_um_lugar.append(a)

	return lixo, frios, so_um_lugar


def cruzar_volumes(grupos_dup):
	"""Para cada grupo duplicado, em quais volumes ele aparece."""
	espalhados, internos = [], []
	for g in grupos_dup:
		vols = sorted({a['vol'] for a in g['itens']})
		destino = espalhados if len(vols) > 1 else internos
		destino.append({'vols': vols, 'itens': g['itens'], 'exato': g['exato']})
	return espalhados, internos


# ─────────────────────────────────────────────────────────────────────────────
# Saídas
# ─────────────────────────────────────────────────────────────────────────────

def tabela(linhas, cabecalho):
	out = ['| ' + ' | '.join(cabecalho) + ' |',
	       '|' + '|'.join(['---'] * len(cabecalho)) + '|']
	out += ['| ' + ' | '.join(str(c) for c in l) + ' |' for l in linhas]
	return '\n'.join(out)


def escrever_relatorio(destino, ctx):
	a = ctx['arquivos']
	total_bytes = sum(f['tamanho'] for f in a)
	desperdicio = sum(
		sum(i['tamanho'] for i in g['itens'][1:])
		for g in ctx['espalhados'] + ctx['internos']
	)

	L = []
	L.append('# Varredura de ambiente\n')
	L.append(f'> Gerado em {ctx["quando"]} · somente leitura · nada foi apagado, movido ou renomeado.\n')

	L.append('## 1. Volumes varridos\n')
	L.append(tabela(
		[(r, c, f'{ctx["por_vol"].get(r, 0):,}'.replace(',', '.'),
		  humano(ctx['bytes_vol'].get(r, 0))) for r, c in ctx['raizes']],
		['Volume', 'Caminho', 'Arquivos', 'Tamanho'],
	))
	L.append('')

	L.append('## 2. Resumo\n')
	L.append(tabela([
		('Arquivos inventariados', f'{len(a):,}'.replace(',', '.')),
		('Volume total', humano(total_bytes)),
		('Grupos de duplicados', len(ctx['espalhados']) + len(ctx['internos'])),
		('— entre volumes diferentes', len(ctx['espalhados'])),
		('— dentro do mesmo volume', len(ctx['internos'])),
		('Espaço recuperável (duplicados)', humano(desperdicio)),
		('Lixo reconhecido', len(ctx['lixo'])),
		('Downloads frios', len(ctx['frios'])),
		('Arquivos >1 MB com CÓPIA ÚNICA', len(ctx['so_um'])),
		('Repositórios git', len([p for p in ctx['projetos'] if p['tipo'] == 'git'])),
		('Projetos Vercel', len([p for p in ctx['projetos'] if p['tipo'] == 'vercel'])),
	], ['Métrica', 'Valor']))
	L.append('')

	L.append('## 3. Garimpo — ativos procurados\n')
	L.append('Os nomes abaixo vêm dos bloqueios do dossiê. "0" significa que o ativo\n'
	         'não está em nenhum volume varrido — e aí o bloqueio continua de pé.\n')
	L.append(tabela(
		[(p, len(ctx['garimpo'].get(p, [])),
		  ', '.join(sorted({x['vol'] for x in ctx['garimpo'].get(p, [])})) or '—')
		 for p in ctx['padroes']],
		['Procurado', 'Achados', 'Volumes'],
	))
	L.append('')
	for p in ctx['padroes']:
		itens = ctx['garimpo'].get(p, [])
		if not itens:
			continue
		L.append(f'<details><summary><code>{p}</code> — {len(itens)} achado(s)</summary>\n')
		for x in sorted(itens, key=lambda i: -i['tamanho'])[:40]:
			L.append(f'- `[{x["vol"]}]` {x["caminho"]} — {humano(x["tamanho"])}')
		if len(itens) > 40:
			L.append(f'- … e mais {len(itens) - 40}')
		L.append('\n</details>\n')

	L.append('## 4. Duplicados ENTRE volumes\n')
	L.append('O que já está em mais de um disco. Estes são os seguros de apagar\n'
	         'em um dos lados — ainda existe cópia.\n')
	if ctx['espalhados']:
		top = sorted(ctx['espalhados'],
		             key=lambda g: -sum(i['tamanho'] for i in g['itens'][1:]))[:60]
		for g in top:
			it = g['itens']
			selo = '' if g['exato'] else '  ⚠️ **provável** — fechado pelo hash das pontas, sem sha256 completo'
			L.append(f'**{it[0]["nome"]}** — {humano(it[0]["tamanho"])} × {len(it)} '
			         f'· volumes: {", ".join(g["vols"])}{selo}')
			for x in it:
				L.append(f'  - `[{x["vol"]}]` {x["caminho"]}')
			L.append('')
	else:
		L.append('_Nenhum._\n')

	L.append('## 5. CÓPIA ÚNICA — risco de perda\n')
	L.append('Arquivos acima de 1 MB que existem em um só lugar. Se aquele disco\n'
	         'morrer, isto morre junto. Os maiores primeiro.\n')
	if ctx['so_um']:
		L.append(tabela(
			[(x['vol'], humano(x['tamanho']),
			  datetime.fromtimestamp(x['mtime']).strftime('%Y-%m-%d'),
			  f'`{x["caminho"]}`')
			 for x in sorted(ctx['so_um'], key=lambda i: -i['tamanho'])[:80]],
			['Volume', 'Tamanho', 'Modificado', 'Caminho'],
		))
	else:
		L.append('_Nenhum._')
	L.append('')

	L.append('## 6. Repositórios e projetos\n')
	gits = [p for p in ctx['projetos'] if p['tipo'] == 'git']
	if gits:
		L.append(tabela(
			[(g['vol'], f'`{g["caminho"]}`', g['branch'] or '?',
			  ('⚠️ ' + str(g['sujo'])) if g['sujo'] else 'limpo',
			  g['remote'] or '—')
			 for g in sorted(gits, key=lambda i: i['caminho'])],
			['Volume', 'Caminho', 'Branch', 'Sujo', 'Remote'],
		))
		L.append('')
	vercs = [p for p in ctx['projetos'] if p['tipo'] == 'vercel']
	if vercs:
		L.append('**Projetos Vercel**\n')
		L.append(tabela(
			[(v['vol'], v['projeto'], f'`{v["caminho"]}`') for v in vercs],
			['Volume', 'Projeto', 'Caminho'],
		))
		L.append('')

	if ctx['precos']:
		L.append('## 7. Preços da tabela morta ainda circulando\n')
		L.append('Arquivos com dois ou mais valores da tabela antiga (1.500 / 2.800 / 4.500).\n')
		L.append(tabela(
			[(p['vol'], ', '.join(p['valores']), f'`{p["caminho"]}`')
			 for p in sorted(ctx['precos'], key=lambda i: i['caminho'])[:120]],
			['Volume', 'Valores', 'Caminho'],
		))
		L.append('')

	L.append('## 8. Lixo e downloads frios\n')
	L.append(f'- Lixo reconhecido: **{len(ctx["lixo"])}** arquivos, {humano(sum(x["tamanho"] for x in ctx["lixo"]))}\n')
	L.append(f'- Downloads sem toque há {ctx["dias_frio"]}+ dias: **{len(ctx["frios"])}** arquivos, '
	         f'{humano(sum(x["tamanho"] for x in ctx["frios"]))}\n')
	L.append('\nAmbos saem listados em `revisar.sh`, comentados, para você aprovar um a um.\n')

	if ctx['erros']:
		L.append('## 9. Erros de leitura\n')
		L.append(f'{len(ctx["erros"])} caminhos não puderam ser lidos '
		         '(permissão, disco desconectado, nome inválido). '
		         'Veja `mapa.json` → `erros`.\n')

	with open(destino, 'w', encoding='utf-8') as f:
		f.write('\n'.join(L) + '\n')


def escrever_script_revisao(destino, ctx):
	"""Gera um .sh com TUDO comentado. O humano descomenta o que aprova."""
	L = [
		'#!/usr/bin/env bash',
		'# Candidatos a remoção — gerado pela varredura.',
		'#',
		'# TODAS as linhas estão comentadas de propósito. Nada roda como está.',
		'# Leia, descomente SÓ o que você aprova, e execute.',
		'#',
		'# Sugestão: rode primeiro com as linhas de "lixo", que são seguras.',
		'set -euo pipefail',
		'',
		'# ─── Lixo do sistema e arquivos vazios ───',
	]
	for x in ctx['lixo']:
		L.append(f'# rm -- {sh(x["caminho"])}')

	por_peso = sorted(ctx['espalhados'], key=lambda g: -sum(i['tamanho'] for i in g['itens'][1:]))
	exatos = [g for g in por_peso if g['exato']]
	provaveis = [g for g in por_peso if not g['exato']]

	L.append('')
	L.append('# ─── Duplicados CONFIRMADOS byte a byte (sha256) ───')
	L.append('# Mantém a 1ª cópia, lista as demais.')
	for g in exatos:
		it = g['itens']
		L.append(f'#  MANTER: {it[0]["caminho"]}  ({humano(it[0]["tamanho"])})')
		for x in it[1:]:
			L.append(f'# rm -- {sh(x["caminho"])}')
		L.append('#')

	if provaveis:
		L.append('')
		L.append('# ═══════════════════════════════════════════════════════════')
		L.append('# ATENÇÃO — os grupos abaixo NÃO foram confirmados byte a byte.')
		L.append('# São arquivos grandes, fechados só pelo tamanho e pelo hash do')
		L.append('# começo e do fim. É provável que sejam iguais, mas não está provado.')
		L.append('#')
		L.append('# Antes de descomentar qualquer linha daqui, confirme o par:')
		L.append('#     shasum -a 256 ARQUIVO_A ARQUIVO_B')
		L.append('# ═══════════════════════════════════════════════════════════')
		for g in provaveis:
			it = g['itens']
			L.append(f'#  MANTER: {it[0]["caminho"]}  ({humano(it[0]["tamanho"])})')
			for x in it[1:]:
				L.append(f'# rm -- {sh(x["caminho"])}   # NÃO CONFIRMADO')
			L.append('#')

	L.append('')
	L.append(f'# ─── Downloads sem uso há {ctx["dias_frio"]}+ dias ───')
	for x in sorted(ctx['frios'], key=lambda i: -i['tamanho']):
		L.append(f'# rm -- {sh(x["caminho"])}   # {humano(x["tamanho"])}')

	with open(destino, 'w', encoding='utf-8') as f:
		f.write('\n'.join(L) + '\n')
	os.chmod(destino, 0o755)


def sh(caminho):
	"""Aspas seguras para shell."""
	return "'" + caminho.replace("'", "'\\''") + "'"


def escrever_json(destino, ctx):
	def enxuto(x):
		return {'caminho': x['caminho'], 'vol': x['vol'], 'tamanho': x['tamanho'],
		        'mtime': round(x['mtime'])}

	dados = {
		'gerado_em': ctx['quando'],
		'raizes': [{'rotulo': r, 'caminho': c} for r, c in ctx['raizes']],
		'resumo': {
			'arquivos': len(ctx['arquivos']),
			'bytes': sum(f['tamanho'] for f in ctx['arquivos']),
			'grupos_duplicados': len(ctx['espalhados']) + len(ctx['internos']),
			'duplicados_entre_volumes': len(ctx['espalhados']),
			'lixo': len(ctx['lixo']),
			'downloads_frios': len(ctx['frios']),
			'copia_unica': len(ctx['so_um']),
		},
		'garimpo': {p: [enxuto(x) for x in itens] for p, itens in ctx['garimpo'].items()},
		'duplicados_entre_volumes': [
			{'vols': g['vols'], 'exato': g['exato'],
			 'itens': [enxuto(x) for x in g['itens']]}
			for g in ctx['espalhados']
		],
		'copia_unica': [enxuto(x) for x in sorted(ctx['so_um'], key=lambda i: -i['tamanho'])[:2000]],
		'projetos': ctx['projetos'],
		'precos_mortos': [{**enxuto(p), 'valores': p['valores']} for p in ctx['precos']],
		'erros': [str(e) for e in ctx['erros'][:500]],
	}
	with open(destino, 'w', encoding='utf-8') as f:
		json.dump(dados, f, ensure_ascii=False, indent=2)


# ─────────────────────────────────────────────────────────────────────────────

def main():
	ap = argparse.ArgumentParser(
		description='Varredura multivolume: inventário, duplicados, garimpo. Nunca apaga.',
	)
	ap.add_argument('raizes', nargs='*', default=[os.path.expanduser('~')],
	                help='pastas ou volumes a varrer (padrão: home)')
	ap.add_argument('--incluir-volumes', action='store_true',
	                help='varre também tudo em /Volumes (MAC Amos, Seagate, etc.)')
	ap.add_argument('--saida', default=None, help='pasta de saída')
	ap.add_argument('--dias-frio', type=int, default=90,
	                help='Downloads sem uso há N dias (padrão 90)')
	ap.add_argument('--max-hash-mb', type=int, default=2048,
	                help='acima disso, confia no hash das pontas (padrão 2048)')
	ap.add_argument('--rapido', action='store_true',
	                help='pula o sha256 completo — mais rápido, um pouco menos exato')
	ap.add_argument('--precos', action='store_true',
	                help='procura a tabela de preço morta dentro de arquivos de texto')
	ap.add_argument('--procurar', action='append', default=[],
	                help='padrão extra para o garimpo (pode repetir)')
	args = ap.parse_args()

	raizes = descobrir_raizes(args)
	if not raizes:
		print('Nenhuma raiz válida. Nada a fazer.', file=sys.stderr)
		return 1

	saida = args.saida or os.path.abspath(
		'varredura-' + datetime.now().strftime('%Y%m%d-%H%M'))
	os.makedirs(saida, exist_ok=True)

	print(f'Varrendo {len(raizes)} volume(s) → {saida}', file=sys.stderr)

	arquivos, projetos, erros = [], [], []
	por_vol, bytes_vol = {}, {}
	for rotulo, caminho in raizes:
		print(f'· {rotulo} ({caminho})', file=sys.stderr)
		antes = len(arquivos)
		varrer(rotulo, caminho, arquivos, projetos, erros)
		novos = arquivos[antes:]
		por_vol[rotulo] = len(novos)
		bytes_vol[rotulo] = sum(x['tamanho'] for x in novos)

	print(f'  {len(arquivos)} arquivos. Procurando duplicados…', file=sys.stderr)
	grupos = achar_duplicados(arquivos, args.max_hash_mb * 1024 * 1024, args.rapido)
	espalhados, internos = cruzar_volumes(grupos)

	print('  Classificando e garimpando…', file=sys.stderr)
	lixo, frios, so_um = classificar(arquivos, grupos, args.dias_frio)
	padroes = GARIMPO_PADRAO + args.procurar
	garimpo = garimpar(arquivos, padroes)

	precos = []
	if args.precos:
		print('  Escaneando preços…', file=sys.stderr)
		precos = escanear_precos(arquivos)

	ctx = {
		'quando': datetime.now().strftime('%Y-%m-%d %H:%M'),
		'raizes': raizes, 'arquivos': arquivos, 'projetos': projetos,
		'espalhados': espalhados, 'internos': internos, 'lixo': lixo,
		'frios': frios, 'so_um': so_um, 'garimpo': garimpo, 'padroes': padroes,
		'precos': precos, 'erros': erros, 'dias_frio': args.dias_frio,
		'por_vol': por_vol, 'bytes_vol': bytes_vol,
	}

	escrever_relatorio(os.path.join(saida, 'RELATORIO.md'), ctx)
	escrever_json(os.path.join(saida, 'mapa.json'), ctx)
	escrever_script_revisao(os.path.join(saida, 'revisar.sh'), ctx)

	print(f'\nPronto.\n  {saida}/RELATORIO.md   ← leia este\n'
	      f'  {saida}/mapa.json       ← para o agente\n'
	      f'  {saida}/revisar.sh      ← tudo comentado, você aprova\n', file=sys.stderr)
	return 0


if __name__ == '__main__':
	sys.exit(main())
