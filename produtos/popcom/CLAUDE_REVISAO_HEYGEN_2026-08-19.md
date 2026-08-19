# Revisão offline do pacote HeyGen — 11 filmes

**Revisado:** `HEYGEN_PREPRODUCTION_PACK_CLAUDE_2026-08-19.md`, commit `808a7c2`
**Data:** 19/08/2026
**Gate respeitado:** nenhuma conexão, nenhum render, nenhum crédito consumido.
O conector HeyGen segue pedindo autorização e esta sessão não executa OAuth.
Revisão feita apenas sobre o texto.

---

## 1. Achado que muda a produção inteira

**A duração não fecha em nenhum dos onze filmes, e a instrução universal manda
a máquina preencher o buraco inventando.**

Os word counts declarados no pacote estão corretos — conferi um a um por
contagem programática, e todos batem. O problema não é a contagem: é a relação
entre ela e o tempo-alvo.

Narração institucional em português do Brasil corre entre **140 e 155 palavras
por minuto**. Abaixo disso arrasta; acima atropela. Com os textos atuais:

| Filme | Palavras | Fala em ~145 ppm | Alvo | Vazio | Ritmo implícito |
|---|---:|---:|---:|---:|---:|
| Puressência | 106 | 44 s | 60 s | **16 s** | 106 ppm |
| Ali Love | 111 | 46 s | 75 s | **29 s** | 89 ppm |
| Prince Andre | 98 | 41 s | 60 s | **19 s** | 98 ppm |
| AB Motion | 88 | 36 s | 45 s | 9 s | 117 ppm |
| AB Cream | 57 | 24 s | 30 s | 6 s | 114 ppm |
| Climbex | 95 | 39 s | 60 s | **21 s** | 95 ppm |
| Trajetum | 93 | 38 s | 60 s | **22 s** | 93 ppm |
| Dr. Brenno | 119 | 49 s | 75 s | **26 s** | 95 ppm |
| Planning institucional | 97 | 40 s | 60 s | **20 s** | 97 ppm |
| Planning tutorial | 185 | 77 s | 120–180 s | **43–103 s** | 74 ppm |
| Impacto Digital | 79 | 33 s | 45 s | 12 s | 105 ppm |

Sozinho, isso seria só um ajuste de montagem. O que transforma em risco é a
regra universal do §4, aplicada a **todos** os prompts:

> *You have full creative freedom to expand, elaborate, add examples, and fill
> the duration naturally. Do not pad with silence or pauses.*

Essa frase convive, no mesmo prompt, com:

> *Do not invent facts, numbers, credentials, clients, media coverage, awards
> or product claims.*

**As duas não podem valer ao mesmo tempo com 30% de tempo vazio.** Mandar
"elaborar, dar exemplos e preencher a duração" e proibir "silêncio ou pausa" é
instruir a máquina a produzir conteúdo novo. E o conteúdo novo mais provável é
justamente exemplo, número e afirmação — as três coisas proibidas.

O risco não é uniforme. Ele é maior exatamente onde dói mais:

- **Planning** — contabilidade e tributário. Exemplo inventado vira orientação fiscal errada.
- **Dr. Brenno** — credencial, instituição, publicação. Exemplo inventado vira currículo falso.
- **AB Cream** — regulatório. Exemplo inventado vira claim de eficácia.
- **Trajetum** — carreira. Exemplo inventado vira promessa de resultado.

### Correção proposta

Duas mudanças, e nenhuma delas exige reescrever roteiro agora.

**Primeira — trocar a frase do §4.** Substituir por algo que preencha tempo com
imagem, não com texto:

```text
This script is the complete and final narration. Do not add, expand,
elaborate, paraphrase or invent any spoken content. If the narration is
shorter than the target duration, fill the remaining time with motion,
b-roll, typography and music beds — never with additional speech. Silence
under music is acceptable and preferred over invented content.
```

**Segunda — decidir por filme:** ou o alvo de duração desce para o que o texto
realmente fala, ou o roteiro é ampliado **por uma pessoa**, com o mesmo rigor de
verdade. Não deixar a diferença para a máquina resolver.

Para os quatro filmes de risco alto, a recomendação é descer o alvo. Um
institucional de 44 segundos bem montado é melhor que um de 60 com 16 segundos
de invenção.

---

## 2. Situação por filme

Legenda: **B-PRON** pronúncia pendente · **B-DIR** direitos/mídia real ·
**B-CONS** consentimento · **B-CONC** conceito ou marca não aprovados ·
**B-DUR** vazio de duração acima de 25%

| # | Filme | Palavras | Fala | Alvo | Status | Bloqueios |
|---|---|---:|---:|---:|---|---|
| 1 | Puressência | 106 | 44 s | 60 s | `BLOCKED` | B-PRON, B-DUR |
| 2 | Ali Love | 111 | 46 s | 75 s | `BLOCKED` | B-DIR, B-PRON, B-DUR |
| 3 | Prince Andre | 98 | 41 s | 60 s | `BLOCKED` | B-DIR, B-CONC, B-PRON, B-DUR |
| 4 | AB Motion | 88 | 36 s | 45 s | `BLOCKED` | B-PRON, B-DIR (cases) |
| 5 | AB Cream | 57 | 24 s | 30 s | `BLOCKED` | B-PRON |
| 6 | Climbex | 95 | 39 s | 60 s | `BLOCKED` | B-PRON, B-DUR |
| 7 | Trajetum | 93 | 38 s | 60 s | `BLOCKED` | B-PRON, B-CONC, B-DUR |
| 8 | Dr. Brenno | 119 | 49 s | 75 s | `BLOCKED` | B-PRON, B-CONC, B-DUR |
| 9 | Planning institucional | 97 | 40 s | 60 s | `BLOCKED` | B-PRON, B-DUR |
| 10 | Planning tutorial | 185 | 77 s | 120–180 s | `BLOCKED` | B-PRON, B-DIR (captura), B-DUR |
| 11 | Impacto Digital | 79 | 33 s | 45 s | `BLOCKED` | B-PRON, B-DUR |

**Nenhum filme está `READY_FOR_PRIVATE_RENDER`.** Isso não é excesso de zelo —
é a regra do próprio pacote, §10: nada é READY enquanto identidade, direitos,
pronúncia ou roteiro estiverem pendentes. E o §5 é ainda mais direto: *"Não
enviar nenhum job enquanto houver item de pronúncia obrigatório sem
confirmação."*

---

## 3. A pronúncia é o gargalo — e é o mais barato de resolver

Onze dos treze termos do glossário estão sem confirmação, e três deles são
**hipóteses declaradas** sobre nomes próprios: `Climbex`, `Trajetum` e
`Brenno Castrillon`. Errar o nome da própria marca num institucional é o tipo
de defeito que não se corrige na edição.

Lido ao pé da letra, o §5 bloqueia os onze filmes de uma vez, porque
*Puressência*, *AB Motion* e *AB Cream* aparecem em quase todos.

**Proposta:** trocar a regra global por uma regra por filme — só bloqueia o
filme a pronúncia que é **falada nele**. Fica assim:

| Confirmar | Destrava |
|---|---|
| Puressência | 1, e libera a marca nos demais |
| Climbex | 6 |
| Trajetum | 7 |
| Brenno Castrillon + escolha de `XAI` | 8 |
| Sankhya + ICMS-ST | 9, 10 |
| Pulso ID | 11 |
| AB Motion, AB Cream | 4, 5 |

**Uma conversa de dez minutos com o proprietário destrava sete filmes.** É o
maior retorno por esforço de todo o pacote, e não custa crédito nenhum.

Ali Love e Prince Andre continuam bloqueados depois disso, por direitos.

---

## 4. Ajustes editoriais

### AB Cream — o mais importante

A narração **fala o disclaimer**:

> *"O case explora materialidade, luz, tipografia e experiência sem inventar
> fórmula, registro, certificação ou eficácia."*

Isso é instrução de compliance recitada como texto de filme. Ninguém narra o
que não vai dizer. Além de soar defensivo, chama atenção justamente para a
dúvida que se quer evitar.

O aviso já existe onde deve existir — no `CRITICAL ON-SCREEN TEXT`
(`SEM CLAIMS DE FÓRMULA OU EFICÁCIA`). Tirar da locução e deixar só na tela.

Substituição sugerida, mesma extensão:

> *"O case explora materialidade, luz, tipografia e experiência: como um sistema
> visual dá presença a uma ideia."*

### Ali Love — a narração descreve o próprio filme

> *"Primeiro, um pulso no escuro. Depois, um sulco que se abre como portal."*

Isso é shot list falada em voz alta. O espectador está **vendo** o pulso e o
sulco; ouvir a descrição do que se vê enfraquece as duas camadas. Num trailer de
campanha artística, a locução deveria dizer o que a imagem **não** diz.

O trecho seguinte já faz isso bem — *"A campanha não promete uma fuga. Ela
lembra por que ainda dançamos juntos."* Recomendo cortar as descrições de plano
e ampliar essa veia. Também resolve parte do vazio de 29 s: menos palavras
descritivas, mais respiro musical, que é o que o próprio pacote pede
("poético; espaço para música/motion").

### Prince Andre — nove itens numa frase só

> *"origem, repertório, risco, silêncio, aprendizado, presença, colaboração,
> transformação e futuro"*

Nove substantivos abstratos em sequência, ~8 s de lista. Ninguém retém. E o
`CRITICAL ON-SCREEN TEXT` não os traz, então também não aparecem escritos.

Melhor: falar três, mostrar os nove em tela conforme os círculos entram. A
imagem carrega a lista; a voz carrega o sentido.

### Demais filmes

Puressência, AB Motion, Climbex, Trajetum, Dr. Brenno, Planning e Impacto estão
editorialmente sólidos. Aberturas fortes e específicas — *"Automação sem processo
só acelera o problema"*, *"Motion não começa no efeito. Começa na decisão"*,
*"Presença digital não é volume"*. O hook nos primeiros cinco segundos, que o §4
exige, está cumprido em todos.

O tutorial da Planning é o melhor texto do pacote em rigor: avisa que não
transmite dados, não substitui análise profissional, e alerta contra dado
sensível — três vezes, nos lugares certos.

---

## 5. Validação asset → cena

| Filme | Asset | Cobre a shot list? | Observação |
|---|---|---|---|
| Puressência | `puressencia-ecossistema-material-v1.png` | parcial | um still para 5 planos; os 4 portais e o mapa do hub são motion a construir |
| Ali Love | `ali-love-cosmic-portal-v1.png` | **não** | cobre planos 1–2; os planos 3–4 exigem acervo real inexistente |
| Prince Andre | `prince-andre-nine-turns-v1.png` | **não** | cobre 1–2; planos 3–4 exigem acervo real |
| AB Motion | `ab-motion-studio-v1.png` | parcial | plano 3 (before/after) precisa de case real autorizado |
| AB Cream | `ab-cream-product-v1.png` | **sim** | único filme com cobertura completa por um asset |
| Climbex | `climbex-bpm-operations-v1.png` | parcial | AS-IS/TO-BE são motion graphics, não o still |
| Trajetum | `trajetum-career-advisory-v1.png` | parcial | diagramas de caminho a construir |
| Dr. Brenno | `dr-brenno-xai-system-v1.png` | parcial | série temporal e contribuição de variáveis são motion |
| Planning inst. | 4× `planning-*-v1.png` | **sim** | melhor proporção asset/plano do pacote |
| Planning tutorial | captura da interface | **não** | depende de preview existente e com picture lock |
| Impacto | `impacto-digital-pulse-team-v1.png` | parcial | as 4 dimensões são motion |

**Padrão:** um still por filme cobre em média dois dos cinco planos. Não é
defeito do bundle — os planos restantes são motion graphics, e é isso que
deveria preencher o vazio de duração em vez de fala inventada. Os dois casos que
realmente faltam material são Ali Love e Prince Andre, e é exatamente onde o
bloqueio de direitos já existe.

---

## 6. Verificações de regra

| Regra | Resultado |
|---|---|
| Climbex ausente de Ali Love | ✅ e o prompt traz a proibição explícita |
| Climbex ausente de Prince Andre | ✅ limpo |
| Sem avatar fabricado para os artistas | ✅ os dois prompts proíbem nominalmente |
| Lockup `LOVE ALWAYS WINS / Ali Love × AB Motion` | ✅ consistente entre narração e tela |
| AB Cream sem claim regulatório | ⚠️ cumprido, mas via disclaimer falado — ver §4 |
| Consentimento preenchido | ❌ nenhuma ficha preenchida; só bloqueia filme com pessoa identificável |
| Prince Andre sem CTA de domínio público | ✅ termina em `PRIVATE REVIEW`, coerente com B1 |

**Nota para leituras futuras:** uma busca por "climbex" **encontra** a palavra
dentro do filme do Ali Love. É a frase que proíbe seu uso, no prompt visual.
Não confundir com violação.

---

## 7. O que fazer, em ordem

1. **Corrigir a frase do §4** que autoriza expandir e preencher duração. É a
   única mudança que protege os onze filmes de uma vez.
2. **Confirmar as pronúncias** numa conversa. Destrava sete filmes.
3. **Decidir a duração** de cada filme: descer o alvo ou ampliar o roteiro com
   revisão humana.
4. **Aplicar os três ajustes editoriais** — AB Cream, Ali Love, Prince Andre.
5. **Começar por AB Cream e Impacto Digital** quando as pronúncias caírem: menor
   vazio de duração, sem pessoa identificável, e no AB Cream o asset cobre a
   shot list inteira. A ordem do §9 sugere Planning primeiro, mas Planning tem o
   maior risco de invenção justamente por ser tributário — melhor depois da
   correção do §4 estar provada em filme de baixo risco.
6. **Ali Love e Prince Andre por último**, como o pacote já prevê.

---

## 8. Perguntas realmente bloqueantes

1. Pronúncia de `Climbex`, `Trajetum` e `Brenno Castrillon` — hoje são hipóteses.
2. `XAI` é lido como sigla ou por extenso?
3. Cada filme desce para a duração que o texto fala, ou o roteiro será ampliado
   por pessoa?
4. Existe bundle de mídia real autorizada de Ali Love e Prince Andre? Sem ele os
   dois filmes não saem do bloqueio.
5. Os cases do AB Motion têm autorização de uso dos clientes?
6. O preview da Planning já está com picture lock para ser capturado no tutorial?

---

*Nenhum render, avatar, upload, conexão ou crédito HeyGen foi utilizado.*
