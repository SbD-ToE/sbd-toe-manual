---
id: baseline
title: Obrigações Mínimas Transversais
sidebar_label: 🛡️ Baseline Obrigatório
description: O núcleo duro de práticas que todas as aplicações devem cumprir, independentemente do nível de risco
tags: [obrigacoes, baseline, minimo, must, nis2, dora, gdpr]
sidebar_position: 4
---

# Obrigações Mínimas Transversais

A segurança de software não pode depender da criticidade de cada aplicação para garantir a existência de um **piso mínimo comum**.  
Sem esse alicerce, a organização fragmenta-se: algumas equipas aplicam práticas robustas, outras não aplicam nenhuma, e o resultado é um ecossistema inconsistente, vulnerável e difícil de auditar.

As **obrigações mínimas transversais** são, por isso, a base do SbD-ToE.  
Não pretendem substituir a proporcionalidade L1–L3, mas antes criar uma camada uniforme que garante que, seja qual for a aplicação, existe sempre um conjunto de controlos elementares implementados.

Estas obrigações não se aplicam apenas ao código ou à aplicação em si. Aplicam-se igualmente a **processos, pipelines, ambientes, automações e integrações externas** que participem no ciclo de vida do software.

A não aplicação de qualquer obrigação mínima **não é uma escolha técnica**, mas uma **decisão organizacional formal**, que deve ser explicitamente justificada, aprovada e rastreável conforme o modelo de governação do SbD-ToE (Cap. 14).

---

## 🎯 O Núcleo Duro: 8 Obrigações Transversais {#-o-núcleo-duro-8-obrigações-transversais}

Independentemente do nível de risco, **todas as aplicações** devem implementar:

### 1️⃣ **Classificação da Criticidade** (Cap. 01) {#1️⃣-classificação-da-criticidade-cap-01}
**O que**: Antes de iniciar qualquer desenvolvimento, classificar o nível de risco da aplicação (L1, L2, L3).

**Por quê**: Sem classificação, é impossível determinar que práticas aplicar. Torna a decisão de investimento em segurança arbitrária.

**Responsável**: Product Owner, Arquiteto, CISO

**Regulamentos**: NIS2 (assessment de risco), DORA (classificação de criticidade)

---

### 2️⃣ **Requisitos Mínimos de Segurança** (Cap. 02) {#2️⃣-requisitos-mínimos-de-segurança-cap-02}
**O que**: Definir e rastrear um conjunto mínimo de requisitos de segurança que a aplicação deve cumprir.

**Por quê**: Requisitos explícitos permitem que DevOps e QA validem implementação; sem eles, segurança fica vaga.

**Responsável**: Product Owner, AppSec, QA

**Regulamentos**: NIS2 (medidas técnicas), GDPR (data protection by design)

---

### 3️⃣ **Gestão Explícita de Dependências** (Cap. 05) {#3️⃣-gestão-explícita-de-dependências-cap-05}
**O what**: Manter um inventário atualizado de todas as dependências críticas (frameworks, bibliotecas, sistemas). Incluir versões e alertas de vulnerabilidades.

**Por quê**: A maioria das vulnerabilidades exploradas vêm de dependências não geridas ou desatualizadas. Um inventário é fundamental para incident response.

**Responsável**: DevOps, Developers, AppSec

**Regulamentos**: NIS2 (supply chain risk), DORA (vendor management)

---

### 4️⃣ **Coding Guidelines Básicas e Validação Automática** (Cap. 06) {#4️⃣-coding-guidelines-básicas-e-validação-automática-cap-06}
**O que**: Aplicar um conjunto mínimo de guidelines de código seguro (ex.: evitar injection, validar inputs, usar hashing seguro). Configurar SAST (Static Application Security Testing) automático em todas as builds.

**Por quê**: Guidelines e SAST combinados eliminam a maioria das vulnerabilidades triviais com custo marginal quase nulo.

**Responsável**: Developers, AppSec, DevOps

**Regulamentos**: GDPR (security by design), NIS2 (medidas técnicas)

---

### 5️⃣ **Pipelines CI/CD com Verificações Mínimas** (Cap. 07) {#5️⃣-pipelines-cicd-com-verificações-mínimas-cap-07}
**O what**: Executar pipelines CI/CD com gates mínimos de segurança (SAST, dependency scanning, secret scanning). Nunca fazer deploy sem validações.

**Por quê**: Pipelines automáticos garantem que nenhum código vulnerável chega a produção por lapso humano. Estas verificações podem ser totalmente automatizadas, desde que os critérios de execução e bloqueio sejam objetivos, determinísticos e auditáveis. A validação automática substitui a aprovação humana quando o dono dessa aprovação a aceitou como suficiente e determinística; o que dela se desvia volta a ele como exceção.

**Responsável**: DevOps, AppSec

**Regulamentos**: NIS2 (controlo de alterações), DORA (change management)

---

### 6️⃣ **Registo e Monitorização Essencial** (Cap. 12) {#6️⃣-registo-e-monitorização-essencial-cap-12}
**O que**: Ativar logging mínimo em todos os serviços (eventos de autenticação, alterações críticas, erros). Correlacionar logs em ponto central e monitorizar anomalias.

**Por quê**: Logs são o alicerce da deteção de incidentes e da accountability regulatória.

**Responsável**: DevOps, Ops, CISO

**Regulamentos**: NIS2 (logging de incidentes), DORA (monitoring), GDPR (audit trails)

---

### 7️⃣ **Formação Inicial em Segurança** (Cap. 13) {#7️⃣-formação-inicial-em-segurança-cap-13}
**O que**: Garantir que todos os membros da equipa (Developers, QA, DevOps, etc.) recebem formação inicial obrigatória em segurança de software, alinhada aos papéis.

**Por quê**: Equipas conscientes de riscos evitam erros. Formação é o investimento com maior ROI em segurança.

**Responsável**: CISO, Security Champion, Gestão

**Regulamentos**: NIS2 (competência), DORA (staff training)

---

### 8️⃣ **Cláusulas Mínimas de Segurança em Fornecedores** (Cap. 14) {#8️⃣-cláusulas-mínimas-de-segurança-em-fornecedores-cap-14}
**O que**: Incluir em contratos com fornecedores/terceiros cláusulas mínimas de segurança (compromisso com responsabilidade de dados, direito de auditoria, notificação de incidentes).

**Por quê**: A cadeia de fornecimento é uma das maiores fontes de risco. Sem cláusulas contractuais, não há forma de exigir compliance.

**Responsável**: GRC, CISO, Jurídico

**Regulamentos**: NIS2 (cadeia de fornecimento), DORA (vendor management), GDPR (data processors)

---

## 📊 Mapa de Cobertura {#-mapa-de-cobertura}

| Obrigação | Capítulo | Responsável | Validação |
|-----------|----------|-------------|-----------|
| 1. Classificação | 01 | Product Owner / Arquiteto | CISO / GRC |
| 2. Requisitos | 02 | AppSec / Product Owner | QA / GRC |
| 3. Dependências | 05 | DevOps / Developers | SCA Tools / AppSec |
| 4. Coding Guidelines | 06 | Developers | SAST Tools / Code Review |
| 5. CI/CD Gates | 07 | DevOps | Automated Pipelines |
| 6. Logging | 12 | DevOps / Ops | Monitoring Tools / Auditores |
| 7. Formação | 13 | CISO / Security Champion | Attendance Tracking |
| 8. Contratos | 14 | GRC / Jurídico | Contract Review / Auditores |

---

## 💡 Racional Técnico-Científico {#-racional-técnico-científico}

A definição destas obrigações mínimas baseia-se em:

### **Estudos de Incidentes Reais** {#estudos-de-incidentes-reais}
Os relatórios de incidentes publicados, como o Verizon DBIR e o ENISA Threat Landscape, descrevem de forma recorrente incidentes com origem em falhas básicas: credenciais comprometidas, vulnerabilidades conhecidas por corrigir, falta de registo. São contexto para a escolha destas obrigações, não prova da sua eficácia; os números de cada edição aplicam-se à população e ao período que essa edição estuda.

### **OWASP Top 10** {#owasp-top-10}
As obrigações mínimas endereçam as categorias do OWASP Top 10 (edição de 2021), sem garantir que as previnem:
- **A01 Broken Access Control** → Requisitos claros (obrigação 2)
- **A02 Cryptographic Failures** → Requisitos e guidelines de código (2, 4)
- **A03 Injection** → Guidelines de código e SAST no pipeline (4, 5)
- **A04 Insecure Design** → Requisitos e classificação de risco (1, 2); o threat modeling (Cap. 03) aprofunda
- **A05 Security Misconfiguration** → Guidelines e verificações no pipeline (4, 5)
- **A06 Vulnerable and Outdated Components** → Gestão de dependências (3)
- **A07 Identification and Authentication Failures** → Requisitos (2)
- **A08 Software and Data Integrity Failures** → Verificações no pipeline (5)
- **A09 Security Logging and Monitoring Failures** → Registo e monitorização (6)
- **A10 SSRF** → Requisitos e guidelines (2, 4); o threat modeling (Cap. 03) aprofunda

### **Modelos de Maturidade** {#modelos-de-maturidade}
As práticas destas obrigações correspondem a práticas de base dos modelos de maturidade usados como referência (OWASP SAMM, BSIMM). É uma correspondência de conteúdo, não uma medição: o Manual não afirma que todas as organizações maduras as partilham.

---

## ⚖️ Baseline vs. Proporcionalidade (L1–L3) {#️-baseline-vs-proporcionalidade-l1l3}

**Importante**: As obrigações mínimas **não substituem** a proporcionalidade L1–L3.

```
┌──────────────────────────────────────┐
│   8 Obrigações Mínimas (SEMPRE)      │
├──────────────────────────────────────┤
│  L1 (Baixo Risco)                    │
│  - Mínimos acima + validações básicas│
├──────────────────────────────────────┤
│  L2 (Risco Moderado)                 │
│  - Mínimos + práticas robustas       │
│  - Threat modeling, security reviews │
├──────────────────────────────────────┤
│  L3 (Risco Crítico)                  │
│  - Mínimos + aplicação integral      │
│  - Red teaming, auditorias rigorosas │
└──────────────────────────────────────┘
```

O que muda entre níveis é a **intensidade, profundidade e formalização**.  
Mas o baseline é transversal e **nunca é negociável**.

---

## 🔄 Pragmatismo e Aplicação Universal {#-pragmatismo-e-aplicação-universal}

Um aspeto essencial é a eficiência: em muitos casos, aplicar **determinadas práticas a todas as aplicações** é mais prático do que discussões caso a caso.

### Exemplos Práticos {#exemplos-práticos}

**SAST em todos os repositórios**  
→ Há ferramentas open source sem custo de licença; o custo operacional (configuração, triagem de resultados, manutenção) existe sempre.  
→ Detecta cedo uma parte dos defeitos triviais; a taxa de falsos positivos depende da ferramenta, da configuração e do código.

**Dependency scanning automático em pipelines**  
→ Um job padrão em todos os projetos simplifica política.  
→ Evita debates sobre "será que este lib é crítico?"

**Logging e monitorização por defeito**  
→ Ativar collectors em todos os serviços facilita auditorias.  
→ Dá a base para detectar incidentes; a rapidez da detecção depende da monitorização e da resposta.

**Templates contratuais mínimos**  
→ Aplicar cláusulas iguais a todos os fornecedores reduz negociação.  
→ Legal fica consistente.

---

## 📋 Checklist de Implementação {#-checklist-de-implementação}

Para cada aplicação, validar:

- [ ] **Classificação (L1/L2/L3)** documentada e aprovada
- [ ] **Requisitos de segurança mínimos** definidos e rastreados
- [ ] **SBOM/inventário de dependências** atualizado
- [ ] **SAST configurado** e integrado em CI/CD
- [ ] **Dependency scanning ativo** com alertas
- [ ] **Coding guidelines** distribuídas à equipa
- [ ] **CI/CD gates** implementados (SAST, deps, secrets)
- [ ] **Logging mínimo** implementado e centralizado
- [ ] **Monitorização essencial** ativa (alertas críticos)
- [ ] **Formação de segurança** completada por todos
- [ ] **Cláusulas contratuais** em lugar com fornecedores

---

## 🔗 Alinhamento Regulatório {#-alinhamento-regulatório}

As 8 obrigações **contribuem** para vários regimes; não equivalem a conformidade com nenhum deles. A cobertura obrigação a obrigação, com o que o Manual cobre, as lacunas declaradas e o que fica fora de âmbito, está nas páginas do [cross-check normativo](/sbd-toe/cross-check-normativo/intro).

### **NIS2 (Directive on Network and Information Security)** {#nis2-directive-on-network-and-information-security}
- Contribuem para as medidas técnicas do art. 21.º (registo, monitorização, gestão de vulnerabilidades, avaliação de risco). Ver o [cross-check NIS2](/sbd-toe/cross-check-normativo/nis2/intro).

### **DORA (Digital Operational Resilience Act)** {#dora-digital-operational-resilience-act}
- Contribuem sobretudo as obrigações 5 a 8 (pipeline, registo, formação, fornecedores). Ver o [cross-check DORA](/sbd-toe/cross-check-normativo/dora/intro).

### **GDPR (General Data Protection Regulation)** {#gdpr-general-data-protection-regulation}
- Contribuem sobretudo as obrigações 2, 4 e 6 para a proteção de dados desde a conceção e a segurança do tratamento. Ver o [cross-check RGPD](/sbd-toe/cross-check-normativo/gdpr/intro).

### **PCI-DSS (Payment Card Industry)** {#pci-dss-payment-card-industry}
- Referência usada, sem cross-check publicado nem mapeamento requisito a requisito. Há sobreposição temática com vários requisitos da norma; isso não é conformidade.

### **ISO/IEC 27001** {#isoiec-27001}
- Referência usada, sem cross-check publicado. Várias obrigações correspondem a controlos do anexo A; a correspondência não está mapeada controlo a controlo.

---

## 📈 Impacto Esperado {#-impacto-esperado}

Com as 8 obrigações implementadas, esperam-se efeitos nesta direcção. São **hipóteses**, sem eficácia demonstrada pelo Manual: dependem do contexto, do ponto de partida e da qualidade da implementação, e cada organização mede-as com os KPIs dos capítulos.

| Área | Efeito esperado (hipótese) |
|---------|---------|
| **Vulnerabilidades triviais** | Menos, por guidelines e SAST |
| **Incidentes por dependências** | Menos, por SCA e inventário |
| **Tempo de detecção (MTTD)** | Menor, por registo e monitorização |
| **Tempo de resposta (MTTR)** | Menor, por registos centralizados |
| **Preparação para auditoria** | Maior, por rastreabilidade |
| **Custo de remediação** | Menor, por detecção mais cedo |

---

## 🎯 Próximos Passos {#-próximos-passos}

1. **Audita o estado atual**: Qual destas 8 obrigações estão já implementadas?
2. **Prioriza gaps**: Qual é mais urgente? (Recomendação: começar com 1, 2, 5, 7)
3. **Aloca recursos**: Cada obrigação tem um "dono" - Define responsabilidades
4. **Define timeline**: Qual é o prazo para implementar as 8 obrigações?
5. **Mede**: Estabelece KPIs para cada obrigação

---

**Leitura Relacionada**:
- [Papéis e Responsabilidades](./roles-responsabilidades/intro) - Quem implementa cada obrigação
- [Cap. 01 - Classificação](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro) - Como classificar aplicações
- [Cap. 02 - Requisitos](/sbd-toe/sbd-manual/requisitos-seguranca/intro) - Como definir requisitos

---

**Nota Final**: O baseline é não-negociável, mas a sua implementação é flexível.  
Uma pequena startup pode aplicar os 8 com ferramentas open source e esforço mínimo.  
Uma enterprise aplicará com frameworks, conformidade regulatória e processos formalizados.  
Mas a essência é sempre a mesma: **nada fica sem segurança básica**.
