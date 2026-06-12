---
id: aplicacao-lifecycle
title: Como Fazer
description: Integração do threat modeling ao longo do ciclo de desenvolvimento
tags: [tipo:aplicacao, ciclo-vida, threat-modeling, requisitos, mitigacao, rastreabilidade]
genia: us-format-normalization
---


# Aplicação de Threat Modeling no Ciclo de Vida

Este anexo prescreve **como aplicar sistematicamente as práticas de Threat Modeling definidas no Capítulo 3** ao longo do ciclo de desenvolvimento, garantindo rastreabilidade, proporcionalidade ao risco e integração com os requisitos de segurança.

Inclui modelos reutilizáveis de user stories, ações por papel, artefactos esperados e quadros de aplicação por nível de criticidade (L1–L3).

---

## 📅 Quando aplicar Threat Modeling

| Fase / Evento                    | Ação esperada                                                                 | Quem participa                                                     | Evidência mínima (artefacto principal) |
|----------------------------------|------------------------------------------------------------------------------|--------------------------------------------------------------------|----------------------------------------|
| Início de projeto / épico        | Criar baseline do Threat Model e definir âmbito/assunções                     | DevOps / SRE, Product Owner, Arquitetos de Software, AppSec Engineer, Scrum Master / Team Lead           | DFD + lista inicial de ameaças + registo de decisão (*baseline*) |
| Grooming / Planeamento           | Rever impacto de novas user stories no Threat Model (delta)                   | Developer, Arquitetos de Software (quando aplicável), AppSec Engineer                    | Atualização versionada + ligação a backlog (`THREAT-*`)          |
| Revisão de Arquitetura / ADR     | Validar ameaças antes de decisões arquiteturais irreversíveis                 | Arquitetos de Software, AppSec Engineer, Scrum Master / Team Lead                                      | ADR + Threat Model revisto + decisões por ameaça                 |
| Alterações críticas / refactors  | Revalidar o modelo quando há mudança estrutural (fluxos, trust boundaries, deps) | Developer, QA, Arquitetos de Software, AppSec Engineer                              | Modelo atualizado + diffs + justificações                         |
| Release / Go-live                | Confirmar ameaças abertas, exceções, risco residual e compensações            | QA, AppSec Engineer, Product Owner (impacto), Scrum Master / Team Lead                | Decisões (mitigar/aceitar) + evidência de aprovação              |
| CI/CD (gate de controlo)         | Verificar “frescura” do Threat Model face a mudanças relevantes (determinístico) | DevOps / SRE, AppSec Engineer                                                 | Resultado de verificação + link para versão do modelo             |

---

## 👥 Quem faz o quê

| Papel / Função             | Responsabilidades-chave |
|----------------------------|--------------------------|
| Arquitetos de Software     | Facilitar sessões, manter modelos atualizados e garantir consistência arquitetural |
| Scrum Master / Team Lead   | **Responsável pela decisão final do modelo** no contexto da equipa/projeto (aprovação do baseline e revisões) |
| Developer                  | Identificar fluxos, pontos de entrada, regras de negócio e mudanças técnicas relevantes |
| QA                         | Traduzir ameaças em critérios de aceitação e validar evidência de mitigação/testes |
| AppSec Engineer            | Identificar ameaças técnicas, rever mitigação, validar risco residual e apoiar decisões de exceção |
| Product Owner              | Priorizar mitigação pelo impacto no negócio e aceitar trade-offs explícitos |
| DevOps / SRE               | Implementar gates determinísticos, assegurar rastreabilidade e retenção de evidência |

---

## 📝 User Stories e Cartões Reutilizáveis
### US-01 - Criação do modelo de ameaça

**Contexto.**  
No início do projeto, deve ser criado um modelo de ameaça proporcional ao risco da aplicação.

:::userstory
**História.**   
Como **Arquitetos de Software** e **Scrum Master / Team Lead**, quero criar um modelo de ameaça inicial com DFDs e STRIDE/LINDDUN, para que os riscos de arquitetura sejam visíveis e tratados desde o início.

**Critérios de aceitação (BDD).**
- **Dado** que o projeto inicia  
  **Quando** construo o modelo de ameaça com DFDs  
  **Então** as ameaças identificadas ficam registadas com decisões explícitas e evidência mínima,
  **e** as assunções/limites do modelo ficam documentados.

**Checklist.**
- [ ] Sessão de threat modeling realizada  
- [ ] DFDs criados e documentados  
- [ ] Ameaças catalogadas (STRIDE, LINDDUN, PASTA)  
- [ ] Ameaças ligadas a requisitos de mitigação  
- [ ] Evidência arquivada em repositório de arquitetura
- [ ] Âmbito, assunções e limites do modelo documentados
- [ ] Responsável pela aprovação do baseline identificado

:::

**Artefactos & evidências.**
- Artefacto: modelo de ameaça inicial (ferramenta ou Markdown)  
- Evidência: ligação a backlog `THREAT-*`

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Checklist simplificada |
| L2 | Sim | Modelos formais com STRIDE |
| L3 | Sim | Modelos completos com STRIDE/LINDDUN/PASTA |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Início | Kick-off do projeto | Arquitetos de Software + AppSec Engineer | Antes do backlog inicial |

**Ligações úteis.**
- 🔗 [OWASP Threat Modeling](https://owasp.org/www-community/Threat_Modeling)  

---

### US-02 - Validação de arquitetura com threat modeling

**Contexto.**  
As revisões de arquitetura devem incluir threat modeling para identificar ameaças estruturais.

:::userstory
**História.**   
Como **Arquitetos de Software** e **AppSec Engineer**, quero validar a arquitetura através de threat modeling, para identificar ameaças críticas antes de decisões de design.

**Critérios de aceitação (BDD).**
- **Dado** que ocorre revisão da arquitetura  
  **Quando** aplico threat modeling  
  **Então** ameaças estruturais são registadas e mitigadas

**Checklist.**
- [ ] Revisão de arquitetura formal realizada  
- [ ] Modelo de ameaça atualizado  
- [ ] Decisões de design documentadas  
- [ ] Evidência arquivada

:::

**Artefactos & evidências.**
- Artefacto: relatórios de revisão de arquitetura  
- Evidência: ameaças registadas ligadas a requisitos

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Revisão simplificada |
| L2 | Sim | Revisão da arquitetura com threat modeling |
| L3 | Sim | Revisão detalhada + validação independente |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Design / Revisão | Revisão da arquitetura | Arquitetos de Software + AppSec Engineer | Antes da aprovação de design |

---

### US-03 - Atualização do modelo após alteração técnica

**Contexto.**  
Sempre que ocorrer uma alteração significativa (nova feature, integração ou refactor), o modelo de ameaça deve ser atualizado.

:::userstory
**História.**   
Como **Arquitetos de Software** e **DevOps/SRE**, quero atualizar o modelo de ameaça sempre que há alterações significativas, para que o modelo permaneça válido e útil.

**Critérios de aceitação (BDD).**
- **Dado** que ocorre alteração significativa  
  **Quando** atualizo o modelo  
  **Então** ameaças novas ou alteradas ficam registadas e mapeadas para requisitos

**Checklist.**
- [ ] Alteração significativa identificada  
- [ ] Modelo de ameaça atualizado  
- [ ] Ameaças novas registadas  
- [ ] Evidência arquivada

:::

**Artefactos & evidências.**
- Artefacto: modelo de ameaça atualizado  
- Evidência: commit ou issue ligada a alteração

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Apenas integrações externas |
| L2 | Sim | Todas as mudanças críticas |
| L3 | Sim | Qualquer alteração da arquitetura |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Refactor / Alteração | Alteração significativa | Arquitetos de Software + Scrum Master / Team Lead | Antes da release |

**Ligações úteis.**
- 🔗 [SSDF Practices](https://csrc.nist.gov/publications/detail/sp/800-218/final)  

---
### US-04 - Justificação formal de risco aceite

**Contexto.**  
Nem todas as ameaças podem ser mitigadas; riscos residuais devem ser formalmente documentados, aprovados e revistos.

:::userstory
**História.**   
Como **AppSec Engineer** e **GRC/Compliance**, quero documentar e aprovar formalmente riscos residuais identificados no threat modeling, para que decisões de aceitação sejam transparentes e auditáveis.

**Critérios de aceitação (BDD).**
- **Dado** que há ameaças não mitigadas  
  **Quando** registo risco aceite  
  **Então** decisão é documentada, aprovada e arquivada

**Checklist.**
- [ ] Risco residual identificado  
- [ ] Justificação documentada  
- [ ] Aprovação formal por AppSec  
- [ ] Prazo e reavaliação definidos  
- [ ] Evidência anexada ao repositório de riscos

:::

**Artefactos & evidências.**
- Artefacto: ficheiros `riscos/*.md`  
- Evidência: issue ou PR com aprovação

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Aceitação informal |
| L2 | Sim | Documentação formal |
| L3 | Sim | Documentação formal + mitigação compensatória |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Planeamento/Release | Identificação de risco não mitigado | AppSec Engineer | Antes do go-live |

**Ligações úteis.**
- 🔗 [Gestão de exceções](/sbd-toe/sbd-manual/requisitos-seguranca/addon/gestao-excecoes) e [risco residual](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/risco-residual)  

---

### US-05 - Gate de controlo de consistência no CI/CD

**Contexto.**  
O pipeline deve garantir que mudanças relevantes não passam sem atualização/revisão do Threat Model, mantendo rastreabilidade e evidência.

:::userstory
**História.**  
Como **DevOps/SRE** e **AppSec Engineer**, quero aplicar um **gate determinístico** que verifique se o Threat Model está atualizado face a alterações relevantes, para impedir releases com modelo obsoleto.

**Critérios de aceitação (BDD).**
- **Dado** que uma alteração relevante é introduzida (ex.: novo fluxo, nova dependência, nova trust boundary)  
  **Quando** a pipeline é executada  
  **Então** o gate exige referência a uma versão atualizada do Threat Model ou uma justificação aprovada  
- **E** a evidência do gate fica registada e auditável

**Checklist.**
- [ ] Critérios objetivos de “alteração relevante” definidos e versionados
- [ ] Gate implementado com verificação determinística (regras, metadados, diffs)
- [ ] Saída do gate registada (logs + referência ao artefacto versionado)
- [ ] Exceções seguem workflow de aprovação (quando aplicável)

:::

**Artefactos & evidências.**
- Artefacto: regra/versionamento de critérios + referência ao Threat Model aprovado
- Evidência: logs de pipeline + link para commit/tag do modelo

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Não | Apenas revisão manual em releases maiores |
| L2 | Sim | Gate não-bloqueante com alerta e obrigação de revisão |
| L3 | Sim | Gate bloqueante com exceções formais e prazo |

---

### US-06 - Validação de impacto no negócio

**Contexto.**  
As ameaças identificadas devem ser priorizadas com base no impacto para o negócio, e não apenas em métricas técnicas.

:::userstory
**História.**   
Como **Product Owner**, quero priorizar as ameaças identificadas no modelo de acordo com impacto no negócio, para otimizar mitigação e investimento.

**Critérios de aceitação (BDD).**
- **Dado** que ameaças foram identificadas  
  **Quando** as avalio pelo impacto de negócio  
  **Então** prioridades são registadas e comunicadas

**Checklist.**
- [ ] Impacto avaliado (financeiro, reputacional, legal)  
- [ ] Priorização documentada  
- [ ] Requisitos derivados priorizados no backlog  
- [ ] Evidência arquivada

:::

**Artefactos & evidências.**
- Artefacto: matriz de impacto vs ameaça  
- Evidência: backlog priorizado

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Avaliação simplificada |
| L2 | Sim | Análise de impacto formal |
| L3 | Sim | Análise formal + revisão executiva |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Planeamento / Grooming | Avaliação de impacto | Product Owner + Gestão Executiva/CISO | Antes de priorização de sprint |

---
### US-07 - Reutilização controlada e revisão de modelos anteriores

**Contexto.**  
A reutilização de modelos anteriores é útil, mas introduz risco quando o contexto mudou. Deve existir revisão explícita antes de considerar um modelo como válido.

:::userstory
**História.**  
Como **Arquitetos de Software** e **AppSec Engineer**, quero reutilizar modelos anteriores apenas com revisão explícita de mudanças de contexto, para reduzir omissões e evitar decisões herdadas incorretas.

**Critérios de aceitação (BDD).**
- **Dado** que existe um modelo anterior semelhante  
  **Quando** o reutilizo como base  
  **Então** documento diferenças de contexto/arquitetura e valido novamente decisões críticas  
- **E** registo um responsável pela aprovação da revisão

**Checklist.**
- [ ] Modelo anterior identificado (referência versionada)
- [ ] Diferenças de arquitetura/fluxos/dependências analisadas
- [ ] Decisões críticas revalidadas (mitigar/aceitar/transferir)
- [ ] Aprovação registada e auditável

:::

**Artefactos & evidências.**
- Artefacto: delta de revisão + referência ao modelo aprovado
- Evidência: PR/issue de revisão com aprovação

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Revisão simplificada |
| L2 | Sim | Revisão formal com diffs |
| L3 | Sim | Revisão formal + revisão independente |


---

### US-08 - Aplicação LINDDUN quando existir tratamento de dados pessoais  *(novo)*

**Contexto.**  
Quando o sistema trata dados pessoais, a análise de privacidade deve complementar a análise de segurança.

:::userstory
**História.**  
Como **Arquitetos de Software + AppSec Engineer**, quero aplicar **LINDDUN** quando exista tratamento de dados pessoais, para garantir cobertura de ameaças de privacidade.

**Critérios de aceitação (BDD).**
- **Dado** que o sistema trata dados pessoais  
  **Quando** executo Threat Modeling  
  **Então** **incluo análise LINDDUN** com ameaças, mitigação e **mapeamento para `REQ-PRIV-*`**  
- E **crio `privacy-dfd`** com trust boundaries específicos  

**Checklist.**
- [ ] `privacy-dfd` criado  
- [ ] Lista LINDDUN preenchida  
- [ ] **Ligação a `REQ-PRIV-*` do Cap. 2**  
- [ ] **Ameaças classificadas quanto a severidade e mitigação**  
- [ ] Evidência arquivada no repositório de arquitetura  
:::

**Artefactos & evidências.**
- `privacy-dfd.*`  
- `privacy-threats.md`  
- Relatório LINDDUN exportado / validado  

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|:---|:---|:---|
| L1 | Opcional | Checklist simplificada |
| L2 | Sim | Análise formal de privacidade |
| L3 | Sim | LINDDUN completo + validação independente (GRC / Compliance (DPO)) |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|:---|:---|:---|:---|
| Design / Revisão | Presença de dados pessoais | Arquitetos de Software + GRC / Compliance | Antes da aprovação de design |

**Ligações úteis.**
- 🔗 [LINDDUN Framework](https://www.linddun.org/)  
- 🔗 [ENISA - Privacy by Design Guidelines](https://www.enisa.europa.eu/)  

---
### US-09 - Aprovação formal do Threat Model (baseline e revisões)

**Contexto.**  
O Threat Modeling só é controlo de segurança quando existe um modelo aprovado, com responsável e evidência mínima.

:::userstory
**História.**  
Como **Scrum Master / Team Lead** e **AppSec Engineer**, quero aprovar formalmente o Threat Model (baseline e revisões), para garantir decisão explícita, rastreabilidade e auditabilidade.

**Critérios de aceitação (BDD).**
- **Dado** que o Threat Model foi atualizado  
  **Quando** concluo a revisão  
  **Então** existe uma decisão formal de aprovação com responsável identificado  
- **E** a evidência mínima obrigatória está presente e versionada

**Checklist.**
- [ ] Âmbito, assunções e limites documentados
- [ ] Ameaças identificadas com decisão por item (mitigar/aceitar/transferir/rejeitar)
- [ ] Ligações a requisitos/mitigações criadas (ex.: `REQ-*`, `THREAT-*`)
- [ ] Evidência mínima anexada (diagramas/versionamento/decisão)
- [ ] Aprovação registada (PR/issue/assinatura conforme processo)

:::

**Artefactos & evidências.**
- Artefacto: Threat Model aprovado (versão/tag) + `decisions.md`
- Evidência: registo de aprovação + links para backlog e requisitos

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Aprovação leve (registo simples) |
| L2 | Sim | Aprovação formal por Scrum Master / Team Lead + AppSec Engineer |
| L3 | Sim | Aprovação formal + revisão independente (segregação) |

---

### US-10 - Controlo de acesso, classificação e retenção dos artefactos de Threat Modeling

**Contexto.**  
Diagramas e decisões de threat modeling são ativos sensíveis e devem ter proteção proporcional ao risco.

:::userstory
**História.**  
Como **Arquitetos de Software** e **DevOps/SRE**, quero controlar acesso e retenção dos artefactos de Threat Modeling, para reduzir risco de exposição de arquitetura e decisões críticas.

**Critérios de aceitação (BDD).**
- **Dado** que artefactos de Threat Modeling são produzidos  
  **Quando** são armazenados e partilhados  
  **Então** seguem regras de acesso mínimo, classificação e retenção definidas  
- **E** existe evidência de onde estão guardados e quem tem acesso

**Checklist.**
- [ ] Local de armazenamento definido e versionado
- [ ] Controlo de acesso aplicado (least privilege)
- [ ] Classificação definida (sensibilidade/partilha interna)
- [ ] Retenção e eliminação definidas (quando aplicável)
- [ ] Evidência de acessos e alterações disponível/auditável

:::

**Artefactos & evidências.**
- Artefacto: política/regras do repositório + estrutura de diretórios
- Evidência: ACLs/grupos + registos de auditoria (quando aplicável)

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Sim | Controlo básico e armazenamento interno |
| L2 | Sim | Controlo formal + rastreio de alterações |
| L3 | Sim | Controlo reforçado + segregação e auditoria |

---

### US-11 - Threat modeling para sistema com agente AI (tool-use) {#us-11}

**Contexto.**
Quando o sistema integra **agentes autónomos** com *tool-use* — modelos que invocam *tools* reais para criar PRs, ler segredos, executar *deploys* ou contactar APIs — a superfície de ataque deixa de ser só o modelo e passa a incluir o conjunto fechado de *tools* invocáveis, a identidade com que o agente opera e a fronteira `agentic → tool` em que o efeito real se materializa. Aplica-se o playbook agentic do Cap. 03 antes da operação e em cada subida de nível de autonomia, para que as ameaças MITRE ATLAS aplicáveis estejam identificadas e ancoradas em controlos citáveis.

:::userstory
**História.**
Como **Software Architect** e **AppSec Engineer**, quero executar o [playbook agentic](./addon/metodologias-e-ferramentas#playbook-agentic) sempre que um agente A1+ é introduzido no sistema ou sobe de nível de autonomia, para que as ameaças aplicáveis sejam catalogadas com IDs reais (MITRE ATLAS `AML.T*` e OWASP LLM Top 10 2025) e cada uma fique ligada a controlos concretos em Caps. 04, 07, 10 ou 12 antes do *go-live*.

**Critérios de aceitação (BDD).**
- **Dado** que um agente AI vai operar em A1+ no projecto
  **Quando** o seu *mandate* ([`REQ-AGN-001`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn)) é proposto
  **Então** existe DFD agentic com cinco participantes (humano → cliente → modelo → *tool runtime* → sistema externo) e quatro fronteiras (input · inference · agentic · tool) explícitas
- **Dado** o DFD agentic
  **Quando** se executa o exercício do playbook
  **Então** as *tools* destrutivas/*side-effectful* estão marcadas, as ameaças aplicáveis vêm citadas por ID canónico (`AML.T0051.001`, `AML.T0086`, `AML.T0110`, `LLM06-2025`, etc.) e cada uma tem mitigação ancorada em capítulo do manual
- **Dado** uma subida de nível de autonomia (A1→A2, A2→A3, …) ou alteração da `tools_allowlist`
  **Quando** se pretende activar
  **Então** o exercício é repetido e o registo do *mandate* referencia o novo *threat model*

**Critérios de aceitação (DoD).**
- [ ] DFD agentic versionado em repositório, com fronteiras de confiança marcadas
- [ ] Lista de *tools* invocáveis pelo agente, etiquetadas `read` / `write` / `destructive` / `external`
- [ ] *Threats* aplicáveis identificadas com **IDs canónicos** (MITRE ATLAS `AML.T*` ou OWASP LLM Top 10 2025); ameaças eliminadas vêm com justificação curta
- [ ] Cada *threat* não eliminada tem entrada de controlo a aterrar em Cap. 04 ([`ARC-014`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-014)/[`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015)), Cap. 07, Cap. 10 ou Cap. 12
- [ ] *Mitigation confidence* (`derived` vs `heuristic`) rotulada em cada ligação *threat*↔controlo
- [ ] Cruzamento com o registo organizacional: se uma mitigação não está implementada, o agente não opera no nível pedido

:::

**Artefactos & evidências.**
- DFD agentic versionado (Mermaid, drawio ou equivalente)
- *Threat model document* com tabela `threat_id` × `boundary` × `mitigations` × `confidence`
- Referência cruzada `mandate_ref` ↔ `threat_model_ref` no registo do *mandate*
- Histórico de revisões do *threat model* ligado às subidas de nível

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Recomendado para A1; obrigatório para A2+ | DFD simplificado + *threat library* curta (Top 3–5 *threats*) |
| L2 | Obrigatório para A1+ | DFD completo + *threat library* completa do playbook + *mitigations* ancoradas |
| L3 | Obrigatório para A1+ | DFD completo + *threat library* + revisão `appsec` independente + cruzamento com cross-check AI Act quando aplicável |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Design | Introdução do agente no sistema | `software_architect` + `appsec` | Antes da activação do *mandate* |
| Subida de nível | Promoção A1→A2 ou superior | `appsec` | Antes da nova activação |
| Alteração de *tools* | Adição/remoção em `tools_allowlist` | `appsec` | Antes de a *tool* entrar em uso |
| Mudança de modelo | Versão maior do *provider* | `appsec` | Antes do *cutover* |

**Ligações úteis.**
- 🔗 [Playbook agentic completo (Cap. 03)](./addon/metodologias-e-ferramentas#playbook-agentic)
- 🔗 [Catálogo `REQ-AGN-*` (Cap. 02)](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn)
- 🔗 [`ARC-015` — agente como *principal* (Cap. 04)](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015)
- 🔗 [Policy 38 — Mandates de Agentes AI](/sbd-toe/assets/policies/policy-mandates-agentes)

---

### US-12 - Threat modeling estendido para componentes AI/ML não-agentic

Sistemas com modelos preditivos, LLMs conversacionais ou RAG têm ameaças adversariais que o STRIDE clássico não cobre, mesmo sem agente tool-use.  

**Contexto.** O [`THR-008`](./addon/catalogo-requisitos-threat-modeling) exige threat model estendido para todos os componentes AI/ML, mas a US-11 só cobre o caso agentic (tool-use). Um modelo preditivo, um classificador, um LLM em interface conversacional ou um pipeline RAG têm superfícies adversariais próprias — model poisoning, training data poisoning, evasion, model theft, prompt injection directa/indirecta — que ficam por modelar quando não há agente. Esta lacuna deixa sistemas AI sem tool-use sem cobertura formal.  

:::userstory
**História.**   
Como **Software Architect** e **AppSec Engineer**, quero estender o threat model com ameaças adversariais AI/ML sempre que o sistema integra componentes de inteligência artificial sem tool-use (modelos preditivos, LLMs conversacionais, RAG), para que as ameaças específicas fiquem catalogadas por ID canónico e ancoradas em controlos antes do go-live.  

**Critérios de aceitação (BDD).**  
- **Dado** um sistema que integra um componente AI/ML sem agente tool-use  
  **Quando** se executa o threat modeling  
  **Então** o STRIDE/LINDDUN baseline é complementado (não substituído) com framing AI/ML, e são identificadas as trust boundaries adicionais (training data → modelo, prompt input → modelo, modelo → output)  
- **Dado** o framing AI/ML aplicado  
  **Quando** se cataloga cada ameaça  
  **Então** vem citada por ID canónico (MITRE ATLAS `AML.T*`, NIST AI 100-2 e2025, ou OWASP LLM/ML Top 10) e tem mitigação ancorada em capítulo do manual  

**Checklist.**  
- [ ] Trust boundaries AI/ML adicionais marcadas no DFD (training-time, inference-time, output)  
- [ ] Ameaças adversariais catalogadas por ID canónico (ATLAS `AML.T*` / NIST AI 100-2 / OWASP LLM/ML Top 10)  
- [ ] STRIDE/LINDDUN baseline complementado, não substituído  
- [ ] Cada ameaça não eliminada ligada a controlo em capítulo do manual  

:::

**Artefactos & evidências.** DFD com trust boundaries AI/ML; tabela `threat_id` × `boundary` × `mitigations` referenciada a ATLAS/NIST/OWASP; ligação a `REQ-*` derivados.  

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Recomendado: triagem por OWASP LLM/ML Top 10 | Obrigatório: framing AI/ML completo + boundaries + mitigações ancoradas | Obrigatório: framing completo + adversary capabilities (NIST AI 100-2) + revisão `appsec` independente |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Design | Introdução de componente AI/ML sem tool-use | `software_architect` + `appsec` | Antes do go-live |
| Alteração | Troca de modelo base, dataset ou pipeline RAG | `appsec` | Antes do cutover |

**Ligações úteis.** [Metodologias — §AI/ML](./addon/metodologias-e-ferramentas#ai-ml) · [`THR-008`](./addon/catalogo-requisitos-threat-modeling)

---

### US-13 - Derivação de abuse/misuse cases para o backlog

A análise centrada no utilizador legítimo deixa escapar caminhos de abuso que só uma perspetiva adversarial revela.  

**Contexto.** O [método de abuse/misuse cases](./addon/abuse-misuse-cases) prescreve um workshop cross-functional que torna adversarial a elicitação de requisitos, mas nenhuma user story o operacionaliza. Sem isso, os abuse cases ficam como exercício pontual cujas conclusões se perdem entre sprints. O método só altera o produto quando cada abuso priorizado se materializa em item rastreável no backlog, com owner e critério de aceitação adversarial, alimentando threat model e testes.  

:::userstory
**História.**   
Como **AppSec Engineer** e **Product Owner**, quero derivar abuse/misuse cases num workshop cross-functional e integrá-los no backlog como requisitos rastreáveis, para que os caminhos de abuso identificados se traduzam em controlos verificáveis e não se percam.  

**Critérios de aceitação (BDD).**  
- **Dado** um fluxo funcional relevante de um sistema L2+  
  **Quando** se conduz o workshop de abuse cases (produto + dev + segurança + QA)  
  **Então** cada fluxo gera o seu contraponto adversarial ("como atacante, quero ⟨objetivo⟩ explorando ⟨fraqueza⟩"), priorizado por risco (Cap. 01)  
- **Dado** os abuse cases priorizados  
  **Quando** se fecha o exercício  
  **Então** cada um entra no backlog como requisito com owner, critério de aceitação adversarial e estado, e alimenta threat model e casos de teste (Cap. 10)  

**Checklist.**  
- [ ] Workshop cross-functional realizado (produto, dev, segurança, QA)  
- [ ] Abuse cases derivados por fluxo e priorizados por risco  
- [ ] Cada abuse case priorizado no backlog com owner e critério de aceitação adversarial  
- [ ] Abuse cases ligados a threat model e a casos de teste  

:::

**Artefactos & evidências.** Registo do workshop; lista de abuse/misuse cases priorizados; itens de backlog com critério de aceitação adversarial; ligação a `THREAT-*` e a testes.  

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Não aplicável | Obrigatório: workshop em fluxos críticos + integração no backlog | Obrigatório: workshop sistemático + cobertura por fluxo + rastreabilidade a testes |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Requisitos / Threat Modeling | Início de épico ou fluxo funcional relevante | `appsec` + `product_owner` | Antes da derivação de requisitos |

**Ligações úteis.** [Método de Abuse e Misuse Cases](./addon/abuse-misuse-cases) · [Estratégia de testes (Cap. 10)](/sbd-toe/sbd-manual/testes-seguranca/addon/estrategia-testes)

---

### US-14 - Revisão independente em L2 e PASTA em alto risco

A revisão independente cobre os pontos cegos da equipa; em alto risco, o método deve escalar para análise baseada em risco.  

**Contexto.** O [`THR-007`](./addon/catalogo-requisitos-threat-modeling) exige revisão independente por AppSec antes de go-live já em **L2** (não só L3), mas a US-09 só explicita a revisão independente em L3 — deixando L2 sem operacionalização. Paralelamente, o [`THR-003`](./addon/catalogo-requisitos-threat-modeling) prescreve **PASTA ou equivalente** em contextos de alto risco (sistemas regulados, exigência formal de rastreio ameaça → risco → controlo), prescrição que nenhuma US operacionaliza. Esta US fecha ambas as lacunas: revisão independente desde L2 e escalonamento metodológico para PASTA em L3.  

:::userstory
**História.**   
Como **AppSec Engineer** e **Scrum Master / Team Lead**, quero que o threat model seja revisto por elemento independente da equipa de entrega antes do go-live a partir de L2, e que sistemas de alto risco apliquem PASTA como metodologia, para garantir cobertura de pontos cegos e rastreio formal ameaça → risco → controlo.  

**Critérios de aceitação (BDD).**  
- **Dado** um sistema L2+ a entrar em go-live ou com alteração arquitetural material  
  **Quando** o threat model é finalizado  
  **Então** é revisto por AppSec ou elemento com competência equivalente, independente da equipa de entrega, com evidência (registo, aprovação ou lista de desvios com plano)  
- **Dado** a ausência dessa revisão  
  **Quando** se tenta avançar para go-live  
  **Então** o go-live é bloqueado  
- **Dado** um sistema de alto risco (regulado ou L3)  
  **Quando** se seleciona a metodologia  
  **Então** aplica-se PASTA ou equivalente, com rastreio ameaça → risco → controlo declarado no artefacto  

**Checklist.**  
- [ ] Revisor independente da equipa de entrega identificado (L2+)  
- [ ] Evidência da revisão produzida (registo/aprovação/lista de desvios)  
- [ ] Go-live bloqueado na ausência de revisão  
- [ ] PASTA (ou equivalente) aplicado e declarado em sistemas de alto risco  

:::

**Artefactos & evidências.** Registo de revisão independente com responsável nomeado; lista de desvios com plano (quando aplicável); artefacto PASTA com mapeamento ameaça → risco → controlo (alto risco).  

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Não aplicável | Revisão independente obrigatória antes de go-live; PASTA opcional | Revisão independente obrigatória + PASTA (ou equivalente) com rastreio formal |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Pré go-live | Go-live de aplicação L2+ ou alteração arquitetural material | `appsec` (independente) | Antes do go-live (bloqueante) |
| Design | Sistema regulado / alto risco | `software_architect` + `appsec` | Na seleção de metodologia |

**Ligações úteis.** [`THR-007`](./addon/catalogo-requisitos-threat-modeling) · [`THR-003`](./addon/catalogo-requisitos-threat-modeling) · [Metodologias — comparação PASTA](./addon/metodologias-e-ferramentas)

---

### US-15 - Tratamento explícito dos riscos de processo do threat modeling

Um threat model plausível mas incompleto dá falsa confiança — pior do que a ausência do artefacto.  

**Contexto.** Os [riscos de processo do threat modeling](./addon/riscos-processo-threat-modeling) — omissão estrutural, enviesamento de perspetiva, confusão entre análise intermédia e decisão formal, dependência acrítica de modelos prévios, resultados plausíveis mas incorretos — são falíveis por natureza e independentes do método. O manual assume-os explicitamente, mas nenhuma user story obriga ao seu reconhecimento e mitigação no artefacto. Sem isso, a equipa trata o threat model como verdade validada em vez de hipótese sujeita a erro.  

:::userstory
**História.**   
Como **AppSec Engineer** e **Arquitetos de Software**, quero reconhecer e tratar explicitamente os riscos de processo do threat modeling em cada modelo produzido, para que omissões, enviesamentos e plausibilidade enganosa sejam assumidos como risco inerente e não confundidos com cobertura real.  

**Critérios de aceitação (BDD).**  
- **Dado** que um threat model é produzido  
  **Quando** se finaliza o artefacto  
  **Então** distingue-se claramente material de apoio (notas, listas exploratórias, hipóteses) de decisão validada e aprovada  
- **Dado** a reutilização de um modelo prévio  
  **Quando** se adota como base  
  **Então** é tratado como hipótese de partida, com revalidação explícita das mudanças de contexto (cruzar com US-07)  
- **Dado** o artefacto finalizado  
  **Então** regista-se que a ausência de uma ameaça não é prova da sua inexistência, e os riscos de omissão/enviesamento ficam assumidos  

**Checklist.**  
- [ ] Material de apoio distinguido de decisão formal aprovada  
- [ ] Modelos reutilizados tratados como hipótese, com revalidação de contexto  
- [ ] Risco de omissão/enviesamento assumido explicitamente no artefacto  
- [ ] Plausibilidade não tratada como substituto de validação e evidência  

:::

**Artefactos & evidências.** Secção de assunções/limites no threat model; separação versionada entre notas exploratórias e decisão aprovada; nota de risco de omissão no artefacto.  

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Nota informal de assunções | Assunções e limites documentados; separação apoio/decisão | Tratamento formal dos riscos de processo + revisão independente da cobertura |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Threat Modeling | Finalização ou reutilização de threat model | `appsec` + `software_architect` | Antes da aprovação do baseline |

**Ligações úteis.** [Riscos de Processo no Threat Modeling](./addon/riscos-processo-threat-modeling) · [Validação e Evidência](./addon/validacao-evidencia-threat-modeling)

---
## ⚖️ Aplicação proporcional por nível de risco (L1–L2–L3)

| Prática / Atividade              | L1 (baixo risco)                         | L2 (médio risco)                                | L3 (alto risco)                                                  |
|----------------------------------|------------------------------------------|-------------------------------------------------|------------------------------------------------------------------|
| Sessões de Threat Modeling       | Básicas (checklist STRIDE simplificada)  | Modelos formais com STRIDE                     | Modelos completos com STRIDE **e LINDDUN** (quando aplicável) + PASTA + automação |
| Revisão de arquitetura           | Opcional                                 | Inclusão obrigatória                           | Sempre obrigatória com revisão independente                      |
| Integração em CI/CD              | Não aplicável                            | Revisão periódica                              | Automação integrada e bloqueante                                 |
| Risco aceite                     | Informal                                 | Documentado                                    | Formal, aprovado por AppSec Engineer e com sunset definido       |
| Automação / Reutilização         | Não aplicável                            | Recomendado (ferramenta ou script)             | Obrigatório (ferramenta centralizada, integração contínua)       |
| **Análise LINDDUN (privacidade)**| Não aplicável                            | Obrigatória se houver dados pessoais           | Sempre obrigatória, com revisão por GRC / Compliance (DPO)       |

---

## 📄 Templates e artefactos esperados

| Artefacto                          | Formato sugerido     | Onde guardar / referenciar                |
|-----------------------------------|----------------------|-------------------------------------------|
| Modelo de ameaça inicial (STRIDE) | Ferramenta / `.md`   | Diretório `docs/` ou repositório          |
| **Modelo de privacidade (LINDDUN)** | Ferramenta / `.md`  | Diretório `docs/privacy/` ou subpasta do modelo |
| Atualizações de modelos            | Ferramenta / `.md`   | Diretório `docs/` ou repositório          |
| Cartões derivados (`THREAT-*`)     | Board / Jira         | Backlog da equipa                         |
| **Cartões de privacidade (`PRIV-*`)** | Board / Jira        | Backlog da equipa                         |
| Justificação de risco aceite       | Markdown / issue     | Diretório `riscos/` ou board              |
| Relatórios de rastreabilidade      | Export / `.csv`      | Arquivo de auditoria                      |
| **Relatórios LINDDUN**             | Export / `.pdf`/`.csv`| Diretório `docs/privacy/` ou auditoria    |
| Modelos automatizados              | Ferramenta           | Repositório central de modelos            |
