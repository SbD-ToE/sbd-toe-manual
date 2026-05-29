---
id: ia-nos-testes
title: IA no Processo de Testes de Segurança
description: Como usar IA/GenAI para acelerar testes de segurança (planeamento, triagem, regressões, fuzzing e validação) sem degradar evidência, confidencialidade ou controlo humano
tags: [genai, ia, testes, seguranca, triagem, regressao, fuzzing, evidencias, governanca]
---

# 🤖 IA no Processo de Testes de Segurança (GenAI)

A adoção pervasiva de IA/GenAI no SSDLC altera profundamente **como produzimos e interpretamos evidência**.  
No domínio de testes de segurança isto é especialmente crítico, porque:

- o output dos scanners já era “ruidoso” (FP/FN), e a IA pode amplificar esse ruído se for usada como oráculo;
- os testes dependem de **contexto** (arquitetura, fluxos autenticados, dados sensíveis, compensating controls);
- a segurança exige **decisão humana rastreável**, e não “decisão automatizada” sem cadeia de responsabilidade.

Este addon prescreve como usar IA para acelerar e aumentar cobertura **sem substituir validação empírica** nem comprometer confidencialidade.

---

## 1) Princípios canónicos

### P1 - IA é “assistente”, não “decisor”
A IA pode propor: triagens, hipóteses, priorização, caminhos de reprodução, patch candidates, testes.  
A decisão final (corrigir/aceitar/suprimir/defer) é sempre humana e rastreável - ver **US-21** e **US-22** no lifecycle.

### P2 - Evidência tem de ser reprodutível sem IA
Qualquer finding confirmado tem de poder ser reproduzido por:
- teste automatizado (regressão),
- PoC mínima,
- log/artefacto determinístico (SARIF, HTTP transcript, crash dump, etc.).

### P3 - Dados sensíveis nunca entram “às cegas” num modelo
Prompts e contextos devem respeitar:
- minimização (apenas o necessário),
- redacção/masking,
- segregação de segredos (nunca colar tokens/headers reais),
- política organizacional de uso de IA (ver anexo transversal de políticas).

### P4 - Risco “modelo/supply chain” também é risco de segurança
Ferramentas de IA (cloud ou local) fazem parte da cadeia de confiança.
Devem existir controlos equivalentes aos aplicados a dependências e CI/CD:
- versionamento do modelo/config,
- logging de prompts/outputs (quando permitido),
- revisão de permissões e acessos,
- verificação de integridade/proveniência quando aplicável.

---

## 2) Casos de uso recomendados (e como fazer com segurança)

### 2.1 Triagem assistida (SAST/DAST/IAST/SCA/Fuzzing)
**Objetivo:** reduzir tempo de análise e melhorar consistência da decisão.

**Prática:**
- Fornecer à IA apenas:
  - ID do finding + regra/tool,
  - excerto mínimo do code path,
  - contexto técnico não sensível (padrão de autenticação, WAF existente, etc.),
  - política de severidade L1–L3 e critérios de gate.
- Exigir output estruturado (JSON/Markdown) com:
  - hipótese de exploitabilidade,
  - condições necessárias,
  - mitigação existente (se aplicável),
  - recomendação de validação empírica (passos concretos).

**Anti-padrão:** “IA disse que é falso positivo” sem prova.

**Evidência esperada:**
- decisão documentada via template (US-21 / T1),
- ligação a validação empírica (US-22 / T1–T5),
- registo de supressão com rationale e aprovador (se FP).

---

### 2.2 Geração assistida de testes de regressão de segurança
**Objetivo:** transformar findings corrigidos em proteção futura.

**Prática:**
- Pedir à IA para produzir:
  - esqueleto de teste (unit/integration/e2e),
  - payloads representativos,
  - asserts que comprovem falha antes e “pass” após correção.
- O developer valida e ajusta:
  - boundary conditions,
  - mocks/stubs,
  - fixtures seguras.

**Restrições:**
- Nunca aceitar código gerado sem revisão.
- Exigir que o teste referencia explicitamente:
  - o finding (ID),
  - o requisito relevante (Cap. 02),
  - o commit/PR de correção.

**Evidência esperada:**
- teste versionado,
- pipeline a executar regressões,
- relatório de execução anexado à release.

---

### 2.3 Assistência para autenticação em DAST (scripts/flows)
**Objetivo:** reduzir fricção em DAST autenticado e aumentar cobertura real.

**Prática:**
- A IA pode ajudar a construir um *login flow* genérico, mas:
  - credenciais reais não entram no prompt,
  - tokens/cookies reais são mascarados,
  - o fluxo final é testado em staging com conta técnica dedicada e rotação.

**Evidência esperada:**
- configuração do DAST versionada,
- cobertura por endpoints críticos,
- relatório DAST autenticado anexado à release.

---

### 2.4 Fuzzing assistido por IA (corpora, mutações e priorização)
**Objetivo:** aumentar capacidade de encontrar edge cases e crashes úteis.

**Prática:**
- IA para:
  - gerar seeds/corpora a partir de schemas (OpenAPI/GraphQL),
  - sugerir mutações (encoding, nesting, size),
  - priorizar endpoints por risco e histórico.
- Execução sempre em ambiente isolado, com:
  - limites de recursos,
  - logs completos,
  - dados não produção.

**Evidência esperada:**
- corpora versionada,
- crash repro + RCA,
- severidade ajustada com base em impacto real (DoS/RCE/etc).

---

### 2.5 Consolidação e deduplicação de findings multi-ferramenta
**Objetivo:** reduzir ruído e melhorar rastreabilidade.

**Prática:**
- IA pode sugerir clusters por:
  - CWE/CVE,
  - componente,
  - code path,
  - fingerprint.
- A regra de dedup final é configurada no sistema central (ex: DefectDojo) e não “na cabeça” do modelo.

**Evidência esperada:**
- regras de correlação versionadas,
- auditoria de merges/splits de findings,
- métricas FP/FN por tool ao longo do tempo.

---

## 3) Controlos obrigatórios quando se usa IA em testes

### C1 - Registo mínimo de “interação com IA” (quando permitido)
Para decisões de severidade ≥ HIGH (L2/L3), registar:
- objetivo do pedido,
- contexto fornecido (redigido),
- output relevante,
- decisão humana final + evidência (PoC/teste/log).

> Se a política de privacidade impedir logging, registar pelo menos: “IA usada” + tipo de apoio + evidência determinística sem prompt.

### C2 - Proteção contra prompt injection / conteúdo malicioso em artefactos
Quando a IA é alimentada com:
- logs,
- outputs de scanners,
- HTML/JS recolhido por DAST,
- payloads de fuzzing,

assumir que o conteúdo pode conter instruções maliciosas (“ignore regras…”, “exfiltra…”).  
Mitigação:
- sanitização,
- *content filtering*,
- execução em contexto “no tools / no network” sempre que possível,
- validação humana.

### C3 - Separação de ambientes e credenciais
IA usada para testes que interagem com runtime:
- só em staging isolado,
- com contas técnicas dedicadas,
- com segredos geridos por vault e nunca copiados.

### C4 - Proibição de “auto-merge” de correções de segurança
Qualquer patch gerado com IA:
- requer revisão humana,
- requer testes (incluindo regressão de segurança),
- nunca pode bypassar gates.

### C5 - *Eval suites* contínuas para agentes em desenvolvimento e produção {#c5-eval-suites}

Os controlos C1–C4 cobrem o caso em que **a IA assiste** quem testa. Quando o sistema **inclui um agente AI em produção** (ou quando o agente é parte do nosso processo de teste, e.g. um auditor de PR automatizado), precisamos de testar **o agente em si** — o mesmo princípio que aplicamos a qualquer outro componente crítico. A esta classe de testes chamamos *eval suites*; não substituem SAST/DAST/SCA, complementam-nos para a fatia agentic.

#### Princípios das *eval suites*

1. **Regressão de prompt como regressão de funcionalidade.** Cada mudança ao *system prompt*, *skill file*, *agent file* ou versão do modelo é tratada como mudança que pode degradar o comportamento; corre-se a *eval suite* antes do *merge* — exactamente como corremos testes de regressão antes de mudanças de código.
2. **Determinismo aproximado em ambiente de teste.** Modelos LLM não são determinísticos, mas em *eval* usamos `temperature=0` ou parametrização equivalente, e medimos com tolerância explícita (e.g. *exact match* vs *semantic match* vs *embedding similarity > k*). A tolerância é declarada por teste.
3. **Avaliação por domínio.** Cobrimos três classes mínimas: (a) **utilidade** — o agente cumpre a tarefa em casos esperados; (b) **segurança** — o agente recusa ou escala em casos hostis (prompt injection, jailbreak, off-policy); (c) **estabilidade** — o agente não degrada entre versões do modelo / prompt.
4. **Suite versionada e mantida.** A *eval suite* tem o mesmo estatuto que a suite de testes do sistema — vive em VCS, evolui com o produto, é revista periodicamente.

#### Composição mínima por nível

| Componente | A1 (assistente) | A2 (executa com confirmação) | A3 (autónomo + revert) | A4 (autónomo em prod) |
|---|---|---|---|---|
| **Regression tests de prompt** | Recomendado | Obrigatório | Obrigatório | Obrigatório (corrido a cada mudança) |
| **Abuse / red-team corpus** (*prompt injection*, *jailbreak*, *off-policy*) | — | Recomendado | Obrigatório | Obrigatório (com red-team manual periódico) |
| **Drift detection** entre versões (modelo, prompt, skill) | — | Recomendado | Obrigatório | Obrigatório (janelas curtas) |
| **A/B testing** antes de promoção de skill | — | Recomendado | Obrigatório | Obrigatório (com critérios pré-acordados) |
| **Test telemetry em produção** (correlacionar evals offline com sinais reais) | — | — | Recomendado | Obrigatório (cross-link Cap. 12) |

#### Aterragem operacional

- **Eval suite vive em VCS** ao lado do código que opera o agente. Mudanças à suite seguem o mesmo *code review* que mudanças ao código.
- **Corre em CI** antes do *merge* de mudanças a *system prompts*, *skill files*, *agent files*, ou após *bump* da versão do modelo. Falha bloqueia o *merge* (ou descida de nível de autonomia até estar resolvido).
- **Resultados arquivados** com `eval_run_id` ligado a `mandate_ref` — auditoria pode reconstruir que versão da suite confirmou que nível de autonomia.
- **Cobertura proporcional ao nível de autonomia** declarado no *mandate*. Subir nível sem *eval suite* à medida é proibido (cross-link Policy 38 §5.4).

#### Anti-padrões

- ❌ "*Vibe checks*" como única validação — corre alguns prompts manuais e dá-se por suficiente. Não fica registo, não detecta regressão.
- ❌ *Eval suite* que nunca falha — sinal de cobertura insuficiente, não de excelência. Adicionamos casos adversariais conhecidos para garantir cobertura útil.
- ❌ Métricas agregadas sem inspecção do corpus — *score* alto pode esconder falhas catastróficas em sub-categorias críticas.
- ❌ *Eval suite* num repositório separado da skill/prompt — abre porta a *drift* silencioso.

#### Onde aterra no resto do manual

- **Cap. 02** — `REQ-AGN-002` exige nível de autonomia justificado; a *eval suite* é a evidência de que o nível é defensável.
- **Cap. 07** — *eval run* obrigatório como *gate* antes de *merge* de mudanças a skill/prompt (cross-link US-19).
- **Cap. 12** — sinais agentic em produção (jailbreaks reais, off-policy actions) realimentam a *eval suite* offline.
- **Policy 19 — Estratégia de Testes** acrescenta o capítulo `eval suites` ao escopo de testes obrigatórios.

> 🧭 Em curto: testar o agente é testar um componente do sistema. A *eval suite* não é trabalho extra — é o trabalho de teste normal aplicado à fatia que opera por linguagem. Sem ela, não temos como sustentar uma classificação A2+ ao longo do tempo.

---

## 4) Integração explícita com este capítulo

Este addon reforça diretamente:

- **US-10/US-11** (centralização e feedback) - IA pode acelerar triagem e reduzir ruído, sem perder rastreabilidade.
- **US-21** (decisão assistida) - IA alimenta hipótese; decisão é humana, documentada.
- **US-22** (validação empírica) - IA sugere como validar; confirmação é sempre por PoC/teste.

---

## 5) Checklist de adoção (binário)

| Item | Sim/Não |
|------|:------:|
| Uso de IA em testes está coberto por política organizacional (minimização, dados, logging) |  |
| Existe template de decisão humana (CORRIGIR/ACEITAR/SUPRIMIR/DEFER) aplicado a findings críticos/altos |  |
| Existe procedimento de validação empírica por tipo de teste (SAST/DAST/IAST/Fuzzing/PenTest) |  |
| Há segregação de ambientes e contas técnicas para DAST/IAST/fuzzing com rotação de credenciais |  |
| Prompts nunca incluem segredos/PII; existe processo de redacção/masking |  |
| Outputs de IA não são usados como “prova” sem artefacto determinístico reprodutível |  |
| Patches gerados por IA nunca fazem auto-merge e passam por revisão + testes |  |
| Existe métrica FP/FN e tempo de decisão/validação por severidade e por L1–L3 |  |

---

## 6) Notas finais

A IA pode ser um multiplicador brutal de produtividade em testes de segurança - **se** for usada como acelerador de análise e geração de artefactos, e não como substituto de evidência e responsabilidade.

O critério de sucesso não é “menos trabalho humano”, mas sim:
- **mais cobertura**, 
- **menos tempo até confirmação**, 
- **melhor rastreabilidade**, 
- **menos decisões não fundamentadas**.
