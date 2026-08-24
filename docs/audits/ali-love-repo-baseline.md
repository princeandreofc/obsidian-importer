# Auditoria — Fase Zero · LOVE IS THE SIGNAL (24/08/2026)

## Repositório canônico deste trabalho

- **Repo:** `princeandreofc/obsidian-importer` · caminho local `/home/user/obsidian-importer`
- **Branch (worktree isolada de desenvolvimento):** `claude/organizar-computador-26sev2` (PR #4 aberto, não mergeado)
- **Commit-base desta rodada:** `023c6a60479fc4f089d2f3aaa357c2f2110e2d1c`
- **Diretório do produto:** `produtos/alilove/cinema5d/`

## Arquitetura real (difere do template do plano)

O plano de implementação foi escrito como template para um repo Next/React/TypeScript
com Vitest. **A realidade auditada é outra**: o produto THE SPIRAL é um **HTML único
autocontido** (`cinema5d-src.html`), sem framework, sem package.json, sem bundler.

- `cinema5d-src.html` — fonte única. Placeholders: `@@THREE@@` (Three.js r149 UMD
  embutido), `@@MODO@@` ("jornada" | "vj"), `@@VJURL@@` (link cruzado),
  `@@CAPAS@@` (capas aprovadas como data-URIs).
- `monta.py` (ferramenta local em /tmp/claude-0/) — gera `the-spiral.html` (jornada)
  e `the-spiral-vj.html` (VJ Studio), ~2,9 MB cada, e extrai o JS para
  `node --check` (validação de sintaxe).
- QA: duas suítes Playwright locais (`teste-jornada.js`, `teste-vj.js`) com Chromium
  headless/SwiftShader, hot-links externos abortados por rota (espelha o sandbox).

**Decisão registrada:** a intenção de cada task do plano é executada NESTA arquitetura
(domínio `LOVE IS THE SIGNAL` como módulo delimitado dentro do HTML único + docs de
auditoria/produção/QA no repo). Criar `src/features/love-signal/*.tsx` + Vitest aqui
produziria código morto que nada consome — não seria "melhora real". O próprio plano
prevê a descoberta (Task 1) e manda falhar-fechado quando o caminho de integração
presumido não existe.

## Baseline (antes das edições desta rodada)

- Última build íntegra commitada: `023c6a6` (rodada das capas) — as duas builds
  montaram, `node --check` passou, as duas suítes Playwright passaram
  (boot, menu, CRT, mundos, sleeves reais, upload de áudio→graves, REC WebM,
  varredura mobile 390px).
- Falhas pré-existentes: nenhuma nas suítes locais. Limitações conhecidas do
  ambiente (não são defeitos): mídia oficial hot-linkada não carrega no sandbox
  do artifact/preview de teste (onerror a esconde); Spotify embed não abre em
  sandbox — ambos carregam em deploy real.
- `cinema5d-src.html` está com trabalho em andamento não commitado desta campanha
  (registro MASTERS + sinal + medeAudio novos; referências ao mic antigo em remoção).

## Fonte de publicação do alilove.world

O site oficial no ar **não** é publicado deste repositório e o repositório de
produção dele **não** está acessível nesta sessão (o projeto Vercel `alilove`
não pode ser presumido como fonte, por instrução da spec). Todo o trabalho desta
campanha acontece no espelho (The Spiral) dentro deste repo. **Nenhuma edição,
configuração ou deploy toca o site no ar.**

## Direitos e ativos no momento da auditoria

- 6 capas aprovadas (PNG do dono, commit `34e8e53`) — uso interno do espelho: ok.
- 2 pôsteres oficiais hot-linkados do próprio site do artista.
- Key visual `resonance-rose-key-visual-v1.png`: **ainda não recebido** — Task 12
  do plano fica pendente; slot `approved-preview` preparado.
- Masters de áudio: **nenhum** com autorização documentada → registro MusicAssetRights
  nasce vazio (fail-closed).

## Ações remotas nesta rodada

Nenhuma. Regime: implementação isolada + build local + QA local + relatório escrito,
e parar (sem push, PR, deploy, alias, settings, artifact).
