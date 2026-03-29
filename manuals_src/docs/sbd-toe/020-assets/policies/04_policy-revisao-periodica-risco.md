---
id: policy-revisao-periodica-risco
title: Política de Revisão Periódica de Risco
description: Política organizacional que define a cadência obrigatória e os triggers de revisão da classificação de risco aplicacional, assegurando que o nível de criticidade e os controlos associados se mantêm adequados ao contexto técnico e de negócio ao longo de todo o ciclo de vida da aplicação.
tags: [policy, revisão periódica, risco, classificação, cap01, cap14, cadência, triggers, event-based, time-based, L1, L2, L3, governance]
sidebar_position: 4
---

# Política de Revisão Periódica de Risco

## 1. Objetivo

Esta política define os mecanismos obrigatórios de revisão da classificação de risco aplicacional e dos controlos de segurança associados, ao longo de todo o ciclo de vida de cada aplicação.

A classificação de risco não é um ato pontual de onboarding — é um estado dinâmico que deve ser mantido atualizado. Alterações técnicas, de negócio ou regulatórias podem modificar a exposição, os dados tratados ou o impacto potencial de um incidente, sem que isso seja imediatamente visível. Sem revisão estruturada, a classificação envelhece silenciosamente e os controlos aplicados deixam de ser proporcionais ao risco real.

Esta política estabelece dois mecanismos complementares de revisão:

- **Time-based** — revisão com cadência periódica fixa, independente de alterações
- **Event-based** — revisão despoletada por eventos técnicos ou de negócio relevantes

---

## 2. Âmbito

Esta política aplica-se a **todas as aplicações com classificação de risco ativa** (L1, L2 ou L3), independentemente do estado de desenvolvimento (em construção, em produção, em manutenção ou em descontinuação).

Aplicações em processo de descomissionamento mantêm a obrigação de revisão até à sua desativação formal e registo de encerramento.

---

## 3. Revisão time-based — cadência periódica

### 3.1 Cadências mínimas obrigatórias

| Nível | Cadência mínima | Obrigatoriedade |
|---|---|---|
| L1 | Anual (12 meses) | Recomendado |
| L2 | Semestral (6 meses) | Obrigatório |
| L3 | Trimestral (3 meses) | Obrigatório |

A data da próxima revisão deve ser registada no documento de classificação no momento de cada revisão. A ausência de data de revisão agendada é tratada como incumprimento.

### 3.2 O que avaliar em cada revisão periódica

- [ ] Reavaliação dos três eixos E, D e I com base no estado atual da aplicação
- [ ] Verificação de alterações técnicas ocorridas desde a última revisão (novas integrações, mudanças de exposição, novos tipos de dados)
- [ ] Verificação de alterações de negócio com impacto potencial no nível de risco
- [ ] Revisão do estado dos controlos aplicados e da sua adequação ao nível atual
- [ ] Revisão dos riscos residuais aceites e da sua validade
- [ ] Decisão documentada: manter nível / alterar nível
- [ ] Agendamento da próxima revisão

### 3.3 Resultado da revisão periódica

| Decisão | Ação |
|---|---|
| Nível mantido | Registar reavaliação com data, responsável e justificação; agendar próxima revisão |
| Nível elevado | Atualizar classificação; rever controlos obrigatórios; comunicar às equipas; obter aprovação |
| Nível reduzido | Atualizar classificação com justificação técnica detalhada; obter aprovação AppSec |

:::warning
A redução de nível de criticidade requer justificação técnica rigorosa e aprovação de AppSec Engineer. Não é aceitável reduzir o nível com base apenas em razões de conveniência operacional ou para reduzir o esforço de conformidade.
:::

---

## 4. Revisão event-based — triggers obrigatórios

### 4.1 Triggers que obrigam a revisão imediata

A revisão da classificação deve ser despoletada **imediatamente** (no prazo máximo de 5 dias úteis) quando ocorra qualquer um dos seguintes eventos:

| Trigger | Descrição |
|---|---|
| Nova integração externa | Ligação a sistema externo, API de terceiro, ou serviço cloud não previsto anteriormente |
| Novo tipo de dado sensível | Início de tratamento de PII, dados regulados, dados de saúde, dados financeiros |
| Alteração de exposição | Abertura de novo endpoint público, autenticação removida, novo canal de acesso |
| Alteração de arquitetura significativa | Mudança de modelo de deployment, migração de infraestrutura, adição de componente crítico |
| Introdução de automação ou IA | Quando modifica exposição, dados tratados ou impacto de decisões |
| Incidente de segurança relevante | Qualquer incidente que evidencie desalinhamento entre o nível classificado e o risco real |
| Alteração regulatória aplicável | Nova obrigação legal ou normativa com impacto na classificação |
| Mudança de modelo de negócio | Alteração do público-alvo, jurisdição ou propósito da aplicação |

### 4.2 Triggers que recomendam revisão

Os seguintes eventos não obrigam a revisão imediata, mas devem ser avaliados pela equipa como potenciais triggers:

- Alteração significativa no volume de dados tratados
- Adição de novos perfis de utilizador com diferentes níveis de acesso
- Mudança de equipa responsável ou de owner de segurança
- Resultados de pentest que evidenciem exposição não prevista na classificação

### 4.3 Processo de revisão event-based

1. **Identificar o trigger** — documentar o evento que originou a revisão
2. **Avaliar o impacto** nos eixos E, D e I
3. **Determinar se o nível deve ser alterado**
4. **Documentar a decisão** com justificação técnica clara
5. **Obter aprovação** pela alçada adequada ao nível resultante
6. **Atualizar** o documento de classificação e comunicar às equipas
7. **Reiniciar o calendário** de revisão periódica com base no novo nível

---

## 5. Deteção assistida por ferramentas

A organização pode utilizar ferramentas automatizadas para deteção de eventos que possam constituir triggers de revisão (ex: análise de commits, PRs, alterações de configuração).

Quando uma ferramenta propõe reclassificação ou alerta para uma potencial alteração relevante:

- O alerta deve ser avaliado por um AppSec Engineer antes de qualquer decisão
- Atualizações de patch em dependências **não constituem**, por si só, trigger de revisão
- Alterações minor/major em dependências críticas **devem ser avaliadas**
- A decisão final é sempre **humana** — a ferramenta sinaliza, não decide

---

## 6. Documentação obrigatória de cada revisão

Cada revisão (periódica ou event-based) deve produzir um registo com:

- [ ] Data da revisão
- [ ] Tipo de revisão (time-based / event-based)
- [ ] Trigger (para event-based) ou cadência (para time-based)
- [ ] Reavaliação dos eixos E, D e I
- [ ] Decisão: nível mantido / alterado (com justificação)
- [ ] Estado dos controlos e riscos aceites verificado
- [ ] Responsável pela revisão
- [ ] Aprovação (se aplicável)
- [ ] Data da próxima revisão agendada

**Artefacto principal:** entrada no documento de classificação da aplicação (`risk-classification.md` ou equivalente), com histórico preservado de todas as revisões anteriores.

---

## 7. Integração com o ciclo de desenvolvimento

| Momento | Ação esperada |
|---|---|
| Sprint planning (L3) | Verificar se algum trigger event-based ocorreu no sprint anterior |
| Release / go-live | Confirmar que a classificação está atualizada e dentro da cadência |
| Retrospetiva de incidente | Verificar se a revisão periódica teria detetado o problema |
| Onboarding de nova equipa | Verificar data da última revisão e iniciar nova se necessário |

---

## 8. Responsabilidades

| Role | Responsabilidade |
|---|---|
| AppSec Engineer | Conduzir e aprovar revisões; monitorizar calendário de revisões por aplicação |
| Tech Lead / Developer | Identificar e reportar eventos técnicos que possam constituir triggers |
| GRC / Compliance | Monitorizar o cumprimento das cadências; emitir alertas de revisões em atraso |
| Gestão de Produto | Comunicar alterações de negócio com impacto potencial na classificação |
| CISO | Supervisionar o programa de revisão; garantir cobertura organizacional |

---

## 9. Incumprimento

A ausência de revisão dentro da cadência definida para o nível constitui incumprimento desta política e deve ser:

- Registada como não-conformidade no sistema GRC
- Escalada para AppSec Engineer e CISO
- Resolvida com revisão imediata e registo da causa do atraso

---

## 10. Revisão e auditoria desta política

Esta política deve ser **revista anualmente** ou após qualquer um dos seguintes eventos:

- Alteração do modelo de classificação SbD-ToE
- Incidente originado em classificação desatualizada
- Alteração regulatória com impacto nas cadências de revisão obrigatórias

O histórico de revisões de todas as aplicações deve ser disponibilizado em auditorias de segurança internas e externas.

---

## 11. Referências normativas e técnicas

| Referência | Relevância |
|---|---|
| SbD-ToE Cap. 01 — Classificação de Aplicações | Modelo E+D+I, cadências de revisão, triggers event-based |
| SbD-ToE Cap. 14 — Governança e Contratação | Ciclo contínuo de revisão e reavaliação de exceções |
| ISO/IEC 27001 — Cláusula 6.1 | Avaliação e tratamento de risco com revisão periódica |
| NIST SP 800-30 | Guide for Conducting Risk Assessments |
| NIST CSF — Identify (ID.RA) | Risk Assessment com revisão contínua |
| SSDF PW.1 | Definição e revisão de requisitos de segurança baseada em risco |
