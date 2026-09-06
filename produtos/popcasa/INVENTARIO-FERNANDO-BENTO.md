# INVENTÁRIO — tudo do Fernando Bento / Grupo POP (06/09/2026)

Varredura feita pela retaguarda (repo + Vercel + Gmail + Drive, somente
leitura) para a **entrega final do Enterprise Hub**. O Codex/Claude local
completa com a varredura do Mac (§E) e NÃO copia material de terceiro
para este repo (ele é público).

## A · No repositório (18 arquivos)

**Núcleo Pop Casa** (`produtos/popcasa/`):
- `ARQUITETURA_CASA_NAVEGAVEL.md` — visão + plano comercial 3 fases
  (piloto → Camargo & Pinheiro → MART) + inspetor híbrido 2D/3D
- `GRUPO_POP_MARCAS.md` — 4 marcas próprias (POPComm, HighFY, We Pick,
  Pop Educ); marcas-cliente SÓ com lista oficial do Fernando
- `CATALOGO_STUDIO_L_2026.md` — catálogo Studio L
- `HEYGEN_PROMPTS_LOJA_2026-08-21.md` — prompts de vídeo da loja
- `experiencia/exp-src.html` + `experiencia/experiencia-pop-casa.html` —
  a EXPERIÊNCIA navegável (fonte + build)
- `loja/loja-pop-casa.html` — a LOJA

**Pop Com** (`produtos/popcom/`):
- `FIXACAO_OBJETOS.md` · `cerebro-campanhas.html` ·
  `HANDOFF_ALILOVE_PRINCEANDRE.md` (conferir se está na pasta certa)

**Holding/entrega**: `produtos/holding/CAMINHO_CODEX_ENTREGA_HOLDING.md`
(o roteiro de entrega do Codex!) · `produtos/holding/IMPLEMENTACAO_IMEDIATA.md`
· `ferramentas/varredura/PACOTE_VARREDURA.md` · `pesquisa/achados/2026-08-21.md`

## B · Na Vercel (previews vivos, team admin-72622007s-projects)

`pop-casa-client-20260821` · `pop-casa-studio-20260821` ·
`pop-casa-meeting-demo-20260821` (demo de fechamento B2B) ·
`camargo-decor-20260821` · `popcom-casa`

## C · No Gmail (trilha comercial — contatos e anexos)

| Data | Thread | O quê |
| --- | --- | --- |
| 28/07 | "Contato PopCom com Climbex Global e ABMotion" | 1º contato do Dr. Brenno (anexo ~635 KB) |
| 05/08 | "Apresentação ClimbEx Global - Trajetum - AB Motion Group" | Apresentação p/ Tina+Fernando (anexo ~1,15 MB) |
| 11/08 | "Próximas etapas e primeira visão ClimbEx p/ Grupo POP" | Visão + anexo ~510 KB; **02/09 o André retomou com a Tina** |

Contatos: **tina.macedo@grupopop.com.br** (ponte p/ Fernando) ·
contato@popcommunication.com.br. Cc padrão: Brenno + André + admin.

## D · No Google Drive (NÃO copiar p/ este repo — material de terceiro)

- **CAT.MART-GERAL.pdf** (18/08) — catálogo geral MART
- **GUIA-DE-COMPRAS-MART.pdf** (01/09 — recente) — guia de compras MART
- **ROTEIRO_REUNIAO_POPCOM_2026-08-19** (Google Doc, 2 cópias) — roteiro
  da reunião de 19/08

→ São OS assets de produto para o inspetor/loja (fase MART). Uso interno
de demo ok; publicação de imagem de produto = gate (direitos do fornecedor).

## E · Roteiro de busca para o Codex no Mac

```bash
mdfind -onlyin "/Volumes/Seagate Portable Drive" "Fernando OR Camargo OR MART OR PopCom OR 'Pop Casa'" | head -40
mdfind "kMDItemFSName == '*MART*'cd || kMDItemFSName == '*camargo*'cd || kMDItemFSName == '*popcom*'cd" | grep -v Library | head -40
ls ~/Downloads ~/Desktop 2>/dev/null | grep -iE "mart|camargo|pop|fernando"
```
Procurar especialmente: fotos de produto Camargo (catálogo 2D), gravação/
transcrição da reunião Zoom (autorização expirou — só com nova autorização
do André), e os PDFs da MART baixados localmente.

## F · O que AINDA FALTA para a entrega final

1. **Lista oficial de marcas-cliente do Fernando** — NÃO localizada em
   nenhuma fonte → área "marcas parceiras" do B2C permanece placeholder.
2. **Fotos de produto Camargo & Pinheiro** — não localizadas no Drive;
   procurar no Mac (§E) ou pedir à Tina.
3. **Transcrição da reunião Zoom** — não confirmada; não inventar o que
   foi dito nela.

## G · Regras de gate desta entrega (Maple OS §3)

Marca-cliente não vira "parceira" sem a lista oficial · imagem de produto
de fornecedor não se publica sem direito · nada de preço/claim inventado ·
nenhuma marca de outra frente (Ali/Prince/Climbex-CTA) entra em peça POP ·
envio de qualquer coisa à Tina/Fernando = gate do André.
