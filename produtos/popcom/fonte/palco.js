/* ══════════════════════════════════════════════════════════════
   PALCO — ciclorama de estúdio com os produtos da campanha.
   Referência: fotografia publicitária de produto, não sala de estar.
   Saídas: PNG (still da campanha) e WebM (volta completa da órbita).
   ══════════════════════════════════════════════════════════════ */
const Palco = (() => {
  const menosMovimento = matchMedia("(prefers-reduced-motion: reduce)").matches;

  let renderer, scene, camera, grupo, relogio, anim = null;
  let orbitando = !menosMovimento, angulo = 0, raio = 13, alvoY = 1.9;
  let dollying = false, fovBase = 42;
  let arrastando = false, ultimoX = 0;
  let gravador = null, pedacos = [];
  let pronto = false;

  const cv = () => document.getElementById("palco");

  /* --- textura do card do produto, desenhada em canvas --- */
  function texturaProduto(p){
    const c = document.createElement("canvas");
    c.width = 512; c.height = 660;
    const g = c.getContext("2d");

    g.fillStyle = "#FCFBF9"; g.fillRect(0,0,512,660);
    g.strokeStyle = "#C9A257"; g.lineWidth = 6;
    g.strokeRect(16,16,480,628);

    g.fillStyle = "#8A6A2C";
    g.font = "700 26px 'JetBrains Mono', monospace";
    g.fillText(p.cod, 44, 84);

    g.fillStyle = "#14181C";
    g.font = "600 38px Archivo, sans-serif";
    const palavras = p.nome.split(" ");
    let linha = "", y = 168;
    for (const w of palavras){
      const teste = linha ? linha + " " + w : w;
      if (g.measureText(teste).width > 420){ g.fillText(linha, 44, y); y += 50; linha = w; }
      else linha = teste;
    }
    if (linha) g.fillText(linha, 44, y);

    g.strokeStyle = "#D8DEE2"; g.lineWidth = 2;
    g.beginPath(); g.moveTo(44, 540); g.lineTo(468, 540); g.stroke();

    g.fillStyle = "#8A6A2C";
    g.font = "700 44px 'JetBrains Mono', monospace";
    g.fillText(p.preco.toLocaleString("pt-BR",{style:"currency",currency:"BRL"}), 44, 604);

    const t = new THREE.CanvasTexture(c);
    t.colorSpace = THREE.SRGBColorSpace ?? t.colorSpace;
    t.anisotropy = 8;
    return t;
  }

  /* --- ciclorama: piso que sobe em curva contínua no fundo --- */
  function ciclorama(){
    const geo = new THREE.PlaneGeometry(110, 110, 90, 90);
    geo.rotateX(-Math.PI/2);
    const pos = geo.attributes.position;
    for (let i = 0; i < pos.count; i++){
      // A curva sobe pela DISTÂNCIA AO CENTRO, não pela profundidade: assim o
      // ciclorama é uma tigela, e a câmera nunca cruza uma borda ao orbitar.
      const raioXZ = Math.hypot(pos.getX(i), pos.getZ(i));
      const t = Math.min(Math.max((raioXZ - 15) / 20, 0), 1);
      pos.setY(i, t * t * 42);
    }
    geo.computeVertexNormals();
    return new THREE.Mesh(geo, new THREE.MeshStandardMaterial({
      color:0x8C857A, roughness:.96, metalness:0,
    }));
  }

  function pedestal(altura){
    const m = new THREE.Mesh(
      new THREE.CylinderGeometry(1.05, 1.15, altura, 48),
      new THREE.MeshStandardMaterial({color:0xF0EDE8, roughness:.62, metalness:.04})
    );
    m.castShadow = true; m.receiveShadow = true;
    return m;
  }

  function iniciar(){
    const canvas = cv();
    renderer = new THREE.WebGLRenderer({canvas, antialias:true, alpha:false,
      preserveDrawingBuffer:true});
    renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
    renderer.shadowMap.enabled = true;
    renderer.shadowMap.type = THREE.PCFSoftShadowMap;
    if (THREE.SRGBColorSpace) renderer.outputColorSpace = THREE.SRGBColorSpace;
    renderer.toneMapping = THREE.ACESFilmicToneMapping;
    renderer.toneMappingExposure = 1.0;

    scene = new THREE.Scene();
    scene.background = new THREE.Color(0x7E776D);

    camera = new THREE.PerspectiveCamera(fovBase, 16/9, .1, 200);

    scene.add(ciclorama());

    // luz de três pontos, como um set de estúdio
    const key = new THREE.DirectionalLight(0xFFF4E2, 3.4);
    key.position.set(7, 11, 8);
    key.castShadow = true;
    key.shadow.mapSize.set(2048, 2048);
    key.shadow.camera.left = -18; key.shadow.camera.right = 18;
    key.shadow.camera.top = 18;  key.shadow.camera.bottom = -18;
    key.shadow.bias = -0.0008;
    scene.add(key);

    const fill = new THREE.DirectionalLight(0xD3E0EE, .5);
    fill.position.set(-9, 5, 6); scene.add(fill);

    const rim = new THREE.DirectionalLight(0xC9A257, 1.9);
    rim.position.set(-4, 7, -10); scene.add(rim);

    scene.add(new THREE.HemisphereLight(0xE8ECEF, 0x4A443C, .3));

    grupo = new THREE.Group();
    scene.add(grupo);

    relogio = new THREE.Clock();
    dimensionar();
    addEventListener("resize", dimensionar);

    // arraste horizontal gira a cena
    canvas.addEventListener("pointerdown", e => {
      arrastando = true; ultimoX = e.clientX; canvas.setPointerCapture(e.pointerId);
    });
    canvas.addEventListener("pointermove", e => {
      if (!arrastando) return;
      angulo -= (e.clientX - ultimoX) * .006;
      ultimoX = e.clientX;
    });
    canvas.addEventListener("pointerup", e => {
      arrastando = false; canvas.releasePointerCapture(e.pointerId);
    });

    pronto = true;
    laco();
  }

  function dimensionar(){
    if (!renderer) return;
    const c = cv(), l = c.clientWidth, a = c.clientHeight;
    renderer.setSize(l, a, false);
    camera.aspect = l / a;
    camera.updateProjectionMatrix();
  }

  /** Monta o palco com os produtos escolhidos. */
  function montar(produtos){
    if (!pronto) return;
    while (grupo.children.length) {
      const o = grupo.children.pop();
      o.traverse(n => { n.geometry?.dispose?.(); n.material?.map?.dispose?.(); n.material?.dispose?.(); });
    }
    document.getElementById("palco-vazio").style.display = produtos.length ? "none" : "grid";
    document.getElementById("palco-sel").textContent = `${produtos.length} ${produtos.length===1?"produto":"produtos"}`;

    const n = produtos.length;
    if (!n) return;
    const passo = Math.PI * 2 / Math.max(n, 3);
    const anelR = Math.min(3.2 + n * .55, 9);

    produtos.forEach((p, i) => {
      const a = i * passo;
      const alturaPed = 1.1 + (i % 3) * .28;

      const base = pedestal(alturaPed);
      base.position.set(Math.cos(a) * anelR, alturaPed/2, Math.sin(a) * anelR);

      const card = new THREE.Mesh(
        new THREE.PlaneGeometry(1.9, 2.45),
        new THREE.MeshStandardMaterial({map:texturaProduto(p), roughness:.55, metalness:.02,
          side:THREE.DoubleSide})
      );
      card.position.set(base.position.x, alturaPed + 1.28, base.position.z);
      card.castShadow = true;
      card.userData.encaraCamera = true;

      grupo.add(base, card);
    });

    raio = anelR + 8.2;
    alvoY = 1.55;
  }

  function laco(){
    anim = requestAnimationFrame(laco);
    const dt = relogio.getDelta();
    if (orbitando && !arrastando) angulo += dt * .12;

    // dolly zoom: aproxima e abre o campo, mantendo o assunto do mesmo tamanho
    if (dollying){
      const t = (Math.sin(relogio.elapsedTime * .35) + 1) / 2;   // 0..1
      const fov = fovBase - t * 16;
      const dist = raio * (Math.tan(THREE.MathUtils.degToRad(fovBase/2)) /
                           Math.tan(THREE.MathUtils.degToRad(fov/2)));
      camera.fov = fov; camera.updateProjectionMatrix();
      camera.position.set(Math.cos(angulo)*dist, alvoY + 1.15, Math.sin(angulo)*dist);
    } else {
      if (camera.fov !== fovBase){ camera.fov = fovBase; camera.updateProjectionMatrix(); }
      camera.position.set(Math.cos(angulo)*raio, alvoY + 1.15, Math.sin(angulo)*raio);
    }
    camera.lookAt(0, alvoY, 0);

    grupo.children.forEach(o => { if (o.userData.encaraCamera) o.lookAt(camera.position); });
    renderer.render(scene, camera);
  }

  /* --- saídas --- */
  async function png(){
    renderer.render(scene, camera);
    const blob = await new Promise(r => cv().toBlob(r, "image/png"));
    if (!blob) return null;
    return new Uint8Array(await blob.arrayBuffer());
  }

  function gravando(){ return !!gravador; }

  /** Grava uma volta completa da órbita. Resolve com os bytes do WebM. */
  function video(segundos = 8){
    return new Promise((resolve, reject) => {
      if (gravador) return reject(new Error("Já está gravando."));
      const stream = cv().captureStream(30);
      const tipo = ["video/webm;codecs=vp9","video/webm;codecs=vp8","video/webm"]
        .find(t => MediaRecorder.isTypeSupported(t));
      if (!tipo) return reject(new Error("Este navegador não grava vídeo."));

      pedacos = [];
      gravador = new MediaRecorder(stream, {mimeType:tipo, videoBitsPerSecond: 6_000_000});
      gravador.ondataavailable = e => { if (e.data.size) pedacos.push(e.data); };
      gravador.onstop = async () => {
        const blob = new Blob(pedacos, {type:"video/webm"});
        gravador = null;
        document.getElementById("rec").classList.remove("on");
        resolve(new Uint8Array(await blob.arrayBuffer()));
      };

      const orbitavaAntes = orbitando;
      orbitando = true;                       // a volta precisa acontecer
      document.getElementById("rec").classList.add("on");
      gravador.start();
      setTimeout(() => {
        orbitando = orbitavaAntes;
        if (gravador && gravador.state !== "inactive") gravador.stop();
      }, segundos * 1000);
    });
  }

  return {
    iniciar, montar, png, video, gravando,
    orbita(v){ orbitando = v; },
    orbitando(){ return orbitando; },
    dolly(v){ dollying = v; },
    dollying(){ return dollying; },
    dimensionar,
    ativo(){ return pronto; },
  };
})();

/* ══════════ ligação com a interface ══════════ */
function palcoAtualizar(){
  if (Palco.ativo()) Palco.montar(selecionados());
}

document.getElementById("d-orbita").addEventListener("click", e => {
  const on = !Palco.orbitando();
  Palco.orbita(on);
  e.currentTarget.setAttribute("data-rot", on ? "Pausar órbita" : "Girar");
});

document.getElementById("d-dolly").addEventListener("click", e => {
  const on = !Palco.dollying();
  Palco.dolly(on);
  e.currentTarget.style.background = on ? "rgba(201,162,87,.28)" : "";
});

document.getElementById("d-png").addEventListener("click", async () => {
  if (!selecionados().length) return aviso("Escolha produtos na aba Campanha.");
  const bytes = await Palco.png();
  if (!bytes) return aviso("Não consegui gerar a imagem.");
  await baixar(`PopCom_Campanha_${Date.now()}.png`, bytes);
});

document.getElementById("d-video").addEventListener("click", async () => {
  if (!selecionados().length) return aviso("Escolha produtos na aba Campanha.");
  if (Palco.gravando()) return;
  aviso("Gravando uma volta completa — 8 segundos.");
  try{
    const bytes = await Palco.video(8);
    await baixar(`PopCom_Campanha_${Date.now()}.webm`, bytes);
  }catch(err){ aviso(err.message); }
});

document.getElementById("d-xr").addEventListener("click", async () => {
  aviso("Modo imersivo depende de headset conectado.");
});

/* dock com ampliação por proximidade (padrão 21st.dev) */
(function dockMagnify(){
  const dock = document.querySelector(".dock");
  if (!dock || matchMedia("(prefers-reduced-motion: reduce)").matches) return;
  const btns = [...dock.querySelectorAll(".dock-btn")];
  dock.addEventListener("pointermove", e => {
    btns.forEach(b => {
      const r = b.getBoundingClientRect();
      const d = Math.abs(e.clientX - (r.left + r.width/2));
      const escala = Math.max(1, 1.42 - d / 130);
      b.style.transform = `scale(${escala.toFixed(3)}) translateY(${((escala-1)*-9).toFixed(1)}px)`;
    });
  });
  dock.addEventListener("pointerleave", () => {
    btns.forEach(b => { b.style.transform = ""; });
  });
})();

/* Motion: entrada dos painéis ao trocar de aba */
function animarPainel(el){
  if (!el || typeof Motion === "undefined") return;
  if (matchMedia("(prefers-reduced-motion: reduce)").matches) return;
  Motion.animate(el, {opacity:[0,1], transform:["translateY(9px)","translateY(0px)"]},
    {duration:.32, easing:[.22,.61,.36,1]});
}
