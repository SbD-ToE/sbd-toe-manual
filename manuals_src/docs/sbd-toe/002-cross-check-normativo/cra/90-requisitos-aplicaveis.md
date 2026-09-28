---
id: requisitos-aplicaveis
title: "Requisitos aplicáveis — Produto com elementos digitais colocado no mercado (CRA)"
description: "Requisitos do Manual que se aplicam sob o contexto CTX-CRA, por nível e grau, com os pisos que o regime eleva e a base legal de cada um."
sidebar_position: 90
tags: [cross-check, cra, requisitos, overlay]
sbdtoe_generated: reg-requirements-view
generated_by: scripts/gen_reg_views.py  # não se edita à mão: editar os catálogos, o overlay e a matriz
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
  - 002-cross-check-normativo/_matriz/cra.yaml
---

# Requisitos aplicáveis: Produto com elementos digitais colocado no mercado (CRA)

Esta página junta, para o contexto **CTX-CRA**, a selecção base do Manual por nível e os **pisos** que o regime eleva, cada um com a obrigação que o fundamenta. Um contexto nunca baixa um mínimo do Manual.

## Quando se aplica {#quando-se-aplica}

A aplicação é ou integra um produto com elementos digitais que a organização coloca no mercado; declara-se por aplicação ou produto. Declara-se por aplicação.

> Reg. (UE) 2024/2847, art. 2.º, n.º 1: «O presente regulamento é aplicável aos produtos com elementos digitais disponibilizados no mercado cuja finalidade prevista ou utilização razoavelmente previsível inclua uma conexão de dados lógica ou física, direta ou indireta, a um dispositivo ou a uma rede.»

## Pisos do contexto {#pisos}

| Piso | Alvo | Grau | Piso exigido | Âmbito | Base legal | Justificação de não aplicabilidade |
|---|---|---|---|---|---|---|
| CTX-CRA-P01 | `DEP-002` | — | obrigatório | Bloqueio por vulnerabilidade explorável conhecida em qualquer nível, além do critério de severidade: nenhuma vulnerabilidade explorável conhecida na colocação no mercado. | Reg. (UE) 2024/2847, anexo I, parte I, ponto 2, al. a): «Ser disponibilizados no mercado sem nenhuma vulnerabilidade passível de ser explorada conhecida» (CRA-AnxI-P1-2a) | não admitida |
| CTX-CRA-P02 | [Política 12 §4](/sbd-toe/assets/policies/policy-excecoes-cve#4-tipos-de-exceção) | — | obrigatório | As excepções «fix deferred» e «risk accepted» não se aplicam a vulnerabilidades exploráveis conhecidas de um produto CRA no momento da colocação no mercado. | Reg. (UE) 2024/2847, anexo I, parte I, ponto 2, al. a): «Ser disponibilizados no mercado sem nenhuma vulnerabilidade passível de ser explorada conhecida» (CRA-AnxI-P1-2a) | não admitida |
| CTX-CRA-P03 | `DEP-006` | — | obrigatório | — | Reg. (UE) 2024/2847, art. 13.º, n.º 5: «os fabricantes devem exercer a diligência devida quando integram componentes provenientes de terceiros» (CRA-13-5) | não admitida |
| CTX-CRA-P04 | `GOV-015` | — | obrigatório | Ponto de contacto único, facilmente identificável e indicado nas informações e instruções ao utilizador (anexo II); endereço de contacto também para vulnerabilidades em componentes de terceiros. | Reg. (UE) 2024/2847, anexo I, parte II, pontos 5 e 6; art. 13.º, n.º 17; anexo II, ponto 2: «Definir e aplicar uma política de divulgação coordenada de vulnerabilidades» (CRA-AnxI-P2-5, CRA-AnxI-P2-6, CRA-13-17, CRA-AnxII-2) | não admitida |

## Requisitos acrescentados pelo regime {#acrescentos}

Estes requisitos só fazem sentido sob o regime e por isso não vivem nos catálogos do Manual; definem-se aqui, com a base legal de cada um.

| Requisito | Nome | Critério de aceitação | Base legal |
|---|---|---|---|
| `CTX-CRA-R01` | Período de apoio determinado, comunicado e cumprido | Período de apoio determinado por produto com os critérios do art. 13.º, n.º 8 (tempo de utilização previsto, expectativas razoáveis dos utilizadores, natureza e finalidade do produto) e com pelo menos cinco anos, salvo utilização prevista inferior; fundamentação registada na documentação técnica; data de fim do apoio indicada nas informações ao utilizador; utilizadores notificados do fim do apoio quando tecnicamente viável; cada actualização de segurança mantida disponível pelo menos 10 anos após a emissão ou pelo resto do período de apoio, se for mais longo; arquivos públicos de versões anteriores com aviso claro dos riscos de uso fora do período de apoio. | Reg. (UE) 2024/2847, art. 13.º, n.os 8, 9, 11 e 19; anexo II, ponto 7; anexo VII, ponto 4: «o período de apoio é de, pelo menos, cinco anos» (CRA-13-8-p2, CRA-13-8-p3, CRA-13-8-p5, CRA-13-9, CRA-13-11, CRA-13-19-p2, CRA-AnxII-7, CRA-AnxVII-4) |
| `CTX-CRA-R02` | Distribuição e mecanismo de actualizações de segurança no utilizador | Actualizações de segurança automáticas configuradas por defeito quando aplicável, com mecanismo de autoexclusão claro, notificação das actualizações disponíveis e opção de adiamento temporário; actualizações de segurança distribuídas sem demora e de forma gratuita (salvo acordo com um utilizador profissional sobre produto personalizado), separadas das actualizações de funcionalidades quando tecnicamente viável e acompanhadas de orientações sobre as medidas a tomar; distribuição segura e verificável (DST-003); instruções para instalar as actualizações e para desligar as automáticas nas informações ao utilizador. | Reg. (UE) 2024/2847, anexo I, parte I, ponto 2, al. c), e parte II, pontos 2, 7 e 8; anexo II, ponto 8, als. c) e e): «Assegurar que as atualizações de segurança disponíveis para resolver problemas de segurança identificados sejam distribuídas sem demora» (CRA-AnxI-P1-2c, CRA-AnxI-P2-2, CRA-AnxI-P2-7, CRA-AnxI-P2-8, CRA-AnxII-8c, CRA-AnxII-8e) |
| `CTX-CRA-R03` | Avisos de segurança públicos sobre vulnerabilidades corrigidas | Depois de disponibilizada a actualização de segurança, aviso público sobre as vulnerabilidades corrigidas, com descrição, informação que permita identificar o produto afectado, impactos, gravidade e informação clara e acessível para a correcção; adiamento da divulgação só em casos devidamente justificados, registados, até os utilizadores terem tido a possibilidade de aplicar a correcção. | Reg. (UE) 2024/2847, anexo I, parte II, ponto 4: «Uma vez disponibilizada uma atualização de segurança, partilhar e divulgar publicamente informações sobre as vulnerabilidades corrigidas» (CRA-AnxI-P2-4) |
| `CTX-CRA-R04` | Comunicação ao mantenedor de vulnerabilidades em componentes | Vulnerabilidade identificada num componente integrado no produto (incluindo de código aberto) comunicada à pessoa ou entidade que o fabrica ou mantém; correcção desenvolvida pela organização partilhada com o responsável pelo componente, se for caso disso em formato legível por máquina; vulnerabilidade tratada segundo a parte II do anexo I (DEP-007, DEP-010). | Reg. (UE) 2024/2847, art. 13.º, n.º 6: «os fabricantes devem comunicar a vulnerabilidade à pessoa ou entidade responsável pelo fabrico ou pela manutenção do componente» (CRA-13-6-a, CRA-13-6-b) |
| `CTX-CRA-R05` | Critério de incidente grave | Um incidente com impacto na segurança do produto é avaliado como grave quando afecta ou pode afectar a capacidade do produto de proteger a disponibilidade, autenticidade, integridade ou confidencialidade de dados ou funções sensíveis ou importantes, ou quando introduz ou pode introduzir código mal-intencionado no produto ou nos sistemas de um utilizador; a avaliação fica registada e, sendo grave, segue os prazos e o conteúdo da Política 32 §6 e §6.1. | Reg. (UE) 2024/2847, art. 14.º, n.os 3 e 5: «um incidente com impacto na segurança do produto com elementos digitais é considerado grave se» (CRA-14-3) |

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
| `AUT-011` | Sem credenciais por defeito | ✔ | ✔ | ✔ | — |
| `AUT-012` | Autenticadores criptográficos e biometria local | ✔ | ✔ | ✔ | — |
| `AUT-013` | Gestão e recuperação dos factores de autenticação | ✔ | ✔ | ✔ | — |
| `ACC-001` | Controlo de acesso RBAC | ✔ | ✔ | ✔ | — |
| `ACC-002` | Princípio do menor privilégio | ✔ | ✔ | ✔ | — |
| `ACC-003` | Bloqueio e auditoria de acessos ilegítimos | ✔ | ✔ | ✔ | — |
| `ACC-004` | Separação de perfis | ✔ | ✔ | ✔ | — |
| `ACC-005` | Controlo de acesso a APIs e serviços | ✔ | ✔ | ✔ | — |
| `ACC-006` | Protecção de recursos sensíveis | ✔ | ✔ | ✔ | — |
| `ACC-007` | Validação do modelo de acesso | — | ✔ | ✔ | — |
| `ACC-008` | Revogação em tempo real | ✔ | ✔ | ✔ | — |
| `ACC-009` | Autorização baseada em atributos (ABAC) | — | — | ✔ | — |
| `ACC-010` | Revisão periódica de permissões | ✔ | ✔ | ✔ | — |
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
| `ENC-007` | Ciclo de vida de chaves, segredos e certificados | — | ✔ | ✔ | — |
| `ENC-008` | Prevenção de caching de dados sensíveis no cliente | — | ✔ | ✔ | — |
| `ENC-009` | Integridade verificável de dados críticos | — | — | ✔ | — |
| `PRI-001` | Minimização dos dados pessoais recolhidos | ✔ | ✔ | ✔ | — |
| `PRI-002` | Retenção de dados pessoais com prazo e apagamento efectivo | ✔ | ✔ | ✔ | — |
| `PRI-003` | Capacidade técnica de acesso, rectificação, apagamento e exportação a pedido | ✔ | ✔ | ✔ | — |
| `PRI-004` | Registo de finalidade e destinatários por conjunto de dados pessoais | — | ✔ | ✔ | — |
| `PRI-005` | Conceito documentado e aplicado de PII em registos | — | ✔ | ✔ | — |
| `PRI-006` | Gestão técnica do consentimento e das preferências de oposição | ✔ | ✔ | ✔ | — |
| `PRI-007` | Privacidade por defeito nas definições voltadas ao utilizador | ✔ | ✔ | ✔ | — |
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
| `THR-003` | Metodologia estruturada aplicada com cobertura mínima garantida | ✔ | ✔ | ✔ | — |
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
| `DEP-002` | SCA integrado em pipeline com bloqueio por política de severidade | ▲ | ▲ | ▲ | CTX-CRA-P01 |
| `DEP-003` | Versões de dependências fixas e auditáveis | ✔ | ✔ | ✔ | — |
| `DEP-004` | Proibição de dependências introduzidas por cópia manual | ✔ | ✔ | ✔ | — |
| `DEP-005` | Registries e repositórios de origem controlados | — | ✔ | ✔ | — |
| `DEP-006` | Aprovação formal para introdução de novas dependências | ▲ | ▲ | ▲ | CTX-CRA-P03 |
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
| `OPS-016` | Cópias de segurança com restauro testado | ✔ | ✔ | ✔ | — |
| `OPS-017` | Objectivos e procedimento de recuperação da aplicação | — | ✔ | ✔ | — |
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
| `GOV-014` | Revisão periódica de acesso aos sistemas de suporte (least privilege) | ✔ | ✔ | ✔ | — |
| `GOV-015` | Divulgação coordenada de vulnerabilidades com canal de receção publicado | ▲ | ▲ | ▲ | CTX-CRA-P04 |
| `GOV-016` | Contas privilegiadas e de administração dos sistemas de suporte | ✔ | ✔ | ✔ | — |
| `GOV-017` | Ciclo de vida das identidades com acesso aos sistemas | ✔ | ✔ | ✔ | — |
| `CTX-CRA-R01` | Período de apoio determinado, comunicado e cumprido | ▲ | ▲ | ▲ | — |
| `CTX-CRA-R02` | Distribuição e mecanismo de actualizações de segurança no utilizador | ▲ | ▲ | ▲ | — |
| `CTX-CRA-R03` | Avisos de segurança públicos sobre vulnerabilidades corrigidas | ▲ | ▲ | ▲ | — |
| `CTX-CRA-R04` | Comunicação ao mantenedor de vulnerabilidades em componentes | ▲ | ▲ | ▲ | — |
| `CTX-CRA-R05` | Critério de incidente grave | ▲ | ▲ | ▲ | — |

## Mapa de evidência da documentação técnica {#mapa-evidencia}

Obrigações documentais do regime (anexo VII do CRA) ligadas aos artefactos do Manual que as alimentam. «Apoia evidência»: o Manual produz a evidência de engenharia e a redacção do documento é de quem coloca o produto no mercado. As lacunas e o que fica fora de âmbito aparecem com a razão. A lista vem da matriz de cobertura do Manual.

| Obrigação | Referência | Força | Como o Manual responde | Nota |
|---|---|---|---|---|
| CRA-AnxVII-7 | Anexo VII, ponto 7 | Fora de âmbito | — | Obrigação do plano da conformidade formal/mercado (declaração UE, marcação CE, organismos notificados, autoridades); fora do âmbito de um manual de engenharia de segurança de software — o próprio Manual declara-o fora («não substitui»). |
| CRA-AnxVII-1 | Anexo VII, ponto 1 | Apoia evidência | [Política 09 §4.1](/sbd-toe/assets/policies/policy-arquitetura-segura#41-arranque-de-projeto-ou-épico-significativo); [Cap. 11 US-09](/sbd-toe/sbd-manual/deploy-seguro/aplicacao-lifecycle#us-09---versionamento-semântico-e-changelog-técnico) | — |
| CRA-AnxVII-2a | Anexo VII, ponto 2, alínea a) | Cobre | `ARC-010`; `ARC-004`; [Política 09 §4.1](/sbd-toe/assets/policies/policy-arquitetura-segura#41-arranque-de-projeto-ou-épico-significativo) | — |
| CRA-AnxVII-2b | Anexo VII, ponto 2, alínea b) | Cobre | `DEP-001`; [Política 12 §4](/sbd-toe/assets/policies/policy-excecoes-cve#4-tipos-de-exceção); `DST-003`; `GOV-015`; `CTX-CRA-R02` | — |
| CRA-AnxVII-2c | Anexo VII, ponto 2, alínea c) | Cobre | `CIC-001`; `CIC-005`; [Política 20 §7](/sbd-toe/assets/policies/policy-release-seguro#7-rastreabilidade-ponta-a-ponta) | — |
| CRA-AnxVII-3 | Anexo VII, ponto 3 | Apoia evidência | `THR-001`; `THR-006` | A ligação ao anexo I é redigida pelo fabricante na documentação técnica; o Manual fornece a evidência (ver o mapa de evidência). |
| CRA-AnxVII-4 | Anexo VII, ponto 4 | Cobre | `CTX-CRA-R01` | — |
| CRA-AnxVII-5 | Anexo VII, ponto 5 | Fora de âmbito | — | Lista de normas harmonizadas/especificações comuns aplicadas: plano da conformidade. |
| CRA-AnxVII-6 | Anexo VII, ponto 6 | Apoia evidência | `TST-004`; [Política 19 §5](/sbd-toe/assets/policies/policy-estrategia-testes#5-rastreabilidade-e-evidência-por-release) | A ligação ao anexo I é redigida pelo fabricante na documentação técnica; o Manual fornece a evidência (ver o mapa de evidência). |
| CRA-AnxVII-8 | Anexo VII, ponto 8 | Cobre | [Política 11 §8.2](/sbd-toe/assets/policies/policy-sbom#82-prazos-de-retenção-mínimos); [Política 11 §10](/sbd-toe/assets/policies/policy-sbom#10-responsabilidades) | — |

## Obrigações do regime por força de cobertura {#forca}

Contagem das obrigações do regime na matriz de cobertura (excluídas as dirigidas às autoridades). A secção [«O que este Manual cobre e o que fica de fora»](#cobertura) lista-as.

| Força | Obrigações |
|---|--:|
| Cobre | 47 |
| Parcial | 20 |
| Apoia evidência | 20 |
| Lacuna | 7 |
| Fora de âmbito | 97 |

## O que este Manual cobre e o que fica de fora {#cobertura}

Todas as obrigações do regime, na matriz de cobertura do Manual, em três categorias: o que o Manual **cobre**, e de que forma; as **lacunas declaradas** (o que não cobre por omissão); e o que fica **fora de âmbito**, com a razão. Nenhuma obrigação fica em silêncio. As 46 obrigações dirigidas às autoridades não criam dever para a organização e não entram nas listas.

### Cobre (67) {#cobre}

Força «cobre» ou «apoia evidência». A forma é a resposta do Manual: requisito do catálogo, política, secção, piso ou requisito acrescentado pelo regime.

| Obrigação | Referência | Força | Forma |
|---|---|---|---|
| CRA-12-1 | Art. 12.º, n.º 1 | Apoia evidência | `ARC-014`; `THR-008` |
| CRA-13-2 | Art. 13.º, n.º 2 | Cobre | `CLA-001`; `THR-001`; [Política 08 §4.1](/sbd-toe/assets/policies/policy-threat-modeling#41-triggers-obrigatórios); [Política 04 §1](/sbd-toe/assets/policies/policy-revisao-periodica-risco#1-objetivo) |
| CRA-13-5 | Art. 13.º, n.º 5 | Cobre | `DEP-006`; [Política 10 §3.1](/sbd-toe/assets/policies/policy-dependencias#31-validação-obrigatória-por-dependência-nova); `GOV-007`; `DEP-002` |
| CRA-13-6-a | Art. 13.º, n.º 6, 1.º período | Cobre | `CTX-CRA-R04` |
| CRA-13-6-b | Art. 13.º, n.º 6, 2.º período | Cobre | `CTX-CRA-R04` |
| CRA-13-7 | Art. 13.º, n.º 7 | Cobre | `DEP-010`; `TST-003`; `GOV-009`; [Política 10 §8](/sbd-toe/assets/policies/policy-dependencias#8-alertas-de-vulnerabilidades-em-produção) |
| CRA-13-8-p1 | Art. 13.º, n.º 8, 1.º parágrafo | Cobre | [Política 19 §4.3](/sbd-toe/assets/policies/policy-estrategia-testes#43-slas-de-triagem-e-resolução); `DEP-007`; [Política 12 §6](/sbd-toe/assets/policies/policy-excecoes-cve#6-prazos-máximos-e-reavaliação); `GOV-015`; `CTX-CRA-R01`; `CTX-CRA-R02`; `CTX-CRA-R03` |
| CRA-13-8-p2 | Art. 13.º, n.º 8, 2.º parágrafo | Cobre | `CTX-CRA-R01` |
| CRA-13-8-p3 | Art. 13.º, n.º 8, 3.º parágrafo | Cobre | `CTX-CRA-R01` |
| CRA-13-8-p5 | Art. 13.º, n.º 8, 5.º parágrafo | Cobre | `CTX-CRA-R01` |
| CRA-13-8-p6 | Art. 13.º, n.º 8, 6.º parágrafo | Cobre | [Política 12 §4](/sbd-toe/assets/policies/policy-excecoes-cve#4-tipos-de-exceção); [Política 19 §4.2](/sbd-toe/assets/policies/policy-estrategia-testes#42-triagem-formal); `DEP-007`; `GOV-015`; `GOV-015` |
| CRA-13-9 | Art. 13.º, n.º 9 | Cobre | `CTX-CRA-R01` |
| CRA-13-11 | Art. 13.º, n.º 11 | Cobre | `CTX-CRA-R01` |
| CRA-13-12-p1 | Art. 13.º, n.º 12, 1.º parágrafo | Apoia evidência | [Política 06 §10](/sbd-toe/assets/policies/policy-rastreabilidade#10-prazos-de-retenção-mínimos); [Política 11 §8.2](/sbd-toe/assets/policies/policy-sbom#82-prazos-de-retenção-mínimos) |
| CRA-13-12-p2 | Art. 13.º, n.º 12, 2.º parágrafo | Apoia evidência | [Política 06 §10](/sbd-toe/assets/policies/policy-rastreabilidade#10-prazos-de-retenção-mínimos); `TST-004` |
| CRA-13-15 | Art. 13.º, n.º 15 | Apoia evidência | [Cap. 11 US-09](/sbd-toe/sbd-manual/deploy-seguro/aplicacao-lifecycle#us-09---versionamento-semântico-e-changelog-técnico); [Política 20 §8](/sbd-toe/assets/policies/policy-release-seguro#8-registo-histórico-de-releases) |
| CRA-13-17 | Art. 13.º, n.º 17 | Cobre | `GOV-015` |
| CRA-13-19-p2 | Art. 13.º, n.º 19, 2.º parágrafo | Cobre | `CTX-CRA-R01` |
| CRA-13-21 | Art. 13.º, n.º 21 | Apoia evidência | `DST-007`; `DPL-005` |
| CRA-14-1 | Art. 14.º, n.º 1 | Cobre | [Política 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória); [Política 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória); [Política 12 §6](/sbd-toe/assets/policies/policy-excecoes-cve#6-prazos-máximos-e-reavaliação); [Cap. 05 US-11](/sbd-toe/sbd-manual/dependencias-sbom-sca/aplicacao-lifecycle#us-11---alertas-sobre-vulnerabilidades-em-componentes-usados) |
| CRA-14-3 | Art. 14.º, n.os 3 e 5 | Cobre | `CTX-CRA-R05`; [Política 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória); [Política 32 §4.1](/sbd-toe/assets/policies/policy-irp#41-triagem-t0----15-minutos-de-detecção) |
| CRA-14-4-c | Art. 14.º, n.º 4, alínea c) | Cobre | [Política 32 §6.1](/sbd-toe/assets/policies/policy-irp#61-critério-e-conteúdo-mínimo-por-regime); [Política 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória) |
| CRA-14-8 | Art. 14.º, n.º 8 | Cobre | [Política 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória); [Política 32 §7](/sbd-toe/assets/policies/policy-irp#7-comunicação-durante-o-incidente); `DST-007` |
| CRA-17-2 | Art. 17.º, n.º 2 | Apoia evidência | [Política 32 §9](/sbd-toe/assets/policies/policy-irp#9-responsabilidades) |
| CRA-23 | Art. 23.º | Apoia evidência | [Política 33 §8](/sbd-toe/assets/policies/policy-contratacao-segura#8-registo-e-rastreabilidade); [Política 10 §3.2](/sbd-toe/assets/policies/policy-dependencias#32-registo-de-aprovação) |
| CRA-31-1 | Art. 31.º, n.º 1 | Apoia evidência | [Política 06 §10](/sbd-toe/assets/policies/policy-rastreabilidade#10-prazos-de-retenção-mínimos); [Política 09 §4.1](/sbd-toe/assets/policies/policy-arquitetura-segura#41-arranque-de-projeto-ou-épico-significativo); [Política 11 §8.2](/sbd-toe/assets/policies/policy-sbom#82-prazos-de-retenção-mínimos) |
| CRA-31-2 | Art. 31.º, n.º 2 | Apoia evidência | `THR-006`; `ARC-010` |
| CRA-69-3 | Art. 69.º, n.º 3 | Cobre | [Política 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória) |
| CRA-AnxI-P1-1 | Anexo I, parte I, ponto 1 | Cobre | `CLA-003`; `CLA-001`; `THR-001` |
| CRA-AnxI-P1-2a | Anexo I, parte I, ponto 2, alínea a) | Cobre | `DEP-002`; [Política 20 §5.1](/sbd-toe/assets/policies/policy-release-seguro#51-critérios-de-bloqueio-automático-no-go); `TST-005`; `TST-008`; [Política 12 §8](/sbd-toe/assets/policies/policy-excecoes-cve#8-integração-no-pipeline) |
| CRA-AnxI-P1-2c | Anexo I, parte I, ponto 2, alínea c) | Cobre | `CTX-CRA-R02` |
| CRA-AnxI-P1-2d | Anexo I, parte I, ponto 2, alínea d) | Cobre | `ACC-001`; `ACC-003`; `AUT-001`; `AUT-010` |
| CRA-AnxI-P1-2e | Anexo I, parte I, ponto 2, alínea e) | Cobre | `ENC-001`; `ENC-002`; `ENC-003` |
| CRA-AnxI-P1-2h | Anexo I, parte I, ponto 2, alínea h) | Cobre | `API-004`; `FIL-001`; `OPS-015`; `DPL-005`; [Política 32 §4.5](/sbd-toe/assets/policies/policy-irp#45-recuperação) |
| CRA-AnxI-P1-2j | Anexo I, parte I, ponto 2, alínea j) | Cobre | `ARC-002`; `API-002`; `CNT-003`; [Política 09 §3](/sbd-toe/assets/policies/policy-arquitetura-segura#3-princípios-de-arquitetura-segura) |
| CRA-AnxI-P1-2k | Anexo I, parte I, ponto 2, alínea k) | Cobre | `ARC-006`; `ACC-002`; `CNT-004`; `CNT-006` |
| CRA-AnxI-P2-1 | Anexo I, parte II, ponto 1 | Cobre | `DEP-001`; [Política 11 §3.2](/sbd-toe/assets/policies/policy-sbom#32-conteúdo-mínimo-obrigatório); `DEP-010` |
| CRA-AnxI-P2-2 | Anexo I, parte II, ponto 2 | Cobre | [Política 19 §4.3](/sbd-toe/assets/policies/policy-estrategia-testes#43-slas-de-triagem-e-resolução); `DEP-007`; `TST-003`; `CTX-CRA-R02` |
| CRA-AnxI-P2-3 | Anexo I, parte II, ponto 3 | Cobre | `TST-001`; `TST-008`; [Política 19 §5](/sbd-toe/assets/policies/policy-estrategia-testes#5-rastreabilidade-e-evidência-por-release) |
| CRA-AnxI-P2-4 | Anexo I, parte II, ponto 4 | Cobre | [Cap. 11 US-09](/sbd-toe/sbd-manual/deploy-seguro/aplicacao-lifecycle#us-09---versionamento-semântico-e-changelog-técnico); `CTX-CRA-R03`; `GOV-015` |
| CRA-AnxI-P2-5 | Anexo I, parte II, ponto 5 | Cobre | `GOV-015` |
| CRA-AnxI-P2-6 | Anexo I, parte II, ponto 6 | Cobre | `GOV-015` |
| CRA-AnxI-P2-7 | Anexo I, parte II, ponto 7 | Cobre | `DST-003`; `CIC-007`; `DPL-002`; `CTX-CRA-R02`; `DST-003` |
| CRA-AnxI-P2-8 | Anexo I, parte II, ponto 8 | Cobre | `CTX-CRA-R02` |
| CRA-AnxII-2 | Anexo II, ponto 2 | Cobre | `GOV-015` |
| CRA-AnxII-3 | Anexo II, ponto 3 | Apoia evidência | [Cap. 11 US-09](/sbd-toe/sbd-manual/deploy-seguro/aplicacao-lifecycle#us-09---versionamento-semântico-e-changelog-técnico) |
| CRA-AnxII-4 | Anexo II, ponto 4 | Apoia evidência | [Política 09 §4.1](/sbd-toe/assets/policies/policy-arquitetura-segura#41-arranque-de-projeto-ou-épico-significativo); `ARC-001` |
| CRA-AnxII-5 | Anexo II, ponto 5 | Apoia evidência | [Cap. 03 US-13](/sbd-toe/sbd-manual/threat-modeling/aplicacao-lifecycle#us-13---derivação-de-abusemisuse-cases-para-o-backlog); `THR-001` |
| CRA-AnxII-7 | Anexo II, ponto 7 | Cobre | `CTX-CRA-R01` |
| CRA-AnxII-8c | Anexo II, ponto 8, alínea c) | Cobre | `CTX-CRA-R02` |
| CRA-AnxII-8e | Anexo II, ponto 8, alínea e) | Cobre | `CTX-CRA-R02` |
| CRA-AnxII-8f | Anexo II, ponto 8, alínea f) | Apoia evidência | `DST-004`; `DEP-001` |
| CRA-AnxVII-1 | Anexo VII, ponto 1 | Apoia evidência | [Política 09 §4.1](/sbd-toe/assets/policies/policy-arquitetura-segura#41-arranque-de-projeto-ou-épico-significativo); [Cap. 11 US-09](/sbd-toe/sbd-manual/deploy-seguro/aplicacao-lifecycle#us-09---versionamento-semântico-e-changelog-técnico) |
| CRA-AnxVII-2a | Anexo VII, ponto 2, alínea a) | Cobre | `ARC-010`; `ARC-004`; [Política 09 §4.1](/sbd-toe/assets/policies/policy-arquitetura-segura#41-arranque-de-projeto-ou-épico-significativo) |
| CRA-AnxVII-2b | Anexo VII, ponto 2, alínea b) | Cobre | `DEP-001`; [Política 12 §4](/sbd-toe/assets/policies/policy-excecoes-cve#4-tipos-de-exceção); `DST-003`; `GOV-015`; `CTX-CRA-R02` |
| CRA-AnxVII-2c | Anexo VII, ponto 2, alínea c) | Cobre | `CIC-001`; `CIC-005`; [Política 20 §7](/sbd-toe/assets/policies/policy-release-seguro#7-rastreabilidade-ponta-a-ponta) |
| CRA-AnxVII-3 | Anexo VII, ponto 3 | Apoia evidência | `THR-001`; `THR-006` |
| CRA-AnxVII-4 | Anexo VII, ponto 4 | Cobre | `CTX-CRA-R01` |
| CRA-AnxVII-6 | Anexo VII, ponto 6 | Apoia evidência | `TST-004`; [Política 19 §5](/sbd-toe/assets/policies/policy-estrategia-testes#5-rastreabilidade-e-evidência-por-release) |
| CRA-AnxVII-8 | Anexo VII, ponto 8 | Cobre | [Política 11 §8.2](/sbd-toe/assets/policies/policy-sbom#82-prazos-de-retenção-mínimos); [Política 11 §10](/sbd-toe/assets/policies/policy-sbom#10-responsabilidades) |
| CRA-AnxVIII-PI-2 | Anexo VIII, parte I (módulo A), ponto 2 | Apoia evidência | [Política 06 §10](/sbd-toe/assets/policies/policy-rastreabilidade#10-prazos-de-retenção-mínimos) |
| CRA-AnxVIII-PI-3 | Anexo VIII, parte I (módulo A), ponto 3 | Cobre | [Política 20 §5.1](/sbd-toe/assets/policies/policy-release-seguro#51-critérios-de-bloqueio-automático-no-go); [Política 19 §4.3](/sbd-toe/assets/policies/policy-estrategia-testes#43-slas-de-triagem-e-resolução); `CIC-001`; `GOV-015`; `CTX-CRA-R01`; `CTX-CRA-R02`; `CTX-CRA-R03` |
| CRA-AnxVIII-PII-7 | Anexo VIII, parte II (módulo B), ponto 7, 2.º parágrafo | Apoia evidência | `ARC-009`; `CLA-006` |
| CRA-AnxVIII-PIII-2 | Anexo VIII, parte III (módulo C), ponto 2 | Cobre | [Política 20 §6](/sbd-toe/assets/policies/policy-release-seguro#6-imutabilidade-do-artefacto); `DPL-002` |
| CRA-AnxVIII-PIV-2 | Anexo VIII, parte IV (módulo H), ponto 2 | Apoia evidência | `GOV-001`; `GOV-010` |
| CRA-AnxVIII-PIV-3.2 | Anexo VIII, parte IV (módulo H), ponto 3.2 | Cobre | `GOV-001`; `TST-001`; `TRN-001`; `GOV-011`; `GOV-015`; `CTX-CRA-R01`; `CTX-CRA-R02` |
| CRA-AnxVIII-PIV-3.4a3.5 | Anexo VIII, parte IV (módulo H), pontos 3.4 e 3.5 | Apoia evidência | `GOV-010` |

### Lacuna declarada (27) {#lacuna}

Força «parcial» ou «lacuna»: o Manual não cobre, ou cobre só em parte, e diz o que falta. As lacunas pendentes de uma ronda do AppSec Core estão marcadas com o nome da ronda.

| Obrigação | Referência | Força | Como o Manual responde | O que falta |
|---|---|---|---|---|
| CRA-4-3 | Art. 4.º, n.os 3 e 4 | Lacuna | — | Não há regra para canais beta/pré-lançamento de software inacabado: período limitado ao ensaio, sinal visível de não conformidade e utilização exclusiva para ensaio. |
| CRA-6 | Art. 6.º | Parcial | [Política 20 §5.1](/sbd-toe/assets/policies/policy-release-seguro#51-critérios-de-bloqueio-automático-no-go); `DEP-001`; `TST-001`; `GOV-015`; `CTX-CRA-R01`; `CTX-CRA-R02`; `CTX-CRA-R03` | Cobertura agregada das partes I e II do anexo I é parcial: o Manual não prescreve a reposição do estado original (P1-2b) nem a remoção/transferência segura de dados (P1-2m). A divulgação coordenada e o contacto (GOV-015), os avisos (CTX-CRA-R03), o mecanismo e a distribuição de atualizações (CTX-CRA-R02) e o período de apoio (CTX-CRA-R01) estão prescritos. |
| CRA-7-1 | Art. 7.º, n.os 1 e 2 | Lacuna | — | O modelo de classificação do Manual (eixos E/D/I → L1–L3, CLA-001) não identifica se o produto pertence às categorias do anexo III (classes I/II) ou do anexo IV, que determinam a rota de avaliação da conformidade. |
| CRA-13-1 | Art. 13.º, n.º 1 | Parcial | `REQ-001`; `CLA-003`; [Política 20 §5.1](/sbd-toe/assets/policies/policy-release-seguro#51-critérios-de-bloqueio-automático-no-go); `CTX-CRA-R02` | Conceção/desenvolvimento conformes com toda a parte I do anexo I: faltam reposição do estado original, remoção e transferência seguras de todos os dados, minimização de dados não pessoais e comunicação de corrupções/acessos ao utilizador em L1. O mecanismo de atualização do produto está em CTX-CRA-R02. |
| CRA-13-3 | Art. 13.º, n.º 3 | Parcial | `THR-006`; [Política 08 §4.2](/sbd-toe/assets/policies/policy-threat-modeling#42-cadência-periódica) | A avaliação de riscos do Manual não indica, requisito a requisito, se e como se aplicam as alíneas do anexo I, parte I, ponto 2, nem como se aplicam o ponto 1 e a parte II; não é estruturada por finalidade prevista, utilização razoavelmente previsível, ambiente operacional e período de utilização; a atualização não está ancorada ao período de apoio. |
| CRA-13-4 | Art. 13.º, n.º 4 | Parcial | [Política 07 §9](/sbd-toe/assets/policies/policy-requisitos-seguranca#9-gestão-de-exceções-a-requisitos); `GOV-009` | Existe justificação formal de requisitos não implementados (exceções), mas não a integração da avaliação de riscos na documentação técnica (anexo VII) nem a justificação por requisito essencial do CRA considerado não aplicável. |
| CRA-13-10 | Art. 13.º, n.º 10 | Lacuna | — | Sem política de versões suportadas: não prevê a faculdade de corrigir só a última versão nem a condição de acesso gratuito a ela. |
| CRA-13-13 | Art. 13.º, n.º 13 | Parcial | [Política 06 §10](/sbd-toe/assets/policies/policy-rastreabilidade#10-prazos-de-retenção-mínimos); [Política 11 §8.2](/sbd-toe/assets/policies/policy-sbom#82-prazos-de-retenção-mínimos); [Política 08 §9.3](/sbd-toe/assets/policies/policy-threat-modeling#93-retenção) | A regra dos 10 anos cobre a SBOM e o pacote de evidências; outros elementos da documentação técnica (versões históricas do threat model: 3 anos; registos de aprovação: 1–3 anos) não estão abrangidos; a declaração UE está fora de âmbito. |
| CRA-13-14 | Art. 13.º, n.º 14 | Parcial | `ARC-009`; `CLA-006`; `REQ-005`; `THR-006` | Alterações de conceção/processo disparam revisão, mas falta acompanhar alterações das normas harmonizadas/especificações comuns que servem de referência à declaração de conformidade. |
| CRA-13-18 | Art. 13.º, n.º 18 | Parcial | [Política 20 §4.1](/sbd-toe/assets/policies/policy-release-seguro#41-critérios-obrigatórios) | Só existe o critério genérico «Documentação de segurança atualizada» (recomendado em L2, obrigatório em L3); falta prescrever o conteúdo do anexo II, o destinatário (utilizador), a língua e a conservação por 10 anos/período de apoio. |
| CRA-14-2-a | Art. 14.º, n.º 2, alínea a) | Parcial | [Política 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória); [Política 32 §4.1](/sbd-toe/assets/policies/policy-irp#41-triagem-t0----15-minutos-de-detecção) | O prazo de 24 h e o registo do momento do conhecimento estão prescritos; falta o conteúdo mínimo (indicação dos Estados-Membros onde o produto foi disponibilizado). |
| CRA-14-2-b | Art. 14.º, n.º 2, alínea b) | Parcial | [Política 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória) | Prazo de 72 h prescrito; falta o conteúdo mínimo (informação geral do produto, natureza da exploração e da vulnerabilidade, medidas corretivas tomadas e a tomar pelos utilizadores, sensibilidade da informação). |
| CRA-14-2-c | Art. 14.º, n.º 2, alínea c) | Parcial | [Política 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória) | Prazo de 14 dias após a medida corretiva prescrito (e a regra de contagem está correta na nota da Política 32 §6); falta o conteúdo do relatório final (gravidade e impacto, agente malicioso, pormenores da atualização). |
| CRA-14-4-a | Art. 14.º, n.º 4, alínea a) | Parcial | [Política 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória) | Prazo de 24 h prescrito; falta indicar a suspeita de ato ilícito/malicioso e os Estados-Membros. |
| CRA-14-4-b | Art. 14.º, n.º 4, alínea b) | Parcial | [Política 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória) | Prazo de 72 h prescrito; falta o conteúdo (natureza, avaliação inicial, medidas, sensibilidade). |
| CRA-14-6 | Art. 14.º, n.º 6 | Lacuna | — | A linha CRA da Política 32 §6 não prevê o relatório intercalar a pedido da CSIRT (existe só na linha NIS2). |
| CRA-14-7 | Art. 14.º, n.º 7 | Parcial | [Política 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória) | Nomeia a CSIRT designada como coordenadora e a plataforma única, mas não a regra de determinação (Estado-Membro do estabelecimento principal e regra subsidiária para fabricantes fora da UE). |
| CRA-AnxI-P1-2b | Anexo I, parte I, ponto 2, alínea b) | Parcial | `CFG-001`; [Política 09 §3](/sbd-toe/assets/policies/policy-arquitetura-segura#3-princípios-de-arquitetura-segura); `CNT-003` | Configuração endurecida do ambiente de produção e «fail secure» existem, mas não configuração segura por defeito do produto entregue ao utilizador nem a possibilidade de repor o estado original. |
| CRA-AnxI-P1-2f | Anexo I, parte I, ponto 2, alínea f) | Parcial | `ENC-009`; `INT-005`; `CIC-007`; `DST-003`; `CFG-007`; `LOG-003` | Integridade de programas (assinatura) e de mensagens coberta em L2/L3; integridade de dados críticos e de configuração só em L3; falta comunicar as corrupções ao utilizador. |
| CRA-AnxI-P1-2g | Anexo I, parte I, ponto 2, alínea g) | Parcial | `PRI-001` | A minimização cobre só dados pessoais (PRI-001, desde L1); o CRA abrange dados «pessoais ou outros». |
| CRA-AnxI-P1-2i | Anexo I, parte I, ponto 2, alínea i) | Parcial | `CNT-012`; `ARC-006` | Isolamento e políticas de rede contêm o impacto lateral, mas não há requisito para que as funções do próprio produto não degradem outros dispositivos/redes (p. ex. limitação de tráfego de saída, tempestades de retry). |
| CRA-AnxI-P1-2l | Anexo I, parte I, ponto 2, alínea l) | Parcial | `LOG-001`; `OPS-001`; `OPS-002` | Registo e monitorização de atividade interna prescritos; falta a opção de exclusão (opt-out) para o utilizador e a orientação para disponibilizar essa informação de segurança ao utilizador. |
| CRA-AnxI-P1-2m | Anexo I, parte I, ponto 2, alínea m) | Parcial | `PRI-003` | Apagamento e exportação a pedido cobrem só os dados pessoais de um titular (PRI-003, desde L1); falta a remoção pelo utilizador de todos os dados e parâmetros, de forma segura e permanente, e a transferência segura para outros produtos. |
| CRA-AnxII-8a | Anexo II, ponto 8, alínea a) | Lacuna | — | Não prescreve guia de colocação em funcionamento e utilização segura para o utilizador (hardening guide); o critério «Documentação de segurança atualizada» da Política 20 §4.1 não define conteúdo. |
| CRA-AnxII-8b | Anexo II, ponto 8, alínea b) | Lacuna | — | Não há instrução ao utilizador sobre como alterações do produto afetam a segurança dos dados. |
| CRA-AnxII-8d | Anexo II, ponto 8, alínea d) | Lacuna | — | Não há instruções de desativação segura e remoção de dados pelo utilizador (capacidade também em falta, CRA-AnxI-P1-2m). |
| CRA-AnxII-9 | Anexo II, ponto 9 | Parcial | `DST-004` | A SBOM é anexada a cada release (L2/L3), mas não se prescreve indicar ao utilizador onde lhe aceder quando o fabricante opta por a disponibilizar. |

### Fora de âmbito (97) {#fora-de-ambito}

Obrigações que o Manual declara fora de âmbito, com a razão.

| Obrigação | Referência | Razão |
|---|---|---|
| CRA-2-1 | Art. 2.º, n.º 1 | Disposição delimitadora de âmbito/qualificação jurídica do produto; não cria dever de engenharia. |
| CRA-2-2a7 | Art. 2.º, n.os 2 a 8 | Disposição delimitadora de âmbito/qualificação jurídica do produto; não cria dever de engenharia. |
| CRA-4-2 | Art. 4.º, n.º 2 | Exposição de protótipos em feiras/demonstrações: logística de mercado, não engenharia. |
| CRA-8-1 | Art. 8.º, n.º 1 | Obrigação do plano da conformidade formal/mercado (declaração UE, marcação CE, organismos notificados, autoridades); fora do âmbito de um manual de engenharia de segurança de software — o próprio Manual declara-o fora («não substitui»). |
| CRA-11 | Art. 11.º | Articulação entre atos legislativos (RSGP); plano jurídico. |
| CRA-12-2a4 | Art. 12.º, n.os 2 a 4 | Obrigação do plano da conformidade formal/mercado (declaração UE, marcação CE, organismos notificados, autoridades); fora do âmbito de um manual de engenharia de segurança de software — o próprio Manual declara-o fora («não substitui»). |
| CRA-13-12-p3 | Art. 13.º, n.º 12, 3.º parágrafo | Obrigação do plano da conformidade formal/mercado (declaração UE, marcação CE, organismos notificados, autoridades); fora do âmbito de um manual de engenharia de segurança de software — o próprio Manual declara-o fora («não substitui»). |
| CRA-13-16 | Art. 13.º, n.º 16 | Identificação do fabricante no produto/embalagem: dever de rotulagem. |
| CRA-13-19-p1 | Art. 13.º, n.º 19, 1.º parágrafo | Indicação comercial da data de fim do apoio no ato de compra; plano de mercado. |
| CRA-13-20 | Art. 13.º, n.º 20 | Obrigação do plano da conformidade formal/mercado (declaração UE, marcação CE, organismos notificados, autoridades); fora do âmbito de um manual de engenharia de segurança de software — o próprio Manual declara-o fora («não substitui»). |
| CRA-13-22 | Art. 13.º, n.º 22 | Relação com autoridades de fiscalização/regime sancionatório; plano jurídico, não de engenharia. |
| CRA-13-23 | Art. 13.º, n.º 23 | Relação com autoridades de fiscalização/regime sancionatório; plano jurídico, não de engenharia. |
| CRA-15-1a2 | Art. 15.º, n.os 1 e 2 | Faculdade (notificação voluntária), não dever; a sua ausência não é lacuna, embora seja prática recomendável de PSIRT. |
| CRA-18-1a2 | Art. 18.º, n.os 1 e 2 | Dever de outro operador económico (importador/distribuidor/mandatário), não do processo de engenharia do fabricante. |
| CRA-18-3 | Art. 18.º, n.º 3, proémio | Dever de outro operador económico (importador/distribuidor/mandatário), não do processo de engenharia do fabricante. |
| CRA-18-3-a | Art. 18.º, n.º 3, alínea a) | Dever de outro operador económico (importador/distribuidor/mandatário), não do processo de engenharia do fabricante. |
| CRA-18-3-b | Art. 18.º, n.º 3, alínea b) | Dever de outro operador económico (importador/distribuidor/mandatário), não do processo de engenharia do fabricante. |
| CRA-18-3-c | Art. 18.º, n.º 3, alínea c) | Dever de outro operador económico (importador/distribuidor/mandatário), não do processo de engenharia do fabricante. |
| CRA-19-1 | Art. 19.º, n.º 1 | Dever de outro operador económico (importador/distribuidor/mandatário), não do processo de engenharia do fabricante. |
| CRA-19-2-a | Art. 19.º, n.º 2, alínea a) | Dever de outro operador económico (importador/distribuidor/mandatário), não do processo de engenharia do fabricante. |
| CRA-19-2-b | Art. 19.º, n.º 2, alínea b) | Dever de outro operador económico (importador/distribuidor/mandatário), não do processo de engenharia do fabricante. |
| CRA-19-2-c | Art. 19.º, n.º 2, alínea c) | Dever de outro operador económico (importador/distribuidor/mandatário), não do processo de engenharia do fabricante. |
| CRA-19-2-d | Art. 19.º, n.º 2, alínea d) | Dever de outro operador económico (importador/distribuidor/mandatário), não do processo de engenharia do fabricante. |
| CRA-19-2-p2 | Art. 19.º, n.º 2, 2.º parágrafo | Dever de outro operador económico (importador/distribuidor/mandatário), não do processo de engenharia do fabricante. |
| CRA-19-3-p1 | Art. 19.º, n.º 3, 1.º parágrafo | Dever de outro operador económico (importador/distribuidor/mandatário), não do processo de engenharia do fabricante. |
| CRA-19-3-p2 | Art. 19.º, n.º 3, 2.º parágrafo | Dever de outro operador económico (importador/distribuidor/mandatário), não do processo de engenharia do fabricante. |
| CRA-19-4 | Art. 19.º, n.º 4 | Dever de outro operador económico (importador/distribuidor/mandatário), não do processo de engenharia do fabricante. |
| CRA-19-5-p1 | Art. 19.º, n.º 5, 1.º parágrafo | Dever de outro operador económico (importador/distribuidor/mandatário), não do processo de engenharia do fabricante. |
| CRA-19-6 | Art. 19.º, n.º 6 | Dever de outro operador económico (importador/distribuidor/mandatário), não do processo de engenharia do fabricante. |
| CRA-19-7 | Art. 19.º, n.º 7 | Dever de outro operador económico (importador/distribuidor/mandatário), não do processo de engenharia do fabricante. |
| CRA-19-8 | Art. 19.º, n.º 8 | Dever de outro operador económico (importador/distribuidor/mandatário), não do processo de engenharia do fabricante. |
| CRA-20-1 | Art. 20.º, n.º 1 | Dever de outro operador económico (importador/distribuidor/mandatário), não do processo de engenharia do fabricante. |
| CRA-20-2-a | Art. 20.º, n.º 2, alínea a) | Dever de outro operador económico (importador/distribuidor/mandatário), não do processo de engenharia do fabricante. |
| CRA-20-2-b | Art. 20.º, n.º 2, alínea b) | Dever de outro operador económico (importador/distribuidor/mandatário), não do processo de engenharia do fabricante. |
| CRA-20-3 | Art. 20.º, n.º 3 | Dever de outro operador económico (importador/distribuidor/mandatário), não do processo de engenharia do fabricante. |
| CRA-20-4-p1 | Art. 20.º, n.º 4, 1.º parágrafo | Dever de outro operador económico (importador/distribuidor/mandatário), não do processo de engenharia do fabricante. |
| CRA-20-5 | Art. 20.º, n.º 5 | Dever de outro operador económico (importador/distribuidor/mandatário), não do processo de engenharia do fabricante. |
| CRA-20-6 | Art. 20.º, n.º 6 | Dever de outro operador económico (importador/distribuidor/mandatário), não do processo de engenharia do fabricante. |
| CRA-19-5-p2 | Art. 19.º, n.º 5, 2.º parágrafo | Dever de outro operador económico (importador/distribuidor/mandatário), não do processo de engenharia do fabricante. |
| CRA-20-4-p2 | Art. 20.º, n.º 4, 2.º parágrafo | Dever de outro operador económico (importador/distribuidor/mandatário), não do processo de engenharia do fabricante. |
| CRA-21 | Art. 21.º | Requalificação jurídica como fabricante. |
| CRA-22 | Art. 22.º | Requalificação jurídica como fabricante. |
| CRA-24-1 | Art. 24.º, n.º 1 | Dever do administrador de software de código aberto (steward); o Manual não modela esse papel. |
| CRA-24-2 | Art. 24.º, n.º 2 | Dever do administrador de software de código aberto (steward); o Manual não modela esse papel. |
| CRA-52-3 | Art. 52.º, n.º 3 | Dever do administrador de software de código aberto (steward); o Manual não modela esse papel. |
| CRA-24-3 | Art. 24.º, n.º 3 | Dever do administrador de software de código aberto (steward); o Manual não modela esse papel. |
| CRA-28-1a2 | Art. 28.º, n.os 1 e 2 | Obrigação do plano da conformidade formal/mercado (declaração UE, marcação CE, organismos notificados, autoridades); fora do âmbito de um manual de engenharia de segurança de software — o próprio Manual declara-o fora («não substitui»). |
| CRA-28-3 | Art. 28.º, n.º 3 | Obrigação do plano da conformidade formal/mercado (declaração UE, marcação CE, organismos notificados, autoridades); fora do âmbito de um manual de engenharia de segurança de software — o próprio Manual declara-o fora («não substitui»). |
| CRA-28-4 | Art. 28.º, n.º 4 | Obrigação do plano da conformidade formal/mercado (declaração UE, marcação CE, organismos notificados, autoridades); fora do âmbito de um manual de engenharia de segurança de software — o próprio Manual declara-o fora («não substitui»). |
| CRA-30-1 | Art. 30.º, n.os 1 e 2 (e art. 29.º) | Obrigação do plano da conformidade formal/mercado (declaração UE, marcação CE, organismos notificados, autoridades); fora do âmbito de um manual de engenharia de segurança de software — o próprio Manual declara-o fora («não substitui»). |
| CRA-30-3a4 | Art. 30.º, n.os 3 e 4 | Obrigação do plano da conformidade formal/mercado (declaração UE, marcação CE, organismos notificados, autoridades); fora do âmbito de um manual de engenharia de segurança de software — o próprio Manual declara-o fora («não substitui»). |
| CRA-31-3a4 | Art. 31.º, n.os 3 e 4 | Obrigação do plano da conformidade formal/mercado (declaração UE, marcação CE, organismos notificados, autoridades); fora do âmbito de um manual de engenharia de segurança de software — o próprio Manual declara-o fora («não substitui»). |
| CRA-32-1 | Art. 32.º, n.º 1 | Obrigação do plano da conformidade formal/mercado (declaração UE, marcação CE, organismos notificados, autoridades); fora do âmbito de um manual de engenharia de segurança de software — o próprio Manual declara-o fora («não substitui»). |
| CRA-32-2 | Art. 32.º, n.º 2 | Obrigação do plano da conformidade formal/mercado (declaração UE, marcação CE, organismos notificados, autoridades); fora do âmbito de um manual de engenharia de segurança de software — o próprio Manual declara-o fora («não substitui»). |
| CRA-32-3 | Art. 32.º, n.º 3 | Obrigação do plano da conformidade formal/mercado (declaração UE, marcação CE, organismos notificados, autoridades); fora do âmbito de um manual de engenharia de segurança de software — o próprio Manual declara-o fora («não substitui»). |
| CRA-32-4 | Art. 32.º, n.º 4 | Obrigação do plano da conformidade formal/mercado (declaração UE, marcação CE, organismos notificados, autoridades); fora do âmbito de um manual de engenharia de segurança de software — o próprio Manual declara-o fora («não substitui»). |
| CRA-32-5 | Art. 32.º, n.º 5 | Obrigação do plano da conformidade formal/mercado (declaração UE, marcação CE, organismos notificados, autoridades); fora do âmbito de um manual de engenharia de segurança de software — o próprio Manual declara-o fora («não substitui»). |
| CRA-33-5 | Art. 33.º, n.º 5 | Obrigação do plano da conformidade formal/mercado (declaração UE, marcação CE, organismos notificados, autoridades); fora do âmbito de um manual de engenharia de segurança de software — o próprio Manual declara-o fora («não substitui»). |
| CRA-58 | Art. 58.º | Obrigação do plano da conformidade formal/mercado (declaração UE, marcação CE, organismos notificados, autoridades); fora do âmbito de um manual de engenharia de segurança de software — o próprio Manual declara-o fora («não substitui»). |
| CRA-AnxV | Anexo V | Obrigação do plano da conformidade formal/mercado (declaração UE, marcação CE, organismos notificados, autoridades); fora do âmbito de um manual de engenharia de segurança de software — o próprio Manual declara-o fora («não substitui»). |
| CRA-AnxVI | Anexo VI | Obrigação do plano da conformidade formal/mercado (declaração UE, marcação CE, organismos notificados, autoridades); fora do âmbito de um manual de engenharia de segurança de software — o próprio Manual declara-o fora («não substitui»). |
| CRA-AnxVII-7 | Anexo VII, ponto 7 | Obrigação do plano da conformidade formal/mercado (declaração UE, marcação CE, organismos notificados, autoridades); fora do âmbito de um manual de engenharia de segurança de software — o próprio Manual declara-o fora («não substitui»). |
| CRA-AnxVIII-PI-4 | Anexo VIII, parte I (módulo A), pontos 4.1 e 4.2 | Obrigação do plano da conformidade formal/mercado (declaração UE, marcação CE, organismos notificados, autoridades); fora do âmbito de um manual de engenharia de segurança de software — o próprio Manual declara-o fora («não substitui»). |
| CRA-AnxVIII-PI-5 | Anexo VIII, parte I (módulo A), ponto 5 | Obrigação do plano da conformidade formal/mercado (declaração UE, marcação CE, organismos notificados, autoridades); fora do âmbito de um manual de engenharia de segurança de software — o próprio Manual declara-o fora («não substitui»). |
| CRA-AnxVIII-PII-3 | Anexo VIII, parte II (módulo B), ponto 3 | Obrigação do plano da conformidade formal/mercado (declaração UE, marcação CE, organismos notificados, autoridades); fora do âmbito de um manual de engenharia de segurança de software — o próprio Manual declara-o fora («não substitui»). |
| CRA-AnxVIII-PII-10 | Anexo VIII, parte II (módulo B), ponto 10 | Obrigação do plano da conformidade formal/mercado (declaração UE, marcação CE, organismos notificados, autoridades); fora do âmbito de um manual de engenharia de segurança de software — o próprio Manual declara-o fora («não substitui»). |
| CRA-AnxVIII-PII-11 | Anexo VIII, parte II (módulo B), ponto 11 | Obrigação do plano da conformidade formal/mercado (declaração UE, marcação CE, organismos notificados, autoridades); fora do âmbito de um manual de engenharia de segurança de software — o próprio Manual declara-o fora («não substitui»). |
| CRA-AnxVIII-PIII-3 | Anexo VIII, parte III (módulo C), pontos 3.1 e 3.2 | Obrigação do plano da conformidade formal/mercado (declaração UE, marcação CE, organismos notificados, autoridades); fora do âmbito de um manual de engenharia de segurança de software — o próprio Manual declara-o fora («não substitui»). |
| CRA-AnxVIII-PIII-4 | Anexo VIII, parte III (módulo C), ponto 4 | Obrigação do plano da conformidade formal/mercado (declaração UE, marcação CE, organismos notificados, autoridades); fora do âmbito de um manual de engenharia de segurança de software — o próprio Manual declara-o fora («não substitui»). |
| CRA-AnxVIII-PIV-3.1 | Anexo VIII, parte IV (módulo H), ponto 3.1 | Obrigação do plano da conformidade formal/mercado (declaração UE, marcação CE, organismos notificados, autoridades); fora do âmbito de um manual de engenharia de segurança de software — o próprio Manual declara-o fora («não substitui»). |
| CRA-AnxVIII-PIV-4.2 | Anexo VIII, parte IV (módulo H), ponto 4.2 | Obrigação do plano da conformidade formal/mercado (declaração UE, marcação CE, organismos notificados, autoridades); fora do âmbito de um manual de engenharia de segurança de software — o próprio Manual declara-o fora («não substitui»). |
| CRA-AnxVIII-PIV-5 | Anexo VIII, parte IV (módulo H), pontos 5.1 e 5.2 | Obrigação do plano da conformidade formal/mercado (declaração UE, marcação CE, organismos notificados, autoridades); fora do âmbito de um manual de engenharia de segurança de software — o próprio Manual declara-o fora («não substitui»). |
| CRA-AnxVIII-PIV-6 | Anexo VIII, parte IV (módulo H), ponto 6 | Obrigação do plano da conformidade formal/mercado (declaração UE, marcação CE, organismos notificados, autoridades); fora do âmbito de um manual de engenharia de segurança de software — o próprio Manual declara-o fora («não substitui»). |
| CRA-AnxVIII-PIV-8 | Anexo VIII, parte IV (módulo H), ponto 8 | Obrigação do plano da conformidade formal/mercado (declaração UE, marcação CE, organismos notificados, autoridades); fora do âmbito de um manual de engenharia de segurança de software — o próprio Manual declara-o fora («não substitui»). |
| CRA-AnxII-6 | Anexo II, ponto 6 | Obrigação do plano da conformidade formal/mercado (declaração UE, marcação CE, organismos notificados, autoridades); fora do âmbito de um manual de engenharia de segurança de software — o próprio Manual declara-o fora («não substitui»). |
| CRA-53 | Art. 53.º | Relação com autoridades de fiscalização/regime sancionatório; plano jurídico, não de engenharia. |
| CRA-54-1-4 | Art. 54.º, n.º 1 (1.º parágrafo, 2.º período) e n.º 4 | Relação com autoridades de fiscalização/regime sancionatório; plano jurídico, não de engenharia. |
| CRA-56-3 | Art. 56.º, n.º 3 (último período) | Relação com autoridades de fiscalização/regime sancionatório; plano jurídico, não de engenharia. |
| CRA-57-2-7 | Art. 57.º, n.os 2 e 7 (último período) | Relação com autoridades de fiscalização/regime sancionatório; plano jurídico, não de engenharia. |
| CRA-64-2 | Art. 64.º, n.º 2 | Relação com autoridades de fiscalização/regime sancionatório; plano jurídico, não de engenharia. |
| CRA-64-3 | Art. 64.º, n.º 3 | Relação com autoridades de fiscalização/regime sancionatório; plano jurídico, não de engenharia. |
| CRA-64-4 | Art. 64.º, n.º 4 | Relação com autoridades de fiscalização/regime sancionatório; plano jurídico, não de engenharia. |
| CRA-64-10 | Art. 64.º, n.º 10 | Relação com autoridades de fiscalização/regime sancionatório; plano jurídico, não de engenharia. |
| CRA-65 | Art. 65.º | Relação com autoridades de fiscalização/regime sancionatório; plano jurídico, não de engenharia. |
| CRA-69-1 | Art. 69.º, n.º 1 | Relação com autoridades de fiscalização/regime sancionatório; plano jurídico, não de engenharia. |
| CRA-69-2 | Art. 69.º, n.º 2 | Regime transitório (aplicação a produtos anteriores só com modificação substancial); plano jurídico. |
| CRA-71-2 | Art. 71.º, n.º 2 | Datas de aplicação; o Manual regista-as corretamente (art. 14.º desde 11.9.2026) na Política 32 §6. |
| CRA-AnxII-1 | Anexo II, ponto 1 | Identificação e contactos do fabricante: rotulagem. |
| CRA-AnxIII-I | Anexo III, classe I | Listas/descrições técnicas das categorias regulamentares de produto (determinam a rota de conformidade). |
| CRA-AnxIII-II | Anexo III, classe II | Listas/descrições técnicas das categorias regulamentares de produto (determinam a rota de conformidade). |
| CRA-AnxIV | Anexo IV | Listas/descrições técnicas das categorias regulamentares de produto (determinam a rota de conformidade). |
| CRA-R2025-2392-2 | Reg. de Execução (UE) 2025/2392, arts. 1.º e 2.º | Listas/descrições técnicas das categorias regulamentares de produto (determinam a rota de conformidade). |
| CRA-R2025-2392-AnxI-CI | Reg. de Execução (UE) 2025/2392, anexo I, classe I | Listas/descrições técnicas das categorias regulamentares de produto (determinam a rota de conformidade). |
| CRA-R2025-2392-AnxI-CII | Reg. de Execução (UE) 2025/2392, anexo I, classe II | Listas/descrições técnicas das categorias regulamentares de produto (determinam a rota de conformidade). |
| CRA-R2025-2392-AnxII | Reg. de Execução (UE) 2025/2392, anexo II | Listas/descrições técnicas das categorias regulamentares de produto (determinam a rota de conformidade). |
| CRA-R2025-1535-1 | Reg. Delegado (UE) 2025/1535, art. 1.º | Disposição delimitadora de âmbito/qualificação jurídica do produto; não cria dever de engenharia. |
| CRA-AnxVII-5 | Anexo VII, ponto 5 | Lista de normas harmonizadas/especificações comuns aplicadas: plano da conformidade. |
