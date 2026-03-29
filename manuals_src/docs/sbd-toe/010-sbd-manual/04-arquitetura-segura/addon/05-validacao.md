---
id: validacao-arquitetural
title: Plano de Validação Arquitetural
description: Critérios de validação por requisito (ARC-001 a ARC-013), com métodos, momentos e responsáveis, organizados por nível de risco
tags: [tipo:addon, tema:arquitetura, ARC, validacao, evidencia, L1, L2, L3]
sidebar_position: 5
---

<!--template: sbdtoe-addon -->

# Plano de Validação Arquitetural

Este documento define como validar cada requisito do catálogo de arquitectura segura (ARC-001 a ARC-013), especificando:

- **o que validar** — o critério concreto de conformidade;
- **como validar** — o método ou artefacto utilizado;
- **quando** — o momento no ciclo de vida em que a validação deve ocorrer;
- **responsável** — o papel que valida.

---

## Validação por Requisito

| Requisito | O que validar | Como validar | Quando | Responsável |
|-----------|---------------|--------------|--------|-------------|
| ARC-001 | Zonas de confiança identificadas e documentadas | Diagrama com zonas assinaladas, justificadas e versionado em repositório | Design inicial; após alteração de topologia ou fronteiras | Arquitecto técnico |
| ARC-002 | Exposição externa minimizada e justificada | Inventário de componentes expostos; cada exposição com controlo associado e justificação técnica documentada | Revisão de arquitectura; auditoria de exposição | AppSec, Arquitecto |
| ARC-003 | Revisão de arquitectura com foco em segurança | Registo formal de revisão (ata, checklist ou relatório AppSec) com data, participantes e decisões | Antes de release significativo; após alteração estrutural | AppSec |
| ARC-004 | Decisões de arquitectura documentadas | ADR ou equivalente com contexto, alternativas, decisão tomada, trade-offs aceites e responsável | Sempre que ocorre decisão estrutural com impacto em segurança, isolamento ou dependências | Arquitecto técnico |
| ARC-005 | Threat modeling integrado nos fluxos críticos | Resultado de threat modeling com ameaças identificadas, fluxos cobertos e mitigações registadas; ligado ao diagrama de arquitectura | Design inicial; após alteração significativa de fluxo ou componente | AppSec, Arquitecto |
| ARC-006 | Controlos técnicos de isolamento entre domínios sensíveis | Evidência de isolamento activo (políticas de rede, firewalls lógicos, segmentação de APIs); configuração testável e auditável | Revisão de arquitectura; inspecção de configuração de rede | AppSec, DevSecOps |
| ARC-007 | Padrões de arquitectura reutilizáveis e aprovados | Repositório de padrões com data de última revisão; evidência de uso de padrão aprovado registada em revisão de arquitectura | Início de projecto; introdução de novo componente estrutural | Equipa de arquitectura |
| ARC-008 | Fluxos de dados entre zonas de confiança protegidos | DFD com controlos explícitos em cada fronteira de confiança; actualizado e versionado em repositório | Design inicial; após alteração de fluxos de dados | Arquitecto, AppSec |
| ARC-009 | Alterações significativas desencadeiam nova revisão | Processo documentado com definição do limiar de "alteração significativa"; evidência de revisão executada após a última alteração relevante | Após cada alteração que atinja o limiar definido no processo | Arquitecto, PO |
| ARC-010 | Diagramas de arquitectura versionados e acessíveis | Diagrama no repositório com histórico de versões; acessível a equipas relevantes; revisto no período definido | Revisão periódica (pelo menos anual ou por release significativo) | Arquitecto, DevOps |
| ARC-011 | Segmentação lógica e física entre ambientes | Evidência de segregação de rede, permissões e identidade entre dev, staging e prod; documentada e verificável por auditoria | Revisão de infraestrutura; auditoria de permissões cross-environment | Engenharia de plataforma, AppSec |
| ARC-012 | Critérios formais de aprovação para aplicações de risco elevado | Checklist formal preenchido e assinado por responsável de segurança; registo de aprovação anterior ao deploy em produção | Gate de release para aplicações L3 | AppSec, Responsável de segurança |
| ARC-013 | Validação automática de topologia em CI/CD ou como código | Job de CI com output de validação de topologia; logs de execução disponíveis; falhas bloqueiam promoção | Por execução de pipeline; revisão periódica de cobertura | DevSecOps, Arquitecto |

---

## Aplicação por nível de risco

| Critério de validação | L1 | L2 | L3 |
|-----------------------|:--:|:--:|:--:|
| Validação informal pelo Arquitecto técnico | ✔ | ✔ | ✔ |
| Revisão formal com registo (ata, checklist ou relatório AppSec) | — | ✔ | ✔ |
| Evidência arquivada com a release | — | ✔ | ✔ |
| Actualização após alteração relevante | ✔ | ✔ | ✔ |
| Revisão por papel independente de segurança | — | — | ✔ |
| Gate formal de aprovação antes de deploy em produção | — | — | ✔ |
| Validação automática de topologia em CI/CD | — | — | ✔ |

---

## Notas

- A validação não é um acto pontual: acompanha a arquitectura ao longo do ciclo de vida. Cada *trigger* de revisão (nova integração, alteração de fluxo de dados, reclassificação de risco) deve desencadear a validação dos requisitos ARC afectados.
- Para L1, uma checklist simples verificada pelo arquitecto ou lead técnico é suficiente para os requisitos marcados como obrigatórios (ARC-001, ARC-002, ARC-006, ARC-008, ARC-010).
- ARC-003, ARC-004, ARC-005 e ARC-009 são orientados para o processo de decisão: a evidência é o registo da decisão, não apenas o diagrama final.

---

> Para o catálogo de requisitos, consultar [Catálogo de Requisitos ARC](./catalogo-requisitos).
> Para rastreabilidade requisito→decisão→evidência, consultar [Rastreabilidade Arquitetural](./rastreabilidade).
> Para gestão de excepções, consultar [Gestão de Excepções](./excecoes).
