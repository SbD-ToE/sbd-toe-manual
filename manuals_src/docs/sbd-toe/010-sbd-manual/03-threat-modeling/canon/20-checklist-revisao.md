---
id: checklist-revisao
title: Checklist SbD-ToE - Threat Modeling
sidebar_label: Checklist de Revisão
sidebar_position: 20
description: Checklist binário e auditável da adoção das práticas de threat modeling do Capítulo 03
tags: [checklist, threat-modeling, validação, auditoria, rastreabilidade]
---

# Checklist de Revisão Periódica - Threat Modeling

Este checklist aplica-se a todas as aplicações com criticidade L2 ou L3, ou que envolvam fluxos sensíveis, exposições externas ou alterações de arquitetura relevantes.

Serve como instrumento de verificação binária e auditável da **adoção prática das prescrições do Capítulo 3 - Threat Modeling** (`THR-001` a `THR-008`), permitindo:

- Verificação formal em revisões técnicas e auditorias;
- Controlo da rastreabilidade entre ameaças, requisitos e controlos;
- Geração de indicadores operacionais agregáveis por projeto ou equipa.

> 🗓️ **Recomenda-se a sua revisão no início de cada épico ou funcionalidade crítica, e antes de alterações significativas no sistema.**

---

## 📋 Itens de Verificação

| Item                                                                                                  | Verificado? |
|-------------------------------------------------------------------------------------------------------|-------------|
| Existe threat model formal documentado para a aplicação (L2+), rastreável à versão de arquitetura avaliada? | ☐           |
| O modelo inclui DFDs atualizados com trust boundaries explícitas e justificadas?                      | ☐           |
| Foi aplicada uma metodologia estruturada com STRIDE como baseline?                                    | ☐           |
| Os sistemas que tratam dados pessoais aplicam LINDDUN sobre o mesmo DFD?                               | ☐           |
| Cada ameaça tem disposição formal explícita (mitigado, aceite, transferido ou excluído) com owner nomeado? | ☐           |
| Cada risco aceite tem justificação documentada, aprovação formal e prazo de reavaliação?              | ☐           |
| Existe rastreabilidade verificável ameaça → requisito → backlog → validação com threat ID referenciado? | ☐           |
| O threat model está versionado e foi atualizado no prazo definido (≤30 dias após trigger ou por release), com gate de frescura no CI/CD? | ☐           |
| O threat model foi revisto por AppSec independente antes do go-live (L2+), com evidência?             | ☐           |
| Os sistemas com componentes AI/ML têm threat model estendido (prompt injection, model poisoning) referenciado a MITRE ATLAS ou NIST AI 100-2? | ☐           |
| Os agentes de IA com uso de tools têm DFD agentic e threat library citada por ID canónico ancorada a controlos? | ☐           |
| Foram derivados abuse/misuse cases e integrados no backlog como requisitos rastreáveis?               | ☐           |
| O threat model foi validado e aprovado por um responsável explícito, distinto dos artefactos de apoio? | ☐           |
| Os artefactos de threat modeling têm controlo de acesso, classificação e retenção definidos?          | ☐           |
| As ameaças foram priorizadas por impacto de negócio e essa priorização reflete-se no backlog?         | ☐           |

---

## 🔄 Integração Operacional

- Este checklist pode ser integrado em **revisões de arquitetura, gates de release, pipelines CI/CD ou sessões de planeamento de sprint.**
- Cada item deve ser validado com **evidência objetiva**: modelos DFD, ficheiros STRIDE, comentários em PRs, links para requisitos no backlog, registos de sessões, etc.

> ⚠️ Em caso de resposta negativa, deve existir exceção formal documentada, com owner e prazo de reavaliação, conforme o modelo do Cap. 2.

---

## ✅ Conformidade e KPI

- A validação deste checklist permite declarar **conformidade com o Capítulo 3 - Threat Modeling**.
- A contagem de respostas afirmativas pode ser usada para **medir o grau de adoção das práticas prescritas**.
- Este resultado pode ser agregado por equipa, domínio ou organização como **indicador de maturidade e cobertura de risco**.

> 📌 Este mecanismo operacional está alinhado com o modelo de rastreabilidade e controlo contínuo definido no SbD-ToE.
