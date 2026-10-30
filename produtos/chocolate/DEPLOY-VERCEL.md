# Chocollate × Bem Bolado — publicação

## Rotas estáticas
- `/`: landing da campanha
- `/dossie/`: dossiê de patrocínio em HTML para leitura e impressão
- `/oficio/`: ofício de solicitação em HTML para leitura e impressão

## Build
Requer Node.js 20+:
```sh
npm run build
```
O build recria `dist/` e copia as três rotas. O diretório `dist/` é a saída de publicação.

## Configuração Vercel
- Framework preset: Other
- Root Directory: `produtos/chocolate`
- Build Command: `npm run build`
- Output Directory: `dist`
- Node.js: 20.x ou superior

O repositório contém `vercel.json` com o comando e diretório de saída. A criação de preview automático depende de o projeto Vercel estar conectado ao repositório e de a branch estar autorizada.

## Materiais comerciais
- Fontes dos materiais: `dossie-src.html`, `oficio-src.html`, além das rotas publicáveis `dossie.html` e `oficio.html`.
- PDF final de 9 páginas e ofício de 1 página foram preparados separadamente para envio, com os nomes:
  - `DOSSIE-CHOCOLLATE-X-BEMBOLADO.pdf`
  - `OFICIO-PATROCINIO-001-2026.pdf`
- O e-mail em `EMAIL-DONO-BEMBOLADO.md` é apenas rascunho; não enviar sem aprovação expressa.

## Gates antes da divulgação
- Não há valores de cotas em nenhuma peça.
- Cidade/data e responsável da Bem Bolado permanecem como placeholders no ofício.
- Nome civil do artista permanece como placeholder.
- Biografia, fotos, vídeo, áudio, capa e créditos do artista precisam ser validados no acervo autorizado. Não publicar suposições.
- Não afirmar números de audiência sem analytics dos canais do artista e da marca. O dossiê propõe linha de base, indicadores e relatório por fase.
- Origem, lote, ingredientes, alergênicos, rotulagem e práticas socioambientais só podem ser comunicados com comprovação e autorização.
- Mock de embalagem é conceitual; não representa produto homologado.

## Estado de deploy
O GitHub foi atualizado na branch `claude/organizar-computador-26sev2`. Não foi possível executar ou confirmar um deploy Vercel nesta sessão; a publicação depende do projeto Vercel conectado e de suas permissões.
