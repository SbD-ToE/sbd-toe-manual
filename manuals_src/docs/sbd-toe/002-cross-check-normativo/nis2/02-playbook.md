---
id: playbook
title: "SbD-ToE 4 NIS2: Playbook de Implementação"
description: Roadmap prático para usar SbD-ToE como base de implementação NIS2, com formalização regulatória adicional quando aplicável
tags: [playbook, nis2, implementacao, roadmap]
sidebar_position: 3
---

# SbD-ToE 4 NIS2: Playbook de Implementação

## Visão Geral {#visão-geral}

Este playbook mapeia **requisitos NIS2 (Diretiva UE 2022/2555) para ações SbD-ToE práticas**.

**Princípio:** Implementar SbD-ToE cria uma base forte para cumprir NIS2, mas a conformidade plena também exige formalização regulatória, responsabilização explícita da gestão e parametrização nacional ou setorial quando aplicável.

O que o Manual cobre, as lacunas que declara e o que fica fora de âmbito, obrigação a obrigação, estão em [Requisitos aplicáveis — O que este Manual cobre e o que fica de fora](./requisitos-aplicaveis#cobertura).

**Estrutura:** Cada seção mostra:
- NIS2 requisito (artigo)
- SbD-ToE capítulo/addon aplicável
- O que fazer (ação concreta)
- Evidência regulatória

Onde necessário, o texto distingue explicitamente:
- o que o manual base já sustenta bem
- e o que deve ser formalizado fora do manual para leitura regulatória completa

> 📚 **Recursos de Suporte:** Para templates práticos e exemplos de implementação, consultar [Exemplo-Playbook](/sbd-toe/cross-check-normativo/exemplo-playbook/exemplo-toolchain-options) com toolchains, KPIs, RACI e relatórios de incidentes reutilizáveis para NIS2 e outros frameworks.

---

## Mapa Rápido: NIS2 Art. → SbD-ToE {#mapa-rápido-nis2-art--sbd-toe}

| NIS2 Artigo | Requisito | Capítulo SbD-ToE | Ação Principal |
|----------|-----------|-----------------|----------------|
| **20** | Governação e Responsabilização | [Cap. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro), [Cap. 13](/sbd-toe/sbd-manual/formacao-onboarding/intro), [Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro) | Formalizar aprovação, supervisão e formação da gestão; usar o catálogo técnico como base de suporte |
| **21** | Medidas de Gestão de Risco | [Cap. 01](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro), [Cap. 02](/sbd-toe/sbd-manual/requisitos-seguranca/intro), [Cap. 03](/sbd-toe/sbd-manual/threat-modeling/intro), [Cap. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro), [Cap. 07](/sbd-toe/sbd-manual/cicd-seguro/intro), [Cap. 08](/sbd-toe/sbd-manual/iac-infraestrutura/intro), [Cap. 10](/sbd-toe/sbd-manual/testes-seguranca/intro), [Cap. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro), [Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro) | Implementar controlos técnicos, evidência e revisão contínua |
| **23** | Reporte de Incidentes | [Cap. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro), [Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro) | Deteção, escalonamento interno e preparação de reporte externo |
| **Cadeia Fornecimento** | Segurança de Fornecedores | [Cap. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro), [Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro) | SBOM, due diligence técnica e supplier governance complementar (`Art. 21(2)(d)`, `21(3)`, `22`) |
| **Continuidade** | Continuidade e Crise | [Cap. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro) | Runbooks e exercícios; cópias de segurança com restauro testado (OPS-016) e recuperação da aplicação (OPS-017) (`Art. 21(2)(c)`); BCM corporativo amplo fica fora |

---

## Como Implementar (Ordem Lógica) {#como-implementar-ordem-lógica}

### Fase 1: Governação (M0–M2) {#fase-1-governação-m0m2}
**NIS2 Art. 20** - Estabelecer responsabilização da gestão

1. **Criar Comissão de Cibersegurança**
   - Membros: Sponsor do órgão de gestão, CISO, CTO, GRC Manager, General Counsel
   - Frequência: Trimestral (mínimo)
   - **Evidência:** Ata de reuniões e decisões formais do órgão de gestão

2. **Aprovar Política de Gestão de Risco de Cibersegurança**
   - Referência principal: [Cap. 14 - Governança e Contratação](/sbd-toe/sbd-manual/governanca-contratacao/intro)
   - Base técnica de suporte: [Cap. 02 - Requisitos de Segurança](/sbd-toe/sbd-manual/requisitos-seguranca/intro)
   - **Aprovação:** Órgão de gestão ou cadeia formal equivalente prevista no modelo de governação aplicável
   - **Conteúdo:** Requisitos L1–L3, ciclo de vida, responsabilidades, medidas Art. 21 e modelo de supervisão

3. **Definir RACI**
   - Quem aprova o quê (aprovações formais e supervisão)
   - Escalations (quando elevar)
   - Referência: [Fundamentos - Papéis e responsabilidades](/sbd-toe/sbd-manual/fundamentos/roles-responsabilidades/intro)

4. **Estabelecer Programa de Formação para a Gestão**
   - Periodicidade: Anual (mínimo)
   - Conteúdo: Ameaças, requisitos NIS2, responsabilidades
   - **Evidência:** Presenças, materiais, avaliações
   - Referência: [Cap. 13 - Formação e Onboarding](/sbd-toe/sbd-manual/formacao-onboarding/intro)
   - **Estado no Manual:** a Política 37 prevê só «Awareness executivo» em L1; o programa para o órgão de direção é lacuna declarada, e cabe à organização formalizá-lo.

---

### Fase 2: Classificação e Inventário (M2–M4) {#fase-2-classificação-e-inventário-m2m4}
**NIS2 Art. 21** - Conhecer o que é crítico

1. **Inventariar Aplicações e Sistemas**
   - Nome, proprietário, dados processados, serviços suportados
   - Dependências (quem depende)
   - **Tipo de entidade:** Essencial / Importante (conforme NIS2 art. 3.º, com base nos setores dos Anexos I/II e na dimensão)
   - Referência: [Cap. 01 - Classificação de Aplicações](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)

2. **Classificar por Risco (L1–L3)**
   - Nível L1–L3 por aplicação, segundo os eixos de exposição, sensibilidade dos dados e impacto (CLA-001); o nível não corresponde às categorias essencial e importante da NIS2
   - O contexto NIS2 declara-se por entidade e aplica os seus pisos a todas as aplicações; nas entidades pertinentes do Reg. de Execução (UE) 2024/2690 aplicam-se também os pisos de grau PERTINENTE
   - Matriz assinada por CTO + Product leads + CISO

3. **Definir Requisitos Mínimos por Nível**
   - L1: base (autenticação, registos, revisão de código, SAST como gate — DEV-003 —, SCA com bloqueio de Critical e High — DEP-002)
   - L2: acrescenta threat modeling formal (THR-001), DAST (TST-005), centralização de logs e alertas automáticos (OPS-004, OPS-005)
   - L3: rigor e evidência reforçados; a seleção exata por nível está no catálogo
   - Referência: [Cap. 02 - Requisitos](/sbd-toe/sbd-manual/requisitos-seguranca/intro)

---

### Fase 3: Medidas de Gestão de Risco (M4–M8) {#fase-3-medidas-de-gestão-de-risco-m4m8}
**NIS2 Art. 21** - Implementar medidas técnicas e organizacionais

#### 3.1 Políticas de Análise de Risco {#31-políticas-de-análise-de-risco}
- **O que:** Identificar e avaliar riscos de cibersegurança
- **Como:** threat modeling em L2 e L3 (THR-001); em L1, só a vertente LINDDUN leve quando há dados pessoais (THR-003). A tolerância ao risco da entidade e a análise de impacto na atividade (BIA) não são prescritas pelo Manual: são lacunas declaradas.
- **Trilho:** Documentar riscos, decisões, mitigações
- **Referência:** [Cap. 03 - Threat Modeling](/sbd-toe/sbd-manual/threat-modeling/intro)

#### 3.2 Tratamento e divulgação de vulnerabilidades {#32-gestão-de-vulnerabilidades-e-patching}
- **O que:** SBOM e SCA, e um processo de divulgação coordenada que recebe e trata as comunicações externas (GOV-015, obrigatório em qualquer nível no contexto NIS2: CTX-NIS2-P14; nas entidades pertinentes, segundo a política nacional de divulgação coordenada: CTX-NIS2-P15)
- **Por quê:** o art. 21.º, n.º 2, al. e), pede o tratamento e a divulgação de vulnerabilidades
- **Como:** Gerar SBOM; scan contínuo; atualizar dependências; publicar o canal de receção de relatos externos
- **Trilho:** Manter SBOM atualizado, vulnerabilidades documentadas
- **Fora do âmbito:** a correção de sistemas operativos, equipamentos de rede e software de prateleira (segurança da entidade).
- **Referência:** [Cap. 05 - Dependências & SBOM](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro), [Cap. 14 - Governança e Contratação](/sbd-toe/sbd-manual/governanca-contratacao/intro)

#### 3.3 Segurança em Desenvolvimento e Manutenção {#33-segurança-em-desenvolvimento-e-manutenção}
- **O que:** Gates de segurança no pipeline
- **Como:** SAST/SCA antes de merge; bloqueio de secrets; validação pré-deploy
- **Trilho:** Logs auditados de quem fez o quê, quando
- **Referência:** [Cap. 06 - Desenvolvimento Seguro](/sbd-toe/sbd-manual/desenvolvimento-seguro/intro), [Cap. 07 - CI/CD Seguro](/sbd-toe/sbd-manual/cicd-seguro/intro)

#### 3.4 IAM e Controlo de Acessos {#34-iam-e-controlo-de-acessos}
- **O que:** Autenticação forte, gestão de privilégios
- **Como:** MFA (AUT-001); menor privilégio; revisão de acessos a intervalos planeados (ACC-010, GOV-014); contas privilegiadas e de administração com autenticação forte e ciclo de vida documentado (GOV-016, GOV-017), obrigatórias nas entidades pertinentes (CTX-NIS2-P12, P13, P18, P19).
- **Lacunas declaradas:** uso exclusivo e separação dos sistemas de administração (ponto 11.4.2) e revisão periódica das tecnologias de autenticação (ponto 11.6.4).
- **Trilho:** Logs de acessos, aprovações, revogações
- **Referência:** [Cap. 02 - Requisitos de Segurança](/sbd-toe/sbd-manual/requisitos-seguranca/intro), [Cap. 04 - Arquitetura Segura](/sbd-toe/sbd-manual/arquitetura-segura/intro)

#### 3.5 Criptografia {#35-criptografia}
- **O que:** Proteção de dados em trânsito e em repouso
- **Como:** TLS 1.2+; encryption at rest; key management
- **Trilho:** Inventário de certificados, rotação de chaves
- **Referência:** [Cap. 02 - Requisitos de Segurança](/sbd-toe/sbd-manual/requisitos-seguranca/intro), [Cap. 04 - Arquitetura Segura](/sbd-toe/sbd-manual/arquitetura-segura/intro)

#### 3.6 Higiene Cibernética e Formação {#36-higiene-cibernética-e-formação}
- **O que:** formação de funções técnicas e de terceiros com acesso (TRN-001, TRN-002, TRN-007)
- **Como:** Programa de formação contínua, simulações
- **Lacuna declarada:** sensibilização calendarizada e práticas de ciber-higiene para todo o pessoal não técnico e para o órgão de direção.
- **Trilho:** Presenças, materiais, avaliações
- **Referência:** [Cap. 13 - Formação e Onboarding](/sbd-toe/sbd-manual/formacao-onboarding/intro)

---

### Fase 4: Segurança da Cadeia de Fornecimento (M6–M10) {#fase-4-segurança-da-cadeia-de-fornecimento-m6m10}
**NIS2 Art. 21** - Gestão de fornecedores e terceiros

#### 4.1 Fornecedores de Componentes (SBOM) {#41-fornecedores-de-componentes-sbom}
**Já em Fase 3.2** - [Cap. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro) cobre isto com SCA + SBOM

#### 4.2 Fornecedores Contratuais {#42-fornecedores-contratuais}
- **O que:** Pessoas/empresas contratadas (contractors, outsourcing)
- **Ciclo de Vida:**
  - **Onboarding:** Validação, formação SbD, sandbox
  - **Operação:** Acesso controlado, revisão periódica
  - **Offboarding:** Revogação de acessos, auditar conclusão
- **Referência:** [Cap. 14 - Governança e Contratação](/sbd-toe/sbd-manual/governanca-contratacao/intro)

#### 4.3 Registo de Fornecedores Críticos {#43-registo-de-fornecedores-críticos}
- **O que:** Inventário de fornecedores TIC críticos
- **Como:** Campos conforme autoridade nacional (seguir guias/portais locais)
- **Estado no Manual:** política de contratação segura (Política 33), cláusulas de segurança (GOV-006) e validação de fornecedores (GOV-007); nas entidades pertinentes, em qualquer nível (CTX-NIS2-P07 a P09). Os campos do registo que a autoridade nacional peça são da organização.
- **Trilho:** Atualizações periódicas, avaliações de risco
- **Referência:** [Cap. 05 - Dependências & SBOM](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro), [Cap. 14 - Governança e Contratação](/sbd-toe/sbd-manual/governanca-contratacao/intro)

---

### Fase 5: Deteção e Resposta a Incidentes (M8–M12) {#fase-5-deteção-e-resposta-a-incidentes-m8m12}
**NIS2 Art. 23** - Reporte de incidentes significativos

#### 5.1 Monitorização Centralizada {#51-monitorização-centralizada}
- **O que:** logs centralizados da aplicação e dos acessos (LOG-001, OPS-001); nas entidades pertinentes, análise regular, alarmes com limiares e cópia de segurança dos registos (CTX-NIS2-P03 a P06). O tráfego de rede e a execução de utilitários de sistema são segurança da entidade, fora do Manual.
- **Retenção:** período definido por tipo de registo (LOG-005; Política 29 §7, escolha do Manual); prevalece o prazo mais exigente da lei, da transposição nacional ou do supervisor
- **Proteção:** Imutabilidade (impedir alteração)
- **Referência:** [Cap. 12 - Monitorização e Operações](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)

#### 5.2 Deteção e Classificação de Incidentes {#52-deteção-e-classificação-de-incidentes}
- **O que:** Identificar eventos anómalos; classificar por severidade
- **Escalação:** Conforme plano (criticidade)
- **Documentação:** O quê, quando, ações, impacto
- **Referência:** [Cap. 12 - Monitorização e Operações](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)

#### 5.3 Reporte de Incidentes Significativos {#53-reporte-de-incidentes-significativos}
- **O que:** Submeter incidentes significativos à CSIRT ou, se aplicável, à autoridade competente (art. 23.º, n.º 4)
- **Prazos:**
  - **Alerta rápido:** ≤ 24h após o conhecimento
  - **Notificação de incidente:** ≤ 72h após o conhecimento, com avaliação inicial
  - **Relatório intercalar:** a pedido da CSIRT ou da autoridade competente
  - **Relatório final:** ≤ 1 mês após a notificação de incidente (se o incidente estiver em curso: relatório intercalar nessa altura e final ≤ 1 mês após a resolução)
- **Conteúdo:** dados de impacto do registo (Política 32 §4.3); critério de incidente significativo (CTX-NIS2-R02) e, nas entidades pertinentes, limiares e agregação dos recorrentes (CTX-NIS2-R03; Política 32 §4.7); conteúdo mínimo de cada etapa (Política 32 §6.1)
- **Como:** exportadores SIEM/ITSM para os formulários da CSIRT nacional; os formulários e os canais são da autoridade
- **Referência:** [Cap. 12 - Monitorização e Operações](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)

---

### Fase 6: Continuidade e Crise (M8–M12) {#fase-6-continuidade-e-crise-m8m12}
**NIS2 Art. 21** - Garantir continuidade operacional

#### 6.1 Backups e Disaster Recovery {#61-backups-e-disaster-recovery}
- **O que:** Backups regulares, testados, off-site
- **Como:** Automatização, testes de restauração periódicos
- **Trilho:** Logs de backups, testes, resultados
- **Estado no Manual:** cópias de segurança com restauro testado em OPS-016 e objectivos e procedimento de recuperação em OPS-017 (Cap. 12); a redundância é requisito do contexto NIS2 para as entidades pertinentes.
- **Referência:** [Cap. 12 - Monitorização e Operações](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)

#### 6.2 Resposta a incidentes graves (a gestão de crises fica fora) {#62-gestão-de-crise}
- **O que:** IRP com playbooks, war room P1 e post-mortem com revisão dos artefactos afetados (Política 32 §4.6; obrigatório em qualquer nível no contexto NIS2: CTX-NIS2-P01)
- **Como:** Runbooks, exercícios, roles definidos
- **Trilho:** Exercícios documentados, lições aprendidas
- **Fora do âmbito:** a gestão de crises da entidade (Reg. de Execução (UE) 2024/2690, ponto 4.3) e o plano de continuidade do negócio.
- **Referência:** [Cap. 12 - Monitorização e Operações](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)

---

### Fase 7: Validação e Testes (M12–M18) {#fase-7-validação-e-testes-m12m18}
**NIS2 Art. 21** - Avaliar eficácia dos controlos

#### 7.1 Testes Contínuos {#71-testes-contínuos}
- **SAST:** Análise estática de código (integrado em CI/CD)
- **DAST:** Análise dinâmica de aplicações em staging
- **Penetração:** Testes manuais baseados em threat model
- **Referência:** [Cap. 10 - Testes de Segurança](/sbd-toe/sbd-manual/testes-seguranca/intro)

#### 7.2 Validação Pré-Deploy {#72-validação-pré-deploy}
- **O que:** Checklist de segurança antes de produção
- **Confirmação:** Todos requisitos L1–L3 cobertos
- **Aprovação:** Formal (AppSec + Gestão para L3)
- **Referência:** [Cap. 11 - Deploy Seguro](/sbd-toe/sbd-manual/deploy-seguro/intro)

#### 7.3 Avaliação da Eficácia {#73-avaliação-da-eficácia}
- **O que:** Revisão periódica dos controlos implementados
- **Como:** Auditorias internas, métricas de segurança, testes
- **Trilho:** Relatórios de auditoria, planos de remediação
- **Lacuna declarada:** análise independente da abordagem de segurança como um todo e independência hierárquica dos revisores (pontos 2.3.1 e 2.3.2).
- **Referência:** [Cap. 12 - Monitorização e Operações](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)

---

## Checklist de Conformidade {#checklist-de-conformidade}

A lista abaixo permite validar o alinhamento do programa SbD-ToE com os requisitos NIS2. Sugere-se a revisão periódica destes pontos para manter o alinhamento:

- [ ] **Governação:** Cadeia formal de aprovação e supervisão documentada; RACI mapeado; formação anual do órgão de direção (assegurada pela organização: lacuna declarada do Manual)
- [ ] **Classificação:** Todas apps classificadas L1–L3; tipo de entidade (essencial/importante) definido
- [ ] **Políticas de Risco:** Threat modeling formal (L2–L3) e LINDDUN leve em L1 quando há dados pessoais (THR-003)
- [ ] **Vulnerabilidades:** SBOM gerado e atualizado; SCA contínuo
- [ ] **CI/CD:** Gates de segurança operacionais
- [ ] **IAM:** MFA implementado; princípio do menor privilégio ativo
- [ ] **Criptografia:** TLS 1.2+; encryption at rest; key management
- [ ] **Formação:** Programa de formação contínua operacional
- [ ] **Fornecedores:** Inventário de fornecedores críticos; ciclo de vida operacional
- [ ] **Monitorização:** Logs centralizados, retenção adequada
- [ ] **Incidentes:** IRP em qualquer nível (CTX-NIS2-P01); deteção, escalonamento e conteúdo mínimo da Política 32 §6.1 para o reporte 24h/72h/1M
- [ ] **Continuidade:** Backups testados; runbooks e recuperação operacional validados
- [ ] **Testes:** SAST/DAST integrados; avaliação da eficácia periódica
- [ ] **Evidência:** Data room com documentação (políticas, testes, logs, formações)

---

## O Que Cada Capítulo SbD-ToE Cobre (Referência Rápida) {#o-que-cada-capítulo-sbd-toe-cobre-referência-rápida}

| Capítulo | NIS2 Artigos | O Que Faz |
|----------|-------------|----------|
| **[Cap. 01](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)** | Art. 21 | Classificação de apps por risco (L1–L3) |
| **[Cap. 02](/sbd-toe/sbd-manual/requisitos-seguranca/intro)** | Art. 21 (primário), Art. 20 (suporte) | Base técnica de requisitos de segurança mínimos por nível |
| **[Cap. 03](/sbd-toe/sbd-manual/threat-modeling/intro)** | Art. 21 | Threat modeling para identificar ameaças realistas |
| **[Cap. 04](/sbd-toe/sbd-manual/arquitetura-segura/intro)** | Art. 21 | Arquitetura segura, IAM, criptografia |
| **[Cap. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro)** | Art. 21 | SBOM, SCA, gestão de vulnerabilidades |
| **[Cap. 06](/sbd-toe/sbd-manual/desenvolvimento-seguro/intro)** | Art. 21 | Desenvolvimento seguro |
| **[Cap. 07](/sbd-toe/sbd-manual/cicd-seguro/intro)** | Art. 21 | CI/CD seguro, gates, trilho auditado |
| **[Cap. 08](/sbd-toe/sbd-manual/iac-infraestrutura/intro)** | Art. 21 | IaC segura |
| **[Cap. 09](/sbd-toe/sbd-manual/containers-imagens/intro)** | Art. 21 | Containers/runtime seguros |
| **[Cap. 10](/sbd-toe/sbd-manual/testes-seguranca/intro)** | Art. 21 | Testes contínuos (SAST/DAST/penetração) |
| **[Cap. 11](/sbd-toe/sbd-manual/deploy-seguro/intro)** | Art. 21 | Validação pré-deploy, conformidade requisitos |
| **[Cap. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)** | Art. 20 (supervisão), Art. 21, 23 | Monitorização, incidentes, runbooks, continuidade operacional e evidência |
| **[Cap. 13](/sbd-toe/sbd-manual/formacao-onboarding/intro)** | Art. 20, 21 | Formação de funções técnicas e de terceiros com acesso; a formação do órgão de direção é lacuna declarada |
| **[Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro)** | Art. 20 (primário), Art. 21, 23 | Governança, cadeia de aprovação, escalonamento e ciclo de vida fornecedores |

---

## Métrica simples: autoavaliação da base {#métrica-simples-estou-compliant}

Cada resposta afirmativa conta um ponto; a leitura do resultado vem a seguir à lista.

1. **Governance:** Tenho cadeia formal de aprovação e supervisão da gestão?
2. **Board Training:** A gestão tem formação anual em cibersegurança?
3. **Risk Management:** Todas as apps estão classificadas?
4. **Policies:** Tenho políticas de análise de risco e segurança?
5. **Vulnerabilities:** Tenho SBOM e SCA ativo?
6. **Development:** CI/CD seguro com gates operacionais?
7. **IAM & Crypto:** MFA e criptografia implementados?
8. **Training:** Programa de formação contínua ativo?
9. **Supply Chain:** Inventário de fornecedores críticos e ciclo de vida operacional?
10. **Operations:** Monitorização centralizada com retenção adequada?
11. **Incident Response:** Consigo detetar, escalar internamente e preparar reporte 24h/72h/1M?
12. **Continuity:** Backups testados, runbooks e recuperação operacional validados?
13. **Testing:** Faço SAST/DAST e avaliação da eficácia?
14. **Evidence:** Consigo demonstrar tudo isto em auditoria?

**Com 12 ou mais em 14:** a base do lado da aplicação é forte. Para uma auditoria NIS2 faltam ainda as medidas da entidade que o Manual deixa fora do âmbito (segurança física, postos de trabalho, RH, continuidade e crise, inventário de todos os ativos), as lacunas declaradas em [Requisitos aplicáveis](./requisitos-aplicaveis#cobertura) e os requisitos nacionais e setoriais.  
**Com menos de 7 em 14:** a prioridade é governação, classificação, monitorização e incidentes.

---

## Nota Crítica: Gestão de Exceções em NIS2 {#nota-crítica-gestão-de-exceções-em-nis2}

NIS2 exige conformidade com medidas de gestão de risco (Art. 21). Exceções (desvios) devem ser formais e auditadas, com trilho documental e aprovação adequada.

O que caracteriza uma exceção em SbD-ToE/NIS2:
- Desvio formal de um requisito
- Exemplo: deploy com uma vulnerabilidade High por corrigir, quando o SCA bloqueia Critical e High em qualquer nível (DEP-002)
- Aprovação formal, justificação, TTL (Time-To-Live), plano de remediação

Quem aprova, no Manual (Política 05 §6):
- L1: Tech Lead ou AppSec Engineer
- L2: AppSec Engineer, com Gestão de Produto para High, e CISO para Critical
- L3: AppSec Engineer com GRC para Medium e CISO para High; o Critical não é aceitável como exceção

Elevar a decisão ao órgão de direção, como a leitura do art. 20.º sugere, é formalização da organização: o Manual não o prescreve (lacuna declarada face ao Reg. de Execução (UE) 2024/2690, ponto 2.3.3).

Implicação regulatória:
- Exceções sem aprovação formal podem comprometer a supervisão (Art. 20)
- Os limites das exceções são os da Política 05 (alçadas e prazos por severidade e nível; Critical não aceitável em L3); a NIS2 não enumera exceções inadmissíveis, mas exige medidas corretivas sem demora injustificada quando há incumprimento (art. 21.º, n.º 4)
- Trilho auditado é obrigatório para demonstrar controlo à autoridade nacional

Sugere-se:
1. Política clara de quem aprova por nível de risco
2. Trilho auditado: O quê, quem, quando, justificação, TTL
3. SLAs de remediação da escada interna do Manual (Política 19 §4.3; escolha do Manual — o art. 21.º, n.º 2, al. e), pede o tratamento de vulnerabilidades sem fixar prazos)
4. Lista de exceções inaceitáveis (política)
5. Revisão periódica, escalação se expirada

A ausência de formalização pode comprometer a conformidade regulatória e expor a organização a riscos desnecessários.

**Referência:** [Cap. 02 - Requisitos de Segurança](/sbd-toe/sbd-manual/requisitos-seguranca/intro) como base técnica e [Cap. 14 - Governança](/sbd-toe/sbd-manual/governanca-contratacao/intro) para formalização das exceções

---

## Recursos Práticos de Implementação {#recursos-práticos-de-implementação}

Para suporte concreto na implementação deste playbook, consultar os seguintes exemplos reutilizáveis:

- 🛠️ **[Opções de Toolchain](../exemplo-playbook/exemplo-toolchain-options)** - Comparação de ferramentas (IaC, logs, SCA, SAST, CI/CD) com exemplos de configuração
- 📊 **[KPIs e Targets](../exemplo-playbook/exemplo-kpis-targets)** - Métricas de segurança por perfil organizacional compatíveis com NIS2
- 👥 **[RACI e Governance](../exemplo-playbook/exemplo-raci-governance)** - Matrizes de responsabilidades alinhadas com Art. 20 (responsabilização de gestão)
- 📝 **[Relatório de Incidentes](../exemplo-playbook/exemplo-relatorio-incidentes)** - Templates de reporte formal com timelines NIS2 (24h/72h/1M)

Estes recursos são **reutilizáveis para múltiplos frameworks** (NIS2, DORA, ISO 27001, CRA) e mostram opções práticas para o que o SbD-ToE deixa deliberadamente configurável (o manual não prescreve ferramentas específicas).

---

## Próximos Passos {#próximos-passos}

Sugere-se a seguinte abordagem para garantir conformidade e maturidade contínua:

1. Audit de conformidade atual: Verificar [Cap. 01](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)–[Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro) do SbD-ToE contra requisitos NIS2
2. Verificar classificação da entidade: Essencial / Importante (conforme Anexos I/II)
3. Definir roadmap: Sequenciar fases conforme contexto organizacional
4. Implementar: Iterar conforme planeado
5. Registar na autoridade nacional: Seguir guias/portais locais (se aplicável)
6. Validar: Demonstrar conformidade em auditoria

Documentação completa: Ver capítulos SbD-ToE 01–14 para detalhe técnico e operacional.

---

## Referências {#referências}

- **SbD-ToE Manual:** Capítulos 01–14 (detalhe técnico por domínio)
- **Cross-Check NIS2:** [Análise normativa completa](/sbd-toe/cross-check-normativo/nis2/intro)
- **Diretiva NIS2:** UE 2022/2555
- **ENISA:** Orientações técnicas e mapeamentos práticos (2024/2025)
- **Autoridades Nacionais:** Guias/portais de registo e requisitos locais

---

**Versão:** 1.1  
**Data:** Setembro 2026  
**Nota:** Este playbook complementa a [análise normativa NIS2](intro) com implementação prática
