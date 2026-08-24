# Ferramentas locais — The Spiral / LOVE IS THE SIGNAL

Snapshot das ferramentas de build e QA (rodam em `/tmp/claude-0/` por padrão;
os caminhos internos apontam para lá — copie para lá ou ajuste as constantes).

- `monta.py` — monta `the-spiral.html` (jornada) e `the-spiral-vj.html` (vj) a
  partir de `cinema5d-src.html`: injeta Three.js r149 UMD, MODO, VJURL e as
  capas de `capas/*.jpg` como data-URIs; extrai o JS para `node --check`.
- `teste-jornada.js` — suíte Playwright da jornada (Chromium headless +
  SwiftShader): boot, gate de direitos, reducer da sessão, CRT, SIGNAL PLAYER
  fail-closed, sleeves, mundos, aviso 528, menu, Resonance Session, mobile 390px.
- `teste-vj.js` — suíte do VJ Studio 2.0: bancos de cena, macros com clamp,
  deriva ancorada, FX, jam local (upload → sinal), REC WebM, mobile.
- `probe-hero.js` / `probe-reduz.js` — screenshots rápidos do hero e smoke de
  `prefers-reduced-motion`.

Requisitos: `playwright` global (`npm root -g`) com Chromium; flags SwiftShader
já embutidas; hot-links externos são abortados por rota nos testes (espelha o
comportamento de sandbox).

Rodar: `python3 monta.py && node --check app-jor.js && node teste-jornada.js && node teste-vj.js`
