# Textos oficiais EUR-Lex — actos do cross-check normativo

Versões PT e EN oficiais dos 6 actos citados em `002-cross-check-normativo/`, obtidas do EUR-Lex a 2026-09-26.
Servem de referência à **regra EUR-Lex** da tradução (termos e citações na forma EN oficial, identificados pela versão PT
oficial do MESMO artigo) e ao **lote jurídico** que o lead vai validar antes da 1.ª tag bilingue.

- `<CELEX>-<PT|EN>.txt` — texto integral extraído do HTML (considerandos, artigos, anexos).
- `<CELEX>-<PT|EN>.articles.json` — `{ "N": "<texto do Artigo N>" }`.
- `definitions.json` — pares PT↔EN dos artigos de definições, por número do ponto.
- `MANIFEST.json` — CELEX, acto, idioma, URL de origem, data de download, sha256 do HTML e de cada ficheiro.

Não é conteúdo publicado nem fonte do Manual. Não editar à mão: regenerar a partir do EUR-Lex e actualizar o manifesto.

## Legislação derivada — `secondary/`

Actos delegados, de execução e de alteração (RTS/ITS do DORA, NIS2 Reg. de Execução 2024/2690, EUCC e alterações, actos do CRA,
Omnibus do AI Act 2026/1744) e versões consolidadas (AI Act, CSA, EUCC — sem valor jurídico; autênticos são só os textos do JO),
PT e EN, no mesmo formato, com rectificações `R(NN)`, HTML de origem em `raw/` e `MANIFEST.json` (sha256 de cada ficheiro,
estado e datas por acto). Obtidos do EUR-Lex a 2026-09-26 por um agente do Orchestrator; copiados e verificados (186 sha256
conferidos contra o manifesto) pelo Manual agent. Ver `secondary/README.md`.
