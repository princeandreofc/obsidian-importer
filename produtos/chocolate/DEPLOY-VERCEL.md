# Chocollate × Bem Bolado — publicação

## Conteúdo
- `index.html`: landing pública da campanha “O Cacau é Nosso”.
- `dossie.html`: fonte editorial do dossiê de patrocínio (9 páginas A4, preparado para impressão pelo navegador).
- `oficio.html`: ofício formal de solicitação de patrocínio, com campos não confirmados preservados.
- `scripts/build-static.mjs`: gera a pasta `dist/` para hospedagem estática.

## Build
Requer Node.js 20+:
```sh
npm run build
```
Publique `dist/` como diretório estático. O projeto pode ser importado na Vercel como “Other”/Static Site com comando de build `npm run build` e output directory `dist`.

## Rotas
- `/` campanha
- `/dossie/` dossiê editorial
- `/oficio/` ofício

## Gates e limitações
- O e-mail ao patrocinador é somente rascunho; envio depende de autorização expressa do responsável.
- Não há valores de cotas em nenhuma peça.
- Nome civil do artista, nome do responsável Bem Bolado, cidade e data permanecem como placeholders.
- Fotografia, vídeo, áudio, biografia e dados de lançamento do artista precisam ser validados no acervo autorizado antes da versão definitiva do EPK. Não publicar suposições.
- Não afirmar números de audiência estimada sem analytics/documentos do artista e da marca. A proposta usa métricas e linha de base a preencher.
- Alegações de sustentabilidade devem ter comprovação documental.
- Os arquivos PDF existentes no histórico da branch são versões anteriores; gerar PDFs finais a partir das fontes HTML e inspecioná-los antes de encaminhar.

## Publicação
A conexão atual permite atualizar GitHub, mas não fornece ferramenta Vercel nesta sessão. Configure a importação do repositório `princeandreofc/obsidian-importer`, branch `claude/organizar-computador-26sev2`, root directory `produtos/chocolate`, build command `npm run build`, output directory `dist`.
