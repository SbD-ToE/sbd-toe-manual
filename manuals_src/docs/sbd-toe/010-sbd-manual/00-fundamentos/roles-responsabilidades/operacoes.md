---
id: operacoes
title: SecOps (Operações de Segurança)
sidebar_label: 🔧 SecOps (Operações de Segurança)
description: Responsabilidades de SecOps (Operações de Segurança) no SbD-ToE
tags: [operacoes, secops, runtime, incident-response, responsabilidades]
sidebar_position: 7
---

# SecOps (Operações de Segurança)

## Visão Geral {#visão-geral}

SecOps mantém a **segurança em runtime**: deteção, alertas de segurança e resposta coordenada a incidentes.  
Responsável por **monitorização de segurança contínua**, configuração de alertas e execução de playbooks de resposta. A operação geral — disponibilidade, patching de rotina, rollback — é de [DevOps / SRE](devops-sre).

**Especializações:** SecOps (IR), também dita Resposta a Incidentes; SecOps (SOC); SecOps (Comandante de Incidente); e o on-call de segurança. O on-call de disponibilidade é de DevOps / SRE.

### Responsabilidades Principais {#responsabilidades-principais}
- Asseguram a deteção de eventos de segurança em runtime
- Acionam o patch de segurança quando uma vulnerabilidade em execução o exige
- Coordenam resposta a incidentes (Cap. 12)
- Garantem a notificação de incidentes dentro dos prazos regulatórios

### Contexto Organizacional {#contexto-organizacional}
SecOps é a **linha da frente no cumprimento de NIS2** (resposta a incidentes, notificação em 24h) e **DORA** (continuidade operacional e gestão de eventos críticos).

## Enquadramento Regulatório {#enquadramento-regulatório}

Linha da frente em:
- **NIS2**: Alerta rápido de incidentes significativos em 24h (notificação de incidente em 72h)
- **DORA**: Continuidade operacional e resiliência

---

## Atividades por Capítulo {#atividades-por-capítulo}

### Cap. 09 - Containers e Imagens {#cap-09---containers-e-imagens}
Acompanhar **vulnerabilidades em imagens em execução** e acionar o patch de segurança; a manutenção da baseline é de DevOps / SRE.

### Cap. 11 - Deploy Seguro {#cap-11---deploy-seguro}
Acionar o **rollback quando um deploy introduz um incidente de segurança**; a execução do rollback é de DevOps / SRE.

### Cap. 12 - Monitorização e Operações {#cap-12---monitorização-e-operações}
Configurar **alertas críticos com SLAs**, integrar alertas com playbooks de incident response, correlacionar eventos multi-fonte, afinar alertas para reduzir falsos positivos, coordenar resposta a incidentes e trabalhar com métricas de deteção e resposta.

**User Stories:**
- [US-03: Alertas críticos com SLAs](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle#us-03---alertas-com-slas-definidos) - Resposta atempada a incidentes
- [US-10: Playbooks de resposta a incidentes](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle#us-10---validação-e-tuning-de-alertas) - Ação rápida e coordenada
- [US-05: Correlação de eventos](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle#us-05---métricas-de-eficácia-mttdmttr) - Deteção de padrões suspeitos (com AppSec Engineer)
- [US-06: Validação e afinação de alertas](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle#us-06---classificação-e-cobertura-de-domínios-de-monitorização) - Reduzir falsos positivos (com AppSec Engineer)

### Cap. 13 - Formação e Onboarding {#cap-13---formação-e-onboarding}
Participar em **simulações de incidentes** (war room, tabletop exercises) para validar processos de resposta.

### Cap. 14 - Governança e Contratação {#cap-14---governança-e-contratação}
Documentar **incidentes e lições aprendidas**, garantindo melhoria contínua dos processos de resposta.

---

## Referências aos Capítulos {#referências-aos-capítulos}

Para contexto e enquadramento completo:

- [Cap. 09 - Containers e Imagens](/sbd-toe/sbd-manual/containers-imagens/intro)
- [Cap. 11 - Deploy Seguro](/sbd-toe/sbd-manual/deploy-seguro/intro)
- [Cap. 12 - Monitorização e Operações](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)
- [Cap. 13 - Formação e Onboarding](/sbd-toe/sbd-manual/formacao-onboarding/intro)
- [Cap. 14 - Governança e Contratação](/sbd-toe/sbd-manual/governanca-contratacao/intro)
