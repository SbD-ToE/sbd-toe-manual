# Fila de termos `pending` — export para o hub

Gerado por `translation/scripts/terms_lint.py export-pending` a partir de `translation/terms/registry.yaml`.
`terms_sha256` do registo: `c069db4027d1da009208887a58c737daa2d252f0406175053a4fe87bb2e106e0`.

**Como responder:** no hub (`sbd-ai-runtime/handover/em-curso/`), por chave → EN decidido (e, se aplicável, PT).
O Manual agent regista a decisão no registo: espécie 2 passa a `coined` (com `ratified_by` e `date`); espécie 1 passa a
`in-record` ou `changed` (com `previous`). Enquanto `pending`, os blocos da fonte que contêm o termo não são traduzidos.

Total pendente: 19.

## `owner: archon` (0)

_Sem entradas._

## `owner: lead` (0)

_Sem entradas._

## `owner: manual-agent` (19)

| chave | espécie | razão | PT | EN actual | proposal | false_friends | senses |
|---|---|---|---|---|---|---|---|
| `apparatus` | 1 | polysemy |  | apparatus |  |  | aparato experimental (MCP, P0/P4/P5) · SHACL apparatus (conjunto de constraints, P6/P7) |
| `artifact` | 1 | polysemy |  | Artifact |  |  | tipo de entidade AppSec Core (ACA-*) — grafia «Artifact» (US) em P6/P7 · artefacto de investigação / de software (DSR) — grafia «artefact» (UK) em P6/P7 · traceability artifact — lacuna aparente que é falha de rastreabilidade, não de conteúdo (P2/P5) |
| `baseline` | 1 | polysemy |  | baseline |  |  | condição experimental de referência · estado de partida do ciclo / da ontologia · baseline de configuração segura (controlo) |
| `completeness_invariant` | 1 | polysemy |  | completeness invariant |  |  | completude do retrieval (invariante formal) · completude iterativa do Manual (P7 Purpose 2) · completude do domínio (negada como objectivo, P2 §7.3) |
| `compliance` | 1 | polysemy | conformidade | compliance |  |  | conformidade regulatória · contract compliance (invariantes do contrato) |
| `control_controls` | 1 | polysemy | controlo | control |  |  | controlo de segurança · factor controlado (experimental) |
| `coverage` | 1 | polysemy | cobertura | coverage |  |  | cobertura de requisitos normativos pelo corpus empírico (P1/P2/P4) · per-source coverage rate — proporção de itens de uma fonte que aterram na ontologia (P6/P7) · coverage adequacy vs domain completeness — distinção explícita (P2 §7.3) |
| `gate` | 1 | polysemy |  | gate |  |  | gate de release/CI (controlo) · gate de governação/admissão |
| `governance_protocol` | 1 | polysemy | governação | governance |  |  | governação da ontologia (protocolo) · governance substance (vista organizacional, fora da ontologia) |
| `grounding` | 1 | polysemy |  | grounding |  |  | LLM grounding — contexto entregue ao modelo (P3/P4/P5, dominante) · grounding metodológico da investigação em instâncias reais (Engström, P0) · substrate-grounding / lexical grounding — ferramenta do ciclo P7 (P6:221) e ontologia v2.6 |
| `harness` | 1 | polysemy |  | harness |  |  | security-requirements harness (consumidor) · evaluation/test harness (P4) |
| `integration_substrate` | 1 | polysemy |  | substrate |  |  | integration substrate = ontologia (P2/P3) · substrate = produto de dados do ciclo (P7) · practical substrate = o Manual (P0) |
| `mechanism` | 1 | polysemy |  | Mechanism |  |  | tipo de entidade AppSec Core (ACM-*) · genérico: mecanismo de retrieval/entrega/override |
| `pilot` | 1 | polysemy |  | pilot |  |  | pilot = registo de uma fonte (P2/P6/P7) · pilot = sessão-piloto de scoring (P4, genérico) |
| `practice` | 1 | polysemy |  | Practice |  |  | tipo de entidade AppSec Core (ACP-*) · uso genérico / de fonte («SSDF prescribes 20 practices», «in practice») |
| `promotion` | 1 | polysemy |  | promotion |  |  | promoção ACR (admissão à ontologia) · Release Promotion (slice ASC-09, sentido de release engineering) · promoção de ficheiro no mirror público (P5:17) |
| `structural_invariance` | 1 | polysemy | invariante | structural invariance |  |  | invariância estrutural entre slices (P1/P6) · invariante formal do contrato de retrieval (P3/P4/P5) |
| `tier` | 1 | polysemy |  | tier |  |  | tier de curadoria por fonte (P7) · Tier A–E de ferramentas do oráculo (P4) |
| `traversal` | 1 | en-vs-en-collision |  | traversal |  |  | algoritmo de retrieval por grafo (P3/P4/P5) · travessia de uma rede de mapeamentos fonte-a-fonte (custo do consumidor, P7 §12.3) |
