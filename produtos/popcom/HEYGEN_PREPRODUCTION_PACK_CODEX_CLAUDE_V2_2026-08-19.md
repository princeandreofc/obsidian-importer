# HEYGEN PRE-PRODUCTION PACK V2 — HOLDING / CODEX + CLAUDE

**Data:** 19/08/2026  
**Estado:** `PARCIALMENTE_LIBERADO` — direitos assinados; gate remanescente é pronúncia  
**Idioma master:** português do Brasil  
**Formato inicial:** landscape 16:9  
**Conta pretendida:** AMOS, saldo superior a 1.000 créditos informado pelo proprietário  
**Fonte revisada:** commit `808a7c2`, SHA-256 `5e64fc20cc9ff3fd4211dcf72f5cf9a1f81633312cbf7eac871ebdab5dcce672`  
**Parecer incorporado:** `CLAUDE_REVISAO_HEYGEN_2026-08-19.md`, commit `81fdcd8`  

### Alterações da V2.1 — 19/08/2026, após a assinatura dos direitos

Declaração do proprietário: **direitos de mídia assinados e autorização de todos
os envolvidos para prévia e validação final.** Consequências registradas:

- `B-DIR` baixado para Ali Love e Prince Andre — o acervo real autorizado existe;
- `B-DUR` deixa de ser bloqueio de pré-voo e vira item de revisão pós-render;
- seis filmes passam a depender de um único gate: pronúncia.

Estado anterior preservado no git, commit `21df9328`.

### Alterações da V2

- remove a autorização para o Video Agent ampliar ou inventar narração;
- separa duração de fala e duração visual;
- transforma pronúncia em gate por filme;
- aplica os ajustes editoriais de Ali Love, Prince Andre e AB Cream;
- registra cobertura asset → cena e os bloqueios por filme;
- prioriza AB Cream e Impacto Digital como primeiros testes privados, depois das aprovações.

## 1. Instrução para o Claude

Este arquivo contém tudo o que pode ser preparado sem OAuth ou consumo de créditos. Não tente conectar a conta, solicitar token/callback, criar avatar ou renderizar vídeo a partir deste documento.

Quando o proprietário conectar HeyGen em `claude.ai → Configurações → Conectores`:

1. usar primeiro somente ferramentas de leitura;
2. confirmar visualmente que a conta conectada é **AMOS**;
3. confirmar visualmente o saldo correto;
4. verificar se `compose`/`render_video` estão disponíveis naquele ambiente;
5. se geração estiver desabilitada para CLI/IDE, registrar isso e encaminhar o pacote para execução pelas skills locais do Mac;
6. não consumir crédito para testar conexão;
7. gerar somente após aprovação explícita do roteiro, estilo, identidade e asset bundle;
8. gerar um master 16:9 por vez, sempre em private review;
9. derivar 9:16 e 4:5 somente depois de picture lock.

Não compartilhar chaves, tokens, URLs de callback ou credenciais em chat.

## 2. Política de identidade e verdade editorial

- Ali Love e Prince Andre: **mídia real autorizada + motion AB Motion**. Não usar avatar fabricado, stock presenter ou pessoa gerada para representar os artistas.
- André, Luiz Antonio e Dr. Brenno: avatar, voz clonada ou aparência identificável somente com consentimento documentado e look aprovado.
- Pessoas geradas nas imagens Wave 1 são cenas institucionais representativas; não identificar como pessoa real.
- Voz-over neutra ou stock presenter é permitido em institucionais quando não produzir falsa atribuição.
- AB Cream é estudo demonstrativo; zero claims de fórmula, registro, certificação ou eficácia.
- Climbex Global nunca aparece em filme, página, metadata ou lockup de Ali Love.
- Lockup correto: `LOVE ALWAYS WINS / Ali Love × AB Motion`.
- Claims acadêmicos, profissionais, musicais e comerciais só entram depois de validação documental.

## 3. Asset bundle local

Diretório master:

`/Users/boliveiracastrillon/Documents/Codex/2026-08-18/l/outputs/ASSET_LIBRARY_HOLDING_WAVE1_2026-08-18/images/`

| Superfície | Asset permitido na prévia | Classe |
|---|---|---|
| Puressência | `puressencia-ecossistema-material-v1.png` | abstrato |
| Ali Love | `ali-love-cosmic-portal-v1.png` | abstrato; não representa o artista |
| Prince Andre | `prince-andre-nine-turns-v1.png` | abstrato; não representa o artista |
| AB Motion | `ab-motion-studio-v1.png` | cena representativa |
| AB Cream | `ab-cream-product-v1.png` | produto demonstrativo |
| Climbex | `climbex-bpm-operations-v1.png` | cena representativa |
| Trajetum | `trajetum-career-advisory-v1.png` | cena representativa |
| Dr. Brenno | `dr-brenno-xai-system-v1.png` | abstrato técnico |
| Planning | quatro imagens `planning-*-v1.png` | cenas representativas |
| Impacto Digital | `impacto-digital-pulse-team-v1.png` | cena representativa |

Ali Love e Prince Andre exigem bundle adicional de fotos/vídeos reais com
autorização. **V2.1: a autorização existe — o bundle ainda não.** Assinatura
libera o uso; não copia arquivo para o disco. Antes do render desses dois,
alguém precisa selecionar o acervo real e depositá-lo no diretório master, com
os planos 3–4 de cada shot list cobertos. Enquanto o bundle não estiver montado,
animatic abstrato segue permitido; apresentar como filme final do artista, não.

### Cobertura asset → cena

| Filme | Cobertura atual | Complemento necessário |
|---|---|---|
| Puressência | parcial | quatro portais e mapa do hub em motion |
| Ali Love | direitos ok; bundle a montar | depositar acervo real autorizado para os planos 3–4 |
| Prince Andre | direitos ok; bundle a montar | depositar acervo real autorizado para os planos 3–4 |
| AB Motion | parcial | case de cliente para o before/after; confirmar se a assinatura cobre |
| AB Cream | completa | motion e tipografia a partir do asset existente |
| Climbex | parcial | diagramas AS-IS/TO-BE em motion |
| Trajetum | parcial | diagramas de caminho em motion |
| Dr. Brenno | parcial | série temporal e contribuição de variáveis em motion |
| Planning institucional | completa | montagem com os quatro assets existentes |
| Planning tutorial | insuficiente | captura do preview após picture lock |
| Impacto Digital | parcial | quatro dimensões em motion |

## 4. Regras universais do prompt HeyGen

Incluir em todo prompt:

```text
Language: Brazilian Portuguese.
Orientation: landscape 16:9.
Private review only. Do not publish or distribute.
One topic only. Front-load the hook in the first five seconds.
Use the attached assets only for the roles explicitly described.
Do not identify representative people as real named individuals.
Do not invent facts, numbers, credentials, clients, media coverage, awards or product claims.
Use motion graphics for titles, diagrams and brand systems.
Use stock media only for generic environments and human activity.
Use AI-generated visuals only for abstract concepts.
Include captions and preserve comfortable safe margins for later vertical crops.
This script is the complete and final narration. Do not add, expand, elaborate, paraphrase or invent any spoken content. If the narration is shorter than the target duration, fill the remaining time with motion, b-roll, typography and music beds — never with additional speech. Silence under music is acceptable and preferred over invented content.
```

Exceção: frases listadas em `CRITICAL ON-SCREEN TEXT` devem aparecer literalmente, sem tradução, correção ou paráfrase.

### Timing calculado da narração

Estimativa-base: aproximadamente 145 palavras por minuto. O alvo original não autoriza fala adicional. A coluna “recomendação” é uma proposta editorial para aprovação humana.

| Filme | Palavras V2 | Fala estimada V2 | Alvo original | Recomendação para o primeiro corte |
|---|---:|---:|---:|---|
| Puressência | 106 | 44 s | 60 s | 45–50 s ou roteiro humano ampliado |
| Ali Love | 102 | 42 s | 75 s | 45–55 s, com respiro musical |
| Prince Andre | 108 | 45 s | 60 s | 45–50 s, com lista visual |
| AB Motion | 88 | 36 s | 45 s | 40–45 s |
| AB Cream | 56 | 23 s | 30 s | 25–30 s |
| Climbex | 95 | 39 s | 60 s | 40–45 s ou roteiro humano ampliado |
| Trajetum | 93 | 38 s | 60 s | 40–45 s ou roteiro humano ampliado |
| Dr. Brenno | 119 | 49 s | 75 s | 50–55 s ou roteiro humano ampliado |
| Planning institucional | 97 | 40 s | 60 s | 40–45 s |
| Planning tutorial | 185 | 77 s | 120–180 s | 90–120 s, conforme captura aprovada |
| Impacto Digital | 79 | 33 s | 45 s | 35–40 s |

O primeiro review deve medir a duração real. Não acelerar a voz para cumprir o alvo e não preencher a diferença com nova fala. Ajustar apenas montagem, motion, música ou texto revisado por pessoa.

**Duração não é mais bloqueio de pré-voo (V2.1).** `B-DUR` existia porque o §4 da
V1 autorizava o modelo a inventar fala para preencher o alvo — decidir a duração
antes do render era a única defesa contra isso. Com a narração travada, essa via
está fechada: sobra de tempo vira motion, b-roll, tipografia ou silêncio sob
música, nunca frase nova. O que resta é preferência editorial, e preferência
editorial se decide assistindo, não lendo tabela.

Risco residual, declarado: se ao assistir a decisão for **ampliar** o roteiro, a
nova copy é escrita por pessoa e o filme é regerado. Isso custa créditos, não
verdade — é retrabalho previsível, não um risco a ser contido por gate.

## 5. Glossário de pronúncia — validar por filme antes do render

| Termo | Orientação inicial | Gate |
|---|---|---|
| Puressência | `pu-re-SÊN-ci-a` | confirmar com proprietário |
| Ali Love | respeitar pronúncia pública do artista | confirmar em mídia real |
| Prince Andre | `Prince André`; não anglicizar André sem aprovação | confirmar com artista |
| AB Motion | letras `A-B`, depois `Motion` | confirmar |
| AB Cream | letras `A-B`, depois `Cream` | confirmar |
| Climbex | `CLAIM-beks` como hipótese | confirmação obrigatória |
| Trajetum | `tra-JÉ-tum` como hipótese | confirmação obrigatória |
| Brenno Castrillon | `Brê-no Cas-tri-ón` como hipótese | confirmação obrigatória |
| XAI | dizer `X-A-I` ou `inteligência artificial explicável` | escolher antes do render |
| Sankhya | usar pronúncia oficial da marca no Brasil | validar em fonte oficial |
| BPO | dizer letras `B-P-O` | aprovado se mantido assim |
| ICMS-ST | dizer letras `I-C-M-S`, pausa, `S-T` | validar com Luiz |
| Pulso ID | `Pulso I-D` | confirmar com Impacto |

O gate é aplicado por filme: não enviar um job enquanto houver termo falado naquele filme sem confirmação. Uma pendência que não aparece na locução do filme não bloqueia esse job.

| Filme | Termos falados que precisam estar confirmados |
|---|---|
| Puressência | Puressência, Ali Love, Prince Andre, AB Motion, AB Cream |
| Ali Love | Ali Love, AB Motion |
| Prince Andre | Prince Andre |
| AB Motion | AB Motion |
| AB Cream | AB Cream |
| Climbex | Climbex |
| Trajetum | Trajetum |
| Dr. Brenno | Brenno Castrillon e escolha de XAI |
| Planning institucional | Sankhya e BPO, quando mantidos na versão final |
| Planning tutorial | Sankhya, BPO e ICMS-ST, quando falados |
| Impacto Digital | Pulso ID |

---

# 6. FILMES

## 6.1 Puressência — manifesto institucional

**Objetivo:** explicar o hub sem apagar as identidades próprias.  
**Duração:** 60 s.  
**Apresentação:** voz-over neutra; sem avatar.  
**Estilo:** `Velvet Standard` + materialidade orgânica; tinta, creme, violeta e ouro cerimonial.  
**Asset principal:** `puressencia-ecossistema-material-v1.png`.

### Narração PT-BR

Ideias diferentes não precisam parecer iguais para pertencer ao mesmo ecossistema. A Puressência conecta música, motion, beleza e tecnologia por uma lógica comum: verdade de origem, direção criativa e execução responsável. Ali Love preserva sua voz. Prince Andre constrói seu próprio percurso. A AB Motion transforma estratégia em imagem em movimento. A AB Cream revela um estudo de marca, produto e materialidade. O hub não mistura essas identidades. Ele mostra os processos, as escolhas e os cases que transformam visão em entrega. Cada projeto encontra sua linguagem. Cada linguagem mantém sua autoria. Entre pelos cases e descubra como cada ideia encontra a forma certa para existir.

### Shot list

1. Matéria escura, luz violeta e textura formando o símbolo Puressência.
2. Quatro materiais/portais distintos surgem sem fundir as marcas.
3. Ali Love e Prince Andre representados apenas por portas abstratas; sem rostos gerados.
4. AB Motion aparece como timeline/processo; AB Cream como macro de embalagem demonstrativa.
5. Mapa do hub converge para quatro CTAs independentes.

### CRITICAL ON-SCREEN TEXT

```text
PURESSÊNCIA
ALI LOVE
PRINCE ANDRE
AB MOTION
AB CREAM
ENTRE PELOS CASES
```

### Prompt visual específico

```text
Voice-over narration only. No visible presenter. Treat the attached Puressência image as an abstract material world, not documentary footage. Build four distinct visual portals and keep each brand identity separate. Use elegant motion graphics for the ecosystem map. STYLE — VELVET STANDARD: black, cream, ceremonial gold and restrained violet. Thin all-caps, wide spacing, generous negative space, slow cross-dissolves. Avoid generic corporate stock, neon cyberpunk and fake artist imagery.
```

## 6.2 Ali Love — LOVE ALWAYS WINS

**Objetivo:** trailer artístico de campanha.  
**Duração:** 60–90 s; aprovar primeiro corte em 75 s.  
**Duração editorial recomendada na V2:** 45–55 s; manter respiro musical, sem fala gerada.  
**Apresentação:** sem presenter/avatar. Voz do artista somente com autorização; fallback é sound design + texto.  
**Estilo:** cosmic disco, instalação de museu, sulco/portal, preto reflexivo.  
**Asset abstrato:** `ali-love-cosmic-portal-v1.png`.  
**Asset obrigatório para filme final:** mídia real autorizada de Ali Love.

### Narração/conceito PT-BR

O amor não é apenas o tema. É a força que atravessa a pista. Fragmentos do acervo real encontram uma instalação cósmica sem apagar o artista, sem substituir sua presença e sem inventar uma nova história. A imagem deixa de ser cenário e vira encontro. A campanha não promete uma fuga. Ela lembra por que ainda dançamos juntos: não para desaparecer, mas para reconhecer no outro o mesmo pulso. No último compasso, movimento, memória e presença convergem para uma afirmação simples. Love Always Wins. Ali Love e AB Motion. Uma experiência construída com acervo real, direção de movimento e respeito à origem.

### Shot list

1. Sulco abstrato pulsa no preto; nenhum rosto.
2. Portal Wave 1 abre em movimento lento.
3. Inserções de mídia real autorizada, nunca gerada.
4. Corpo coletivo/silhuetas genéricas sem representar o artista.
5. Órbita fecha em emblema e lockup.

### CRITICAL ON-SCREEN TEXT

```text
LOVE ALWAYS WINS
ALI LOVE × AB MOTION
ENTER THE EXPERIENCE
```

### Prompt visual específico

```text
No presenter and no synthetic artist likeness. Use the attached portal image only as an abstract campaign environment. Real Ali Love footage may appear only when attached and explicitly rights-cleared. Build a slow cosmic-disco ritual with vinyl grooves, smoke, reflective black surfaces and museum-installation restraint. Motion should feel hypnotic, not like a generic EDM trailer. Avoid lasers, DJ silhouettes, cyberpunk grids and invented performance footage. End on the exact approved lockup. Climbex Global must never appear.
```

## 6.3 Prince Andre — Nove Voltas

**Objetivo:** manifesto de retorno/percurso, sujeito à aprovação do conceito.  
**Duração:** 60 s.  
**Duração editorial recomendada na V2:** 45–50 s; três conceitos na voz e nove em tela.  
**Apresentação:** sem presenter/avatar fabricado; voz do artista somente autorizada.  
**Estilo:** nove cores, círculos, memória e progressão.  
**Asset abstrato:** `prince-andre-nine-turns-v1.png`.  
**Asset obrigatório para filme final:** mídia real autorizada de Prince Andre.

### Narração PT-BR

Toda trajetória volta diferente. Nove voltas, nove pulsos, uma identidade em movimento. Cada círculo revela uma camada. Na voz, três pontos orientam o percurso: origem, presença e futuro. Na imagem, as nove voltas se revelam sem pressa. O material abstrato abre o espaço. O acervo real comprova o artista. A edição reúne os dois sem inventar biografia, performance ou conquista. Prince Andre não retorna para repetir uma versão anterior. Ele volta para mostrar o que permaneceu, o que mudou e o que ainda precisa nascer. O percurso não termina quando o círculo se fecha. Ele ganha outro sentido. Conheça Prince Andre. Ouça o percurso. Veja o próximo movimento.

### Shot list

1. Primeiro círculo surge no silêncio.
2. Nove cores entram uma por vez; manter legibilidade.
3. Mídia real autorizada ancora o artista.
4. Arquivo, estúdio e palco somente se forem materiais reais.
5. Nono círculo abre para o CTA, sem domínio público enquanto B1 estiver aberto.

### CRITICAL ON-SCREEN TEXT

```text
NOVE VOLTAS
PRINCE ANDRE
ORIGEM
REPERTÓRIO
RISCO
SILÊNCIO
APRENDIZADO
PRESENÇA
COLABORAÇÃO
TRANSFORMAÇÃO
FUTURO
OUÇA O PERCURSO
VEJA O PRÓXIMO MOVIMENTO
PRIVATE REVIEW
```

### Prompt visual específico

```text
No presenter and no synthetic artist likeness. Use the attached nine-turns artwork as an abstract color and motion system. Use real Prince Andre media only when explicitly attached and rights-cleared. Reveal nine circles with deliberate pacing and distinct colors. Keep the treatment musical, authored and restrained. Do not invent stage footage, biography, achievements, releases or audience scale. End as PRIVATE REVIEW with no public domain CTA while domain gate B1 remains open.
```

## 6.4 AB Motion — processo antes do efeito

**Objetivo:** studio/case reel.  
**Duração:** 45 s.  
**Apresentação:** voz-over neutra; André somente após avatar/voz autorizados.  
**Estilo:** `Geometric Bold`, processo visível, before/after.  
**Asset:** `ab-motion-studio-v1.png`.

### Narração PT-BR

Motion não começa no efeito. Começa na decisão. Primeiro, o briefing. Depois, pesquisa, linguagem, ritmo e protótipo. Cada etapa transforma uma intenção abstrata em uma escolha que pode ser vista, testada e revisada. A AB Motion reúne direção de arte, audiovisual e tecnologia para construir movimento com propósito. O case não mostra apenas o resultado bonito. Mostra o problema, o processo e a razão por trás de cada solução. Da primeira referência ao render final, autoria e evidência permanecem visíveis. Traga o desafio. Vamos desenhar o movimento certo.

### Shot list

1. Briefing e referências em mesa/parede representativa.
2. Storyboard, grid e curvas de movimento.
3. Before/after com casos reais autorizados.
4. Timeline, revisão e render.
5. CTA sobre fundo limpo.

### CRITICAL ON-SCREEN TEXT

```text
BRIEFING
PESQUISA
LINGUAGEM
RITMO
PROTÓTIPO
REVISÃO
ENTREGA
AB MOTION
```

### Prompt visual específico

```text
Voice-over narration only unless an approved André avatar is explicitly selected. Use the attached studio image as a representative process scene. Use real case media only when attached and approved. STYLE — GEOMETRIC BOLD: maximum three flat colors per frame, sixty percent negative space, bold type as the primary element, clean cuts on beat. Show process before outcome. Do not expose legacy/private files.
```

## 6.5 AB Cream — case demonstrativo

**Objetivo:** estudo de marca/produto.  
**Duração:** 30 s.  
**Duração editorial recomendada na V2:** 25–30 s.  
**Apresentação:** voz-over; sem pessoa real.  
**Estilo:** macro premium, materialidade, `Velvet Standard`.  
**Asset:** `ab-cream-product-v1.png`.

### Narração PT-BR

Um produto demonstrativo também precisa parecer verdadeiro. AB Cream é um estudo de marca, embalagem, textura e presença digital. O case explora materialidade, luz, tipografia e experiência: como um sistema visual dá presença a uma ideia. A imagem mostra como esse sistema transforma intenção em linguagem reconhecível. Veja o processo de marca por trás da imagem.

### Shot list

1. Macro da embalagem demonstrativa.
2. Textura, luz e tipografia.
3. Grid de identidade e aplicações digitais.
4. Disclosure demonstrativo.
5. CTA do case.

### CRITICAL ON-SCREEN TEXT

```text
AB CREAM
ESTUDO DEMONSTRATIVO
SEM CLAIMS DE FÓRMULA OU EFICÁCIA
VEJA O SISTEMA DE MARCA
```

### Prompt visual específico

```text
Voice-over narration only. Treat the attached product image as a fictional demonstrative brand study. STYLE — VELVET STANDARD with black, cream and one restrained accent. Use macro photography language, material textures and elegant typography. Do not generate medical, cosmetic, regulatory or efficacy claims. Keep the demonstrative disclosure readable.
```

## 6.6 Climbex Global — processo antes da automação

**Objetivo:** explicar BPM, tecnologia, IA e automação.  
**Duração:** 60 s.  
**Apresentação:** stock presenter ou voz-over; avatar real somente autorizado.  
**Estilo:** `Swiss Pulse`/`Digital Grid`.  
**Asset:** `climbex-bpm-operations-v1.png`.

### Narração PT-BR

Automação sem processo só acelera o problema. A Climbex começa pela operação real. Primeiro, mapeia a situação atual. Depois, identifica papéis, dados, gargalos e decisões. Com essa base, desenha o processo futuro e define o que precisa ser governado, medido e melhorado. Só então entram BPM, tecnologia, inteligência artificial e automação. O objetivo não é adicionar ferramentas. É construir um fluxo compreensível, seguro e capaz de evoluir. Uma tela bonita não corrige uma operação confusa. Um processo bem desenhado cria clareza para pessoas e sistemas. Comece pelo processo que mais impede sua operação de avançar.

### Shot list

1. Operação atual com gargalos representativos.
2. Mapa AS-IS e papéis.
3. Fluxo TO-BE animado.
4. Tecnologia/IA conectada depois do processo.
5. CTA consultivo.

### CRITICAL ON-SCREEN TEXT

```text
SITUAÇÃO ATUAL
PAPÉIS
DADOS
PROCESSO FUTURO
BPM + TECNOLOGIA + IA + AUTOMAÇÃO
COMECE PELO PROCESSO
```

### Prompt visual específico

```text
Use voice-over or a clearly generic stock presenter. Use the attached operations image as a representative scene. STYLE — SWISS PULSE: black and white with electric blue, grid-locked layouts, Helvetica-style bold type, animated counters only when sourced, diagonal accents and grid wipes. Use motion graphics for AS-IS and TO-BE diagrams. Do not mention Ali Love anywhere.
```

## 6.7 Trajetum — trajetórias com contexto

**Objetivo:** apresentar Education, Career e Technical Advisory.  
**Duração:** 60 s.  
**Apresentação:** voz-over/stock; Dr. Brenno somente autorizado.  
**Estilo:** humano, editorial, progressão.  
**Asset:** `trajetum-career-advisory-v1.png`.

### Narração PT-BR

Carreira não é uma linha reta. É uma sequência de escolhas com contexto. A Trajetum reúne educação, desenvolvimento de carreira e advisory técnico para transformar experiência em direção. O trabalho começa com perguntas, evidências e limites claros. O que precisa ser aprendido? Qual decisão está sendo adiada? Que experiência pode se tornar contribuição? Não há promessa de atalho nem fórmula universal. Há um percurso que pode ser explicado, avaliado e ajustado ao longo do tempo. Formação, progressão e impacto passam a fazer parte da mesma trajetória. Descubra qual caminho precisa ser desenhado agora.

### Shot list

1. Caminhos/linhas convergem de forma editorial.
2. Cena representativa de conversa e aprendizagem.
3. Três pilares aparecem separadamente.
4. Evidências e checkpoints substituem promessas.
5. CTA sem formulário real.

### CRITICAL ON-SCREEN TEXT

```text
EDUCATION
CAREER
TECHNICAL ADVISORY
EVIDÊNCIA · CONTEXTO · DIREÇÃO
TRAJETUM — PREVIEW EDITORIAL
```

### Prompt visual específico

```text
Use voice-over or a generic stock presenter. Do not depict or name a generated person as Dr. Brenno. Use the attached image as a representative learning and career scene. Favor warm editorial framing, path diagrams and evidence checkpoints. Avoid promises, coaching clichés and guaranteed outcomes. Keep PREVIEW EDITORIAL visible in the end card.
```

## 6.8 Dr. Brenno — XAI e decisão compreensível

**Objetivo:** explainer técnico.  
**Duração:** 75 s.  
**Apresentação:** voz-over neutra; avatar/voz do Dr. Brenno somente autorizados.  
**Estilo:** `Digital Grid` com precisão acadêmica.  
**Asset:** `dr-brenno-xai-system-v1.png`.

### Narração PT-BR

Detectar uma anomalia é importante. Explicar por que ela aconteceu muda a decisão. Sistemas industriais produzem sinais complexos, em grande volume e sob condições que nem sempre se repetem. A inteligência artificial pode identificar padrões, desvios e combinações difíceis de perceber. Mas um alerta sem contexto ainda deixa perguntas abertas. A inteligência artificial explicável conecta dado, condição operacional e causa provável. Ela mostra quais sinais influenciaram o resultado, onde estão os limites do modelo e o que precisa ser verificado por especialistas humanos. Explicar não significa prometer certeza. Significa tornar o raciocínio rastreável, discutível e útil. Educação, pesquisa aplicada e advisory técnico se encontram quando um resultado deixa de ser apenas computado e passa a apoiar uma decisão compreensível.

### Shot list

1. Série temporal/sinais abstratos.
2. Anomalia destacada com origem rastreável.
3. Camadas de explicação e contribuição de variáveis.
4. Especialista humano revisa o contexto; pessoa genérica.
5. End card técnico sem afiliação não validada.

### CRITICAL ON-SCREEN TEXT

```text
DETECÇÃO
EXPLICAÇÃO
CONTEXTO
LIMITES
DECISÃO HUMANA
XAI — INTELIGÊNCIA ARTIFICIAL EXPLICÁVEL
```

### Prompt visual específico

```text
Voice-over narration only unless an approved Dr. Brenno avatar and voice are explicitly selected. Use the attached XAI image as an abstract technical system, not as documentary proof. STYLE — DIGITAL GRID: dark background, cyan and amber accents, monospaced type, signal plots and clean grid wipes. Use motion graphics for anomaly detection and feature contribution. Do not invent affiliations, papers, institutions, metrics or credentials.
```

## 6.9 Planning — institucional

**Objetivo:** apresentar as cinco frentes de atuação.  
**Duração:** 60 s.  
**Apresentação:** voz-over ou stock presenter; Luiz somente autorizado.  
**Estilo:** `Velvet Standard`/`Swiss Pulse`, contabilidade contemporânea.  
**Assets:** quatro masters `planning-*-v1.png`.

### Narração PT-BR

Fechar números é o começo. Decidir melhor é o trabalho. A Planning integra cinco frentes para manter a empresa organizada, em conformidade e preparada para escolher com mais segurança. A assessoria contábil tradicional cuida das rotinas fiscal, pessoal e contábil. O BPO assume operações contábeis, fiscais e financeiras com apoio consultivo. Em processos e ERP Sankhya, tecnologia e rotina passam a funcionar juntas. Para o agronegócio de Mato Grosso, o planejamento considera as regras específicas do setor. No varejo e na distribuição, a atuação cobre apuração, ICMS-ST, créditos e planejamento tributário. Primeiro, informação organizada. Depois, decisão responsável.

### Shot list

1. Hero institucional representativo.
2. Cinco frentes entram em cards claros.
3. Equipe mapeia processo/ERP.
4. Agro e distribuição aparecem como setores distintos.
5. CTA para diagnóstico, sem coleta real no preview.

### CRITICAL ON-SCREEN TEXT

```text
PLANNING
ASSESSORIA CONTÁBIL
BPO CONTÁBIL, FISCAL E FINANCEIRO
PROCESSOS E ERP SANKHYA
AGRONEGÓCIO DE MATO GROSSO
VAREJO E DISTRIBUIÇÃO
INFORMAÇÃO ORGANIZADA. DECISÃO RESPONSÁVEL.
```

### Prompt visual específico

```text
Use voice-over or a clearly generic stock presenter. Do not depict a generated person as Luiz Antonio. Use the four attached Planning images only as representative institutional scenes. Combine VELVET STANDARD restraint with SWISS PULSE information design. Use motion graphics for the five service fronts. Do not invent tax savings, compliance guarantees, client numbers or legal advice.
```

## 6.10 Planning — tutorial do diagnóstico

**Objetivo:** ensinar o uso do preview sem coletar dados reais.  
**Duração:** 2–3 min.  
**Apresentação:** stock presenter ou voz-over; captura do preview.  
**Estilo:** tutorial limpo, `Swiss Pulse`.  
**Asset obrigatório:** captura autorizada do preview Planning.

### Narração PT-BR

Neste tutorial, você vai conhecer o diagnóstico demonstrativo da Planning. O preview foi criado para organizar uma conversa inicial. Ele não transmite dados e não substitui análise contábil, fiscal ou jurídica.

Comece escolhendo a frente que melhor representa sua prioridade: assessoria contábil, BPO, processos e ERP Sankhya, agronegócio ou varejo e distribuição. Em seguida, indique o estágio atual da operação. O objetivo não é julgar a empresa, mas entender quanto do processo já está documentado e acompanhado.

Depois, selecione a urgência. Uma obrigação próxima, uma implantação de ERP ou uma mudança operacional podem exigir ritmos diferentes. Revise as respostas antes de avançar. O sistema gera um resumo para facilitar a conversa, sem produzir diagnóstico profissional definitivo.

Se o resumo estiver correto, copie o conteúdo. Encaminhe pelo canal oficial da Planning somente depois de concordar com o compartilhamento. Não inclua senha, documento pessoal, dado bancário, segredo comercial ou informação sensível no preview.

O próximo passo é humano. A equipe avalia contexto, documentos necessários e limites do atendimento. Use esta ferramenta para chegar à conversa com mais clareza — não para substituir a análise de um profissional habilitado.

### Shot list

1. Aviso inicial: preview demonstrativo, sem transmissão.
2. Seleção da frente prioritária.
3. Estágio da operação.
4. Urgência.
5. Revisão e resumo.
6. Cópia consciente e canal oficial.
7. Aviso de dados sensíveis e análise humana.

### CRITICAL ON-SCREEN TEXT

```text
PREVIEW DEMONSTRATIVO
NENHUM DADO É TRANSMITIDO
1. ESCOLHA A FRENTE
2. INDIQUE O ESTÁGIO
3. DEFINA A URGÊNCIA
4. REVISE O RESUMO
NÃO INFORME DADOS SENSÍVEIS
O DIAGNÓSTICO NÃO SUBSTITUI ANÁLISE CONTÁBIL, FISCAL OU JURÍDICA
```

### Prompt visual específico

```text
Use voice-over or a generic stock presenter. This is a screen-guided tutorial for a non-submitting preview. Use the attached or captured Planning interface as the primary B-roll. STYLE — SWISS PULSE: grid-locked information design, black and white with restrained blue, clear numbered steps, no decorative counters. Never show real personal, fiscal, banking or client data. Keep every safety notice on screen long enough to read.
```

## 6.11 Impacto Digital — Pulso ID

**Objetivo:** manifesto curto do sistema Pulso ID.  
**Duração:** 45 s.  
**Apresentação:** voz-over ou stock presenter.  
**Estilo:** `Geometric Bold`, pulso e progressão.  
**Asset:** `impacto-digital-pulse-team-v1.png`.

### Narração PT-BR

Presença digital não é volume. É direção percebida. O Pulso ID conecta estratégia, marca, conteúdo e aquisição em um sistema único. Direção organiza a mensagem. Presença torna a marca reconhecível. Impacto transforma atenção em ação. Progresso mede o que realmente mudou. Pessoas, processo e tecnologia deixam de funcionar como peças isoladas e passam a responder ao mesmo objetivo. Menos atividade sem sentido. Mais clareza sobre o próximo movimento. Encontre o ponto do seu pulso digital que precisa ganhar direção.

### Shot list

1. Pulso visual nasce no centro.
2. Quatro dimensões aparecem em sequência.
3. Equipe representativa conecta estratégia e execução.
4. Métricas genéricas sem números inventados.
5. CTA Pulso ID.

### CRITICAL ON-SCREEN TEXT

```text
PULSO ID
DIREÇÃO
PRESENÇA
IMPACTO
PROGRESSO
ENCONTRE O PRÓXIMO MOVIMENTO
```

### Prompt visual específico

```text
Use voice-over or a clearly generic stock presenter. Use the attached team image as a representative scene. STYLE — GEOMETRIC BOLD: limited palette, strong negative space, type-led composition and clean cuts on beat. Animate Direction, Presence, Impact and Progress as one connected pulse. Do not invent performance metrics, clients or campaign results.
```

---

## 7. Checklist de consentimento — voz, avatar e mídia real

Preencher por pessoa antes de qualquer geração identificável:

```text
PESSOA:
PAPEL NO VÍDEO:
TIPO: voz real | voz clonada | avatar | foto | vídeo real
FINALIDADE:
MARCAS/PROJETOS AUTORIZADOS:
ROTEIRO/VERSÃO APROVADA:
LOOK/AVATAR APROVADO:
IDIOMA:
FORMATOS:
PLATAFORMAS:
TERRITÓRIO:
PRAZO DE USO:
MÍDIA PAGA AUTORIZADA: SIM | NÃO
EDIÇÃO/DERIVAÇÕES AUTORIZADAS:
DIREITO DE REVOGAÇÃO:
EVIDÊNCIA DO CONSENTIMENTO:
DATA:
APROVADOR:
```

Consentimento para um projeto não se transfere automaticamente para outra marca, campanha, formato ou mídia paga.

### Registro de direitos — declarado em 19/08/2026

| Campo | Estado |
|---|---|
| Declarante | proprietário da holding |
| Escopo declarado | direito de mídia assinado; autorização de todos os envolvidos |
| Finalidade autorizada | **prévia e validação final** pelos próprios titulares |
| Cobre | Ali Love, Prince Andre — acervo real para uso em filme |
| Não cobre por si só | publicação, distribuição, mídia paga, derivações 9:16/4:5 |
| Documento/versão | *preencher localmente — não transcrever contrato aqui* |
| Territórios e prazo | *preencher localmente* |
| Evidência arquivada em | *preencher localmente* |

O documento assinado **não deve ser colado em chat, PR ou neste arquivo.** Bastam
nome, versão e data para a rastreabilidade; o conteúdo fica no arquivo privado.

**O que a assinatura não altera:** Ali Love e Prince Andre continuam sem avatar
fabricado. A regra nunca foi falta de permissão — é que pessoa gerada não
representa o artista. Com acervo real autorizado em mãos, a regra deixa de ser
restrição e vira o caminho: agora existe material verdadeiro para usar.

**Escopo a confirmar em uma linha:** a assinatura cobre os *artistas*. Cases de
clientes do AB Motion (before/after) e a interface do tutorial Planning envolvem
terceiros que provavelmente não estavam nessa assinatura. Nenhum dos dois trava
os filmes — o AB Motion roda sem o before/after, e o tutorial já depende de
picture lock. Só não devem ser tratados como cobertos sem alguém dizer que sim.

## 8. Checklist do primeiro render privado

- [ ] Conector ligado à conta AMOS e saldo confirmado visualmente
- [ ] Ferramenta de geração realmente disponível no ambiente
- [ ] Roteiro aprovado pelo proprietário/marca
- [ ] Pronúncias confirmadas
- [ ] Asset bundle revisado e com direitos
- [ ] Presenter/voz/identidade definidos
- [ ] Consentimento documentado quando houver pessoa real
- [ ] Prompt contém `CRITICAL ON-SCREEN TEXT`
- [ ] Prompt contém a narração final travada e proíbe fala adicional
- [ ] Prompt declara 16:9, PT-BR e private review
- [ ] Um único tema
- [ ] Sem claim inventado
- [ ] Sem Climbex em Ali Love
- [ ] Sem avatar fabricado para Ali Love ou Prince Andre
- [ ] Session/video identificados no log privado
- [ ] Revisão de duração, legenda, texto, pronúncia, música e identidade
- [ ] Nenhuma publicação ou derivação antes de picture lock

### Status por filme — V2.1, após a assinatura dos direitos

Legenda: `B-PRON` pronúncia · `B-CONC` conceito/claims · `B-CONS` consentimento
de pessoa identificável · `B-CAP` captura/picture lock · `B-ROT` aprovação de
roteiro. `B-DIR` baixado pela assinatura. `B-DUR` reclassificado como revisão
pós-render (§4) e não consta mais como bloqueio.

| Filme | Status | Bloqueios remanescentes |
|---|---|---|
| Puressência | `PENDENTE_PRON` | B-PRON |
| Ali Love | `PENDENTE_PRON` | B-PRON |
| AB Motion | `PENDENTE_PRON` | B-PRON |
| Climbex | `PENDENTE_PRON` | B-PRON |
| Planning institucional | `PENDENTE_PRON` | B-PRON |
| Impacto Digital | `PENDENTE_PRON` | B-PRON |
| AB Cream | `PENDENTE_PRON` | B-PRON, B-ROT |
| Prince Andre | `BLOCKED` | B-PRON, B-CONC |
| Trajetum | `BLOCKED` | B-PRON, B-CONC |
| Planning tutorial | `BLOCKED` | B-PRON, B-CAP |
| Dr. Brenno | `BLOCKED` | B-PRON, B-CONC, B-CONS |

`PENDENTE_PRON` significa: confirmada a pronúncia daquele filme, ele vira
`READY_FOR_PRIVATE_RENDER` sem nenhuma outra decisão. São **seis filmes** nessa
condição, mais o AB Cream com o aceite do roteiro V2.

Nenhum filme está `READY_FOR_PRIVATE_RENDER` neste momento, porque nenhuma
pronúncia foi confirmada ainda. Esse é o único item que separa a maioria da fila
do primeiro render privado.

**Por que os quatro últimos seguem `BLOCKED`:** os direitos de mídia não validam
afirmação. Prince Andre e Trajetum fazem afirmações de percurso e resultado;
Dr. Brenno cita credenciais e usa pessoa identificável; o tutorial mostra uma
interface que ainda não tem picture lock. Isso é checagem de conteúdo, não
permissão de imagem — segue aberto mesmo com tudo assinado.

## 9. Ordem recomendada de produção — V2.1

Reordenada pela distância até o render, não mais pelo risco factual: os que
dependem só de pronúncia vêm primeiro.

**Onda 1 — só pronúncia separa do render privado**

1. AB Cream — menor risco factual; asset cobre a shot list; precisa também do aceite do roteiro V2.
2. Impacto Digital — manifesto curto, voz-over; confirmar `Pulso ID` com a Impacto.
3. Puressência — manifesto abstrato; depende das pronúncias das cinco marcas citadas.
4. Climbex — processo/BPM, sem pessoa identificável.
5. Planning institucional — confirmar `Sankhya` e `BPO` em fonte oficial.
6. AB Motion — voz-over; roda sem o before/after enquanto o case do cliente não estiver confirmado.
7. Ali Love — acervo real autorizado disponível; sem avatar, sem presenter.

**Onda 2 — dependem de checagem de conteúdo, não de imagem**

8. Trajetum — depois de conceito e claims aprovados.
9. Prince Andre — acervo liberado; falta aprovar o conceito das nove voltas e o que a locução afirma.
10. Planning tutorial — depois do picture lock da interface.
11. Dr. Brenno — depois de claims, credenciais e consentimento de pessoa identificável.

## 10. Entrega esperada do Claude sem acesso de geração

Claude pode devolver, sem tocar HeyGen:

- revisão editorial por roteiro;
- tabela de duração/palavras;
- shot list refinada;
- pronúncias marcadas como confirmadas ou pendentes;
- `CRITICAL ON-SCREEN TEXT` consolidado;
- mapa asset → cena;
- prompts finais 16:9;
- lista de perguntas realmente bloqueantes;
- ordem de renders com estimativa de créditos somente depois de ler a conta conectada;
- relatório `READY_FOR_PRIVATE_RENDER` ou `BLOCKED`, por filme.

Nenhum item deve ser marcado `READY_FOR_PRIVATE_RENDER` enquanto identidade, direitos, pronúncia ou roteiro estiverem pendentes.
