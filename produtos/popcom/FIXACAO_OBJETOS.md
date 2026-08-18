# Por que os objetos flutuam — e o conserto

> Para aplicar no `index.html` da Pop Casa. Escrito para o Claude Code local,
> que tem o arquivo. Não vi o código — o que segue são as duas causas que
> produzem exatamente esse sintoma numa cena Three.js e o conserto de cada uma.

---

## São dois problemas diferentes, com a mesma aparência

**Um é geométrico:** a peça está no ar de verdade.
**O outro é perceptivo:** a peça está no chão, mas *parece* flutuando porque
não há sombra de contato. Resolver só o primeiro não mata a sensação.

Os dois precisam de conserto.

---

## Causa 1 — a origem do objeto não é a base dele

O erro clássico: ao soltar a peça, o código faz

```js
objeto.position.copy(ponto);          // ponto = onde o raio bateu no piso
```

Só que `position` é a **origem** da malha, que quase sempre está no **centro**.
Metade da peça vai para baixo do piso, metade para cima — e a peça parece
enterrada ou flutuando, dependendo do modelo.

### Conserto: assentar pela base

Mede a caixa da peça e desloca pela distância entre a origem e o ponto mais baixo.
Funciona qualquer que seja a origem do modelo.

```js
/** Assenta a peça de modo que a base dela encoste no ponto informado. */
function assentar(objeto, ponto){
  objeto.position.copy(ponto);
  objeto.updateMatrixWorld(true);

  const caixa = new THREE.Box3().setFromObject(objeto);
  const pesAteOrigem = objeto.position.y - caixa.min.y;   // origem → base

  objeto.position.y = ponto.y + pesAteOrigem;
}
```

Chame `assentar()` no soltar **e** ao final de cada arraste, nunca
`position.copy()` direto.

---

## Causa 2 — o raio não tem em que bater

Se a cena é uma foto de fundo sem geometria, o raycast não encontra piso e o
código cai num plano fixo em `y=0` ou na profundidade da câmera. Aí a peça fica
onde o mouse estava, no ar.

### Conserto: planos invisíveis de piso e parede

Um plano de colisão para cada superfície, alinhado à perspectiva da foto,
invisíveis mas presentes para o raycaster.

```js
const superficies = new THREE.Group();
scene.add(superficies);

// piso
const piso = new THREE.Mesh(
  new THREE.PlaneGeometry(40, 40),
  new THREE.MeshBasicMaterial({visible:false})
);
piso.rotation.x = -Math.PI/2;
piso.name = "piso";
piso.userData.ancoragem = "piso";
superficies.add(piso);

// parede do fundo
const parede = new THREE.Mesh(
  new THREE.PlaneGeometry(40, 20),
  new THREE.MeshBasicMaterial({visible:false})
);
parede.position.set(0, 10, -8);
parede.name = "parede-fundo";
parede.userData.ancoragem = "parede";
superficies.add(parede);
```

> Ajuste `position` e `rotation` até os planos coincidirem com a perspectiva da
> foto. Para conferir, troque `visible:false` por `wireframe:true` enquanto calibra.

---

## Cada produto conhece onde ele pousa

O puff vai no piso. O quadro vai na parede. Isso é dado do SKU, não regra solta:

```js
// no catálogo
{cod:"MRT-3062", nome:"Puff redondo bouclé cru",      ancoragem:"piso"},
{cod:"MRT-3055", nome:"Quadro decorativo 70×100",     ancoragem:"parede"},
{cod:"MRT-3007", nome:"Luminária de piso arco latão", ancoragem:"piso"},
```

E o raycast só considera as superfícies compatíveis:

```js
function superficieAlvo(produto){
  return superficies.children.filter(s => s.userData.ancoragem === produto.ancoragem);
}

function posicionar(objeto, produto, evento){
  const ndc = new THREE.Vector2(
    (evento.clientX / innerWidth) * 2 - 1,
    -(evento.clientY / innerHeight) * 2 + 1
  );
  raycaster.setFromCamera(ndc, camera);

  const hits = raycaster.intersectObjects(superficieAlvo(produto), false);
  if (!hits.length) return false;          // fora da superfície: não solta

  const hit = hits[0];
  if (produto.ancoragem === "parede"){
    objeto.position.copy(hit.point);
    objeto.lookAt(hit.point.clone().add(hit.face.normal));   // encosta na parede
  } else {
    assentar(objeto, hit.point);
  }
  return true;
}
```

Repare: se o raio não bate em superfície compatível, a peça **não é solta**.
Isso sozinho já elimina a maior parte dos objetos no ar.

---

## Sombra de contato — o que faz parecer plantado

Peça assentada sem sombra continua parecendo colada por cima. Uma sombra suave
embaixo resolve a percepção, e é barata: um plano com textura de gradiente radial.

```js
function sombraDeContato(largura){
  const c = document.createElement("canvas");
  c.width = c.height = 128;
  const g = c.getContext("2d");
  const grad = g.createRadialGradient(64,64,4, 64,64,64);
  grad.addColorStop(0,   "rgba(0,0,0,.42)");
  grad.addColorStop(0.6, "rgba(0,0,0,.14)");
  grad.addColorStop(1,   "rgba(0,0,0,0)");
  g.fillStyle = grad; g.fillRect(0,0,128,128);

  const plano = new THREE.Mesh(
    new THREE.PlaneGeometry(largura*1.5, largura*1.5),
    new THREE.MeshBasicMaterial({
      map:new THREE.CanvasTexture(c), transparent:true,
      depthWrite:false, opacity:.9
    })
  );
  plano.rotation.x = -Math.PI/2;
  plano.position.y = 0.004;          // acima do piso, evita z-fighting
  plano.renderOrder = -1;
  return plano;
}
```

Adicione como filha da peça, na base dela. Só isso muda mais a sensação de
"plantado" do que qualquer ajuste de posição.

---

## O botão de fixar

Fixar é tirar a peça do conjunto arrastável e marcar isso visualmente.

```js
function fixar(objeto, fixo){
  objeto.userData.fixo = fixo;
  // o conjunto que o arraste consulta
  arrastaveis = pecas.filter(p => !p.userData.fixo);
  // estado visível: contorno some quando fixo
  if (objeto.userData.contorno) objeto.userData.contorno.visible = !fixo;
}
```

Regras que valem a pena:

- Fixar **sempre reassenta** antes de travar — nunca congela uma peça no ar.
- Peça fixa continua selecionável (para desfixar), só não arrasta.
- Fixe automaticamente ao soltar, com um botão "destravar" para reposicionar.
  Menos cliques, e resolve o sintoma sem o vendedor precisar lembrar.

---

## Persistir

Se o estado não é salvo, tudo volta a flutuar no reload:

```js
const estado = pecas.map(p => ({
  cod:  p.userData.cod,
  pos:  p.position.toArray(),
  rot:  p.rotation.toArray().slice(0,3),
  esc:  p.scale.toArray(),
  fixo: !!p.userData.fixo,
}));
```

Ao restaurar, aplique e **chame `assentar()` de novo** para peças de piso — se o
plano mudou entre versões, a peça reassenta em vez de voltar ao ar.

---

## Ordem de aplicação

1. Planos invisíveis de piso e parede, calibrados com `wireframe` ligado
2. `ancoragem` em cada SKU do catálogo
3. `assentar()` no soltar e ao fim do arraste
4. Recusar o solte quando não há superfície compatível
5. Sombra de contato
6. Botão de fixar, com reassentamento antes de travar
7. Persistência

Os passos 1 a 4 matam a flutuação geométrica. O passo 5 mata a sensação.
Os passos 6 e 7 fecham o fluxo.

---

## Como conferir que acabou

- Solte uma peça de piso em vários pontos: a base encosta em todos
- Solte um quadro: encosta na parede, alinhado à normal dela
- Tente soltar um quadro no piso: recusa
- Fixe, arraste: não move
- Recarregue: tudo volta onde estava, nada no ar
