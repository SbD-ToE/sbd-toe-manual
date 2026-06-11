---
id: checklist-revisao
title: Checklist de Revisão - Classificação de Aplicações
sidebar_position: 20
sidebar_label: Checklist de Revisão
tags: [canon, checklist, controlo, projeto, aplicacao]
---

# Checklist de Revisão - Classificação da Criticidade Aplicacional

Este checklist aplica-se a todas as aplicações classificadas segundo os critérios definidos no **Capítulo 01 - Classificação da Criticidade Aplicacional**.
Serve como **instrumento de verificação periódica, auditoria interna e KPI operativo de maturidade**, permitindo confirmar se:

- A classificação está atualizada e justificada;
- Foram aplicados os controlos mínimos correspondentes;
- Existem evidências rastreáveis que sustentem as decisões de risco.

> 🗓️ **Recomenda-se revisão no mínimo a cada 6 meses**, ou sempre que existirem alterações relevantes (funcionalidade, dados, exposição).

---

## 📋 Itens de Verificação

| Item                                                                                               | Verificado? |
|----------------------------------------------------------------------------------------------------|-------------|
| Existe classificação de criticidade formal documentada, cobrindo os três eixos (exposição, dados, impacto)? | ☐           |
| A classificação foi aprovada pela autoridade proporcional ao nível (L1 tech lead, L2 AppSec, L3 CISO), datada e atribuída a um responsável? | ☐           |
| O nível atribuído determina e ativa os controlos mínimos, rastreáveis ao pipeline ou backlog atuais? | ☐           |
| Foi avaliado se os atributos do risco (detetabilidade, não-determinismo, delegação ou execução automática) exigem reforço para o nível superior, e aplicado quando indicado? | ☐           |
| Sempre que automação ou apoio à decisão (incl. IA) altera exposição, dados ou delegação, os eixos foram reavaliados com racional registado? | ☐           |
| Existem critérios e triggers de reclassificação documentados?                                      | ☐           |
| Após cada mudança significativa, a classificação foi reavaliada no prazo máximo definido (≤30 dias)? | ☐           |
| A classificação foi revista dentro do ciclo periódico do nível (L1 anual, L2 semestral, L3 trimestral), com evidência? | ☐           |
| As decisões de aceitação de risco verificam os critérios formais do nível (evidência suficiente; risco residual dentro do limiar L1≤9 / L2≤6 / L3≤4)? | ☐           |
| O risco residual aceite está documentado com compensação, owner e data de expiração, sem exceções expiradas por renovar? | ☐           |
| Cada risco está validado por pelo menos uma ameaça de catálogo reconhecido (STRIDE, MITRE ATT&CK ou CAPEC)? | ☐           |
| A aplicação consta de inventário central ou GRC com nível, data de revisão, owner e estado de conformidade, acessível para auditoria? | ☐           |
| A decisão de classificação está registada em repositório versionado e rastreável?                  | ☐           |
| Quando uma ferramenta participou na classificação, está registado ferramenta, versão, data e a decisão final humana? | ☐           |

---

## 🔄 Notas Finais

- Este checklist pode ser usado como **formulário digital ou template de revisão**, e integrado em pipelines, dashboards ou ferramentas de backlog.
- A validação completa permite afirmar conformidade com o Capítulo 01 - sendo uma **evidência objetiva de maturidade e controlo de segurança** no modelo SbD-ToE.
- Deve ser arquivado como registo auditável e associado ao ciclo de release correspondente.
