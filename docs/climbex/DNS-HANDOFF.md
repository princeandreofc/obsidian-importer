# HANDOFF — Climbex DNS / subdomínios (para o Claude LOCAL · desktop)

**Gerado em 24/08/2026 ~23h UTC pela sessão remota, após diagnóstico
somente-leitura executado de verdade** (DoH público + HTTP + Vercel API
read-only). Nenhuma alteração foi feita em DNS, Vercel, Squarespace,
segurança ou produção.

---

## 1 · DIAGNÓSTICO REAL (24/08) — e o que ele muda no plano

O documento "Situação consolidada" listava CNAMEs `andre`/`brenno` como
**pendentes**. A realidade medida hoje é outra:

| Verificação | Resultado medido | Evidência |
| --- | --- | --- |
| Nameservers | **Squarespace ativos** (nse1–4.squarespacedns.com) | DoH NS |
| DNSSEC | **DS ausente — limpo** (a confirmação pedida via `dig DS`: feita) | DoH DS, NOERROR sem registros |
| MX | **iCloud intactos** mx01/mx02.mail.icloud.com | DoH MX |
| TXT | SPF `v=spf1 include:icloud.com ~all` + `apple-domain=…` + google-site-verification | DoH TXT |
| Apex `climbexglobal.com` | A **76.76.21.21** (Vercel) → **HTTP 200, server: Vercel** | DoH A + curl |
| `andre.climbexglobal.com` | **CNAME cname.vercel-dns.com JÁ EXISTE** → **HTTP 200, Vercel** | DoH CNAME + curl |
| `brenno.climbexglobal.com` | **CNAME cname.vercel-dns.com JÁ EXISTE** → **HTTP 200, Vercel** | DoH CNAME + curl |

**Conclusões:**
1. **Os dois subdomínios já estão NO AR**, servidos pela Vercel, pelo DNS
   atual do Squarespace. "Criar os CNAMEs" já aconteceu (no Squarespace).
   O "pendente" do documento refere-se apenas à **zona Cloudflare** (que
   segue `Pending` porque os NS não foram trocados).
2. Como respondem 200, os hostnames **estão atribuídos a projetos Vercel**
   (hostname sem projeto devolve DEPLOYMENT_NOT_FOUND). Falta só CONFERIR
   **qual projeto serve cada um** e se o CONTEÚDO é o desejado.
3. **A migração para Cloudflare virou OPCIONAL**, não pré-requisito: nada
   depende dela para andre/brenno funcionarem. Só vale fazer se quisermos
   os benefícios Cloudflare (proxy/WAF/analytics) — com o risco de mexer em
   NS de domínio com e-mail iCloud em produção.
4. E-mail iCloud está íntegro no estado atual.

## 2 · Primeiro passo LOCAL (leitura, 2 minutos)

No dashboard Vercel (team `admin-72622007s-projects` /
`team_PsN45axWZMm0jzgjvcIdOlS2`) conferir **Settings → Domains** dos
candidatos e anotar aqui o mapeamento real:

- `climbexglobal.com` → provavelmente projeto `climbexglobal`
  (`prj_aU2oJNSACKUPtdSCnEswwdFUg3AF`) — confirmar.
- `andre.climbexglobal.com` → candidatos: `andreboliveira`, `andre-v2`,
  `andre-v1`, `andre-corporate` — confirmar qual.
- `brenno.climbexglobal.com` → candidatos: `brenno-idi`, `brennocastrillon`
  — confirmar qual.

E **abrir os dois no navegador** para decidir a pergunta de conteúdo:
- https://andre.climbexglobal.com — é a página institucional certa do André?
- https://brenno.climbexglobal.com — é a página institucional do Dr. Brenno?
  (Recomendação em pé: destino = página institucional do Dr. Brenno. Se o
  conteúdo servido hoje não for esse, a mudança é **atribuir o domínio ao
  projeto certo na Vercel** — não é mudança de DNS.)

## 3 · Decisões que continuam com o André

1. **Conteúdo de `brenno.`** — aprovar o que está no ar ou apontar o
   domínio para outro projeto (ação na Vercel, reversível).
2. **Migrar ou não para Cloudflare** (troca de NS no Squarespace). Agora é
   escolha estratégica, não necessidade. Se sim, seguir a ordem do §4.
3. **Follow-up PopCom** — minuta existe em outra sessão; não foi enviada
   nem salva. Sem resposta no fio desde 28/07. Colar a minuta para revisão
   → salvar como rascunho Gmail → envio só pelo André.

## 4 · SE (e só se) a migração Cloudflare for autorizada — ordem segura

1. Recriar na zona Cloudflare **todos** os registros atuais (lista viva no
   §6) **como `DNS only` (nuvem cinza)** — especialmente MX/SPF/TXT Apple
   (e-mail) e os CNAMEs andre/brenno + apex A 76.76.21.21.
2. Conferir os 10 registros contra o §6 (paridade 1:1).
3. Trocar os nameservers no Squarespace pelos dois da Cloudflare.
4. Aguardar zona `Active` (horas). **Não ligar proxy laranja, SSL strict,
   DNSSEC novo nem cloudflared nessa janela.**
5. Testar: site, andre., brenno., **enviar+receber e-mail iCloud**.
6. Só depois, um por vez: proxy/SSL/DNSSEC — cada um com aprovação própria.

**Regras invioláveis herdadas:** nada de DNS/domínio/alias/certificado sem
autorização escrita específica; www.alilove.world nunca sai do ar;
trajetum.com fica no Squarespace; planning.com(.br) são de terceiros;
andreboliveira.com fica onde está; e-mail iCloud é intocável.

## 5 · Verificação repetível (rodar local a qualquer momento)

```bash
for q in "climbexglobal.com NS" "climbexglobal.com DS" "climbexglobal.com MX" \
         "climbexglobal.com TXT" "climbexglobal.com A" \
         "andre.climbexglobal.com CNAME" "brenno.climbexglobal.com CNAME"; do
  set -- $q
  curl -sS "https://cloudflare-dns.com/dns-query?name=$1&type=$2" \
    -H "accept: application/dns-json"; echo
done
curl -sI https://andre.climbexglobal.com | head -3
curl -sI https://brenno.climbexglobal.com | head -3
```

## 6 · Snapshot dos registros medidos hoje (paridade para o Cloudflare)

| Host | Tipo | Valor |
| --- | --- | --- |
| climbexglobal.com | A | 76.76.21.21 |
| climbexglobal.com | MX 10 | mx01.mail.icloud.com |
| climbexglobal.com | MX 10 | mx02.mail.icloud.com |
| climbexglobal.com | TXT | v=spf1 include:icloud.com ~all |
| climbexglobal.com | TXT | apple-domain=txXqdBBgJuWYW0tf |
| climbexglobal.com | TXT | google-site-verification=KPsLQ9zSZumPL9JcmdGPsIDLHbIT6rNPUeRWa1bD_YA |
| andre.climbexglobal.com | CNAME | cname.vercel-dns.com |
| brenno.climbexglobal.com | CNAME | cname.vercel-dns.com |

> Nota: o DKIM iCloud (CNAME `sig1._domainkey…`) não aparece em consulta
> pública sem o nome exato — conferir no painel Squarespace ao copiar a
> zona (o documento consolidado fala em 8 registros; validar 1:1 lá).

## 6b · Veredito dos erros Vercel (25/08 — diagnóstico fechado)

Os projetos **andre-corporate** e **alilove** estão git-linkados ao
`obsidian-importer` (repo de conteúdo) com framework Next/Preact — todo push
falha com `NEXT_NO_VERSION` / build ausente. **Ambos `live:false`, sem
domínio público** (andre-corporate serve só .vercel.app internos): a pilha
de ERRORs no painel nunca derrubou nada. **Cura definitiva:** Settings →
Git → Disconnect nos DOIS projetos (clique do dono). Nada no ar muda;
os pushes param de gerar erro; o PR fica limpo.

## 7 · Contexto irmão

O handoff do projeto Ali Love/The Spiral está em
`produtos/alilove/cinema5d/HANDOFF.md` — mesma branch. Os dois documentos
juntos são a continuidade completa para o Claude Code desktop.
