# Handoff — Ali Love e Prince Andre

> Escrito para quem assumir a execução: Codex, Claude Code local, ou pessoa.
> Contém o que está feito, o que trava, o padrão a aplicar e as regras que não
> podem ser quebradas. Autossuficiente — não precisa da conversa anterior.

---

## 0. Estado das três frentes

| Frente | Situação | Quem toca agora |
|---|---|---|
| **Pop** | Pop Casa (cliente) e Pop Campanhas (interna) entregues e testadas | Codex |
| **Ali Love** | site existe; refação em padrão internacional **não iniciada** | esta frente |
| **Prince Andre** | EPK esqueleto; refação **não iniciada** | esta frente |

Pop Campanhas publicada com palco 3D, lâmina e as duas planilhas do Mercos.
Fonte e script de montagem em `produtos/popcom/fonte/`.

---

## 1. O que trava, e por quê importa

O pedido é **refazer a versão atual sem alterar nada de texto**. Isso tem uma
dependência dura: a versão atual.

Os dois materiais estão fora de alcance de qualquer sessão em nuvem:

| Material | Onde está |
|---|---|
| Site Ali Love | `Projects/alilove/` |
| EPK Prince Andre | `Projects/andre-corporate/out/prince-andre/epk/` |

Sem o texto, refazer vira **escrever copy nova** — o oposto do pedido, e num
site de cliente. Por isso a extração vem antes de qualquer linha de código.

### Como destravar em uma colagem

No Claude Code **local**, que tem os arquivos:

```
Percorra Projects/alilove/ e Projects/andre-corporate/out/prince-andre/epk/.
Para cada página, me devolva um markdown com:

1. A rota (ex.: /film, /epk)
2. TODO o texto visível, verbatim, na ordem em que aparece — títulos,
   parágrafos, legendas, botões, rodapé. Não resuma, não corrija, não traduza.
3. Os créditos oficiais exatamente como estão
4. A lista de imagens e vídeos com caminho e dimensão
5. O bloco de tokens do CSS: cores, fontes, escalas
6. Metadados: title, description, og:image

Um arquivo por frente. Só o conteúdo, sem comentários seus.
```

Com esses dois markdowns a refação começa imediatamente e o texto fica intacto
por construção — ele é copiado, não reescrito.

---

## 2. O que "padrão máximo internacional" significa aqui

Não é adjetivo. É esta lista, que já foi executada e validada na Pop Campanhas
e deve valer para as duas frentes:

**Render e movimento**
- Three.js para cena 3D; ciclorama radial quando houver órbita — a curva sobe
  pela distância ao centro, não pela profundidade, senão a câmera cruza a borda
- Iluminação de três pontos, sombras reais, tone mapping ACES
- Motion para revelação e transição; **toda** trilha desligada sob
  `prefers-reduced-motion`, e a cena carrega parada
- Dolly zoom onde a narrativa pedir, não como efeito solto

**Saídas**
- Imagem: PNG do quadro
- Vídeo: WebM gravado do próprio canvas via `captureStream` + `MediaRecorder`;
  sem biblioteca de codificação, sem servidor
- A gravação liga o movimento pela duração e devolve o estado anterior no fim

**Página**
- Tokens de cor em `:root`, redefinidos em `prefers-color-scheme: dark` **e**
  em `[data-theme="dark"]`; nenhuma cor definida só dentro de media query
- `body` com fundo explícito — fundo transparente empresta o tema do hospedeiro
- Tipografia: display + texto + dados, com escala declarada
- Mobile 390 px sem overflow horizontal; alvos de toque de 44 px
- Zero erro de console

**Bibliotecas**
- Página publicada como artifact recusa script de CDN: as bibliotecas vão
  embutidas no arquivo. Three r149 UMD (608 KB) e Motion 11 UMD (64 KB)
  expõem `THREE` e `Motion` globais e funcionam inline
- Página gerada por script de montagem, com asserção em cada ponto de junção —
  fonte alterada falha alto em vez de gerar página quebrada

**Cuidado que custou tempo e vale registrar:** `typeof X` sobre um `const` ainda
não inicializado **lança** em vez de devolver `"undefined"`. Guardas escritas
com `typeof` na zona morta temporal derrubam o script inteiro.

---

## 3. Regras que não podem ser quebradas

Do briefing de 11/ago, e valem literalmente:

1. **Não misturar as marcas.** Nada de campanha do Prince Andre, widget Climbex,
   CTA comercial de outra marca ou peça institucional dentro do site do Ali Love.
   Verificado: a rota `/epk/` do `Projects/alilove/` é o EPK **do próprio Ali
   Love** e não cita Prince Andre. A separação está intacta — manter assim.
2. **Domínio do Ali Love é `www.alilove.world`.** O `CENTRAL_DE_CONTROLE.md`
   ainda lista `alilove.vercel.app` e se declara canônico. Está errado nesse
   ponto. Conferir `Projects/alilove/src/content/site.ts`, não a CENTRAL.
3. **São dois projetos Vercel do Ali Love:** `alilove` (site oficial) e
   `alilove-vinyl` (peça separada). Confirmar em qual se está mexendo.
4. **`alilove.world` nunca é desligado.** Se migrar, redirecionamento 301.
5. **Não publicar.** Página gêmea é para aprovação, não para produção.
6. **Não editar `CENTRAL_DE_CONTROLE.md`.** Divergência vira pendência.

### Prince Andre: publicação está bloqueada

O bloqueio **B1** continua de pé: não há domínio canônico definido, e o acesso
à conta GoDaddy de `princeandre.com` está perdido. O EPK hoje vive em
`/prince-andre/epk/` dentro de `andreboliveiramotion.com` — domínio da AB
Motion, não do artista — com `noindex, nofollow` e fora do sitemap.

Consequência prática: **refazer pode; publicar não.** A gêmea de aprovação é o
entregável possível hoje. Definir o domínio é decisão do Amós, e vem antes de
qualquer publicação.

---

## 4. Entregáveis de música — bloqueado, não esquecido

O bloqueio **B3** vale aqui: `MIX_MASTER_ORIGINALS.md` não foi localizado.
Acredita-se estar no volume `MAC Amos`.

A regra do briefing §12 é explícita: sem esse arquivo, **registrar o bloqueio e
não inventar processo**. Não deduzir cadeia de masterização, não assumir
formatos de entrega, não escrever especificação de áudio por analogia.

O que destrava: montar o `MAC Amos` e rodar a varredura de
`ferramentas/varredura/` — o garimpo procura esse nome em todos os volumes.
Se aparecer, B3 cai e os entregáveis de música saem do bloqueio.

Enquanto isso: material audiovisual do **Fernando Bento** também segue travado
por **B4** — clipes inventariados, sem seleção nem autorização.

---

## 5. Ordem de execução

1. **Extrair o texto** das duas frentes (§1). Nada começa antes.
2. **Ali Love primeiro.** É site de cliente com data e domínio vivo; tem mais a
   perder e mais a ganhar.
3. Refazer com o padrão do §2, **texto copiado verbatim**.
4. Gêmea de aprovação lado a lado com a atual — a comparação é o entregável.
5. **Prince Andre depois**, mesma técnica, ciente de que publicação está travada
   por B1.
6. Música só depois que B3 cair.

---

## 6. Critérios de encerramento

- [ ] Texto das duas frentes extraído verbatim e conferido contra o original
- [ ] Ali Love refeito, sem uma palavra alterada
- [ ] Gêmea de aprovação publicada em endereço privado, produção intocada
- [ ] `www.alilove.world` respondendo como antes, sem deploy novo
- [ ] Nenhuma marca cruzada entre as frentes
- [ ] Prince Andre refeito, não publicado, B1 registrado como pendente
- [ ] Música: B3 registrado, nenhum processo inventado

---

*Nenhum deploy, envio ou alteração financeira foi feito. Nenhum arquivo
existente foi apagado, movido ou reescrito. `CENTRAL_DE_CONTROLE.md` intocado.*
