# CODEX — EXECUÇÃO ENXUTA (nova workspace · 06/09/2026)

Primeira mensagem sugerida ao Codex: *"Lê AGENTS.md, MAPLE-OS.md §3 e
`produtos/holding/CODEX-EXECUCAO-ENXUTA.md`; executa as etapas na ordem,
com commit+push ao fim de CADA etapa."*

## Regra nº 1 — crédito é o recurso escasso

- **Reconhecimento JÁ FOI FEITO. Não repita.** Zero auditoria, zero
  varredura de repo, zero releitura de QA. A tabela de fontes abaixo diz
  onde está cada coisa; confie nela.
- **Commit + push ao fim de CADA etapa** (branch `codex/…`). Crédito pode
  acabar no meio: o que foi pushado sobrevive; o resto morre.
- Diff pequeno, 1 build + 1 verificação por entrega, sem loops de
  re-teste. Bloqueio de permissão → reporta o erro exato e PULA para a
  próxima etapa (não contorna, não insiste).
- Se o crédito acabar: a próxima sessão abre este arquivo e retoma da
  primeira etapa sem ✔ no relatório da branch.

## Autorização registrada (gate §3)

Em 06/09/2026, no chat com o Codex, o **André deu APROVADO explícito**
para **produção e deploy** das entregas listadas neste arquivo
("agora tá autorizado toda produção e deploy… entregáveis no ar sem
preview"). Este parágrafo é o registro exigido pelo MAPLE-OS.md §3; fora
deste escopo, o AGENTS.md continua valendo por inteiro. **Continuam sendo
gate mesmo agora**: enviar e-mail/mensagem a quem quer que seja ·
dinheiro/assinatura · DNS/domínio · `alilove.world` (intocável) · deletar
ou sobrescrever originais · merge em `master` (quem merge é o André, via
PR).

## Fontes (ler só a da etapa em curso)

| Preciso de… | Está em… |
| --- | --- |
| Contrato e gate | `AGENTS.md` (auto) · `MAPLE-OS.md` §3 |
| Tudo do Fernando Bento | `produtos/popcasa/INVENTARIO-FERNANDO-BENTO.md` |
| Alvos de master + catálogo | `produtos/princeandre/library-master.md` |
| Molde de página da casa | `produtos/princeandre/landing-999.html` |
| Detalhe fino dos pedidos | `SUPER_HANDOFF_CODEX_CLI_MAPLE_OS*.md` em `~/Downloads` do Mac (não estão no repo) |

**Relatório da rodada anterior** (`codex/maple-os-handoff-20260906`,
`47c9c9e`): **JÁ TRATADO** — as propostas A/B/C/F foram aplicadas no
PR #6 pela retaguarda em 06/09. Não reaplicar, não redescobrir; a branch
pode ser encerrada depois que o André mergear o PR #6.

## ETAPA 0 · Sincronizar (2 min)

`git fetch origin master` → branch nova `codex/entrega-<data>` a partir de
`origin/master`. Não tocar em branches `claude/*` nem nas cópias antigas
do Mac (Seagate/CerebroMestre) — se estiverem em outra branch, deixe como
estão.

## ETAPA 1 · Enterprise Hub Fernando Bento — NO AR

1. Página single-file `produtos/popcasa/hub/fernando-hub.html` no molde
   da casa (referência de caliber: `landing-999.html`), montando o hub
   com o que JÁ EXISTE: experiência + loja + catálogo Studio L + 4 marcas
   próprias (INVENTÁRIO §A). Assets locais do Mac: roteiro de busca no
   §E do inventário.
2. **Placeholders honestos** onde falta material (§F): lista oficial de
   marcas-cliente (não inventar "parceiras"), fotos Camargo. **Nenhum
   material de terceiro (PDFs MART, fotos de fornecedor) entra neste
   repo público — nunca.**
3. Deploy Vercel (team `admin-72622007s-projects`) em **projeto novo**
   (ex.: `fernando-hub`); não usar `andre-corporate`/`alilove` (projetos
   quebrados). Autorizado a ir direto a produção (registro acima).
4. Entregável: URL no ar + hash. **Enviar o link à Tina/Fernando = gate
   do André.**

## ETAPA 2 · Cloudflare deployment-control + Agents SDK

Pastas no Mac: `~/Documents/Codex/cloudflare-deployment-control`
(wrangler.jsonc, package.json, CLAUDE.md) ·
`~/CerebroMestre/Projects/ecossistema-cloudflare` ·
skill `~/.agents/skills/agents-sdk/SKILL.md`.

1. Atualizar o deployment-control conforme o SUPER_HANDOFF (ler 1×) e
   ligar os dois projetos ao Maple OS: CLAUDE.md/AGENTS.md deles passam a
   apontar para o MAPLE-OS.md deste repo (gate incluído).
2. Alinhar a skill agents-sdk ao contrato (gate §3 vale para agentes que
   ela criar).
3. Deploy dos workers autorizado (registro acima) — **exceto** qualquer
   rota/DNS novo em domínio da holding (gate).
4. Entregável: lista curta do que mudou + URLs/hashes. Commit em cada
   repo local; o que for documento de contrato, espelhar aqui em
   `produtos/holding/`.

## ETAPA 3 · Master do álbum (em CÓPIAS, sempre)

1. Localizar as faixas no Mac (Logic/bounces). **Copiar para pasta de
   trabalho; originais e sessões de Logic intocáveis.**
2. Master por faixa: **−14 LUFS integrado · true peak ≤ −1 dBTP**
   (pipeline em `library-master.md`) + melhorar beats onde o André pediu
   — sem regravar identidade da faixa.
3. Registrar cada master no catálogo do `library-master.md` com o
   **título real do arquivo** (não inventar título/crédito; "gravada c/
   Ali?" fica `a confirmar` — o André não lembra quais são as 5, e isso
   NÃO bloqueia o master).
4. **Master ≠ publicação**: nenhuma faixa entra em site/palco/streaming
   sem direitos documentados (`cleared-production`, fail-closed no
   player) e sem o André. Falta de música nunca trava as etapas 1–2.
5. Entregável: tabela preenchida + caminho das cópias masterizadas.

## Fim de cada etapa (obrigatório)

`git add` → commit descritivo → `git push -u origin codex/entrega-<data>`
→ UMA linha ao André: etapa ✔ + hash (ou o erro exato). No fim de tudo:
abrir PR para `master` — quem merge é o André.
