import re,os,base64,glob
sc="/tmp/claude-0/-home-user-obsidian-importer/d0c3c9d6-2774-5776-8a8a-3ab6877f5855/scratchpad"
src=open("/home/user/obsidian-importer/produtos/alilove/cinema5d/cinema5d-src.html").read()
three="<script>\n"+open(sc+"/popcom/three.min.js").read()+"\n</script>"
URL_MAIN="https://claude.ai/code/artifact/8ae9e2fa-be3d-4aee-b92b-c6d3343c6d50"
URL_VJ="https://claude.ai/code/artifact/0f9562be-2e63-4036-b524-2a0fb84e9bcd"
# capas: /tmp/claude-0/capas/<tema>.jpg → data URI; ausente → {}
capas={}
for f in glob.glob("/tmp/claude-0/capas/*.jpg"):
    tema=os.path.splitext(os.path.basename(f))[0]
    b=base64.b64encode(open(f,"rb").read()).decode()
    capas[tema]=f"data:image/jpeg;base64,{b}"
capas_js="{"+",".join(f'{t}:"{u}"' for t,u in capas.items())+"}"
print("capas embutidas:",list(capas.keys()) or "nenhuma (fallback gerativo)")
def monta(modo,vjurl,titulo=None):
    out=src.replace("@@THREE@@",three,1).replace("@@MODO@@",modo)\
           .replace("@@VJURL@@",vjurl).replace("@@CAPAS@@",capas_js)
    if titulo:out=out.replace("<title>The Spiral</title>",f"<title>{titulo}</title>",1)
    return out
jor=monta("jornada",URL_VJ)
vj=monta("vj",URL_MAIN,"The Spiral VJ Studio")
open("/home/user/obsidian-importer/produtos/alilove/cinema5d/the-spiral.html","w").write(jor)
open("/home/user/obsidian-importer/produtos/alilove/cinema5d/the-spiral-vj.html","w").write(vj)
open("/tmp/claude-0/app-jor.js","w").write(re.findall(r"<script>(.*?)</script>",jor,re.S)[-1])
open("/tmp/claude-0/app-vj.js","w").write(re.findall(r"<script>(.*?)</script>",vj,re.S)[-1])
print("jornada",len(jor),"vj",len(vj))
