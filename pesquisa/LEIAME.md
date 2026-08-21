# Pesquisa — como o ciclo funciona

Três peças, uma alimenta a outra.

| Peça | Onde | O que faz |
|---|---|---|
| Skill `/analise-conteudo` | `.claude/skills/` | analisa link sob demanda, um ou dezenas |
| Fila | `FILA.md` | onde você cola link enquanto rola o feed |
| Achados | `achados/AAAA-MM-DD.md` | o que o briefing diário produziu |

## O ciclo

1. Você rola o feed e cola link na `FILA.md`. Sem organizar.
2. O briefing diário roda, lê a fila, analisa o que é novo.
3. Ele também busca sozinho nos assuntos de `NICHOS.md`.
4. Sai um arquivo em `achados/` e um resumo curto para você.
5. O que virar decisão vira tarefa; o resto fica registrado e some do caminho.

## O que a automação consegue e o que não consegue

**Consegue:** ler página pública — conta, data, legenda, curtidas, comentários.
Buscar na web por técnica nova. Cruzar um conjunto atrás de padrão. Propor
implementação nas marcas.

**Não consegue:** assistir vídeo. Rolar feed sozinha. Ver conteúdo privado ou
atrás de login. Transcrever áudio.

Por isso a fila existe: **a curadoria é sua, a análise é dela.** Você já faz a
parte que ela não faz — pesquisa muito, verifica fonte, acompanha discussão de
dev. Colar o link custa dois segundos e é o que liga uma coisa na outra.

## Custo

O briefing consome uso todo dia. Se ficar caro ou virar ruído, é só pedir para
pausar ou espaçar — não precisa apagar nada.
