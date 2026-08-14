# Pacote de Varredura — mapeamento de ambiente multivolume

> **Para quem pega isto frio** (GPT, Codex, Claude Code local, ou pessoa).
> Este documento é autossuficiente: contrato, comandos, saídas esperadas e as
> regras que não podem ser quebradas. Leia a seção 0 antes de executar qualquer coisa.

---

## 0. Contrato

**O que este pacote faz**
Inventaria um ou mais volumes, cruza o conteúdo entre eles e responde:
o que existe, o que está repetido, o que é lixo, o que só tem uma cópia,
e onde estão os ativos que o dossiê dá como perdidos.

**O que este pacote NÃO faz**
Não apaga. Não move. Não renomeia. Não faz deploy. Não envia nada.
Não altera nenhum arquivo existente. É leitura pura.
As remoções saem num script à parte, com **todas as linhas comentadas** —
nada roda sem um humano descomentar linha por linha.

**Por que a varredura roda na máquina, e não numa sessão em nuvem**
Sessões do Claude Code na web rodam em container isolado, sem acesso ao disco
do usuário nem aos volumes externos. O material real (Mac interno, `MAC Amos`,
Seagate, iCloud) só é alcançável de um agente rodando **localmente**.
Nenhuma autorização, permissão ou token muda isso — é limite de arquitetura,
não de permissão. Portanto: **execute na máquina onde os discos estão montados.**

---

## 1. Estado conhecido antes de varrer

Consolidado em 11/ago/2026. Não recomeçar nada — isto aponta para o que já existe.

**Verificado (tem arquivo provando)**

- Domínio canônico do Ali Love é `www.alilove.world`.
  O `CENTRAL_DE_CONTROLE.md` ainda lista `alilove.vercel.app` e declara de si
  mesmo que "se divergirem, vale a CENTRAL" — ou seja, **induz ao erro**.
  A CENTRAL é documento canônico do Amós: **não editar sem autorização dele.**
- Existem **dois** projetos Vercel para o Ali Love: `alilove` (site oficial) e
  `alilove-vinyl` (peça separada, guarda a página de entrega).
  Confirmar em qual se está mexendo antes de qualquer entrega.
- Da página de entrega: *"Do not switch alilove.world off. Redirect it."*
  Se migrar, **301** — nunca desligar.
- O EPK do Prince Andre existe como esqueleto em `/prince-andre/epk/`, com
  `noindex, nofollow` e fora do sitemap, servido pelo projeto `andre-corporate`
  (domínio da AB Motion, não do artista).
- **Três** tabelas de preço vivas ao mesmo tempo:
  `790 / 1.690 / 2.900` (canônica, 08/ago) ·
  `1.500 / 2.800 / 4.500` (morta, ainda no repositório) ·
  `14.900 / 19.900` (acervo/checkout, ausentes da canônica).
  30 ocorrências da tabela morta em `andre-portfolio`, inclusive em proposta
  comercial `.html` e `.docx`.

**Fora de alcance — é isto que a varredura vai procurar**

| Ativo | Onde se acredita que esteja | Bloqueio |
|---|---|---|
| `MIX_MASTER_ORIGINALS.md` | volume `MAC Amos` | B3 |
| Acervo MART Decoração (planilhas, lâminas, catálogos) | iCloud | B8 |
| DNA AMOZZ · pipeline De-AI | volume `MAC Amos` | F6 |

Se a varredura **não achar** um destes em nenhum volume, o bloqueio continua
de pé e isso deve ser registrado — **não inventar o conteúdo nem o processo.**

---

## 2. Como executar

Requer apenas `python3` (biblioteca padrão, zero dependências).

```bash
# 1. Varredura completa: home + todos os volumes montados
python3 varredura.py ~ --incluir-volumes --precos

# 2. Ou nomeando os volumes explicitamente (aspas por causa do espaço)
python3 varredura.py ~ "/Volumes/MAC Amos" /Volumes/Seagate --precos

# 3. Primeira passada rápida em disco grande ou lento (pula o sha256 completo)
python3 varredura.py ~ --incluir-volumes --rapido

# 4. Garimpo extra além da lista padrão
python3 varredura.py ~ --incluir-volumes --procurar "Tina" --procurar "Mercos"
```

Opções que importam:

| Flag | Efeito |
|---|---|
| `--incluir-volumes` | varre tudo em `/Volumes` — MAC Amos, Seagate, pendrives |
| `--precos` | procura a tabela morta dentro de arquivos de texto |
| `--rapido` | confia no hash das pontas; bem mais rápido, um pouco menos exato |
| `--dias-frio N` | idade para considerar um Download abandonado (padrão 90) |
| `--max-hash-mb N` | acima disso não faz sha256 completo (padrão 2048) |
| `--procurar P` | acrescenta um padrão ao garimpo (pode repetir) |

Discos externos são lentos. Numa primeira volta use `--rapido`; depois rode a
completa só nos volumes que interessarem.

---

## 3. O que sai

Numa pasta `varredura-AAAAMMDD-HHMM/`:

| Arquivo | Para quem | Conteúdo |
|---|---|---|
| `RELATORIO.md` | humano | inventário, garimpo, duplicados, cópias únicas, projetos, preços |
| `mapa.json` | agente | os mesmos dados, estruturados, para consumo por LLM |
| `revisar.sh` | humano | candidatos a remoção, **100% comentados** |

Seções do relatório, na ordem em que devem ser lidas:

1. **Volumes varridos** — confirma que o disco certo estava montado.
   Se `MAC Amos` não aparecer aqui, ele não estava conectado: **repita**.
2. **Resumo** — números gerais e espaço recuperável.
3. **Garimpo** — os ativos perdidos. Esta é a seção que derruba B3 e B8.
4. **Duplicados entre volumes** — o que já existe em mais de um disco.
   É o que se pode apagar de um lado com segurança.
5. **Cópia única** — arquivos >1 MB que existem em um lugar só.
   Se aquele disco morrer, isto morre junto. **Backup antes de limpar qualquer coisa.**
6. **Repositórios e projetos** — todo git (branch, remote, sujo) e todo projeto Vercel.
7. **Preços da tabela morta** — arquivos com dois ou mais valores antigos (B5).
8. **Lixo e downloads frios**.

---

## 4. Ordem de operação recomendada

Nesta ordem, e não em outra:

1. **Rodar a varredura** com todos os volumes montados.
2. **Ler a seção Cópia única primeiro.** Antes de apagar qualquer coisa, garantir
   que o que tem uma cópia só esteja copiado para um segundo lugar.
3. **Ler o Garimpo.** Se `MIX_MASTER_ORIGINALS` ou o acervo MART apareceram,
   copiar uma amostra para o repositório e derrubar B3/B8.
4. **Só então** abrir `revisar.sh`, começando pelo bloco de lixo, que é o seguro.
5. **Duplicados entre volumes** por último, conferindo caso a caso qual cópia
   manter — a mais recente nem sempre é a boa.

Nunca inverter os passos 2 e 5.

---

## 5. Regras que não podem ser quebradas

Valem para qualquer agente que execute este pacote.

1. **Não apagar nada automaticamente.** Nem lixo. O `revisar.sh` existe para
   que a decisão seja humana e explícita.
2. **Não editar `CENTRAL_DE_CONTROLE.md`.** É documento canônico do Amós.
   Divergências se registram como pendência, não se corrigem por conta própria.
3. **Não publicar, deployar nem enviar nada.** Nenhum `vercel deploy`, nenhum
   e-mail, nenhuma alteração financeira.
4. **Não misturar as marcas.** Nada de campanha do Prince Andre, widget Climbex,
   CTA comercial de outra marca ou peça institucional dentro do site do Ali Love.
5. **Não levar preço à mesa antes de B5 cair.** Enquanto houver três tabelas
   vivas, nenhum número é confiável.
6. **Não inventar processo para ativo ausente.** Se `MIX_MASTER_ORIGINALS.md`
   não aparecer, registrar o bloqueio — não deduzir o pipeline de áudio.
7. **Relato não vira fato.** O que veio de conversa fica marcado como hipótese
   até existir documento.

---

## 6. O que a varredura NÃO resolve

Ela mapeia disco. Não decide. Continuam abertos, e todos dependem de decisão
humana — nenhum é técnico:

| # | Bloqueio | Dono |
|---|---|---|
| B1 | Domínio canônico do Prince Andre; acesso ao GoDaddy perdido | Amós |
| B2 | Nenhum caso real da Pop autorizado | Amós · Tina |
| B4 | Clipes de Fernando Bento sem seleção nem autorização | Amós · Fernando |
| B5 | Qual tabela de preço vale | Amós |
| B6 | Planos da OpenAI não verificados no painel oficial | Amós |
| B7 | Nenhum registro do que houve na reunião de 06/08 | Amós |

B3 e B8 saem desta lista **se e somente se** o garimpo achar os ativos.

---

*Somente leitura. Nenhum arquivo existente é apagado, movido ou reescrito.*
