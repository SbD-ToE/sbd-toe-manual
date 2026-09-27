# tools/ — re-alinhar `out.json` de tradutores depois de um `prepare --force`

Quando o registo de termos ou `protected_tokens.py` mudam DEPOIS de os tradutores terem entregue os `out.json`, um
`prepare --force` gera jobs com marcadores novos (nomes/ids passaram a protegidos) e a numeração `⟦Pn⟧` desloca-se.
Ordem de aplicação, por directório de jobs:

1. `out_restore_markers.py <jobs-dir>` — substitui pelo marcador o texto protegido (ou a sua variante en-GB) que o
   tradutor deixou literal.
2. `out_drop_nonunits.py <jobs-dir>` — remove do `out.json` ids que deixaram de ser unidades traduzíveis (células só
   com o nome protegido).
3. `out_renumber_markers.py <job-base-path> <unit-id>` — para as unidades que o `assemble` ainda acusa («missing
   marker»): renumera os marcadores antigos pela ordem dos itens protegidos cuja forma literal NÃO está no texto.
4. `translate.py assemble … --write` e `translate.py check`.

Usados a 2026-09-25 para re-estampar os caps. 00–02 após os prefixos de id dos domínios e os nomes V1 protegidos.
