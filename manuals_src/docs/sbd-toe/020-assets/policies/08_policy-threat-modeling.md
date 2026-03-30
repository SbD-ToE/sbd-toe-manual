---
id: policy-threat-modeling
title: Política de Threat Modeling
description: Política organizacional que define a obrigatoriedade, metodologia, triggers de execução, requisitos de aprovação formal, rastreabilidade e gestão dos artefactos de threat modeling ao longo do ciclo de vida de aplicações classificadas L2 e L3.
tags: [policy, threat modeling, STRIDE, LINDDUN, PASTA, ameaças, cap03, cap04, L2, L3, governance, arquitetura, rastreabilidade]
sidebar_position: 8
---

# Política de Threat Modeling

## 1. Objetivo

Esta política define os requisitos para a realização de **threat modeling** - modelação sistemática de ameaças - em aplicações classificadas como L2 ou L3.

O threat modeling é o elo entre a classificação de risco, os requisitos de segurança e os controlos aplicados. Sem modelação de ameaças, os requisitos de segurança perdem contexto e os controlos aplicados deixam de ter origem justificada: são aplicados por hábito ou convenção, não por análise de risco real.

O objetivo desta política é garantir que:

- As ameaças relevantes para cada aplicação são identificadas sistematicamente
- As decisões de mitigação, aceitação ou transferência de risco são documentadas e aprovadas
- O modelo de ameaças permanece válido e atualizado ao longo do ciclo de vida
- Os artefactos produzidos são rastreáveis, protegidos e auditáveis

---

## 2. Âmbito e obrigatoriedade

| Nível | Obrigatoriedade |
|---|---|
| L1 | Opcional; recomendado para aplicações com lógica crítica ou exposição externa |
| L2 | Obrigatório |
| L3 | Obrigatório; com revisão independente e aprovação formal |

---

## 3. Metodologias

A organização adota as seguintes metodologias, selecionadas proporcionalmente ao contexto:

| Metodologia | Foco | Quando aplicar |
|---|---|---|
| **STRIDE** | Ameaças técnicas (Spoofing, Tampering, Repudiation, Information Disclosure, DoS, Elevation of Privilege) | Aplicações expostas ou com lógica crítica - uso base em L2 e L3 |
| **LINDDUN** | Ameaças à privacidade | Sistemas com dados pessoais, sujeitos a RGPD ou obrigações de consentimento |
| **PASTA** | Modelação baseada em risco de negócio | Sistemas regulados, críticos ou em contextos com exigência formal elevada |

Em L2, STRIDE é suficiente como metodologia base. Em L3, LINDDUN deve ser aplicado sempre que existam dados pessoais, e PASTA deve ser considerado em contextos regulatórios.

---

## 4. Quando realizar threat modeling

### 4.1 Triggers obrigatórios

| Evento | Obrigatoriedade |
|---|:---:|
| Arranque de novo projeto ou produto (L2/L3) | Obrigatório |
| Nova integração externa ou exposição adicional | Obrigatório |
| Alteração significativa de arquitetura | Obrigatório |
| Novo tipo de dado sensível tratado | Obrigatório |
| Adição de novo perfil de utilizador com privilégios | Obrigatório |
| Resultado de pentest que evidencie lacuna no modelo | Obrigatório |
| Pós-incidente com origem em ameaça não modelada | Obrigatório |

### 4.2 Cadência periódica

Em complemento aos triggers, o modelo de ameaças deve ser revisto com cadência mínima:

| Nível | Cadência mínima |
|---|---|
| L2 | Anual ou por cada release major |
| L3 | Semestral ou por cada release major |

---

## 5. Processo de threat modeling

### 5.1 Passos obrigatórios

1. **Definir âmbito e assunções** - fronteiras do sistema, componentes incluídos, assunções de confiança, perfis de atacante
2. **Criar ou atualizar o diagrama de arquitetura** - DFD (Data Flow Diagram) ou equivalente, com trust boundaries explícitas
3. **Identificar ameaças** - usando a metodologia selecionada (STRIDE, LINDDUN, PASTA)
4. **Avaliar e priorizar** - impacto, probabilidade, severidade por ameaça
5. **Decidir por ameaça** - mitigar / aceitar / transferir / rejeitar - com justificação documentada
6. **Mapear para requisitos e controlos** - ligar cada ameaça mitigada ao requisito ou controlo correspondente
7. **Aprovar formalmente** - pela alçada adequada ao nível de risco
8. **Arquivar** - versão aprovada com metadados de rastreabilidade

### 5.2 Checklist de conteúdo mínimo do modelo

- [ ] Âmbito, assunções e limites documentados
- [ ] Diagrama de arquitetura com trust boundaries
- [ ] Lista de ameaças identificadas por componente/fluxo
- [ ] Decisão documentada por ameaça (mitigar / aceitar / transferir / rejeitar)
- [ ] Ligação a requisitos de segurança (`REQ-*`) ou controlos (`CTRL-*`) para ameaças mitigadas
- [ ] Riscos aceites com justificação e referência ao processo de aceitação de risco
- [ ] Versão, data e responsável pela elaboração
- [ ] Aprovação formal registada

---

## 6. Aprovação formal

O modelo de ameaças só é válido como controlo de segurança quando existe **aprovação formal** documentada.

| Nível | Aprovação mínima requerida |
|---|---|
| L2 | AppSec Engineer + Tech Lead |
| L3 | AppSec Engineer + Arquiteto de Software + revisão independente |

A aprovação deve incluir:
- Confirmação de que o âmbito está correto e completo
- Confirmação de que as decisões por ameaça são tecnicamente fundamentadas
- Data e identificação do aprovador

---

## 7. Atualização por alteração técnica

Sempre que ocorra uma alteração significativa, o modelo de ameaças deve ser atualizado **antes da promoção a produção**:

- [ ] Alteração significativa identificada e documentada
- [ ] Ameaças novas ou alteradas registadas
- [ ] Decisões de mitigação ou aceitação atualizadas
- [ ] Nova versão aprovada formalmente
- [ ] Ligação ao commit ou PR que originou a alteração

O pipeline CI/CD deve incluir um gate que verifique se o modelo de ameaças está atualizado face a alterações relevantes, bloqueando a promoção em L2/L3 quando o modelo estiver desatualizado sem justificação aprovada.

---

## 8. Integração com arquitetura

O threat modeling e a arquitetura segura devem estar sincronizados de forma bidirecional:

- Decisões de arquitetura devem refletir as ameaças priorizadas no modelo
- Alterações arquiteturais devem despoletar atualização do modelo de ameaças quando aplicável
- Architecture Decision Records (ADR) devem referenciar ameaças relevantes quando a decisão tem impacto de segurança

---

## 9. Proteção e retenção dos artefactos

Os artefactos de threat modeling (diagramas, modelos, decisões) são **ativos sensíveis** - contêm informação sobre a arquitetura interna, fluxos de dados e vulnerabilidades identificadas.

### 9.1 Controlo de acesso

- Acesso restrito ao princípio do menor privilégio
- Partilha apenas com funções que necessitem do acesso para exercer as suas responsabilidades
- Não publicar em repositórios públicos ou sistemas sem controlo de acesso

### 9.2 Classificação

| Nível | Classificação mínima recomendada |
|---|---|
| L2 | Confidencial - interno à equipa de produto e segurança |
| L3 | Confidencial / Restrito - acesso limitado a AppSec, arquitetura e gestão |

### 9.3 Retenção

| Artefacto | Retenção mínima |
|---|---|
| Modelo de ameaças (versão ativa) | Enquanto a aplicação estiver ativa |
| Versões históricas aprovadas | 3 anos após substituição |
| Registos de aprovação | 3 anos |
| Riscos aceites associados | Conforme Política de Aceitação de Risco Residual |

---

## 10. Reutilização de modelos anteriores

A reutilização de um modelo de ameaças anterior como base para um novo projeto ou revisão é permitida, desde que:

- [ ] O modelo anterior seja explicitamente identificado como referência
- [ ] As diferenças de contexto, arquitetura e fluxos sejam analisadas e documentadas
- [ ] Decisões críticas herdadas sejam revalidadas explicitamente
- [ ] A reutilização seja registada com o responsável pela revisão

A reutilização sem revisão explícita é equivalente a não ter threat modeling - o modelo original não é válido para um contexto diferente.

---

## 11. Proporcionalidade por nível

| Requisito | L1 | L2 | L3 |
|---|---|---|---|
| Threat modeling obrigatório | Não | Sim | Sim |
| STRIDE como metodologia base | Recomendado | Obrigatório | Obrigatório |
| LINDDUN (dados pessoais) | Opcional | Recomendado | Obrigatório |
| Aprovação formal | Não aplicável | AppSec + Tech Lead | AppSec + Arquiteto + revisão independente |
| Gate no pipeline CI/CD | Não aplicável | Recomendado | Obrigatório |
| Revisão periódica | A pedido | Anual / release major | Semestral / release major |
| Artefactos com controlo de acesso | Recomendado | Obrigatório | Obrigatório |

---

## 12. Responsabilidades

| Role | Responsabilidade |
|---|---|
| Arquiteto de Software | Conduzir ou coordenar o threat modeling; manter o diagrama de arquitetura atualizado |
| AppSec Engineer | Apoiar na identificação de ameaças; aprovar o modelo; garantir rastreabilidade |
| Tech Lead / Developer | Participar na sessão de threat modeling; implementar mitigações atribuídas |
| DevOps / SRE | Configurar gate de consistência no pipeline; gerir armazenamento protegido dos artefactos |
| GRC / Compliance | Garantir que todas as aplicações L2/L3 têm modelo aprovado e atualizado |

---

## 13. Revisão e auditoria desta política

Esta política deve ser **revista anualmente** ou após qualquer um dos seguintes eventos:

- Incidente originado em ameaça não modelada
- Atualização das metodologias de referência (STRIDE, LINDDUN, PASTA)
- Alteração regulatória com impacto na obrigatoriedade de threat modeling

---

## 14. Referências normativas e técnicas

| Referência | Relevância |
|---|---|
| SbD-ToE Cap. 03 - Threat Modeling | Metodologias, user stories, artefactos, integração no SDLC |
| SbD-ToE Cap. 04 - Arquitetura Segura | Sincronização threat modeling ↔ arquitetura |
| SbD-ToE Cap. 02 - Requisitos de Segurança | Ligação ameaça → requisito |
| STRIDE (Microsoft) | Metodologia de categorização de ameaças técnicas |
| LINDDUN | Metodologia de ameaças à privacidade |
| PASTA | Process for Attack Simulation and Threat Analysis |
| OWASP Threat Modeling Cheat Sheet | Guia prático de implementação |
| NIST SP 800-154 | Guide to Data-Centric System Threat Modeling |
| SSDF PW.1 | Análise de ameaças como base para requisitos de segurança |
| ISO/IEC 27005 | Gestão de risco de segurança da informação |
