const path=require('path');
const {chromium}=require(path.join(require('child_process').execSync('npm root -g').toString().trim(),'playwright'));
(async()=>{
  const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader']});
  const ctx=await b.newContext({viewport:{width:1440,height:900}});
  await ctx.route(/alilove\.world|spotify\.com/,r=>r.abort());
  const p=await ctx.newPage();
  await p.goto('file:///tmp/claude-0/jornada-tmp.html');
  await p.waitForTimeout(3500);
  await p.screenshot({path:'/tmp/claude-0/probe-hero.png'});
  await b.close();
})().catch(e=>{console.error(e);process.exit(1)});
