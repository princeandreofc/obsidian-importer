# Pipeline de ativos — Resonance Rose / LOVE IS THE SIGNAL (24/08/2026)

Contrato de intercâmbio entre o runtime web (The Spiral, WebGL2) e a produção
offline/ao vivo. Ferramentas: **Cinema 4D + Redshift** (autoria 3D principal),
**Houdini** (apenas especialista: superfícies tipo-Faraday, tinta, fluidos),
**TouchDesigner** (look-dev em tempo real + MIDI/OSC), **Resolume Arena**
(playback/mapping de show), **DaVinci Resolve** (conform, cor, masters).

## Topologia canônica da Rose (fonte: runtime, seed 528)

- 12 pétalas harmônicas · 6 eixos cristalinos · espiral interna da memória
- 2 campos orbitais contrarrotantes · 24 partículas humanas com pontes
- núcleo quente (Ritual Amber #F4B65A) em luz fria (Signal Cyan #51D9E8)
- assimetria leve (±0,07 rad por pétala) — viva, nunca corporativa
- respiração: ciclo de 5.280 ms; transições: 528 ms (tokens SIGNAL_528)

## Cor

- Trabalho offline em **ACEScg**; entrega web com transform explícito **sRGB**.
- Paleta: Vinyl Black #070709 · Midnight Indigo #10122E · Signal Cyan #51D9E8 ·
  Ink Crimson #D83B48 · Ritual Amber #F4B65A · Paper Pearl #F2EEE7 ·
  Day Signal Orange #F06A2A.

## Formatos

| Uso | Formato |
| --- | --- |
| Geometria web | GLB/glTF (Draco só se o custo de decode compensar) |
| Texturas web | KTX2/Basis; masters offline EXR/PNG/TIFF |
| Animação | transforms/morphs baked, FPS documentado por arquivo |
| Masters de filme | ProRes 4444 (alpha) / 422 HQ 4K |
| Cópias de show | DXV3 (Resolume) + fallback HAP/ProRes |
| Derivados web | AV1/WebM + fallback H.264 MP4 |
| Loops alpha | modo straight/premultiplied documentado por ativo |

## Regras

1. Todo arquivo exportado recebe sidecar de proveniência (JSON: origem, direitos,
   status `concept|approved-preview|cleared-production|withheld`, SHA-256, aprovador).
2. Nenhum ativo nasce `cleared-production` — a promoção é ato editorial explícito.
3. Nada de imagens de Emoto reproduzidas nem alegações científicas/terapêuticas
   sobre 528 Hz; referência de física real: ondas de Faraday (tier A) apenas como
   referência de geometria, rotulada `physics-reference`.
4. Loop handles de 528 ms nas pontas; nomes: `alilove-lits-<peça>-<ratio>-<dur>-vNN`.
5. Checksums no manifesto de entrega; nada é publicado a partir deste repo.
