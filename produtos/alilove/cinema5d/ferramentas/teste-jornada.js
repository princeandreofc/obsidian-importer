const path=require('path');
const {chromium}=require(path.join(require('child_process').execSync('npm root -g').toString().trim(),'playwright'));
const FILE=process.argv[2]||'file:///tmp/claude-0/jornada-tmp.html';
const OUT='/tmp/claude-0/';
const ruido=s=>/fonts\.g|ERR_CONNECTION|net::|favicon/.test(s);
(async()=>{
  const browser=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader']});
  const errs=[];
  const ctx=await browser.newContext({viewport:{width:1440,height:900}});
  await ctx.route(/alilove\.world|spotify\.com/,r=>r.abort());
  const page=await ctx.newPage();
  page.on('pageerror',e=>errs.push('PE: '+e.message));
  page.on('console',m=>{if(m.type()==='error'&&!ruido(m.text()))errs.push('C: '+m.text().slice(0,200))});
  await page.goto(FILE);await page.waitForTimeout(3000);
  const boot=await page.evaluate(()=>({
    semGl:document.body.classList.contains('sem-gl'),
    era:document.getElementById('v-era').textContent,
    menu:document.querySelectorAll('.menu button').length,
    deckVisivel:!!document.getElementById('deck').offsetParent,
    rosa3d:typeof rosa!=='undefined'&&!!rosa&&rosa.children.length>=5,
    rosa2d:document.querySelectorAll('svg.rosa-2d ellipse').length
  }));
  console.log('BOOT',JSON.stringify(boot));
  // gate fail-closed: limpo passa; memória não liberada bloqueia
  const gate=await page.evaluate(()=>{
    let limpo=true,bloqueia=false;
    try{__gate()}catch(e){limpo=false}
    try{__gate([{id:'x',enabled:true,evidence:'public-catalog',rights:'approved-preview'}])}
    catch(e){bloqueia=/memory:x/.test(e.message)}
    return {limpo,bloqueia};
  });
  console.log('GATE',JSON.stringify(gate));
  // reducer da sessão: determinístico, lembra com hold, sem game over
  const red=await page.evaluate(()=>{
    let s=__sessaoInicial(528);
    s=__sessaoReduz(s,{type:'TICK',tMs:6000,dtMs:0,res:.6});
    const aposBuild=s.status;
    s=__sessaoReduz(s,{type:'TICK',tMs:19000,dtMs:0,res:.9});
    s=__sessaoReduz(s,{type:'TICK',tMs:25900,dtMs:6900,res:.9});
    s=__sessaoReduz(s,{type:'TICK',tMs:26500,dtMs:600,res:.9});
    const lembrou=s.status;
    let z=__sessaoInicial(1);
    z=__sessaoReduz(z,{type:'TICK',tMs:30000,dtMs:100,res:0});
    return {aposBuild,lembrou,semGameOver:z.status,fim:z.fim};
  });
  console.log('REDUCER',JSON.stringify(red));
  await page.screenshot({path:OUT+'j0-hero.png'});

  async function mergulha(frac,minDep){
    await page.evaluate(f=>{const max=document.documentElement.scrollHeight-innerHeight;scrollTo(0,max*f)},frac);
    await page.waitForFunction(md=>parseInt(document.getElementById('v-dep').textContent)>=md,minDep,{timeout:30000});
    await page.waitForTimeout(700);
  }
  // VISUALS (CRT + link VJ)
  await mergulha(.30,27);
  console.log('VISUAIS',JSON.stringify(await page.evaluate(()=>({
    era:document.getElementById('v-era').textContent,
    crt:document.getElementById('crt').classList.contains('on'),
    vjHref:document.querySelector('#cap2 a.btn-ouro').getAttribute('href').slice(0,40)
  }))));
  await page.screenshot({path:OUT+'j1-visuals.png'});
  // LISTEN — SIGNAL PLAYER fail-closed, Spotify independente, mic removido
  await mergulha(.60,56);
  await page.waitForTimeout(1600);
  console.log('LISTEN',JSON.stringify(await page.evaluate(()=>({
    era:document.getElementById('v-era').textContent,
    micRemovido:!document.getElementById('p-mic'),
    painel:!!document.getElementById('p-masters'),
    now:document.getElementById('p-now').textContent,
    notaFailClosed:/fail-closed/.test(document.getElementById('p-nota').textContent),
    spotify:!!document.querySelector('.spotify-box iframe'),
    mundos:!!document.getElementById('mundos'),
    rosaCamViva:typeof rosaProemCam!=='undefined'?+rosaProemCam.toFixed(2):-1,
    grave:(typeof nivelGrave!=='undefined'?+nivelGrave.toFixed(2):-1)
  }))));
  await page.screenshot({path:OUT+'j2-listen.png'});
  // RECORDS (sleeves reais)
  await mergulha(.705,66);
  console.log('RECORDS',JSON.stringify(await page.evaluate(()=>({
    era:document.getElementById('v-era').textContent,
    sleevesReais:document.querySelectorAll('#sleeves img').length,
    mundosDivs:document.querySelectorAll('#mundos .mundo').length
  }))));
  await page.screenshot({path:OUT+'j3-records.png'});
  // ARCHIVE + EPK + aviso 528
  await mergulha(1.0,97);
  console.log('EPK',JSON.stringify(await page.evaluate(()=>({
    era:document.getElementById('v-era').textContent,
    caps:document.querySelectorAll('.cap.viva').length,
    rodape:document.querySelector('#cap10').textContent.includes('© 2026 ALI LOVE'),
    aviso528:/cultural and\s+compositional/.test(document.querySelector('#cap10 .aviso-528').textContent)
  }))));
  await page.screenshot({path:OUT+'j4-epk.png'});
  // menu click → Archive
  await page.click('.menu button[data-sec="7"]');
  await page.waitForFunction(()=>document.getElementById('v-era').textContent==='THE ARCHIVE',null,{timeout:20000});
  console.log('MENU-CLICK ok');
  // RESONANCE SESSION — abre, roda, teclado, fecha
  await page.click('#b-sessao');
  await page.waitForTimeout(900);
  const ses1=await page.evaluate(()=>({
    aberta:!document.getElementById('sessao').hidden,
    estado:document.getElementById('ses-estado').textContent,
    prog:document.getElementById('ses-prog').style.width
  }));
  await page.keyboard.press('ArrowRight');await page.keyboard.press('ArrowUp');
  await page.waitForTimeout(1200);
  const ses2=await page.evaluate(()=>({
    estado:document.getElementById('ses-estado').textContent,
    prog:document.getElementById('ses-prog').style.width,
    tune:SES?+SES.tune.toFixed(2):-1
  }));
  console.log('SESSAO',JSON.stringify({...ses1,depois:ses2}));
  await page.screenshot({path:OUT+'j9-sessao.png'});
  await page.keyboard.press('Escape');
  const sesFechada=await page.evaluate(()=>document.getElementById('sessao').hidden);
  console.log('SESSAO-FECHA',sesFechada);
  await ctx.close();

  // MOBILE — o Ali aprova no celular
  const mctx=await browser.newContext({viewport:{width:390,height:844},hasTouch:true,isMobile:true});
  await mctx.route(/alilove\.world|spotify\.com/,r=>r.abort());
  const m=await mctx.newPage();
  m.on('pageerror',e=>errs.push('M-PE: '+e.message));
  await m.goto(FILE);await m.waitForTimeout(2800);
  const alvoSes=await m.evaluate(()=>{
    const b=document.getElementById('b-sessao');if(!b)return null;
    const r=b.getBoundingClientRect();return {w:Math.round(r.width),h:Math.round(r.height)};
  });
  console.log('MOBILE b-sessao',JSON.stringify(alvoSes));
  const fracs=[0,.30,.60,.705,1.0];
  let overflowMax=0;
  for(const f of fracs){
    await m.evaluate(fr=>{const max=document.documentElement.scrollHeight-innerHeight;scrollTo(0,max*fr)},f);
    await m.waitForTimeout(1400);
    const o=await m.evaluate(()=>document.documentElement.scrollWidth);
    overflowMax=Math.max(overflowMax,o);
    if(f===0)await m.screenshot({path:OUT+'j6-mob-hero.png'});
    if(f===.60)await m.screenshot({path:OUT+'j7-mob-listen.png'});
    if(f===1.0)await m.screenshot({path:OUT+'j8-mob-epk.png'});
  }
  console.log('MOBILE overflowMax='+overflowMax+' (limite 391)');
  await browser.close();
  console.log('ERRS',errs.length?errs.join(' | '):'nenhum');
})().catch(e=>{console.error('FALHA',e);process.exit(1)});
