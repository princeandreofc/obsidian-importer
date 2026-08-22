# HeyGen — prompts dos filmes da loja Pop Casa

**Data:** 21/08/2026 · **Estado:** `CANÔNICO` — validado em 22/08/2026; nenhum crédito consumido
**Herda do pacote V2:** narração travada (sobra vira motion/b-roll/música, nunca fala nova),
private review, PT-BR, sem claim inventado, gate de pronúncia por filme.

**Regra específica desta série:** os filmes são de LOJA DE VERDADE. Todo plano de
produto usa **foto/vídeo oficial do SKU ou captura de tela real dos sites** — nunca
produto gerado por IA. Onde o material oficial ainda não existe, o plano usa a
interface real (que já está no ar) — a interface é verdadeira.

**Assets de captura disponíveis hoje:**
- https://pop-casa-meeting-demo-20260821.vercel.app/ (Demo MART)
- https://pop-casa-studio-20260821.vercel.app/ (B2B)
- https://pop-casa-client-20260821.vercel.app/ (B2C)
- https://camargo-decor-20260821.vercel.app/ (Camargo Decor)
- Loja Pop Casa (73 fichas Studio L, folha de proposta) — arquivo no repo
- **Experiência Pop Casa** (galeria 3D navegável) — arquivo no repo; gravar tela
  do passeio, do foco 360 e do Efeito Vertigo

## Gramática de câmera (vale para os quatro filmes)

```text
CAMERA GRAMMAR — real store, cinematic:
- Slow dolly-in as the only establishing move; no whip pans, no shake.
- Product close-ups: 360 turntable macro on OFFICIAL product photography or
  real screen capture only. Shallow depth of field, single key light look.
- Screen captures: capture at 60fps, move like a camera (ease-in-out pans,
  parallax between UI layers), never a static screencast.
- Zoom in/out only as intentional beats (dolly feel), max twice per film.
- Cut on action; hold final frames 1.5s. Music bed low; silence acceptable.
- Grade: warm dark editorial, soft grain, gentle vignette. No neon, no HDR clip.
```

## Bloco universal (prefixa todo prompt)

```text
Language: Brazilian Portuguese. Orientation: landscape 16:9.
Private review only. Do not publish or distribute.
This script is the complete and final narration. Do not add, expand, elaborate,
paraphrase or invent any spoken content. Fill remaining time with motion,
real screen capture, typography and music beds — never with additional speech.
Use ONLY the attached real screen recordings and official product photos.
Do not generate product imagery. Do not invent prices, brands, clients or claims.
Do not show partner-brand names in the B2C film until the official list arrives.
```

## Filme 1 — Demo MART (reunião Tina & Fernando Bento) · 45 s

**Narração (travada, 82 palavras ≈ 34 s @145wpm):**
> Isto não é um catálogo. É a casa onde o catálogo mora. Quatro peças reais da
> MART, dois mil e vinte e seis, cada uma na sua vitrine de luz. Role, e você
> caminha. Clique, e você chega perto — trezentos e sessenta graus ao redor da
> peça. Troque o acabamento do ambiente e veja a mesma peça em outra casa.
> Quando a escolha estiver feita, a proposta sai pronta, em uma folha. Pop Casa:
> o jeito novo de comprar decoração no atacado.

**Shot list:** 1) dolly-in na abertura da Experiência ("Entre na casa") · 2) passeio
por scroll passando duas vitrines · 3) foco: órbita 360 na estação SKU 23189 ·
4) troca de paleta areia→noite ao vivo · 5) corte para a folha de proposta
imprimindo na Loja · 6) lockup Pop Casa.
**CRITICAL ON-SCREEN TEXT:** `POP CASA` · `MART · 2026` · `SKU 23407 · 23189 · 23190 · 22098` · `A PROPOSTA SAI PRONTA`

## Filme 2 — Pop Casa Studio B2B · 30 s

**Narração (52 palavras ≈ 22 s):**
> Vendedor não precisa de mais um PDF. Precisa de uma sala. Aqui o lojista anda
> pelo mix, vê a peça de todos os lados, monta o pedido brincando — e sai com a
> folha de proposta assinável na mão. Sem preço público. Sem fricção. Pop Casa
> Studio: a visita presencial, sem o deslocamento.

**Shot list:** captura real do B2B: filtros → card → escala humana (barra 1,70 m) →
carrinho→proposta → folha A4. Fechar no contato Camargo & Pinheiro.
**CRITICAL ON-SCREEN TEXT:** `SEM PREÇO PÚBLICO · PROPOSTA POR ESCOPO` · `POP CASA STUDIO`

## Filme 3 — Pop Casa Client B2C · 30 s

**Narração (49 palavras ≈ 20 s):**
> Tem site que a gente visita. E tem site que a gente conta pros amigos. Entre,
> ande pela casa, chegue perto do que gostou, gire, aproxime, troque o ambiente
> de cor. Mesmo sem comprar nada hoje, você vai querer voltar amanhã. Pop Casa:
> a loja que é um lugar.

**Shot list:** mobile-first: dedo rolando o passeio → pinça de zoom na órbita →
Vertigo 2 s → paleta terracota → reação de compartilhamento (mock de UI própria,
sem app de terceiros). **Área de marcas parceiras: NÃO aparece** até a lista
oficial do Fernando Bento.
**CRITICAL ON-SCREEN TEXT:** `POP CASA` · `ENTRE. ANDE. VOLTE.`

## Filme 4 — Camargo Decor · 20 s

**Narração (34 palavras ≈ 14 s):**
> Camargo e Pinheiro, desde dois mil e doze: o mix que veste a loja inteira.
> Agora, com uma casa digital para cada lojista visitar. Peça a visita — ou
> entre agora, a porta está aberta.

**Shot list:** captura do site Camargo Decor → corte para a Experiência →
contato 48 99988-2213. **CRITICAL:** `CAMARGO & PINHEIRO · DESDE 2012`

## Gate por filme

| Filme | Pendências antes do render |
|---|---|
| Demo MART | pronúncia `MART` confirmada; captura da Experiência gravada |
| B2B | nenhuma além da captura |
| B2C | lista de marcas do Fernando Bento **não entra** neste corte |
| Camargo | confirmar leitura do telefone em voz (dígito a dígito) |


---

## Canonização — validação de 22/08/2026

**O que está garantido por verificação, não por promessa:**

| Verificação | Resultado |
|---|---|
| 4 sites de captura respondendo | HTTP 200 nos quatro |
| Experiência Pop Casa renderizando | testada em Chromium headless, screenshots em anexo no PR |
| Contagem das 4 narrações | recontada por script; números corrigidos (82/52/49/34) |
| Fala × alvo | todas cabem com folga de +6 a +11 s — sobra vira motion, nunca fala |
| Regra anti-invenção | herdada do pacote V2, presente no bloco universal |

**O que NENHUM documento pode garantir daqui:** o comportamento do render do
HeyGen em si — isso só se verifica no primeiro render privado, com o conector
autorizado pelo proprietário. O primeiro corte é o teste; os prompts foram
escritos para que a única variável seja o HeyGen, não o material.

**Nota sobre as capas aprovadas (Cosmic Top Secret, Secret Gardens/Observatory
Sessions, Lunar/Moon Tides):** carregam selo e numeração de catálogo no estilo
Hot Creations (HOTC-283/284). Para prévia e validação interna, cobertas pela
autorização assinada. **Antes de qualquer publicação**, a numeração e o selo
precisam do aval do label — número de catálogo é afirmação factual do label,
não nossa.