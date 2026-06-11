---
id: checklist-revisao
title: Checklist de Revisão - Arquitetura Segura
description: Lista de verificação binária e auditável para controlo da aplicação dos requisitos de arquitetura segura
tags: [checklist, arquitetura, validação, requisitos]
sidebar_position: 20
sidebar_label: Checklist de Revisão
---

# Checklist de Revisão - Arquitetura Segura

Este checklist aplica-se a todas as aplicações avaliadas segundo os critérios definidos neste capítulo.
Serve como instrumento de verificação binária e auditável da **adoção prática das prescrições de arquitetura segura**, permitindo:

- Controlo contínuo da aplicação dos requisitos `ARC-001` a `ARC-015`
- Verificação por projeto em momentos-chave do ciclo de vida
- Geração de indicadores operacionais agregáveis por equipa ou organização

> 🗓️ **Deve ser revisto a cada release ou alteração arquitetónica significativa**, conforme indicado na `aplicacao-lifecycle`.

---

## 📋 Itens de Verificação

| Item                                                                                                                        | Verificado? |
|-----------------------------------------------------------------------------------------------------------------------------|-------------|
| As zonas de confiança estão delimitadas, justificadas e documentadas em diagrama versionado? (`ARC-001`)                   | ☐           |
| Os componentes expostos externamente estão inventariados, cada um com justificação técnica e controlo de fronteira (gateway, WAF, ACL)? (`ARC-002`) | ☐           |
| Existe registo formal da revisão de arquitetura com foco em segurança (data, participantes, decisões)? (`ARC-003`)         | ☐           |
| As decisões estruturais significativas estão documentadas em ADR (contexto, alternativas, trade-offs, responsável)? (`ARC-004`) | ☐           |
| Foi realizado threat modeling dos fluxos críticos, arquivado e ligado ao diagrama? (`ARC-005`)                            | ☐           |
| Existem controlos técnicos de isolamento entre domínios sensíveis, testáveis e auditáveis? (`ARC-006`)                     | ☐           |
| Foram usados apenas padrões arquitetónicos aprovados, ou a não-adesão foi justificada formalmente? (`ARC-007`)             | ☐           |
| Os fluxos de dados entre zonas estão representados num DFD com controlo explícito em cada fronteira, versionado? (`ARC-008`) | ☐           |
| Existe limiar documentado de "alteração significativa" e evidência de revisão após a última que o atingiu? (`ARC-009`)     | ☐           |
| Os diagramas estão versionados, acessíveis e revistos há ≤12 meses ou no último release significativo? (`ARC-010`)         | ☐           |
| Para aplicações L3, existe segregação de rede, permissões e identidade entre dev, staging e produção? (`ARC-011`)          | ☐           |
| Para aplicações L3, existe checklist formal de aprovação assinado por responsável de segurança antes do deploy? (`ARC-012`) | ☐           |
| Para aplicações L3, a topologia é validada automaticamente em CI/CD, com bloqueio de promoção em falha? (`ARC-013`)        | ☐           |
| Os sistemas com componentes AI/ML têm trust boundaries explícitas (training/inference/agentic), controlos anti-prompt-injection (input/output) e proveniência de modelos/datasets, figurando a IA como participante distinto? (`ARC-014`) | ☐           |
| Cada agente de IA com uso de tools opera com identidade dedicada efémera e scope mínimo por tool e ambiente, sem reuso de credenciais humanas? (`ARC-015`) | ☐           |
| Em autonomia A2+, existe intent declaration em audit antes de tool-call destrutivo, aprovação humana out-of-band, kill-switch exercitado e audit por tool invocation integrado com o Cap. 12? (`ARC-015`) | ☐           |
| Existe rastreabilidade requisito ARC → ameaça → decisão/ADR → controlo → evidência, com exceções aprovadas (compensação, owner, sunset)? | ☐           |

---

## 📌 Notas de Aplicação Prática

- Este checklist **deve ser integrado** em tarefas de sprint, gates de release ou revisões técnicas regulares.
- Deve ser usado como **instrumento de controlo e reporting operacional** por equipas de arquitetura, segurança e auditoria.
- Todos os campos devem ser validados com **evidência objetiva** (ex: ficheiros versionados, comentários de PR, ligações internas).

> ⚠️ Em caso de resposta negativa, deve existir exceção formal aprovada (ver `ARC-011`).

---

## 📊 Conformidade e KPI

- A validação deste checklist permite declarar **conformidade com o Capítulo 04 - Arquitetura Segura**.
- Os resultados por projeto podem ser **agregados para efeitos de medição de maturidade e rastreabilidade organizacional**.
- Este mecanismo pode ser integrado em **dashboards, métricas de equipa e processos de auditoria contínua**.

> ✅ Este instrumento está alinhado com a lógica de controlo contínuo definida no modelo SbD-ToE.
