# Codex — contrato deste repositório (Maple OS)

**Leia `MAPLE-OS.md` (raiz) antes de qualquer edição.** Papel do Codex no
sistema (§2): trabalho PONTUAL e bem delimitado — reconhecimento de repo,
refactor mecânico pedido explicitamente, segunda opinião técnica.

## Limites rígidos

1. **NUNCA**: push/commit em `master`; deploy; mexer em DNS/domínio;
   enviar e-mail/mensagem; gastar dinheiro; instalar dependência nova sem
   pedir; deletar ou sobrescrever arquivo que não criou; editar
   `CENTRAL_DE_CONTROLE.md`.
2. **`produtos/alilove/cinema5d/`** só depois de ler o
   `HANDOFF.md` da pasta — e sem tocar nas regras de direitos
   (MusicAssetRights fail-closed) nem na estrutura das 11 seções.
3. Trabalhe em branch própria com prefixo `codex/`; entregue diff pequeno
   e descrito; teste com `python3 produtos/alilove/cinema5d/ferramentas/monta.py`
   + `node --check` quando tocar no Spiral.
4. Qualquer coisa listada no gate (§3 do MAPLE-OS.md) → pare e devolva ao
   André com o pedido no formato padrão. Na dúvida: é gate.
5. Falha silenciosa é proibida: erro se reporta com a mensagem exata.
6. Não inventar fato, preço, data, título ou crédito. Segredo comercial:
   o stack interno chama-se apenas "stack Climbex".
