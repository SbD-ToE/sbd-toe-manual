---
id: recomendacoes-avancadas
title: Recomendações Avançadas - Arquitetura Segura
description: Práticas avançadas para contextos de elevada maturidade em arquitetura segura
tags: [avancado, arquitetura, maturidade, zero-trust, sbomm]
sidebar_position: 30
---

# Recomendações Avançadas - Arquitetura Segura

Este documento complementa as práticas fundamentais do capítulo com recomendações orientadas a contextos de **elevada maturidade organizacional**, sistemas críticos ou ambientes regulamentados.

> As recomendações aqui descritas são opcionais, mas altamente desejáveis para equipas que já aplicam os requisitos ARC de forma consistente.

---

## 🧱 Recomendações Arquitetónicas Avançadas

| Prática / Recomendação                             | Benefício direto                             | Requisitos reforçados |
|------------------------------------------------------|------------------------------------------------|------------------------|
| Adotar o princípio de Zero Trust entre microserviços  | Reduz risco de lateral movement                | ARC-002, ARC-006       |
| Aplicar OPA ou rego para enforcement dinâmico        | Governa políticas de acesso da arquitetura       | ARC-001, ARC-008       |
| Usar sidecars para segurança e comunicação interservice | Cria controlo de rede e logging distribuído   | ARC-002, ARC-003       |
| Aplicar segmentação em ambiente de CI/CD             | Garante que a execução reflete o desenho arquitetónico | ARC-004, ARC-007 |
| Integrar threat modeling em stories e epics          | Deteta falhas antes do desenho detalhado       | ARC-005, ARC-010       |
| Formalizar ADRs para todas as decisões de arquitetura  | Melhora auditabilidade e revisão futura        | ARC-004, ARC-011       |
| Validar consistência entre arquitetura e SBOMs       | Garante que o SBOM reflete a arquitetura planeada | ARC-006, ARC-007       |

---

## 🧩 Modelos e Frameworks Recomendados

- **Modelo de Confiança por Contexto** (Context-Aware Trust Models)
- **Architecture Decision Records (ADRs)** com integração Git
- **Modelos de Zoneamento Baseado em Risco**
- **Threat Modeling como parte da Definition of Done**
- **Frameworks**: SABSA, ISO/IEC 42010, NIST SP 800-160 Vol 1
- **SBOMM** (Security BOM Maturity Model) - integração entre arquitetura e composição de software

---

## ✅ Quando aplicar estas recomendações?

- Ambientes regulamentados (financeiro, saúde, defesa)
- Arquiteturas distribuídas de alta complexidade (ex: multicloud, event-driven)
- Plataformas com alto volume de integração externa
- Organizações com função de arquitetura ou segurança dedicada

> 🧭 Estas recomendações alinham com os níveis mais elevados de maturidade em SAMM, SSDF e DSOMM.

---

## 🤖 Padrões arquitetónicos para sistemas AI/ML {#ai-ml}

Sistemas que integram componentes de inteligência artificial — LLMs em interface conversacional, modelos preditivos, sistemas de retrieval-augmented generation (RAG), agentes autónomos com tool invocation — introduzem padrões arquitetónicos com superfícies de ataque qualitativamente distintas das aplicações tradicionais. As recomendações nesta secção complementam (não substituem) ARC-001..ARC-013 e operacionalizam o requisito [ARC-014](./addon/catalogo-requisitos-arquitetura#arc-014).

### Trust zones em arquitecturas AI/ML

Componentes AI/ML introduzem três classes de fronteira de confiança que devem ser explicitamente marcadas em DFDs:

| Boundary | Descrição | Ameaças canónicas | Controlos arquitectónicos típicos |
|---|---|---|---|
| **Training-time** | Entre datasets externos e pipeline de treino | Training data poisoning (`AML.T0020`); Publish Poisoned Datasets (`AML.T0019`); ML02-2023 Data Poisoning | Curadoria de fontes; checksum/signature de datasets; isolamento de pipeline de treino; revisão humana antes de retraining |
| **Inference-time** | Entre input externo (utilizador, RAG retrieval, file ingestion) e contexto do modelo | Prompt injection directa e indirecta (LLM01-2025; `AML.T0051.001`); `AML.T0093` Prompt Infiltration via Public-Facing App | Input sanitization específico para prompt context; separação clara entre system prompt e user input; output filtering anti-extracção de system prompt |
| **Agentic** | Entre output do modelo e tool invocations executadas (functions, MCP servers, APIs) | Exfiltration via AI Agent Tool Invocation (`AML.T0086`); AI Agent Tool Poisoning (`AML.T0110`); Data Destruction via AI Agent (`AML.T0101`); LLM06-2025 Excessive Agency | Aprovação humana para acções write/mutativas; rate limiting por tool; allowlist de tool scopes; logging completo de tool calls (ver Cap. 12 — observabilidade AI) |

### Boundary controls para prompt injection

Prompt injection é a vulnerabilidade arquitectónica mais comum em aplicações LLM. Controlos arquitectónicos relevantes:

- **Separar canalmente** system prompt (configuração da aplicação) de user input (dados não confiáveis) — usar mensagens estruturadas (ex: roles `system`/`user`/`assistant`) em vez de string concatenation
- **Tratar todo conteúdo retrieval-augmented como user-level untrusted** — em sistemas RAG, documentos retornados são dados externos; aplicar mesmos controlos que ao input directo do utilizador (`AML.T0051.001` Indirect Prompt Injection)
- **Output filtering** anti-extracção de system prompt (`AML.T0069.002`); detectar padrões de exfiltração de instruções
- **Confidentialidade de system prompts** — não assumir que o conteúdo é secreto; arquitectar como se fosse público

### LLM ↔ backend tool invocation security

Agentes AI com capacidade de invocar tools backend (APIs, file systems, databases via MCP, function calls) exigem isolamento arquitectónico análogo a controlo de privilégios em sistemas tradicionais:

- **Princípio de menor privilégio aplicado a agentes** — cada tool exposta a um agente AI deve ter scope mínimo necessário; agentes não devem operar com credentials de utilizador real (LLM06-2025 Excessive Agency)
- **Aprovação humana out-of-band** para tool calls com impacto crítico (delete, transfer, send) — particularmente relevante em workflows em que o agente é autónomo
- **Auditoria completa de tool invocations** — cada chamada com timestamp, contexto, agent identity, scope; integrar com pipeline de observabilidade do Cap. 12 (`AML.M0024` AI Telemetry Logging)
- **Validação de MCP servers e tools** como dependências de supply chain — ver Cap. 5 §AI/ML para framing supply chain (`AML.T0110` AI Agent Tool Poisoning)

### Considerações de design

- **AI components NÃO são bibliotecas opacas** — devem aparecer como participantes distintos em DFDs de arquitectura, com inputs, outputs, dependências (modelos, datasets, prompts) e trust boundaries explicitamente modeladas
- **Cross-zone propagation** — outputs de modelos AI podem propagar-se a zonas de confiança elevada (ex: model output usado para tomar decisões automáticas em sistemas críticos); aplicar mesma análise de propagation que aplicaria a inputs externos não confiáveis
- **Resiliência a model degradation** — design considera fallback para quando o modelo está indisponível, retorna outputs degradados, ou foi comprometido (`AML.T0031` Erode AI Model Integrity)

> A análise de threat modeling para arquitecturas AI/ML usa MITRE ATLAS como complemento a STRIDE — ver [Cap. 03 — Metodologias AI/ML](../threat-modeling/addon/metodologias-e-ferramentas#ai-ml).

### Padrões para agentes AI como *principals* (ARC-015) {#agentes-principals}

Os padrões acima cobrem *componentes AI/ML* em geral. Quando o sistema tem **agentes autónomos** que executam acções com efeito real — invocar tools, criar PRs, ler segredos, fazer deploy, escrever em sistemas externos — adoptamos uma postura arquitectónica diferente: tratamos o agente como **mais um *principal* não-humano**, sujeito aos mesmos princípios que aplicamos a *workload identities* tradicionais, especializados para o caso em que quem decide a próxima acção é um modelo.

Esta secção operacionaliza o requisito [ARC-015](./addon/catalogo-requisitos-arquitetura#arc-015) e cruza com os requisitos `REQ-AGN-001..004` definidos no [Cap. 02 — Modelo de níveis de autonomia](../requisitos-seguranca/addon/governanca-automatismos#niveis-autonomia).

#### Identidade do agente — workload identity efémera

- **Identidade dedicada por agente** (e por ambiente). O agente recebe credenciais via **OIDC / workload identity**, com TTL ≤ 1h, sem reutilização de identidade humana. Princípio idêntico ao US-04 do Cap. 07 e ao US-10 do Cap. 08 — aplicado a um novo tipo de *principal*.
- **Scope mínimo por tool** (e por ambiente, ver `ARC-011`). Um agente que precisa de abrir PRs **não recebe** *scope* para apagar o repositório; um agente que opera em *staging* **não vê** credenciais de *production*. Sem excepções tácitas.
- **Revogação por *kill-switch*** (ver [`REQ-AGN-003`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn)) tem de ser arquitectonicamente possível em segundos — i.e. a revogação de credenciais não pode depender de redeploy ou de propagação eventual.

> A regra que aplicamos para *workload identity* humana — *"se temos de partilhar a credencial, o desenho está errado"* — vale literalmente para agentes. Se dois agentes partilham a mesma identidade, o *audit trail* deixa de ser útil.

#### Intent declaration antes de tool calls destrutivos

Em níveis A2+, antes de cada *tool call* com efeito destrutivo, *side-effectful* ou em sistemas externos críticos, o agente declara à infraestrutura **o que vai fazer e porquê**. O *intent* é um evento estruturado, registado em audit, com (no mínimo): identidade do agente, *tool* a invocar, argumentos materiais, *intent* humano-legível, *expected outcome*, *risco residual* na perspectiva do agente. O *gate* operacional valida *intent* declarado vs *acção real executada* a posteriori — divergência é sinal de incidente.

| Campo do *intent event* | Propósito |
|---|---|
| `agent_id` | Identidade do *principal* (ARC-015) |
| `mandate_ref` | Versão do *mandate* sob o qual o agente opera ([`REQ-AGN-001`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn)) |
| `tool` + `args` | O que vai ser invocado e com que argumentos materiais |
| `intent` | Frase humano-legível: "vou fazer X para resolver Y" |
| `expected_outcome` | Estado pós-acção esperado |
| `risk_self_assessment` | O que o agente considera como risco residual da acção |

Este desenho não pede que o agente *peça permissão* a cada passo — pede que **deixe rasto** do que tencionava fazer antes de o fazer. A diferença é operacional: permite-nos comparar intenção e acção, e detectar comportamento off-policy mesmo quando a acção isolada parece legítima.

#### Aprovação humana out-of-band

Para acções com efeito crítico (delete, transfer, send, deploy, rotate-secrets, contactar sistemas externos sensíveis), exigimos aprovação **fora do canal do agente** — Slack approval, GitHub review com 2FA, webhook assinado, *push notification* a humano de plantão. A razão é simples: se o canal de aprovação é o mesmo onde o agente actua, a aprovação está sujeita ao mesmo conjunto de adversários do canal principal (prompt injection inclusive). Out-of-band força um *humano real, num canal independente*, a confirmar.

#### Kill-switch operacional

O *kill-switch* ([`REQ-AGN-003`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn)) é um mecanismo arquitectónico, não um botão simbólico. Compõe-se de:

- **Revogação imediata de credenciais** (revogação do token OIDC; *workload identity* binding invalidado em segundos).
- **Terminação do *runtime*** do agente (sessão MCP encerrada; *worker* terminado).
- **Isolamento do *namespace*** onde o agente operava (impedir reanimação até diagnóstico).
- **Sinal operacional** (alerta on-call) para garantir que humano sabe que disparou.

Em A3/A4 exercitamos o *kill-switch* em sandbox/staging com cadência registada (≥ 1×/trimestre para A3, ≥ 1×/mês para A4). Sem este exercício, o *kill-switch* é decorativo.

#### Audit completo por tool invocation

Cada *tool call* gera um *audit event* estruturado — não basta logar "agente fez algo". Sugerimos como mínimo:

- `timestamp`, `agent_id`, `session_id`, `mandate_ref`, `autonomy_level` (A0–A4)
- `tool`, `tool_version`, `args` (com redação de PII e segredos)
- `intent_event_ref` (referência ao *intent* declarado, se A2+)
- `outcome`: success / failure / timeout / rejected_by_gate; payload de retorno (resumido)
- `external_effect`: se o tool afectou sistema externo, qual e como (URL, recurso, mudança de estado)

Estes eventos alimentam directamente a observabilidade do Cap. 12 (a aterrar na v1.6.0 — `REQ-MON-AI-*`) e a evidência de auditoria operacional periódica (Cap. 14).

> 🧭 Tudo o que descrevemos nesta secção é especialização do que já praticamos para identidades não-humanas tradicionais. Se a equipa já tem maturidade em OIDC + scope mínimo + audit por invocação, falta-lhe apenas reconhecer o agente como mais um *principal* a passar pelo mesmo crivo — e adicionar *intent declaration* e *kill-switch* exercitado, que são as duas peças genuinamente novas.

### Padrões para sistemas RAG (*Retrieval-Augmented Generation*) {#rag-patterns}

RAG é hoje a arquitectura dominante em aplicações LLM em produção — o modelo recebe, além do *prompt* do utilizador, conteúdo recuperado de uma fonte externa (base de documentos, vector DB, *knowledge base* corporativa) que enriquece o contexto. A vantagem operacional é clara: respostas baseadas em informação actual da organização sem re-treinar o modelo. O preço é que **a fronteira `inference-time` deixa de ser uma só** — passam a existir duas entradas distintas no contexto do modelo, com graus de confiança muito diferentes, e ambas merecem tratamento como *user-untrusted*.

Esta secção complementa o que já dissemos sobre [trust zones em arquitecturas AI/ML](#ai-ml) e [boundary controls para prompt injection](#boundary-controls-para-prompt-injection), com a especialização operacional para RAG.

#### O que muda em RAG

| Componente novo | O que introduz | Porque importa para segurança |
|---|---|---|
| **Vector DB / *index store*** | Armazena *embeddings* + chunks de documentos | Novo activo da supply chain; controlo de acesso e integridade dedicados |
| ***Embedding model*** | Converte query e documentos em vectores | Dependência adicional na cadeia (model registry); *pinning* obrigatório |
| ***Retriever*** | Selecciona top-k chunks por similaridade vectorial | Determina o que entra no contexto do LLM; *attack surface* nova |
| ***Re-ranker*** (opcional) | Re-ordena chunks recuperados | Ponto adicional de manipulação se baseado em modelo |
| ***Document corpus*** | Fonte de conteúdo a ingerir | Vector primário de *indirect prompt injection* (`AML.T0051.001`) |

#### Padrões arquitectónicos para RAG seguro

- **Tratar *retrieved content* como *user-untrusted* por desenho** — em RAG, o documento recuperado entra no contexto do modelo como se fosse texto do utilizador. Aplica-se literalmente o controlo da secção [boundary controls para prompt injection](#boundary-controls-para-prompt-injection): separação canónica `system` / `user` / `retrieved_context` quando o modelo suporta (Anthropic *documents* parameter, OpenAI *tool messages*) — não fazer *string concatenation*. Onde o modelo não distingue estruturalmente, isolar com *delimiters* + *prompt hardening* no *system prompt*.
- **Curadoria da ingestão** — documentos ingeridos no corpus passam por um *pipeline* de curadoria: validação de origem, *content scanning* para padrões adversariais conhecidos (LLM01-2025 *indirect prompt injection* patterns), classificação de sensibilidade. Não tratar a ingestão como *trusted by default*.
- **Vector DB como activo crítico** — controlo de acesso (autenticação + autorização per-namespace), *audit log* de leituras e escritas, encriptação *at-rest* e *in-transit*, integridade dos *embeddings* (hash sobre o conteúdo original que originou cada *embedding*).
- ***Embedding model* pinned** — versão fixa explícita (cross-link [`DEP-013`](../dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-013)). Mudança de versão maior do *embedding model* obriga a re-indexar o corpus inteiro e a re-correr *eval suite* RAG (ver abaixo) — *embedding spaces* não são compatíveis entre versões maiores.
- ***Retriever* com filtros de autorização** — top-k retrieval respeita *row-level security* / *namespace boundary* do utilizador que faz a query. Falha clássica em RAG corporativo: utilizador A consegue ver chunks que pertencem ao perímetro do utilizador B porque o retriever não filtra. Tratamos como *access control* normal.
- ***Output filtering* anti-extracção de corpus** — detectar padrões em que o modelo está a regurgitar conteúdo do corpus sem o tratar (potencial *membership inference* sobre que documentos estão no índice, ou *exfiltration* dirigida).
- ***Provenance* no output** — quando o modelo cita documentos do corpus, expor *provenance* (que documento, que chunk) ao utilizador. Tem dupla função: auditabilidade e dificultar exfiltração silenciosa.

#### Threats específicas a RAG

Adicionamos à [threat library agentic do Cap. 03](../threat-modeling/addon/metodologias-e-ferramentas#playbook-agentic) os seguintes vectores RAG-específicos:

| Threat | ID | Fronteira-alvo | Mitigação primária |
|---|---|---|---|
| ***Indirect prompt injection* via documento ingerido** | `AML.T0051.001` · LLM01-2025 | Inference (via retrieval) | Curadoria da ingestão; tratar *retrieved content* como *user-untrusted*; *output filtering* |
| ***Embedding poisoning*** (training-time do *embedding model* ou ingestion-time do corpus) | `AML.T0020` (adaptado) | Training-time / Ingestion-time | *Embedding model* de fonte aprovada ([`DEP-014`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-014)); validação da ingestão |
| ***Vector DB exfiltration*** | `AML.T0086` (adaptado) | Vector DB | Controlo de acesso + audit; *row-level security* no retriever |
| ***Membership inference* sobre o corpus** | LLM02-2025 (*sensitive info disclosure*) | Inference | *Output filtering*; rate-limiting; detecção de *probing queries* |
| ***Cross-namespace contamination*** | LLM06-2025 (*excessive agency*, em variante RAG) | Retriever | Filtro de autorização no top-k retrieval |

#### Eval suite para RAG

A *eval suite* (Cap. 10 §C5) ganha em RAG uma camada própria:

- ***Retrieval relevance*** — top-k contém chunks relevantes para a query?
- ***Citation faithfulness*** — o output cita correctamente os chunks recuperados, sem inventar conteúdo?
- ***Adversarial documents corpus*** — documentos com tentativas conhecidas de *indirect prompt injection* devem ser detectados ou neutralizados sem alterar o comportamento do modelo.
- ***Cross-namespace isolation*** — query do utilizador A nunca retorna chunks do namespace de B.

Para sistemas A2+ que invocam *tools* a partir de contexto RAG, esta camada da *eval suite* é obrigatória — porque o vector de ataque mais comum em produção é precisamente *"documento envenenado leva o agente a invocar tool destrutiva"*.

> 🧭 RAG vê-se frequentemente como "apenas adicionar contexto ao prompt". Tecnicamente é mais do que isso: introduz uma nova fronteira de confiança (`retrieved_context`) que tem o mesmo poder de manipular o modelo que o input do utilizador, mas chega por um canal que parece interno. É essa assimetria que torna RAG seguro um problema arquitectónico distinto.

### Nota sobre sistemas multi-agente

*Frameworks* de orquestração multi-agente (*LangGraph*, *CrewAI*, *AutoGen*, *orchestrator → executor → reviewer* construídos sobre SDKs próprios) tornaram-se comuns durante 2024–2025 e continuam em evolução rápida. Não escrevemos uma secção dedicada porque o espaço de soluções **ainda não estabilizou** — convenções de *agent-to-agent communication*, *trust delegation* entre agentes e supervisão hierárquica variam significativamente entre *frameworks*. O nosso princípio operacional é, no entanto, estável:

- **Cada agente no sistema é um *principal* distinto** ([`ARC-015`](./addon/catalogo-requisitos-arquitetura#arc-015)) com identidade, *mandate* (Policy 38) e nível A0–A4 próprios. Um orquestrador não "empresta" as suas credenciais a um sub-agente.
- ***Trust delegation* explícita** — quando um agente invoca outro, a chamada é tratada como *tool call* (auditada por [`OPS-012`](../monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-012)), com `intent` declarado quando destrutiva.
- ***Out-of-band approval* no agente que executa**, não no orquestrador — a aprovação humana é exigida no ponto onde a acção destrutiva acontece, não no ponto onde foi decidida.

Quando os padrões multi-agente estabilizarem (provavelmente 2026–2027), revisitaremos para extrair uma secção dedicada com base na prática operacional acumulada.

---

## 📌 Consideração Final

Estas práticas não substituem os requisitos normativos (ARC), mas representam **próximos passos naturais para equipas que já aplicam arquitetura segura de forma estruturada e consistente**.

> Aplicar estas recomendações de forma seletiva pode acelerar a maturidade e prepara a organização para modelos de governaça baseados em evidência e controlo distribuído.
