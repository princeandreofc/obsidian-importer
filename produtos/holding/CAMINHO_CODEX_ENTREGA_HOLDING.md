# Caminho para o Codex — entrega da holding

**Data:** 19/08/2026
**Para:** Codex (execução), com Claude Code local como alternativa
**Origem:** lista de correções do proprietário sobre os deploys de produção de 19/08

---

## 0. Por que travou

O Codex não errou o diagnóstico. Ele acertou — inclusive a parte difícil: percebeu
que a repetição de "Processo e demonstração" é uma regra geradora de fallback, não
dezenas de textos independentes. Isso está certo.

O que travou foi outra coisa: **a lista de correções mistura, em um único bloco,
trabalho que só depende de código com trabalho que depende de arquivo que não
existe no disco.** Tratada como blob único, ela para no primeiro item impossível
e fica pedindo aprovação para prosseguir. Foi exatamente o que aconteceu no
"Step 1 / 6".

A correção de método é esta: **separar por dependência, não por site.** Tudo que
não precisa de asset novo é executável hoje, sem perguntar nada a ninguém. O que
precisa de asset vira pedido único e específico, feito uma vez.

---

## 1. Executável agora — nenhum asset novo necessário

Isto está pré-aprovado. Não peça confirmação item a item; execute, faça deploy em
preview, e reporte de uma vez.

| # | Item | Site | Natureza |
|---|---|---|---|
| 1 | Regra geradora do catálogo (fallback + duplicação) | AB Motion | código |
| 2 | Aplicar a lista de remoções do catálogo | AB Motion | config |
| 3 | `Fundamentos BPM` começar em 12 s | AB Motion | código |
| 4 | Enquadramento do vertical (cara cortada) | AB Motion | CSS |
| 5 | Logo e link da Puressência no bloco Origem e Legado | AB Motion | conteúdo |
| 6 | **Hub Puressência inteiro** — hoje vazio | Puressência | conteúdo |
| 7 | Trajetum até a paridade de conteúdo com a Climbex | Trajetum | conteúdo |
| 8 | CTA de mentoria 1:1 no Trajetum | Trajetum | conteúdo |
| 9 | Link Trajetum → mídia educacional da Climbex | Trajetum | conteúdo |

Nove itens. Nenhum depende de arquivo que não exista. O item 6 é o mais
importante da entrega inteira e é 100% escrita — está pronto no §4 abaixo.

## 2. Travado em asset ou decisão — não tente contornar

| Item | O que falta | Quem destrava |
|---|---|---|
| Filme principal de 5 min | o arquivo final e a legenda | proprietário |
| Filme de 5 min "no lugar errado" | dizer qual é o lugar certo | proprietário |
| EPK Prince Andre original | o pacote original com todos os assets | proprietário |
| Loja com preços reais | a tabela de preços aprovada | proprietário |
| Documentário Ali Love | o corte final autorizado | proprietário |
| Voz "Andre Professor" no HeyGen | conector autorizado + qual vídeo, qual voz | proprietário |

**Regra dura:** nenhum desses vira placeholder inventado. O texto atual de
pendência do filme ("arquivo final ainda não foi fornecido; nenhum vídeo
alternativo foi inventado ou publicado no lugar dele") está **certo** e deve
permanecer até existir arquivo real. Prometer filme inexistente é pior que
admitir a pendência.

---

## 3. Onda 0 — conserto do catálogo · faça isto primeiro

Não é o item mais importante, mas é o primeiro por um motivo prático: **enquanto
o catálogo estiver poluído, ninguém consegue revisar visualmente o resto.** Toda
captura de tela sai com dezenas de cards errados por cima do trabalho novo.
É uma hora de trabalho que devolve a capacidade de enxergar.

São dois bugs distintos na mesma tela, e vale não confundi-los:

**Bug A — descrição de fallback.** Todo card exibe a mesma frase, "Processo e
demonstração". Isso não são textos independentes: é um valor padrão aplicado
quando a descrição por item está ausente.

> Correção: **suprimir a descrição quando ela não existir**, em vez de preencher
> com o padrão. Card sem descrição é limpo; card com a mesma frase quarenta vezes
> parece defeito — e é. Escrever descrições reais só para os itens que
> sobreviverem à lista de remoções, depois.

**Bug B — emissão duplicada.** `Andre 01`, `Andre 02`, `Andre 03`, `Andre 04`,
`Andre 05`, `Andre 06`, `Brenno Blazer`, `Brenno Hero`, `Brenno Janela`,
`Brenno Preta`, `Brenno Verde` aparecem **duas vezes cada um**. O padrão de
nomenclatura (`Abmotion Desktop` / `Vertical`) indica a causa: o gerador emite
desktop e vertical como dois cards em vez de duas variantes do mesmo item.

> Correção: deduplicar pelo asset base e tratar orientação como variante interna
> do card, não como card próprio.

Conserte a regra geradora em `generate-service-library.mjs`. Não edite os cards
um a um — a regra errada os regenera na próxima execução.

### Lista de remoções, verbatim do proprietário

- `Brand System Motion · Abmotion Desktop`
- `Andre 01 · Andre`
- `V Media`
- `Talento Global · People`
- `Andre 06 · Andre` (a duplicata)
- `Brenno Janela · Mentoria` (a duplicata)
- `Brenno Verde · Mentoria` (a duplicata)
- `Ancora Feminina Recomendacao · Posters`

### Ajustes pontuais

- `Fundamentos BPM` — iniciar em **12 s**. Use fragmento de mídia (`#t=12`) ou
  o parâmetro de início do player; não recorte o arquivo.
- `Brenno Apresentacao Vertical` — a face está cortada. É enquadramento, não
  arquivo: `object-fit: cover` com `object-position` ajustado para o terço
  superior. Confira nos três breakpoints antes de dar por resolvido.

---

## 4. Onda 1 — Puressência, o hub · a entrega central

O proprietário foi explícito, duas vezes: *"esta é a árvore que comporta todos os
sites, o verdadeiro hub de toda holding, tem que ser o mais completo"* e
*"Puressência, que é o centro de toda a holding, não tem nada."*

Hoje `/puressencia/ab-cream/` está vazio. Isso é a maior lacuna da entrega — e é
inteiramente escrita, o que significa que **não há nada travando.**

### Estrutura obrigatória

Seis blocos. Cada marca tem seção própria, e as seções não se contaminam: o CTA
de uma marca nunca aparece dentro do bloco de outra.

1. **Abertura** — o que é a Puressência e por que as marcas convivem
2. **Ali Love** — a parceria
3. **Prince Andre** — a história
4. **Climbex Global e Trajetum** — as parcerias de operação e formação
5. **Lojas AB Motion e AB Cream** — com demo e link
6. **Mapa do hub** — quatro CTAs independentes

### Copy — use como está, ajuste só o que souber ser diferente

Escrita a partir dos materiais que o próprio proprietário já publicou. Onde falta
um dado, há um slot marcado `[…]` — **preencha ou remova a frase; não invente.**

#### 1. Abertura

> **Uma origem, quatro linguagens.**
>
> A Puressência não é uma marca guarda-chuva que uniformiza o que abriga. É a raiz
> comum de projetos que escolheram caminhos próprios: música, imagem em movimento,
> operação e formação.
>
> O que se repete entre eles não é estética — é método. Verdade de origem, direção
> criativa e execução responsável. Cada projeto encontra sua linguagem. Cada
> linguagem mantém sua autoria.

#### 2. Ali Love — a parceria

> **Da Da On, e o que veio depois.**
>
> Em 2023, Prince Andre assinou com Ali Love a faixa *Da Da On*, lançada pela
> Hot Creations sob o catálogo HOTC204. O encontro não terminou no disco.
>
> A relação seguiu para o território visual, onde a AB Motion passou a construir
> o mundo de imagem da campanha **Love Always Wins** — acervo real, direção de
> movimento e respeito à origem, sem substituir a presença do artista por imagem
> fabricada.
>
> A campanha vive em endereço próprio, com identidade própria.
>
> `[CTA: Conhecer a campanha → www.alilove.world]`

> **Nota de execução, não publicar:** este bloco fala *sobre* a parceria a partir
> da Puressência. Ele não traz CTA da Climbex, do Trajetum ou de loja para dentro
> de si. A regra de não misturar marcas dentro do site do Ali Love continua
> valendo integralmente — e aqui, por simetria, o bloco do Ali Love também não
> recebe comércio de terceiros.

#### 3. Prince Andre — a história

> **Um disco é o começo, não o ponto final.**
>
> Prince Andre é a identidade artística de André Boliveira — produtor, compositor
> e criador visual brasileiro. O trabalho reúne 230 letras originais e um arquivo
> de cerca de 3.000 faixas, tratando som e imagem como um instrumento só.
>
> A prática atual desenvolve um modo de lançamento em que cada disco chega com seu
> próprio mundo de imagem em movimento, produzido por pipeline independente e
> construído para continuidade — não para uma campanha isolada.
>
> `[CTA: Ver o EPK → /prince-andre/epk/]`

#### 4. Climbex Global e Trajetum — operação e formação

> **O que sustenta o trabalho criativo.**
>
> Nem tudo na holding é imagem. A **Climbex Global** trata de processos, clareza
> operacional e transformação responsável — o modo de organizar operação,
> conhecimento e execução que sustenta o resto.
>
> O **Trajetum** cuida do outro lado da mesma moeda: formação, progressão de
> carreira e atuação consultiva. Uma jornada contínua entre decisões de formação,
> desenvolvimento profissional e advisory.
>
> As duas frentes se encontram na educação: o **Curso Fundamentos de BPM** nasce
> na Climbex e conduz ao Trajetum.
>
> `[CTA: Climbex Global → climbexglobal.com]`
> `[CTA: Trajetum → trajetum.com]`

#### 5. Lojas AB Motion e AB Cream

> **Do estúdio ao produto.**
>
> A **AB Motion** transforma estratégia em imagem em movimento — o estúdio que
> produz campanhas, sistemas visuais e material de lançamento.
>
> A **AB Cream** é um estudo demonstrativo de marca, produto e materialidade:
> como um sistema visual dá presença a uma ideia.
>
> `[CTA: Loja AB Motion → …]`
> `[CTA: AB Cream → …]`

> **Trava obrigatória na AB Cream:** zero afirmação de fórmula, registro,
> certificação ou eficácia. É estudo de marca e materialidade, não produto com
> alegação. Qualquer frase que sugira efeito, aprovação regulatória ou composição
> sai antes do deploy.
>
> **Demo:** o proprietário pediu "com demo". Se o material de demonstração
> existir, use-o. Se não existir, use o asset `ab-cream-product-v1.png` como peça
> de estúdio, sem legenda que o apresente como produto à venda — e registre a
> pendência. Não fabrique demonstração de produto.

#### 6. Mapa do hub

Quatro portas, uma por marca, sem fundir identidades. O mapa é o fecho da página
e o único ponto onde as quatro convivem visualmente.

### Volume

O proprietário definiu o padrão em uma frase: *"todos os sites têm que ter a mesma
quantidade da Climbex ou mais em conteúdo."* A Climbex tem **37 páginas**, número
do relatório do próprio Codex. Esse é o alvo mensurável — e sendo a Puressência o
hub, ela deve ficar **acima** dele, não igual.

---

## 5. Onda 2 — Trajetum até a paridade

Diagnóstico do proprietário: *"site está curto e genérico."*

- Alvo de volume: **37 páginas ou mais**, mesmo padrão editorial da Climbex
- Aplicar a skill `padrao-climbex-sites`, que existe exatamente para isso
- **CTA de mentoria 1:1** — item pedido explicitamente, hoje ausente
- **Link direto para a mídia educacional da Climbex**, não para a home
- Manter a estrutura Jornada / Frentes / Instituto / Fundador que já existe

**Limite externo preservado:** `trajetum.com` continua apontando ao Squarespace
com "Em breve". A troca de DNS é decisão do proprietário e **não deve ser feita
por iniciativa da execução** — publique em `trajetum.vercel.app` e deixe o DNS
como está.

---

## 6. Onda 3 — EPK Prince Andre

O proprietário registrou que esta é a falha mais visível: *"Codex não conseguiu
entregar o EPK Prince Andre."*

O EPK atual já tem estrutura boa — statement, release selecionado, escuta privada,
sistema visual, biografia, imagens de imprensa, contato. O que falta não é
arquitetura, é **material**: *"inserir EPK original, todos os assets, fazer deploy."*

**Pedido único ao proprietário, e o mais específico possível:**

1. Onde está o pacote do EPK original — caminho ou link
2. As imagens de imprensa em resolução de download (hoje os botões existem, os
   arquivos não)
3. Os links privados de áudio das três faixas, ou a confirmação de que seguem
   pendentes
4. O filme de artista de 60–90 s, ou a confirmação de que segue em picture lock

Enquanto 3 e 4 não chegarem, os marcadores `Pending` e `Picture lock pending`
**ficam como estão** — são honestos e não prometem o que não existe.

**Sobre as afirmações do EPK:** 230 letras, ~3.000 faixas, HOTC204/2023 são
declarações do próprio artista sobre si mesmo, já publicadas por ele. Carregue-as
**verbatim**. Isso não é inventar fato — é preservar o que o titular afirmou. Não
adicione número, prêmio, cobertura de imprensa ou cliente que não esteja no
original.

---

## 7. Onda 4 — Ali Love, documentário

Depende do corte final autorizado. Os direitos de mídia foram assinados, com
autorização para prévia e validação final — mas **assinatura libera uso, não
entrega arquivo.** O acervo real precisa ser selecionado e depositado antes de
qualquer montagem.

Regras que não mudam com a assinatura:

- Sem avatar fabricado e sem presenter sintético para o artista
- Lockup exato: `LOVE ALWAYS WINS / Ali Love × AB Motion`
- **Climbex Global nunca aparece** em filme, página, metadata ou lockup do Ali Love
- `www.alilove.world` nunca sai do ar; se migrar, 301

---

## 8. Onda 5 — HeyGen

**Estado real, sem rodeio:** o conector HeyGen não está autorizado nesta sessão.
Nenhuma sessão em nuvem pode conectá-lo sozinha — a autorização é feita pelo
proprietário em `claude.ai → Configurações → Conectores`. Sem isso, nada de
HeyGen executa, aqui ou no Codex.

O que já está pronto e esperando: `produtos/popcom/HEYGEN_PREPRODUCTION_PACK_CODEX_CLAUDE_V2_2026-08-19.md`,
com onze roteiros travados, prompts finais, shot lists e gate de pronúncia por filme.

**Estado dos onze filmes:** seis dependem só de confirmação de pronúncia para
virar `READY_FOR_PRIVATE_RENDER`. Um único item separa mais da metade da fila do
primeiro render.

### A troca de voz pedida

*"O áudio deve ser trocado no HeyGen, a voz Andre Professor deve ser colocada.
Este vídeo deve estar em Climbex Global"* — e, em outra linha, *"deve ser vídeo
principal em Climbex Global."*

Para executar, faltam três respostas curtas:

1. **Qual vídeo exatamente** — há mais de um `Processo e demonstração · Áudio PT`
   no catálogo, e a instrução aparece duas vezes com destinos diferentes
   (estar na Climbex × ser o principal da Climbex). São o mesmo vídeo ou dois?
2. **Qual voz** — "Andre Professor" é voz já existente na conta HeyGen, ou
   precisa ser criada? Se precisa ser criada a partir da voz real do André,
   entra a trava de consentimento documentado.
3. **Autorização de crédito** — troca de áudio gera render novo e consome saldo.

---

## 9. O que só o Amós pode dar

Seis itens. Respondidos de uma vez, destravam tudo que hoje está parado.

- [ ] **Pronúncias:** `Puressência`, `Ali Love`, `Prince Andre`, `AB Motion`,
      `AB Cream`, `Climbex` — mais `Sankhya` em fonte oficial e `Pulso ID` com a
      Impacto. Destrava seis filmes.
- [ ] **Filme de 5 min:** o arquivo final, a legenda, e **em qual site ele deve
      estar** (a nota diz "no lugar errado" sem dizer o certo).
- [ ] **EPK Prince Andre:** caminho do pacote original e das imagens de imprensa.
- [ ] **Preços reais** da loja, para substituir "tabela em revisão".
- [ ] **HeyGen:** autorizar o conector, e responder as três perguntas do §8.
- [ ] **Acervo Ali Love:** selecionar e depositar a mídia real autorizada.

---

## 10. Regras que continuam valendo

Nada aqui foi flexibilizado pela ida à produção.

1. **Não inventar mídia, preço, biografia ou claim.** Pendência declarada é
   melhor que placeholder plausível.
2. **AB Cream:** zero afirmação de fórmula, registro, certificação ou eficácia.
3. **Climbex Global nunca aparece no Ali Love.**
4. **Sem avatar fabricado** para Ali Love ou Prince Andre.
5. **Não mexer em DNS.** `trajetum.com` fica no Squarespace; `planning.com` e
   `planning.com.br` são de terceiros e não se sobrescrevem; `andreboliveira.com`
   fica no projeto anterior.
6. **`www.alilove.world` nunca sai do ar.**
7. **Não apagar** original, sessão do Logic, `legado/`, foto ou mídia-fonte.
8. **Preview antes de produção.** Os deploys de 19/08 foram direto para produção
   em site de cliente vivo. Deu certo, mas o padrão seguro é publicar em preview,
   conferir, e só então promover.
9. **Não editar `CENTRAL_DE_CONTROLE.md`.** Divergência vira pendência registrada.

---

## Ordem, em uma linha

Onda 0 destrava a revisão visual. Onda 1 é a entrega que falta. As demais esperam
material — e material se pede uma vez, não a cada tentativa.

`catálogo → Puressência → Trajetum → EPK → Ali Love → HeyGen`
