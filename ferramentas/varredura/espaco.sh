#!/usr/bin/env bash
# Diagnóstico de espaço em disco — macOS.
#
# SÓ LÊ. Não apaga, não move, não renomeia nada. Mede os lugares onde o espaço
# costuma sumir, ordena por tamanho e diz o que é seguro remover.
#
# "Seguro" aqui significa: o sistema ou a ferramenta regenera sozinho quando
# precisar. Nenhum trabalho seu é perdido.
#
# Uso:
#   ./espaco.sh                # relatório
#   ./espaco.sh --comandos     # relatório + comandos de limpeza (comentados)

set -uo pipefail

COMANDOS=0
[[ "${1:-}" == "--comandos" ]] && COMANDOS=1

# tamanho de um caminho em KB; 0 se não existir
kb() {
	[[ -e "$1" ]] || { echo 0; return; }
	du -sk "$1" 2>/dev/null | awk '{print $1}' || echo 0
}

humano() {
	awk -v k="$1" 'BEGIN{
		if (k >= 1048576) printf "%.1f GB", k/1048576;
		else if (k >= 1024) printf "%.0f MB", k/1024;
		else printf "%d KB", k
	}'
}

echo "════════════════════════════════════════════════════════"
echo " Diagnóstico de espaço — $(date '+%Y-%m-%d %H:%M')"
echo "════════════════════════════════════════════════════════"
echo
echo "── Disco ──"
df -h / | sed -n '1p;2p'
echo

LIVRE_KB=$(df -k / | awk 'NR==2{print $4}')
echo "Livre agora: $(humano "$LIVRE_KB")"
echo "Uma atualização do macOS costuma pedir de 20 a 40 GB livres."
echo

# ── candidatos: rótulo | caminho | seguro(S/R) ────────────────────────────
# S = seguro, regenerável.  R = revisar antes, pode conter trabalho seu.
CANDIDATOS=(
	"Lixeira|$HOME/.Trash|S"
	"Downloads|$HOME/Downloads|R"
	"Desktop|$HOME/Desktop|R"
	"Filmes|$HOME/Movies|R"
	"Cache npm|$HOME/.npm|S"
	"Cache pnpm|$HOME/Library/pnpm|S"
	"Store pnpm|$HOME/.pnpm-store|S"
	"Cache yarn|$HOME/Library/Caches/Yarn|S"
	"Cache bun|$HOME/.bun/install/cache|S"
	"Xcode DerivedData|$HOME/Library/Developer/Xcode/DerivedData|S"
	"Xcode Archives|$HOME/Library/Developer/Xcode/Archives|R"
	"Simuladores iOS|$HOME/Library/Developer/CoreSimulator/Devices|S"
	"Docker|$HOME/Library/Containers/com.docker.docker|S"
	"Cache pip|$HOME/Library/Caches/pip|S"
	"Cargo registry|$HOME/.cargo/registry|S"
	"Gradle|$HOME/.gradle/caches|S"
	"Caches do usuário|$HOME/Library/Caches|S"
	"Backups de iPhone/iPad|$HOME/Library/Application Support/MobileSync/Backup|R"
	"Mail|$HOME/Library/Mail|R"
	"Fotos|$HOME/Pictures/Photos Library.photoslibrary|R"
)

echo "── Onde está o peso ──"
echo
printf "%-28s %10s  %s\n" "LUGAR" "TAMANHO" "STATUS"
printf "%-28s %10s  %s\n" "----------------------------" "----------" "------"

TOTAL_SEGURO=0
LINHAS=""
for entrada in "${CANDIDATOS[@]}"; do
	IFS='|' read -r rotulo caminho seguro <<< "$entrada"
	tam=$(kb "$caminho")
	[[ "$tam" -lt 51200 ]] && continue          # ignora abaixo de 50 MB
	if [[ "$seguro" == "S" ]]; then
		TOTAL_SEGURO=$((TOTAL_SEGURO + tam))
		status="seguro apagar"
	else
		status="REVISAR antes"
	fi
	LINHAS+="$tam|$rotulo|$status|$caminho"$'\n'
done

echo "$LINHAS" | sort -t'|' -k1 -rn | while IFS='|' read -r tam rotulo status caminho; do
	[[ -z "$tam" ]] && continue
	printf "%-28s %10s  %s\n" "$rotulo" "$(humano "$tam")" "$status"
done

echo
echo "Recuperável só com o que é seguro: $(humano "$TOTAL_SEGURO")"
echo

# ── snapshots locais do Time Machine ──────────────────────────────────────
if command -v tmutil >/dev/null 2>&1; then
	SNAPS=$(tmutil listlocalsnapshots / 2>/dev/null | grep -c 'com.apple.TimeMachine' || echo 0)
	if [[ "$SNAPS" -gt 0 ]]; then
		echo "── Time Machine ──"
		echo "$SNAPS snapshot(s) local(is) ocupando espaço no disco interno."
		echo "Costuma ser o peso invisível que o Finder não mostra."
		echo
	fi
fi

# ── node_modules espalhados ───────────────────────────────────────────────
echo "── node_modules ──"
echo "Procurando (pode demorar um pouco)…"
NM_TOTAL=0
NM_LISTA=""
while IFS= read -r d; do
	t=$(kb "$d")
	NM_TOTAL=$((NM_TOTAL + t))
	[[ "$t" -ge 102400 ]] && NM_LISTA+="$t|$d"$'\n'
done < <(find "$HOME" -maxdepth 6 -type d -name node_modules -prune 2>/dev/null)

if [[ "$NM_TOTAL" -gt 0 ]]; then
	echo "Total: $(humano "$NM_TOTAL") — todos regeneráveis com um install."
	echo "$NM_LISTA" | sort -t'|' -k1 -rn | head -10 | while IFS='|' read -r t d; do
		[[ -z "$t" ]] && continue
		printf "  %10s  %s\n" "$(humano "$t")" "$d"
	done
else
	echo "Nenhum encontrado."
fi
echo

if [[ "$COMANDOS" -eq 1 ]]; then
	echo "════════════════════════════════════════════════════════"
	echo " Comandos de limpeza — TODOS COMENTADOS"
	echo " Leia, descomente só o que aprovar, e execute."
	echo "════════════════════════════════════════════════════════"
	cat <<'CMDS'

# ── 100% seguro: caches que se regeneram sozinhos ──
# npm cache clean --force
# pnpm store prune
# yarn cache clean
# rm -rf ~/Library/Developer/Xcode/DerivedData/*
# xcrun simctl delete unavailable
# docker system prune -a          # se usa Docker
# rm -rf ~/Library/Caches/pip

# ── Time Machine: snapshots locais ──
# tmutil listlocalsnapshots /      # ver antes
# tmutil thinlocalsnapshots / 21474836480 4    # libera ~20 GB

# ── Lixeira ──
# rm -rf ~/.Trash/*

# ── node_modules: apaga, e um "install" traz de volta ──
# find ~ -maxdepth 6 -type d -name node_modules -prune -exec rm -rf {} +

# ── REVISAR antes: pode ter trabalho seu ──
# Downloads, Desktop, Filmes, backups de iPhone, Fotos.
# Melhor MOVER para o disco externo do que apagar:
# rsync -av --remove-source-files ~/Movies/ "/Volumes/Seagate/Movies/"
CMDS
	echo
fi

echo "Nada foi apagado. Este script só mede."
