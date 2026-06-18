---
id: intro
title: AI Act - Cross-Check Normativo
description: Análise de como o SbD-ToE cobre os requisitos técnicos do Regulamento (UE) 2024/1689 (AI Act) - exatidão, robustez, cibersegurança, logging, gestão de risco e monitorização pós-comercialização de sistemas de IA
tags: [cross-check, ai-act, regulamento-ia, ia, machine-learning, robustez, ciberseguranca, gpai]
sidebar_position: 6
---

# AI Act: Cross-Check Normativo

> Para implementação prática, consulte o [Playbook SbD-ToE 4 AI Act](/sbd-toe/cross-check-normativo/ai-act/playbook).
>
> Para padrões aplicacionais universais, ver capítulos base do SbD-ToE (01–14).

## Âmbito

### 🤖 AI Act - Regulamento de Inteligência Artificial

O **AI Act** é o **Regulamento (UE) 2024/1689** (CELEX: [32024R1689](https://eur-lex.europa.eu/legal-content/PT/TXT/?uri=CELEX:32024R1689)), o primeiro quadro jurídico horizontal do mundo dedicado à inteligência artificial. Entrou em vigor a 1 de agosto de 2024 e aplica-se de forma faseada:

- **2 de fevereiro de 2025** - práticas proibidas (Art. 5) e literacia em IA (Art. 4).
- **2 de agosto de 2025** - modelos de IA de finalidade geral (GPAI, Capítulo V), governação e regime sancionatório.
- **2 de agosto de 2026** - generalidade das obrigações para sistemas de IA de **alto risco** do Anexo III.
- **2 de agosto de 2027** - sistemas de alto risco abrangidos pela legislação de produto do Anexo I.

> ℹ️ **Nota (2026):** o acordo político **Digital Omnibus** (2026) prevê **diferir** as obrigações de alto risco — Anexo III para **2 de dezembro de 2027** e Anexo I para **2 de agosto de 2028**. As datas acima são as **promulgadas**; o diferimento só produz efeitos com a publicação no Jornal Oficial.

O AI Act adota uma **abordagem baseada no risco**, com quatro patamares: risco **inaceitável** (proibido, Art. 5), **alto risco** (Art. 6 e Anexos I/III, sujeito ao grosso das obrigações técnicas), risco **limitado** (deveres de transparência, Art. 50) e risco **mínimo** (sem obrigações específicas). Sobre estes patamares incidem ainda regras próprias para **GPAI** (Art. 53) e GPAI com **risco sistémico** (Art. 55).

É essencial enquadrar a natureza do regulamento: o AI Act é, antes de tudo, **legislação de segurança de produto e de proteção de direitos fundamentais** aplicada a sistemas de IA, não uma norma de segurança aplicacional (AppSec). Contudo, as obrigações para sistemas de alto risco incorporam **requisitos técnicos substanciais** que cruzam diretamente com o SbD-ToE - em particular:

- **Art. 9** - sistema de gestão de risco ao longo do ciclo de vida;
- **Art. 12 / Art. 19** - registo automático de eventos (logging) e conservação de logs;
- **Art. 15** - exatidão, robustez e **cibersegurança** (incluindo resiliência a ataques adversariais);
- **Art. 17** - sistema de gestão da qualidade (QMS);
- **Art. 72** - monitorização pós-comercialização;
- **Art. 73** - comunicação de incidentes graves.

No SbD-ToE, o AI Act é operacionalizado através das mesmas disciplinas técnicas que sustentam qualquer software seguro - engenharia segura (requisitos, arquitetura, desenvolvimento, IaC, pipelines, testes), cadeia de fornecimento e proveniência (dependências, containers, SBOM), processos de monitorização e resposta, e governação/contratação - aplicadas agora ao **ciclo de vida de sistemas de IA** (datasets, modelos, pipelines de treino e inferência, serviços de inferência).

> ⚖️ **Nota editorial.**
> Esta secção é uma **síntese operacional** dos artigos relevantes do AI Act, não uma citação literal do regulamento.
> Baseia-se, em particular, nos Artigos 9.º (gestão de risco), 10.º (dados e governação de dados), 11.º e Anexo IV (documentação técnica), 12.º e 19.º (registos/logs), 13.º–14.º (transparência e supervisão humana), 15.º (exatidão, robustez, cibersegurança), 17.º (QMS), 72.º (monitorização pós-comercialização), 73.º (incidentes graves) e 53.º/55.º (GPAI e risco sistémico).

> ⚖️ **Nota sobre referências técnicas.**
> O AI Act estabelece requisitos essenciais mas remete o detalhe técnico para **normas harmonizadas** (a desenvolver pelo CEN-CENELEC) e especificações comuns.
> Padrões como **ISO/IEC 42001** (sistema de gestão de IA), **ISO/IEC 23894** (gestão de risco de IA), **ISO/IEC 27090** (segurança de IA, em desenvolvimento), o **NIST AI Risk Management Framework (AI RMF 1.0)**, o **MITRE ATLAS** (táticas e técnicas adversariais contra ML), o **OWASP Machine Learning Security Top 10** e o **OWASP Top 10 for LLM Applications** são amplamente reconhecidos e fornecem base sólida para cumprir os requisitos técnicos e processuais.
> O SbD-ToE assume estes padrões como **boas práticas recomendadas**, não como requisitos legais em si mesmos.

## Aviso Regulatório

O SbD-ToE cobre o **"como" técnico** dos requisitos de alto risco, mas **não substitui** as dimensões jurídicas, de domínio de IA e de avaliação de conformidade do AI Act. Em concreto, ficam **fora do âmbito** do manual:

- **Classificação de risco** (Art. 6 e Anexos I/III) - determinação jurídica de se um sistema é de alto risco.
- **Governação de dados de treino, validação e teste** (Art. 10) - representatividade, deteção e mitigação de enviesamento (*bias*), qualidade estatística dos conjuntos de dados. Estas são questões de **domínio de IA/ciência de dados**, não de AppSec.
- **Transparência e informação ao utilizador implementador** (Art. 13) e a pessoas singulares (Art. 50).
- **Supervisão humana** (Art. 14) - a **conceção/UX** dos mecanismos de *human-in-the-loop* / *human-on-the-loop* e o juízo humano (supervisão-como-compreensão). A faceta de **interrupção (*stop/override*) e governação** está coberta tecnicamente (ver matriz, Art. 14).
- **Avaliação de impacto sobre os direitos fundamentais (FRIA)** (Art. 27) - obrigação dos utilizadores implementadores (*deployers*).
- **Avaliação de conformidade** (Art. 43), envolvimento de **organismos notificados**, **declaração UE de conformidade** (Art. 47), **marcação CE** (Art. 48) e **registo na base de dados da UE** (Art. 49/71).
- **Determinação de práticas proibidas** (Art. 5) e qualificação jurídica de papéis (provider, deployer, importador, distribuidor).

Estas dimensões são da competência de equipas de compliance, jurídico, ciência de dados e da relação com a autoridade competente. O SbD-ToE fornece os controlos técnicos e a evidência; não emite o juízo de conformidade.

---

## Matriz de Cross-Check (resumo)

> ✏️ **Refresh 2026-05-30.** Esta matriz foi actualizada na sequência do *release agentic* (Cap. 02 §A0–A4, Cap. 03 playbook agentic, [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015), `DEP-012..014`, `OPS-012..014`, Policy 38, Policy 39, US-13/14/15/16/19/21). Várias lacunas que estavam classificadas como "intencionais" (por desenho fora de AppSec) ficaram **parcial ou totalmente colmatadas** — assinalamos onde.

| Domínio AI Act | Referência (artigo) | Cobertura SbD-ToE | Lacuna residual | Ação de adaptação |
|---|---|---|---|---|
| Literacia em IA | Art. 4 | Cap. 13 (formação), Policy 37 §11 (matriz por *role*) | Avaliação formal de literacia | Documentar conclusões dos trilhos formativos como evidência |
| Sistema de gestão de risco | Art. 9 | Cap. 01 (classificação), Cap. 02 (requisitos), Cap. 02 §A0–A4 + [`REQ-AGN-002`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn) (níveis de autonomia), Cap. 03 (threat modeling + playbook agentic), Cap. 12 (monitorização) | Risco para saúde, segurança e direitos fundamentais ao longo do uso previsto | Estender threat model com taxonomia de risco de IA (ATLAS — já incluída) e impacto societal |
| Dados e governação de dados | Art. 10 | Cap. 05 (proveniência), [`DEP-011`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-011) (inventário AI), [`DEP-012`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-012) (AI BOM CycloneDX 1.6 ml-bom), Policy 39, Cap. 02 (requisitos de dados) | Representatividade, enviesamento, qualidade estatística (domínio IA) | Processo de *data governance* de ciência de dados; *datasheets*/*data cards* |
| Documentação técnica | Art. 11, Anexo IV | Cap. 02, Cap. 04 (arquitetura + [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015)), Cap. 05 ([`DEP-012`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-012) AI BOM), Cap. 06, Policy 38 (mandate) | Estrutura formal do Anexo IV; *model cards* | Mapear artefactos SbD-ToE (incluindo mandate + AI BOM) para o índice do Anexo IV |
| Registo de eventos (logging) | Art. 12, Art. 19 | Cap. 12 (observabilidade), [`OPS-011`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes) (AI/ML), [`OPS-012`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-012) (audit per *tool invocation* com `mandate_ref`), Cap. 12 US-13 (telemetria agentic), Policy 30 §9 | Esquema de campos específico do *model output* fica configurável | Documentar esquema de inferência por sistema |
| Transparência aos deployers | Art. 13 | Cap. 02, Cap. 04 (parcial), Policy 38 (mandate como fonte estruturada de *capabilities*, limitações e supervisão) | Métricas de desempenho específicas do modelo | Derivar "instruções de utilização" a partir do mandate + artefactos Cap. 04/06 |
| Supervisão humana | Art. 14 ⚡ | Cap. 02 §A0–A4 + `REQ-AGN-001..004` (mandate, classificação de nível, *kill-switch*, *intent declaration*), Cap. 04 [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015) (OOB approval + *kill-switch* arquitectónico), Policy 38 (ciclo de vida do mandate) | UX/fluxo de intervenção humano (domínio IA/produto) | Desenho da UX continua na equipa de IA; controlo técnico e governação operacional já dentro |
| Exatidão, robustez e cibersegurança | Art. 15 | Cap. 03 playbook agentic + MITRE ATLAS, Cap. 04 ([`ARC-014`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-014)+[`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015)), Cap. 05 (AI BOM), Cap. 10 §C5 (*eval suites*), Cap. 12 + [`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014) (*jailbreak* / *off-policy*) | Métricas de exatidão declaradas; limiares regulamentares | Declarar métricas em articulação com equipa de IA |
| Sistema de gestão da qualidade | Art. 17 | Cap. 07 (CI/CD), Cap. 11 (release), Cap. 06, Cap. 14, Policy 38 (mandate lifecycle), Policy 39 (AI BOM lifecycle) | Manual da qualidade formal | Mapear gates SbD-ToE + ciclos Policy 38/39 para os elementos do QMS |
| Cadeia de fornecimento | Art. 25 | [`DEP-013`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-013) (*pinning*), [`DEP-014`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-014) (lista de *providers* aprovados), Policy 39, Cap. 14 US-21 | — | — |
| Obrigações do *deployer* | Art. 26 | Policy 38 (mandate + ownership), Cap. 02 §A0–A4, Cap. 12 US-13 (logs sob controlo do *deployer*) | Documentação operacional do *deployer* | Estender mandate com obrigações específicas quando organização é *deployer* |
| Conformidade e marcação CE | Art. 43, 47–49 | — ([`DEP-014`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-014) é a declaração de conformidade do *provider*, não a marcação CE da própria organização) | Avaliação de conformidade do sistema + marcação CE da organização | Estabelecer swimlane GRC + jurídico para o circuito de avaliação |
| GPAI e risco sistémico | Art. 53, Art. 55 | Cap. 03 playbook + Cap. 05 (AI BOM), Cap. 10 §C5 (*eval suites* + *red teaming*), Cap. 12 US-13 + [`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014), Policy 19 §7, Policy 30 §9 | Documentação técnica GPAI (Anexo XI/XII); política de *copyright* | Documentação delegada à equipa de IA; *cybersecurity* já dentro |
| Monitorização pós-comercialização | Art. 72 | Cap. 12 (monitorização, *drift*), `OPS-011..014`, Cap. 12 US-13 | Plano formal de monitorização pós-mercado por sistema | Formalizar plano por sistema com base nos sinais já disponíveis |
| Incidentes graves | Art. 73 | Cap. 12, Cap. 14, [`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014) (*off-policy* → IR), Policy 30 §9.3, Policy 16 §11.4 (incidentes agentic-específicos) | Definição regulamentar de "incidente grave"; prazos (2/10/15 dias) e *templates* | Parametrizar *runbook* e exportadores SIEM/ITSM |

---

## PARTE I: ANÁLISE NORMATIVA

### Artigo 4 - Literacia em IA

**Conteúdo normativo**

O Art. 4 obriga *providers* e *deployers* a assegurar que os colaboradores envolvidos na operação ou utilização de sistemas de IA têm um **nível adequado de literacia em IA**, ponderando os seus conhecimentos técnicos, experiência, educação e formação, bem como o contexto em que o sistema vai ser usado e os destinatários previstos.

**Cobertura SbD-ToE**

| Requisito AI Act | Capítulo SbD-ToE | Cobertura |
|---|---|---|
| Formação proporcional por papel | Cap. 13 + Policy 37 §11 | Matriz de cobertura por *role* (developer, appsec, devops, grc, tech lead, PO/SM, CISO) + exercícios práticos |
| Atualização periódica | Policy 37 §11 | Cadências: onboarding + actualização anual ou semestral conforme *role* |
| Trilhos para uso assistido vs autónomo | Cap. 13 (addon 12) + Policy 16 + Policy 38 | Diferenciação entre uso assistido (A0–A1) e operação autónoma (A2+) |

**O que o SbD-ToE cobre**

- **Matriz de cobertura formativa por *role*** (Policy 37 §11) — define conteúdos mínimos, cadência e exercícios práticos por papel.
- **Distinção entre uso assistido e autónomo** — quem opera agentes A2+ tem trilho formativo específico (modelo A0–A4, `REQ-AGN-*`, *kill-switch*, OOB approval), além do trilho de uso assistido.
- **Exercícios práticos** — *tabletops* de *off-policy action*, *red team* contra agente em sandbox, exercício de classificação de *mandate* (Policy 37 §11.2).
- **Activação automática** — quando a organização adopta agentes AI em A1+, o módulo agentic da Policy 37 §11 passa a ser **obrigatório** (em vez de recomendado).

**Lacunas residuais**

A **avaliação formal de literacia** (testes, certificações internas, acompanhamento de competência ao longo do tempo) é trabalho de RH e da função de capacitação. O SbD-ToE define o **conteúdo mínimo** e a **cadência**, não o método de avaliação individual.

**Como cumprir**

A Policy 37 §11 é directamente operacionalizável. Para organizações com adopção heavy de agentes, sugere-se complementar com avaliação periódica de competência e registo formal das conclusões dos trilhos como evidência para Art. 4.

---

### Artigo 9 - Sistema de gestão de risco

**Conteúdo normativo**

O Art. 9 exige um sistema de gestão de risco **contínuo e iterativo** ao longo de todo o ciclo de vida do sistema de IA de alto risco: identificação e análise dos riscos conhecidos e razoavelmente previsíveis para a saúde, segurança e direitos fundamentais; estimativa dos riscos em uso previsto e em utilização indevida razoavelmente previsível; adoção de medidas de gestão de risco adequadas; e teste para identificar as medidas mais apropriadas.

**Cobertura SbD-ToE**

| Requisito AI Act | Capítulo SbD-ToE | Cobertura |
|---|---|---|
| Identificação e análise de riscos | Cap. 03 | Threat modeling (STRIDE, MITRE ATT&CK) + [playbook agentic](/sbd-toe/sbd-manual/threat-modeling/addon/metodologias-e-ferramentas#playbook-agentic) com MITRE ATLAS já incluído |
| Proporcionalidade ao risco | Cap. 01 + Cap. 02 §A0–A4 | Classificação L1–L3 + níveis de autonomia agentic A0–A4 ([`REQ-AGN-002`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn)) |
| Medidas de gestão de risco | Cap. 02 | Catálogo de requisitos por nível + `REQ-AGN-001..004` |
| Avaliação iterativa e contínua | Cap. 12 | Monitorização contínua, melhoria + `OPS-011..014` |

**O que o SbD-ToE cobre**

- Identificação estruturada de ameaças via threat modeling (Cap. 03), com o **playbook agentic** já incorporado e MITRE ATLAS como catálogo activo (não apenas extensível).
- Classificação de criticidade aplicacional (Cap. 01), base para proporcionalidade de controlos, **complementada pelos níveis de autonomia A0–A4** para sistemas que incluem agentes AI com *tool-use* ([`REQ-AGN-002`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn)).
- Catálogo de requisitos de segurança e respetivas medidas (Cap. 02), incluindo o subconjunto agentic `REQ-AGN-001..004`.
- Reavaliação contínua, em ciclo, com métricas operacionais (Cap. 12), incluindo sinais agentic-específicos (`OPS-011..014`).

**Lacunas intencionais**

O threat modeling do SbD-ToE é, por construção, **agnóstico ao domínio**: cobre ameaças de segurança ao sistema, mas não prescreve a análise de riscos para **saúde, segurança e direitos fundamentais** específica do AI Act (p. ex., risco de discriminação, impacto societal). Esta dimensão é própria do AI Act e exige envolvimento de equipas de domínio, ética e jurídico.

**Como cumprir**

Sugere-se estender o threat model do Cap. 03 com uma taxonomia de risco de IA - usando o **MITRE ATLAS** para o vetor adversarial e o **NIST AI RMF** / **ISO/IEC 23894** para o enquadramento de risco - e ligar a iteração ao ciclo de melhoria contínua do Cap. 12. Documentar o risco residual e as medidas, mantendo o registo auditável que o Art. 9 pressupõe.

---

### Artigo 10 - Dados e governação de dados

**Conteúdo normativo**

O Art. 10 exige que os conjuntos de dados de treino, validação e teste obedeçam a práticas de governação de dados adequadas: relevância, representatividade, ausência de erros e completude na medida do possível, propriedades estatísticas apropriadas, e exame de possíveis enviesamentos suscetíveis de afetar saúde, segurança ou direitos fundamentais.

**Cobertura SbD-ToE**

| Requisito AI Act | Capítulo SbD-ToE | Cobertura |
|---|---|---|
| Proveniência e integridade de dados | Cap. 05 + [`DEP-011`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-011) (inventário AI) + [`DEP-012`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-012) (AI BOM CycloneDX 1.6 *ml-bom*) | Proveniência, integridade e *pinning* de *datasets* e modelos |
| Requisitos de tratamento de dados | Cap. 02 | Requisitos de segurança de dados |
| Controlo de acesso e proteção | Cap. 04 | Arquitetura segura, classificação de dados |
| *Pinning* + lista de *providers* aprovados | `DEP-013/014` + Policy 39 | Versão fixa explícita; *providers* aprovados com cláusulas contratuais |

**O que o SbD-ToE cobre**

- Proveniência e integridade de artefactos da cadeia de fornecimento, aplicável a *datasets*, modelos, MCP *tools* e prompts embebidos (Cap. 05 §`DEP-011..014`).
- **AI BOM por *build*** em formato standardizado (CycloneDX 1.6 *ml-bom*) — operacionaliza a *AI-BOM* que estava sugerida na primeira versão deste cross-check (Policy 39, Cap. 05 US-14).
- Requisitos de proteção, classificação e controlo de acesso a dados (Cap. 02, Cap. 04).

**Lacunas residuais**

A **qualidade estatística, representatividade e deteção/mitigação de enviesamento** continuam a ser problemas de **ciência de dados e do domínio de aplicação**, não de segurança aplicacional. O SbD-ToE não prescreve métricas de *fairness*, técnicas de *debiasing* nem critérios de representatividade — corretamente, pois variam por caso de uso e são da competência das equipas de IA/dados.

**Como cumprir**

A *AI-BOM* que estava sugerida em versões anteriores deste documento **já está implementada** ([`DEP-012`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-012), Policy 39, Cap. 05 US-14). Resta complementar o SbD-ToE com um processo de *data governance* de ciência de dados — linhagem de dados, *datasheets for datasets*, *data cards*, avaliação de enviesamento — articulado com a equipa de IA.

---

### Artigo 11 e Anexo IV - Documentação técnica

**Conteúdo normativo**

O Art. 11 exige documentação técnica elaborada **antes** da colocação no mercado e mantida atualizada, demonstrando conformidade. O Anexo IV detalha o índice mínimo: descrição geral do sistema, elementos de desenvolvimento e conceção, monitorização e controlo, gestão de risco, alterações ao longo do ciclo de vida, e lista de normas aplicadas.

**Cobertura SbD-ToE**

| Requisito AI Act | Capítulo SbD-ToE | Cobertura |
|---|---|---|
| Descrição técnica e de arquitetura | Cap. 04 + `ARC-014/015` | Documentação de arquitetura segura, incluindo padrões agentic |
| Requisitos e medidas de segurança | Cap. 02 + `REQ-AGN-001..004` | Catálogo de requisitos (incluindo subconjunto agentic) |
| Processo de desenvolvimento | Cap. 06, Cap. 07 | Desenvolvimento seguro, CI/CD com gates |
| Gestão de risco e alterações | Cap. 03, Cap. 12 | Threat model + playbook agentic; monitorização e melhoria |
| Inventário de componentes e modelos | Cap. 05 + [`DEP-012`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-012) AI BOM + Policy 39 | Lista de componentes (Anexo IV §2(a)) incluindo modelos, datasets, *tools* e prompts |
| Operação sob mandate | Policy 38 | *Mandate* documentado e versionado por agente AI |

**O que o SbD-ToE cobre**

- Documentação de arquitetura e decisões de segurança (Cap. 04), incluindo padrões agentic [`ARC-014`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-014) e [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015).
- Requisitos e medidas por nível de criticidade (Cap. 02), incluindo os requisitos `REQ-AGN-*` para agentes AI.
- Evidência de processo de desenvolvimento e pipeline (Cap. 06, Cap. 07).
- **AI BOM** como artefacto auditável que materializa parte da lista de componentes exigida pelo Anexo IV §2(a) ([`DEP-012`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-012), Policy 39).
- ***Mandate*** de cada agente AI como artefacto operacional rastreável (Policy 38) — entra no índice Anexo IV §2(b) (elementos de desenvolvimento e conceção) sempre que o sistema inclui agentes.

**Lacunas intencionais**

O SbD-ToE não gera a documentação **na estrutura formal do Anexo IV** nem um **model card** normalizado. A organização dos artefactos segundo o índice regulamentar é trabalho de mapeamento, não de produção técnica nova.

**Como cumprir**

Sugere-se construir um "índice Anexo IV" que aponte para os artefactos SbD-ToE existentes (arquitetura, requisitos, threat model, evidência de pipeline e testes), complementado por um *model card* (finalidade, dados de treino, métricas de desempenho, limitações) da responsabilidade da equipa de IA.

---

### Artigo 12 e Artigo 19 - Registo de eventos (logging) e conservação de logs

**Conteúdo normativo**

O Art. 12 exige capacidade de **registo automático de eventos** (logs) ao longo do ciclo de vida, com nível de rastreabilidade adequado à finalidade, permitindo identificar situações de risco e suportar a monitorização pós-comercialização. O Art. 19 obriga os fornecedores a **conservar os logs** gerados automaticamente, na medida em que estejam sob o seu controlo.

**Cobertura SbD-ToE**

| Requisito AI Act | Capítulo SbD-ToE | Cobertura |
|---|---|---|
| Logging "by design" | Cap. 12 | Observabilidade, logging estruturado |
| Rastreabilidade de eventos | Cap. 12 + [`OPS-011`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes) (AI/ML) + [`OPS-012`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-012) (audit per *tool invocation*) | Trilho auditável e correlação, com agente identificado por `agent_id` + `session_id` + `mandate_ref` |
| *Tool invocation audit* | [`OPS-012`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-012) + Cap. 12 US-13 | Cada *tool call* gera *audit event* estruturado (com `intent_event_ref` em A2+) |
| Detecção de *off-policy* e *jailbreak* | [`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014) + Policy 30 §9.3 | Sinais accionáveis ligados a IR |
| Conservação e retenção | Cap. 12 + `OPS-003` | Políticas de retenção e imutabilidade |

**O que o SbD-ToE cobre**

- Logging estruturado e observabilidade "by design" (Cap. 12).
- **Audit completo por *tool invocation*** quando há agentes AI ([`OPS-012`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-012)) — cada chamada gera evento com `timestamp`, `agent_id`, `session_id`, `mandate_ref`, `autonomy_level`, `tool`, `tool_version`, `args` (PII redactada), `intent_event_ref`, `outcome`, `external_effect`. Granular numa dimensão **complementar** (operacional) à do log epistémico de inferência exigido pelo Art. 12 — não o substitui.
- Trilho auditável e correlação de eventos, com orientação para retenção e imutabilidade (Cap. 12).
- **Telemetria operacional agentic** (Cap. 12 US-13) que sustenta a base evidencial para Art. 72 (monitorização pós-mercado) e Art. 73 (incidentes graves).

**Lacunas residuais**

O esquema do *model output* (versão de modelo, *features* relevantes, decisão, confiança) continua **configurável por sistema** — depende do caso de uso e do equilíbrio com a proteção de dados pessoais. O Cap. 12 fixa o esquema *operacional* (quem invocou, com que mandate, sobre que recurso); o esquema *epistémico* (porquê este output) é declarado por sistema.

**Como cumprir**

A camada operacional já está implementada (`OPS-011..014` + Cap. 12 US-13). Resta declarar o esquema do *model output* por sistema, garantindo retenção alinhada com a vida útil e com requisitos do RGPD. Documentar o período de conservação como evidência para Art. 12/19.

---

### Artigo 13 - Transparência e prestação de informação aos utilizadores implementadores

**Conteúdo normativo**

O Art. 13 exige que os sistemas de alto risco sejam suficientemente transparentes para que os *deployers* interpretem e usem o output adequadamente, acompanhados de **instruções de utilização** com identidade do fornecedor, características, capacidades, limitações de desempenho, riscos conhecidos e medidas de supervisão humana.

**Cobertura SbD-ToE**

| Requisito AI Act | Capítulo SbD-ToE | Cobertura |
|---|---|---|
| Documentação de capacidades e limitações | Cap. 02, Cap. 04, Policy 38 (mandate) | Requisitos, arquitetura e *mandate* com `capabilities` + `scope` + `risk_residual` |
| Identidade do *provider* e *runtime* | Policy 38 (`agent_runtime` no mandate) + [`DEP-014`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-014) (lista de *providers*) | Identidade do *provider* AI + versão *pinned* do modelo |
| Supervisão humana exigida | Cap. 02 §A0–A4 + Policy 38 | Nível de autonomia A0–A4 declarado por uso/contexto |

**O que o SbD-ToE cobre**

- Base documental de requisitos e arquitetura que alimenta parte das instruções de utilização (Cap. 02, Cap. 04).
- ***Mandate*** (Policy 38) como **fonte estruturada** de *capabilities*, *scope*, *autonomy_level*, *risk_residual* e procedimentos de supervisão — directamente extractável para "instruções de utilização" do *deployer*.

**Lacunas residuais**

As **métricas de desempenho** (acurácia, precisão, *recall*) e os **níveis de exatidão** continuam a depender do modelo concreto e do domínio — declaração pela equipa de IA. O SbD-ToE não substitui esse trabalho, mas reduziu materialmente o que falta produzir para as instruções de utilização.

**Como cumprir**

Sugere-se derivar um documento de "instruções de utilização" a partir do ***mandate*** (Policy 38), dos artefactos do Cap. 04 (arquitetura, fronteiras de confiança) e Cap. 06, complementado pelas métricas de desempenho e limitações fornecidas pela equipa de IA.

---

### Artigo 14 - Supervisão humana

> ⚡ **Refresh 2026-05-30.** A primeira versão deste cross-check tratava o Art. 14 como largamente fora de AppSec ("desenho de mecanismos de supervisão é problema de IA/produto"). Com a camada agentic introduzida em 2026 — A0–A4, `REQ-AGN-*`, [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015), Policy 38 — a **faceta de interrupção (*stop/override*) e de governação** ficou coberta. A **supervisão-como-compreensão** (o juízo humano e a UX de intervenção) permanece domínio da equipa de IA/produto; o *como* arquitectónico e o *quando* governativo já vivem no manual.

**Conteúdo normativo**

O Art. 14 exige que os sistemas de alto risco sejam concebidos para permitir **supervisão humana efetiva**, incluindo a capacidade de compreender as capacidades e limitações, detetar e interpretar o output, decidir não usar ou anular o sistema, e interromper o seu funcionamento (*stop*).

**Cobertura SbD-ToE**

| Requisito AI Act | Capítulo SbD-ToE | Cobertura |
|---|---|---|
| Definir nível de supervisão proporcional | Cap. 02 §A0–A4 + [`REQ-AGN-002`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn) | Cinco níveis de autonomia (A0 leitura → A4 autónomo); classificação por contexto |
| Mandate operacional com supervisão declarada | Policy 38 (mandate) + [`REQ-AGN-001`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn) | *Owner*, *approver*, `review_cadence`, *kill-switch*, *intent audit sink* |
| Capacidade arquitectónica de interrupção (*stop*) | [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015) + [`REQ-AGN-003`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn) (*kill-switch*) | Revogação de credenciais + terminação de *runtime* + isolamento de *namespace* + alerta on-call, em segundos |
| Anulação consciente de acção destrutiva | [`REQ-AGN-004`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn) (*intent declaration*) + [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015) (OOB approval) | Agente declara intenção antes de *tool call* destrutivo; aprovação humana *out-of-band* exigida em A2+ |
| Exercício periódico do *stop* | Policy 38 + Policy 18 §9.3 | *Kill-switch* exercitado em sandbox/staging (anual A2, trimestral A3, mensal A4) com cronómetro registado |
| Auditoria de *off-policy actions* | [`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014) + Policy 30 §9.3 + Policy 16 §11.4 | Divergência entre `intent` declarado e acção real gera alerta accionável + entra em IR |

**O que o SbD-ToE cobre**

- **Modelo normativo de níveis de supervisão** (Cap. 02 §A0–A4). A escolha *human-in-the-loop* / *human-on-the-loop* / *autonomous* é declarada explicitamente por contexto, com critérios de promoção e descida; subir nível exige evidência operacional dos pré-requisitos.
- ***Mandate*** (Policy 38) — operacionaliza Art. 14 declarando, para cada agente em uso, **quem supervisiona**, **com que cadência**, **com que *kill-switch*** e **sob que mandato assinado**.
- ***Kill-switch* arquitectónico** ([`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015) + [`REQ-AGN-003`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn)) — não é um botão simbólico: revoga credenciais OIDC + termina sessões + isola *namespace* + alerta on-call, com tempo medido. Exercitado periodicamente conforme nível de autonomia.
- ***Intent declaration*** ([`REQ-AGN-004`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn)) — em A2+, antes de cada *tool call* destrutivo o agente declara à infraestrutura *o que vai fazer e porquê*; o gate cruza intent vs acção real a posteriori ([`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014)).
- **Aprovação humana *out-of-band*** — fora do canal do agente (Slack, GitHub review, webhook assinado), para que *prompt injection* no canal principal não consiga "auto-aprovar".

**Lacunas residuais**

A **UX da decisão humana** (como o utilizador interpreta o output e decide intervir) e a especificação dos **pontos cognitivos de supervisão** (quando o sistema deve pedir confirmação, que informação mostrar) continuam fora do âmbito AppSec — são desenho de sistema de IA e fatores humanos. O SbD-ToE garante que a interrupção é **implementável, exercitada, audita­da e governativa­mente exigida**; não desenha a interface de supervisão.

**Como cumprir**

A maior parte do trabalho técnico está agora dentro do manual: declarar o nível A0–A4 no *mandate* (Policy 38), instrumentar *kill-switch* exercitado ([`REQ-AGN-003`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn)) e *intent declaration* ([`REQ-AGN-004`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn)) conforme [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015), e configurar [`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014) para detectar divergência. A equipa de IA/produto complementa com a UX da intervenção e os pontos cognitivos de supervisão. Para sistemas de alto risco com componente agentic, a US-15 (Cap. 02) + US-16 (Cap. 04) constituem o checklist operacional.

---

### Artigo 15 - Exatidão, robustez e cibersegurança

> 🎯 **Núcleo do cross-check.** É no Art. 15 que o SbD-ToE oferece a cobertura mais forte e direta. A cibersegurança de sistemas de IA é, em grande medida, a disciplina central do manual aplicada a um novo tipo de artefacto (modelos e pipelines de ML).

**Conteúdo normativo**

O Art. 15 exige que os sistemas de alto risco atinjam um nível adequado de **exatidão, robustez e cibersegurança** e tenham desempenho consistente ao longo do ciclo de vida. O n.º 5 é explícito quanto ao vetor adversarial: os sistemas devem ser resilientes a tentativas de terceiros não autorizados de alterar o uso, output ou desempenho explorando vulnerabilidades, e as medidas técnicas devem prevenir, detetar, responder, resolver e controlar ataques que visem o **envenenamento de dados (*data poisoning*)**, o **envenenamento de modelo (*model poisoning*)**, os **exemplos adversariais ou evasão de modelo (*adversarial examples / model evasion*)**, os **ataques à confidencialidade** e as **falhas do modelo (*model flaws*)**.

**Cobertura SbD-ToE**

| Requisito AI Act | Capítulo SbD-ToE | Cobertura |
|---|---|---|
| Identificação de ameaças adversariais | Cap. 03 + [playbook agentic](/sbd-toe/sbd-manual/threat-modeling/addon/metodologias-e-ferramentas#playbook-agentic) | MITRE ATLAS + OWASP LLM Top 10 2025 já incorporados como catálogos activos |
| Defesa em profundidade e isolamento | Cap. 04 ([`ARC-014`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-014)/[`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015)) | Trust boundaries (incl. *agentic boundary*); agente como *principal* isolado |
| Integridade da cadeia (dados/modelos) | Cap. 05 (`DEP-011..014`) + Policy 39 | Proveniência + AI BOM + *pinning* + *providers* aprovados |
| Testes de robustez e *red teaming* | Cap. 10 §C5 + Policy 19 §7 | *Eval suites* contínuas (regression de prompt, abuse corpus, *A/B*, drift) |
| Deteção e resposta em *runtime* | Cap. 12 + [`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014) + Policy 30 §9 | Detecção de *jailbreak* / *off-policy*; *audit per tool invocation* |
| Hardening do serviço de inferência | Cap. 04, Cap. 09 + [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015) | Arquitetura, containers/runtime, identidade efémera |

**O que o SbD-ToE cobre**

- **Modelação de ameaças** (Cap. 03), com o **playbook agentic** (DFD + threat library MITRE ATLAS + OWASP LLM Top 10 2025) já incluído como catálogo activo — não apenas extensível.
- **Arquitetura defensiva** (Cap. 04): fronteiras de confiança (incluindo a *agentic boundary* em [`ARC-014`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-014) e o agente como *principal* em [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015)), segregação, validação de input, limitação de exposição do serviço de inferência.
- **Integridade da cadeia de fornecimento** (Cap. 05 `DEP-011..014`): proveniência, AI BOM ([`DEP-012`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-012) CycloneDX 1.6 *ml-bom*), *pinning* de versão ([`DEP-013`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-013) — mitiga `AML.T0109` *Supply Chain Rug Pull*), lista de *providers* aprovados ([`DEP-014`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-014)).
- **Testes de segurança** (Cap. 10 §C5 *eval suites*): regression tests de prompt/skill, *abuse* / *red-team corpus* (LLM01-2025 prompt injection, LLM06-2025 excessive agency), *drift detection*, *A/B testing*.
- **Monitorização em runtime** (Cap. 12 + `OPS-011..014`): deteção de anomalias, *model drift*, *audit per tool invocation* ([`OPS-012`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-012)), *budget / runaway* ([`OPS-013`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-013)), *jailbreak* / *off-policy actions* ([`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014)).
- **Hardening de runtime** (Cap. 09 + [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015)): isolamento do serviço de inferência em containers; agente AI com *workload identity* efémera OIDC + *scope* mínimo por *tool*.

**Lacunas intencionais**

O SbD-ToE não fixa **métricas de exatidão** nem limiares regulamentares de desempenho (são específicos do modelo e do caso de uso). Não prescreve, na versão base, técnicas adversariais concretas (*adversarial training*, *input sanitization* específica de ML, *output filtering* de LLM) - estas são adições de domínio que o manual enquadra mas não impõe, para preservar universalidade.

**Como cumprir**

Sugere-se: (1) estender o threat model (Cap. 03) com o **MITRE ATLAS** e o **OWASP ML/LLM Top 10**; (2) adicionar ao catálogo de testes (Cap. 10) **testes de robustez adversarial** e um programa de **AI red teaming**; (3) tratar a proveniência de dados e modelos como cadeia de fornecimento crítica (Cap. 05); (4) configurar a monitorização (Cap. 12) para *drift* e padrões de ataque; (5) declarar as métricas de exatidão obtidas e os limiares aceitáveis, em articulação com a equipa de IA.

---

### Artigo 17 - Sistema de gestão da qualidade (QMS)

**Conteúdo normativo**

O Art. 17 obriga os fornecedores a um sistema de gestão da qualidade documentado, abrangendo estratégia de conformidade, procedimentos de conceção e desenvolvimento, controlo de qualidade, testes e validação, gestão de risco, monitorização pós-comercialização e comunicação de incidentes.

**Cobertura SbD-ToE**

| Requisito AI Act | Capítulo SbD-ToE | Cobertura |
|---|---|---|
| Procedimentos de desenvolvimento | Cap. 06, Cap. 07 (incl. US-19) | Desenvolvimento seguro, CI/CD com gates, agentes como *principals* na pipeline |
| Controlo de qualidade e validação | Cap. 10 §C5 (*eval suites*) + Cap. 11 | Testes, gate de release, regression de prompts |
| Gestão de risco | Cap. 03 + playbook agentic | Threat modeling + threat library MITRE ATLAS |
| Governação e responsabilidades | Cap. 14 + Policy 38 (mandates) + Policy 39 (AI BOM lifecycle) | RACI, políticas, aprovações; ciclo de vida formal para agentes e supply chain AI |
| Monitorização e incidentes | Cap. 12 + `OPS-012..014` + Policy 30 §9 | Monitorização agentic + IR para *off-policy* / *jailbreak* |

**O que o SbD-ToE cobre**

- Procedimentos de desenvolvimento e pipeline com gates auditáveis (Cap. 06, Cap. 07), incluindo agentes AI como *principals* (US-19).
- Controlo de qualidade técnico e validação pré-release (Cap. 10, Cap. 11), incluindo *eval suites* contínuas para agentes (§C5).
- Estrutura de governação, papéis e aprovações (Cap. 14).
- **Ciclo de vida formal de governação para agentes AI** (Policy 38) — *mandate* com proposta → avaliação → aprovação → activação → operação → revisão / revogação. Mapeável directamente aos elementos do QMS do Art. 17 §3 (procedimentos, sistemas de gestão de dados, registos de comunicação).
- **Ciclo de vida formal para *supply chain* AI** (Policy 39) — formato AI BOM, *pinning*, lista aprovada de *providers*, resposta a incidentes *upstream* por classe.

**Lacunas intencionais**

O SbD-ToE fornece os **componentes operacionais** de um QMS técnico, mas não a sua **estrutura formal e documental** conforme o Art. 17 (procedimentos escritos, responsabilidades de gestão, manual da qualidade). Esta formalização é trabalho de organização documental.

**Como cumprir**

Sugere-se mapear os gates e processos SbD-ToE (Cap. 06/07/10/11/14) para os elementos do Art. 17, produzindo um documento de QMS que referencie estes controlos como evidência - reaproveitando, quando aplicável, um sistema **ISO/IEC 42001** já existente.

---

### Artigo 25 - Cadeia de fornecimento e responsabilidades ao longo da cadeia

**Conteúdo normativo**

O Art. 25 trata da distribuição de responsabilidades quando vários intervenientes contribuem para um sistema de IA — *providers* a montante, distribuidores, importadores, integradores, *deployers* — e exige cooperação contratual, partilha de informação necessária ao cumprimento das obrigações e tratamento de mudanças substanciais que possam reclassificar o sistema.

**Cobertura SbD-ToE**

| Requisito AI Act | Capítulo SbD-ToE | Cobertura |
|---|---|---|
| Versão *pinned* de modelos e componentes AI | [`DEP-013`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-013) | Versão fixa explícita; sem `latest` / ranges / aliases dinâmicos |
| Lista de *providers* AI aprovados | [`DEP-014`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-014) + Policy 39 | Lista versionada com `risk_classification`, `contract_ref`, cláusulas críticas |
| AI BOM por *build* | [`DEP-012`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-012) + Policy 39 | CycloneDX 1.6 *ml-bom* gerado por *release* |
| Cláusulas contratuais com *providers* | Cap. 14 US-21 + Policy 33 §10 | Cláusulas de retention, localização, audit, notificação, conformidade |
| Resposta a incidentes *upstream* | Policy 39 §7 | Triagem por classe (`AML.T0019` *data poisoning*, `AML.T0109` *rug pull*, `AML.T0110` *tool poisoning*, *provider outage*) |

**O que o SbD-ToE cobre**

- **Materialização da cadeia de fornecimento AI** como inventário auditável: *pinning*, lista de *providers* aprovados, AI BOM por *release*.
- **Cláusulas contratuais** específicas para *providers* AI (Policy 33 §10) — data retention, training opt-out, localização (RGPD Art. 44–49), *audit rights*, SLA de notificação prévia de mudanças, declaração de conformidade Art. 53/55 quando GPAI.
- **Resposta a incidentes *upstream*** por classe — `AML.T0019` *Publish Poisoned Datasets*, `AML.T0109` *AI Supply Chain Rug Pull*, `AML.T0110` *AI Agent Tool Poisoning*, *provider outage* — com *runbooks* específicos.
- **Reclassificação por mudança material** — Cap. 03 US-11 e Cap. 04 US-16 obrigam a revisão do *threat model* e da arquitectura quando o *provider* muda versão maior do modelo ou quando a `tools_allowlist` muda.

**Lacunas residuais**

A **definição contratual jurídica** das responsabilidades ao longo da cadeia (quem responde por quê em caso de incidente, distribuição de SLA de notificação a autoridades) continua do âmbito Legal — o SbD-ToE fornece a estrutura técnica e operacional, não a redacção jurídica.

**Como cumprir**

Operacionalmente já está implementado (Policy 39 + `DEP-013/014` + Cap. 14 US-21). Resta a articulação Legal para garantir que as cláusulas contratuais alinhadas com Policy 33 §10 satisfazem também os requisitos do Art. 25 — em particular para sistemas em que a organização é simultaneamente *provider* e *deployer*.

---

### Artigo 26 - Obrigações dos *deployers*

**Conteúdo normativo**

O Art. 26 define obrigações específicas dos *deployers* de sistemas de IA de alto risco: usar o sistema conforme as instruções de utilização, atribuir supervisão humana qualificada, assegurar input data adequado, monitorizar o funcionamento, conservar logs sob seu controlo (Art. 19), e cooperar com autoridades.

**Cobertura SbD-ToE**

| Requisito AI Act | Capítulo SbD-ToE | Cobertura |
|---|---|---|
| Uso conforme instruções; supervisão atribuída | Policy 38 (mandate com `owner`, `approver`, `autonomy_level`) | *Mandate* declara *quem supervisiona*, *com que cadência*, *sob que mandato* |
| Atribuição de supervisão qualificada | Cap. 00 (nota AI Reliability Engineer) + Policy 37 §11 | Função composta + literacia obrigatória por *role* |
| Monitorização do funcionamento | Cap. 12 US-13 + `OPS-011..014` | Telemetria agentic em produção |
| Conservação de logs (Art. 19) | Cap. 12 + `OPS-003` (retention) + [`OPS-012`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-012) (audit per tool) | *Audit trail* completo sob controlo do *deployer* |
| Comunicação a autoridades | Cap. 12 + Cap. 14 + Policy 30 §9.3 + Policy 32 (IRP) | IR alimenta notificação a autoridades |

**O que o SbD-ToE cobre**

- **Mandate como artefacto de *deployer*** (Policy 38) — quando a organização opera (e não fornece) um sistema de IA de alto risco, o *mandate* é a evidência formal de "como usa-se este sistema, sob que supervisão, com que *kill-switch*". Directamente extractável para auditoria do Art. 26.
- **Função composta para supervisão qualificada** (Cap. 00 nota *AI Reliability Engineer*) — `appsec` + `devops` + `grc` sob mandate do `CISO`, com literacia obrigatória (Policy 37 §11).
- **Monitorização operacional** (Cap. 12 US-13, `OPS-011..014`) — logs e sinais sob controlo do *deployer*, conservados conforme política (`OPS-003`).
- **Resposta a incidentes** ligada à notificação a autoridades (Cap. 12 + Policy 30 §9.3 + Policy 32) — *off-policy actions* e *jailbreak* em produção entram no fluxo IR que alimenta Art. 73.

**Lacunas residuais**

Quando a organização é simultaneamente *provider* e *deployer* (caso comum em desenvolvimento *first-party*), a separação de obrigações entre os dois papéis fica diluída — convém clarificar internamente (e contratualmente quando há sub-deployers) qual papel se assume em cada uso.

**Como cumprir**

Para usos em que a organização é *deployer*, o *mandate* (Policy 38) é o artefacto central. Sugere-se um *template* específico para *deployer mandate* que documente explicitamente a referência ao *provider* (`contract_ref` + [`DEP-014`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-014)), as instruções de utilização recebidas, e o alinhamento com os requisitos do Art. 26.

---

### Artigo 72 - Monitorização pós-comercialização

**Conteúdo normativo**

O Art. 72 exige um sistema de monitorização pós-comercialização proporcional, com um plano documentado, que recolha e analise dados sobre o desempenho do sistema ao longo da sua vida, permitindo avaliar a conformidade contínua.

**Cobertura SbD-ToE**

| Requisito AI Act | Capítulo SbD-ToE | Cobertura |
|---|---|---|
| Recolha contínua de telemetria | Cap. 12 + `OPS-011..014` + Cap. 12 US-13 | Observabilidade AI/ML + sinais agentic-específicos |
| Análise de desempenho e degradação | Cap. 12 + [`OPS-011`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes) | Deteção de *drift*, anomalias, degradação de precisão |
| *Audit per tool invocation* | [`OPS-012`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-012) | Reconstrução *post-mortem* de qualquer sessão agentic |
| *Token budget* e *runaway* | [`OPS-013`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-013) | Detecção de consumo descontrolado e mudanças de eficiência |
| *Off-policy actions* e *jailbreak* | [`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014) + Policy 30 §9.3 | Sinais accionáveis ligados a IR |
| Melhoria contínua | Cap. 12 + Cap. 10 §C5 (*eval suites*) | Ciclo pós-incidente realimenta *eval suite* offline |

**O que o SbD-ToE cobre**

- Recolha e análise contínua de telemetria operacional (Cap. 12), com sinais agentic-específicos completos (`OPS-011..014`).
- **Telemetria agentic** (Cap. 12 US-13) que materializa a base evidencial para o plano de monitorização pós-mercado: *tool invocation audit events*, *intent events*, *budget metrics*, *off-policy / jailbreak detection*.
- Deteção de degradação de desempenho e *model drift* (Cap. 12, [`OPS-011`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes)).
- **Ciclo de realimentação para *eval suites*** (Cap. 10 §C5) — incidentes detectados em produção alimentam a suite offline, fortalecendo a regressão futura.

**Lacunas intencionais**

O SbD-ToE não define o **plano formal de monitorização pós-mercado** com a estrutura do Art. 72 nem os indicadores específicos de desempenho de IA a reportar à autoridade.

**Como cumprir**

Sugere-se formalizar um plano de monitorização pós-mercado assente na observabilidade do Cap. 12, com *dashboards* de desempenho, *drift* e estado de vulnerabilidades, e gatilhos de reavaliação que alimentem o ciclo do Art. 9.

---

### Artigo 73 - Comunicação de incidentes graves

**Conteúdo normativo**

O Art. 73 obriga os fornecedores a comunicar **incidentes graves** às autoridades de fiscalização do mercado, em prazos definidos — em regra **até 15 dias** após conhecimento; **até 10 dias** em caso de morte de uma pessoa; e **até 2 dias** em caso de infração generalizada ou de perturbação grave e irreversível de infraestrutura crítica (Art. 3.º, n.º 49, al. b)) — e a tomar medidas corretivas.

**Cobertura SbD-ToE**

| Requisito AI Act | Capítulo SbD-ToE | Cobertura |
|---|---|---|
| Deteção e resposta a incidentes | Cap. 12 + [`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014) (*jailbreak* / *off-policy*) + Policy 30 §9.3 | Processo de deteção, resposta, pós-incidente; sinais agentic accionáveis |
| Classes de incidente agentic-específicas | Policy 16 §11.4 | *Off-policy action*, *intent-action divergence*, *prompt injection* bem-sucedida, falha de *kill-switch*, *credential exposure* |
| Resposta a incidentes *upstream* | Policy 39 §7 | *Rug pull*, *dataset poisoning*, *tool poisoning*, *provider outage* |
| Escalonamento e responsabilidades | Cap. 14 + Policy 38 | Papéis e responsabilidades; *owner* + *approver* declarados no *mandate* |
| Classificação de severidade | Cap. 01, Cap. 12 | Critérios de impacto, classificação |

**O que o SbD-ToE cobre**

- Processo de deteção, resposta e pós-incidente (Cap. 12).
- **Classes de incidente agentic-específicas** definidas (Policy 16 §11.4): *off-policy action*, *intent-action divergence*, *prompt injection* bem-sucedida que resultou em *tool call* não autorizada, falha do *kill-switch*, *credential exposure*.
- **Resposta a incidentes *upstream*** (Policy 39 §7) — quando o incidente origina no *provider* de modelo / dataset / MCP server, e não na operação interna.
- Papéis de escalonamento e responsabilidades (Cap. 14, Policy 38).
- Critérios de impacto que suportam a classificação de severidade (Cap. 01, Cap. 12).

**Lacunas intencionais**

O SbD-ToE não fixa a **definição regulamentar de "incidente grave"** do AI Act, nem os prazos (15 dias / 10 dias / 2 dias consoante a gravidade), templates de submissão ou o circuito para a autoridade competente. À semelhança de NIS2 e DORA, estes campos são deixados configuráveis.

**Como cumprir**

Sugere-se parametrizar o runbook e o esquema de incidente do Cap. 12 com a tipologia e prazos do Art. 73, e configurar exportadores do SIEM/ITSM para gerar a notificação pronta a submeter à autoridade de fiscalização do mercado.

---

### Modelos de IA de finalidade geral - Artigos 53 e 55 (GPAI)

**Conteúdo normativo**

O Art. 53 impõe aos fornecedores de **GPAI** documentação técnica do modelo, informação para integradores a jusante, política de respeito pelo direito de autor e um resumo dos dados de treino. O Art. 55 acresce, para GPAI com **risco sistémico**, a obrigação de **avaliação adversarial (*adversarial testing* / *red teaming*)**, avaliação e mitigação de riscos sistémicos, comunicação de incidentes graves e garantia de **cibersegurança adequada do modelo e da infraestrutura física**.

**Cobertura SbD-ToE**

| Requisito AI Act | Capítulo SbD-ToE | Cobertura |
|---|---|---|
| Avaliação adversarial / *red teaming* | Cap. 10 §C5 + Policy 19 §7 + Cap. 03 playbook agentic | *Eval suites* contínuas (regression de prompt, *abuse corpus*, *A/B*, *drift*) + threat library MITRE ATLAS |
| Cibersegurança do modelo e infraestrutura | Cap. 04 ([`ARC-014`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-014)/[`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015)), Cap. 08, Cap. 09 | Arquitetura agentic, IaC, containers/runtime |
| Proteção de pesos e artefactos | Cap. 05 (`DEP-011..014`) + Policy 39 + Cap. 04 | Integridade, proveniência, AI BOM, *pinning*, controlo de acesso |
| Monitorização e incidentes | Cap. 12 + `OPS-011..014` + Policy 30 §9 | Detecção de *off-policy* / *jailbreak* / *exfiltration* via tool |
| Cláusulas contratuais para GPAI | Cap. 14 US-21 + Policy 33 §10 + [`DEP-014`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-014) | Declaração contratual de conformidade Art. 53/55 dos *providers* |

**O que o SbD-ToE cobre**

- **AI red teaming contínuo** materializado (Cap. 10 §C5 + Policy 19 §7) — não apenas como recomendação. *Eval suites* incluem *abuse corpus* (LLM01-2025 *prompt injection*, LLM06-2025 *excessive agency*) com cadência exigida em A4 (mensal).
- **Cibersegurança da infraestrutura** que serve o modelo (Cap. 04 incl. [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015), Cap. 08, Cap. 09).
- **Proteção de integridade e acesso** a pesos, *checkpoints* e *datasets* — agora com AI BOM auditável e *pinning* exigido (`DEP-012/013`, Policy 39). Resposta a `AML.T0109` *Supply Chain Rug Pull* documentada em Policy 39 §7.
- **Monitorização e resposta** (Cap. 12 + [`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014)) — detecção activa de *jailbreak* (LLM01-2025) e *off-policy actions* em produção; corpus de detecção actualizado conforme cadência do *mandate*.
- **Conformidade contratual declarada pelos *providers* GPAI** ([`DEP-014`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-014), Cap. 14 US-21, Policy 33 §10) — exigida no processo de aprovação do *provider*.

**Lacunas intencionais**

O SbD-ToE não prescreve a **documentação técnica GPAI** (Anexo XI/XII), a **política de copyright** nem o **resumo dos dados de treino** - são obrigações de domínio e jurídicas. A avaliação de **riscos sistémicos** (capacidades de impacto à escala) é igualmente externa ao AppSec.

**Como cumprir**

Sugere-se: tratar pesos, *checkpoints* e *datasets* como ativos de cadeia de fornecimento com proveniência e controlo de acesso (Cap. 05); instituir AI red teaming contínuo (Cap. 10) alinhado com o MITRE ATLAS; aplicar hardening de infraestrutura (Cap. 04/08/09); e remeter documentação GPAI, copyright e avaliação de risco sistémico para as equipas de IA, jurídico e compliance.

---

### Práticas proibidas e transparência (Artigos 5 e 50)

**Conteúdo normativo**

O Art. 5 proíbe um conjunto de práticas (p. ex., manipulação subliminar prejudicial, *social scoring* por entidades públicas, certa identificação biométrica remota em tempo real). O Art. 50 impõe deveres de transparência para sistemas de risco limitado (informar que se interage com IA; marcar conteúdo sintético / *deepfakes*).

**Cobertura SbD-ToE**

Ambos os artigos são **essencialmente de natureza jurídica e de conceção de produto**, fora do âmbito técnico-AppSec do SbD-ToE.

**Lacunas intencionais (por desenho)**

O SbD-ToE não determina a admissibilidade de uma finalidade (Art. 5) nem desenha os mecanismos de divulgação ao utilizador (Art. 50). Tecnicamente, pode suportar a **marcação de proveniência de conteúdo** (p. ex., *watermarking*/credenciais de conteúdo) quando essa decisão de produto for tomada.

**Como cumprir**

A determinação de proibições e os deveres de transparência devem ser conduzidos por jurídico e produto. O SbD-ToE entra apenas na **implementação técnica fiável** dos mecanismos escolhidos (integridade da marcação, registo auditável).

---

## PARTE II: SÍNTESE E REFERÊNCIAS

### Síntese da cobertura AI Act / SbD-ToE

O AI Act pede sistemas de IA **seguros, robustos, documentados e supervisionáveis**, com responsabilidade do fornecedor ao longo de todo o ciclo de vida. O SbD-ToE oferece o **coração técnico-operacional** desse esforço: gestão de risco técnico (Cap. 01, 03), arquitetura defensiva (Cap. 04), integridade da cadeia de dados e modelos (Cap. 05), pipelines e gates de qualidade (Cap. 06, 07, 11), testes e robustez adversarial (Cap. 10), logging e monitorização pós-mercado (Cap. 12) e governação (Cap. 14).

A cobertura mais **forte e direta** está no **Art. 15** (exatidão, robustez, cibersegurança) e nos seus correlatos operacionais (Art. 12 logging, Art. 72 monitorização, Art. 73 incidentes, Art. 17 QMS) - é aqui que "implementar SbD-ToE" se aproxima de "cumprir o AI Act".

As lacunas observadas **não são falhas do modelo**, mas **abstenções deliberadas**: dimensões próprias do domínio de IA (governação de dados/enviesamento, exatidão estatística, supervisão humana, transparência) e dimensões jurídicas (classificação de risco, FRIA, avaliação de conformidade, marcação CE, práticas proibidas). Estas exigem equipas de ciência de dados, ética, produto, jurídico e compliance - o SbD-ToE fornece-lhes a evidência técnica, não o juízo de conformidade.

O resultado é coerente com a filosofia do manual:

- **Hoje**, o SbD-ToE permite construir e operar o software de um sistema de IA com segurança por desenho.
- **Amanhã**, quando a organização tiver de cumprir o AI Act, liga os detalhes - estende o threat model ao vetor adversarial (ATLAS), formaliza o QMS (Art. 17), parametriza incidentes (Art. 73) e a monitorização pós-mercado (Art. 72), e articula com as equipas de domínio as dimensões de dados, supervisão e transparência.

### Âmbito, papéis e sanções

O AI Act distingue **fornecedores (providers)**, **utilizadores implementadores (deployers)**, importadores e distribuidores, com obrigações distintas. O grosso das obrigações técnicas (e da cobertura SbD-ToE) recai sobre o **fornecedor de sistema de alto risco**; o *deployer* tem obrigações próprias (uso conforme às instruções, supervisão humana, em certos casos FRIA - Art. 26, 27).

Em termos sancionatórios (Art. 99), o regulamento estabelece patamares máximos:

- **Práticas proibidas (Art. 5)**: até **35 M€** ou **7%** do volume de negócios anual mundial (o que for mais elevado).
- **Incumprimento de outras obrigações** (incluindo as do fornecedor de alto risco, Art. 16): até **15 M€** ou **3%**.
- **Informação incorreta, incompleta ou enganosa** a organismos notificados ou autoridades: até **7,5 M€** ou **1%**.
- Para fornecedores de **GPAI** (Art. 101): até **15 M€** ou **3%**.

### Referências

- **AI Act**: Regulamento (UE) 2024/1689 (CELEX: [32024R1689](https://eur-lex.europa.eu/legal-content/PT/TXT/?uri=CELEX:32024R1689)).
- **Art. 9** - Sistema de gestão de risco (ciclo de vida).
- **Art. 10** - Dados e governação de dados (representatividade, enviesamento).
- **Art. 11 e Anexo IV** - Documentação técnica.
- **Art. 12 / Art. 19** - Registo de eventos e conservação de logs.
- **Art. 13 / Art. 14** - Transparência aos deployers e supervisão humana.
- **Art. 15** - Exatidão, robustez e cibersegurança (resiliência a ataques adversariais).
- **Art. 17** - Sistema de gestão da qualidade.
- **Art. 72 / Art. 73** - Monitorização pós-comercialização e incidentes graves.
- **Art. 53 / Art. 55** - Obrigações GPAI e GPAI com risco sistémico.
- **Art. 99 / Art. 101** - Regime sancionatório.
- **ISO/IEC 42001** - Sistema de gestão de inteligência artificial.
- **ISO/IEC 23894** - Gestão de risco de IA.
- **ISO/IEC 27090** (em desenvolvimento) - Cibersegurança de IA.
- **NIST AI Risk Management Framework (AI RMF 1.0)**.
- **MITRE ATLAS** - Adversarial Threat Landscape for Artificial-Intelligence Systems.
- **OWASP Machine Learning Security Top 10** e **OWASP Top 10 for LLM Applications**.

---

:::note Exceções e evidência de controlo

O AI Act, tal como NIS2 e DORA, beneficia de um processo formal de exceções à conformidade. Casos em que um requisito não é aplicável, ou em que se aceita um risco residual temporário (p. ex., um vetor adversarial mitigado por compensação enquanto se prepara o *retraining*), devem ser documentados, aprovados ao nível adequado e revistos periodicamente.

O Cap. 14 (Governança e Contratação) do SbD-ToE fornece os artefactos necessários: registo de exceções, critérios de aceitação de risco, cadeia de aprovação e plano de remediação. Note-se que certos desvios **não são exceptuáveis** no contexto AI Act - desde logo, qualquer uso que recaia nas práticas proibidas do Art. 5. A existência de um processo formal de exceções não é sinal de fragilidade: é evidência de governação madura e de controlo consciente sobre o perfil de risco.

:::

---

**Versão:** 1.0
**Data:** Maio 2026
**Próxima revisão:** Novembro 2026
