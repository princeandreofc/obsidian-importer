---
name: analise-conteudo
description: Analisa links de conteúdo social (Instagram, TikTok, YouTube, X, LinkedIn) e devolve leitura estruturada — números reais, mecânica de alcance, gancho, e o que dá para implementar nas marcas da holding. Aceita um link ou dezenas de uma vez; com mais de um, cruza o conjunto atrás de padrão. Use quando o usuário colar link de vídeo ou post, pedir análise de conteúdo, de concorrente, de referência criativa, ou perguntar por que algo viralizou.
---

# Análise de conteúdo

Lê o que é público e verificável, separa isso do que não dá para ler, e termina
no que interessa: **o que implementar**.

## Regra que não se quebra

**Não invente o que não leu.** Transcrição, ritmo de corte, timing de gancho e
layout visual estão dentro do arquivo de vídeo, não na página. Buscar a página
devolve conta, data, legenda e números — nada mais.

Se não leu, vai para a seção `Não verificado`. Análise inventada é pior que
análise ausente, porque parece igual à verdadeira.

## Processo

1. `WebFetch` em cada link. Peça explicitamente: conta, data, legenda completa,
   contagem de curtidas e comentários, meta tags `og:`.
2. Se a página não devolver conteúdo (muro de login, post privado, removido),
   registre e siga — não tente contornar nem preencher por dedução.
3. Rode a análise individual abaixo.
4. Com dois links ou mais, rode também a análise do conjunto.

## Saída por item

```
## <conta> — <data>
<url>

NÚMEROS
  Curtidas:     N
  Comentários:  N
  Proporção:    N%     ← comentários ÷ curtidas

MECÂNICA
  Por que alcançou. Nomeie o mecanismo, não o mérito.

GANCHO
  A primeira linha da legenda, verbatim, e por que ela para o dedo.

ESTRUTURA
  Como a legenda se organiza: promessa, prova, virada, chamada.

IMPLEMENTÁVEL
  1–3 itens concretos para Ali Love, Prince Andre, AB Motion, AB Cream,
  Climbex, Trajetum ou Puressência. Específico, não genérico.

NÃO VERIFICADO
  Lista do que não deu para ler.
```

### Como ler a proporção comentário/curtida

É o indicador mais revelador e quase ninguém olha.

**Leia sempre junto com o que a legenda pede.** O número sozinho classifica
errado — isso foi verificado em caso real, não é hipótese.

Primeiro identifique o pedido da legenda:

| A legenda pede | Então proporção alta significa |
|---|---|
| **comentário** ("comente X e eu envio") | mecânica de engajamento — pedágio |
| **save**, ou não pede nada | conversa real, marcação de colega, debate |

Só então aplique a faixa:

| Proporção | Com pedido de comentário | Com pedido de save, ou sem pedido |
|---|---|---|
| 1–3% | pedágio que não funcionou | orgânico normal |
| 4–10% | pedágio fraco | boa conversa |
| acima de 20% | pedágio funcionando | conteúdo altamente marcável ou polêmico |
| acima de 50% | o conteúdo é só o pedágio | raríssimo; investigue antes de concluir |

Caso que gerou esta regra: `gowtham_techie` teve 22% pedindo **save**, sem
pedágio nenhum — carrossel de ferramentas de dev, altamente marcável. A tabela
antiga o classificaria como mecânica de engajamento, e estaria errada.

### A regra do que é retido

Quando há pedágio, o resultado é proporcional ao que fica retido — não à
existência do pedágio.

| Reteve | Resultado observado |
|---|---|
| o método inteiro (kallawaymarketing) | 96% |
| um item de cinco, com quatro já entregues (grafikcem) | 1,7% |

Mesma técnica, 56× de diferença. Ao avaliar se vale replicar, pergunte **o que
sobra sem o comentário** — se sobra quase tudo, o pedágio não vai funcionar.

Proporção alta não significa conteúdo bom. Significa desenho eficiente, ou
assunto que provoca conversa. Diga qual dos três é — o usuário decide se quer
replicar.

## Saída do conjunto

Com vários links, o valor está no cruzamento:

```
# Conjunto — N itens

PADRÕES QUE SE REPETEM
  O que aparece em três ou mais. Só conte o que realmente se repete.

DISPERSÃO DE ENGAJAMENTO
  Tabela ordenada por proporção. Os extremos denunciam a mecânica.

FORMATOS
  Quais formatos dominam o conjunto.

O QUE VALE TESTAR
  Ranqueado por: impacto esperado × esforço. Máximo cinco.
  Cada linha diz em qual marca e por quê.

O QUE NÃO VALE
  Padrões que funcionam no nicho de origem e não transferem para as marcas
  da holding. Dizer o porquê poupa mais tempo que a lista anterior.
```

## Travas das marcas

Ao propor implementação, respeite o que já está decidido:

- **Ali Love** — nunca citar Climbex Global. Sem avatar fabricado nem presença
  sintética do artista. Lockup exato: `LOVE ALWAYS WINS / Ali Love × AB Motion`
- **Prince Andre** — sem avatar fabricado. Afirmação de percurso só com validação
- **AB Cream** — zero alegação de fórmula, registro, certificação ou eficácia
- **Nada de mistura de marca** — CTA de uma marca não entra em peça de outra
- **Puressência** é o único lugar onde as quatro convivem

## Quando o usuário quer o vídeo analisado de verdade

Para o que exige assistir, existem dois caminhos honestos, e vale oferecer:

1. Ele assiste e descreve os cortes, e a análise usa isso como fonte declarada
2. Ele baixa a legenda/transcrição e cola

Em ambos, marque a origem: `fonte: descrição do usuário` — para depois ninguém
confundir observação com dedução.
