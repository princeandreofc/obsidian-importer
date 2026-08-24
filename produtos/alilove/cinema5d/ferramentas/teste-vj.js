const path=require('path');
const {chromium}=require(path.join(require('child_process').execSync('npm root -g').toString().trim(),'playwright'));
const FILE='file:///home/user/obsidian-importer/produtos/alilove/cinema5d/the-spiral-vj.html';
(async()=>{
  const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader']});
  const ctx=await b.newContext({viewport:{width:1440,height:900},acceptDownloads:true});
  await ctx.route(/alilove\.world|spotify\.com/,r=>r.abort());
  const p=await ctx.newPage();
  const errs=[];
  p.on('pageerror',e=>errs.push('PE: '+e.message));
  p.on('console',m=>{if(m.type()==='error'&&!/fonts\.g|ERR_CONN|net::/.test(m.text()))errs.push('C: '+m.text().slice(0,150))});
  await p.goto(FILE);await p.waitForTimeout(3000);
  const boot=await p.evaluate(()=>({
    deckOn:document.getElementById('deck').classList.contains('on'),
    capsVisiveis:[...document.querySelectorAll('.cap')].filter(c=>c.offsetParent).length,
    menuVisivel:!!document.querySelector('.menu')?.offsetParent,
    voltar:!!document.querySelector('.voltar')?.offsetParent,
    bancos:document.querySelectorAll('.banco').length,
    macros:document.querySelectorAll('.macros input').length,
    micRemovido:!document.getElementById('vj-mic'),
    avisoVisualOnly:/visual-only/.test(document.querySelector('.aviso').textContent),
    dep:document.getElementById('v-dep').textContent
  }));
  console.log('BOOT',JSON.stringify(boot));
  const d1=await p.evaluate(()=>parseInt(document.getElementById('v-dep').textContent));
  await p.waitForTimeout(4000);
  const d2=await p.evaluate(()=>parseInt(document.getElementById('v-dep').textContent));
  console.log('DERIVA',d1,'->',d2,d2!==d1?'OK':'PARADA');
  // bancos de cena: clique (C GARDEN) e tecla (d = RITUAL); clamp dos macros
  await p.click('.banco[data-cena="garden"]');
  await p.waitForTimeout(600);
  const cenaC=await p.evaluate(()=>({
    pressed:document.querySelector('.banco[data-cena="garden"]').getAttribute('aria-pressed'),
    con:+__macro.connection.toFixed(2),
    slider:document.getElementById('mc-connection').value,
    clampAlto:(()=>{const v=defineMacro('energy',7);const r=v===1;defineMacro('energy',.3);return r})(),
    clampBaixo:(()=>{const v=defineMacro('depth',-3);const r=v===0;defineMacro('depth',.5);return r})()
  }));
  console.log('CENA-C',JSON.stringify(cenaC));
  await p.keyboard.press('d');
  await p.waitForTimeout(2600);
  const cenaD=await p.evaluate(()=>({
    pressed:document.querySelector('.banco[data-cena="ritual"]').getAttribute('aria-pressed'),
    alvo:cenaAtiva?cenaAtiva.id:null,
    dep:document.getElementById('v-dep').textContent
  }));
  console.log('CENA-D',JSON.stringify(cenaD));
  await p.keyboard.press('2');await p.keyboard.press('3');
  await p.waitForTimeout(900);
  console.log('FX',JSON.stringify(await p.evaluate(()=>({
    trails:document.querySelector('.pad[data-fx="trails"]').getAttribute('aria-pressed'),
    filtro:document.getElementById('cena').style.filter.includes('hue-rotate')
  }))));
  await p.screenshot({path:'/tmp/claude-0/vj0-palco.png'});
  // jam local: gaveta avançada → upload → graves medidos pelo SIGNAL PLAYER
  await p.evaluate(()=>{document.getElementById('vj-mais').open=true});
  await p.setInputFiles('#vj-arquivo','/tmp/claude-0/teste.wav');
  await p.waitForTimeout(1500);
  console.log('AUDIO',await p.evaluate(
    "JSON.stringify({grave:+nivelGrave.toFixed(2),energy:+__sinal.energy.toFixed(2),playing:__sinal.playing})"));
  const dl=p.waitForEvent('download',{timeout:15000}).catch(()=>null);
  await p.keyboard.press('r');await p.waitForTimeout(1500);await p.keyboard.press('r');
  console.log('REC',(await dl)?.suggestedFilename()||'SEM-DOWNLOAD');
  await p.screenshot({path:'/tmp/claude-0/vj1-audio.png'});
  await ctx.close();
  const mctx=await b.newContext({viewport:{width:390,height:844},hasTouch:true,isMobile:true});
  await mctx.route(/alilove\.world|spotify\.com/,r=>r.abort());
  const m=await mctx.newPage();
  await m.goto(FILE);await m.waitForTimeout(2600);
  console.log('MOBILE',JSON.stringify(await m.evaluate(()=>({
    overflow:document.documentElement.scrollWidth,
    deck:document.getElementById('deck').classList.contains('on'),
    banco:(r=>({w:Math.round(r.width),h:Math.round(r.height)}))(
      document.querySelector('.banco').getBoundingClientRect())
  }))));
  await m.screenshot({path:'/tmp/claude-0/vj2-mob.png'});
  await b.close();
  console.log('ERRS',errs.length?errs.join(' | '):'nenhum');
})().catch(e=>{console.error('FALHA',e);process.exit(1)});
