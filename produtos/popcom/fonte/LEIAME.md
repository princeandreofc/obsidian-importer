# Fonte da Pop Campanhas

O `cerebro-campanhas.html` publicado é **gerado**, não editado à mão: ele traz
o three.js e o motion embutidos (a política de segurança da página publicada
recusa script de CDN), o que o deixa com cerca de 700 KB.

Edite as partes e monte de novo:

| Arquivo | O que é |
|---|---|
| `parte-html.txt` | marcação e estilos da página |
| `parte-js.txt` | campanha, lâmina, planilhas, pedidos |
| `palco.js` | cena 3D, órbita, dolly zoom, saída em imagem e vídeo |
| `palco.css` | estilos do palco e do dock |
| `montar.py` | junta tudo e embute as bibliotecas |

```bash
curl -sSL -o three.min.js https://unpkg.com/three@0.149.0/build/three.min.js
curl -sSL -o motion.js    https://unpkg.com/motion@11.11.17/dist/motion.js
python3 montar.py
```

O `montar.py` falha alto se qualquer ponto de junção mudar de forma — é
proposital, para não gerar uma página silenciosamente quebrada.
