# Pop Casa — loja completa e casa navegável

**Data:** 21/08/2026
**Objetivo comercial:** ferramenta de fechamento B2B. Piloto → Camargo e Pinheiro
→ MART. Um contrato desse porte viabiliza um ano de operação.

---

## 1. O que realmente fecha negócio B2B

Vale separar duas coisas que costumam ser confundidas, porque a diferença
decide onde gastar esforço.

**Realismo impressiona. Agência fecha.**

O comprador da Camargo e Pinheiro já viu render bonito. O que ele nunca viu é
**o catálogo dele** dentro de um ambiente que ele controla. O que muda a
conversa numa reunião:

| Alavanca | Peso no fechamento | Custo de produção |
|---|---|---|
| Ver o **próprio SKU** no ambiente | altíssimo | baixo — é dado, não render |
| **Trocar** produto e ver o cômodo reagir | altíssimo | médio |
| **Levar algo embora** — PDF/imagem da sala montada | alto | baixo, já existe no Pop |
| Navegação em primeira pessoa | alto | médio |
| Mais 20% de polígono | baixo | altíssimo |

A última linha é a armadilha. Perseguir realismo puro consome todo o orçamento
e entrega a alavanca mais fraca.

**O leave-behind é subestimado e barato.** O Pop Campanhas já exporta PNG e
WebM do canvas. Um botão que gera a **folha de proposta com a sala montada,
SKUs, quantidades e código** vale mais numa reunião que qualquer ganho de
render — porque sai da sala com o cliente e circula internamente na empresa
dele.

---

## 2. A dependência crítica: de onde vem o 3D dos produtos

**Este é o ponto que pode quebrar o projeto na frente da MART. Precisa ser
decidido antes de qualquer linha de código.**

O pedido é "giro sob o produto". Giro de 360° exige uma de três coisas:

| Origem | Existe hoje? | Risco |
|---|---|---|
| Modelo 3D real do produto | **provavelmente não** — catálogo é foto 2D | — |
| Sequência de fotos multiângulo | raro em catálogo comercial | — |
| 3D gerado por IA a partir de foto | tecnicamente possível | **inaceitável** |

**Por que a terceira opção está fora.** Gerar o verso de um sofá que só foi
fotografado de frente é **inventar a aparência de um produto real de um
fornecedor real**. O comprador da Camargo conhece o produto dele melhor que
nós. Ele vai girar, ver o encosto errado, e a reunião acaba ali — junto com a
credibilidade para as fases 2 e 3.

Não é preciosismo. É o mesmo princípio que já vale para AB Cream e Ali Love:
não fabricar o que não se tem.

### A saída: híbrido honesto

Duas camadas, com papéis distintos:

**Camada 1 — produto no ambiente.** Recorte da foto oficial em plano, com
sombra de contato real, iluminação da cena e escala correta. À distância de
navegação, isso lê como objeto. É como cenografia de vitrine funciona.

**Camada 2 — inspetor de produto.** Ao clicar, sai da navegação e entra num
visualizador dedicado. Aqui:
- SKU com 3D real disponível → **giro 360° verdadeiro**
- SKU só com foto → **ficha técnica rica**: zoom alto, variações de acabamento,
  medidas, material, ambientação. Sem giro falso.

O inspetor **nunca gira o que não pode girar**. E isso vira argumento de venda,
não desculpa: *"os SKUs com 3D completo giram; os demais entram assim que a
MART liberar os modelos"* — o que **cria a demanda da fase 3**.

### O que isso desbloqueia comercialmente

A conversa com a MART deixa de ser "contratem um site" e passa a ser: *"seu
catálogo já está navegável; para girar tudo precisamos dos modelos, ou de um
protocolo de fotografia que a gente especifica."* Isso é entrada por
necessidade demonstrada, não por proposta fria.

---

## 3. Arquitetura

### 3.1 Cômodos — a geometria não é o gargalo

Cômodo é caixa com aberturas. **O que vende realismo não é complexidade de
malha: é luz, material e escala.** Sala simples com proporção correta,
iluminação de ambiente, madeira e tecido com mapas reais e pós-processamento lê
como fotografia. Modelo complexo com luz chapada lê como videogame de 2005.

Ordem de investimento, do maior retorno para o menor:

1. **Escala correta** — pé-direito 2,70 m, porta 2,10 m, sofá 0,85 m de altura.
   Erro de escala destrói realismo instantaneamente e ninguém sabe dizer por quê
2. **Iluminação de ambiente** — HDRI de interior via `PMREMGenerator`, mais luz
   de janela direcional com sombra suave
3. **Material com mapas** — piso, parede, tecido, madeira. `MeshPhysicalMaterial`
4. **Pós-processamento** — bloom sutil, vinheta, grão, correção de tom
5. **Geometria** — molduras, rodapé, batente. Só depois de tudo acima

Opção a avaliar: o conector **SketchUp** disponível no ambiente pode gerar a
base dos cômodos. Vale testar antes de modelar à mão.

### 3.2 Navegação em primeira pessoa

- `PointerLockControls` + WASD no desktop
- **Mobile precisa de plano B real**: joystick virtual em tela, ou navegação por
  pontos de interesse (clica no chão, a câmera desliza até lá). Reunião B2B
  acontece em notebook, mas o cliente reabre no celular depois
- **Colisão simples** — caixas invisíveis nas paredes. Atravessar parede mata a
  ilusão mais rápido que textura ruim
- **Altura de olho travada em 1,60 m.** Câmera flutuando é o erro nº 1
- Transição entre cômodos com deslocamento suave, nunca corte seco

### 3.3 Performance — risco de reunião

**Se travar durante a apresentação, a apresentação morre.** Isso é risco
comercial, não técnico.

- Carregar **um cômodo por vez**; os vizinhos entram em segundo plano
- Orçamento de textura por cômodo, com compressão
- Instanciar o que repete
- **Teste obrigatório em notebook mediano**, não na máquina de quem desenvolve
- Modo de contingência: se o FPS cair, reduzir sombra e pós-processamento
  automaticamente, sem avisar

### 3.4 A loja

A casa é a vitrine; a loja é a operação.

- Catálogo completo com filtro por cômodo, linha, acabamento e faixa de preço
- Seleção monta o cômodo em tempo real
- Carrinho vira **proposta**, não checkout — B2B fecha com pedido, não cartão
- Exportação: folha de proposta com sala montada, SKUs, quantidade e código
- A planilha do Mercos que o Pop já lê continua sendo a fonte

---

## 4. As três fases, casadas com o plano comercial

| Fase | Para quem | Escopo | Depende de |
|---|---|---|---|
| **1 — Piloto** | seus clientes comerciais | hall + 3 cômodos, SKUs reais MART, navegação, inspetor, exportação | catálogo em `vendas/` |
| **2 — Camargo e Pinheiro** | parceiro MART | catálogo e marca deles, mais cômodos | aceite da fase 1 |
| **3 — MART** | fabricante | catálogo completo, 3D real dos produtos | modelos 3D da MART |

A fase 1 precisa ser **excelente e barata**, porque é trabalho especulativo. A
excelência vem de luz, escala e acabamento — não de volume de conteúdo. Três
cômodos impecáveis fecham mais que dez medianos.

---

## 5. O que preciso de você

**Bloqueante — o catálogo.** A pasta `vendas/` está no seu Mac; nenhuma sessão
em nuvem alcança. Preciso saber:

1. **Quantos SKUs** o catálogo oficial da MART tem
2. **Formato das imagens** — resolução, e se há fundo branco recortável
3. **Há algum modelo 3D?** `.obj`, `.fbx`, `.glb`, `.skp`, `.3ds`. Fabricante de
   móveis às vezes tem, para render de catálogo. **Se houver um só, muda o plano**
4. **Há foto multiângulo** de algum produto?
5. **Campos disponíveis** — medida, material, acabamento, cor, linha

Uma amostra de 5 SKUs com tudo que existe já me deixa começar.

**Decisão sua:** quais **3 cômodos** entram na fase 1. Sugestão pela densidade
de catálogo e apelo comercial: **sala de estar, quarto de casal, home office.**

---

## 6. O que dá para construir sem esperar nada

A casca não depende do catálogo. Enquanto a amostra não chega, dá para fechar:

- Cômodo com escala real, HDRI, materiais e pós-processamento
- Navegação em primeira pessoa com colisão e altura travada
- Inspetor de produto com giro, alimentado por placeholder
- Troca de cômodo
- Estrutura de dados de produto pronta para receber o catálogo real

Quando a amostra chegar, ela **entra na estrutura** — não é retrabalho.

---

## 7. Travas

1. **Não inventar aparência de produto.** Sem 3D gerado de produto real de
   fornecedor real. Sem giro falso
2. **Não publicar** sem autorização. Piloto é endereço privado
3. **Preço só do catálogo oficial.** Nada estimado ou arredondado
4. **Sem checkout.** B2B fecha por pedido; carrinho vira proposta
5. **Não apagar** nada de `vendas/` — leitura apenas
