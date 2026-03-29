---
id: catalogo-requisitos-arquitetura
title: Catálogo de Requisitos de Arquitectura Segura
description: Catálogo canónico de requisitos de segurança estruturais e de design (ARC-001 a ARC-013), organizados por nível de risco, com critérios de aceitação para revisão de arquitectura, ADRs e auditorias técnicas.
requirement_class: dominio
tags: [tipo:catalogo, classe:dominio, tema:arquitetura, ARC, rastreabilidade, L1, L2, L3, threat-modeling, zonas-de-confianca, ADR, auditoria]
sidebar_position: 1
---

<!--template: sbdtoe-addon -->

# Catálogo de Requisitos de Arquitectura Segura

## Âmbito: requisitos estruturais e de design

Este catálogo cobre **requisitos de segurança que se aplicam à concepção, documentação e revisão da arquitectura do sistema** — as propriedades estruturais que devem estar garantidas antes e independentemente da implementação. Incluem-se: definição de zonas de confiança, minimização da superfície de exposição, documentação de decisões de design, integração de threat modeling no processo de arquitectura, padrões reutilizáveis aprovados e versionamento de diagramas.

Para o mapeamento completo de todos os catálogos de requisitos do SbD-ToE por domínio técnico, prefixo canónico e responsável, consultar [Cap. 02 — Mapeamento de Catálogos](/sbd-toe/sbd-manual/requisitos-seguranca/addon/lista-requisitos-base#mapeamento-de-catalogos).

Os requisitos aqui definidos são avaliados em **revisões de arquitectura**, na aprovação de decisões estruturais e em auditorias técnicas — não em testes de runtime nem em pipelines de CI/CD.

> **Sobre a curadoria:** Este catálogo foi consolidado a partir de práticas reconhecidas — NIST SSDF, OWASP SAMM, ISO/IEC 27001, threat modeling frameworks (STRIDE, PASTA) e práticas de arquitectura segura. Deve ser adaptado ao contexto organizacional e revisto com cada ciclo de arquitectura significativo.

Para a instanciação em projecto e a nomenclatura operacional de rastreabilidade (`SEC-Lx-ARC-CODIGO`), ver [Taxonomia e Rastreabilidade](/sbd-toe/sbd-manual/requisitos-seguranca/addon/taxonomia-rastreabilidade).

---

## Convenções

| Símbolo | Significado |
|---------|-------------|
| ✔ | Requisito obrigatório para este nível |
| — | Não aplicável ou não obrigatório a este nível |

Os níveis são cumulativos: L3 inclui todos os requisitos de L1 e L2; L2 inclui todos os de L1.

---

## Catálogo ARC — Arquitectura Segura

Requisitos que garantem que o sistema é concebido, documentado e revisto com controlos estruturais proporcionais ao seu nível de risco.

| ID | Nome | L1 | L2 | L3 | Critério de aceitação |
|----|------|:--:|:--:|:--:|----------------------|
| ARC-001 | Zonas de confiança identificadas e documentadas | ✔ | ✔ | ✔ | Diagrama com zonas de confiança delimitadas, identificadas e justificadas; versionado em repositório; revisto na última revisão de arquitectura. |
| ARC-002 | Exposição externa minimizada e justificada | ✔ | ✔ | ✔ | Inventário de componentes expostos externamente; cada exposição acompanhada de justificação técnica e controlo associado (gateway, proxy, WAF, ACL). |
| ARC-003 | Revisão de arquitectura com foco em segurança | — | ✔ | ✔ | Registo formal de revisão (ata, checklist ou relatório AppSec) com data, participantes e decisões; proporcional ao nível de risco da aplicação. |
| ARC-004 | Decisões de arquitectura documentadas | — | ✔ | ✔ | ADR (Architecture Decision Record) ou equivalente para cada decisão estrutural significativa; campos: responsável, data, alternativas consideradas e justificação. |
| ARC-005 | Threat modeling integrado nos fluxos críticos | — | ✔ | ✔ | Resultado de threat modeling disponível com ameaças identificadas, fluxos de dados críticos cobertos e mitigações registadas; ligado ao diagrama de arquitectura. |
| ARC-006 | Controlos técnicos de isolamento entre domínios sensíveis | ✔ | ✔ | ✔ | Evidência de isolamento activo entre domínios sensíveis: políticas de rede, firewalls lógicos ou segmentação de APIs; testável e auditável. |
| ARC-007 | Padrões de arquitectura reutilizáveis e aprovados | — | ✔ | ✔ | Repositório de padrões aprovados com data de última revisão; evidência de uso de padrão aprovado registada em revisão de arquitectura. |
| ARC-008 | Fluxos de dados entre zonas de confiança protegidos | ✔ | ✔ | ✔ | Diagrama de fluxo de dados (DFD) com controlos explícitos em cada fronteira de confiança; actualizado e versionado. |
| ARC-009 | Alterações significativas desencadeiam nova revisão | — | ✔ | ✔ | Processo documentado que define o limiar de "alteração significativa"; evidência de revisão executada após a última alteração que atingiu esse limiar. |
| ARC-010 | Diagramas de arquitectura versionados e acessíveis | ✔ | ✔ | ✔ | Diagrama no repositório com histórico de versões; acessível às equipas relevantes; revisto pelo menos anualmente ou por release significativo. |
| ARC-011 | Segmentação lógica e física entre ambientes | — | — | ✔ | Evidência de segregação de rede, permissões e identidade entre dev, staging e prod; documentada e verificável. |
| ARC-012 | Critérios formais de aprovação para aplicações de risco elevado | — | — | ✔ | Checklist formal de aprovação preenchido e assinado por responsável de segurança; registo de aprovação anterior ao deploy em produção. |
| ARC-013 | Validação automática de topologia em CI/CD ou como código | — | — | ✔ | Job de CI com output de validação de topologia (ex: Cartography, diagramas-como-código, checkov para topologia); logs de execução disponíveis. |

---

## Notas explicativas

- **ARC-003**: A revisão pode ser feita com checklist estruturado, peer review de arquitectura ou workshop de AppSec; o formato é proporcional à complexidade da aplicação.
- **ARC-005**: O threat modeling neste contexto é aplicado como instrumento de revisão de arquitectura — complementar ao processo autónomo de threat modeling descrito no Cap. 03.
- **ARC-009**: Define-se "alteração significativa" como qualquer mudança que afecte fronteiras de confiança, fluxos de dados críticos, exposição externa ou decisões de isolamento documentadas.
- **ARC-011**: Aplica-se tanto a isolamento de rede (VLANs, namespaces, peering policies) como a isolamento de identidade (IAM policies, service accounts distintas, sem cross-env credentials).
- **ARC-013**: Ferramentas de exemplo: validação de diagramas `.drawio` como código, Cartography para análise de grafo de infra, ou verificações de topologia em pipelines Terraform/Pulumi.

---

> Para critérios de validação por requisito, método e papel responsável, consultar o [Plano de Validação Arquitetural](./validacao).
> Para rastreabilidade entre requisitos, decisões e evidência, consultar [Rastreabilidade Arquitetural](./rastreabilidade).
> Para gestão de excepções a estes requisitos, consultar [Gestão de Excepções](./excecoes).
