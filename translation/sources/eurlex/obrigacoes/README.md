# Obrigações por acto — texto oficial sic

Um ficheiro por acto do cross-check normativo (`cra`, `dora`, `nis2`, `aiact`, `rgpd`, `csa`). Cada obrigação tem um **id estável**
(p. ex. `DORA-RTS1774-21-e-iv`), a referência (artigo, número, alínea), o CELEX do acto de origem, a classe
(engenharia | organizacional | jurídico-contratual | autoridade) e o **texto oficial PT sic**, recortado por script dos textos
EUR-Lex desta pasta e de `secondary/`.

- **Quem lê:** as matrizes de cobertura em `manuals_src/docs/sbd-toe/002-cross-check-normativo/_matriz/<acto>.yaml`
  (schema `sbdtoe-reg-coverage/1`) referenciam cada obrigação pelo id e fixam o `sha256` do ficheiro em `fonte_obrigacoes`.
  A matriz nunca duplica o texto. `scripts/check_reg_context.py` falha se o sha256 não conferir ou se alguma obrigação
  não estiver na matriz nem em `excluidas`.
- **Elisões:** «[…]» separa trechos não contíguos. Entre o proémio de um número e a alínea citada, o texto junta-os pelo
  rótulo estrutural da alínea («…as seguintes condições: b) …»), sem «[…]». Cada trecho confere por correspondência exata.
- **Ids:** um id nunca muda. Uma obrigação que deixe de existir fica declarada como retirada na matriz; não se apaga.
- **Não editar à mão.** Uma correcção regenera o ficheiro, actualiza `MANIFEST.json` e o `sha256` da matriz no mesmo commit.

Origem e verificação: `MANIFEST.json`.
