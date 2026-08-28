const path=require('path');
const {chromium}=require(path.join(require('child_process').execSync('npm root -g').toString().trim(),'playwright'));
(async()=>{
  const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader']});
  const ctx=await b.newContext({viewport:{width:1440,height:900},reducedMotion:'reduce'});
  await ctx.route(/alilove\.world|spotify\.com/,r=>r.abort());
  const p=await ctx.newPage();
  const errs=[];
  p.on('pageerror',e=>errs.push(e.message));
  await p.goto('file:///tmp/claude-0/jornada-tmp.html');
  await p.waitForTimeout(3000);
  console.log('REDUZ-BOOT',JSON.stringify(await p.evaluate(()=>({
    reduz:matchMedia('(prefers-reduced-motion: reduce)').matches,
    semGl:document.body.classList.contains('sem-gl'),
    rosa:typeof rosa!=='undefined'&&!!rosa
  }))));
  // sessão sob movimento reduzido: abre e progride
  await p.click('#b-sessao');
  await p.waitForTimeout(1500);
  console.log('REDUZ-SESSAO',JSON.stringify(await p.evaluate(()=>({
    aberta:!document.getElementById('sessao').hidden,
    prog:document.getElementById('ses-prog').style.width
  }))));
  console.log('REDUZ-ERRS',errs.length?errs.join('|'):'nenhum');
  await b.close();
})().catch(e=>{console.error('FALHA',e);process.exit(1)});
