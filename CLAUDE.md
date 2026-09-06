# Claude Code — contrato deste repositório

**Leia `MAPLE-OS.md` (raiz) ANTES de qualquer edição.** Ele é a
constituição: memória (§1), papéis (§2), gate de aprovação humana (§3),
anti-falha (§4). Este arquivo só resume o que muda para o Claude.

## Regras operacionais imediatas

1. **Fonte de verdade = este repo, branch `master`.** Trabalhe sempre em
   branch própria; NUNCA commit direto no master; merge só o André.
2. **Antes de editar uma frente, leia o handoff dela** (mapa no
   MAPLE-OS.md §1). As frentes principais:
   `produtos/alilove/cinema5d/HANDOFF.md` ·
   `docs/climbex/DNS-HANDOFF.md` · `produtos/princeandre/`.
3. **Gate (§3 do MAPLE-OS.md)**: produção, DNS/domínio, ENVIAR qualquer
   mensagem/e-mail, dinheiro, direitos de música/imagem, deleção de
   originais, contratos — pare e peça APROVADO ao André. Rascunho pode;
   envio jamais. Na dúvida: é gate.
4. **Fim de sessão**: commit + push + uma linha com o hash (ou o erro
   exato). Falha silenciosa é proibida.
5. **The Spiral** (`produtos/alilove/cinema5d/`): fonte única é
   `cinema5d-src.html`; build com `ferramentas/monta.py`; testes
   Playwright em `ferramentas/`; direitos de música são fail-closed no
   código — não afrouxe. Estrutura das 11 seções do site é intocável;
   só se acrescenta.
6. **Não inventar** fato, preço, data, título, crédito ou percurso.
   Marcas não se misturam; Climbex nunca aparece em peça do Ali Love.
