# Implementação imediata — AB Cream interativa

**Data:** 21/08/2026
**Para:** Codex
**Origem:** pesquisa de 21/08 (`pesquisa/achados/2026-08-21.md`), seis contas medidas

---

## 0. Por que esta peça, e não outra

A pesquisa produziu um achado com consequência prática direta: `polanaeem.tech`
publicou um site de café com scroll animado — 4.200 curtidas, 1.100 comentários,
e `DM "COFFEE" to create a website like this for your brand` como funil. Peça
impressionante publicada, cliente chegando no direct.

**É o modelo de funil que falta à holding.** E a AB Cream é a única frente que
consegue executá-lo hoje:

| Frente | Bloqueio |
|---|---|
| Ali Love | acervo real ainda não depositado no bundle |
| Prince Andre | EPK original e imagens de imprensa ausentes |
| AB Motion | case de cliente para o before/after não confirmado |
| Planning | picture lock da interface |
| **AB Cream** | **nenhum — asset existe, direito não se aplica** |

`ab-cream-product-v1.png` já está no bundle. Não há pessoa, não há direito de
imagem, não há terceiro para autorizar. É a peça que dá para fazer agora.

E ela resolve três coisas de uma vez: vira portfólio da AB Motion, vira
implementação de referência das cinco decisões de render que faltam nas outras
frentes, e alimenta o gig e o template da Hotmart.

---

## 1. A trava que define o conteúdo

**AB Cream é estudo demonstrativo de marca, produto e materialidade. Zero
alegação de fórmula, registro, certificação ou eficácia.**

Isso não é limitação — é o que torna a peça interessante para portfólio. As
camadas que se revelam no scroll **não são ingredientes**. São camadas de
**design**: tipografia, paleta, material, luz, movimento.

A narrativa é: *como um sistema visual dá presença a uma ideia.*

Qualquer frase que sugira efeito, composição, aprovação regulatória ou benefício
sai antes do deploy. Se na dúvida, corte.

---

## 2. Estrutura da página

Cinco seções, scroll-driven, uma ideia por seção.

| # | Seção | O que acontece |
|---|---|---|
| 1 | **Escuro** | produto no breu, uma luz entra devagar, revela silhueta |
| 2 | **Matéria** | câmera aproxima; superfície, textura, comportamento da luz |
| 3 | **Sistema** | tipografia, paleta e grid surgem como camada sobre o objeto |
| 4 | **Movimento** | o próprio sistema de motion demonstrado — antes/depois |
| 5 | **Fecho** | lockup, e CTA de contato |

O produto fica **em cena o tempo todo**. O scroll move câmera e luz, não troca
de tela. É isso que separa a peça do `polanaeem.tech` de um site comum: não são
seções empilhadas, é uma cena contínua.

---

## 3. As cinco decisões de render

São elas que separam "exercício" de "foto de produto". Nenhuma é opcional.

### 3.1 Ambiente e tone mapping — maior impacto isolado

```js
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = 1.0;
renderer.outputColorSpace = THREE.SRGBColorSpace;

const pmrem = new THREE.PMREMGenerator(renderer);
pmrem.compileEquirectangularShader();
scene.environment = pmrem.fromScene(new RoomEnvironment(), 0.04).texture;
```

Luz pontual sozinha dá cara de exercício. Ambiente dá cara de produto. É a
mudança de maior efeito por linha escrita.

### 3.2 Pós-processamento

`EffectComposer` com, nesta ordem: `RenderPass` → `UnrealBloomPass` → vinheta →
grão. **Bloom sutil** — se está visível como efeito, está forte demais. Serve
para tirar o aspecto plástico, não para brilhar.

### 3.3 Material

`MeshPhysicalMaterial`, nunca cor chapada:

```js
new THREE.MeshPhysicalMaterial({
  roughness: 0.35, metalness: 0.0,
  clearcoat: 1.0, clearcoatRoughness: 0.15,
  roughnessMap, normalMap,
})
```

O `clearcoat` é o que faz embalagem parecer embalagem.

### 3.4 Movimento

**Lenis** para o scroll, com easing declarado. Revelação escalonada, nunca
simultânea. Lento lê como caro; rápido e linear lê como amador.

```js
const lenis = new Lenis({ duration: 1.2, easing: t => Math.min(1, 1.001 - 2**(-10*t)) });
```

### 3.5 Câmera

Distância focal curta (`fov` 35–40) com profundidade de campo rasa. Câmera
padrão lê como visualizador de CAD.

---

## 4. Restrições técnicas

**Este é site publicado na Vercel, não artifact.** A restrição de CSP que forçou
embutir Three r149 UMD na Pop Campanhas **não se aplica aqui**. Use módulos ES
com `importmap`, o que libera `RoomEnvironment`, `EffectComposer` e os passes —
que não existem no bundle UMD.

```html
<script type="importmap">
{"imports":{"three":"https://unpkg.com/three@0.160.0/build/three.module.js",
"three/addons/":"https://unpkg.com/three@0.160.0/examples/jsm/"}}
</script>
```

Se a entrega exigir arquivo único autossuficiente (padrão `site-imersivo-editorial`),
embuta os addons também — são pequenos. **Decida antes de começar**, porque muda
a estrutura do arquivo.

**Obrigatório em qualquer caso:**

- `prefers-reduced-motion`: cena carrega parada, scroll normal, zero animação
- Tokens de cor em `:root`, redefinidos em `prefers-color-scheme: dark` **e** em
  `[data-theme="dark"]`. Nenhuma cor definida só dentro de media query
- `body` com fundo explícito
- Mobile 390 px sem overflow horizontal; alvos de toque de 44 px
- Zero erro de console
- Degradação: sem WebGL, a página mostra a imagem estática e o texto

**Armadilha registrada:** `typeof X` sobre um `const` ainda não inicializado
**lança** em vez de devolver `"undefined"`. Guarda escrita com `typeof` na zona
morta temporal derruba o script inteiro. Já custou tempo uma vez.

---

## 5. Copy da página

Fecho e CTA, prontos. O resto da página é visual — texto mínimo, por design.

> **Presença antes de promessa.**
>
> A AB Cream é um estudo: marca, produto e materialidade tratados como um
> sistema só. Nenhuma camada aqui é ingrediente. São decisões de tipografia,
> luz, material e movimento — o que faz uma ideia ganhar presença.
>
> `AB CREAM — estudo de sistema visual`
> `AB Motion`

CTA de fecho — modelo do `polanaeem.tech`, adaptado ao registro da casa:

> **Uma página assim para a sua marca.**
> `Falar sobre o projeto →`

Sem preço, sem checkout. Escopo primeiro.

---

## 6. O que sai daqui para as outras frentes

A peça é implementação de referência. Uma vez pronta, as cinco decisões do §3
se propagam:

- **Puressência** — o hub (copy já escrita em `CAMINHO_CODEX_ENTREGA_HOLDING.md`)
  ganha os seis blocos com revelação por progresso de scroll
- **Ali Love** — mesma base de render quando o acervo real for depositado
- **Trajetum** — Lenis e revelação escalonada ao subir para a paridade de 37 páginas

Não refaça a decisão em cada frente. Resolva aqui, replique.

---

## 7. Posicionamento — sai da pesquisa, entra no material comercial

Da análise do `textura.eu`, uma frase que a holding já poderia estar usando e
não usa:

> *"Você não recebe um punhado de componentes soltos. Recebe um sistema sobre o
> qual dá para construir."*

É literalmente o que a skill `site-imersivo-editorial` entrega — tokens
trocáveis, presets, blocos-padrão, regras de movimento. Aplicar no gig e no
template da Hotmart.

Do `insiderforce` (113% de proporção comentário/curtida, o recorde medido), o
princípio de retenção para Climbex e Trajetum: **descrever o método por
completo e reter só o acesso.** Quem mais convence antes de cobrar, mais colhe.

**Não aplicar em Ali Love nem Prince Andre.** Marca de artista vive de desejo, e
pedágio expõe o mecanismo.

---

## 8. Consertos que continuam na fila

Não fazem parte desta peça, mas seguem pendentes de
`CAMINHO_CODEX_ENTREGA_HOLDING.md`, e o primeiro deles bloqueia revisão visual:

1. **Gerador do catálogo AB Motion** — dois bugs distintos: descrição de fallback
   aplicada a todo card, e emissão de desktop/vertical como cards separados
2. **Hub Puressência** — copy pronta, aguarda implementação
3. **Trajetum** — 37 páginas, CTA de mentoria 1:1, link para mídia educacional

---

## 9. Critérios de aceite

- [ ] Cinco seções, produto em cena contínua, sem troca de tela
- [ ] Ambiente HDRI e ACES aplicados; sem luz pontual isolada
- [ ] Pós-processamento presente e **sutil** — bloom não visível como efeito
- [ ] `MeshPhysicalMaterial` com clearcoat e mapas; nenhuma cor chapada
- [ ] Lenis com easing declarado; revelação escalonada
- [ ] `fov` entre 35 e 40, profundidade de campo rasa
- [ ] `prefers-reduced-motion` desliga tudo; cena carrega parada
- [ ] Tokens em `:root` + dark em media query **e** `[data-theme]`
- [ ] Mobile 390 px sem overflow; toque de 44 px
- [ ] Zero erro de console; degradação sem WebGL
- [ ] **Nenhuma alegação de fórmula, registro, certificação ou eficácia**
- [ ] Deploy em **preview**, não produção

---

*Sem DNS, sem alias, sem preço público, sem envio. Nenhum arquivo original
apagado. `CENTRAL_DE_CONTROLE.md` intocado.*
