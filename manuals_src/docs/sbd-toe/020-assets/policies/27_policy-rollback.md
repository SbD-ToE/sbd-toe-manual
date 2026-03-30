---
id: policy-rollback
title: Política de Rollback
description: Política organizacional que define os requisitos para a capacidade de rollback de deploys em produção, incluindo tipos de rollback por componente (binário, configuração, base de dados, infraestrutura), critérios de activação, RTO por nível de criticidade, procedimentos de teste periódico e rastreabilidade, proporcional ao nível de criticidade (L1, L2, L3).
tags: [policy, rollback, reversão, deploy, RTO, base de dados, infraestrutura, resiliência, cap11, L1, L2, L3, governance]
grupo: pipeline-entrega
sidebar_position: 27
---

# Política de Rollback

## 1. Objetivo

Esta política define os requisitos para a **capacidade de rollback de deploys em produção** - a capacidade de reverter, de forma controlada e verificável, uma versão de software ou de infraestrutura para o estado anterior em caso de incidente, regressão ou anomalia detectada pós-deploy.

Rollback não é um plano de contingência de última instância - é um requisito de resiliência que deve ser planeado, implementado e testado antes de ser necessário. A diferença entre uma crise e uma resolução controlada está frequentemente na capacidade de reverter em minutos em vez de horas. Sem rollback testado, cada deploy em produção acumula risco operacional que só se materializa no pior momento possível.

O objetivo desta política é garantir que:

- A capacidade de rollback está disponível antes de qualquer deploy em produção
- O RTO de rollback é definido e testado periodicamente por nível de criticidade
- Os diferentes tipos de rollback (binário, configuração, BD, infraestrutura) têm procedimentos específicos
- O rollback é executado de forma controlada e deixa evidência auditável

---

## 2. Âmbito e obrigatoriedade

| Nível | Obrigatoriedade |
|---|---|
| L1 | Recomendado; rollback manual documentado; versão anterior disponível |
| L2 | Obrigatório; rollback automatizado para binários e configuração; testado trimestralmente |
| L3 | Obrigatório; rollback automatizado para todos os tipos; testado trimestralmente; RTO ≤ 15 minutos |

---

## 3. Tipos de rollback e requisitos específicos

### 3.1 Rollback de binário (aplicação/imagem)

O tipo mais frequente e geralmente o mais simples - reverter para a versão anterior do artefacto:

| Requisito | L1 | L2 | L3 |
|---|---|---|---|
| Versão anterior disponível no registo (sem expiry imediato) | Obrigatório | Obrigatório | Obrigatório |
| Rollback via pipeline (não manual) | Recomendado | Obrigatório | Obrigatório |
| RTO | Sem definição | ≤ 30 minutos | ≤ 15 minutos |

### 3.2 Rollback de configuração

Alterações de configuração (variáveis de ambiente, feature flags, configurações de serviço) devem ser reversíveis:

- [ ] Configurações versionadas (Git, ConfigMap, sistema de configuração centralizado)
- [ ] Versão anterior da configuração identificável e aplicável sem rebuild
- [ ] Rollback de configuração independente do rollback de binário (podem ser executados separadamente)
- [ ] Feature flags como mecanismo de rollback funcional sem novo deploy

### 3.3 Rollback de base de dados

O rollback de alterações de base de dados é o mais complexo e o com maior risco de perda de dados:

| Requisito | L1 | L2 | L3 |
|---|---|---|---|
| Migrações de BD reversíveis (down migration disponível) | Recomendado | Obrigatório | Obrigatório |
| Snapshot/backup pré-deploy disponível | Recomendado | Obrigatório | Obrigatório |
| Verificação de consistência após rollback de BD | Recomendado | Obrigatório | Obrigatório |
| Plano documentado para alterações destrutivas (sem down migration possível) | Recomendado | Obrigatório | Obrigatório |

:::warning
Alterações de BD destrutivas (remoção de colunas, tabelas, mudança de tipos) são irreversíveis sem perda de dados. Devem ser planeadas em múltiplas fases: primeiro deprecar/ignorar, depois remover em release posterior. A remoção directa sem fase de transição proíbe rollback sem perda de dados.
:::

### 3.4 Rollback de infraestrutura (IaC)

A reversão de alterações de infraestrutura (IaC) deve seguir o mesmo processo de aprovação que o apply original:

- [ ] Estado IaC anterior disponível no histórico de versões
- [ ] Plan de rollback gerado e revisto antes de apply reverso
- [ ] Rollback de IaC executado via pipeline, não manualmente
- [ ] Snapshot do estado real de infraestrutura pré-alteração disponível em L3

---

## 4. Critérios de activação de rollback

O rollback deve ser activado quando um dos seguintes critérios é verificado após o deploy:

| Critério | Threshold de activação |
|---|---|
| Taxa de erros HTTP 5xx | > threshold definido (ex: > 1% durante 5 minutos) |
| Latência de resposta (P99) | > threshold definido (ex: > 2x baseline durante 10 minutos) |
| Health check de produção | Falha persistente em ≥ 2 instâncias/pods |
| Alerta de segurança | Anomalia de segurança detectada por monitorização de runtime |
| Crash loop | Container em restart loop após deploy |
| Rollback manual solicitado | Decisão humana explícita do Tech Lead ou On-Call |

Os thresholds devem ser documentados, versionados e revistos periodicamente.

---

## 5. Processo de rollback

### 5.1 Rollback automático

Em L2/L3, o rollback deve ser iniciado automaticamente quando os critérios de activação são atingidos durante uma janela de observação pós-deploy:

1. Sistema de monitorização detecta violação do critério de saúde
2. Alerta gerado com identificação do deployment afectado
3. Rollback iniciado automaticamente para a versão anterior do binário
4. Confirmação de estado de saúde após rollback
5. Notificação à equipa com detalhes da reversão

### 5.2 Rollback manual

Quando o rollback é iniciado por decisão humana (fora da janela automática ou para tipos não cobertos pelo rollback automático):

1. Decisão documentada (quem decidiu, quando, com que base)
2. Versão de destino identificada
3. Rollback executado via pipeline (não directamente na plataforma)
4. Verificação de saúde pós-rollback
5. Registo da execução com evidência

---

## 6. RTO de rollback por nível

| Nível | RTO alvo (rollback de binário) | RTO alvo (rollback de BD simples) |
|---|---|---|
| L1 | Sem definição formal | Sem definição formal |
| L2 | ≤ 30 minutos | ≤ 60 minutos |
| L3 | ≤ 15 minutos | ≤ 30 minutos |

O RTO deve ser medido a partir da detecção do problema até ao serviço estar disponível na versão anterior com estado de saúde verificado.

---

## 7. Teste periódico de rollback

A capacidade de rollback deve ser testada periodicamente - um rollback não testado é uma capacidade teórica, não operacional:

| Nível | Cadência mínima | Âmbito do teste |
|---|---|---|
| L1 | Anual | Rollback de binário em staging |
| L2 | Trimestral | Rollback de binário + configuração em staging |
| L3 | Trimestral | Rollback de todos os tipos em staging; RTO medido e documentado |

Os resultados dos testes devem ser documentados, incluindo:

- [ ] RTO efectivo medido
- [ ] Problemas encontrados e acções correctivas
- [ ] Comparação com RTO alvo definido
- [ ] Aprovação de que a capacidade está operacional

---

## 8. Rastreabilidade de rollbacks

Cada rollback executado em produção deve produzir evidência auditável:

| Artefacto | Conteúdo |
|---|---|
| Log de rollback | Timestamp, versão origem, versão destino, trigger, executor |
| Estado de saúde pós-rollback | Resultado dos health checks após reversão |
| Registo de decisão | Quem decidiu, quando, com que informação disponível |
| Incidente associado | Referência ao incidente que motivou o rollback |

---

## 9. Responsabilidades

| Role | Responsabilidade |
|---|---|
| DevOps / SRE | Configurar e manter capacidade de rollback automático; executar testes periódicos; documentar procedimentos |
| Developer | Garantir que migrações de BD têm down migration; testar rollback em staging antes de deploy em produção |
| Tech Lead / On-Call | Tomar decisão de rollback manual quando necessário; registar a decisão |
| AppSec Engineer | Verificar que o processo de rollback não compromete controlos de segurança |
| GRC / Compliance | Auditar registos de rollback; verificar que RTOs são cumpridos nos testes |

---

## 10. Revisão e auditoria desta política

Esta política deve ser **revista anualmente** ou após qualquer um dos seguintes eventos:

- Incidente em que o rollback falhou ou excedeu o RTO alvo
- Alteração da plataforma de deploy que afecte a capacidade de rollback
- Alteração de arquitectura que introduza novos tipos de estado (ex: nova base de dados, novo sistema de mensagens)

---

## 11. Referências normativas e técnicas

| Referência | Relevância |
|---|---|
| SbD-ToE Cap. 11 - Deploy Seguro | US-04 (rollback rápido e testado), US-12 (rollback estruturado por tipo) |
| Política de Deploy Seguro (`25_policy-deploy-seguro.md`) | Estratégias de deploy progressivo e rollback automático |
| Política de Monitorização Pós-Deploy (`28_policy-monitorizacao-pos-deploy.md`) | Critérios de activação de rollback por monitorização |
| ISO/IEC 22301 | Business Continuity Management - RTO e RPO |
| NIST SP 800-61 | Computer Security Incident Handling Guide |
| Site Reliability Engineering (Google SRE Book) | Práticas de rollback e error budget |
