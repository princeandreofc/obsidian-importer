# HANDOFF — FRENTE CHOCOLLATE (Claude Code no terminal, Mac com Seagate)

**Urgência real: o dono da Bem Bolado está esperando o E-MAIL com a proposta.**
Você está no Mac — você TEM acesso ao Seagate. A nuvem não tinha; por isso
esta frente passa para você. Execute na ordem, sem perguntar o que já está
decidido aqui.

## O padrão de entrega (não é figura de linguagem)

O nível exigido é o do **material completo do Ali Love** já entregue:
`produtos/alilove/cinema5d/` (fonte `cinema5d-src.html`, build
`ferramentas/monta.py`, testes Playwright, HANDOFF.md da frente). Antes de
produzir qualquer peça, abra `cinema5d-src.html` no navegador e olhe o
acabamento — ESSE é o régua: editorial escuro, tipografia grande, grão,
movimento, nada de card genérico. A skill `site-imersivo-editorial`
(template da casa) é o caminho para o EPK.

## Regras fixas desta frente

1. Nome do artista: **CHOCOLLATE** — dois L, sempre. ("chocolate" minúsculo
   = o produto/cacau, esse fica.)
2. **NENHUM valor de cota em NENHUMA peça.** O André ainda vai definir
   valores com o dono da Bem Bolado — os documentos já estão desenhados
   para falar de alcance, benefícios e custo de mercado sem citar preço.
   Não acrescente número de cota nem "a partir de".
3. Enviar e-mail/mensagem = **GATE**: rascunho sim, envio só o André.
4. Não inventar fato, data, crédito ou percurso do artista. Biografia só
   com o que estiver no material do Seagate. Sustentabilidade só por
   prática documentada. **Ali Love não aparece em peça da Bem Bolado**
   ("padrão Ali Love" é régua interna, não argumento de venda).
5. Originais do Seagate: **copiar, nunca mover/editar no lugar**.
6. Este repo é o de trabalho; material bruto de artista (fotos/vídeos/áudio)
   NÃO entra no git — fica em pasta local fora do repo + backup no Drive
   (pasta `CHOCOLLATE_LANCAMENTO`, compartilhar com admin@climbexglobal.com,
   que é o e-mail que a nuvem opera).

## O que JÁ existe nesta branch (`claude/organizar-computador-26sev2`)

- `produtos/chocolate/dossie-src.html` — dossiê de patrocínio **refeito em
  9 páginas A4** (capa com fruto em corte, momento de mercado com fontes,
  parceria, brand board "terra, polpa e ouro", campanha T−28→T+30,
  benefícios Master, linha premium com mockup vetorial da embalagem,
  custo de mercado, próximo passo). Falta: fotos reais + re-render do PDF.
- `produtos/chocolate/oficio-src.html` — Ofício nº 001/2026 de pedido de
  patrocínio, com placeholders `[cidade]`, `[dia/mês]`,
  `[nome do responsável]` e `[nome civil do artista]`.
- `produtos/chocolate/cacau-bembolado.html` — landing do pitch (padrão
  site-imersivo).
- Os PDFs antigos no repo (`DOSSIE-CHOCOLATE-X-BEMBOLADO.pdf`,
  `OFICIO-PATROCINIO-001-2026.pdf`) estão **desatualizados** (grafia e
  design antigos): apague e re-gere.
- Claude Doc "Chocollate × Bem Bolado — lançamento e patrocínio"
  (claude.ai/artifact/CqzhtGkMMnzqNEZAKFyQoC): plano de negócio, roteiro da
  ligação, **guia CD Baby passo a passo**, campanha completa, checklist do
  material do Seagate, one-pager, riscos. Use como fonte de texto.

## FAZER, na ordem

**1. Seagate — localizar e inventariar o material do CHOCOLLATE.**
Monte em `/Volumes/` e procure (ls + mdfind/find por "chocollate",
"chocolate", nome civil se souber):
fotos, vídeos, capas/artes, biografia, letras, bounces/músicas do álbum.
Escreva `produtos/chocolate/INVENTARIO-SEAGATE.md` com caminho, tipo e
estado de cada item (mesmo molde do inventário do Fernando Bento em
`produtos/popcasa/`). Copie o que for usar para uma pasta de trabalho
LOCAL fora do repo e suba backup no Drive `CHOCOLLATE_LANCAMENTO`.

**2. EPK do Chocollate** — single-file HTML pela skill
`site-imersivo-editorial`, preset Cacau Bahia (tokens no dossiê:
ink #1A0F08 · paper #F4E9D6 · clay #A6552D · rose #C96F4A · moss #5E7A52 ·
gold #D9A441), nível do `cinema5d-src.html`: bio real (do material, nada
inventado), fotos, discografia/álbum, vídeos, contato. Salvar como
`produtos/chocolate/epk-chocollate-src.html` + PDF.

**3. Dossiê v2 com imagem real** — em `dossie-src.html`, trocar as células
do brand board (página 4, bloco `.mood`) e a capa por fotos reais do
Seagate quando houver; manter o resto. Re-gerar PDF A4:
Playwright/Chrome headless, `page.pdf({format:'A4', printBackground:true,
margin:0})` após `networkidle` (+ ~1,2 s para fontes). Nome:
`DOSSIE-CHOCOLLATE-X-BEMBOLADO.pdf`. Idem `oficio-src.html` →
`OFICIO-PATROCINIO-001-2026.pdf` (preencher cidade/data; os dois nomes em
placeholder, perguntar ao André se não estiverem no material).

**4. Kit de lançamento** (textos prontos no Claude Doc):
- Capas de pré-save nas proporções 1:1, 9:16 e 16:9 com a arte da campanha.
- Posts do cronograma T−28 → T+30 (legendas no doc).
- `produtos/chocolate/GUIA-CDBABY.md` — exportar o guia do doc para o repo.

**5. RASCUNHO do e-mail ao dono da Bem Bolado** (GATE — não enviar):
corpo curto em PT-BR (3 parágrafos: a campanha "O Cacau é Nosso", o que a
marca leva como Master, próximo passo = reunião de 30 min), anexos =
dossiê + ofício. Deixar como rascunho no Gmail admin@ ou como
`produtos/chocolate/EMAIL-DONO-BEMBOLADO.md` para o André colar. Valores
de cota: NÃO mencionar — "condições comerciais em documento próprio".

**6. Fim de sessão:** commit + push nesta branch + uma linha com o hash
(ou o erro exato). O PR #8 já está aberto; o push atualiza ele.

## O que fica com o André (lembrar, não executar)

- Definir os valores das cotas com o dono (nenhum doc cita valor).
- Apertar ENVIAR no e-mail.
- Nome civil do artista + nome do responsável da Bem Bolado para o ofício.
