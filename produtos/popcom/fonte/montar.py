#!/usr/bin/env python3
"""Monta a Pop Campanhas v3: v2 + palco 3D + bibliotecas embutidas."""
import pathlib, re, sys

d = pathlib.Path(__file__).parent
ler = lambda n: (d / n).read_text(encoding="utf-8")

html = ler("parte-html.txt")
js   = ler("parte-js.txt")
css_palco = ler("palco.css")
js_palco  = ler("palco.js")
three = ler("three.min.js")
motion = ler("motion.js")

# ── 1. estilos do palco ───────────────────────────────────────────
html = html.replace("</style>", css_palco + "\n</style>", 1)

# ── 2. aba Palco, entre Campanhas e Pedidos ───────────────────────
aba_nova = ('<button class="tab" role="tab" aria-selected="false" data-tab="palco">Palco</button>\n    '
            '<button class="tab" role="tab" aria-selected="false" data-tab="ped">')
assert '<button class="tab" role="tab" aria-selected="false" data-tab="ped">' in html
html = html.replace('<button class="tab" role="tab" aria-selected="false" data-tab="ped">',
                    aba_nova, 1)

# ── 3. painel do palco, antes do painel de pedidos ────────────────
PANE = '''
  <!-- ══════════════ PALCO ══════════════ -->
  <artifact-local>
  <div id="pane-palco" hidden>
    <div class="palco-wrap">
      <canvas id="palco" aria-label="Palco tridimensional da campanha"></canvas>
      <span class="palco-sel" id="palco-sel">0 produtos</span>
      <span class="rec-dot" id="rec">gravando</span>
      <div class="palco-vazio" id="palco-vazio">
        Escolha produtos na aba <strong>Campanha</strong><br>para montá-los no palco.
      </div>

      <div class="dock" role="toolbar" aria-label="Controles do palco">
        <button class="dock-btn" id="d-orbita" type="button" data-rot="Pausar órbita" aria-label="Pausar órbita">
          <svg viewBox="0 0 24 24"><ellipse cx="12" cy="12" rx="10" ry="4.5"/><circle cx="12" cy="12" r="3"/></svg>
        </button>
        <button class="dock-btn" id="d-dolly" type="button" data-rot="Dolly zoom" aria-label="Dolly zoom">
          <svg viewBox="0 0 24 24"><path d="M3 8V4h4M21 8V4h-4M3 16v4h4M21 16v4h-4"/><circle cx="12" cy="12" r="3.4"/></svg>
        </button>
        <span class="dock-sep"></span>
        <button class="dock-btn" id="d-png" type="button" data-rot="Baixar imagem" aria-label="Baixar imagem">
          <svg viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="14" rx="2.5"/><circle cx="8.5" cy="10" r="1.6"/><path d="M21 16l-5.5-5L7 19"/></svg>
        </button>
        <button class="dock-btn" id="d-video" type="button" data-rot="Gravar vídeo" aria-label="Gravar vídeo">
          <svg viewBox="0 0 24 24"><rect x="2.5" y="6" width="13" height="12" rx="2.5"/><path d="M15.5 10.5L21.5 7v10l-6-3.5z"/></svg>
        </button>
        <span class="dock-sep"></span>
        <button class="dock-btn" id="d-xr" type="button" data-rot="Modo imersivo" aria-label="Modo imersivo">
          <svg viewBox="0 0 24 24"><rect x="2" y="7.5" width="20" height="9" rx="4.5"/><path d="M9.6 16.5l1.4-2.4h2l1.4 2.4"/></svg>
        </button>
      </div>
    </div>
    <p class="note" style="margin:14px 0 0">
      A imagem sai como PNG do quadro atual. O vídeo grava <strong>uma volta completa</strong>
      da órbita em WebM, direto do palco — sem codificação externa.
    </p>
  </div>
  </artifact-local>
'''
marca_ped = "  <!-- ══════════════ PEDIDOS ══════════════ -->"
assert marca_ped in html
html = html.replace(marca_ped, PANE + "\n" + marca_ped, 1)

# ── 4. troca de abas: inclui o palco, inicia sob demanda ──────────
antigo = '''document.querySelectorAll(".tab").forEach(t=>t.addEventListener("click",()=>{
  document.querySelectorAll(".tab").forEach(x=>x.setAttribute("aria-selected",String(x===t)));
  document.getElementById("pane-camp").hidden = t.dataset.tab!=="camp";
  document.getElementById("pane-ped").hidden  = t.dataset.tab!=="ped";
}));'''
novo = '''document.querySelectorAll(".tab").forEach(t=>t.addEventListener("click",()=>{
  document.querySelectorAll(".tab").forEach(x=>x.setAttribute("aria-selected",String(x===t)));
  const aba=t.dataset.tab;
  document.getElementById("pane-camp").hidden  = aba!=="camp";
  document.getElementById("pane-palco").hidden = aba!=="palco";
  document.getElementById("pane-ped").hidden   = aba!=="ped";
  if(aba==="palco"){
    // WebGL só é ligado quando o palco é visto pela primeira vez
    if(!Palco.ativo()) { Palco.iniciar(); }
    Palco.dimensionar();
    palcoAtualizar();
  }
  animarPainel(document.getElementById("pane-"+aba));
}));'''
assert antigo in js
js = js.replace(antigo, novo, 1)

# ── 5. seleção de produtos remonta o palco ────────────────────────
# Nada de `typeof Palco` aqui: Palco é const e, antes de inicializado,
# typeof sobre ele LANÇA (zona morta temporal) em vez de devolver "undefined".
# O boot foi movido para depois da definição, então basta chamar direto.
alvo = '  document.getElementById("c-conta").textContent=escolhidos.size;\n  pintarLamina();'
assert alvo in js
js = js.replace(alvo, alvo + '\n  if(Palco.ativo()) palcoAtualizar();', 1)

# ── 6. o boot sai do fim do v2 e vai para depois do palco ─────────
boot = "pintarCatalogo();\ncontarFila();"
assert boot in js
js = js.replace(boot, "", 1)

# ── 7. junta tudo ─────────────────────────────────────────────────
saida = (html
    + "<script>/* three.js r149 — MIT */\n" + three + "\n</script>\n"
    + "<script>/* motion 11 — MIT */\n" + motion + "\n</script>\n"
    + "<script>\n" + js + "\n" + js_palco
    + "\n\n/* boot, com tudo já definido */\npintarCatalogo();\ncontarFila();\n</script>\n")

(d / "cerebro-campanhas.html").write_text(saida, encoding="utf-8")
kb = len(saida.encode()) / 1024
print(f"montado: {kb:.0f} KB")
