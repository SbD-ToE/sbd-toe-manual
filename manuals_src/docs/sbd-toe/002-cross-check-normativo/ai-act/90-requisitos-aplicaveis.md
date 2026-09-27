---
id: requisitos-aplicaveis
title: "Requisitos aplicáveis — Sistema de IA de risco elevado (AI Act)"
description: "Vista gerada: requisitos do Manual que se aplicam sob o contexto CTX-AIA-RE, por nível e grau, com os pisos que o regime eleva e a base legal de cada um."
sidebar_position: 90
tags: [cross-check, ai-act, requisitos, overlay, gerado]
sbdtoe_generated: reg-requirements-view
derived_from:
  - 010-sbd-manual/01-classificacao-aplicacoes/addon/00-catalogo-requisitos.md
  - 010-sbd-manual/02-requisitos-seguranca/addon/02-lista-requisitos-base.md
  - 010-sbd-manual/02-requisitos-seguranca/addon/09-governaca-automatismos.md
  - 010-sbd-manual/03-threat-modeling/addon/00-catalogo-requisitos.md
  - 010-sbd-manual/04-arquitetura-segura/addon/01-catalogo-requisitos.md
  - 010-sbd-manual/05-dependencias-sbom-sca/addon/00-catalogo-requisitos.md
  - 010-sbd-manual/06-desenvolvimento-seguro/addon/00-catalogo-requisitos.md
  - 010-sbd-manual/07-cicd-seguro/addon/00-catalogo-requisitos.md
  - 010-sbd-manual/08-iac-infraestrutura/addon/08-matriz-requisitos-iac.md
  - 010-sbd-manual/09-containers-imagens/addon/00-catalogo-requisitos.md
  - 010-sbd-manual/10-testes-seguranca/addon/00-catalogo-requisitos.md
  - 010-sbd-manual/11-deploy-seguro/addon/00-catalogo-requisitos.md
  - 010-sbd-manual/12-monitorizacao-operacoes/addon/00-catalogo-requisitos.md
  - 010-sbd-manual/13-formacao-onboarding/addon/00-catalogo-requisitos.md
  - 010-sbd-manual/14-governanca-contratacao/addon/00-catalogo-requisitos.md
  - 002-cross-check-normativo/_contextos-regulatorios.yaml
  - 002-cross-check-normativo/_matriz/aiact.yaml
---

# Requisitos aplicáveis: Sistema de IA de risco elevado (AI Act)

> **Página gerada** por `scripts/gen_reg_views.py` a partir dos catálogos de requisitos e de `002-cross-check-normativo/_contextos-regulatorios.yaml`. Não se edita à mão: o catálogo de cada requisito é a fonte canónica, e esta página é uma vista do overlay regulatório.

Esta página junta, para o contexto **CTX-AIA-RE**, a selecção base do Manual por nível e os **pisos** que o regime eleva, cada um com a obrigação que o fundamenta. Um contexto nunca baixa um mínimo do Manual.

## Quando se aplica {#quando-se-aplica}

O sistema de IA é de risco elevado nos termos do art. 6.º (com a qualificação jurídica anexada à declaração). Os pisos sem grau aplicam-se a sistemas de risco elevado; o grau ART50 declara-se também sozinho, para sistemas só abrangidos pelo art. 50.º. Nível L3 não equivale a risco elevado. Declara-se por aplicação.

> Reg. (UE) 2024/1689, art. 6.º, n.os 1 a 3: «os sistemas de IA a que se refere o anexo III são também considerados de risco elevado»

## Graus {#graus}

- **ART50** — Abrangido pelo art. 50.º (transparência) (declarável sozinho). Sistema de IA abrangido pelas obrigações de transparência do art. 50.º (interacção directa com pessoas singulares, conteúdo sintético, falsificações profundas), seja ou não de risco elevado.

## Pisos do contexto {#pisos}

| Piso | Alvo | Grau | Piso exigido | Âmbito | Base legal | Justificação de não aplicabilidade |
|---|---|---|---|---|---|---|
| CTX-AIA-RE-P01 | `OPS-011` | — | obrigatório | — | Reg. (UE) 2024/1689, art. 12.º, n.os 1 e 2: «Os sistemas de IA de risco elevado devem permitir tecnicamente o registo automático de eventos («registos») durante a vida útil do sistema.» (AIA-12-1, AIA-12-2) | não admitida |
| CTX-AIA-RE-P02 | `OPS-012` | — | obrigatório | Quando o sistema inclui agentes de IA com invocação de ferramentas. | Reg. (UE) 2024/1689, art. 12.º, n.os 1 e 2: «Os sistemas de IA de risco elevado devem permitir tecnicamente o registo automático de eventos («registos») durante a vida útil do sistema.» (AIA-12-1, AIA-12-2) | admitida |
| CTX-AIA-RE-P03 | `OPS-003` | — | obrigatório; retenção dos registos gerados automaticamente ≥ 6 meses («de pelo menos seis meses») | Sem excepção abaixo do piso legal; aplica-se aos registos sob controlo do prestador ou do responsável pela implantação. | Reg. (UE) 2024/1689, art. 19.º, n.º 1, e art. 26.º, n.º 6: «os registos devem ser conservados por um período adequado à finalidade prevista do sistema de IA de risco elevado, de pelo menos seis meses» (AIA-19-1, AIA-26-6) | não admitida |
| CTX-AIA-RE-P04 | `THR-008` | — | obrigatório | — | Reg. (UE) 2024/1689, art. 15.º, n.º 5: «Os sistemas de IA de risco elevado devem ser resistentes a tentativas de terceiros não autorizados de alterar a sua utilização, os seus resultados ou seu desempenho explorando as vulnerabilidades do sistema.» (AIA-15-5) | não admitida |
| CTX-AIA-RE-P05 | `ARC-014` | — | obrigatório | — | Reg. (UE) 2024/1689, art. 15.º, n.º 5: «Os sistemas de IA de risco elevado devem ser resistentes a tentativas de terceiros não autorizados de alterar a sua utilização, os seus resultados ou seu desempenho explorando as vulnerabilidades do sistema.» (AIA-15-5) | não admitida |
| CTX-AIA-RE-P06 | `DEP-011` | — | obrigatório | — | Reg. (UE) 2024/1689, art. 15.º, n.º 5: «Os sistemas de IA de risco elevado devem ser resistentes a tentativas de terceiros não autorizados de alterar a sua utilização, os seus resultados ou seu desempenho explorando as vulnerabilidades do sistema.» (AIA-15-5) | não admitida |
| CTX-AIA-RE-P07 | `DEP-012` | — | obrigatório | — | Reg. (UE) 2024/1689, art. 15.º, n.º 5: «Os sistemas de IA de risco elevado devem ser resistentes a tentativas de terceiros não autorizados de alterar a sua utilização, os seus resultados ou seu desempenho explorando as vulnerabilidades do sistema.» (AIA-15-5) | não admitida |

> **ART50.** Sem pisos por enquanto: as obrigações do art. 50.º (informar as pessoas e marcar o conteúdo sintético) estão declaradas como lacunas na matriz _matriz/aiact.yaml.

## Como se lê a lista {#como-se-le}

Legenda: ✔ selecção base do nível; ▲ elevado ou acrescentado pelo regime (aplica-se pelo regime; se o componente não existir, exige justificação documentada de não aplicabilidade); — não seleccionado.

**Regra de activação.** Requisitos efectivos = selecção técnica ∪ elevados ∪ acrescentados. Os ids de origem «base» só entram se a selecção técnica (contexto técnico da aplicação) os activar. Um id elevado ou acrescentado sem activação técnica não cai em silêncio: entra marcado «aplica-se pelo regime; se o componente não existir, exige justificação documentada de não aplicabilidade» (modelo do Reg. de Execução (UE) 2024/2690, art. 2.º).

## Lista de requisitos — contexto (sem grau) {#lista-contexto}

| Requisito | Nome | L1 | L2 | L3 | Pisos |
|---|---|:--:|:--:|:--:|---|
| `CLA-001` | Classificação formal segundo o modelo de eixos de risco | ✔ | ✔ | ✔ | — |
| `CLA-002` | Aprovação proporcional ao nível de risco atribuído | ✔ | ✔ | ✔ | — |
| `CLA-003` | Activação de controlos base determinada pela classificação | ✔ | ✔ | ✔ | — |
| `CLA-004` | Critérios de reclassificação documentados e monitorizados | ✔ | ✔ | ✔ | — |
| `CLA-005` | Ciclo periódico de revisão de classificação diferenciado por nível | ✔ | ✔ | ✔ | — |
| `CLA-006` | Reavaliação de classificação após evento de mudança significativa | ✔ | ✔ | ✔ | — |
| `CLA-007` | Risco residual com compensação formalizada, owner e TTL | — | ✔ | ✔ | — |
| `CLA-008` | Inventário de aplicações actualizado e acessível para auditoria | ✔ | ✔ | ✔ | — |
| `AUT-001` | MFA obrigatório | — | ✔ | ✔ | — |
| `AUT-002` | Política de passwords | ✔ | ✔ | ✔ | — |
| `AUT-003` | Protecção contra brute force | ✔ | ✔ | ✔ | — |
| `AUT-004` | Revogação activa de sessões | ✔ | ✔ | ✔ | — |
| `AUT-005` | Expiração automática de sessão | ✔ | ✔ | ✔ | — |
| `AUT-006` | Proibição de credenciais em claro | ✔ | ✔ | ✔ | — |
| `AUT-007` | Suporte a autenticação federada | — | ✔ | ✔ | — |
| `AUT-008` | Step-up para acções sensíveis | — | ✔ | ✔ | — |
| `AUT-009` | Reautenticação para alterações críticas | ✔ | ✔ | ✔ | — |
| `AUT-010` | Alerta de acessos suspeitos | — | ✔ | ✔ | — |
| `ACC-001` | Controlo de acesso RBAC | ✔ | ✔ | ✔ | — |
| `ACC-002` | Princípio do menor privilégio | ✔ | ✔ | ✔ | — |
| `ACC-003` | Bloqueio e auditoria de acessos ilegítimos | ✔ | ✔ | ✔ | — |
| `ACC-004` | Separação de perfis | ✔ | ✔ | ✔ | — |
| `ACC-005` | Controlo de acesso a APIs e serviços | ✔ | ✔ | ✔ | — |
| `ACC-006` | Protecção de recursos sensíveis | ✔ | ✔ | ✔ | — |
| `ACC-007` | Validação do modelo de acesso | — | ✔ | ✔ | — |
| `ACC-008` | Revogação em tempo real | ✔ | ✔ | ✔ | — |
| `ACC-009` | Autorização baseada em atributos (ABAC) | — | — | ✔ | — |
| `ACC-010` | Revisão periódica de permissões | — | ✔ | ✔ | — |
| `LOG-001` | Registo de eventos críticos | ✔ | ✔ | ✔ | — |
| `LOG-002` | Atributos mínimos em logs | ✔ | ✔ | ✔ | — |
| `LOG-003` | Protecção de integridade e acesso aos logs | ✔ | ✔ | ✔ | — |
| `LOG-004` | Análise periódica de logs | — | ✔ | ✔ | — |
| `LOG-005` | Retenção mínima dos logs | ✔ | ✔ | ✔ | — |
| `LOG-006` | Envio para sistema centralizado | — | ✔ | ✔ | — |
| `LOG-007` | Classificação e detecção de anomalias | — | ✔ | ✔ | — |
| `LOG-008` | Alarme em falhas do mecanismo de logging | — | ✔ | ✔ | — |
| `LOG-009` | Logs suportam resposta a incidentes | — | ✔ | ✔ | — |
| `LOG-010` | Logging de eventos críticos de negócio | — | — | ✔ | — |
| `SES-001` | Expiração automática por inactividade | ✔ | ✔ | ✔ | — |
| `SES-002` | Logout manual e após alteração de credenciais | ✔ | ✔ | ✔ | — |
| `SES-003` | Identificadores de sessão imprevisíveis | ✔ | ✔ | ✔ | — |
| `SES-004` | Transmissão segura dos tokens | ✔ | ✔ | ✔ | — |
| `SES-005` | Ligação da sessão ao contexto do cliente | — | ✔ | ✔ | — |
| `SES-006` | Revogação explícita da sessão | ✔ | ✔ | ✔ | — |
| `SES-007` | Prevenção de sessões long-lived | — | ✔ | ✔ | — |
| `SES-008` | Scope, TTL e revogação de tokens JWT | — | ✔ | ✔ | — |
| `VAL-001` | Validação geral de entradas externas | ✔ | ✔ | ✔ | — |
| `VAL-002` | Uso de whitelists em vez de blacklists | ✔ | ✔ | ✔ | — |
| `VAL-003` | Validadores de esquema (JSON/XML schema) | — | ✔ | ✔ | — |
| `VAL-004` | Sanitização contra injecções | ✔ | ✔ | ✔ | — |
| `VAL-005` | Validação antes do uso interno | ✔ | ✔ | ✔ | — |
| `VAL-006` | Mensagens de erro seguras na validação | ✔ | ✔ | ✔ | — |
| `VAL-007` | Testes automáticos contra entradas maliciosas | — | ✔ | ✔ | — |
| `VAL-008` | Codificação/escaping de output em renderização (anti-XSS) | ✔ | ✔ | ✔ | — |
| `FIL-001` | Limite de tamanho processável por upload | ✔ | ✔ | ✔ | — |
| `FIL-002` | Validação de tipo por conteúdo, não só por extensão | ✔ | ✔ | ✔ | — |
| `FIL-003` | Tratamento seguro de arquivos comprimidos | — | ✔ | ✔ | — |
| `FIL-004` | Quota de armazenamento por utilizador | — | ✔ | ✔ | — |
| `FIL-005` | Armazenamento fora da árvore servida, com nomes gerados | ✔ | ✔ | ✔ | — |
| `FIL-006` | Serving de ficheiros em contexto inerte | — | ✔ | ✔ | — |
| `FIL-007` | Rastreio anti-malware de ficheiros de origem não confiável | — | ✔ | ✔ | — |
| `FIL-008` | Limite de dimensão de imagens (pixel flood) | — | ✔ | ✔ | — |
| `ERR-001` | Erros não expõem dados sensíveis | ✔ | ✔ | ✔ | — |
| `ERR-002` | Mensagens genéricas no cliente | ✔ | ✔ | ✔ | — |
| `ERR-003` | Não revelar existência de recursos | ✔ | ✔ | ✔ | — |
| `ERR-004` | Mensagens localizadas e seguras | ✔ | ✔ | ✔ | — |
| `ERR-005` | Gestão padronizada e centralizada | — | ✔ | ✔ | — |
| `ERR-006` | Testes automáticos para erros excessivos | — | ✔ | ✔ | — |
| `ERR-007` | Logs de erro com contexto pseudonimizado | — | ✔ | ✔ | — |
| `CFG-001` | Debug e flags desactivados em produção | ✔ | ✔ | ✔ | — |
| `CFG-002` | Separação de ambientes com validação automática | ✔ | ✔ | ✔ | — |
| `CFG-003` | Ausência de parâmetros hardcoded | ✔ | ✔ | ✔ | — |
| `CFG-004` | Configuração externa com permissões controladas | ✔ | ✔ | ✔ | — |
| `CFG-005` | Validação de configuração no arranque | — | ✔ | ✔ | — |
| `CFG-006` | Uso de cofres e gestão segura de segredos | — | ✔ | ✔ | — |
| `CFG-007` | Monitorização de drift de configuração | — | — | ✔ | — |
| `ENC-001` | Encriptação de todas as comunicações em trânsito | ✔ | ✔ | ✔ | — |
| `ENC-002` | Encriptação de dados sensíveis em repouso | — | ✔ | ✔ | — |
| `ENC-003` | Algoritmos e configurações criptográficas robustas | — | ✔ | ✔ | — |
| `ENC-004` | Hashing adaptativo de passwords | ✔ | ✔ | ✔ | — |
| `ENC-005` | Mascaramento de dados sensíveis em logs, outputs e respostas API | ✔ | ✔ | ✔ | — |
| `ENC-006` | Detecção e prevenção de segredos expostos em repositórios | ✔ | ✔ | ✔ | — |
| `ENC-007` | Rotação periódica de chaves e segredos | — | ✔ | ✔ | — |
| `ENC-008` | Prevenção de caching de dados sensíveis no cliente | — | ✔ | ✔ | — |
| `ENC-009` | Integridade verificável de dados críticos | — | — | ✔ | — |
| `PRI-001` | Minimização dos dados pessoais recolhidos | — | ✔ | ✔ | — |
| `PRI-002` | Retenção de dados pessoais com prazo e apagamento efectivo | — | ✔ | ✔ | — |
| `PRI-003` | Capacidade técnica de apagamento e exportação a pedido | — | ✔ | ✔ | — |
| `PRI-004` | Registo de finalidade por conjunto de dados pessoais | — | ✔ | ✔ | — |
| `PRI-005` | Conceito documentado e aplicado de PII em registos | — | ✔ | ✔ | — |
| `API-001` | Autenticação e autorização de chamadas API | ✔ | ✔ | ✔ | — |
| `API-002` | Endpoints desnecessários removidos ou ocultos | ✔ | ✔ | ✔ | — |
| `API-003` | Validação de input em APIs | ✔ | ✔ | ✔ | — |
| `API-004` | Rate limiting e detecção de abusos | — | ✔ | ✔ | — |
| `API-005` | Protecção por TLS e certificados actualizados | ✔ | ✔ | ✔ | — |
| `API-006` | Verificação de SDKs e wrappers utilizados | ✔ | ✔ | ✔ | — |
| `API-007` | Logging e auditoria de chamadas externas | — | ✔ | ✔ | — |
| `INT-001` | Validação de mensagens entre sistemas | ✔ | ✔ | ✔ | — |
| `INT-002` | Autenticação mútua ou tokens seguros | ✔ | ✔ | ✔ | — |
| `INT-003` | Transmissão cifrada com TLS | ✔ | ✔ | ✔ | — |
| `INT-004` | Proibição de protocolos inseguros | ✔ | ✔ | ✔ | — |
| `INT-005` | Assinatura e integridade de mensagens | — | ✔ | ✔ | — |
| `INT-006` | Validação cruzada de origem e destino | — | ✔ | ✔ | — |
| `INT-007` | Monitorização e detecção de padrões anómalos | — | — | ✔ | — |
| `INT-008` | Revisão de segurança e contrato em integrações | — | — | ✔ | — |
| `INT-009` | Consumidores idempotentes | — | ✔ | ✔ | — |
| `INT-010` | Fila de mensagens mortas com tratamento e alarme | — | ✔ | ✔ | — |
| `INT-011` | Protecção contra replay de mensagens | — | ✔ | ✔ | — |
| `INT-012` | Ordem de processamento onde semanticamente exigida | — | — | ✔ | — |
| `REQ-001` | Inclusão de requisitos de segurança | ✔ | ✔ | ✔ | — |
| `REQ-002` | Revisão formal de segurança dos requisitos | ✔ | ✔ | ✔ | — |
| `REQ-003` | Alinhamento com classificação de risco | ✔ | ✔ | ✔ | — |
| `REQ-004` | Versionamento e gestão de requisitos | ✔ | ✔ | ✔ | — |
| `REQ-005` | Nova análise de ameaça após alteração de requisito | — | ✔ | ✔ | — |
| `REQ-006` | Rastreabilidade requisito → ameaça → teste | — | ✔ | ✔ | — |
| `REQ-007` | Revisão iterativa com equipas | — | ✔ | ✔ | — |
| `DST-001` | Repositórios autenticados e auditáveis | ✔ | ✔ | ✔ | — |
| `DST-002` | Aprovação para publicação pública | — | ✔ | ✔ | — |
| `DST-003` | Assinatura digital ou checksum | — | ✔ | ✔ | — |
| `DST-004` | Inclusão de SBOM nos artefactos | — | ✔ | ✔ | — |
| `DST-005` | Acesso segregado por role e ambiente | — | ✔ | ✔ | — |
| `DST-006` | Deploy apenas via pipeline validado | — | ✔ | ✔ | — |
| `DST-007` | Revogação e limpeza de artefactos comprometidos | ✔ | ✔ | ✔ | — |
| `IDE-001` | Ferramentas e IDEs autorizadas | ✔ | ✔ | ✔ | — |
| `IDE-002` | Actualização e gestão de vulnerabilidades | ✔ | ✔ | ✔ | — |
| `IDE-003` | Auditoria de código gerado por ferramentas | — | ✔ | ✔ | — |
| `IDE-004` | Extensões e plugins de fontes confiáveis | ✔ | ✔ | ✔ | — |
| `IDE-005` | Controlo de permissões de extensões | — | ✔ | ✔ | — |
| `IDE-006` | Limitação de ambientes locais sem controlo | — | ✔ | ✔ | — |
| `REQ-AGN-001` | Mandate registado e versionado | ✔ | ✔ | ✔ | — |
| `REQ-AGN-002` | Nível de autonomia classificado por contexto | ✔ | ✔ | ✔ | — |
| `REQ-AGN-003` | Kill-switch operacional documentado e testado | — | ✔ | ✔ | — |
| `REQ-AGN-004` | Intent declaration antes de tool-call destrutivo | — | ✔ | ✔ | — |
| `THR-001` | Threat modeling formal em aplicações L2+ e alterações arquitecturais significativas | — | ✔ | ✔ | — |
| `THR-002` | Arquitectura actual representada com DFDs e trust boundaries explícitos | — | ✔ | ✔ | — |
| `THR-003` | Metodologia estruturada aplicada com cobertura mínima garantida | — | ✔ | ✔ | — |
| `THR-004` | Disposição formal de cada ameaça identificada com owner | — | ✔ | ✔ | — |
| `THR-005` | Rastreabilidade ameaça → requisito → backlog → validação | — | ✔ | ✔ | — |
| `THR-006` | Threat model versionado e actualizado dentro do ciclo ou após trigger | — | ✔ | ✔ | — |
| `THR-007` | Revisão independente por AppSec antes de go-live em L2 e L3 | — | ✔ | ✔ | — |
| `THR-008` | Threat modeling estendido para sistemas com componentes AI/ML | ▲ | ▲ | ▲ | CTX-AIA-RE-P04 |
| `ARC-001` | Zonas de confiança identificadas e documentadas | ✔ | ✔ | ✔ | — |
| `ARC-002` | Exposição externa minimizada e justificada | ✔ | ✔ | ✔ | — |
| `ARC-003` | Revisão de arquitectura com foco em segurança | — | ✔ | ✔ | — |
| `ARC-004` | Decisões de arquitectura documentadas | — | ✔ | ✔ | — |
| `ARC-005` | Threat modeling integrado nos fluxos críticos | — | ✔ | ✔ | — |
| `ARC-006` | Controlos técnicos de isolamento entre domínios sensíveis | ✔ | ✔ | ✔ | — |
| `ARC-007` | Padrões de arquitectura reutilizáveis e aprovados | — | ✔ | ✔ | — |
| `ARC-008` | Fluxos de dados entre zonas de confiança protegidos | ✔ | ✔ | ✔ | — |
| `ARC-009` | Alterações significativas desencadeiam nova revisão | — | ✔ | ✔ | — |
| `ARC-010` | Diagramas de arquitectura versionados e acessíveis | ✔ | ✔ | ✔ | — |
| `ARC-011` | Segmentação lógica e física entre ambientes | — | — | ✔ | — |
| `ARC-012` | Critérios formais de aprovação para aplicações de risco elevado | — | — | ✔ | — |
| `ARC-013` | Validação automática de topologia em CI/CD ou como código | — | — | ✔ | — |
| `ARC-014` | Padrões arquitetónicos específicos para sistemas com componentes AI/ML | ▲ | ▲ | ▲ | CTX-AIA-RE-P05 |
| `ARC-015` | Agentes AI operam como principals isolados com mandate e least privilege | — | ✔ | ✔ | — |
| `DEP-001` | SBOM gerado por build, em formato standardizado | ✔ | ✔ | ✔ | — |
| `DEP-002` | SCA integrado em pipeline com bloqueio por política de severidade | ✔ | ✔ | ✔ | — |
| `DEP-003` | Versões de dependências fixas e auditáveis | ✔ | ✔ | ✔ | — |
| `DEP-004` | Proibição de dependências introduzidas por cópia manual | ✔ | ✔ | ✔ | — |
| `DEP-005` | Registries e repositórios de origem controlados | — | ✔ | ✔ | — |
| `DEP-006` | Aprovação formal para introdução de novas dependências | — | ✔ | ✔ | — |
| `DEP-007` | Política de actualização com SLA definido por severidade | ✔ | ✔ | ✔ | — |
| `DEP-008` | Actualização automatizada com análise de impacto | — | ✔ | ✔ | — |
| `DEP-009` | Detecção de dependências não-intencionais ou emergentes | — | — | ✔ | — |
| `DEP-010` | Rastreabilidade SBOM → vulnerabilidade → correcção | — | ✔ | ✔ | — |
| `DEP-011` | Inventário e proveniência de dependências AI/ML | ▲ | ▲ | ▲ | CTX-AIA-RE-P06 |
| `DEP-012` | AI BOM gerado por build em formato standardizado | ▲ | ▲ | ▲ | CTX-AIA-RE-P07 |
| `DEP-013` | Versão pinned explícita para modelos AI e providers | — | ✔ | ✔ | — |
| `DEP-014` | Lista de providers AI aprovados com classificação de risco | — | ✔ | ✔ | — |
| `DEV-001` | Guidelines de código seguro versionadas e aprovadas por stack | ✔ | ✔ | ✔ | — |
| `DEV-002` | Linters e rulesets de segurança configurados e enforced | ✔ | ✔ | ✔ | — |
| `DEV-003` | Análise estática (SAST) integrada como gate de integração | ✔ | ✔ | ✔ | — |
| `DEV-004` | Revisão de código com checklist de segurança em componentes críticos | ✔ | ✔ | ✔ | — |
| `DEV-005` | Gestão formal de excepções técnicas e desvios a guidelines | — | ✔ | ✔ | — |
| `DEV-006` | Proveniência do código incorporado identificada e controlada | — | ✔ | ✔ | — |
| `DEV-007` | Constrangimentos técnicos explícitos para código gerado por IA | — | ✔ | ✔ | — |
| `DEV-008` | Perfis de qualidade com thresholds mínimos de segurança por nível de risco | — | ✔ | ✔ | — |
| `DEV-009` | Anotações de segurança rastreáveis no código e nos testes | — | — | ✔ | — |
| `CIC-001` | Pipelines como código, versionados e sujeitos a revisão | ✔ | ✔ | ✔ | — |
| `CIC-002` | Triggers controlados e restritos a fontes autorizadas | ✔ | ✔ | ✔ | — |
| `CIC-003` | Gestão segura de segredos no pipeline | ✔ | ✔ | ✔ | — |
| `CIC-004` | Gates de segurança obrigatórios antes de promoção entre ambientes | ✔ | ✔ | ✔ | — |
| `CIC-005` | Rastreabilidade completa de cada execução de pipeline | ✔ | ✔ | ✔ | — |
| `CIC-006` | Isolamento de runners e ambientes de execução | — | ✔ | ✔ | — |
| `CIC-007` | Integridade e proveniência verificável dos artefactos produzidos | — | ✔ | ✔ | — |
| `CIC-008` | Separação de responsabilidades entre build, test e deploy | — | ✔ | ✔ | — |
| `CIC-009` | Credenciais do pipeline com âmbito mínimo e rotação definida | — | ✔ | ✔ | — |
| `CIC-010` | Protecção contra execução de código não autorizado em runners | — | — | ✔ | — |
| `CIC-011` | Promoção entre ambientes atribuível a um responsável identificado | — | ✔ | ✔ | — |
| `IAC-001` | Backend remoto autenticado com locking activo | — | ✔ | ✔ | — |
| `IAC-002` | Ambientes segregados e versionados | ✔ | ✔ | ✔ | — |
| `IAC-003` | Validações automáticas obrigatórias em pipeline | ✔ | ✔ | ✔ | — |
| `IAC-004` | Módulos reutilizados com origem confiável e versão imutável | — | ✔ | ✔ | — |
| `IAC-005` | Histórico completo com versionamento, tags e releases | ✔ | ✔ | ✔ | — |
| `IAC-006` | Convenções formais de naming, tagging e layout | — | ✔ | ✔ | — |
| `IAC-007` | Plan rastreável e aprovado antes de qualquer apply | — | ✔ | ✔ | — |
| `IAC-008` | Rastreabilidade ficheiro → recurso → ambiente | — | ✔ | ✔ | — |
| `IAC-009` | Enforcement automático de políticas em pipeline | — | — | ✔ | — |
| `IAC-010` | Artefactos de plan e manifests versionados e com hash | — | ✔ | ✔ | — |
| `IAC-011` | Gestão segura de segredos - proibição de hardcoding | ✔ | ✔ | ✔ | — |
| `IAC-012` | Detecção automatizada de drift entre IaC e estado real | — | ✔ | ✔ | — |
| `IAC-013` | Revisão periódica formal de módulos e templates | — | — | ✔ | — |
| `CNT-001` | Imagens base de origem confiável e aprovada | ✔ | ✔ | ✔ | — |
| `CNT-002` | Scanning de vulnerabilidades em imagens no CI/CD | ✔ | ✔ | ✔ | — |
| `CNT-003` | Imagens minimalistas - ausência de componentes não necessários | ✔ | ✔ | ✔ | — |
| `CNT-004` | Execução como utilizador não-root | ✔ | ✔ | ✔ | — |
| `CNT-005` | Sistema de ficheiros em modo de leitura em runtime | — | ✔ | ✔ | — |
| `CNT-006` | Restrição de capabilities do kernel e perfis de syscall | — | ✔ | ✔ | — |
| `CNT-007` | Assinatura e verificação de proveniência de imagens | — | ✔ | ✔ | — |
| `CNT-008` | SBOM por imagem publicada | — | ✔ | ✔ | — |
| `CNT-009` | Políticas de admission control activas | — | ✔ | ✔ | — |
| `CNT-010` | Renovação periódica de imagens base | ✔ | ✔ | ✔ | — |
| `CNT-011` | Acesso ao registry com autenticação e rastreabilidade | ✔ | ✔ | ✔ | — |
| `CNT-012` | Isolamento de namespace e políticas de rede em Kubernetes | — | — | ✔ | — |
| `TST-001` | Estratégia formal de testes de segurança por nível de risco | ✔ | ✔ | ✔ | — |
| `TST-002` | SAST com perfil de cobertura gerido e baseline de falsos positivos | ✔ | ✔ | ✔ | — |
| `TST-003` | Gestão formal de findings com SLA de correcção por severidade | ✔ | ✔ | ✔ | — |
| `TST-004` | Evidência de testes reproduzível, auditável e ligada ao build | ✔ | ✔ | ✔ | — |
| `TST-005` | DAST integrado em ambiente de staging antes de promoção | — | ✔ | ✔ | — |
| `TST-006` | Testes de regressão de segurança para vulnerabilidades corrigidas | — | ✔ | ✔ | — |
| `TST-007` | Thresholds mínimos de cobertura de testes de segurança por risco | — | ✔ | ✔ | — |
| `TST-008` | Testes de penetração periódicos com escopo e metodologia definidos | — | ✔ | ✔ | — |
| `TST-009` | Fuzzing sistemático em componentes de processamento de input complexo | — | — | ✔ | — |
| `TST-010` | IAST em ambiente de staging para validação comportamental em runtime | — | — | ✔ | — |
| `DPL-001` | Aprovação formal obrigatória antes de deploy em produção | ✔ | ✔ | ✔ | — |
| `DPL-002` | Promoção apenas de artefactos com proveniência verificada | ✔ | ✔ | ✔ | — |
| `DPL-003` | Gates automáticos de segurança como condição de promoção | ✔ | ✔ | ✔ | — |
| `DPL-004` | Rastreabilidade end-to-end de cada deploy | ✔ | ✔ | ✔ | — |
| `DPL-005` | Rollback configurado, testado e com SLA definido | ✔ | ✔ | ✔ | — |
| `DPL-006` | Credenciais de deploy com âmbito mínimo e vida curta | ✔ | ✔ | ✔ | — |
| `DPL-007` | Validação em staging antes de promoção a produção | — | ✔ | ✔ | — |
| `DPL-008` | Monitorização activa durante e após deploy | — | ✔ | ✔ | — |
| `DPL-009` | Deploy progressivo com contenção de impacto para aplicações críticas | — | — | ✔ | — |
| `DPL-010` | Release gates para sistemas com agentes AI | — | ✔ | ✔ | — |
| `DPL-011` | Canary e demoção de autonomia no release de modelos | — | — | ✔ | — |
| `OPS-001` | Logging estruturado e persistente para todos os componentes em produção | ✔ | ✔ | ✔ | — |
| `OPS-002` | Catálogo de eventos críticos de segurança definido e verificado | ✔ | ✔ | ✔ | — |
| `OPS-003` | Retenção de logs conforme política e requisitos regulatórios | ▲ | ▲ | ▲ | CTX-AIA-RE-P03 |
| `OPS-004` | Centralização de logs em sistema SIEM ou equivalente | — | ✔ | ✔ | — |
| `OPS-005` | Alertas automáticos para eventos de segurança críticos | — | ✔ | ✔ | — |
| `OPS-006` | SLA de resposta a alertas definido e medido | — | ✔ | ✔ | — |
| `OPS-007` | Integração com processo formal de resposta a incidentes | — | ✔ | ✔ | — |
| `OPS-008` | Correlação de eventos entre múltiplas fontes | — | — | ✔ | — |
| `OPS-009` | Deteção comportamental e baseline de actividade normal | — | — | ✔ | — |
| `OPS-010` | Métricas de eficácia da monitorização medidas e revistas | — | — | ✔ | — |
| `OPS-011` | Observabilidade dedicada a componentes AI/ML em produção | ▲ | ▲ | ▲ | CTX-AIA-RE-P01 |
| `OPS-012` | Audit completo por tool invocation de agente AI | ▲ | ▲ | ▲ | CTX-AIA-RE-P02 |
| `OPS-013` | Budget e detecção de runaway em consumo de modelo (token spend) | — | ✔ | ✔ | — |
| `OPS-014` | Detecção de jailbreak / off-policy actions em produção | — | — | ✔ | — |
| `OPS-015` | Sinais contínuos de saúde e disponibilidade operacional | — | ✔ | ✔ | — |
| `TRN-001` | Trilhos de formação de segurança definidos por perfil e nível de criticidade | ✔ | ✔ | ✔ | — |
| `TRN-002` | Onboarding de segurança obrigatório antes de trabalho autónomo | ✔ | ✔ | ✔ | — |
| `TRN-003` | Validação objectiva do onboarding com critério de aceitação definido | ✔ | ✔ | ✔ | — |
| `TRN-004` | Acesso a ambientes críticos condicionado a onboarding validado | ✔ | ✔ | ✔ | — |
| `TRN-005` | Formação de segurança contínua para equipas em projectos L2 e L3 | — | ✔ | ✔ | — |
| `TRN-006` | Conteúdo formativo versionado e actualizado após triggers definidos | — | ✔ | ✔ | — |
| `TRN-007` | Onboarding de segurança equivalente para terceiros e contratados | ✔ | ✔ | ✔ | — |
| `TRN-008` | Programa formal de Security Champions em equipas L3 | — | — | ✔ | — |
| `TRN-009` | KPIs de formação definidos, recolhidos e accionados | — | ✔ | ✔ | — |
| `GOV-001` | Modelo formal de governação de segurança aprovado | ✔ | ✔ | ✔ | — |
| `GOV-002` | Ownership de segurança atribuído por aplicação ou projecto | ✔ | ✔ | ✔ | — |
| `GOV-003` | Alçadas de aprovação definidas e conhecidas por nível de risco | — | ✔ | ✔ | — |
| `GOV-004` | Processo formal de gestão de excepções activo | ✔ | ✔ | ✔ | — |
| `GOV-005` | Excepções com validade, monitorização e revalidação obrigatória | — | ✔ | ✔ | — |
| `GOV-006` | Cláusulas de segurança proporcionais ao risco em contratos com terceiros | ✔ | ✔ | ✔ | — |
| `GOV-007` | Validação formal de fornecedores antes de onboarding | ✔ | ✔ | ✔ | — |
| `GOV-008` | Rastreabilidade organizacional de decisões de segurança por aplicação | — | ✔ | ✔ | — |
| `GOV-009` | Evidência de decisões rastreável, referenciável e retida | ✔ | ✔ | ✔ | — |
| `GOV-010` | Ciclo de validação contínua e revisão periódica de conformidade | — | ✔ | ✔ | — |
| `GOV-011` | KPIs de governação definidos, recolhidos e reportados | — | ✔ | ✔ | — |
| `GOV-012` | Modelo de maturidade activo com evolução medida e planeada | — | — | ✔ | — |
| `GOV-013` | Onboarding técnico e formação obrigatória pré-acesso de terceiros | — | ✔ | ✔ | — |
| `GOV-014` | Revisão periódica de acesso de terceiros (least privilege) | ✔ | ✔ | ✔ | — |
| `GOV-015` | Divulgação coordenada de vulnerabilidades com canal de receção publicado | ✔ | ✔ | ✔ | — |

## Lista de requisitos — ART50 {#lista-art50}

| Requisito | Nome | L1 | L2 | L3 | Pisos |
|---|---|:--:|:--:|:--:|---|
| `CLA-001` | Classificação formal segundo o modelo de eixos de risco | ✔ | ✔ | ✔ | — |
| `CLA-002` | Aprovação proporcional ao nível de risco atribuído | ✔ | ✔ | ✔ | — |
| `CLA-003` | Activação de controlos base determinada pela classificação | ✔ | ✔ | ✔ | — |
| `CLA-004` | Critérios de reclassificação documentados e monitorizados | ✔ | ✔ | ✔ | — |
| `CLA-005` | Ciclo periódico de revisão de classificação diferenciado por nível | ✔ | ✔ | ✔ | — |
| `CLA-006` | Reavaliação de classificação após evento de mudança significativa | ✔ | ✔ | ✔ | — |
| `CLA-007` | Risco residual com compensação formalizada, owner e TTL | — | ✔ | ✔ | — |
| `CLA-008` | Inventário de aplicações actualizado e acessível para auditoria | ✔ | ✔ | ✔ | — |
| `AUT-001` | MFA obrigatório | — | ✔ | ✔ | — |
| `AUT-002` | Política de passwords | ✔ | ✔ | ✔ | — |
| `AUT-003` | Protecção contra brute force | ✔ | ✔ | ✔ | — |
| `AUT-004` | Revogação activa de sessões | ✔ | ✔ | ✔ | — |
| `AUT-005` | Expiração automática de sessão | ✔ | ✔ | ✔ | — |
| `AUT-006` | Proibição de credenciais em claro | ✔ | ✔ | ✔ | — |
| `AUT-007` | Suporte a autenticação federada | — | ✔ | ✔ | — |
| `AUT-008` | Step-up para acções sensíveis | — | ✔ | ✔ | — |
| `AUT-009` | Reautenticação para alterações críticas | ✔ | ✔ | ✔ | — |
| `AUT-010` | Alerta de acessos suspeitos | — | ✔ | ✔ | — |
| `ACC-001` | Controlo de acesso RBAC | ✔ | ✔ | ✔ | — |
| `ACC-002` | Princípio do menor privilégio | ✔ | ✔ | ✔ | — |
| `ACC-003` | Bloqueio e auditoria de acessos ilegítimos | ✔ | ✔ | ✔ | — |
| `ACC-004` | Separação de perfis | ✔ | ✔ | ✔ | — |
| `ACC-005` | Controlo de acesso a APIs e serviços | ✔ | ✔ | ✔ | — |
| `ACC-006` | Protecção de recursos sensíveis | ✔ | ✔ | ✔ | — |
| `ACC-007` | Validação do modelo de acesso | — | ✔ | ✔ | — |
| `ACC-008` | Revogação em tempo real | ✔ | ✔ | ✔ | — |
| `ACC-009` | Autorização baseada em atributos (ABAC) | — | — | ✔ | — |
| `ACC-010` | Revisão periódica de permissões | — | ✔ | ✔ | — |
| `LOG-001` | Registo de eventos críticos | ✔ | ✔ | ✔ | — |
| `LOG-002` | Atributos mínimos em logs | ✔ | ✔ | ✔ | — |
| `LOG-003` | Protecção de integridade e acesso aos logs | ✔ | ✔ | ✔ | — |
| `LOG-004` | Análise periódica de logs | — | ✔ | ✔ | — |
| `LOG-005` | Retenção mínima dos logs | ✔ | ✔ | ✔ | — |
| `LOG-006` | Envio para sistema centralizado | — | ✔ | ✔ | — |
| `LOG-007` | Classificação e detecção de anomalias | — | ✔ | ✔ | — |
| `LOG-008` | Alarme em falhas do mecanismo de logging | — | ✔ | ✔ | — |
| `LOG-009` | Logs suportam resposta a incidentes | — | ✔ | ✔ | — |
| `LOG-010` | Logging de eventos críticos de negócio | — | — | ✔ | — |
| `SES-001` | Expiração automática por inactividade | ✔ | ✔ | ✔ | — |
| `SES-002` | Logout manual e após alteração de credenciais | ✔ | ✔ | ✔ | — |
| `SES-003` | Identificadores de sessão imprevisíveis | ✔ | ✔ | ✔ | — |
| `SES-004` | Transmissão segura dos tokens | ✔ | ✔ | ✔ | — |
| `SES-005` | Ligação da sessão ao contexto do cliente | — | ✔ | ✔ | — |
| `SES-006` | Revogação explícita da sessão | ✔ | ✔ | ✔ | — |
| `SES-007` | Prevenção de sessões long-lived | — | ✔ | ✔ | — |
| `SES-008` | Scope, TTL e revogação de tokens JWT | — | ✔ | ✔ | — |
| `VAL-001` | Validação geral de entradas externas | ✔ | ✔ | ✔ | — |
| `VAL-002` | Uso de whitelists em vez de blacklists | ✔ | ✔ | ✔ | — |
| `VAL-003` | Validadores de esquema (JSON/XML schema) | — | ✔ | ✔ | — |
| `VAL-004` | Sanitização contra injecções | ✔ | ✔ | ✔ | — |
| `VAL-005` | Validação antes do uso interno | ✔ | ✔ | ✔ | — |
| `VAL-006` | Mensagens de erro seguras na validação | ✔ | ✔ | ✔ | — |
| `VAL-007` | Testes automáticos contra entradas maliciosas | — | ✔ | ✔ | — |
| `VAL-008` | Codificação/escaping de output em renderização (anti-XSS) | ✔ | ✔ | ✔ | — |
| `FIL-001` | Limite de tamanho processável por upload | ✔ | ✔ | ✔ | — |
| `FIL-002` | Validação de tipo por conteúdo, não só por extensão | ✔ | ✔ | ✔ | — |
| `FIL-003` | Tratamento seguro de arquivos comprimidos | — | ✔ | ✔ | — |
| `FIL-004` | Quota de armazenamento por utilizador | — | ✔ | ✔ | — |
| `FIL-005` | Armazenamento fora da árvore servida, com nomes gerados | ✔ | ✔ | ✔ | — |
| `FIL-006` | Serving de ficheiros em contexto inerte | — | ✔ | ✔ | — |
| `FIL-007` | Rastreio anti-malware de ficheiros de origem não confiável | — | ✔ | ✔ | — |
| `FIL-008` | Limite de dimensão de imagens (pixel flood) | — | ✔ | ✔ | — |
| `ERR-001` | Erros não expõem dados sensíveis | ✔ | ✔ | ✔ | — |
| `ERR-002` | Mensagens genéricas no cliente | ✔ | ✔ | ✔ | — |
| `ERR-003` | Não revelar existência de recursos | ✔ | ✔ | ✔ | — |
| `ERR-004` | Mensagens localizadas e seguras | ✔ | ✔ | ✔ | — |
| `ERR-005` | Gestão padronizada e centralizada | — | ✔ | ✔ | — |
| `ERR-006` | Testes automáticos para erros excessivos | — | ✔ | ✔ | — |
| `ERR-007` | Logs de erro com contexto pseudonimizado | — | ✔ | ✔ | — |
| `CFG-001` | Debug e flags desactivados em produção | ✔ | ✔ | ✔ | — |
| `CFG-002` | Separação de ambientes com validação automática | ✔ | ✔ | ✔ | — |
| `CFG-003` | Ausência de parâmetros hardcoded | ✔ | ✔ | ✔ | — |
| `CFG-004` | Configuração externa com permissões controladas | ✔ | ✔ | ✔ | — |
| `CFG-005` | Validação de configuração no arranque | — | ✔ | ✔ | — |
| `CFG-006` | Uso de cofres e gestão segura de segredos | — | ✔ | ✔ | — |
| `CFG-007` | Monitorização de drift de configuração | — | — | ✔ | — |
| `ENC-001` | Encriptação de todas as comunicações em trânsito | ✔ | ✔ | ✔ | — |
| `ENC-002` | Encriptação de dados sensíveis em repouso | — | ✔ | ✔ | — |
| `ENC-003` | Algoritmos e configurações criptográficas robustas | — | ✔ | ✔ | — |
| `ENC-004` | Hashing adaptativo de passwords | ✔ | ✔ | ✔ | — |
| `ENC-005` | Mascaramento de dados sensíveis em logs, outputs e respostas API | ✔ | ✔ | ✔ | — |
| `ENC-006` | Detecção e prevenção de segredos expostos em repositórios | ✔ | ✔ | ✔ | — |
| `ENC-007` | Rotação periódica de chaves e segredos | — | ✔ | ✔ | — |
| `ENC-008` | Prevenção de caching de dados sensíveis no cliente | — | ✔ | ✔ | — |
| `ENC-009` | Integridade verificável de dados críticos | — | — | ✔ | — |
| `PRI-001` | Minimização dos dados pessoais recolhidos | — | ✔ | ✔ | — |
| `PRI-002` | Retenção de dados pessoais com prazo e apagamento efectivo | — | ✔ | ✔ | — |
| `PRI-003` | Capacidade técnica de apagamento e exportação a pedido | — | ✔ | ✔ | — |
| `PRI-004` | Registo de finalidade por conjunto de dados pessoais | — | ✔ | ✔ | — |
| `PRI-005` | Conceito documentado e aplicado de PII em registos | — | ✔ | ✔ | — |
| `API-001` | Autenticação e autorização de chamadas API | ✔ | ✔ | ✔ | — |
| `API-002` | Endpoints desnecessários removidos ou ocultos | ✔ | ✔ | ✔ | — |
| `API-003` | Validação de input em APIs | ✔ | ✔ | ✔ | — |
| `API-004` | Rate limiting e detecção de abusos | — | ✔ | ✔ | — |
| `API-005` | Protecção por TLS e certificados actualizados | ✔ | ✔ | ✔ | — |
| `API-006` | Verificação de SDKs e wrappers utilizados | ✔ | ✔ | ✔ | — |
| `API-007` | Logging e auditoria de chamadas externas | — | ✔ | ✔ | — |
| `INT-001` | Validação de mensagens entre sistemas | ✔ | ✔ | ✔ | — |
| `INT-002` | Autenticação mútua ou tokens seguros | ✔ | ✔ | ✔ | — |
| `INT-003` | Transmissão cifrada com TLS | ✔ | ✔ | ✔ | — |
| `INT-004` | Proibição de protocolos inseguros | ✔ | ✔ | ✔ | — |
| `INT-005` | Assinatura e integridade de mensagens | — | ✔ | ✔ | — |
| `INT-006` | Validação cruzada de origem e destino | — | ✔ | ✔ | — |
| `INT-007` | Monitorização e detecção de padrões anómalos | — | — | ✔ | — |
| `INT-008` | Revisão de segurança e contrato em integrações | — | — | ✔ | — |
| `INT-009` | Consumidores idempotentes | — | ✔ | ✔ | — |
| `INT-010` | Fila de mensagens mortas com tratamento e alarme | — | ✔ | ✔ | — |
| `INT-011` | Protecção contra replay de mensagens | — | ✔ | ✔ | — |
| `INT-012` | Ordem de processamento onde semanticamente exigida | — | — | ✔ | — |
| `REQ-001` | Inclusão de requisitos de segurança | ✔ | ✔ | ✔ | — |
| `REQ-002` | Revisão formal de segurança dos requisitos | ✔ | ✔ | ✔ | — |
| `REQ-003` | Alinhamento com classificação de risco | ✔ | ✔ | ✔ | — |
| `REQ-004` | Versionamento e gestão de requisitos | ✔ | ✔ | ✔ | — |
| `REQ-005` | Nova análise de ameaça após alteração de requisito | — | ✔ | ✔ | — |
| `REQ-006` | Rastreabilidade requisito → ameaça → teste | — | ✔ | ✔ | — |
| `REQ-007` | Revisão iterativa com equipas | — | ✔ | ✔ | — |
| `DST-001` | Repositórios autenticados e auditáveis | ✔ | ✔ | ✔ | — |
| `DST-002` | Aprovação para publicação pública | — | ✔ | ✔ | — |
| `DST-003` | Assinatura digital ou checksum | — | ✔ | ✔ | — |
| `DST-004` | Inclusão de SBOM nos artefactos | — | ✔ | ✔ | — |
| `DST-005` | Acesso segregado por role e ambiente | — | ✔ | ✔ | — |
| `DST-006` | Deploy apenas via pipeline validado | — | ✔ | ✔ | — |
| `DST-007` | Revogação e limpeza de artefactos comprometidos | ✔ | ✔ | ✔ | — |
| `IDE-001` | Ferramentas e IDEs autorizadas | ✔ | ✔ | ✔ | — |
| `IDE-002` | Actualização e gestão de vulnerabilidades | ✔ | ✔ | ✔ | — |
| `IDE-003` | Auditoria de código gerado por ferramentas | — | ✔ | ✔ | — |
| `IDE-004` | Extensões e plugins de fontes confiáveis | ✔ | ✔ | ✔ | — |
| `IDE-005` | Controlo de permissões de extensões | — | ✔ | ✔ | — |
| `IDE-006` | Limitação de ambientes locais sem controlo | — | ✔ | ✔ | — |
| `REQ-AGN-001` | Mandate registado e versionado | ✔ | ✔ | ✔ | — |
| `REQ-AGN-002` | Nível de autonomia classificado por contexto | ✔ | ✔ | ✔ | — |
| `REQ-AGN-003` | Kill-switch operacional documentado e testado | — | ✔ | ✔ | — |
| `REQ-AGN-004` | Intent declaration antes de tool-call destrutivo | — | ✔ | ✔ | — |
| `THR-001` | Threat modeling formal em aplicações L2+ e alterações arquitecturais significativas | — | ✔ | ✔ | — |
| `THR-002` | Arquitectura actual representada com DFDs e trust boundaries explícitos | — | ✔ | ✔ | — |
| `THR-003` | Metodologia estruturada aplicada com cobertura mínima garantida | — | ✔ | ✔ | — |
| `THR-004` | Disposição formal de cada ameaça identificada com owner | — | ✔ | ✔ | — |
| `THR-005` | Rastreabilidade ameaça → requisito → backlog → validação | — | ✔ | ✔ | — |
| `THR-006` | Threat model versionado e actualizado dentro do ciclo ou após trigger | — | ✔ | ✔ | — |
| `THR-007` | Revisão independente por AppSec antes de go-live em L2 e L3 | — | ✔ | ✔ | — |
| `THR-008` | Threat modeling estendido para sistemas com componentes AI/ML | — | ✔ | ✔ | — |
| `ARC-001` | Zonas de confiança identificadas e documentadas | ✔ | ✔ | ✔ | — |
| `ARC-002` | Exposição externa minimizada e justificada | ✔ | ✔ | ✔ | — |
| `ARC-003` | Revisão de arquitectura com foco em segurança | — | ✔ | ✔ | — |
| `ARC-004` | Decisões de arquitectura documentadas | — | ✔ | ✔ | — |
| `ARC-005` | Threat modeling integrado nos fluxos críticos | — | ✔ | ✔ | — |
| `ARC-006` | Controlos técnicos de isolamento entre domínios sensíveis | ✔ | ✔ | ✔ | — |
| `ARC-007` | Padrões de arquitectura reutilizáveis e aprovados | — | ✔ | ✔ | — |
| `ARC-008` | Fluxos de dados entre zonas de confiança protegidos | ✔ | ✔ | ✔ | — |
| `ARC-009` | Alterações significativas desencadeiam nova revisão | — | ✔ | ✔ | — |
| `ARC-010` | Diagramas de arquitectura versionados e acessíveis | ✔ | ✔ | ✔ | — |
| `ARC-011` | Segmentação lógica e física entre ambientes | — | — | ✔ | — |
| `ARC-012` | Critérios formais de aprovação para aplicações de risco elevado | — | — | ✔ | — |
| `ARC-013` | Validação automática de topologia em CI/CD ou como código | — | — | ✔ | — |
| `ARC-014` | Padrões arquitetónicos específicos para sistemas com componentes AI/ML | — | ✔ | ✔ | — |
| `ARC-015` | Agentes AI operam como principals isolados com mandate e least privilege | — | ✔ | ✔ | — |
| `DEP-001` | SBOM gerado por build, em formato standardizado | ✔ | ✔ | ✔ | — |
| `DEP-002` | SCA integrado em pipeline com bloqueio por política de severidade | ✔ | ✔ | ✔ | — |
| `DEP-003` | Versões de dependências fixas e auditáveis | ✔ | ✔ | ✔ | — |
| `DEP-004` | Proibição de dependências introduzidas por cópia manual | ✔ | ✔ | ✔ | — |
| `DEP-005` | Registries e repositórios de origem controlados | — | ✔ | ✔ | — |
| `DEP-006` | Aprovação formal para introdução de novas dependências | — | ✔ | ✔ | — |
| `DEP-007` | Política de actualização com SLA definido por severidade | ✔ | ✔ | ✔ | — |
| `DEP-008` | Actualização automatizada com análise de impacto | — | ✔ | ✔ | — |
| `DEP-009` | Detecção de dependências não-intencionais ou emergentes | — | — | ✔ | — |
| `DEP-010` | Rastreabilidade SBOM → vulnerabilidade → correcção | — | ✔ | ✔ | — |
| `DEP-011` | Inventário e proveniência de dependências AI/ML | — | ✔ | ✔ | — |
| `DEP-012` | AI BOM gerado por build em formato standardizado | — | ✔ | ✔ | — |
| `DEP-013` | Versão pinned explícita para modelos AI e providers | — | ✔ | ✔ | — |
| `DEP-014` | Lista de providers AI aprovados com classificação de risco | — | ✔ | ✔ | — |
| `DEV-001` | Guidelines de código seguro versionadas e aprovadas por stack | ✔ | ✔ | ✔ | — |
| `DEV-002` | Linters e rulesets de segurança configurados e enforced | ✔ | ✔ | ✔ | — |
| `DEV-003` | Análise estática (SAST) integrada como gate de integração | ✔ | ✔ | ✔ | — |
| `DEV-004` | Revisão de código com checklist de segurança em componentes críticos | ✔ | ✔ | ✔ | — |
| `DEV-005` | Gestão formal de excepções técnicas e desvios a guidelines | — | ✔ | ✔ | — |
| `DEV-006` | Proveniência do código incorporado identificada e controlada | — | ✔ | ✔ | — |
| `DEV-007` | Constrangimentos técnicos explícitos para código gerado por IA | — | ✔ | ✔ | — |
| `DEV-008` | Perfis de qualidade com thresholds mínimos de segurança por nível de risco | — | ✔ | ✔ | — |
| `DEV-009` | Anotações de segurança rastreáveis no código e nos testes | — | — | ✔ | — |
| `CIC-001` | Pipelines como código, versionados e sujeitos a revisão | ✔ | ✔ | ✔ | — |
| `CIC-002` | Triggers controlados e restritos a fontes autorizadas | ✔ | ✔ | ✔ | — |
| `CIC-003` | Gestão segura de segredos no pipeline | ✔ | ✔ | ✔ | — |
| `CIC-004` | Gates de segurança obrigatórios antes de promoção entre ambientes | ✔ | ✔ | ✔ | — |
| `CIC-005` | Rastreabilidade completa de cada execução de pipeline | ✔ | ✔ | ✔ | — |
| `CIC-006` | Isolamento de runners e ambientes de execução | — | ✔ | ✔ | — |
| `CIC-007` | Integridade e proveniência verificável dos artefactos produzidos | — | ✔ | ✔ | — |
| `CIC-008` | Separação de responsabilidades entre build, test e deploy | — | ✔ | ✔ | — |
| `CIC-009` | Credenciais do pipeline com âmbito mínimo e rotação definida | — | ✔ | ✔ | — |
| `CIC-010` | Protecção contra execução de código não autorizado em runners | — | — | ✔ | — |
| `CIC-011` | Promoção entre ambientes atribuível a um responsável identificado | — | ✔ | ✔ | — |
| `IAC-001` | Backend remoto autenticado com locking activo | — | ✔ | ✔ | — |
| `IAC-002` | Ambientes segregados e versionados | ✔ | ✔ | ✔ | — |
| `IAC-003` | Validações automáticas obrigatórias em pipeline | ✔ | ✔ | ✔ | — |
| `IAC-004` | Módulos reutilizados com origem confiável e versão imutável | — | ✔ | ✔ | — |
| `IAC-005` | Histórico completo com versionamento, tags e releases | ✔ | ✔ | ✔ | — |
| `IAC-006` | Convenções formais de naming, tagging e layout | — | ✔ | ✔ | — |
| `IAC-007` | Plan rastreável e aprovado antes de qualquer apply | — | ✔ | ✔ | — |
| `IAC-008` | Rastreabilidade ficheiro → recurso → ambiente | — | ✔ | ✔ | — |
| `IAC-009` | Enforcement automático de políticas em pipeline | — | — | ✔ | — |
| `IAC-010` | Artefactos de plan e manifests versionados e com hash | — | ✔ | ✔ | — |
| `IAC-011` | Gestão segura de segredos - proibição de hardcoding | ✔ | ✔ | ✔ | — |
| `IAC-012` | Detecção automatizada de drift entre IaC e estado real | — | ✔ | ✔ | — |
| `IAC-013` | Revisão periódica formal de módulos e templates | — | — | ✔ | — |
| `CNT-001` | Imagens base de origem confiável e aprovada | ✔ | ✔ | ✔ | — |
| `CNT-002` | Scanning de vulnerabilidades em imagens no CI/CD | ✔ | ✔ | ✔ | — |
| `CNT-003` | Imagens minimalistas - ausência de componentes não necessários | ✔ | ✔ | ✔ | — |
| `CNT-004` | Execução como utilizador não-root | ✔ | ✔ | ✔ | — |
| `CNT-005` | Sistema de ficheiros em modo de leitura em runtime | — | ✔ | ✔ | — |
| `CNT-006` | Restrição de capabilities do kernel e perfis de syscall | — | ✔ | ✔ | — |
| `CNT-007` | Assinatura e verificação de proveniência de imagens | — | ✔ | ✔ | — |
| `CNT-008` | SBOM por imagem publicada | — | ✔ | ✔ | — |
| `CNT-009` | Políticas de admission control activas | — | ✔ | ✔ | — |
| `CNT-010` | Renovação periódica de imagens base | ✔ | ✔ | ✔ | — |
| `CNT-011` | Acesso ao registry com autenticação e rastreabilidade | ✔ | ✔ | ✔ | — |
| `CNT-012` | Isolamento de namespace e políticas de rede em Kubernetes | — | — | ✔ | — |
| `TST-001` | Estratégia formal de testes de segurança por nível de risco | ✔ | ✔ | ✔ | — |
| `TST-002` | SAST com perfil de cobertura gerido e baseline de falsos positivos | ✔ | ✔ | ✔ | — |
| `TST-003` | Gestão formal de findings com SLA de correcção por severidade | ✔ | ✔ | ✔ | — |
| `TST-004` | Evidência de testes reproduzível, auditável e ligada ao build | ✔ | ✔ | ✔ | — |
| `TST-005` | DAST integrado em ambiente de staging antes de promoção | — | ✔ | ✔ | — |
| `TST-006` | Testes de regressão de segurança para vulnerabilidades corrigidas | — | ✔ | ✔ | — |
| `TST-007` | Thresholds mínimos de cobertura de testes de segurança por risco | — | ✔ | ✔ | — |
| `TST-008` | Testes de penetração periódicos com escopo e metodologia definidos | — | ✔ | ✔ | — |
| `TST-009` | Fuzzing sistemático em componentes de processamento de input complexo | — | — | ✔ | — |
| `TST-010` | IAST em ambiente de staging para validação comportamental em runtime | — | — | ✔ | — |
| `DPL-001` | Aprovação formal obrigatória antes de deploy em produção | ✔ | ✔ | ✔ | — |
| `DPL-002` | Promoção apenas de artefactos com proveniência verificada | ✔ | ✔ | ✔ | — |
| `DPL-003` | Gates automáticos de segurança como condição de promoção | ✔ | ✔ | ✔ | — |
| `DPL-004` | Rastreabilidade end-to-end de cada deploy | ✔ | ✔ | ✔ | — |
| `DPL-005` | Rollback configurado, testado e com SLA definido | ✔ | ✔ | ✔ | — |
| `DPL-006` | Credenciais de deploy com âmbito mínimo e vida curta | ✔ | ✔ | ✔ | — |
| `DPL-007` | Validação em staging antes de promoção a produção | — | ✔ | ✔ | — |
| `DPL-008` | Monitorização activa durante e após deploy | — | ✔ | ✔ | — |
| `DPL-009` | Deploy progressivo com contenção de impacto para aplicações críticas | — | — | ✔ | — |
| `DPL-010` | Release gates para sistemas com agentes AI | — | ✔ | ✔ | — |
| `DPL-011` | Canary e demoção de autonomia no release de modelos | — | — | ✔ | — |
| `OPS-001` | Logging estruturado e persistente para todos os componentes em produção | ✔ | ✔ | ✔ | — |
| `OPS-002` | Catálogo de eventos críticos de segurança definido e verificado | ✔ | ✔ | ✔ | — |
| `OPS-003` | Retenção de logs conforme política e requisitos regulatórios | — | ✔ | ✔ | — |
| `OPS-004` | Centralização de logs em sistema SIEM ou equivalente | — | ✔ | ✔ | — |
| `OPS-005` | Alertas automáticos para eventos de segurança críticos | — | ✔ | ✔ | — |
| `OPS-006` | SLA de resposta a alertas definido e medido | — | ✔ | ✔ | — |
| `OPS-007` | Integração com processo formal de resposta a incidentes | — | ✔ | ✔ | — |
| `OPS-008` | Correlação de eventos entre múltiplas fontes | — | — | ✔ | — |
| `OPS-009` | Deteção comportamental e baseline de actividade normal | — | — | ✔ | — |
| `OPS-010` | Métricas de eficácia da monitorização medidas e revistas | — | — | ✔ | — |
| `OPS-011` | Observabilidade dedicada a componentes AI/ML em produção | — | ✔ | ✔ | — |
| `OPS-012` | Audit completo por tool invocation de agente AI | — | ✔ | ✔ | — |
| `OPS-013` | Budget e detecção de runaway em consumo de modelo (token spend) | — | ✔ | ✔ | — |
| `OPS-014` | Detecção de jailbreak / off-policy actions em produção | — | — | ✔ | — |
| `OPS-015` | Sinais contínuos de saúde e disponibilidade operacional | — | ✔ | ✔ | — |
| `TRN-001` | Trilhos de formação de segurança definidos por perfil e nível de criticidade | ✔ | ✔ | ✔ | — |
| `TRN-002` | Onboarding de segurança obrigatório antes de trabalho autónomo | ✔ | ✔ | ✔ | — |
| `TRN-003` | Validação objectiva do onboarding com critério de aceitação definido | ✔ | ✔ | ✔ | — |
| `TRN-004` | Acesso a ambientes críticos condicionado a onboarding validado | ✔ | ✔ | ✔ | — |
| `TRN-005` | Formação de segurança contínua para equipas em projectos L2 e L3 | — | ✔ | ✔ | — |
| `TRN-006` | Conteúdo formativo versionado e actualizado após triggers definidos | — | ✔ | ✔ | — |
| `TRN-007` | Onboarding de segurança equivalente para terceiros e contratados | ✔ | ✔ | ✔ | — |
| `TRN-008` | Programa formal de Security Champions em equipas L3 | — | — | ✔ | — |
| `TRN-009` | KPIs de formação definidos, recolhidos e accionados | — | ✔ | ✔ | — |
| `GOV-001` | Modelo formal de governação de segurança aprovado | ✔ | ✔ | ✔ | — |
| `GOV-002` | Ownership de segurança atribuído por aplicação ou projecto | ✔ | ✔ | ✔ | — |
| `GOV-003` | Alçadas de aprovação definidas e conhecidas por nível de risco | — | ✔ | ✔ | — |
| `GOV-004` | Processo formal de gestão de excepções activo | ✔ | ✔ | ✔ | — |
| `GOV-005` | Excepções com validade, monitorização e revalidação obrigatória | — | ✔ | ✔ | — |
| `GOV-006` | Cláusulas de segurança proporcionais ao risco em contratos com terceiros | ✔ | ✔ | ✔ | — |
| `GOV-007` | Validação formal de fornecedores antes de onboarding | ✔ | ✔ | ✔ | — |
| `GOV-008` | Rastreabilidade organizacional de decisões de segurança por aplicação | — | ✔ | ✔ | — |
| `GOV-009` | Evidência de decisões rastreável, referenciável e retida | ✔ | ✔ | ✔ | — |
| `GOV-010` | Ciclo de validação contínua e revisão periódica de conformidade | — | ✔ | ✔ | — |
| `GOV-011` | KPIs de governação definidos, recolhidos e reportados | — | ✔ | ✔ | — |
| `GOV-012` | Modelo de maturidade activo com evolução medida e planeada | — | — | ✔ | — |
| `GOV-013` | Onboarding técnico e formação obrigatória pré-acesso de terceiros | — | ✔ | ✔ | — |
| `GOV-014` | Revisão periódica de acesso de terceiros (least privilege) | ✔ | ✔ | ✔ | — |
| `GOV-015` | Divulgação coordenada de vulnerabilidades com canal de receção publicado | ✔ | ✔ | ✔ | — |

## Obrigações do regime por força de cobertura {#forca}

Contagem das obrigações da matriz `_matriz/aiact.yaml` (excluídas as dirigidas às autoridades). A secção «O que este Manual cobre e o que fica de fora» da página do cross-check detalha-as.

| Força | Obrigações |
|---|--:|
| Cobre | 14 |
| Parcial | 62 |
| Apoia evidência | 29 |
| Lacuna | 32 |
| Fora de âmbito | 108 |
