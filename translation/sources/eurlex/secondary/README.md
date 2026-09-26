# Textos oficiais EUR-Lex — legislação derivada (DORA, NIS2, CSA, CRA, AI Act)

Versões PT e EN oficiais dos actos delegados, de execução e de alteração dos 5 actos-base já guardados em
`SbD-ToE-Manual/translation/sources/eurlex/`, obtidas do EUR-Lex a 2026-09-26. Servem para verificar afirmações jurídicas do Manual.
Mesmo formato da pasta de referência.

- `<CELEX>-<PT|EN>.txt` — texto integral extraído do HTML oficial (considerandos, artigos, anexos).
- `<CELEX>-<PT|EN>.articles.json` — `{ "N": "<texto do Artigo N>" }` (inclui artigos inseridos, ex. `4a`; conteúdo final/anexos anexado ao último artigo, como na referência).
- `<CELEX>R(NN)-<PT|EN>.txt` — rectificações PT/EN (não incorporadas nos textos; ler em conjunto).
- `0<...>-<data>` — versões consolidadas (Serviço das Publicações): instrumento de documentação, sem valor jurídico. Autênticos são só os textos do JO.
- `raw/` — HTML de origem exacto (sha256 no manifesto) e páginas de procedimento legislativo EUR-Lex.
- `MANIFEST.json` — por acto: CELEX, títulos PT/EN, referência e data do JO, entrada em vigor, estado (in force), aplicação, artigos;
  por ficheiro: URL de origem, data de download, sha256 do HTML e do ficheiro derivado; estado das propostas (Digital Omnibus, CSA2, NIS2-alteração); o que não existe/não foi obtido.

Todos os textos estavam disponíveis em HTML oficial; nenhum PDF foi necessário.
Não é conteúdo publicado nem fonte do Manual. Não editar à mão: regenerar a partir do EUR-Lex e actualizar o manifesto.
