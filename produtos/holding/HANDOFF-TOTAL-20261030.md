# HANDOFF TOTAL — operação da holding (30/10/2026, retaguarda nuvem)

Para o Claude Code no Mac. Ritual: `git pull` neste repo, ler `MAPLE-OS.md`
(lembrete: o sistema hoje chama-se **Eloa OS**; "Maple" é referência
histórica; o canônico TÉCNICO vive em `princeandreofc/climbexglobal`) e
este arquivo. Depois executar na ordem de prioridade abaixo. Regra de ouro:
commit+push ao fim de cada etapa; falha se reporta com a mensagem exata.

## P1 · ELOA OS — retomar o preview Cloudflare (técnico, destravado p/ Mac)

Repo `princeandreofc/climbexglobal`, branch `codex/eloa-os-final-handoff-20261015`
@ `cb719fb` (checkpoint da nuvem, 20/10). Já PASSARAM: eloa:approval:smoke,
lint, next build (41 páginas, /eloa/approval-preview no bundle), vinext
check (96%, 0 issues). BLOQUEADO na nuvem: `npm run build:vinext` falha sob
Node 22 (bug dos module hooks do @cloudflare/config beta — detalhe no
RESUME) e wrangler sem auth. **No Mac (Node 24 + wrangler logado):**

1. `git fetch && git checkout codex/eloa-os-final-handoff-20261015 && npm ci`
2. `npm run build:vinext` — deve passar em Node 24; se falhar, registrar no
   RESUME e parar (não forçar).
3. `npx wrangler@latest whoami` (conferir conta Climbex) → `npm run deploy:vinext`
   (worker `eloa-control-preview`, workers.dev) → smoke do slice
   `/eloa/approval-preview` (desktop+mobile, approve/reject, external.send DENY).
4. Atualizar `docs/handoffs/ELOA_OS_RESUME_CWB-20260921-001.md` com evidência
   real + push. Preview LIBERADO; produção/DNS/billing = gate.

## P2 · BRENNO — 3 fechamentos comerciais abertos (receita que salva pendências)

**a) Prax Industries (URGENTE — e-mail deles chegou 28/10, janela de 48h já estourando).**
Plano completo + precificação com fontes: doc "Brenno × Prax — preço e
fechamento" (claude.ai/artifact/CMm1bCTxfD4HRG8VHEjutf; o André tem o PDF).
Essência: contato = Yonah Citron (Deployment Strategist/FDE, Londres);
preço = sessão 90min US$ 1.500 · dia US$ 6.000 · discovery sprint
US$ 20–24k · retainer US$ 9–12k/mês (escada ≈ US$ 50–60k/trimestre);
rascunho da resposta EN pronto no doc (falta 1 frase de credencial do
Brenno + entidade USD). **Um e-mail consolidado ao Brenno ficou PRONTO mas
NÃO ENVIADO na nuvem** — ou o Mac envia o resumo ao
brennocastrillon@climbexglobal.com, ou o André mostra o doc direto ao
Brenno. O que importa: Brenno responder ao Yonah JÁ.

**b) OpenAI — candidatura de parceiro parada desde 19/10.** A Renata (OpenAI)
mandou o próximo passo; os links estão na msg do Hugo de 16/10 na thread
"OpenAI // Climbex Global" (Gmail admin@): SMB Referral Onboarding Interest
Form (Google Forms) e/ou OPN Partner Portal (partners.openai.com/s/).
Recomendação registrada: começar POC no ChatGPT Business (3–6 semanas),
independe da aprovação de parceria. Ação: submeter a(s) candidatura(s).

**c) Engro/ETS — ação da CLIMBEX pendente desde 10/09** (ata na thread
"Fw: Business Opportunities in Brazil", Gmail admin@, deck ETS anexo):
item 4 = Climbex revisar ofertas da ETS e mapear oportunidades no Brasil
(AspenTech APC/DMC3/RTO, process modeling, digitalização industrial —
especialidade do Brenno); depois framework comercial + 1º piloto (itens
5–6). Logo da Engro no site SÓ após MoU. Ação: rascunhar a resposta ao
Zaid (zaid.ashraf@engro.com) para o Brenno revisar.

## P3 · SAM/FURLANETTO — fechar o kit (BOILER é 31/10, AMANHÃ)

Entrega principal foi ENVIADA 20/10 (links, thread no Gmail admin@). Falta:
1. **E-mail 2 (kit do vendedor) está em RASCUNHO** no Gmail admin@
   (assunto "Sam — seu kit de parceiro…"): anexar os 3 PDFs (SELLER_KIT_
   SAM_SANTANA, MARKET_SNAPSHOT_EN, GROWTH_DESK_ONE_PAGER_EN — estão no
   Mac), ZIPs do Growth Desk vão por LINK do Drive (anexo .zip com .js
   volta no Gmail — comprovado 2×), apagar o bloco [ANDRÉ — ANTES DE
   ENVIAR] e enviar.
2. Briefing interativo publicado (claude.ai/artifact/DZLXRLYt9xHn8RjYc2mdHy)
   — precisa de 1 clique em Compartilhar para abrir para o Sam.
3. Cobrar do Sam os dados do BOILER 31/10 (casa, horário, line-up) para
   fechar as peças datadas.

## P4 · POP / VERTICAIS — vitrine de cliente

- Storefront PÚBLICO vivo: pop-verticals-client.vercel.app (único link que
  se mostra/envia a cliente). Demos Pop Casa/Camargo/popcom = protegidas
  por login (certo assim). **Link morto na entrega canônica**: o catálogo
  `pop-verticals-catalog.climbexglobal-b258.chatgpt.site` não responde —
  corrigir o doc 00_LEIA_PRIMEIRO_ENTREGA_FINAL_POP_COMM (Drive) para
  apontar ao storefront vivo.
- Vitrine única para cliente aguarda MÍDIAS do Seagate: vídeos/artes
  Higgsfield + fotos POP → copiar (nunca mover) para pasta "VITRINE_POP"
  no Drive do andreboliveira@, compartilhada com admin@ — a nuvem monta a
  página com elas. Fotos MART/fornecedor = demo interna ok, publicar = gate.
- Lista oficial de marcas-cliente do Fernando: segue pendente (Tina).

## P5 · MÚSICA

- **Zaza Moça V17 "Balanced Groove"** (checkpoint de revisão):
  `/Volumes/Seagate Portable Drive/PRINCE_ANDRE_ZAZA_MOCA_VERSAO_GFUNK_CHICAGO_2026-10-16/08_BOUNCES_V17/`
  — o André quer OUVIR; mandar o MP3 a ele e **subir backup no Drive (hoje
  não existe backup de nuvem — risco real)**.
- Masters do álbum: sempre em CÓPIAS, alvos −14 LUFS int / TP ≤ −1 dBTP
  (produtos/princeandre/library-master.md). Originais/Logic intocáveis.
- Frente Ali Love segue EXCLUSIVA do André.

## 1-cliques do André (lembrar a ele, não executar)

merge do PR #8 (estado vivo, obsidian-importer) · enviar e-mail 2 do Sam ·
Compartilhar o briefing do Sam · responder à Renata (OpenAI) com a
candidatura · CLOUDFLARE_API_TOKEN como secret do environment da nuvem
(destrava deploy Cloudflare de lá) · claim princeandre.world ($3,99).

## Gates (sempre)

Produção/DNS/domínio/dinheiro/contratos/envio externo = APROVADO explícito
do André (Prax: André já aprovou preço/plano; o ENVIO ao Yonah é do
Brenno). Marcas não se misturam; Prax é frente pessoal do Brenno; stack
interno = só "stack Climbex"; nada de fato/preço/data inventado; anexo
.zip no Gmail volta — usar Drive.
