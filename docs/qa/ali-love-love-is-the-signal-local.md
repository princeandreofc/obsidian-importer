# LOVE IS THE SIGNAL / THE SPIRAL — LOCAL BUILD READY

Data: 24/08/2026 · Executor: Fable 5 · Regime: implementação isolada +
build local + QA local + relatório — **nenhuma ação remota**.

## Repo real

- canonical: `princeandreofc/obsidian-importer` · `/home/user/obsidian-importer`
- branch/worktree: `claude/organizar-computador-26sev2` (linha isolada; PR #4 aberto, não tocado nesta rodada)
- base commit: `023c6a60479fc4f089d2f3aaa357c2f2110e2d1c`
- framework and versions: **sem framework** — HTML único autocontido
  (`produtos/alilove/cinema5d/cinema5d-src.html`) + Three.js r149 UMD embutido;
  build por `ferramentas/monta.py` (Python 3); QA por Playwright/Chromium
  headless (SwiftShader). O plano-template presumia Next/React/Vitest; a
  Task 1 registrou a realidade e a intenção de cada task foi executada nesta
  arquitetura (decisão documentada em `docs/audits/ali-love-repo-baseline.md`).

## Baseline

- initial build: `023c6a6` montava e passava as duas suítes (registro na auditoria).
- pre-existing failures: nenhuma nas suítes locais; limitações de sandbox
  (hot-links e Spotify embed não carregam em preview de artifact) não são defeitos.
- real alilove.world pipeline: **não é publicado deste repo**; o repo de produção
  não está acessível nesta sessão e nada aqui toca o site no ar.

## Delivered

- campaign shell: hierarquia LOVE IS THE SIGNAL aplicada ao espelho existente —
  estrutura das 11 fases do site preservada intacta; adições apenas.
- Resonance Rose: 3D procedural determinística (seed 528; 12 pétalas fundidas
  em 1 draw call, 6 eixos, espiral da memória, 2 órbitas contrarrotantes,
  24 partículas com pontes, núcleo âmbar) no céu do hero enquadrada pela pose
  real da câmera; emblema íntimo diante da câmera no Listen e no finale;
  SVG 2D acessível (`role="img"`) no player e no fallback sem-WebGL.
- 528 framing: tokens SIGNAL_528 (528 ms/1056 ms/5280 ms) em CSS e na respiração
  da Rose; aviso cultural/composicional publicado no EPK; zero alegação médica.
- Spiral integration: rosa dirigida por fase (`ROSA_PROEM`) + sinal de áudio;
  nenhuma segunda engine, nenhum segundo loop.
- game: RESONANCE SESSION — overlay canvas 2D, reducer puro determinístico
  (janelas 0–5/18/26/30 s; unstable→listening→resonant→remembered; sem game
  over), clusters com pontes, teclado + toque + ponteiro, pausa com aba oculta,
  SAVE IMAGE + SAVE LOOP (visual-only), "THE ROOM REMEMBERS".
- VJ: STUDIO 2.0 — 5 bancos de cena (ORBIT/GROOVE/GARDEN/RITUAL/DAY SIGNAL,
  teclas a–e) ancorando deriva+tintura+fx, 4 macros ENERGY/DEPTH/MEMORY/
  CONNECTION presos a [0,1], upload em gaveta avançada, contrato compartilhado
  em `docs/production/vj-control-map.json`.
- biography/archive: ledger BIOGRAFIA com três camadas éticas e gate — tudo
  `enabled:false` até verificação; nada não verificado renderiza.
- recording: REC do palco visual-only por construção; trilha só entra com
  master `downloadableCaptureAudio=true` (gate implementado); sessão idem.
- mobile/accessibility: sem overflow em 390 px; alvos ≥44 px; aria em controles
  novos; `prefers-reduced-motion` → rosa estática, sem Ken Burns, sem giro de
  portal, sessão completável.
- **SIGNAL PLAYER + MusicAssetRights (fail-closed)**: registro MASTERS vazio →
  nada toca; `podeTocar`/`podeGravarAudio` exigem `cleared-production` +
  webPlayback + interactiveSync + visualizerUse (+ captura p/ export);
  `sinal={low,mid,high,energy,positionMs,durationMs,playing}` dirige tudo;
  **microfone removido** (a versão antiga era captação de Spotify — proibida);
  Spotify permanece o player oficial, independente e nunca fonte de motion;
  manifesto RELEASE embargoed → "NOW TRANSMITTING — NEW TRANSMISSION" sem
  título/data inventados; `validaConteudoPublico` bloqueia produção não liberada.

## QA evidence

- unit: `node --check` nas duas builds — OK.
- E2E: `teste-jornada.js` e `teste-vj.js` (final) — **todas as sondas verdes,
  ERRS nenhum** nas duas; inclui GATE {limpo:true, bloqueia:true} e REDUCER
  {listening→remembered, sem game over}.
- build: `monta.py` — jornada 2.996.738 B · vj 2.996.743 B (autocontidos).
- desktop/mobile: 1440×900 + 390×844 (touch) — sem overflow (máx. 390), botão
  sessão 202×44, banco 47×44.
- reduced motion: probe dedicado — boot ok, rosa presente, sessão progride, 0 erros.
- audio/microphone: áudio só após gesto (upload/master); mic inexistente no
  build; jam local mediu grave 0,35 e `sinal.playing=true`.
- REC: download `the-spiral-vj-loop.webm` confirmado na suíte.
- console: zero erros não filtrados nas três execuções.

## Performance

- FPS p50/p10: não medível com honestidade neste container (SwiftShader =
  GL por software); em GPU real, pendente de medição na próxima rodada.
- DPR: governador ativo — <32 fps por 3 s → pixelRatio 1 + vagalumes off.
- draw calls: Rose adiciona ~9 no céu (pétalas fundidas = 1 call) + 5 no
  emblema de câmera; sem novas luzes, sem pós-processamento novo.
- textures/geometries: novas texturas = 2 sprites radiais 64², texturas de
  cena inalteradas; sem crescimento por frame (pontes pré-computadas).
- Three chunk: r149 UMD embutido (inalterado).
- interactive first frame: HTML/DOM visível antes do 3D (estrutura preservada).

## Content and rights

- approved-preview: 6 capas (uso interno do espelho), 2 pôsteres oficiais
  hot-linkados do site do artista; entradas BIOGRAFIA public-catalog (disabled).
- cleared-production: **nenhum** — nenhum master, nenhuma foto, nenhum vídeo.
- withheld: memórias precisando verificação do artista (disabled).
- production gate result: `__gate()` limpo passa (nada não-liberado exposto);
  memória habilitada sem clearance → **bloqueia** (`memory:x`); masters não
  liberados bloqueariam. Scan de copy proibida: limpo (sem "healing/therapeutic/
  coming soon/título inventado"). `Cosmic Rave` permanece apenas como nome do
  filme/arquivo existente, nunca como título de álbum.

## Scope

- remote actions performed: **none** (sem push, PR, deploy, alias, Vercel
  settings, artifact republish).
- deploy performed: **no**.

## Pendências que dependem do dono

1. Key visual `resonance-rose-key-visual-v1.png` ainda não recebido → Task 12
   (asset + sidecar de proveniência) pendente; slot `approved-preview` pronto.
2. Masters de áudio com autorização documentada → primeiro registro no MASTERS
   liga o player (fail-closed até lá).
3. Trabalho está **apenas local** — container é efêmero; quando quiser
   persistir/ver no preview, autorize o push.

## Next approval gate

Preview deployment, publication, production configuration and media clearance
require explicit approval from André.
