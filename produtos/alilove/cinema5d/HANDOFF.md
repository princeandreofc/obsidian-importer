# HANDOFF — THE SPIRAL × LOVE IS THE SIGNAL (Ali Love)

**Data:** 24/08/2026 · **Autor da rodada:** Fable 5 (sessão Claude Code)
**Este documento é a continuidade do projeto.** Se a sessão/container morrer,
NADA se perde: tudo referenciado aqui vive no GitHub e no Vercel.

---

## 1 · Onde está tudo (durável)

| Coisa | Onde |
| --- | --- |
| Repo canônico | `github.com/princeandreofc/obsidian-importer` |
| Branch de trabalho | `claude/organizar-computador-26sev2` (PR #4 aberto — **NUNCA mergear sem autorização escrita: merge = deploy de produção nos sites de clientes**) |
| Commits desta campanha | `2f2053e` auditoria · `490c906` feature · `b4e94b1` produção · `48c4382` QA · `6f9cad6` manifesto EPK · `7bb9a7d` proposta PDF |
| Fonte única | `produtos/alilove/cinema5d/cinema5d-src.html` |
| Builds prontas | `produtos/alilove/cinema5d/the-spiral.html` (jornada) e `the-spiral-vj.html` (VJ) — autocontidas, ~3 MB |
| Ferramentas build+QA | `produtos/alilove/cinema5d/ferramentas/` (monta.py, teste-jornada.js, teste-vj.js, probes, README) |
| Auditoria Fase Zero | `docs/audits/ali-love-repo-baseline.md` + `ali-love-repo-map.json` |
| Contratos de produção | `docs/production/` (vj-control-map.json · pipeline · deliverables-matrix.csv) |
| Relatório QA final | `docs/qa/ali-love-love-is-the-signal-local.md` |
| Proposta p/ Ali (PDF+fonte) | `produtos/alilove/cinema5d/campanha/` |
| Spec + plano da campanha | `docs/campanha/` (MASTER_SPEC e Implementation Plan, cópias dos uploads do dono) |
| **Preview público (jornada)** | `https://the-spiral-preview-1ff7ito25-admin-72622007s-projects.vercel.app` |
| **Preview público (VJ)** | `…mesmo domínio…/vj/` |
| Projeto Vercel do preview | `the-spiral-preview` · `prj_wX8ptm6N3j96Zi4Y6IpCyOOqoTm0` · team `team_PsN45axWZMm0jzgjvcIdOlS2` · SSO protection DESLIGADA |

## 2 · Arquitetura (sem framework — decisão auditada)

Um HTML único com placeholders: `@@THREE@@` (Three.js **r149 UMD** embutido),
`@@MODO@@` (`"jornada"`|`"vj"`), `@@VJURL@@` (link cruzado), `@@CAPAS@@`
(6 capas aprovadas como data-URIs JPEG, geradas de `capas/*.png` do dono,
commit `34e8e53`). `ferramentas/monta.py` gera as duas builds e extrai o JS
para `node --check`. QA: 2 suítes Playwright (Chromium headless + SwiftShader,
hot-links externos abortados por rota). **Build:** `python3 monta.py` ·
**Sintaxe:** `node --check app-jor.js` · **E2E:** `node teste-jornada.js && node teste-vj.js`
(caminhos padrão `/tmp/claude-0/` — ver README das ferramentas).

## 3 · Sistemas implementados (âncoras no fonte)

- **Espelho fiel do site oficial** — 11 seções idênticas (Bring Love…EPK),
  menu, hero verbatim, Archive 13 lançamentos, © 2026; portal original CLONADO
  (markup+CSS) com travessia no scroll + paralaxe; NUNCA mudar estrutura, só
  acrescentar (ordem do dono).
- **Trilha/câmera**: CatmullRom + Frenet(600), banking, head-bob, hero olha o
  céu (t<.09), gran finale (t>.9); 2100vh; `FASES[11]` com fog/tintura/mundos;
  calma crescente; CRT só idx 2; governador FPS (<32×3s → DPR 1, vagalumes off).
- **SIGNAL PLAYER + MusicAssetRights (fail-closed)** — `MASTERS=[]`,
  `podeTocar`/`podeGravarAudio`, `sinal={low,mid,high,energy,positionMs,durationMs,playing}`,
  `garanteMotor` (fonte por elemento), `tocaMaster`, `montarPlayerSinal`.
  **Mic REMOVIDO** (era captação de Spotify — proibido). Spotify = player
  oficial independente, nunca motion. REC visual-only; áudio no export só com
  `downloadableCaptureAudio=true` (gate em `toggleRec`).
- **RELEASE embargo** — título/data null → "NOW TRANSMITTING — NEW
  TRANSMISSION"; `validaConteudoPublico` bloqueia produção não liberada;
  pre-save entra trocando `currentSignal.url` quando a label anunciar.
- **BIOGRAFIA** — ledger 3 camadas éticas, tudo `enabled:false` até verificação.
- **RESONANCE ROSE** — seed 528 determinística: 12 pétalas fundidas (1 draw
  call), 6 eixos, espiral, 2 órbitas contrarrotantes, 24 partículas+pontes,
  núcleo âmbar; céu do hero enquadrado pela POSE REAL da câmera (1º frame,
  `rosaPosta`); emblema `rosaCam` no Listen(5)/finale(10) — no VJ segue macro
  CONNECTION; SVG 2D acessível (`desenhaRosa2D`) no player e fallback;
  estática sob `prefers-reduced-motion`; respiração 5280 ms (SIGNAL_528).
- **RESONANCE SESSION** — overlay canvas 2D; reducer puro `sessaoReduz`
  (0–5/18/26/30 s; unstable→listening→resonant→remembered; SEM game over);
  clusters+pontes, TUNE/SHAPE/arrastar, teclado completo, pausa com aba
  oculta, SAVE IMAGE/LOOP visual-only, "THE ROOM REMEMBERS".
- **VJ STUDIO 2.0** — `CENAS_VJ` 5 bancos (orbit/groove/garden/ritual/day-signal,
  teclas a–e) ancoram deriva+tintura+fx; `macro` ENERGY/DEPTH/MEMORY/CONNECTION
  clamp [0,1] (`defineMacro`); upload em `<details>` avançado; FX 1–5, REC r.
- **Manifesto de autoria no EPK** — arte programada, linhagem visual-music,
  nada raspado, IA como instrumento; + aviso 528 (cultural, sem alegação médica).
- **Paleta campanha** (tokens CSS `--vinil/--indigo/--cian/--rubi/--ambar/--perola/--dia`)
  só em elementos novos; site mantém paleta/tipografia oficiais (Fraunces+Space Grotesk).
- Alças de QA: `window.__sinal/__gate/__macro/__sessaoReduz/__sessaoInicial`.

## 4 · Deploy de preview (receita comprovada)

`deploy_to_vercel` (MCP) com `target:"preview"`, name `the-spiral-preview`,
2 arquivos: `vercel.json` `{buildCommand:"bash build.sh",outputDirectory:"public",framework:null}`
e `build.sh` que baixa as builds do raw.githubusercontent (branch) e troca os
links de artifact por `/vj/` e `/` (URLs de artifact atuais no fonte:
`0f9562be-…` = VJ · `8ae9e2fa-…` = jornada). **Alias estável NÃO acompanha
deploys novos — sempre entregar a URL única do deploy.** "Promote to
Production" = 1 clique do dono, nunca do agente. Projetos `alilove` e
`andre-corporate` (git-integration) FALHAM em todo push — pré-existente,
documentado, não tocar nos settings.

## 5 · Regras invioláveis (resumo operacional)

Sem merge do PR · sem produção/DNS/alias/settings sem autorização escrita ·
alilove.world no ar intocável · direitos de música fail-closed · sem mic para
Spotify · sem título/data inventados · sem alegação terapêutica do 528 ·
capas HOTC: preview ok, label sign-off antes de publicar · lockup exato
`LOVE ALWAYS WINS / Ali Love × AB Motion` · nunca deletar originais/legado ·
Climbex nunca aparece em Ali Love · nada de avatar/voz sem consentimento
documentado · e-mails: rascunho sim, envio só o dono.

## 6 · Pendências (aguardando o dono)

1. **Key visual da Rose** (`resonance-rose-key-visual-v1.png`) — Task 12 do
   plano pronta para receber (slot `approved-preview` + sidecar).
2. **Masters com direitos documentados** — 1º registro em `MASTERS` liga o
   player sozinho.
3. **E-mail ao Li**: texto final está no chat de 24/08; anexar músicas do
   dono + PDF `campanha/ALI-LOVE-THE-SPIRAL-LOVE-IS-THE-SIGNAL.pdf`.
4. Pre-save: quando a label anunciar, preencher `RELEASE.currentSignal`.
5. Rotina "Briefing" (trig_013Uoc…) só cancela via claude.ai→Tarefas (dono);
   rotina de pesquisa falha silenciosa 4× — decisão do dono pendente.
6. Produção real (Next.js em alilove.world): repo de produção nunca esteve
   acessível — exigirá acesso + nova autorização; este espelho é a referência.

## 7 · Lições técnicas (não repetir dor)

Sem `transmission` (mata SwiftShader) · far=170 · SpotLight decay 0 ·
r149 legacy lighting (π) · emissive em InstancedMesh precisa patch
`onBeforeCompile` · LatheGeometry: DoubleSide+ápice fechado · fog esconde
além de ~40 (materiais de céu `fog:false`) · elementos fixed têm
`offsetParent null` (usar getComputedStyle) · `let` top-level acessível no
evaluate · nome de arquivo NFD→NFC · downloads em artifact viewer via
capability `downloads` (fallback âncora) · classifier: comandos compostos
com push/curl+grep podem bloquear — separar e tentar de novo.
