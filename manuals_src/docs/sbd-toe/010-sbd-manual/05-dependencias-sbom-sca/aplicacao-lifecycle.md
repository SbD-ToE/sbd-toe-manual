---
id: aplicacao-lifecycle
title: Como Fazer
description: Integração prática das prescrições de gestão de dependências, geração de SBOM e execução de SCA ao longo do ciclo de vida da aplicação
tags: [tipo:aplicacao, ciclo-vida, dependencias, sbom, sca, supply-chain, governance]
genia: us-format-normalization
---

# Aplicação no Ciclo de Vida - Dependências, SBOM e SCA

## 🧭 Quando aplicar

As práticas acompanham a aplicação desde o arranque até ao *post‑release*.  
Cada evento é um **trigger** que deve produzir evidências objetivas.

| Fase SDLC / Evento | Ação esperada | Artefacto/Evidência |
|--------------------|---------------|---------------------|
| Início de projeto  | Publicar política e configurar repositórios internos | Documento de política + `repo-config.yaml` |
| Nova dependência   | Rever origem, licença, manutenção e CVEs | Ticket de aprovação + registo |
| Build / CI         | Gerar SBOM e executar SCA com *gates* | `sbom.*` + `sca-report.*` + logs |
| Release            | Rever findings/exceções e decidir *go/no-go* | `releases.md` + `excecoes.yaml` |
| Ciclo regular      | **Bots** abrem PRs de atualização com **avaliação de impacto** | PRs automáticos + testes/logs |
| CVE crítico público| Análise de impacto + *backport/fix* | Issue de resposta + plano de mitigação |

---

## 👥 Quem executa cada ação

A governação é **coletiva** - papéis e responsabilidades consistentes com o intro.md.

| Papel | Responsabilidade |
|------|-------------------|
| **Developer / Lead** | Incluir dependências, triagem inicial, *pinning*, correções |
| **AppSec Engineer** | Políticas, *tuning* de *gates*, gestão de exceções e risco |
| **DevOps / CI/CD** | SBOM, SCA, repositórios internos, bots de atualização e *impact analysis* |
| **QA** | Evidências, testes de regressão, validação de PRs de bots |
| **Product Owner** | Decisão *go/no-go* e aceitação de risco residual |
| **GRC / Gestão** | Auditoria, conformidade, retenção de evidências |

---

## 📖 User Stories Reutilizáveis

Cada US transforma a prescrição em backlog acionável, com **contexto, rationale científico, BDD/checklist, artefactos, proporcionalidade L1–L3 e integração no SDLC**.

---

### US-01 - Gestão de dependências seguras

**Contexto.**  
Dependências externas sem validação introduzem risco invisível (componentes abandonados, origem duvidosa, licenças incompatíveis).

:::userstory
**História.**   
Como **Developer**, quero **usar apenas dependências aprovadas**, para **reduzir risco de vulnerabilidades herdadas e conflitos de licença**.

**Critérios de aceitação (BDD).**
- **Dado** que pretendo incluir uma dependência
  **Quando** submeto pedido de aprovação
  **Então** a dependência é validada segundo a política (origem, licença, manutenção, CVEs)

**Checklist.**
- [ ] Dependência aprovada formalmente  
- [ ] Licença validada / compatível  
- [ ] Sem CVEs críticos conhecidos  
- [ ] Proveniência confirmada (repositório interno)

:::

**Artefactos & evidências.**
- `dependencies-approval.md`  
- Ticket de validação no backlog

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Aprovação simplificada |
| L2 | Sim | Validação formal + licença |
| L3 | Sim | Revisão AppSec + proveniência

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Design/Dev | Inclusão de dependência | Developer + AppSec | Na aprovação da dependência |

**Ligações úteis.**  
- [Pilares de governação](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro#pilares-de-governação)

---

### US-02 - SBOM em cada build

**Contexto.**  
Sem SBOM atualizado não é possível determinar rapidamente exposição a CVEs e cumprir requisitos de auditoria.

:::userstory
**História.**   
Como **DevOps / SRE**, quero **gerar SBOM em cada build**, para **rastreabilidade completa de componentes**.

**Critérios de aceitação (BDD).**
- **Dado** que um build é acionado
  **Quando** o artefacto é produzido
  **Então** é gerado um SBOM em formato CycloneDX ou SPDX

- **Dado** um SBOM gerado
- **Quando** é associado à release
- **Então** é armazenado e acessível para auditoria

**Checklist.**
- [ ] SBOM no formato CycloneDX ou SPDX  
- [ ] SBOM versionado e associado à release  
- [ ] Acessível para auditoria

:::

**Artefactos & evidências.**
- `sbom.json` / `sbom.xml`

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Sim | SBOM básico |
| L2 | Sim | SBOM completo, incluído na release |
| L3 | Sim | SBOM assinado + verificação de integridade

**Integração no SDLC.**
| Fase | Trigger | Responsável |
|---|---|---|
| CI | Execução de build | DevOps

**Ligações úteis.**  
- [SBOM - Normas CycloneDX e SPDX](https://www.cyclonedx.org)
- [US-10 - Inventário e SBOM por Build](#us-10---inventário-e-sbom-por-build)

---

### US-03 - SCA automático com *gates*

**Contexto.**  
SCA identifica vulnerabilidades conhecidas em dependências (diretas e transitivas) e deve bloquear risco inaceitável.

:::userstory
**História.**   
Como **AppSec Engineer**, quero **executar SCA automático nos pipelines**, para **detetar CVEs antes de produção**.

**Critérios de aceitação (BDD).**
- **Dado** um build
  **Quando** o SBOM é gerado
  **Então** o SCA corre e **bloqueia** findings que excedam o threshold por Lx

**Checklist.**
- [ ] Scanner SCA integrado (ex.: Dependency‑Check/Trivy/Grype)  
- [ ] Findings documentados e triados  
- [ ] Bloqueio automático para CVEs críticos (L2) e médios+ (L3)

:::

**Artefactos & evidências.**
- `sca-report.html` / JSON
- Logs de pipeline com *gates*

**Proporcionalidade por risco.**
| Nível | Política |
|---|---|
| L1 | Alerta |
| L2 | Bloqueio High/Critical |
| L3 | Bloqueio Medium+

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| CI | Geração de SBOM | DevOps + AppSec | Durante o build (bloqueio imediato) |

**Ligações úteis.**  
- [Guia de thresholds por L1–L3](/sbd-toe/sbd-manual/dependencias-sbom-sca/aplicacao-lifecycle#matriz-de-proporcionalidade-l1l3)

---

### US-04 - Exceções a CVEs formais e temporárias

**Contexto.**  
Nem todos os findings podem ser resolvidos de imediato; exceções devem ser **formais, justificadas e temporárias**.

:::userstory
**História.**   
Como **AppSec Engineer**, quero **formalizar exceções a CVEs**, para **manter governação e justificar risco residual**.

**Critérios de aceitação (BDD).**
- **Dado** que existe um CVE não resolvido
  **Quando** é solicitada uma exceção
  **Então** a exceção é formalizada em `excecoes.yaml` com justificativa técnica e de negócio, aprovador e prazo

- **Dado** uma exceção com prazo definido
- **Quando** passa o prazo
- **Então** é acionada revisão periódica com reavaliação do risco

**Checklist.**
- [ ] `excecoes.yaml` com justificativa técnica e de negócio  
- [ ] Aprovador e prazo definidos  
- [ ] Controlo compensatório especificado  
- [ ] Revisão periódica agendada

:::

**Artefactos & evidências.**
- `excecoes.yaml` (versionado)
- Aprovação registada no backlog

> **Referência:** Este US implementa [Cap 14-US-01: Processo formal de exceções]
> no contexto de vulnerabilidades em dependências (CVEs). O processo de aprovação, TTL e revalidação devem seguir a política master de exceções em Cap 14.

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Justificação simples |
| L2 | Sim | Revisão periódica (30–90 dias) |
| L3 | Sim | Validação executiva + métricas de risco

**Integração no SDLC.**
| Fase | Trigger | Responsável |
|---|---|---|
| Release | Findings pendentes | AppSec + Product Owner

**Ligações úteis.**  
- [Exceções e Aceitação de Risco em Vulnerabilidades](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/excecoes-e-aceitacao-risco)

---

### US-05 - Validação de release (*go/no-go*)

**Contexto.**  
Cada release é uma decisão de risco que deve ser **explícita e rastreável**.

:::userstory
**História.**   
Como **Product Owner**, quero **validar findings e exceções antes do go‑live**, para **tomar decisão informada de *go/no-go***.

**Critérios de aceitação (BDD).**
- **Dado** uma release candidata
  **Quando** verifico critérios de segurança e risco residual
  **Então** documento a decisão e condicionantes (se existirem)

**Checklist.**
- [ ] Lista de findings e estado  
- [ ] Exceções aprovadas e válidas  
- [ ] Decisão *go/no-go* documentada

:::

**Artefactos & evidências.**
- `releases.md` com histórico e justificações

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Decisão simples |
| L2 | Sim | Revisão formal |
| L3 | Sim | Revisão formal + AppSec envolvido

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Pré‑release | RC pronta | Product Owner + QA + AppSec | Antes do deploy a produção |

**Ligações úteis.**  
<!-- genia_suggest: Criar addon/10-checklist-release-segura.md com checklist de validação de release por L1-L3 -->
- [Artefactos esperados](/sbd-toe/sbd-manual/dependencias-sbom-sca/aplicacao-lifecycle#-artefactos-esperados)

---

### US-06 - Repositórios internos como fonte única

**Contexto.**  
Sem repositórios internos, dependências podem ser resolvidas de fontes não controladas (*typosquatting*, *confusion*, malícia).

:::userstory
**História.**   
Como **DevOps / SRE**, quero ***enforce* repositórios internos aprovados**, para **garantir proveniência e consistência**.

**Critérios de aceitação (BDD).**
- **Dado** que o *package manager* resolve dependências
  **Quando** a build ocorre
  **Então** só aceita fontes do repositório interno aprovado

**Checklist.**
- [ ] `repo-config.yaml` ativo (proxy/registry interno)  
- [ ] Bloqueio a fontes externas (allowlist)  
- [ ] Logs de acesso monitorizados e retidos

:::

**Artefactos & evidências.**
- `repo-config.yaml`  
- Logs de CI/CD com origem validada

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Recomendado |
| L2 | Sim | Obrigatório |
| L3 | Sim | Obrigatório + assinatura/verificação de pacotes

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Build | Resolução de dependências | DevOps/CI | Imediato (bloqueio em tempo real) |

**Ligações úteis.**  
- SLSA Provenance (conceitos)

---

### US-07 - Proibir bibliotecas copiadas manualmente

**Contexto.**  
JS, PHP, DLLs, JARs copiados diretamente para o repo escapam ao SBOM e ao SCA, criando *shadow dependencies*.

:::userstory
**História.**   
Como **Developer**, quero **usar apenas *package managers*/repositórios internos**, **nunca** copiar bibliotecas para o repo.

**Critérios de aceitação (BDD).**
- **Dado** que preciso de uma biblioteca externa
  **Quando** a adiciono ao projeto
  **Então** é gerida via *package manager* e **não** por cópia manual

**Checklist.**
- [ ] Zero libs copiadas manualmente  
- [ ] Todas via *package manager*  
- [ ] Auditoria periódica confirma ausência

:::

**Artefactos & evidências.**
- `package.json` / `pom.xml` / `composer.json`  
- Logs de build (resolução via repos internos)

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Sim | Política documentada |
| L2 | Sim | Auditorias periódicas |
| L3 | Sim | Enforcement automático em CI/CD

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Dev | Inclusão de nova lib | Developer + AppSec | Na aprovação da dependência |

**Ligações úteis.**  
<!-- genia_suggest: Criar addon/11-bibliotecas-locais-migracao.md com padrões de migração por stack (npm, maven, composer, etc) -->
- [Governança de Bibliotecas de Terceiros](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/governanca-libs-terceiros)

---

### US-08 - Automação da atualização com avaliação de impacto

**Contexto.**  
Dependências degradam com o tempo; é necessário atualizar **com segurança e rapidez**.  
Ferramentas modernas avaliam **impacto** (semver, *release notes*, *diffs*, cobertura de testes) e:
- **abrem PRs automáticos** com *auto‑merge* quando a alteração é segura (*patch/minor* sem impacto, testes verdes, *gates* OK);
- **marcam como requires‑human** quando há impacto (API quebrada, *major*), anexando *guidelines* de *refactor*.

:::userstory
**História.**   
Como **DevOps/Developer**, quero **bots de atualização com avaliação de impacto**, para **receber PRs seguros automaticamente e *handoff* humano quando necessário**.

**Critérios de aceitação (BDD).**
- **Dado** que é publicada nova versão
  **Quando** o bot executa **impact analysis**
- Então:
  - Se **no‑impact** ⇒ PR com **auto‑merge** condicionado a CI verde e *gates* ok  
  - Se **impact** ⇒ PR **requires‑human** com *diff*, *breaking notes*, *refactor hints*, ou mesmo *GenAI com a alteração* adequada.

**Checklist.**
- [ ] Bot ativo (Renovate/Dependabot/afins)  
- [ ] **Impact analysis** configurado (semver + testes + changelog)  
- [ ] Critérios de **auto‑merge seguro** por L1–L3  
- [ ] Etiquetas (`no-impact`, `requires-human`) e *routing* para revisores  
- [ ] *Canary/rollout* definido (L3)

:::

**Artefactos & evidências.**
- PRs automáticos com labels e logs  
- Relatórios de testes e *gates* do CI/CD

**Proporcionalidade por risco.**
| Nível | Política |
|---|---|
| L1 | Bots opcionais; *auto‑PR* para *patch/minor* |
| L2 | Bots obrigatórios; *auto‑merge* para *patch* com CI verde |
| L3 | Bots obrigatórios; *impact analysis* + *canary*; *auto‑merge* apenas *patch*; *minor/major* requer aprovação humana e promoção por estágios |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Dev/CI | Nova versão publicada | DevOps + Developer + QA | Automático (PR aberto e processado por bot) |

**Ligações úteis.**  
- [Política de Atualizações Automáticas](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/politica-atualizacoes)
- [Integração CI/CD](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/integracao-ci-cd)

---

### US-09 - Auditoria Periódica de Bibliotecas Copiadas Manualmente

**Contexto.**  
Bibliotecas copiadas manualmente escapam ao SBOM e ao SCA. É necessário **automação periódica** para detetar estas dependências ocultas e ***enforce* substituição** via package manager ou bloqueio em CI/CD.

:::userstory
**História.**   
Como **AppSec Engineer**, quero **executar auditoria periódica automatizada** para detetar bibliotecas copiadas manualmente (JS, PHP, DLL, JAR, etc.), para **bloquear a sua utilização em CI/CD e garantir SBOM e SCA completos**.

**Critérios de aceitação (BDD).**
- **Dado** que é executada auditoria periódica (semanal/mensal conforme Lx)
  **Quando** encontradas bibliotecas copiadas não via package manager
  **Então** é criada issue no backlog com prazo de substituição via repositório/package manager

**Checklist.**
- [ ] Scanner automático configurado (ex: busca de padrões de libs copiadas, extensões JS/PHP/DLL/JAR)
- [ ] Frequência de auditoria definida por Lx (L1: mensal, L2: quinzenal, L3: semanal)
- [ ] Resultados versionados no repositório (`.audit-libs.json`)
- [ ] Bloqueio em CI/CD para L2–L3 quando detectadas libs copiadas
- [ ] Zero libs detectadas como meta

:::

**Artefactos & evidências.**
- `.audit-libs.json` / `.audit-libs.yaml` (versionado)
- Logs de auditoria e scanner
- Issues de correção no backlog

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Sim | Política documentada; auditoria manual mensal |
| L2 | Sim | Scanner automático quinzenal; alerta em pipeline |
| L3 | Sim | Scanner automático semanal; bloqueio em CI/CD |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Ciclo regular | Auditoria periódica (cronograma) | AppSec Engineer + DevOps | L1: mensal, L2: quinzenal, L3: semanal |
| Build | Detecção em CI/CD (L2–L3) | DevOps (bloqueio) | Imediato (bloqueio em tempo real) |
| Backlog | Libs detectadas | Developer (remediação)

**Ligações úteis.**  
- [US-07 - Proibir bibliotecas copiadas manualmente](#us-07---proibir-bibliotecas-copiadas-manualmente)
<!-- genia_suggest: Criar addon/12-padroes-deteccao-libs.md com padrões regex e ferramentas por stack (npm, Python, Java, PHP, etc) -->
- [Governança de Bibliotecas de Terceiros](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/governanca-libs-terceiros)

---

### US-10 - Inventário e SBOM por Build

**Contexto.**  
Cada build deve produzir uma **Software Bill of Materials (SBOM)** assinada e rastreável, identificando todas as dependências utilizadas (diretas e transitivas).  
Esta SBOM deve poder ser **correlacionada com o artefacto implantado** e servir de base à deteção de desvios (“drift”) entre o que foi construído e o que está efetivamente a executar.

:::userstory
**História.**  
Como **DevOps / SRE**, quero gerar automaticamente um **SBOM assinado por build**, que se mantenha associado a cada imagem, pacote ou artefacto implantado, permitindo identificar todos os componentes e as suas versões.

**Critérios de aceitação (BDD).**
- **Dado** um pipeline de build  
  **Quando** o artefacto é produzido  
  **Então** é gerado um **SBOM CycloneDX ou SPDX** assinado e arquivado com metadados de commit, versão e hash.  
  
- **Dado** um SBOM assinado no build  
  **Quando** o serviço é implantado em `stage` ou `prod`  
  **Então** o orquestrador mantém **etiquetas de proveniência** (commit, build-id, imagem) que associam cada instância ao SBOM correto. 

- **Dado** telemetria de runtime  
  **Quando** é detetado um componente carregado que não existe no SBOM  
  **Então** é aberto **incidente de drift** com correção requerida.  

- **Dado** um pedido de auditoria ou compliance  
  **Quando** o auditor solicita o inventário de componentes  
  **Então** é possível exportar a SBOM e proveniência por versão.

**Checklist.**
- [ ] SBOM gerado por build (standard SPDX ou CycloneDX).  
- [ ] Assinatura e armazenamento seguro do SBOM.  
- [ ] Proveniência do deploy (attestations e labels por ambiente).  
- [ ] Comparação runtime vs SBOM e deteção de drift.  
- [ ] Exportação de inventário para CMDB ou data-lake de compliance.  
- [ ] Integração com alertas de vulnerabilidade e com Cap. 12 (Monitorização & Operação Segura).

:::

**Artefactos & evidências.**  
`sbom-<build>.json`, `attestation-<build>.json`, `proveniencia-<deploy>.json`, relatórios de drift e logs de build.

**Proporcionalidade.**
| Nível | Obrigatório? | Cobertura |
|---|---:|---|
| L1 | Sim | SBOM por build e associação básica por imagem. |
| L2 | Sim | Attestations + labels por ambiente, deteção de drift básica. |
| L3 | Sim | Drift contínuo + bloqueio de execuções não atestadas. |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| CI | Execução de build | DevOps / SRE | No build (geração automática) |
| Deploy | Implantação em ambiente | DevOps / SRE | Imediato (associação com metadados) |
| Operação | Monitorização contínua | DevOps + AppSec | Contínuo (deteção de drift) |

**Ligações úteis.**
- [SLSA Provenance - Conceitos e Implementação](https://slsa.dev)
- [Inventário e SBOM](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/inventario-sbom)
- [US-11 - Alertas sobre Vulnerabilidades](#us-11---alertas-sobre-vulnerabilidades-em-componentes-usados)

---

### US-11 - Alertas sobre Vulnerabilidades em Componentes Usados

**Contexto.**  
Os sistemas devem **detetar automaticamente vulnerabilidades conhecidas (CVEs)** nas dependências utilizadas.  
Além dos alertas durante o build, devem existir **alertas em produção**, correlacionando as versões efetivamente implantadas e os ambientes onde se encontram.  
O sistema deve conhecer **onde corre cada versão** para avaliar impacto real e priorizar correção.

:::userstory
**História.**  
Como **Gestor de Aplicação** e **AppSec**, quero **receber alertas correlacionados por ambiente** quando surgir uma CVE que afete versões em execução, para priorizar a correção e reduzir o MTTR.

**Critérios de aceitação (BDD).**
- **Dado** um inventário por serviço/ambiente com SBOM associado  
  **Quando** é publicada uma CVE que afeta uma versão implantada  
  **Então** é gerado um **alerta único** com componente, versão, serviços/ambientes impactados, *exploitability*, exposição e SLA recomendado.  
- **Dado** um alerta com SLA L2/L3  
  **Quando** passa o tempo de triagem sem ação  
  **Então** é **escalado automaticamente** (Cap. 12) e criado incidente no sistema de ITSM.  
- **Dado** uma exceção de risco aceite (VEX/justificativa)  
  **Quando** passa a existir *exploit ativo*  
  **Então** a exceção é reavaliada e o alerta reativado.  
- **Dado** o ciclo de vida de patch management  
  **Quando** a correção é implantada  
  **Então** o alerta é fechado automaticamente e registado como *resolved CVE*.  

**Checklist.**
- [ ] Inventário contínuo por serviço e ambiente com SBOM associado.  
- [ ] Correlação de CVEs e advisories para versões implantadas.  
- [ ] Enriquecimento de risco (exploit disponível, exposição, dados sensíveis).  
- [ ] Integração com Cap. 12 (SIEM/SOAR/alerting) e ITSM (incidentes/tarefas).  
- [ ] Processo de exceções com VEX e reavaliação automática.  
- [ ] KPIs: MTTA/MTTR por severidade e ambiente; % cobertura inventário vs deploys.

:::

**Artefactos & evidências.**  
`sbom-<build>.json` assinado; `inventario-runtime-<servico>-<ambiente>.json`; feed de CVEs correlacionadas; tickets/incidentes; decisões VEX.

**Proporcionalidade.**
| Nível | Obrigatório? | SLA triagem | SLA mitigação | Ajustes |
|---|---:|---:|---:|---|
| L1 | Sim | 5 dias úteis | 30 dias | Alertar apenas *high/critical* implantadas sem compensações. |
| L2 | Sim | 2 dias úteis | 14 dias | Incluir *medium* em serviços expostos; escalonamento automático. |
| L3 | Sim | 1 dia útil | 7 dias | *Blockers* com auto-rollback/kill-switch quando aplicável. |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Publicação CVE | Nova vulnerabilidade pública | Automático (feed) | Detecção automática (1–6h) |
| Triagem | CVE correlacionada com versão implantada | AppSec + DevOps | L1: 5d, L2: 2d, L3: 1d |
| Mitigação | Plano de correção ou exceção | DevOps + AppSec | L1: 30d, L2: 14d, L3: 7d |

**Ligações úteis.**
- [US-02 - SBOM em cada build](#us-02---sbom-em-cada-build)
- [US-10 - Inventário e SBOM por Build](#us-10---inventário-e-sbom-por-build)
- [Cap. 12 - Monitorização & Operação Segura](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle)


---

### US-12 - Validação Automática de Compatibilidade de Licenças

**Contexto.**  
Dependências com licenças incompatíveis (GPL, AGPL, etc.) podem introduzir obrigações legais inesperadas. É necessário **validar automaticamente a compatibilidade** contra lista branca organizacional.

:::userstory
**História.**   
Como **Developer**, quero **validar automaticamente a compatibilidade de licenças** de novas dependências, para **garantir conformidade legal e evitar conflitos**.

**Critérios de aceitação (BDD).**
- **Dado** que é adicionada nova dependência
  **Quando** o build executa
  **Então** validador de licenças avalia compatibilidade contra lista branca organizacional

- **Dado** que uma licença é incompatível
- **Quando** o build tenta resolver a dependência
- **Então** o pipeline bloqueia com mensagem clara (L2–L3) ou avisa (L1)

**Checklist.**
- [ ] Lista branca de licenças aprovadas definida (ex: MIT, Apache 2.0, BSD)
- [ ] Validador automático de licenças integrado no CI/CD
- [ ] Bloqueio para licenças proibidas/incompatíveis (L2–L3)
- [ ] Alerta para licenças não reconhecidas (para revisão manual)
- [ ] Documentação do critério de aprovação por licença

:::

**Artefactos & evidências.**
- `licenses-whitelist.yaml` / `.licenseignore` (versionado)
- Logs de CI/CD com validação de licenças
- Issues de remediação (trocar dependência ou requerer exceção formal)

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Validação manual, ad hoc |
| L2 | Sim | Automática com alerta; bloqueio para GPL/AGPL |
| L3 | Sim | Automática com bloqueio; exceções requerem aprovação formal |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Design/Dev | Inclusão de dependência | Developer | Na aprovação da dependência |
| Build | Resolução de dependências | CI/CD (bloqueio/alerta) | Durante o build (imediato) |
| Exceção | Licença incompatível com business case | AppSec + Legal (se necessário) | Antes do go-live |

**Ligações úteis.**  
- [US-01 - Gestão de dependências seguras](#us-01---gestão-de-dependências-seguras)
- [SPDX License List](https://spdx.org/licenses/)

---

### US-13 - Inventário e controlo de dependências emergentes

**Contexto.**  
Em arquiteturas modernas, nem todas as dependências entram por declaração explícita em manifests ou lockfiles. Ferramentas de build, pipelines, code generation, plugins e carregamento em runtime podem introduzir **dependências emergentes** que não são imediatamente visíveis.

:::userstory
**História.**  
Como **Arquitetos de Software + AppSec Engineer**, quero identificar e controlar dependências emergentes (não explicitamente declaradas), para garantir que a composição real do software permanece governada, rastreável e alinhada com os requisitos de segurança.

**Critérios de aceitação (BDD).**
- **Dado** que um SBOM é gerado para a aplicação ou pipeline  
  **Quando** comparo a composição atual com a baseline conhecida  
  **Então** consigo identificar dependências novas, inesperadas ou fora da fronteira definida

**Checklist.**
- [ ] Fronteira de inventário (SBOM boundary) definida e documentada
- [ ] Fontes de dependência identificadas (build tools, plugins, pipelines, runtime fetch)
- [ ] Baseline de dependências aprovada e versionada
- [ ] Deteção de *delta* de dependências implementada
- [ ] Dependências emergentes sujeitas a revisão/aprovação
- [ ] Evidência arquivada por release

:::

**Artefactos & evidências.**
- `sbom-boundary.md`
- `sbom-baseline.json`
- Relatório de *delta* de dependências por build/release

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Análise manual pontual |
| L2 | Sim | Deteção automática de *delta* |
| L3 | Sim | *Gate* automático + aprovação formal |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| CI/CD | Build / Release | DevOps + AppSec | Em cada release |

**Ligações úteis.**
- 🔗 Cap. 04 - Arquitetura Segura: `/sbd-manual/arquitetura-segura/intro`
- 🔗 Cap. 07 - CI/CD Seguro: `/sbd-manual/cicd-seguro/intro`

---

### US-14 - AI BOM e gestão de *providers* de modelos AI {#us-14}

**Contexto.**
A US-10 cobre SBOM clássico — pacotes via *package manager*, dependências directas e transitivas. Quando o sistema inclui **componentes AI** (modelos, datasets, MCP servers/tools, prompts embebidos), há uma classe de "dependências" que escapa ao *package manager* tradicional: artefactos opacos com versão própria, *providers* externos (Anthropic, OpenAI, HuggingFace), e mecanismos de actualização que podem mudar comportamento sem mudar versão visível. Operacionalizamos [`DEP-011`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-011), [`DEP-012`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-012), [`DEP-013`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-013) e [`DEP-014`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-014) para que essas dependências fiquem tão auditáveis como o resto do *stack*.

:::userstory
**História.**
Como **AppSec / DevOps**, quero que cada *release* do sistema gere um **AI BOM em formato standardizado** (preferencialmente CycloneDX 1.6 `ml-bom`) com modelos, datasets, MCP servers/tools e prompts embebidos *pinned* a versões específicas, alinhado com a lista de *providers* aprovados, para garantir rastreabilidade equivalente à do SBOM clássico e detecção rápida de incidentes *upstream* em qualquer das classes.

**Critérios de aceitação (BDD).**
- **Dado** um *build* de sistema com componentes AI
  **Quando** o pipeline gera o SBOM
  **Então** é também gerado o **AI BOM** em formato `ml-bom` (CycloneDX 1.6) ou equivalente, integrado com o SBOM principal
- **Dado** um modelo AI em uso operacional
  **Quando** declarado no AI BOM
  **Então** vem **com versão fixa explícita** (ex.: `claude-opus-4-7@sha:…`) — sem `latest`, sem ranges, sem aliases dinâmicos
- **Dado** que um *provider* AI muda versão maior do modelo
  **Quando** o *pinning* é actualizado
  **Então** corre nova *eval suite* (Cap. 10 §C5) e *threat model* é revisto (Cap. 03 US-11) antes do *cutover*
- **Dado** que um *provider* AI **não** está na lista aprovada
  **Quando** se tenta usar em código de produção
  **Então** o *gate* de CI bloqueia (cross-link Cap. 07 US-19) ou exige excepção formal

**Checklist.**
- [ ] AI BOM gerado por *build* em formato standardizado (preferência: CycloneDX 1.6 `ml-bom`)
- [ ] Modelos, datasets, MCP servers/tools, prompts com versão *pinned* + hash + *provider*
- [ ] Lista de *providers* AI aprovados versionada em VCS, com classificação de risco
- [ ] Cláusulas contratuais aplicáveis registadas por *provider* (cross-link Cap. 14, Policy 33)
- [ ] *Gate* de CI que falha se: (a) AI BOM não foi gerado, (b) componente usa `latest`/range, (c) *provider* não está na lista aprovada
- [ ] Processo de triagem `DEP-007` estendido a incidentes em modelos/datasets/MCP/prompts (`AML.T0010`, `AML.T0019`, `AML.T0109`, `AML.T0110`, LLM03-2025)
- [ ] *Eval suite* + *threat model* corridos em cada mudança de versão maior

**Artefactos & evidências.**
- `ai-bom.cdx.json` (CycloneDX 1.6) ou equivalente por *release*, arquivado e ligado ao SBOM principal
- Lista de *providers* aprovados em VCS (`governance/ai-providers.yaml` ou equivalente)
- *Logs* do *gate* CI a confirmar conformidade do AI BOM
- Registo de eval/threat-review por mudança de versão (referencia `eval_run_id` e `threat_model_ref`)
- Histórico de versões pinned por modelo, com data e SHA

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Recomendado | AI BOM em formato simples; lista de providers conhecida |
| L2 | Sim | AI BOM em formato standard; *providers* aprovados; *gate* de CI |
| L3 | Sim | AI BOM standard + revisão GRC dos *providers*; cláusulas contratuais detalhadas (data retention, audit rights, localização); cross-link com cross-check AI Act |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Build | Cada *build* | DevOps (gera AI BOM) + AppSec (revê) | Por *build* |
| Aprovação de provider | Adição de novo *provider* AI | AppSec + GRC (+ Legal se necessário) | Antes do uso operacional |
| Mudança de versão | *Bump* de modelo / MCP server / dataset | AppSec + DevOps | Antes do *cutover* — com *eval* e *threat review* concluídos |

**Ligações úteis.**
- 🔗 [`DEP-011..014` — Inventário e supply chain AI](./addon/catalogo-requisitos-dependencias#dep-011)
- 🔗 [Policy 39 — AI BOM e Supply Chain](/sbd-toe/assets/policies/policy-ai-bom-supply-chain)
- 🔗 [Policy 10 — Dependências (anexo provedores AI)](/sbd-toe/assets/policies/policy-dependencias)
- 🔗 [Policy 11 — SBOM (anexo AI BOM)](/sbd-toe/assets/policies/policy-sbom)
- 🔗 [Cap. 14 — Contratação de AI providers](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle)
- 🔗 [Cross-check AI Act](/sbd-toe/cross-check-normativo/ai-act/intro)

---

### US-15 - Pinning de versões e integridade por hash

Uma dependência sem versão fixa e sem hash verificável é uma porta aberta a substituição silenciosa na cadeia de fornecimento.  

**Contexto.** `DEP-003` exige *lockfile* versionado, sem referências `latest`/`*`/ranges não limitados, e integridade verificável por hash (`integrity` em npm, `--hash` em pip). Nenhuma US operacionaliza este controlo de forma direta — US-01 trata aprovação e US-13 trata *delta* de inventário, mas o *pinning* e a verificação de hash ficavam sem backlog próprio. Sem versão fixa, o mesmo manifesto resolve artefactos diferentes entre builds; sem hash, um artefacto adulterado *upstream* (typosquatting, *registry* comprometido) passa despercebido.  

:::userstory
**História.**   
Como **Developer/Lead**, quero **fixar todas as dependências a versões exactas e verificar a sua integridade por hash em cada resolução**, para **garantir builds reprodutíveis e bloquear substituição não autorizada de artefactos**.  

**Critérios de aceitação (BDD).**  
- **Dado** um manifesto de dependências  
  **Quando** o build resolve as dependências  
  **Então** existe um *lockfile* versionado em VCS sem `latest`/`*`/ranges não limitados, e o build falha se o *lockfile* estiver ausente ou desactualizado  
- **Dado** um *lockfile* com hashes de integridade  
  **Quando** o *package manager* descarrega um artefacto  
  **Então** o hash descarregado é comparado com o hash *pinned* e a resolução aborta em caso de divergência  

**Checklist.**  
- [ ] *Lockfile* presente e versionado, regenerado de forma determinística  
- [ ] Ausência de `latest`/`*`/ranges não limitados (verificável por *linter* em CI)  
- [ ] Campo de integridade por hash presente e validado na resolução  
- [ ] *Gate* de CI que falha perante *lockfile* ausente/desactualizado ou divergência de hash  

:::

**Artefactos & evidências.** `package-lock.json`/`poetry.lock`/`Gemfile.lock`/`go.sum` (versionado); relatório do *linter* de *pinning*; logs de CI com verificação de hash.  

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| *Lockfile* presente; *pinning* recomendado | *Lockfile* obrigatório + verificação de hash | *Lockfile* + hash + proveniência verificada (*attestation*) e *gate* bloqueante |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Dev | Inclusão/alteração de dependência | Developer/Lead | Na alteração do manifesto |
| Build | Resolução de dependências | DevOps/CI | Durante o build (bloqueio imediato) |

**Ligações úteis.** [DEP-003 — Versões fixas e auditáveis](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias)

---

### US-16 - Governação documentada de política de severidade, registries e registo de aprovação

Controlos de supply chain só são auditáveis quando a regra que distingue bloquear-de-alertar, a origem permitida e o registo de quem aprovou o quê estão escritos e versionados.  

**Contexto.** Três prescrições do catálogo ficavam só parcialmente operacionalizadas. `DEP-002` exige **política de severidade documentada** que distinga findings que bloqueiam dos que apenas alertam (US-03 aplica *gates* mas não exige a política escrita). `DEP-005` exige *allowlist* de *registries* enforced **com fallback para fontes externas controlado e auditado** (US-06 enforça a *allowlist* mas não trata o *fallback*). `DEP-006` exige registo de aprovação rastreável **com versão, hash, responsável e data** (US-01 aprova mas não fixa os campos do registo). Consolidam-se por serem todos artefactos de governação documentada que tornam os *gates* já existentes auditáveis.  

:::userstory
**História.**   
Como **AppSec Engineer**, quero **manter versionada a política de severidade, a *allowlist* de *registries* com regra de *fallback* auditada e o registo de aprovação com campos obrigatórios**, para **tornar as decisões de supply chain explícitas, rastreáveis e auditáveis**.  

**Critérios de aceitação (BDD).**  
- **Dado** o pipeline de SCA  
  **Quando** um finding é avaliado  
  **Então** a decisão bloquear-vs-alertar segue uma política de severidade documentada e versionada, e não critérios *ad hoc* do scanner  
- **Dado** que o build resolve dependências de uma fonte fora da *allowlist*  
  **Quando** ocorre *fallback* para um *registry* externo  
  **Então** o evento é registado, auditado e sujeito a aprovação conforme a política, ou bloqueado  
- **Dado** a aprovação de uma nova dependência  
  **Quando** é registada  
  **Então** o registo inclui versão, hash, responsável e data, e é rastreável por dependência  

**Checklist.**  
- [ ] Política de severidade documentada e versionada (limiares de bloqueio/alerta por Lx)  
- [ ] *Allowlist* de *registries* enforced com regra de *fallback* explícita e auditada  
- [ ] Registo de aprovação com versão, hash, responsável e data por dependência  
- [ ] Evidência de auditoria dos eventos de *fallback* (logs retidos)  

:::

**Artefactos & evidências.** `severity-policy.yaml`; `repo-config.yaml` com regra de *fallback*; `dependencies-approval.md` com campos versão/hash/responsável/data; logs de *fallback* auditados.  

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Política de severidade mínima documentada; *registries* recomendados; aprovação simples | Política versionada; *allowlist* enforced + *fallback* auditado; registo com campos obrigatórios | Idem + revisão AppSec/GRC do *fallback* e do registo; *fallback* requer aprovação formal por evento |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Início de projeto | Publicação/revisão de política | AppSec + GRC | Na adoção e em revisão periódica |
| Build | *Fallback* para *registry* externo | AppSec + DevOps | No evento (registo/auditoria imediatos) |
| Dev | Aprovação de nova dependência | AppSec + Developer | Na aprovação da dependência |

**Ligações úteis.** [DEP-002/005/006 — Catálogo de Requisitos](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias) · [Controlo de registos de origem](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/controle-registos-origem)

---

## 🧩 Nota complementar - Inventário contínuo de componentes e alertas em produção

A gestão de dependências não termina no build.  
Deve existir um **inventário contínuo de componentes de 3.ºs** por projeto e ambiente (dev/test/stage/prod), com **alertas automáticos** quando são publicadas vulnerabilidades que afetem versões implantadas.  

Isto complementa o SCA no pipeline ao:  
- Fechar o ciclo *build → deploy → run*;  
- Priorizar pelo risco real (exposição e exploitability);  
- Acionar resposta operacional via Cap. 12 (Monitorização & Operação Segura).

**Prática recomendada.**
1. Gerar SBOM no build e assinar.  
2. Etiquetar por ambiente no registo/orquestrador.  
3. Descoberta contínua em runtime (inventário por deploy) e comparação com SBOM.  
4. Correlação de CVEs e alertas quando: versão implantada afetada / exploit ativo / caminho crítico.  
5. Abertura automática de incidente/tarefa com SLA proporcional L1–L3.  
6. Evidência: SBOM, inventário, alertas, VEX, histórico de patching.

**Integração com Cap. 12 - Monitorização & Operação Segura.**

Os user stories 10 e 11 estão muito relacionados com o exposto no **Cap. 12 - Monitorização & Operação Segura.**, evidenciando o aspeto critico de monitorização além da execução de um qualquer pipeline de build. É fácil implementar medidas de segurança durante o build, mas, depois de entrar em produção uma aplicação pode estar um longo periodo de tempo sem voltar ao pipeline de desenvolvimento, é portanto essencial rever periodicamente, ou espontaneamente, o SBOM das aplicações em produção. É mais grave uma nova vulnerabilidade ser encontrada numa aplicação em produção do que durante o processo de desenvolvimento, principalmente sem medidas de alarmistica ou periodicas de deteção.
Ums dos aspetos fundamentais no  **Cap. 12 - Monitorização & Operação Segura.** é exatamente esse controlo, definindo:

- Eventos: criação/fecho de alerta, mudança de exploitability, violação de SLA, drift.  
- Métricas: MTTA, MTTR, ativos afetados, % exceções ativas, *patch latency*.  
- Automação: enriquecimento, priorização, escalonamento, playbooks SOAR.  
- Relato executivo: compliance Cap. 05 + Cap. 12, visão por L1–L3.

---
## 📦 Artefactos esperados

| Artefacto | Evidência |
|-----------|-----------|
| `dependencies-approval.md` | Lista aprovada de dependências |
| `sbom.json` / `sbom.xml` | Inventário por build (CycloneDX/SPDX) |
| `attestation-<build>.json` | Proveniência e assinatura do build |
| `inventario-runtime-<servico>-<ambiente>.json` | Inventário de componentes efetivamente implantados |
| `sca-report.html/json` | Vulnerabilidades detetadas e *gates* aplicados |
| `cve-alerts.json` | Alertas correlacionados por ambiente e severidade |
| `vex.yaml` | Exceções justificadas e estado de reavaliação |
| `excecoes.yaml` | Exceções formais aprovadas |
| `releases.md` | Decisões *go/no-go* e histórico de *patching* |
| `repo-config.yaml` | Repositórios internos configurados |
| `.audit-libs.json` / `.audit-libs.yaml` | Resultados de auditoria periódica de libs copiadas |
| `licenses-whitelist.yaml` | Lista branca de licenças aprovadas |
| **PRs de bots** | *Labels* de impacto, logs e testes |
| **Relatórios de drift** | Diferenças entre SBOM e runtime |
| **Tickets ITSM / Incidentes** | Evidência de tratamento de CVE e SLA cumprido |

---

## ⚖️ Matriz de proporcionalidade L1–L3 {#matriz-de-proporcionalidade-l1l3}

| Prática | L1 | L2 | L3 |
|---------|----|----|----|
| SBOM | Básico por build | Completo por release | Assinado + integridade + proveniência |
| Inventário runtime | Recomendado | Obrigatório | Contínuo + deteção de *drift* |
| SCA | Aviso | Bloqueio High/Critical | Bloqueio Medium+ + feed CVE ativo |
| Alertas CVE implantadas | Manual / ad hoc | Automático por ambiente | Automático + correlação e escalonamento |
| Pinning de versões | Recomendado | Obrigatório | Obrigatório + validação de proveniência |
| Exceções / VEX | Simples | Formais + revisão periódica | Formais + revalidação automática |
| Repositório interno | Recomendado | Obrigatório | Obrigatório + assinatura e *provenance attestation* |
| Bibliotecas copiadas | Proibidas (política) | Auditoria periódica | Enforcement CI/CD + bloqueio |
| Auditoria de libs copiadas | Política documentada; mensal | Scanner automático; quinzenal | Scanner automático; semanal + bloqueio CI/CD |
| Validação de licenças | Manual, ad hoc | Automática com alerta | Automática com bloqueio (exceto exceções formais) |
| Bots / automação de patching | Opcional | Ativos + *auto-merge patch* | Ativos + *impact analysis*, *canary* e rollback |
| Integração com Cap. 12 | Opcional | Alertas SIEM básicos | Total: SOAR, métricas MTTR/MTTA e escalonamento |

---

## 🏁 Recomendações finais

- **SBOM** deve ser tratado como documento vivo, com assinatura e proveniência verificável por build e por ambiente.  
- **Inventário contínuo** em produção é essencial: deteta *drift* e vulnerabilidades em versões efetivamente implantadas.  
- **SCA automatizado** com *gates* proporcionais ao risco e integração com alertas CVE em runtime.  
- **Repositórios internos** e *attestations* são a base da confiança na supply chain.  
- **Exceções formais e temporárias** (VEX) devem ser reavaliadas automaticamente quando muda o risco ou surge *exploit ativo*.  
- **Eliminar bibliotecas copiadas manualmente** (US-07) com **auditoria periódica automatizada** (US-09) e bloqueio em CI/CD para L2–L3.  
- **Validar compatibilidade de licenças** (US-12) contra lista branca, bloqueando ou alertando conforme criticidade.  
- **Bots com avaliação de impacto** (US-08):  
  - PRs de *patches triviais* → *auto-merge*;  
  - PRs com impacto → revisão humana, *canary* e promoção por estágios (sobretudo em L3).  
- **Integração com Cap. 12** deve garantir visibilidade total, alertas em tempo real e métricas operacionais de resposta (MTTA/MTTR) por severidade e ambiente.

