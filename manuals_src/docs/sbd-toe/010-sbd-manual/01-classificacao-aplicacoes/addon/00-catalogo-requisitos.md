---
id: catalogo-requisitos-classificacao
title: Catálogo de Requisitos de Classificação de Aplicações
description: Catálogo canónico de requisitos de classificação de criticidade aplicacional (CLA-001 a CLA-008), com aplicabilidade por nível de risco e critérios de aceitação para classificação formal, reclassificação, risco residual e proporcionalidade de controlos.
requirement_class: dominio
tags: [tipo:catalogo, classe:dominio, tema:classificacao, CLA, classificacao, reclassificacao, risco-residual, proporcionalidade, inventario, L1, L2, L3, auditoria]
sidebar_position: 0
---

<!--template: sbdtoe-addon -->

# Catálogo de Requisitos de Classificação de Aplicações

## Âmbito: a classificação como controlo fundacional de proporcionalidade

Este catálogo cobre os **requisitos de classificação de criticidade aplicacional** — os controlos que determinam com que rigor, frequência e profundidade a segurança é aplicada em cada projecto ou aplicação.

A classificação não é uma etiqueta administrativa: é o mecanismo que activa o conjunto de controlos proporcionais ao risco real. Uma aplicação mal classificada tem os controlos errados — tipicamente insuficientes — e essa lacuna é invisível até ao incidente.

Os requisitos CLA são verificáveis: a existência de uma classificação aprovada, de critérios de reclassificação documentados, de um ciclo de revisão activo e de risco residual com TTL são factos auditáveis. A ausência de evidência equivale a ausência de controlo.

Para o mapeamento completo de todos os catálogos de requisitos do SbD-ToE por domínio técnico, prefixo canónico e responsável, consultar [Cap. 02 - Mapeamento de Catálogos](/sbd-toe/sbd-manual/requisitos-seguranca/addon/lista-requisitos-base#mapeamento-de-catalogos).

> **Sobre a curadoria:** Consolidado a partir de NIST SSDF, NIST SP 800-30, ISO/IEC 27001, ISO/IEC 27005, OWASP SAMM v2.1, OWASP DSOMM, BSIMM13 e práticas de governação aplicacional orientadas a risco. Deve ser adaptado ao modelo organizacional de risco, mas sem perder a rastreabilidade para L1, L2 e L3.

Para instanciação em projecto e nomenclatura operacional (`SEC-Lx-CLA-CODIGO`), ver [Taxonomia e Rastreabilidade](/sbd-toe/sbd-manual/requisitos-seguranca/addon/taxonomia-rastreabilidade).

---

## Convenções

| Símbolo | Significado |
|---------|-------------|
| ✔ | Requisito obrigatório para este nível |
| - | Não aplicável ou não obrigatório a este nível |

Os níveis são cumulativos: L3 inclui todos os requisitos de L1 e L2; L2 inclui todos os de L1.

---

## Catálogo CLA - Classificação de Aplicações

Requisitos que garantem que cada aplicação tem uma classificação de criticidade formal, proporcional ao risco real, actualizada e utilizada como base de selecção de controlos.

| ID | Nome | L1 | L2 | L3 | Critério de aceitação |
|----|------|:--:|:--:|:--:|----------------------|
| CLA-001 | Classificação formal segundo o modelo de eixos de risco | ✔ | ✔ | ✔ | Cada aplicação tem classificação de criticidade formalizada segundo os eixos de exposição, sensibilidade de dados e impacto de incidente; a classificação está documentada, aprovada pelo owner de segurança e registada em inventário ou ferramenta GRC; é utilizada como entrada directa para selecção de controlos e gates de pipeline. |
| CLA-002 | Aprovação proporcional ao nível de risco atribuído | ✔ | ✔ | ✔ | A classificação de cada aplicação é aprovada pela entidade proporcional ao risco: L1 pelo tech lead ou equivalente, L2 pelo AppSec referente da equipa, L3 pelo CISO ou equivalente; a aprovação é documentada, datada e rastreável ao responsável. |
| CLA-003 | Activação de controlos base determinada pela classificação | ✔ | ✔ | ✔ | O nível de classificação determina o conjunto de controlos base obrigatórios — incluindo gates de CI/CD, requisitos de testes, frequência de revisões e obrigações de monitorização; a activação dos controlos é verificável por rastreabilidade entre a classificação e o pipeline ou backlog actuais. |
| CLA-004 | Critérios de reclassificação documentados e monitorizados | ✔ | ✔ | ✔ | Existem critérios explícitos de reclassificação documentados: novos fluxos de dados sensíveis, integração com sistemas de maior criticidade, exposição a novos contextos regulatórios, incidente de segurança relevante ou mudança de modelo de ameaça; cada critério tem trigger de revisão associado. |
| CLA-005 | Ciclo periódico de revisão de classificação diferenciado por nível | ✔ | ✔ | ✔ | Aplicações L1 revistas anualmente, L2 semestralmente, L3 trimestralmente; cada revisão produz evidência rastreável com data, revisor e conclusão; em caso de manutenção da classificação, a justificação é documentada; revisão em atraso é tratada como não conformidade activa. |
| CLA-006 | Reavaliação de classificação após evento de mudança significativa | ✔ | ✔ | ✔ | Após mudança significativa — nova integração crítica, alteração de exposição, incidente de segurança ou alteração regulatória relevante — a classificação é reavaliada no prazo máximo de 30 dias; a reavaliação é rastreável ao evento que a desencadeou e ao responsável que a conduziu. |
| CLA-007 | Risco residual com compensação formalizada, owner e TTL | - | ✔ | ✔ | Quando a classificação resulta em controlos parcialmente aplicados (desvio aceite), o risco residual é documentado com compensação explícita, owner da excepção, prazo de resolução e data de expiração; excepção expirada sem renovação é tratada como não conformidade activa e reportada ao owner de segurança. |
| CLA-008 | Inventário de aplicações actualizado e acessível para auditoria | ✔ | ✔ | ✔ | Existe inventário central ou GRC com registo de cada aplicação, incluindo nível de classificação actual, data de última revisão, owner de segurança e estado de conformidade; o inventário é actualizado após cada alteração de classificação ou transferência de responsabilidade; acessível para auditoria sem preparação manual. |

---

## Notas explicativas

- **CLA-001**: A classificação multi-eixo (exposição, dados, impacto) previne a subestimação de risco de aplicações que parecem simples à superfície mas têm dados sensíveis ou impacto crítico em caso de comprometimento. Um único eixo de classificação é invariavelmente incompleto.
- **CLA-002**: A proporcionalidade na aprovação não é burocracia — é o mecanismo que confere autoridade à classificação. Uma classificação aprovada apenas pelo developer que a criou não tem força para impor controlos onerosos e não é defensável em auditoria.
- **CLA-003**: Sem activação explícita de controlos proporcional à classificação, o nível atribuído é meramente decorativo. Este requisito fecha a ligação entre a decisão de classificação e as consequências operacionais que dela decorrem.
- **CLA-004 e CLA-005**: A distinção é operacionalmente relevante: CLA-004 verifica que existem gatilhos de reclassificação activos (classificação responde a eventos); CLA-005 verifica que existe um ciclo proactivo independente de eventos (classificação é revisitada mesmo em ausência de incidentes ou mudanças). Ambos são necessários.
- **CLA-006**: O prazo de 30 dias para reavaliação após evento significativo é propositadamente conservador — suficiente para uma avaliação rigorosa, mas curto o bastante para prevenir classificações desactualizadas em aplicações que mudaram de perfil de risco. Para L3, o prazo pode ser mais restritivo por política organizacional.
- **CLA-007**: O risco residual documentado com TTL serve dois propósitos: informa o owner da lacuna existente e cria um compromisso de resolução com data. A ausência de TTL converte uma excepção temporária num desvio permanente invisível.
- **CLA-008**: O inventário é o artefacto de evidência primário em auditorias de conformidade. Um inventário actualizável manualmente mas não actualizado de facto equivale a ausência de inventário para fins de auditoria.

---

> Para o modelo formal de classificação por eixos, consultar [Modelo de Classificação por Eixos](./modelo-classificacao-eixos).
> Para o ciclo de vida do risco associado à classificação, consultar [Ciclo de Vida do Risco](./ciclo-vida-risco).
> Para critérios de aceitação de risco por nível, consultar [Critérios de Aceitação de Risco](./criterios-aceitacao-risco).
> Para gestão de risco residual, consultar [Risco Residual](./risco-residual).
> Para activação de controlos base por nível de risco, consultar [Matriz de Controlos por Risco](./matriz-controlos-por-risco).
> Para KPIs e métricas de classificação, consultar [KPIs e Métricas de Classificação](./12-kpis-metricas.md).
