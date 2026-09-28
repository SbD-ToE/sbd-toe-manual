---
id: requisitos-aplicaveis
title: "Requisitos aplicáveis — Entidade financeira (DORA)"
description: "Requisitos do Manual que se aplicam sob o contexto CTX-DORA, por nível e grau, com os pisos que o regime eleva e a base legal de cada um."
sidebar_position: 90
tags: [cross-check, dora, requisitos, overlay]
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
  - 002-cross-check-normativo/_matriz/dora.yaml
---

# Requisitos aplicáveis: Entidade financeira (DORA)

Esta página junta, para o contexto **CTX-DORA**, a selecção base do Manual por nível e os **pisos** que o regime eleva, cada um com a obrigação que o fundamenta. Um contexto nunca baixa um mínimo do Manual.

## Quando se aplica {#quando-se-aplica}

A organização é uma das entidades financeiras enumeradas no art. 2.º, n.º 1, do Reg. (UE) 2022/2554. Os pisos sem grau aplicam-se a todas as aplicações da entidade; os de grau FCI só às que suportam uma função crítica ou importante. Declara-se por entidade e é herdado por todas as aplicações.

> Reg. (UE) 2022/2554, art. 2.º, n.º 1: «o presente regulamento é aplicável às seguintes entidades»

## Graus {#graus}

- **FCI** — Suporta função crítica ou importante (cumulativo com o contexto). A aplicação suporta uma função crítica ou importante no inventário de funções da entidade financeira; declara-se por aplicação, com remissão para esse inventário.

## Pisos do contexto {#pisos}

| Piso | Alvo | Grau | Piso exigido | Âmbito | Base legal | Justificação de não aplicabilidade |
|---|---|---|---|---|---|---|
| CTX-DORA-P01 | [Política 32 §2](/sbd-toe/assets/policies/policy-irp#2-âmbito-e-obrigatoriedade) | — | obrigatório | Processo de gestão de incidentes de TIC definido, estabelecido e aplicado em qualquer nível, incluindo o registo de todos os incidentes e o post-mortem dos incidentes de caráter severo, com a revisão dos artefactos afectados (§4.6). | Reg. (UE) 2022/2554, art. 17.º, n.º 1: «As entidades financeiras definem, estabelecem e aplicam um processo de gestão de incidentes relacionados com as TIC» (DORA-17-1) | não admitida |
| CTX-DORA-P02 | `OPS-007` | — | obrigatório | — | Reg. (UE) 2022/2554, art. 17.º, n.º 1: «As entidades financeiras definem, estabelecem e aplicam um processo de gestão de incidentes relacionados com as TIC» (DORA-17-1) | não admitida |
| CTX-DORA-P03 | `TST-005` | — | obrigatório | Testes dinâmicos (a par dos estáticos, já obrigatórios por DEV-003), com testes de segurança dos sistemas e aplicações expostos à Internet. | Reg. Delegado (UE) 2024/1774, art. 16.º, n.º 3: «deve incluir o desempenho das análises do código-fonte que abranjam testes estáticos e dinâmicos» (DORA-RTS1774-16-3) | não admitida |
| CTX-DORA-P04 | `LOG-008` | — | obrigatório | — | Reg. Delegado (UE) 2024/1774, art. 12.º, n.º 2, al. e): «Medidas para detetar uma falha nos sistemas de registo» (DORA-RTS1774-12-2-e) | não admitida |
| CTX-DORA-P05 | `ACC-010` | — | obrigatório; frequência de actualização dos direitos de acesso ≥ anual («pelo menos, uma vez por ano para todos os sistemas de TIC que não sejam sistemas de TIC que apoiem funções críticas ou importantes») | — | Reg. Delegado (UE) 2024/1774, art. 21.º, al. e), subal. iv): «atualização dos direitos de acesso sempre que sejam necessárias alterações e, pelo menos, uma vez por ano para todos os sistemas de TIC» (DORA-RTS1774-21-e-iv) | não admitida |
| CTX-DORA-P06 | `ACC-010` | FCI | obrigatório; frequência de actualização dos direitos de acesso ≥ semestral («pelo menos a cada seis meses para os sistemas de TIC que apoiem funções críticas ou importantes») | — | Reg. Delegado (UE) 2024/1774, art. 21.º, al. e), subal. iv): «pelo menos a cada seis meses para os sistemas de TIC que apoiem funções críticas ou importantes» (DORA-RTS1774-21-e-iv) | não admitida |
| CTX-DORA-P07 | `AUT-001` | — | obrigatório | Autenticação forte dos utilizadores da aplicação no acesso a activos de TIC que apoiem funções críticas ou importantes e a activos de TIC acessíveis ao público (o acesso remoto e o privilegiado estão em CTX-DORA-P13). | Reg. Delegado (UE) 2024/1774, art. 21.º, al. f), subal. ii); art. 33.º, al. d) (regime simplificado): «a utilização de métodos de autenticação forte em conformidade com as melhores práticas e técnicas para o acesso remoto à rede da entidade financeira, para o acesso privilegiado e ainda para o acesso a ativos de TIC que apoiem funções críticas ou importantes ou ativos de TIC acessíveis ao público» (DORA-RTS1774-21-f-ii, DORA-RTS1774-33-d) | admitida |
| CTX-DORA-P08 | [Política 10 §9](/sbd-toe/assets/policies/policy-dependencias#9-auditoria-periódica) | FCI | obrigatório; frequência da análise automatizada de vulnerabilidades ≥ semanal («pelo menos semanalmente») | Análise automatizada de vulnerabilidades dos activos de TIC que apoiam funções críticas ou importantes, não só das dependências e imagens. | Reg. Delegado (UE) 2024/1774, art. 10.º, n.º 2, al. b), e segundo parágrafo: «as entidades financeiras devem realizar, pelo menos semanalmente, uma análise automatizada da vulnerabilidade e avaliações dos ativos de TIC para os ativos de TIC que apoiam funções críticas ou importantes» (DORA-RTS1774-10-2-b) | não admitida |
| CTX-DORA-P09 | `OPS-005` | FCI | obrigatório | — | Reg. Delegado (UE) 2024/1774, art. 23.º, n.º 2, al. b): «implementar ferramentas geradoras de alertas para atividades e comportamentos anómalos, pelo menos para os ativos de TIC e de informação que apoiem funções críticas ou importantes» (DORA-RTS1774-23-2-b) | não admitida |
| CTX-DORA-P10 | `GOV-015` | — | obrigatório | Divulgação responsável aos clientes, às contrapartes e ao público. | Reg. Delegado (UE) 2024/1774, art. 10.º, n.º 2, al. e): «Estabelecer procedimentos para a divulgação responsável das vulnerabilidades aos clientes, às contrapartes e ao público» (DORA-RTS1774-10-2-e) | não admitida |
| CTX-DORA-P11 | `OPS-016` | — | obrigatório | Restauro em sistemas física e logicamente separados do sistema de origem, protegidos contra acesso não autorizado e corrupção; testes periódicos de salvaguarda e de restauração. | Reg. (UE) 2022/2554, art. 12.º, n.os 1 a 3; Reg. Delegado (UE) 2024/1774, art. 8.º, n.º 2, al. b), subal. i), e art. 39.º, n.º 2, al. g): «utilizam sistemas de TIC que estejam física e logicamente separados do sistema de TIC de origem» (DORA-12-1-a, DORA-12-2, DORA-12-3, DORA-RTS1774-8-2-b-i, DORA-RTS1774-39-2-g) | não admitida |
| CTX-DORA-P12 | `OPS-017` | FCI | obrigatório | Também em L1 para aplicações que suportam funções críticas ou importantes: níveis e prazos de recuperação e dependências de prestadores de serviços de TIC. | Reg. (UE) 2022/2554, art. 12.º, n.º 6; Reg. Delegado (UE) 2024/1774, art. 39.º, n.º 2, al. d): «Ao determinar o tempo de recuperação e os objetivos concretos de recuperação para cada função» (DORA-12-6, DORA-RTS1774-39-2-d) | não admitida |
| CTX-DORA-P13 | `GOV-016` | — | obrigatório | Autenticação forte no acesso remoto à rede da entidade e no acesso privilegiado; contas dedicadas às tarefas administrativas e gestão automatizada do acesso privilegiado (PAM) quando viável e adequado, em qualquer nível. | Reg. Delegado (UE) 2024/1774, art. 21.º, als. e) e f), subal. ii), e art. 33.º, als. c) e d): «devem utilizar, sempre que possível, contas específicas para a execução de tarefas administrativas» (DORA-RTS1774-21-e, DORA-RTS1774-21-e-ii, DORA-RTS1774-21-f-ii, DORA-RTS1774-33-c, DORA-RTS1774-33-d) | não admitida |
| CTX-DORA-P14 | `GOV-017` | — | obrigatório | Identificação e autenticação únicas de pessoas e sistemas; processo de gestão do ciclo de vida de identidades e contas, com soluções automatizadas sempre que possível e adequado; contas genéricas e partilhadas limitadas, em qualquer nível. | Reg. Delegado (UE) 2024/1774, art. 20.º, n.os 1 e 2, al. b), e art. 21.º, al. c): «Um processo de gestão do ciclo de vida das identidades e das contas» (DORA-RTS1774-20-1, DORA-RTS1774-20-2-b, DORA-RTS1774-21-c) | não admitida |
| CTX-DORA-P15 | `ENC-007` | — | obrigatório | Ciclo de vida completo das chaves criptográficas em qualquer nível. | Reg. Delegado (UE) 2024/1774, art. 7.º, n.º 1: «requisitos relativos à gestão das chaves criptográficas ao longo de todo o seu ciclo de vida» (DORA-RTS1774-7-1) | admitida |
| CTX-DORA-P16 | `ENC-007` | FCI | obrigatório | Registo de todos os certificados e dos dispositivos que os guardam, mantido actualizado, com renovação antes da expiração, em qualquer nível. | Reg. Delegado (UE) 2024/1774, art. 7.º, n.os 4 e 5: «devem criar e manter um registo de todos os certificados e dispositivos de armazenamento de certificados» (DORA-RTS1774-7-4) | não admitida |
| CTX-DORA-P17 | `ENC-003` | — | obrigatório | Inventário e revisão criptográfica em qualquer nível, com actualização da tecnologia criptográfica perante a evolução da criptoanálise ou, não sendo possível, medidas de atenuação. | Reg. Delegado (UE) 2024/1774, art. 6.º, n.º 4: «com base na evolução da criptoanálise» (DORA-RTS1774-6-4) | admitida |
| CTX-DORA-P18 | `ARC-006` | FCI | obrigatório | Revisão das regras de filtragem de rede pelo menos semestral, em qualquer nível, para os sistemas que apoiam funções críticas ou importantes. | Reg. Delegado (UE) 2024/1774, art. 13.º, al. h), e segundo parágrafo: «pelo menos, a cada seis meses» (DORA-RTS1774-13-h) | não admitida |

## Requisitos acrescentados pelo regime {#acrescentos}

Estes requisitos só fazem sentido sob o regime e por isso não vivem nos catálogos do Manual; definem-se aqui, com a base legal de cada um.

| Requisito | Nome | Critério de aceitação | Base legal |
|---|---|---|---|
| `CTX-DORA-R01` | Capacidades de TIC redundantes e teste de comutação | Capacidades de TIC redundantes, com recursos, capacidade e funções adequados às necessidades do negócio, para os sistemas de que a aplicação depende (as microempresas avaliam a necessidade pelo perfil de risco); planos de resposta e recuperação testados pelo menos uma vez por ano, incluindo, nas entidades que não sejam microempresas, cenários de ciberataque e de comutação entre a infraestrutura primária e a capacidade redundante. | Reg. (UE) 2022/2554, art. 12.º, n.º 4, e art. 11.º, n.º 6, al. a): «mantêm capacidades de TIC redundantes equipadas com recursos, capacidade e funções suficientes» (DORA-12-4, DORA-11-6-a) |
| `CTX-DORA-R02` | Classificação dos incidentes de TIC e agregação dos recorrentes | Os incidentes de TIC classificam-se e o seu impacto determina-se com os critérios do art. 18.º, n.º 1 (clientes, contrapartes e transacções afectados; reputação; duração e indisponibilidade; distribuição geográfica; perdas de dados; criticidade dos serviços; impacto económico) e com os limiares de materialidade do Reg. Delegado (UE) 2024/1772, a partir dos dados de impacto do registo (Política 32 §4.3). Mensalmente, avalia-se a existência de incidentes recorrentes: os que ocorreram pelo menos duas vezes em seis meses, com a mesma causa primária aparente, e cumprem em conjunto os critérios contam como um incidente de caráter severo (excepto microempresas e as entidades do art. 16.º, n.º 1). | Reg. (UE) 2022/2554, arts. 17.º, n.º 3, al. b), e 18.º, n.º 1; Reg. Delegado (UE) 2024/1772, art. 8.º, n.º 2: «avaliar mensalmente a existência de incidentes recorrentes» (DORA-17-3-b, DORA-18-1, DORA-RTS1772-8-2, DORA-RTS1772-8-2-p2) |
| `CTX-DORA-R03` | Registo de ciberameaças significativas | Além dos incidentes, as ciberameaças significativas que afectam a aplicação ou os seus sistemas ficam registadas (descrição, fonte, sistemas visados, avaliação e medidas), com a possibilidade de notificação voluntária à autoridade competente (art. 19.º, n.º 2). | Reg. (UE) 2022/2554, art. 17.º, n.º 2: «As entidades financeiras registam todos os incidentes relacionados com as TIC, bem como as ciberameaças significativas» (DORA-17-2) |

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
| `AUT-001` | MFA obrigatório | ▲ | ▲ | ▲ | CTX-DORA-P07 |
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
| `ACC-010` | Revisão periódica de permissões | ▲ | ▲ | ▲ | CTX-DORA-P05 |
| `LOG-001` | Registo de eventos críticos | ✔ | ✔ | ✔ | — |
| `LOG-002` | Atributos mínimos em logs | ✔ | ✔ | ✔ | — |
| `LOG-003` | Protecção de integridade e acesso aos logs | ✔ | ✔ | ✔ | — |
| `LOG-004` | Análise periódica de logs | — | ✔ | ✔ | — |
| `LOG-005` | Retenção mínima dos logs | ✔ | ✔ | ✔ | — |
| `LOG-006` | Envio para sistema centralizado | — | ✔ | ✔ | — |
| `LOG-007` | Classificação e detecção de anomalias | — | ✔ | ✔ | — |
| `LOG-008` | Alarme em falhas do mecanismo de logging | ▲ | ▲ | ▲ | CTX-DORA-P04 |
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
| `ENC-003` | Algoritmos e configurações criptográficas robustas | ▲ | ▲ | ▲ | CTX-DORA-P17 |
| `ENC-004` | Hashing adaptativo de passwords | ✔ | ✔ | ✔ | — |
| `ENC-005` | Mascaramento de dados sensíveis em logs, outputs e respostas API | ✔ | ✔ | ✔ | — |
| `ENC-006` | Detecção e prevenção de segredos expostos em repositórios | ✔ | ✔ | ✔ | — |
| `ENC-007` | Ciclo de vida de chaves, segredos e certificados | ▲ | ▲ | ▲ | CTX-DORA-P15 |
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
| `TST-005` | DAST integrado em ambiente de staging antes de promoção | ▲ | ▲ | ▲ | CTX-DORA-P03 |
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
| `OPS-007` | Integração com processo formal de resposta a incidentes | ▲ | ▲ | ▲ | CTX-DORA-P02 |
| `OPS-008` | Correlação de eventos entre múltiplas fontes | — | — | ✔ | — |
| `OPS-009` | Deteção comportamental e baseline de actividade normal | — | — | ✔ | — |
| `OPS-010` | Métricas de eficácia da monitorização medidas e revistas | — | — | ✔ | — |
| `OPS-011` | Observabilidade dedicada a componentes AI/ML em produção | — | ✔ | ✔ | — |
| `OPS-012` | Audit completo por tool invocation de agente AI | — | ✔ | ✔ | — |
| `OPS-013` | Budget e detecção de runaway em consumo de modelo (token spend) | — | ✔ | ✔ | — |
| `OPS-014` | Detecção de jailbreak / off-policy actions em produção | — | — | ✔ | — |
| `OPS-015` | Sinais contínuos de saúde e disponibilidade operacional | — | ✔ | ✔ | — |
| `OPS-016` | Cópias de segurança com restauro testado | ▲ | ▲ | ▲ | CTX-DORA-P11 |
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
| `GOV-015` | Divulgação coordenada de vulnerabilidades com canal de receção publicado | ▲ | ▲ | ▲ | CTX-DORA-P10 |
| `GOV-016` | Contas privilegiadas e de administração dos sistemas de suporte | ▲ | ▲ | ▲ | CTX-DORA-P13 |
| `GOV-017` | Ciclo de vida das identidades com acesso aos sistemas | ▲ | ▲ | ▲ | CTX-DORA-P14 |
| `CTX-DORA-R01` | Capacidades de TIC redundantes e teste de comutação | ▲ | ▲ | ▲ | — |
| `CTX-DORA-R02` | Classificação dos incidentes de TIC e agregação dos recorrentes | ▲ | ▲ | ▲ | — |
| `CTX-DORA-R03` | Registo de ciberameaças significativas | ▲ | ▲ | ▲ | — |

## Lista de requisitos — FCI {#lista-fci}

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
| `AUT-001` | MFA obrigatório | ▲ | ▲ | ▲ | CTX-DORA-P07 |
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
| `ACC-010` | Revisão periódica de permissões | ▲ | ▲ | ▲ | CTX-DORA-P05, CTX-DORA-P06 |
| `LOG-001` | Registo de eventos críticos | ✔ | ✔ | ✔ | — |
| `LOG-002` | Atributos mínimos em logs | ✔ | ✔ | ✔ | — |
| `LOG-003` | Protecção de integridade e acesso aos logs | ✔ | ✔ | ✔ | — |
| `LOG-004` | Análise periódica de logs | — | ✔ | ✔ | — |
| `LOG-005` | Retenção mínima dos logs | ✔ | ✔ | ✔ | — |
| `LOG-006` | Envio para sistema centralizado | — | ✔ | ✔ | — |
| `LOG-007` | Classificação e detecção de anomalias | — | ✔ | ✔ | — |
| `LOG-008` | Alarme em falhas do mecanismo de logging | ▲ | ▲ | ▲ | CTX-DORA-P04 |
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
| `ENC-003` | Algoritmos e configurações criptográficas robustas | ▲ | ▲ | ▲ | CTX-DORA-P17 |
| `ENC-004` | Hashing adaptativo de passwords | ✔ | ✔ | ✔ | — |
| `ENC-005` | Mascaramento de dados sensíveis em logs, outputs e respostas API | ✔ | ✔ | ✔ | — |
| `ENC-006` | Detecção e prevenção de segredos expostos em repositórios | ✔ | ✔ | ✔ | — |
| `ENC-007` | Ciclo de vida de chaves, segredos e certificados | ▲ | ▲ | ▲ | CTX-DORA-P15, CTX-DORA-P16 |
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
| `ARC-006` | Controlos técnicos de isolamento entre domínios sensíveis | ▲ | ▲ | ▲ | CTX-DORA-P18 |
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
| `TST-005` | DAST integrado em ambiente de staging antes de promoção | ▲ | ▲ | ▲ | CTX-DORA-P03 |
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
| `OPS-005` | Alertas automáticos para eventos de segurança críticos | ▲ | ▲ | ▲ | CTX-DORA-P09 |
| `OPS-006` | SLA de resposta a alertas definido e medido | — | ✔ | ✔ | — |
| `OPS-007` | Integração com processo formal de resposta a incidentes | ▲ | ▲ | ▲ | CTX-DORA-P02 |
| `OPS-008` | Correlação de eventos entre múltiplas fontes | — | — | ✔ | — |
| `OPS-009` | Deteção comportamental e baseline de actividade normal | — | — | ✔ | — |
| `OPS-010` | Métricas de eficácia da monitorização medidas e revistas | — | — | ✔ | — |
| `OPS-011` | Observabilidade dedicada a componentes AI/ML em produção | — | ✔ | ✔ | — |
| `OPS-012` | Audit completo por tool invocation de agente AI | — | ✔ | ✔ | — |
| `OPS-013` | Budget e detecção de runaway em consumo de modelo (token spend) | — | ✔ | ✔ | — |
| `OPS-014` | Detecção de jailbreak / off-policy actions em produção | — | — | ✔ | — |
| `OPS-015` | Sinais contínuos de saúde e disponibilidade operacional | — | ✔ | ✔ | — |
| `OPS-016` | Cópias de segurança com restauro testado | ▲ | ▲ | ▲ | CTX-DORA-P11 |
| `OPS-017` | Objectivos e procedimento de recuperação da aplicação | ▲ | ▲ | ▲ | CTX-DORA-P12 |
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
| `GOV-015` | Divulgação coordenada de vulnerabilidades com canal de receção publicado | ▲ | ▲ | ▲ | CTX-DORA-P10 |
| `GOV-016` | Contas privilegiadas e de administração dos sistemas de suporte | ▲ | ▲ | ▲ | CTX-DORA-P13 |
| `GOV-017` | Ciclo de vida das identidades com acesso aos sistemas | ▲ | ▲ | ▲ | CTX-DORA-P14 |
| `CTX-DORA-R01` | Capacidades de TIC redundantes e teste de comutação | ▲ | ▲ | ▲ | — |
| `CTX-DORA-R02` | Classificação dos incidentes de TIC e agregação dos recorrentes | ▲ | ▲ | ▲ | — |
| `CTX-DORA-R03` | Registo de ciberameaças significativas | ▲ | ▲ | ▲ | — |

## Obrigações do regime por força de cobertura {#forca}

Contagem das obrigações do regime na matriz de cobertura (excluídas as dirigidas às autoridades). A secção [«O que este Manual cobre e o que fica de fora»](#cobertura) lista-as.

| Força | Obrigações |
|---|--:|
| Cobre | 166 |
| Parcial | 104 |
| Apoia evidência | 123 |
| Lacuna | 3 |
| Fora de âmbito | 230 |

## O que este Manual cobre e o que fica de fora {#cobertura}

Todas as obrigações do regime, na matriz de cobertura do Manual, em três categorias: o que o Manual **cobre**, e de que forma; as **lacunas declaradas** (o que não cobre por omissão); e o que fica **fora de âmbito**, com a razão. Nenhuma obrigação fica em silêncio. As 13 obrigações dirigidas às autoridades não criam dever para a organização e não entram nas listas.

### Cobre (289) {#cobre}

Força «cobre» ou «apoia evidência». A forma é a resposta do Manual: requisito do catálogo, política, secção, piso ou requisito acrescentado pelo regime.

| Obrigação | Referência | Força | Forma |
|---|---|---|---|
| DORA-4-1 | art. 4.º, n.º 1 | Apoia evidência | [Política 02 §3](/sbd-toe/assets/policies/policy-classificacao-risco#3-modelo-de-classificação---eixos-edi); `CLA-003` |
| DORA-4-2 | art. 4.º, n.º 2 | Apoia evidência | [Política 02 §3](/sbd-toe/assets/policies/policy-classificacao-risco#3-modelo-de-classificação---eixos-edi); `CLA-003` |
| DORA-5-1 | art. 5.º, n.º 1 | Apoia evidência | `GOV-001`; [Governação e Gestão de Risco TIC (Artigos 5–6 DORA)](/sbd-toe/cross-check-normativo/dora/intro#governação-e-gestão-de-risco-tic-artigos-56-dora) |
| DORA-5-2 | art. 5.º, n.º 2, 1.º parágrafo | Apoia evidência | `GOV-001`; [Governação e Gestão de Risco TIC (Artigos 5–6 DORA)](/sbd-toe/cross-check-normativo/dora/intro#governação-e-gestão-de-risco-tic-artigos-56-dora) |
| DORA-5-2-a | art. 5.º, n.º 2, al. a) | Apoia evidência | `GOV-001` |
| DORA-5-2-b | art. 5.º, n.º 2, al. b) | Apoia evidência | `GOV-001`; [Política 06 §10](/sbd-toe/assets/policies/policy-rastreabilidade#10-prazos-de-retenção-mínimos) |
| DORA-5-2-c | art. 5.º, n.º 2, al. c) | Apoia evidência | `GOV-002`; `GOV-003` |
| DORA-5-2-d | art. 5.º, n.º 2, al. d) | Apoia evidência | [Política 03 §5](/sbd-toe/assets/policies/policy-aceitacao-risco#5-limiares-de-aceitação-por-nível) |
| DORA-5-2-e | art. 5.º, n.º 2, al. e) | Apoia evidência | [Política 32 §3](/sbd-toe/assets/policies/policy-irp#3-critérios-de-activação-do-irp) |
| DORA-5-2-h | art. 5.º, n.º 2, al. h) | Apoia evidência | [Política 33 §3.2](/sbd-toe/assets/policies/policy-contratacao-segura#32-resultado-da-due-diligence); `GOV-006` |
| DORA-5-2-i | art. 5.º, n.º 2, al. i) | Apoia evidência | [Política 35 §5](/sbd-toe/assets/policies/policy-kpis-governacao#5-cadência-de-recolha-e-reporte); [Política 32 §7](/sbd-toe/assets/policies/policy-irp#7-comunicação-durante-o-incidente) |
| DORA-6-1 | art. 6.º, n.º 1 | Apoia evidência | `GOV-001`; [Política 02 §3](/sbd-toe/assets/policies/policy-classificacao-risco#3-modelo-de-classificação---eixos-edi); [Política 03 §5](/sbd-toe/assets/policies/policy-aceitacao-risco#5-limiares-de-aceitação-por-nível); [Política 04 §3.1](/sbd-toe/assets/policies/policy-revisao-periodica-risco#31-cadências-mínimas-obrigatórias) |
| DORA-6-5 | art. 6.º, n.º 5 | Apoia evidência | `GOV-010` |
| DORA-6-6 | art. 6.º, n.º 6 | Apoia evidência | [Política 35 §5](/sbd-toe/assets/policies/policy-kpis-governacao#5-cadência-de-recolha-e-reporte) |
| DORA-6-7 | art. 6.º, n.º 7 | Apoia evidência | `GOV-010` |
| DORA-6-8 | art. 6.º, n.º 8, proémio | Apoia evidência | `GOV-001`; [Para que serve este documento](/sbd-toe/sbd-manual/governanca-contratacao/kpis-kri-executivo#para-que-serve-este-documento) |
| DORA-6-8-a | art. 6.º, n.º 8, al. a) | Apoia evidência | `GOV-001` |
| DORA-6-8-b | art. 6.º, n.º 8, al. b) | Apoia evidência | [Política 03 §5](/sbd-toe/assets/policies/policy-aceitacao-risco#5-limiares-de-aceitação-por-nível); [Política 03 §7](/sbd-toe/assets/policies/policy-aceitacao-risco#7-alçadas-de-aprovação) |
| DORA-6-8-f | art. 6.º, n.º 8, al. f) | Apoia evidência | [Política 35 §5](/sbd-toe/assets/policies/policy-kpis-governacao#5-cadência-de-recolha-e-reporte) |
| DORA-6-8-h | art. 6.º, n.º 8, al. h) | Apoia evidência | [Política 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória) |
| DORA-8-3 | art. 8.º, n.º 3 | Cobre | [Política 04 §4.1](/sbd-toe/assets/policies/policy-revisao-periodica-risco#41-triggers-que-obrigam-a-revisão-imediata); `CLA-006`; `ARC-009`; `THR-006` |
| DORA-9-1 | art. 9.º, n.º 1 | Cobre | [6️⃣ Registo e Monitorização Essencial (Cap. 12)](/sbd-toe/sbd-manual/fundamentos/baseline#6️⃣-registo-e-monitorização-essencial-cap-12); `OPS-001`; `OPS-005` |
| DORA-9-3-a | art. 9.º, n.º 3, al. a) | Cobre | `ENC-001`; `INT-003`; `INT-004` |
| DORA-9-3-b | art. 9.º, n.º 3, al. b) | Cobre | `ACC-006`; `ENC-009`; `INT-009`; `OPS-016` |
| DORA-9-3-c | art. 9.º, n.º 3, al. c) | Cobre | `ENC-009`; `ACC-006`; `OPS-015`; `OPS-016`; `OPS-017`; `CTX-DORA-R01` |
| DORA-9-4-a | art. 9.º, n.º 4, al. a) | Apoia evidência | `GOV-001` |
| DORA-9-4-d | art. 9.º, n.º 4, al. d) | Cobre | `ENC-007`; `AUT-001`; [🛡️ Requisitos de segurança por ambiente](/sbd-toe/sbd-manual/deploy-seguro/addon/08-segregacao-e-validacao-operacional#️-requisitos-de-segurança-por-ambiente); `CFG-006`; `ENC-007` |
| DORA-10-1-p2 | art. 10.º, n.º 1, 2.º parágrafo | Cobre | `OPS-007`; [Política 30 §7](/sbd-toe/assets/policies/policy-monitorizacao-seguranca#7-validação-e-tuning-de-regras-de-detecção) |
| DORA-10-2 | art. 10.º, n.º 2 | Cobre | `OPS-005`; `OPS-008`; [Política 32 §3](/sbd-toe/assets/policies/policy-irp#3-critérios-de-activação-do-irp) |
| DORA-11-6-p3 | art. 11.º, n.º 6, 3.º parágrafo | Apoia evidência | [Política 32 §8](/sbd-toe/assets/policies/policy-irp#8-testes-periódicos-do-irp) |
| DORA-11-8 | art. 11.º, n.º 8 | Cobre | [Política 32 §4.2](/sbd-toe/assets/policies/policy-irp#42-contenção-t1---início-imediato-após-confirmação); [Política 32 §4.3](/sbd-toe/assets/policies/policy-irp#43-investigação); `LOG-009` |
| DORA-12-1-a | art. 12.º, n.º 1, al. a) | Cobre | `OPS-016` |
| DORA-12-1-b | art. 12.º, n.º 1, al. b) | Cobre | [Política 27 §7](/sbd-toe/assets/policies/policy-rollback#7-teste-periódico-de-rollback); [Política 32 §4.5](/sbd-toe/assets/policies/policy-irp#45-recuperação); `OPS-017` |
| DORA-12-2 | art. 12.º, n.º 2 | Cobre | `OPS-016`; `OPS-016` |
| DORA-12-3 | art. 12.º, n.º 3 | Cobre | `OPS-016` |
| DORA-12-4 | art. 12.º, n.º 4 | Cobre | `CTX-DORA-R01` |
| DORA-12-6 | art. 12.º, n.º 6 | Cobre | [🔁 Mapeamento prático entre DRP/BIA e risco de segurança](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/adopcao-drp-bia#-mapeamento-prático-entre-drpbia-e-risco-de-segurança); [Política 27 §6](/sbd-toe/assets/policies/policy-rollback#6-rto-de-rollback-por-nível); `OPS-017` |
| DORA-13-1 | art. 13.º, n.º 1 | Cobre | [Política 10 §8](/sbd-toe/assets/policies/policy-dependencias#8-alertas-de-vulnerabilidades-em-produção); [Cap. 12 US-16](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle#us-16---cobertura-attck-e-priorização-epsskev); [Política 11 §7](/sbd-toe/assets/policies/policy-sbom#7-inventário-em-produção) |
| DORA-13-2 | art. 13.º, n.º 2, 1.º e 3.º parágrafos | Cobre | [Política 32 §4.6](/sbd-toe/assets/policies/policy-irp#46-post-mortem); [Política 32 §4.3](/sbd-toe/assets/policies/policy-irp#43-investigação) |
| DORA-13-3 | art. 13.º, n.º 3 | Cobre | [Política 04 §4.1](/sbd-toe/assets/policies/policy-revisao-periodica-risco#41-triggers-que-obrigam-a-revisão-imediata); `CLA-006`; `TRN-006` |
| DORA-13-4 | art. 13.º, n.º 4 | Apoia evidência | `GOV-011`; [Política 35 §5](/sbd-toe/assets/policies/policy-kpis-governacao#5-cadência-de-recolha-e-reporte) |
| DORA-13-5 | art. 13.º, n.º 5 | Apoia evidência | [Política 35 §5](/sbd-toe/assets/policies/policy-kpis-governacao#5-cadência-de-recolha-e-reporte); [Para que serve este documento](/sbd-toe/sbd-manual/governanca-contratacao/kpis-kri-executivo#para-que-serve-este-documento) |
| DORA-13-7 | art. 13.º, n.º 7 | Apoia evidência | [Política 10 §8](/sbd-toe/assets/policies/policy-dependencias#8-alertas-de-vulnerabilidades-em-produção); `TRN-006` |
| DORA-14-3 | art. 14.º, n.º 3 | Apoia evidência | [Política 32 §7](/sbd-toe/assets/policies/policy-irp#7-comunicação-durante-o-incidente) |
| DORA-16-1-a | art. 16.º, n.º 1, 2.º parágrafo, al. a) | Apoia evidência | `GOV-001`; [Política 02 §3](/sbd-toe/assets/policies/policy-classificacao-risco#3-modelo-de-classificação---eixos-edi); [Política 03 §5](/sbd-toe/assets/policies/policy-aceitacao-risco#5-limiares-de-aceitação-por-nível) |
| DORA-16-1-b | art. 16.º, n.º 1, 2.º parágrafo, al. b) | Cobre | [6️⃣ Registo e Monitorização Essencial (Cap. 12)](/sbd-toe/sbd-manual/fundamentos/baseline#6️⃣-registo-e-monitorização-essencial-cap-12); `OPS-001` |
| DORA-16-1-d | art. 16.º, n.º 1, 2.º parágrafo, al. d) | Cobre | `OPS-005`; [Política 32 §3](/sbd-toe/assets/policies/policy-irp#3-critérios-de-activação-do-irp) |
| DORA-16-1-f | art. 16.º, n.º 1, 2.º parágrafo, al. f) | Cobre | [Política 32 §4.5](/sbd-toe/assets/policies/policy-irp#45-recuperação); [Política 27 §7](/sbd-toe/assets/policies/policy-rollback#7-teste-periódico-de-rollback); `OPS-016`; `OPS-016` |
| DORA-16-2 | art. 16.º, n.º 2 | Apoia evidência | `GOV-010` |
| DORA-17-1 | art. 17.º, n.º 1 | Cobre | [Política 32 §2](/sbd-toe/assets/policies/policy-irp#2-âmbito-e-obrigatoriedade); [Política 32 §2](/sbd-toe/assets/policies/policy-irp#2-âmbito-e-obrigatoriedade); [Política 32 §3](/sbd-toe/assets/policies/policy-irp#3-critérios-de-activação-do-irp); [Política 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória); `OPS-007` |
| DORA-17-2 | art. 17.º, n.º 2 | Cobre | `CTX-DORA-R03`; [Política 32 §4.1](/sbd-toe/assets/policies/policy-irp#41-triagem-t0----15-minutos-de-detecção); [Política 32 §4.3](/sbd-toe/assets/policies/policy-irp#43-investigação) |
| DORA-17-3-a | art. 17.º, n.º 3, al. a) | Cobre | `OPS-005`; `LOG-007` |
| DORA-17-3-b | art. 17.º, n.º 3, al. b) | Cobre | `CTX-DORA-R02`; [Política 32 §4.3](/sbd-toe/assets/policies/policy-irp#43-investigação); [Política 31 §3](/sbd-toe/assets/policies/policy-gestao-alertas#3-classificação-de-alertas); [Política 32 §4.1](/sbd-toe/assets/policies/policy-irp#41-triagem-t0----15-minutos-de-detecção); [Incidentes, Classificação e Reporte (Artigos 17–23 DORA)](/sbd-toe/cross-check-normativo/dora/intro#incidentes-classificação-e-reporte-artigos-1723-dora) |
| DORA-17-3-c | art. 17.º, n.º 3, al. c) | Cobre | [Política 32 §5](/sbd-toe/assets/policies/policy-irp#5-playbooks-de-resposta); [Política 32 §4.1](/sbd-toe/assets/policies/policy-irp#41-triagem-t0----15-minutos-de-detecção) |
| DORA-17-3-d | art. 17.º, n.º 3, al. d) | Cobre | [Política 32 §7](/sbd-toe/assets/policies/policy-irp#7-comunicação-durante-o-incidente); [Política 31 §5](/sbd-toe/assets/policies/policy-gestao-alertas#5-escalonamento-automático); [Política 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória) |
| DORA-17-3-f | art. 17.º, n.º 3, al. f) | Cobre | [Política 32 §4.2](/sbd-toe/assets/policies/policy-irp#42-contenção-t1---início-imediato-após-confirmação); [Política 32 §4.5](/sbd-toe/assets/policies/policy-irp#45-recuperação) |
| DORA-18-1 | art. 18.º, n.º 1, als. a) a f) | Cobre | `CTX-DORA-R02`; [Política 32 §4.3](/sbd-toe/assets/policies/policy-irp#43-investigação); [Política 32 §4.1](/sbd-toe/assets/policies/policy-irp#41-triagem-t0----15-minutos-de-detecção); [Incidentes, Classificação e Reporte (Artigos 17–23 DORA)](/sbd-toe/cross-check-normativo/dora/intro#incidentes-classificação-e-reporte-artigos-1723-dora) |
| DORA-18-2 | art. 18.º, n.º 2 | Apoia evidência | [Cap. 12 US-16](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle#us-16---cobertura-attck-e-priorização-epsskev) |
| DORA-19-1 | art. 19.º, n.º 1, 1.º, 3.º, 4.º e 5.º parágrafos | Apoia evidência | [Política 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória); [Política 32 §4.1](/sbd-toe/assets/policies/policy-irp#41-triagem-t0----15-minutos-de-detecção) |
| DORA-19-3 | art. 19.º, n.º 3, 1.º parágrafo | Apoia evidência | [Política 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória) |
| DORA-19-4-a | art. 19.º, n.º 4, al. a) | Apoia evidência | [Política 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória) |
| DORA-19-4-b | art. 19.º, n.º 4, al. b) | Apoia evidência | [Política 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória) |
| DORA-19-4-c | art. 19.º, n.º 4, al. c) | Apoia evidência | [Política 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória); [Política 32 §4.6](/sbd-toe/assets/policies/policy-irp#46-post-mortem) |
| DORA-24-1 | art. 24.º, n.os 1 e 2 | Cobre | `TST-001`; [Política 19 §2.1](/sbd-toe/assets/policies/policy-estrategia-testes#21-matriz-de-obrigatoriedade-por-nível) |
| DORA-24-3 | art. 24.º, n.º 3 | Cobre | `TST-001`; `CLA-003` |
| DORA-24-5 | art. 24.º, n.º 5 | Cobre | `TST-003`; [Política 19 §4.3](/sbd-toe/assets/policies/policy-estrategia-testes#43-slas-de-triagem-e-resolução); `TST-006` |
| DORA-24-6 | art. 24.º, n.º 6 | Cobre | [Política 36 §2](/sbd-toe/assets/policies/policy-pentesting#2-âmbito-e-obrigatoriedade); [Política 36 §9](/sbd-toe/assets/policies/policy-pentesting#9-cadência-de-pentesting); `TST-008` |
| DORA-25-2 | art. 25.º, n.º 2 | Cobre | `DPL-003`; `TST-005` |
| DORA-25-3 | art. 25.º, n.º 3 | Cobre | `TST-001` |
| DORA-26-2 | art. 26.º, n.º 2 | Apoia evidência | [6) Checklist de readiness (binário)](/sbd-toe/sbd-manual/testes-seguranca/addon/tlpt-readiness#6-checklist-de-readiness-binário) |
| DORA-26-5 | art. 26.º, n.º 5 | Apoia evidência | [Política 36 §4.2](/sbd-toe/assets/policies/policy-pentesting#42-regras-de-engajamento) |
| DORA-28-1 | art. 28.º, n.º 1, al. a) e b) | Apoia evidência | `GOV-007`; [Política 33 §3.2](/sbd-toe/assets/policies/policy-contratacao-segura#32-resultado-da-due-diligence) |
| DORA-28-2 | art. 28.º, n.º 2 | Apoia evidência | [Política 33 §3.2](/sbd-toe/assets/policies/policy-contratacao-segura#32-resultado-da-due-diligence); `GOV-006` |
| DORA-28-3 | art. 28.º, n.º 3, 1.º parágrafo | Apoia evidência | `GOV-008`; [Gestão de Fornecedores Críticos (Artigos 28–30 DORA)](/sbd-toe/cross-check-normativo/dora/intro#gestão-de-fornecedores-críticos-artigos-2830-dora) |
| DORA-28-4-a | art. 28.º, n.º 4, al. a) | Apoia evidência | `GOV-007` |
| DORA-28-4-c | art. 28.º, n.º 4, al. c) | Apoia evidência | [Política 33 §3.1](/sbd-toe/assets/policies/policy-contratacao-segura#31-critérios-de-avaliação) |
| DORA-28-7 | art. 28.º, n.º 7, al. a) a d) | Apoia evidência | [Política 33 §4.1](/sbd-toe/assets/policies/policy-contratacao-segura#41-cláusulas-universais-todos-os-níveis) |
| DORA-28-8 | art. 28.º, n.º 8, 1.º parágrafo | Apoia evidência | [Política 33 §7.1](/sbd-toe/assets/policies/policy-contratacao-segura#71-checklist-de-offboarding) |
| DORA-30-1 | art. 30.º, n.º 1 | Apoia evidência | [Política 33 §4.3](/sbd-toe/assets/policies/policy-contratacao-segura#43-modelo-contratual-de-referência); [8️⃣ Cláusulas Mínimas de Segurança em Fornecedores (Cap. 14)](/sbd-toe/sbd-manual/fundamentos/baseline#8️⃣-cláusulas-mínimas-de-segurança-em-fornecedores-cap-14) |
| DORA-30-2-a | art. 30.º, n.º 2, al. a) | Apoia evidência | [Política 33 §4.1](/sbd-toe/assets/policies/policy-contratacao-segura#41-cláusulas-universais-todos-os-níveis) |
| DORA-30-2-b | art. 30.º, n.º 2, al. b) | Apoia evidência | [Política 33 §10.2](/sbd-toe/assets/policies/policy-contratacao-segura#102-localização-de-processamento) |
| DORA-30-2-c | art. 30.º, n.º 2, al. c) | Apoia evidência | [Política 33 §4.1](/sbd-toe/assets/policies/policy-contratacao-segura#41-cláusulas-universais-todos-os-níveis) |
| DORA-30-2-d | art. 30.º, n.º 2, al. d) | Apoia evidência | [Política 33 §7.1](/sbd-toe/assets/policies/policy-contratacao-segura#71-checklist-de-offboarding) |
| DORA-30-2-e | art. 30.º, n.º 2, al. e) | Apoia evidência | [🏷️ SaaS / Serviços geridos](/sbd-toe/sbd-manual/governanca-contratacao/addon/clausulas-contratuais#️-saas--serviços-geridos) |
| DORA-30-2-f | art. 30.º, n.º 2, al. f) | Apoia evidência | [Política 33 §4.1](/sbd-toe/assets/policies/policy-contratacao-segura#41-cláusulas-universais-todos-os-níveis) |
| DORA-30-2-h | art. 30.º, n.º 2, al. h) | Apoia evidência | [Política 33 §4.1](/sbd-toe/assets/policies/policy-contratacao-segura#41-cláusulas-universais-todos-os-níveis) |
| DORA-30-2-i | art. 30.º, n.º 2, al. i) | Apoia evidência | [Política 33 §4.2](/sbd-toe/assets/policies/policy-contratacao-segura#42-cláusulas-adicionais-por-nível-de-risco); `GOV-013` |
| DORA-30-3-b | art. 30.º, n.º 3, al. b) | Apoia evidência | [Política 33 §10.4](/sbd-toe/assets/policies/policy-contratacao-segura#104-sla-de-notificação-prévia) |
| DORA-30-3-c | art. 30.º, n.º 3, al. c) | Apoia evidência | [Política 33 §3.1](/sbd-toe/assets/policies/policy-contratacao-segura#31-critérios-de-avaliação) |
| DORA-30-3-e | art. 30.º, n.º 3, al. e) | Apoia evidência | [Política 33 §4.2](/sbd-toe/assets/policies/policy-contratacao-segura#42-cláusulas-adicionais-por-nível-de-risco); [🏷️ SaaS / Serviços geridos](/sbd-toe/sbd-manual/governanca-contratacao/addon/clausulas-contratuais#️-saas--serviços-geridos) |
| DORA-30-4 | art. 30.º, n.º 4 | Apoia evidência | [Política 33 §4.3](/sbd-toe/assets/policies/policy-contratacao-segura#43-modelo-contratual-de-referência) |
| DORA-RTS1773-1 | art. 1.º, al. a) a j) | Apoia evidência | [Política 33 §3.2](/sbd-toe/assets/policies/policy-contratacao-segura#32-resultado-da-due-diligence) |
| DORA-RTS1773-3-3 | art. 3.º, n.º 3 | Apoia evidência | `GOV-002` |
| DORA-RTS1773-3-6 | art. 3.º, n.º 6, al. a) a d) | Apoia evidência | [🏷️ SaaS / Serviços geridos](/sbd-toe/sbd-manual/governanca-contratacao/addon/clausulas-contratuais#️-saas--serviços-geridos); `GOV-006` |
| DORA-RTS1773-4 | art. 4.º, al. a) a f) | Apoia evidência | [Política 33 §3.2](/sbd-toe/assets/policies/policy-contratacao-segura#32-resultado-da-due-diligence); [Política 33 §6.2](/sbd-toe/assets/policies/policy-contratacao-segura#62-reavaliação-periódica); [Política 33 §7.1](/sbd-toe/assets/policies/policy-contratacao-segura#71-checklist-de-offboarding) |
| DORA-RTS1773-5-2 | art. 5.º, n.º 2, al. a) a i) | Apoia evidência | [Política 33 §3.1](/sbd-toe/assets/policies/policy-contratacao-segura#31-critérios-de-avaliação) |
| DORA-RTS1773-6-1 | art. 6.º, n.º 1, al. a) a f) | Apoia evidência | [Política 33 §3.2](/sbd-toe/assets/policies/policy-contratacao-segura#32-resultado-da-due-diligence) |
| DORA-RTS1773-6-3 | art. 6.º, n.º 3, al. a) a e) | Apoia evidência | [Política 33 §3.1](/sbd-toe/assets/policies/policy-contratacao-segura#31-critérios-de-avaliação) |
| DORA-RTS1773-6-4 | art. 6.º, n.º 4 | Apoia evidência | [Política 33 §6.1](/sbd-toe/assets/policies/policy-contratacao-segura#61-indicadores-de-conformidade-a-monitorizar) |
| DORA-RTS1773-8-1 | art. 8.º, n.º 1 | Apoia evidência | [Política 33 §4.3](/sbd-toe/assets/policies/policy-contratacao-segura#43-modelo-contratual-de-referência) |
| DORA-RTS1773-8-2 | art. 8.º, n.º 2, al. a) a d) | Apoia evidência | [Política 33 §4.2](/sbd-toe/assets/policies/policy-contratacao-segura#42-cláusulas-adicionais-por-nível-de-risco); [🏷️ SaaS / Serviços geridos](/sbd-toe/sbd-manual/governanca-contratacao/addon/clausulas-contratuais#️-saas--serviços-geridos) |
| DORA-RTS1773-8-3 | art. 8.º, n.º 3, al. a) a h) | Apoia evidência | [Política 33 §3.1](/sbd-toe/assets/policies/policy-contratacao-segura#31-critérios-de-avaliação) |
| DORA-RTS1773-9-1 | art. 9.º, n.º 1 | Apoia evidência | [Política 33 §6.1](/sbd-toe/assets/policies/policy-contratacao-segura#61-indicadores-de-conformidade-a-monitorizar) |
| DORA-RTS1773-9-2 | art. 9.º, n.º 2, al. a) a e) | Cobre | [Política 33 §6.1](/sbd-toe/assets/policies/policy-contratacao-segura#61-indicadores-de-conformidade-a-monitorizar); [Política 33 §6.2](/sbd-toe/assets/policies/policy-contratacao-segura#62-reavaliação-periódica) |
| DORA-RTS1773-9-3 | art. 9.º, n.º 3 | Cobre | [Política 33 §6.2](/sbd-toe/assets/policies/policy-contratacao-segura#62-reavaliação-periódica) |
| DORA-RTS1773-9-4 | art. 9.º, n.º 4 | Cobre | [Política 33 §6.2](/sbd-toe/assets/policies/policy-contratacao-segura#62-reavaliação-periódica) |
| DORA-RTS532-3-1 | art. 3.º, n.º 1, 1.º parágrafo e al. a) a e) | Apoia evidência | [Política 33 §4.1](/sbd-toe/assets/policies/policy-contratacao-segura#41-cláusulas-universais-todos-os-níveis) |
| DORA-RTS532-3-2 | art. 3.º, n.º 2 | Apoia evidência | [Política 33 §6.2](/sbd-toe/assets/policies/policy-contratacao-segura#62-reavaliação-periódica) |
| DORA-RTS532-4-1-i | art. 4.º, n.º 1, al. i) | Apoia evidência | [Política 33 §4.1](/sbd-toe/assets/policies/policy-contratacao-segura#41-cláusulas-universais-todos-os-níveis); `GOV-006` |
| DORA-RTS1774-1 | art. 1.º | Apoia evidência | [Política 02 §3](/sbd-toe/assets/policies/policy-classificacao-risco#3-modelo-de-classificação---eixos-edi); `CLA-003` |
| DORA-RTS1774-2-1 | art. 2.º, n.º 1 | Apoia evidência | `GOV-001` |
| DORA-RTS1774-2-1-c | art. 2.º, n.º 1, al. c) | Cobre | `ENC-001`; `ENC-002`; `ENC-003`; `ENC-009` |
| DORA-RTS1774-2-2-a | art. 2.º, n.º 2, al. a) | Apoia evidência | `GOV-001` |
| DORA-RTS1774-2-2-b | art. 2.º, n.º 2, al. b) | Apoia evidência | `GOV-001` |
| DORA-RTS1774-2-2-c | art. 2.º, n.º 2, al. c) | Cobre | `GOV-004`; `GOV-011`; [Política 05 §3](/sbd-toe/assets/policies/policy-gestao-excecoes#3-princípios-fundamentais) |
| DORA-RTS1774-2-2-d | art. 2.º, n.º 2, al. d) | Apoia evidência | `GOV-002` |
| DORA-RTS1774-2-2-f | art. 2.º, n.º 2, al. f) | Apoia evidência | [Política 06 §10](/sbd-toe/assets/policies/policy-rastreabilidade#10-prazos-de-retenção-mínimos) |
| DORA-RTS1774-2-2-h | art. 2.º, n.º 2, al. h) | Cobre | [Mapeamento de catálogos por domínio técnico](/sbd-toe/sbd-manual/requisitos-seguranca/addon/lista-requisitos-base#mapeamento-de-catalogos) |
| DORA-RTS1774-2-2-i | art. 2.º, n.º 2, al. i) | Apoia evidência | `GOV-001` |
| DORA-RTS1774-2-2-j | art. 2.º, n.º 2, al. j) | Apoia evidência | `GOV-010` |
| DORA-RTS1774-2-2-k | art. 2.º, n.º 2, al. k) | Apoia evidência | `GOV-010` |
| DORA-RTS1774-3 | art. 3.º, prim. parágrafo | Apoia evidência | [Política 02 §3](/sbd-toe/assets/policies/policy-classificacao-risco#3-modelo-de-classificação---eixos-edi); [Política 03 §5](/sbd-toe/assets/policies/policy-aceitacao-risco#5-limiares-de-aceitação-por-nível) |
| DORA-RTS1774-3-a | art. 3.º, al. a) | Apoia evidência | [Política 03 §5](/sbd-toe/assets/policies/policy-aceitacao-risco#5-limiares-de-aceitação-por-nível); [Política 03 §7](/sbd-toe/assets/policies/policy-aceitacao-risco#7-alçadas-de-aprovação) |
| DORA-RTS1774-3-b | art. 3.º, al. b) | Cobre | [Política 02 §3](/sbd-toe/assets/policies/policy-classificacao-risco#3-modelo-de-classificação---eixos-edi); `THR-003`; [Cap. 12 US-16](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle#us-16---cobertura-attck-e-priorização-epsskev) |
| DORA-RTS1774-3-c | art. 3.º, al. c) | Cobre | `THR-004`; [Política 03 §5](/sbd-toe/assets/policies/policy-aceitacao-risco#5-limiares-de-aceitação-por-nível) |
| DORA-RTS1774-3-d | art. 3.º, al. d) | Cobre | `CLA-007`; [Política 03 §8](/sbd-toe/assets/policies/policy-aceitacao-risco#8-reavaliação-e-expiração); `GOV-004` |
| DORA-RTS1774-3-d-iv | art. 3.º, al. d), subal. iv) | Cobre | [Política 05 §7](/sbd-toe/assets/policies/policy-gestao-excecoes#7-prazos-máximos-de-validade-ttl); [Política 03 §8](/sbd-toe/assets/policies/policy-aceitacao-risco#8-reavaliação-e-expiração) |
| DORA-RTS1774-3-e | art. 3.º, al. e) | Cobre | [Política 10 §8](/sbd-toe/assets/policies/policy-dependencias#8-alertas-de-vulnerabilidades-em-produção); [Cap. 12 US-16](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle#us-16---cobertura-attck-e-priorização-epsskev); [Política 11 §7](/sbd-toe/assets/policies/policy-sbom#7-inventário-em-produção) |
| DORA-RTS1774-3-f | art. 3.º, al. f) | Apoia evidência | [Política 04 §4.1](/sbd-toe/assets/policies/policy-revisao-periodica-risco#41-triggers-que-obrigam-a-revisão-imediata) |
| DORA-RTS1774-5-2 | art. 5.º, n.º 2 | Cobre | [Política 02 §3](/sbd-toe/assets/policies/policy-classificacao-risco#3-modelo-de-classificação---eixos-edi); `CLA-001` |
| DORA-RTS1774-6-1 | art. 6.º, n.º 1 | Cobre | `ENC-001`; `ENC-002`; `ENC-003`; `ENC-007` |
| DORA-RTS1774-6-2 | art. 6.º, n.º 2, prim. parágrafo | Cobre | `ENC-002`; `CLA-003` |
| DORA-RTS1774-6-2-a | art. 6.º, n.º 2, al. a) | Cobre | `ENC-001`; `ENC-002` |
| DORA-RTS1774-6-2-c | art. 6.º, n.º 2, al. c) | Cobre | `ENC-001`; `INT-003` |
| DORA-RTS1774-6-2-d | art. 6.º, n.º 2, al. d) | Cobre | `ENC-007`; [Política 18 §6.4](/sbd-toe/assets/policies/policy-gestao-segredos#64-ciclo-de-vida-das-chaves-e-inventário-de-certificados); `ENC-007`; `CFG-006`; `ENC-002` |
| DORA-RTS1774-6-3 | art. 6.º, n.º 3 | Cobre | `ENC-003`; `GOV-004` |
| DORA-RTS1774-6-4 | art. 6.º, n.º 4 | Cobre | `ENC-003` |
| DORA-RTS1774-6-5 | art. 6.º, n.º 5 | Cobre | `GOV-004`; [Política 05 §3](/sbd-toe/assets/policies/policy-gestao-excecoes#3-princípios-fundamentais) |
| DORA-RTS1774-7-1 | art. 7.º, n.º 1 | Cobre | `ENC-007`; [Política 18 §6.4](/sbd-toe/assets/policies/policy-gestao-segredos#64-ciclo-de-vida-das-chaves-e-inventário-de-certificados); `ENC-007`; [Política 18 §6](/sbd-toe/assets/policies/policy-gestao-segredos#6-ttl-rotação-e-revogação); [Política 18 §6.3](/sbd-toe/assets/policies/policy-gestao-segredos#63-revogação-por-exposição-suspeita) |
| DORA-RTS1774-7-2 | art. 7.º, n.º 2 | Cobre | `CFG-006`; `ENC-002` |
| DORA-RTS1774-7-3 | art. 7.º, n.º 3 | Cobre | [Política 18 §6.3](/sbd-toe/assets/policies/policy-gestao-segredos#63-revogação-por-exposição-suspeita); `ENC-007` |
| DORA-RTS1774-7-4 | art. 7.º, n.º 4 | Cobre | `ENC-007`; [Política 18 §6.4](/sbd-toe/assets/policies/policy-gestao-segredos#64-ciclo-de-vida-das-chaves-e-inventário-de-certificados) |
| DORA-RTS1774-7-5 | art. 7.º, n.º 5 | Cobre | [Política 18 §6.4](/sbd-toe/assets/policies/policy-gestao-segredos#64-ciclo-de-vida-das-chaves-e-inventário-de-certificados); `API-005` |
| DORA-RTS1774-8-2-b-i | art. 8.º, n.º 2, al. b), subal. i) | Cobre | `OPS-016`; `OPS-016` |
| DORA-RTS1774-8-2-b-iii | art. 8.º, n.º 2, al. b), subal. iii) | Cobre | `LOG-001`; `LOG-002`; [Política 29 §4](/sbd-toe/assets/policies/policy-logging-estruturado#4-eventos-de-segurança-obrigatórios) |
| DORA-RTS1774-8-2-b-iv | art. 8.º, n.º 2, al. b), subal. iv) | Cobre | [Política 36 §4.2](/sbd-toe/assets/policies/policy-pentesting#42-regras-de-engajamento); `TST-005` |
| DORA-RTS1774-8-2-b-v | art. 8.º, n.º 2, al. b), subal. v) e segundo parágrafo | Cobre | `CFG-002`; `IAC-002`; [Política 25 §6](/sbd-toe/assets/policies/policy-deploy-seguro#6-separação-de-ambientes-e-dados); `ARC-011` |
| DORA-RTS1774-8-2-b-vi | art. 8.º, n.º 2, al. b), subal. vi) | Cobre | `CFG-002`; `IAC-002` |
| DORA-RTS1774-10-1 | art. 10.º, n.º 1 | Cobre | [Política 10 §8](/sbd-toe/assets/policies/policy-dependencias#8-alertas-de-vulnerabilidades-em-produção); [Política 12 §6.1](/sbd-toe/assets/policies/policy-excecoes-cve#61-ttl-por-severidade-e-tipo); [Política 19 §4.3](/sbd-toe/assets/policies/policy-estrategia-testes#43-slas-de-triagem-e-resolução); `TST-003` |
| DORA-RTS1774-10-2-a | art. 10.º, n.º 2, al. a) | Cobre | [Política 10 §8](/sbd-toe/assets/policies/policy-dependencias#8-alertas-de-vulnerabilidades-em-produção) |
| DORA-RTS1774-10-2-d | art. 10.º, n.º 2, al. d) e quarto parágrafo | Cobre | `DEP-001`; `DEP-007`; `DEP-008`; [Política 11 §7](/sbd-toe/assets/policies/policy-sbom#7-inventário-em-produção) |
| DORA-RTS1774-10-2-e | art. 10.º, n.º 2, al. e) | Cobre | `DST-007`; `GOV-015` |
| DORA-RTS1774-10-2-f | art. 10.º, n.º 2, al. f) e quinto parágrafo | Cobre | [Política 19 §4.3](/sbd-toe/assets/policies/policy-estrategia-testes#43-slas-de-triagem-e-resolução); [Cap. 12 US-16](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle#us-16---cobertura-attck-e-priorização-epsskev) |
| DORA-RTS1774-10-2-g | art. 10.º, n.º 2, al. g) | Cobre | `TST-006`; `DEP-010` |
| DORA-RTS1774-10-2-h | art. 10.º, n.º 2, al. h) | Cobre | `TST-003`; `DEP-010` |
| DORA-RTS1774-10-4-a | art. 10.º, n.º 4, al. a) | Cobre | `DEP-008`; [Política 13 §2](/sbd-toe/assets/policies/policy-atualizacao-automatica#2-âmbito-e-obrigatoriedade) |
| DORA-RTS1774-10-4-b | art. 10.º, n.º 4, al. b) | Cobre | [Política 26 §7](/sbd-toe/assets/policies/policy-aprovacao-release#7-releases-de-emergência); [Política 32 §5](/sbd-toe/assets/policies/policy-irp#5-playbooks-de-resposta) |
| DORA-RTS1774-10-4-c | art. 10.º, n.º 4, al. c) | Cobre | `DPL-007`; `CFG-002` |
| DORA-RTS1774-10-4-d | art. 10.º, n.º 4, al. d) | Cobre | [Política 19 §4.3](/sbd-toe/assets/policies/policy-estrategia-testes#43-slas-de-triagem-e-resolução); `DEP-007`; [Política 05 §7](/sbd-toe/assets/policies/policy-gestao-excecoes#7-prazos-máximos-de-validade-ttl) |
| DORA-RTS1774-11-1 | art. 11.º, n.º 1 | Cobre | `CLA-003` |
| DORA-RTS1774-11-2-a | art. 11.º, n.º 2, al. a) | Cobre | `ACC-001`; `ACC-006`; `CLA-003` |
| DORA-RTS1774-12-1 | art. 12.º, n.º 1 | Cobre | `OPS-001`; `LOG-001`; [Política 29 §4](/sbd-toe/assets/policies/policy-logging-estruturado#4-eventos-de-segurança-obrigatórios) |
| DORA-RTS1774-12-2-a | art. 12.º, n.º 2, al. a) e segundo parágrafo | Cobre | `OPS-002`; `OPS-003`; [Política 29 §7](/sbd-toe/assets/policies/policy-logging-estruturado#7-retenção-de-logs) |
| DORA-RTS1774-12-2-b | art. 12.º, n.º 2, al. b) | Cobre | `LOG-002`; `LOG-009` |
| DORA-RTS1774-13-a | art. 13.º, al. a) | Cobre | `ARC-006`; `ARC-011`; `CNT-012` |
| DORA-RTS1774-13-e | art. 13.º, al. e) | Cobre | `ENC-001`; `INT-004` |
| DORA-RTS1774-13-g | art. 13.º, al. g) | Cobre | `ARC-002`; `ARC-008` |
| DORA-RTS1774-13-h | art. 13.º, al. h) e segundo parágrafo | Cobre | `ARC-006` |
| DORA-RTS1774-13-j | art. 13.º, al. j) | Cobre | [Política 32 §4.2](/sbd-toe/assets/policies/policy-irp#42-contenção-t1---início-imediato-após-confirmação); [Política 32 §5](/sbd-toe/assets/policies/policy-irp#5-playbooks-de-resposta) |
| DORA-RTS1774-13-m | art. 13.º, al. m) | Apoia evidência | `GOV-006` |
| DORA-RTS1774-14-1 | art. 14.º, n.º 1 | Cobre | `ENC-001`; `INT-003` |
| DORA-RTS1774-14-1-a | art. 14.º, n.º 1, al. a) | Cobre | `ENC-001`; `INT-005` |
| DORA-RTS1774-14-1-c | art. 14.º, n.º 1, al. c) | Apoia evidência | [Política 33 §4.1](/sbd-toe/assets/policies/policy-contratacao-segura#41-cláusulas-universais-todos-os-níveis) |
| DORA-RTS1774-14-2 | art. 14.º, n.º 2 | Cobre | `ENC-001`; `INT-005`; `CLA-003` |
| DORA-RTS1774-15-1 | art. 15.º, n.º 1 | Apoia evidência | `REQ-001`; [Política 09 §6.1](/sbd-toe/assets/policies/policy-arquitetura-segura#61-inventário-de-trust-boundaries) |
| DORA-RTS1774-15-2 | art. 15.º, n.º 2 | Apoia evidência | `REQ-001` |
| DORA-RTS1774-15-3 | art. 15.º, n.º 3, als. a) a f) | Apoia evidência | `REQ-001`; `ARC-003` |
| DORA-RTS1774-15-3-g | art. 15.º, n.º 3, al. g) | Cobre | `DPL-001`; `DPL-003`; `ARC-012` |
| DORA-RTS1774-15-4 | art. 15.º, n.º 4 | Apoia evidência | `REQ-007` |
| DORA-RTS1774-16-1 | art. 16.º, n.º 1, prim. parágrafo | Cobre | `DEV-001`; [Política 15 §2](/sbd-toe/assets/policies/policy-revisao-codigo#2-âmbito-e-obrigatoriedade); [4️⃣ Coding Guidelines Básicas e Validação Automática (Cap. 06)](/sbd-toe/sbd-manual/fundamentos/baseline#4️⃣-coding-guidelines-básicas-e-validação-automática-cap-06) |
| DORA-RTS1774-16-1-a | art. 16.º, n.º 1, al. a) | Cobre | `DEV-001`; `DEV-002`; `DEV-003` |
| DORA-RTS1774-16-1-b | art. 16.º, n.º 1, al. b) | Cobre | `REQ-001`; `REQ-002`; `REQ-003` |
| DORA-RTS1774-16-1-c | art. 16.º, n.º 1, al. c) | Cobre | [🛠️ Práticas](/sbd-toe/sbd-manual/cicd-seguro/addon/gestao-codigo-fonte#️-práticas); `CIC-007`; `DPL-002`; [Política 20 §6](/sbd-toe/assets/policies/policy-release-seguro#6-imutabilidade-do-artefacto) |
| DORA-RTS1774-16-2 | art. 16.º, n.º 2, prim. parágrafo | Cobre | `DPL-001`; `DPL-003`; `TST-001` |
| DORA-RTS1774-16-3-a | art. 16.º, n.º 3, al. a) | Cobre | `DEV-003`; `TST-002` |
| DORA-RTS1774-16-3-b | art. 16.º, n.º 3, al. b) | Cobre | `TST-003`; [Política 19 §4.3](/sbd-toe/assets/policies/policy-estrategia-testes#43-slas-de-triagem-e-resolução) |
| DORA-RTS1774-16-3-c | art. 16.º, n.º 3, al. c) | Cobre | `TST-003`; `GOV-011` |
| DORA-RTS1774-16-4 | art. 16.º, n.º 4 | Cobre | `DEP-002`; [Política 19 §2.1](/sbd-toe/assets/policies/policy-estrategia-testes#21-matriz-de-obrigatoriedade-por-nível) |
| DORA-RTS1774-16-5 | art. 16.º, n.º 5 | Cobre | [Política 25 §6](/sbd-toe/assets/policies/policy-deploy-seguro#6-separação-de-ambientes-e-dados); [🛡️ Requisitos de segurança por ambiente](/sbd-toe/sbd-manual/deploy-seguro/addon/08-segregacao-e-validacao-operacional#️-requisitos-de-segurança-por-ambiente); [4.1 Prescrições obrigatórias](/sbd-toe/sbd-manual/testes-seguranca/addon/evidencia-reprodutibilidade#41-prescrições-obrigatórias) |
| DORA-RTS1774-16-7 | art. 16.º, n.º 7 | Cobre | [🛠️ Práticas](/sbd-toe/sbd-manual/cicd-seguro/addon/gestao-codigo-fonte#️-práticas); [🛠️ Práticas](/sbd-toe/sbd-manual/cicd-seguro/addon/gestao-codigo-fonte#️-práticas); `CIC-001` |
| DORA-RTS1774-16-8 | art. 16.º, n.º 8 | Cobre | `DEP-002`; `DEP-006`; [Política 10 §3](/sbd-toe/assets/policies/policy-dependencias#3-critérios-de-aprovação-de-dependências) |
| DORA-RTS1774-17-1-a | art. 17.º, n.º 1, al. a) | Cobre | `DPL-003`; `CIC-004` |
| DORA-RTS1774-17-1-b | art. 17.º, n.º 1, al. b) | Cobre | [Política 22 §5](/sbd-toe/assets/policies/policy-aprovacao-plan-iac#5-separação-de-funções-sod); `CIC-011`; `DPL-001` |
| DORA-RTS1774-17-1-c | art. 17.º, n.º 1, al. c) | Cobre | `CIC-008`; `DPL-007` |
| DORA-RTS1774-17-1-e | art. 17.º, n.º 1, al. e) | Cobre | `DPL-005`; [Política 27 §7](/sbd-toe/assets/policies/policy-rollback#7-teste-periódico-de-rollback) |
| DORA-RTS1774-17-1-f | art. 17.º, n.º 1, al. f) | Cobre | [Política 26 §7](/sbd-toe/assets/policies/policy-aprovacao-release#7-releases-de-emergência); [Política 22 §9](/sbd-toe/assets/policies/policy-aprovacao-plan-iac#9-apply-de-emergência) |
| DORA-RTS1774-17-1-g | art. 17.º, n.º 1, al. g) | Cobre | [Política 26 §7](/sbd-toe/assets/policies/policy-aprovacao-release#7-releases-de-emergência); [Política 22 §9](/sbd-toe/assets/policies/policy-aprovacao-plan-iac#9-apply-de-emergência) |
| DORA-RTS1774-17-1-h | art. 17.º, n.º 1, al. h) | Cobre | `ARC-009`; `REQ-005`; [Política 04 §4.1](/sbd-toe/assets/policies/policy-revisao-periodica-risco#41-triggers-que-obrigam-a-revisão-imediata) |
| DORA-RTS1774-19-a | art. 19.º, al. a) | Apoia evidência | `TRN-002`; `GOV-002` |
| DORA-RTS1774-19-b-i | art. 19.º, al. b), subal. i) | Apoia evidência | `TRN-002`; `TRN-007`; `GOV-013` |
| DORA-RTS1774-19-b-ii | art. 19.º, al. b), subal. ii) | Apoia evidência | `TRN-002` |
| DORA-RTS1774-20-1 | art. 20.º, n.º 1 | Cobre | `ACC-004`; `CIC-009`; [Cap. 07 US-20](/sbd-toe/sbd-manual/cicd-seguro/aplicacao-lifecycle#us-20); `GOV-017` |
| DORA-RTS1774-20-2-b | art. 20.º, n.º 2, al. b) e terceiro parágrafo | Cobre | `ACC-008`; [Política 33 §7.1](/sbd-toe/assets/policies/policy-contratacao-segura#71-checklist-de-offboarding); `GOV-014`; `GOV-017`; `GOV-017` |
| DORA-RTS1774-21-a | art. 21.º, al. a) | Cobre | `ACC-001`; `ACC-002` |
| DORA-RTS1774-21-b | art. 21.º, al. b) | Cobre | `CIC-008`; [Política 22 §5](/sbd-toe/assets/policies/policy-aprovacao-plan-iac#5-separação-de-funções-sod); `ACC-004` |
| DORA-RTS1774-21-c | art. 21.º, al. c) | Cobre | `ACC-004`; [Cap. 07 US-20](/sbd-toe/sbd-manual/cicd-seguro/aplicacao-lifecycle#us-20); `GOV-017`; `GOV-017` |
| DORA-RTS1774-21-d | art. 21.º, al. d) | Cobre | `ACC-003`; `ACC-005`; `ACC-006` |
| DORA-RTS1774-21-e | art. 21.º, al. e), subals. i) a iii) | Cobre | `ACC-008`; [Política 33 §7.2](/sbd-toe/assets/policies/policy-contratacao-segura#72-prazos-de-offboarding); `GOV-016`; `GOV-016` |
| DORA-RTS1774-21-e-ii | art. 21.º, al. e), subal. ii), e parágrafo 'Para efeitos da alínea e), subalínea ii)' | Cobre | `ACC-004`; `GOV-016`; `GOV-016` |
| DORA-RTS1774-21-e-iv | art. 21.º, al. e), subal. iv) | Cobre | `ACC-010`; `GOV-014`; `ACC-010`; `GOV-014` |
| DORA-RTS1774-21-f-i | art. 21.º, al. f), subal. i) | Cobre | `AUT-001`; `AUT-008`; `CLA-003` |
| DORA-RTS1774-21-f-ii | art. 21.º, al. f), subal. ii) | Cobre | `AUT-001`; [🛡️ Requisitos de segurança por ambiente](/sbd-toe/sbd-manual/deploy-seguro/addon/08-segregacao-e-validacao-operacional#️-requisitos-de-segurança-por-ambiente); `GOV-016` |
| DORA-RTS1774-22-a | art. 22.º, al. a) | Cobre | [Política 32 §2](/sbd-toe/assets/policies/policy-irp#2-âmbito-e-obrigatoriedade); [Política 32 §3](/sbd-toe/assets/policies/policy-irp#3-critérios-de-activação-do-irp) |
| DORA-RTS1774-22-c | art. 22.º, al. c) | Cobre | `OPS-005`; `OPS-007` |
| DORA-RTS1774-22-d | art. 22.º, al. d) e segundo parágrafo | Cobre | [Política 32 §4.2](/sbd-toe/assets/policies/policy-irp#42-contenção-t1---início-imediato-após-confirmação); [Política 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória) |
| DORA-RTS1774-22-e | art. 22.º, al. e) | Cobre | [Política 32 §4.7](/sbd-toe/assets/policies/policy-irp#47-análise-de-recorrência); [Política 32 §4.6](/sbd-toe/assets/policies/policy-irp#46-post-mortem); `OPS-010` |
| DORA-RTS1774-23-1 | art. 23.º, n.º 1 | Cobre | [Política 32 §4.1](/sbd-toe/assets/policies/policy-irp#41-triagem-t0----15-minutos-de-detecção); `OPS-007` |
| DORA-RTS1774-23-2-c | art. 23.º, n.º 2, al. c) | Cobre | [Política 31 §3](/sbd-toe/assets/policies/policy-gestao-alertas#3-classificação-de-alertas); `OPS-006`; [Política 31 §7](/sbd-toe/assets/policies/policy-gestao-alertas#7-alertas-p1-em-horas-não-laborais-on-call) |
| DORA-RTS1774-23-2-d | art. 23.º, n.º 2, al. d) | Cobre | `LOG-004`; `OPS-009` |
| DORA-RTS1774-23-5 | art. 23.º, n.os 5 e 6 | Cobre | [Política 32 §3](/sbd-toe/assets/policies/policy-irp#3-critérios-de-activação-do-irp) |
| DORA-RTS1774-24-1-b | art. 24.º, n.º 1, al. b) | Apoia evidência | [🔁 Mapeamento prático entre DRP/BIA e risco de segurança](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/adopcao-drp-bia#-mapeamento-prático-entre-drpbia-e-risco-de-segurança) |
| DORA-RTS1774-28-1 | art. 28.º, n.º 1 | Apoia evidência | `GOV-001` |
| DORA-RTS1774-28-2-a | art. 28.º, n.º 2, al. a) | Apoia evidência | `GOV-001` |
| DORA-RTS1774-28-2-b | art. 28.º, n.º 2, al. b) | Apoia evidência | `GOV-002`; `GOV-003` |
| DORA-RTS1774-28-2-c | art. 28.º, n.º 2, al. c) | Apoia evidência | `REQ-001` |
| DORA-RTS1774-28-2-d | art. 28.º, n.º 2, al. d) | Apoia evidência | `CLA-002`; [🔁 Mapeamento prático entre DRP/BIA e risco de segurança](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/adopcao-drp-bia#-mapeamento-prático-entre-drpbia-e-risco-de-segurança) |
| DORA-RTS1774-28-2-f | art. 28.º, n.º 2, als. f) e g) | Apoia evidência | `GOV-001` |
| DORA-RTS1774-28-2-h | art. 28.º, n.º 2, al. h) | Apoia evidência | `TRN-001` |
| DORA-RTS1774-28-2-i | art. 28.º, n.º 2, al. i) | Apoia evidência | [Política 35 §5](/sbd-toe/assets/policies/policy-kpis-governacao#5-cadência-de-recolha-e-reporte) |
| DORA-RTS1774-28-5 | art. 28.º, n.º 5 | Apoia evidência | [Política 35 §5](/sbd-toe/assets/policies/policy-kpis-governacao#5-cadência-de-recolha-e-reporte) |
| DORA-RTS1774-28-6 | art. 28.º, n.º 6 | Apoia evidência | `GOV-010` |
| DORA-RTS1774-29-1 | art. 29.º, n.º 1 | Apoia evidência | `GOV-001` |
| DORA-RTS1774-30-2 | art. 30.º, n.º 2 | Apoia evidência | `GOV-007` |
| DORA-RTS1774-31-1 | art. 31.º, n.º 1 | Cobre | [Política 03 §5](/sbd-toe/assets/policies/policy-aceitacao-risco#5-limiares-de-aceitação-por-nível); [Política 02 §3](/sbd-toe/assets/policies/policy-classificacao-risco#3-modelo-de-classificação---eixos-edi); `THR-004`; [Política 04 §4.1](/sbd-toe/assets/policies/policy-revisao-periodica-risco#41-triggers-que-obrigam-a-revisão-imediata) |
| DORA-RTS1774-31-2 | art. 31.º, n.º 2 | Cobre | [Política 02 §5](/sbd-toe/assets/policies/policy-classificacao-risco#5-cadência-de-revisão-periódica); `CLA-005` |
| DORA-RTS1774-31-3 | art. 31.º, n.º 3 | Cobre | [Política 10 §8](/sbd-toe/assets/policies/policy-dependencias#8-alertas-de-vulnerabilidades-em-produção); [Política 08 §4.2](/sbd-toe/assets/policies/policy-threat-modeling#42-cadência-periódica) |
| DORA-RTS1774-31-4 | art. 31.º, n.º 4 | Cobre | `OPS-005`; [Política 32 §3](/sbd-toe/assets/policies/policy-irp#3-critérios-de-activação-do-irp) |
| DORA-RTS1774-33-a | art. 33.º, al. a) | Cobre | `ACC-002`; `ACC-001` |
| DORA-RTS1774-33-b | art. 33.º, al. b) | Cobre | `ACC-004`; `LOG-002` |
| DORA-RTS1774-33-c | art. 33.º, al. c) e segundo parágrafo | Cobre | `ACC-004`; [Política 29 §4](/sbd-toe/assets/policies/policy-logging-estruturado#4-eventos-de-segurança-obrigatórios); `GOV-016` |
| DORA-RTS1774-33-d | art. 33.º, al. d) e terceiro parágrafo | Cobre | `AUT-001`; [🛡️ Requisitos de segurança por ambiente](/sbd-toe/sbd-manual/deploy-seguro/addon/08-segregacao-e-validacao-operacional#️-requisitos-de-segurança-por-ambiente); `GOV-016` |
| DORA-RTS1774-33-e | art. 33.º, al. e) | Cobre | `ACC-010`; `ACC-008`; `ACC-010` |
| DORA-RTS1774-34-d | art. 34.º, al. d) | Cobre | `DEP-002`; `CNT-002`; [Política 10 §9](/sbd-toe/assets/policies/policy-dependencias#9-auditoria-periódica); [Política 19 §4.3](/sbd-toe/assets/policies/policy-estrategia-testes#43-slas-de-triagem-e-resolução) |
| DORA-RTS1774-34-g | art. 34.º, al. g) | Cobre | [6️⃣ Registo e Monitorização Essencial (Cap. 12)](/sbd-toe/sbd-manual/fundamentos/baseline#6️⃣-registo-e-monitorização-essencial-cap-12); `OPS-005`; `OPS-009` |
| DORA-RTS1774-34-h | art. 34.º, al. h) | Cobre | [Cap. 12 US-16](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle#us-16---cobertura-attck-e-priorização-epsskev); [Política 10 §8](/sbd-toe/assets/policies/policy-dependencias#8-alertas-de-vulnerabilidades-em-produção) |
| DORA-RTS1774-35-c | art. 35.º, al. c) | Cobre | `ARC-002`; `ARC-006` |
| DORA-RTS1774-35-d | art. 35.º, al. d) | Cobre | `ENC-001`; `INT-005` |
| DORA-RTS1774-36-1 | art. 36.º, n.º 1 | Cobre | `TST-001` |
| DORA-RTS1774-36-2 | art. 36.º, n.º 2 | Cobre | `TST-001`; `TST-007` |
| DORA-RTS1774-36-3 | art. 36.º, n.º 3 | Cobre | `TST-003`; `TST-006` |
| DORA-RTS1774-37 | art. 37.º, prim. parágrafo | Cobre | `DEV-001`; [4️⃣ Coding Guidelines Básicas e Validação Automática (Cap. 06)](/sbd-toe/sbd-manual/fundamentos/baseline#4️⃣-coding-guidelines-básicas-e-validação-automática-cap-06) |
| DORA-RTS1774-37-a | art. 37.º, al. a) | Cobre | `REQ-001`; `REQ-002` |
| DORA-RTS1774-37-b | art. 37.º, al. b) | Cobre | `DPL-001`; `DPL-003` |
| DORA-RTS1774-37-c | art. 37.º, al. c) | Cobre | [🛠️ Práticas](/sbd-toe/sbd-manual/cicd-seguro/addon/gestao-codigo-fonte#️-práticas); `CIC-007` |
| DORA-RTS1774-38-1 | art. 38.º, n.º 1 | Apoia evidência | `REQ-001` |
| DORA-RTS1774-39-2-d | art. 39.º, n.º 2, als. d) a f) | Cobre | [🔁 Mapeamento prático entre DRP/BIA e risco de segurança](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/adopcao-drp-bia#-mapeamento-prático-entre-drpbia-e-risco-de-segurança); [Política 27 §6](/sbd-toe/assets/policies/policy-rollback#6-rto-de-rollback-por-nível); [Política 32 §3](/sbd-toe/assets/policies/policy-irp#3-critérios-de-activação-do-irp); `OPS-017`; `OPS-017` |
| DORA-RTS1774-39-2-g | art. 39.º, n.º 2, al. g) | Cobre | `OPS-016` |
| DORA-RTS1772-1-1 | art. 1.º, n.º 1 | Cobre | `CTX-DORA-R02`; [Política 32 §4.3](/sbd-toe/assets/policies/policy-irp#43-investigação) |
| DORA-RTS1772-1-2 | art. 1.º, n.º 2 | Cobre | `CTX-DORA-R02`; [Política 32 §4.3](/sbd-toe/assets/policies/policy-irp#43-investigação) |
| DORA-RTS1772-1-3 | art. 1.º, n.º 3 | Cobre | `CTX-DORA-R02`; [Política 32 §4.3](/sbd-toe/assets/policies/policy-irp#43-investigação) |
| DORA-RTS1772-1-4 | art. 1.º, n.º 4 | Apoia evidência | `LOG-010` |
| DORA-RTS1772-1-5 | art. 1.º, n.º 5; art. 9.º, n.º 1, 2.º par. | Cobre | `CTX-DORA-R02`; [Política 32 §4.3](/sbd-toe/assets/policies/policy-irp#43-investigação) |
| DORA-RTS1772-2-1 | art. 2.º, n.º 1 | Cobre | `CTX-DORA-R02`; [Política 32 §4.3](/sbd-toe/assets/policies/policy-irp#43-investigação) |
| DORA-RTS1772-2-2 | art. 2.º, n.º 2 | Cobre | `CTX-DORA-R02`; [Política 32 §4.3](/sbd-toe/assets/policies/policy-irp#43-investigação) |
| DORA-RTS1772-3-1 | art. 3.º, n.º 1 | Cobre | `CTX-DORA-R02`; [Política 32 §4.3](/sbd-toe/assets/policies/policy-irp#43-investigação) |
| DORA-RTS1772-3-2 | art. 3.º, n.º 2 | Cobre | `CTX-DORA-R02`; [Política 32 §4.3](/sbd-toe/assets/policies/policy-irp#43-investigação) |
| DORA-RTS1772-4 | art. 4.º | Cobre | `CTX-DORA-R02`; [Política 32 §4.3](/sbd-toe/assets/policies/policy-irp#43-investigação) |
| DORA-RTS1772-5 | art. 5.º | Cobre | `CTX-DORA-R02`; [Política 32 §4.3](/sbd-toe/assets/policies/policy-irp#43-investigação) |
| DORA-RTS1772-6 | art. 6.º | Cobre | `CTX-DORA-R02`; [Política 32 §4.3](/sbd-toe/assets/policies/policy-irp#43-investigação) |
| DORA-RTS1772-7-1 | art. 7.º, n.os 1 e 2 | Cobre | `CTX-DORA-R02`; [Política 32 §4.3](/sbd-toe/assets/policies/policy-irp#43-investigação) |
| DORA-RTS1772-7-3 | art. 7.º, n.os 3 e 4 | Cobre | `CTX-DORA-R02`; [Política 32 §4.3](/sbd-toe/assets/policies/policy-irp#43-investigação) |
| DORA-RTS1772-8-1 | art. 8.º, n.º 1; art. 9.º | Apoia evidência | [Política 32 §4.1](/sbd-toe/assets/policies/policy-irp#41-triagem-t0----15-minutos-de-detecção); [Incidentes, Classificação e Reporte (Artigos 17–23 DORA)](/sbd-toe/cross-check-normativo/dora/intro#incidentes-classificação-e-reporte-artigos-1723-dora) |
| DORA-RTS1772-8-2 | art. 8.º, n.º 2, 1.º par. | Cobre | `CTX-DORA-R02`; [Política 32 §4.7](/sbd-toe/assets/policies/policy-irp#47-análise-de-recorrência); [Incidentes, Classificação e Reporte (Artigos 17–23 DORA)](/sbd-toe/cross-check-normativo/dora/intro#incidentes-classificação-e-reporte-artigos-1723-dora) |
| DORA-RTS1772-8-2-p2 | art. 8.º, n.º 2, 2.º par. | Cobre | `CTX-DORA-R02` |
| DORA-RTS1772-10 | art. 10.º | Apoia evidência | [Cap. 12 US-16](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle#us-16---cobertura-attck-e-priorização-epsskev) |
| DORA-RTS301-5-1-a | art. 5.º, n.º 1, al. a) | Apoia evidência | [Política 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória) |
| DORA-RTS301-5-1-b | art. 5.º, n.º 1, al. b) | Apoia evidência | [Política 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória) |
| DORA-RTS301-5-1-c | art. 5.º, n.º 1, al. c) | Apoia evidência | [Política 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória) |
| DORA-RTS301-5-2 | art. 5.º, n.º 2 | Apoia evidência | [Política 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória) |
| DORA-RTS1190-4-2-a | art. 4.º, n.º 2, al. a) | Apoia evidência | [6) Checklist de readiness (binário)](/sbd-toe/sbd-manual/testes-seguranca/addon/tlpt-readiness#6-checklist-de-readiness-binário) |
| DORA-RTS1190-4-2-c | art. 4.º, n.º 2, al. c) | Apoia evidência | [Política 32 §3](/sbd-toe/assets/policies/policy-irp#3-critérios-de-activação-do-irp) |
| DORA-RTS1190-5-1 | art. 5.º, n.º 1 | Apoia evidência | [Política 36 §4.2](/sbd-toe/assets/policies/policy-pentesting#42-regras-de-engajamento) |
| DORA-RTS1190-5-2 | art. 5.º, n.º 2 | Apoia evidência | [Política 36 §4.2](/sbd-toe/assets/policies/policy-pentesting#42-regras-de-engajamento) |
| DORA-RTS1190-6-1 | art. 6.º, n.º 1 | Apoia evidência | [Política 36 §4.2](/sbd-toe/assets/policies/policy-pentesting#42-regras-de-engajamento) |
| DORA-RTS1190-7-1-i | art. 7.º, n.º 1, al. i) | Apoia evidência | [Política 36 §4.2](/sbd-toe/assets/policies/policy-pentesting#42-regras-de-engajamento) |
| DORA-RTS1190-9-6 | art. 9.º, n.º 6, 1.º período; anexo II | Apoia evidência | [6) Checklist de readiness (binário)](/sbd-toe/sbd-manual/testes-seguranca/addon/tlpt-readiness#6-checklist-de-readiness-binário) |
| DORA-RTS1190-9-7 | art. 9.º, n.º 7 | Apoia evidência | [6) Checklist de readiness (binário)](/sbd-toe/sbd-manual/testes-seguranca/addon/tlpt-readiness#6-checklist-de-readiness-binário) |
| DORA-RTS1190-10-1 | art. 10.º, n.º 1 | Apoia evidência | [6) Checklist de readiness (binário)](/sbd-toe/sbd-manual/testes-seguranca/addon/tlpt-readiness#6-checklist-de-readiness-binário); [Cap. 12 US-16](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle#us-16---cobertura-attck-e-priorização-epsskev) |
| DORA-RTS1190-13-2 | art. 13.º, n.º 2 | Apoia evidência | `TST-003`; [Política 32 §4.6](/sbd-toe/assets/policies/policy-irp#46-post-mortem) |

### Lacuna declarada (107) {#lacuna}

Força «parcial» ou «lacuna»: o Manual não cobre, ou cobre só em parte, e diz o que falta. As lacunas pendentes de uma ronda do AppSec Core estão marcadas com o nome da ronda.

| Obrigação | Referência | Força | Como o Manual responde | O que falta |
|---|---|---|---|---|
| DORA-6-2 | art. 6.º, n.º 2 | Parcial | `CLA-003`; `ARC-006`; `ACC-006` | Proteção de hardware, servidores físicos, instalações e centros de dados. |
| DORA-6-3 | art. 6.º, n.º 3, 1.º per. | Parcial | `CLA-003`; [Política 32 §5](/sbd-toe/assets/policies/policy-irp#5-playbooks-de-resposta) | Medidas de minimização de impacto ao nível da entidade (redundância, continuidade). |
| DORA-6-8-c | art. 6.º, n.º 8, al. c) | Parcial | `GOV-011`; [Para que serve este documento](/sbd-toe/sbd-manual/governanca-contratacao/kpis-kri-executivo#para-que-serve-este-documento) | Objetivos de segurança da informação da entidade inscritos na estratégia de resiliência. |
| DORA-6-8-d | art. 6.º, n.º 8, al. d) | Parcial | `ARC-007`; `ARC-010` | Arquitetura de referência TIC da entidade e alterações necessárias aos objetivos de negócio. |
| DORA-6-8-e | art. 6.º, n.º 8, al. e) | Parcial | [6️⃣ Registo e Monitorização Essencial (Cap. 12)](/sbd-toe/sbd-manual/fundamentos/baseline#6️⃣-registo-e-monitorização-essencial-cap-12); `OPS-005`; `OPS-007` | Inscrição dos mecanismos na estratégia (documento de estratégia é organizacional). |
| DORA-6-8-g | art. 6.º, n.º 8, al. g) | Parcial | `TST-001` | Estratégia de testes de resiliência operacional (cap. IV) — o Manual tem estratégia de testes de segurança aplicacional; faltam testes de continuidade, desempenho e cenários. |
| DORA-7 | art. 7.º, als. a) a d) | Parcial | `OPS-015`; `DEP-007` | Dimensionamento de capacidade (picos) e resiliência tecnológica em condições de tensão de mercado. |
| DORA-8-1 | art. 8.º, n.º 1 | Parcial | `CLA-001`; `CLA-005`; `CLA-008`; `DEP-001` | Identificação e classificação de funções de negócio e papéis; o Manual classifica aplicações (E+D+I), não funções críticas ou importantes. |
| DORA-8-2 | art. 8.º, n.º 2 | Parcial | `THR-001`; [Política 08 §4.2](/sbd-toe/assets/policies/policy-threat-modeling#42-cadência-periódica); [Política 10 §8](/sbd-toe/assets/policies/policy-dependencias#8-alertas-de-vulnerabilidades-em-produção) | Threat modeling formal só a partir de L2; revisão anual de cenários de risco não prescrita para L1. |
| DORA-8-4 | art. 8.º, n.º 4 | Parcial | `CLA-008`; `DEP-001`; `ARC-010`; `IAC-008` | Inventário de hardware, recursos de rede e ativos remotos; mapeamento de configuração e interdependências fora do perímetro aplicacional. |
| DORA-8-5 | art. 8.º, n.º 5 | Parcial | `DEP-001`; `GOV-007` | Identificação de processos de negócio dependentes de terceiros TIC e das interligações com FCI. |
| DORA-8-6 | art. 8.º, n.º 6 | Parcial | `CLA-008`; [Política 11 §7](/sbd-toe/assets/policies/policy-sbom#7-inventário-em-produção) | Inventários de funções e de dependências de terceiros atualizados a cada alteração importante. |
| DORA-8-7 | art. 8.º, n.º 7 | Parcial | [🛠️ Abordagem proposta](/sbd-toe/sbd-manual/governanca-contratacao/addon/governanca-legada#️-abordagem-proposta); [Política 04 §4.1](/sbd-toe/assets/policies/policy-revisao-periodica-risco#41-triggers-que-obrigam-a-revisão-imediata) | Avaliação anual específica de sistemas legados e avaliação antes/depois de cada conexão. |
| DORA-9-2 | art. 9.º, n.º 2 | Parcial | `ENC-001`; `ENC-002`; `ENC-009` | Dados em utilização; disponibilidade/continuidade dos sistemas. |
| DORA-9-3-d | art. 9.º, n.º 3, al. d) | Parcial | `CFG-004`; `IAC-007`; [Política 22 §5](/sbd-toe/assets/policies/policy-aprovacao-plan-iac#5-separação-de-funções-sod) | Controlos contra erro humano na administração de dados em produção (fora de IaC/deploy). |
| DORA-9-4-b | art. 9.º, n.º 4, al. b), e 2.º parágrafo | Parcial | `ARC-006`; `ARC-011`; `CNT-012`; [Política 32 §4.2](/sbd-toe/assets/policies/policy-irp#42-contenção-t1---início-imediato-após-confirmação) | Configuração da interligação de redes para corte/segmentação instantâneos ao nível da entidade. |
| DORA-9-4-c | art. 9.º, n.º 4, al. c) | Parcial | `ACC-001`; `ACC-002`; `ACC-010` | Acesso físico. |
| DORA-9-4-e | art. 9.º, n.º 4, al. e), e 3.º parágrafo | Parcial | `DPL-001`; `DPL-004`; `CIC-004`; `IAC-007`; [Política 26 §7](/sbd-toe/assets/policies/policy-aprovacao-release#7-releases-de-emergência) | Alterações de hardware/firmware e de parâmetros fora de pipelines. |
| DORA-9-4-f | art. 9.º, n.º 4, al. f) | Parcial | `DEP-007`; [Política 19 §4.3](/sbd-toe/assets/policies/policy-estrategia-testes#43-slas-de-triagem-e-resolução); [Política 13 §2](/sbd-toe/assets/policies/policy-atualizacao-automatica#2-âmbito-e-obrigatoriedade); [Política 24 §6](/sbd-toe/assets/policies/policy-golden-base-images#6-sla-de-patching) | Correções de sistemas operativos, firmware e hardware fora das imagens base. |
| DORA-10-1 | art. 10.º, n.º 1 | Parcial | [6️⃣ Registo e Monitorização Essencial (Cap. 12)](/sbd-toe/sbd-manual/fundamentos/baseline#6️⃣-registo-e-monitorização-essencial-cap-12); `OPS-005`; `OPS-009` | Identificação de pontos únicos de falha significativos; desempenho de rede. |
| DORA-10-3 | art. 10.º, n.º 3 | Parcial | `OPS-006`; [Política 31 §7](/sbd-toe/assets/policies/policy-gestao-alertas#7-alertas-p1-em-horas-não-laborais-on-call) | Afetação de recursos humanos à monitorização (decisão organizacional). |
| DORA-11-2 | art. 11.º, n.º 2, als. a) a e) | Parcial | [Política 32 §4.2](/sbd-toe/assets/policies/policy-irp#42-contenção-t1---início-imediato-após-confirmação); [Política 32 §4.5](/sbd-toe/assets/policies/policy-irp#45-recuperação); [Política 32 §7](/sbd-toe/assets/policies/policy-irp#7-comunicação-durante-o-incidente) | Planos de continuidade das funções críticas e estimativa preliminar de impactos; o Manual cobre contenção e resposta a incidentes. |
| DORA-11-3 | art. 11.º, n.º 3 | Parcial | [Política 32 §5](/sbd-toe/assets/policies/policy-irp#5-playbooks-de-resposta); [Política 27 §7](/sbd-toe/assets/policies/policy-rollback#7-teste-periódico-de-rollback) | Planos de recuperação de TIC para além de playbooks/rollback; auditoria interna independente. |
| DORA-11-4 | art. 11.º, n.º 4 | Parcial | [Política 32 §8](/sbd-toe/assets/policies/policy-irp#8-testes-periódicos-do-irp) | Testes de planos de continuidade (incl. funções externalizadas); só se testam o IRP e o rollback. |
| DORA-11-5 | art. 11.º, n.º 5 | Parcial | [🔁 Mapeamento prático entre DRP/BIA e risco de segurança](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/adopcao-drp-bia#-mapeamento-prático-entre-drpbia-e-risco-de-segurança) | Realização da BIA e desenho de redundância dos componentes críticos; o Manual apenas reutiliza BIA existente como input de classificação. |
| DORA-11-6-a | art. 11.º, n.º 6, al. a), e 2.º parágrafo | Parcial | [Política 32 §8](/sbd-toe/assets/policies/policy-irp#8-testes-periódicos-do-irp); [Política 27 §7](/sbd-toe/assets/policies/policy-rollback#7-teste-periódico-de-rollback); `CTX-DORA-R01`; `OPS-017` | Testes dos planos de continuidade das actividades da entidade (fora do âmbito do Manual); a recuperação da aplicação (OPS-016, OPS-017) e a comutação para a capacidade redundante (CTX-DORA-R01) estão prescritas. |
| DORA-12-7 | art. 12.º, n.º 7 | Parcial | [Política 32 §4.5](/sbd-toe/assets/policies/policy-irp#45-recuperação); `ENC-009` | Reconciliação de dados na recuperação e na reconstrução de dados de partes externas. |
| DORA-13-6 | art. 13.º, n.º 6 | Parcial | `TRN-001`; [7️⃣ Formação Inicial em Segurança (Cap. 13)](/sbd-toe/sbd-manual/fundamentos/baseline#7️⃣-formação-inicial-em-segurança-cap-13); [Política 37 §2](/sbd-toe/assets/policies/policy-formacao-seguranca#2-âmbito-e-obrigatoriedade) | Módulos obrigatórios para todo o pessoal (não técnico) e direção de topo; conteúdo de resiliência operacional digital. |
| DORA-16-1-c | art. 16.º, n.º 1, 2.º parágrafo, al. c) | Parcial | `ENC-001`; `ENC-002`; `DEP-007` | Resiliência dos sistemas (redundância). |
| DORA-16-1-e | art. 16.º, n.º 1, 2.º parágrafo, al. e) | Parcial | `DEP-001`; `GOV-007` | Dependências de prestadores de serviços TIC (não só componentes/fornecedores com acesso). |
| DORA-16-1-g | art. 16.º, n.º 1, 2.º parágrafo, al. g) | Parcial | `TST-001`; [Política 32 §8](/sbd-toe/assets/policies/policy-irp#8-testes-periódicos-do-irp) | Testes de planos de continuidade. |
| DORA-16-1-h | art. 16.º, n.º 1, 2.º parágrafo, al. h) | Parcial | [Política 32 §4.6](/sbd-toe/assets/policies/policy-irp#46-post-mortem); `TRN-001` | Formação da administração. |
| DORA-17-3-e | art. 17.º, n.º 3, al. e) | Parcial | [Política 32 §7](/sbd-toe/assets/policies/policy-irp#7-comunicação-durante-o-incidente) | Reporte de incidentes severos ao órgão de administração (só «management» em P1). |
| DORA-24-4 | art. 24.º, n.º 4 | Parcial | `THR-007`; `TST-008` | Garantia de independência dos testadores e gestão de conflitos de interesses de testadores internos. |
| DORA-25-1 | art. 25.º, n.º 1 | Parcial | [Política 19 §2.1](/sbd-toe/assets/policies/policy-estrategia-testes#21-matriz-de-obrigatoriedade-por-nível); `DEP-002`; `TST-008` | Testes de segurança de rede, segurança física, desempenho, compatibilidade, extremo-a-extremo e baseados em cenários. |
| DORA-26-1 | art. 26.º, n.º 1 | Parcial | [Quem está sujeito a TLPT](/sbd-toe/sbd-manual/testes-seguranca/addon/tlpt-readiness#quem-está-sujeito-a-tlpt); [4) O que o TLPT exige além do SbD-ToE](/sbd-toe/sbd-manual/testes-seguranca/addon/tlpt-readiness#4-o-que-o-tlpt-exige-além-do-sbd-toe) | Execução do TLPT segundo o RTS 2025/1190 declarada fora de âmbito; o Manual cobre a prontidão. |
| DORA-28-4-d | art. 28.º, n.º 4, al. d) | Parcial | [Política 33 §3.1](/sbd-toe/assets/policies/policy-contratacao-segura#31-critérios-de-avaliação); [Política 33 §3.2](/sbd-toe/assets/policies/policy-contratacao-segura#32-resultado-da-due-diligence); `GOV-007` | Critérios de devida diligência do RTS 2024/1773 (capacidade e continuidade do prestador, localização, idoneidade); critérios do Manual só para L2/L3 e para fornecedores com acesso técnico. |
| DORA-28-5 | art. 28.º, n.º 5 | Parcial | [Política 33 §3.1](/sbd-toe/assets/policies/policy-contratacao-segura#31-critérios-de-avaliação); `GOV-007` | Verificação prévia das «normas mais atualizadas e rigorosas» para FCI; certificações só obrigatórias em L3 para dados regulados. |
| DORA-28-6 | art. 28.º, n.º 6, 1.º parágrafo | Parcial | [Política 33 §6.2](/sbd-toe/assets/policies/policy-contratacao-segura#62-reavaliação-periódica); [Política 33 §4.2](/sbd-toe/assets/policies/policy-contratacao-segura#42-cláusulas-adicionais-por-nível-de-risco) | Programa de auditorias/inspeções a prestadores com frequência baseada no risco (direito de auditoria só L3). |
| DORA-28-8-p4 | art. 28.º, n.º 8, 4.º parágrafo | Parcial | [Política 33 §7.1](/sbd-toe/assets/policies/policy-contratacao-segura#71-checklist-de-offboarding) | Planos de transição e migração segura e integral de dados para outro prestador ou internamente. |
| DORA-RTS1773-3-2 | art. 3.º, n.º 2 | Lacuna | [🔁 Mapeamento prático entre DRP/BIA e risco de segurança](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/adopcao-drp-bia#-mapeamento-prático-entre-drpbia-e-risco-de-segurança) | Metodologia para determinar que serviços TIC (e ativos) apoiam funções críticas ou importantes e quando é revista; o Manual não tem a noção de FCI. |
| DORA-RTS1774-2-1-a | art. 2.º, n.º 1, al. a) | Parcial | `ARC-006`; `ARC-011` | Política de segurança de redes da entidade. |
| DORA-RTS1774-2-1-b | art. 2.º, n.º 1, al. b) | Parcial | `ACC-003`; `ACC-006`; `OPS-009` | Deteção de intrusões ao nível de rede. |
| DORA-RTS1774-2-1-d | art. 2.º, n.º 1, al. d) | Parcial | `INT-009`; `INT-010`; `INT-012` | Garantia de transmissão rápida sem atrasos indevidos (desempenho). |
| DORA-RTS1774-3-c-p2 | art. 3.º, segundo parágrafo, als. a) a c) | Parcial | `GOV-010`; `OPS-010` | Verificação sistemática de se a tolerância foi atingida após tratamento. |
| DORA-RTS1774-5-1 | art. 5.º, n.º 1 | Parcial | `CLA-008`; [Política 11 §7](/sbd-toe/assets/policies/policy-sbom#7-inventário-em-produção) | Procedimento de gestão de ativos TIC (não só aplicações e componentes). |
| DORA-RTS1774-6-2-b | art. 6.º, n.º 2, al. b) e segundo parágrafo | Lacuna | — | Regras para dados em utilização ou ambiente separado equivalente. |
| DORA-RTS1774-8-1 | art. 8.º, n.º 1 | Parcial | `OPS-001`; [Política 31 §3](/sbd-toe/assets/policies/policy-gestao-alertas#3-classificação-de-alertas); [Política 27 §7](/sbd-toe/assets/policies/policy-rollback#7-teste-periódico-de-rollback) | Documentação operacional de operação, controlo e restauração de ativos TIC. |
| DORA-RTS1774-8-2-a | art. 8.º, n.º 2, al. a) | Parcial | `IAC-003`; `CNT-003`; `CFG-001`; [🛠️ Abordagem proposta](/sbd-toe/sbd-manual/governanca-contratacao/addon/governanca-legada#️-abordagem-proposta) | Desinstalação segura e gestão dos ativos de informação tratados. |
| DORA-RTS1774-8-2-b-vii | art. 8.º, n.º 2, al. b), subal. vii) e terceiro parágrafo | Parcial | [Política 36 §4.2](/sbd-toe/assets/policies/policy-pentesting#42-regras-de-engajamento) | Regras para desenvolvimento/testes em produção: identificação, fundamentação, limitação temporal e aprovação. |
| DORA-RTS1774-8-2-c | art. 8.º, n.º 2, al. c) | Parcial | [Política 31 §5](/sbd-toe/assets/policies/policy-gestao-alertas#5-escalonamento-automático); [Política 27 §7](/sbd-toe/assets/policies/policy-rollback#7-teste-periódico-de-rollback); [Política 32 §4.5](/sbd-toe/assets/policies/policy-irp#45-recuperação) | Contactos de suporte externos e procedimentos de reinício/retoma de sistemas. |
| DORA-RTS1774-9-1 | art. 9.º, n.º 1 | Parcial | `OPS-015` | Gestão de capacidade e desempenho (requisitos de capacidade, otimização, prevenção de escassez). |
| DORA-RTS1774-10-2-b | art. 10.º, n.º 2, al. b) e segundo parágrafo | Parcial | [Política 10 §9](/sbd-toe/assets/policies/policy-dependencias#9-auditoria-periódica); [Cap. 05 US-09](/sbd-toe/sbd-manual/dependencias-sbom-sca/aplicacao-lifecycle#us-09---auditoria-periódica-de-bibliotecas-copiadas-manualmente); [Política 23 §4](/sbd-toe/assets/policies/policy-containers-seguros#4-scanning-de-imagens); [Política 11 §7](/sbd-toe/assets/policies/policy-sbom#7-inventário-em-produção) | Análise automatizada de vulnerabilidades pelo menos semanal em todos os ativos que apoiam FCI (incl. infraestrutura, não só dependências/imagens). |
| DORA-RTS1774-10-2-c | art. 10.º, n.º 2, al. c) e terceiro parágrafo | Parcial | [Política 33 §3.1](/sbd-toe/assets/policies/policy-contratacao-segura#31-critérios-de-avaliação); [Política 33 §6.1](/sbd-toe/assets/policies/policy-contratacao-segura#61-indicadores-de-conformidade-a-monitorizar); [💽 Contratos de licenciamento (software externo)](/sbd-toe/sbd-manual/governanca-contratacao/addon/clausulas-contratuais#-contratos-de-licenciamento-software-externo) | Pedido ao prestador de investigação, análise de causa e mitigação; estatísticas e tendências. |
| DORA-RTS1774-10-3 | art. 10.º, n.º 3 | Parcial | `DEP-007`; [Política 13 §2](/sbd-toe/assets/policies/policy-atualizacao-automatica#2-âmbito-e-obrigatoriedade); [Política 24 §6](/sbd-toe/assets/policies/policy-golden-base-images#6-sla-de-patching) | Correções de SO/firmware/hardware fora das imagens base. |
| DORA-RTS1774-11-2-b | art. 11.º, n.º 2, al. b) e segundo parágrafo | Parcial | `CNT-003`; `CNT-004`; `IAC-003`; `CFG-007`; [Política 24 §6](/sbd-toe/assets/policies/policy-golden-base-images#6-sla-de-patching) | Baselines de hardening para servidores/SO e verificação regular fora de containers/IaC. |
| DORA-RTS1774-11-2-c | art. 11.º, n.º 2, al. c) | Parcial | `IDE-001`; `CNT-001`; `DEP-005` | Controlo de software autorizado em todos os sistemas e terminais. |
| DORA-RTS1774-11-2-d | art. 11.º, n.º 2, al. d) | Parcial | `FIL-007` | Proteção anti-malware de servidores e terminais. |
| DORA-RTS1774-11-2-g | art. 11.º, n.º 2, al. g) | Parcial | `PRI-002` | Apagamento seguro de dados não pessoais e em locais externos. |
| DORA-RTS1774-11-2-i | art. 11.º, n.º 2, al. i) | Parcial | [Política 30 §3.2](/sbd-toe/assets/policies/policy-monitorizacao-seguranca#32-exfiltração-e-acesso-a-dados); `ENC-005` | Medidas de prevenção de perda e fuga de dados (DLP) em terminais. |
| DORA-RTS1774-11-2-k | art. 11.º, n.º 2, al. k) e terceiro parágrafo | Parcial | `GOV-006`; `IAC-003` | Repartição de responsabilidades de segurança e parâmetros do vendedor para ativos operados por terceiros (cloud). |
| DORA-RTS1774-12-2-c | art. 12.º, n.º 2, al. c) | Parcial | [Política 29 §4](/sbd-toe/assets/policies/policy-logging-estruturado#4-eventos-de-segurança-obrigatórios); `DPL-004`; `CIC-005` | Eventos de acesso físico, gestão de capacidade e tráfego/desempenho de rede. |
| DORA-RTS1774-12-2-d | art. 12.º, n.º 2, al. d) | Parcial | `LOG-003`; [Política 29 §8](/sbd-toe/assets/policies/policy-logging-estruturado#8-integridade-e-imutabilidade) | Proteção em trânsito e em utilização. |
| DORA-RTS1774-12-2-e | art. 12.º, n.º 2, al. e) | Parcial | `LOG-008`; `OPS-004` | Deteção de falhas de registo em L1. |
| DORA-RTS1774-12-2-f | art. 12.º, n.º 2, al. f) | Parcial | [🛠️ Requisitos funcionais da integração](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/integracao-siem#️-requisitos-funcionais-da-integração) | Sincronização documentada de todos os sistemas TIC com referência temporal fiável (o Manual só normaliza timestamps na integração SIEM). |
| DORA-RTS1774-13 | art. 13.º, prim. parágrafo | Parcial | `ARC-006`; [Política 09 §6.1](/sbd-toe/assets/policies/policy-arquitetura-segura#61-inventário-de-trust-boundaries) | Política de gestão da segurança das redes com os elementos a) a m). |
| DORA-RTS1774-13-b | art. 13.º, al. b) | Parcial | `ARC-008`; `THR-002` | Documentação de todas as ligações de rede (não só fluxos entre zonas de confiança da aplicação). |
| DORA-RTS1774-13-c | art. 13.º, al. c) | Lacuna | — | Rede/plano de administração separado e dedicado. |
| DORA-RTS1774-13-f | art. 13.º, al. f) | Parcial | `ARC-001`; `ARC-006`; [Política 09 §6.1](/sbd-toe/assets/policies/policy-arquitetura-segura#61-inventário-de-trust-boundaries) | Conceção das redes da entidade. |
| DORA-RTS1774-13-i | art. 13.º, al. i) | Parcial | `ARC-010`; `ARC-003` | Análise anual da arquitetura e conceção de segurança da rede (o Manual revê diagramas aplicacionais anualmente). |
| DORA-RTS1774-13-l | art. 13.º, al. l) | Parcial | `SES-001`; `AUT-005` | Encerramento de sessões remotas de administração/sistemas após inatividade (o Manual cobre sessões aplicacionais). |
| DORA-RTS1774-14-1-b | art. 14.º, n.º 1, al. b) | Parcial | [Política 30 §3.2](/sbd-toe/assets/policies/policy-monitorizacao-seguranca#32-exfiltração-e-acesso-a-dados); `INT-002`; `INT-006` | Prevenção de fugas de dados (DLP) na transferência com partes externas. |
| DORA-RTS1774-16-3 | art. 16.º, n.º 3 | Parcial | [Política 19 §2.1](/sbd-toe/assets/policies/policy-estrategia-testes#21-matriz-de-obrigatoriedade-por-nível); `DEV-003`; `TST-005`; [4️⃣ Coding Guidelines Básicas e Validação Automática (Cap. 06)](/sbd-toe/sbd-manual/fundamentos/baseline#4️⃣-coding-guidelines-básicas-e-validação-automática-cap-06) | DAST obrigatório em todos os níveis (incl. sistemas expostos à Internet). |
| DORA-RTS1774-16-6 | art. 16.º, n.º 6 | Parcial | [4.1 Prescrições obrigatórias](/sbd-toe/sbd-manual/testes-seguranca/addon/evidencia-reprodutibilidade#41-prescrições-obrigatórias); [Cap. 10 US-19](/sbd-toe/sbd-manual/testes-seguranca/aplicacao-lifecycle#us-19---proteção-dos-ativos-do-processo-de-teste) | Limitação temporal e comunicação à função de gestão do risco TIC. |
| DORA-RTS1774-16-9 | art. 16.º, n.º 9 | Parcial | [🎯 Âmbito e enquadramento](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#-âmbito-e-enquadramento) | Aplicação do SDLC a end-user computing/shadow IT fora da função TIC. |
| DORA-RTS1774-17-1 | art. 17.º, n.º 1, prim. parágrafo | Parcial | `DPL-001`; `DPL-004`; [Política 26 §7](/sbd-toe/assets/policies/policy-aprovacao-release#7-releases-de-emergência); [Política 22 §5](/sbd-toe/assets/policies/policy-aprovacao-plan-iac#5-separação-de-funções-sod) | Alterações de hardware/firmware. |
| DORA-RTS1774-17-1-d | art. 17.º, n.º 1, al. d) | Parcial | `DPL-004`; `IAC-007` | Documentação do objetivo e resultados esperados de cada alteração. |
| DORA-RTS1774-19-b-iii | art. 19.º, al. b), subal. iii) | Parcial | [Política 33 §7.1](/sbd-toe/assets/policies/policy-contratacao-segura#71-checklist-de-offboarding) | Devolução de ativos por colaboradores internos (o Manual cobre contractors/fornecedores). |
| DORA-RTS1774-20-2-a | art. 20.º, n.º 2, al. a) e segundo parágrafo | Parcial | `ACC-004`; [Cap. 07 US-20](/sbd-toe/sbd-manual/cicd-seguro/aplicacao-lifecycle#us-20) | Identidade única por membro do pessoal com registo conservado após fim da relação. |
| DORA-RTS1774-22 | art. 22.º, prim. parágrafo | Parcial | [Política 32 §2](/sbd-toe/assets/policies/policy-irp#2-âmbito-e-obrigatoriedade); [Política 32 §3](/sbd-toe/assets/policies/policy-irp#3-critérios-de-activação-do-irp); [Política 32 §5](/sbd-toe/assets/policies/policy-irp#5-playbooks-de-resposta) | Obrigatório em L1 pelo piso CTX-DORA-P01, que assenta no art. 17.º do DORA (ver DORA-17-1); o artigo do RTS não está na base do piso. |
| DORA-RTS1774-22-b | art. 22.º, al. b) | Parcial | [Política 31 §7](/sbd-toe/assets/policies/policy-gestao-alertas#7-alertas-p1-em-horas-não-laborais-on-call) | Lista de contactos externos (autoridades, CSIRT, prestadores). |
| DORA-RTS1774-23-2-a | art. 23.º, n.º 2, al. a) | Parcial | `OPS-004`; [Cap. 12 US-16](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle#us-16---cobertura-attck-e-priorização-epsskev); [Política 33 §4.1](/sbd-toe/assets/policies/policy-contratacao-segura#41-cláusulas-universais-todos-os-níveis) | Reportes de utilizadores como fonte obrigatória. |
| DORA-RTS1774-23-2-b | art. 23.º, n.º 2, al. b) e segundo parágrafo | Parcial | `LOG-008`; `OPS-004`; `OPS-005` | Alertas automáticos sobre integridade/completude da recolha para ativos de FCI classificados L1. |
| DORA-RTS1774-23-3 | art. 23.º, n.º 3 | Parcial | `LOG-003`; [Política 29 §8](/sbd-toe/assets/policies/policy-logging-estruturado#8-integridade-e-imutabilidade) | Proteção obrigatória em L1 (ver 12-2-d). |
| DORA-RTS1774-23-4 | art. 23.º, n.º 4 | Parcial | [Política 32 §4.1](/sbd-toe/assets/policies/policy-irp#41-triagem-t0----15-minutos-de-detecção); `LOG-002` | Registo distinto de data/hora de ocorrência e de deteção. |
| DORA-RTS1774-25-1 | art. 25.º, n.º 1 | Parcial | [Política 32 §8](/sbd-toe/assets/policies/policy-irp#8-testes-periódicos-do-irp); [🔁 Mapeamento prático entre DRP/BIA e risco de segurança](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/adopcao-drp-bia#-mapeamento-prático-entre-drpbia-e-risco-de-segurança) | Testes de planos de continuidade baseados na BIA. |
| DORA-RTS1774-25-2 | art. 25.º, n.º 2 | Parcial | [Política 32 §8](/sbd-toe/assets/policies/policy-irp#8-testes-periódicos-do-irp); [Política 27 §7](/sbd-toe/assets/policies/policy-rollback#7-teste-periódico-de-rollback) | Cenários de falha de terceiros e de failover para redundância/cópias. |
| DORA-RTS1774-25-5 | art. 25.º, n.º 5 | Parcial | [Política 32 §8](/sbd-toe/assets/policies/policy-irp#8-testes-periódicos-do-irp) | Comunicação das deficiências ao órgão de administração. |
| DORA-RTS1774-26-1 | art. 26.º, n.º 1 | Parcial | [Política 32 §5](/sbd-toe/assets/policies/policy-irp#5-playbooks-de-resposta); [🔁 Mapeamento prático entre DRP/BIA e risco de segurança](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/adopcao-drp-bia#-mapeamento-prático-entre-drpbia-e-risco-de-segurança) | Planos de recuperação baseados na BIA com critérios de ativação/desativação e objetivos de recuperação. |
| DORA-RTS1774-26-2 | art. 26.º, n.º 2 | Parcial | [Política 32 §5](/sbd-toe/assets/policies/policy-irp#5-playbooks-de-resposta) | Cenários não cibernéticos (instalações, pessoal, clima, pandemia, energia, instabilidade política). |
| DORA-RTS1774-26-4 | art. 26.º, n.º 4 | Parcial | [Política 33 §10.5](/sbd-toe/assets/policies/policy-contratacao-segura#105-sla-de-disponibilidade-e-fallback) | Medidas de continuidade face a falhas de prestadores de FCI em geral (o Manual só prevê fallback para fornecedores de IA). |
| DORA-RTS1774-29-2 | art. 29.º, n.º 2 | Parcial | `CLA-003`; `GOV-006` | Medidas mitigadoras aplicadas por prestadores TIC. |
| DORA-RTS1774-30-1 | art. 30.º, n.º 1 | Parcial | `CLA-001`; `CLA-008` | Identificação de funções críticas ou importantes e interdependências. |
| DORA-RTS1774-33 | art. 33.º, prim. parágrafo | Parcial | `ACC-001`; `ACC-010` | Controlo de acesso físico. |
| DORA-RTS1774-34-b | art. 34.º, al. b) | Parcial | [Política 24 §6](/sbd-toe/assets/policies/policy-golden-base-images#6-sla-de-patching) | Verificação do suporte de terceiros para todos os ativos (EOL fora de imagens base/dependências). |
| DORA-RTS1774-34-c | art. 34.º, al. c) | Parcial | `OPS-015` | Planeamento de capacidade. |
| DORA-RTS1774-34-e | art. 34.º, al. e) | Parcial | [🛠️ Abordagem proposta](/sbd-toe/sbd-manual/governanca-contratacao/addon/governanca-legada#️-abordagem-proposta); [Política 24 §6](/sbd-toe/assets/policies/policy-golden-base-images#6-sla-de-patching) | Gestão de riscos de hardware obsoleto/sem suporte. |
| DORA-RTS1774-34-f | art. 34.º, al. f) e segundo parágrafo | Parcial | [Política 29 §4](/sbd-toe/assets/policies/policy-logging-estruturado#4-eventos-de-segurança-obrigatórios); `DPL-004` | Eventos de acesso físico e de tráfego de rede. |
| DORA-RTS1774-34-i | art. 34.º, al. i) | Parcial | [Política 10 §8](/sbd-toe/assets/policies/policy-dependencias#8-alertas-de-vulnerabilidades-em-produção); `ENC-006`; `FIL-007` | Fugas de informação e vulnerabilidades de hardware. |
| DORA-RTS1774-35 | art. 35.º, prim. parágrafo | Parcial | `ACC-003`; `ACC-006`; `ENC-001` | Salvaguardas contra intrusão ao nível de rede/terminais. |
| DORA-RTS1774-35-a | art. 35.º, al. a) | Parcial | `ENC-001`; `ENC-002` | Dados em utilização. |
| DORA-RTS1774-35-b | art. 35.º, al. b) | Parcial | `IDE-001`; `CNT-001` | Suportes de armazenamento e terminais. |
| DORA-RTS1774-35-e | art. 35.º, al. e) | Parcial | `PRI-002` | Apagamento seguro de dados não pessoais. |
| DORA-RTS1774-38-2 | art. 38.º, n.º 2 | Parcial | `DPL-001`; `DPL-004`; [Política 26 §7](/sbd-toe/assets/policies/policy-aprovacao-release#7-releases-de-emergência) | Alterações de hardware/firmware. |
| DORA-RTS1774-39-1 | art. 39.º, n.º 1 | Parcial | [Política 32 §5](/sbd-toe/assets/policies/policy-irp#5-playbooks-de-resposta) | Planos de continuidade (o Manual tem playbooks de incidente, incl. ransomware). |
| DORA-RTS1774-40-1 | art. 40.º, n.os 1 e 2 | Parcial | [Política 32 §8](/sbd-toe/assets/policies/policy-irp#8-testes-periódicos-do-irp); [Política 27 §7](/sbd-toe/assets/policies/policy-rollback#7-teste-periódico-de-rollback); `OPS-016` | Testes dos planos de continuidade da entidade com cenários (fora do âmbito do Manual); o teste de salvaguarda e restauração está prescrito (OPS-016). |
| DORA-RTS1774-40-3 | art. 40.º, n.º 3 | Parcial | [Política 32 §8](/sbd-toe/assets/policies/policy-irp#8-testes-periódicos-do-irp) | Reporte de deficiências ao órgão de administração. |

### Fora de âmbito (230) {#fora-de-ambito}

Obrigações que o Manual declara fora de âmbito, com a razão.

| Obrigação | Referência | Razão |
|---|---|---|
| DORA-5-2-f | art. 5.º, n.º 2, al. f) | Dever do órgão de administração / estrutura de governo interno; o Manual não fixa órgãos nem alçadas societárias. Aprovação de planos de auditoria interna. |
| DORA-5-2-g | art. 5.º, n.º 2, al. g) | Dever do órgão de administração / estrutura de governo interno; o Manual não fixa órgãos nem alçadas societárias. Orçamento. |
| DORA-5-3 | art. 5.º, n.º 3 | Dever do órgão de administração / estrutura de governo interno; o Manual não fixa órgãos nem alçadas societárias. Cargo de monitorização dos acordos com terceiros TIC. |
| DORA-5-4 | art. 5.º, n.º 4 | Dever do órgão de administração / estrutura de governo interno; o Manual não fixa órgãos nem alçadas societárias. A Política 37 abrange apenas colaboradores com funções técnicas. |
| DORA-6-3-p2 | art. 6.º, n.º 3, 2.º per. | Reporte/relação com a autoridade competente — plano jurídico-regulatório, não prescrição de engenharia de software. |
| DORA-6-4 | art. 6.º, n.º 4 | Dever do órgão de administração / estrutura de governo interno; o Manual não fixa órgãos nem alçadas societárias. Função de controlo independente e modelo de três linhas de defesa. |
| DORA-6-10 | art. 6.º, n.º 10 | Princípio de responsabilidade jurídica mantida na verificação subcontratada. |
| DORA-10-4 | art. 10.º, n.º 4 | Obrigação sectorial específica (CCP/CSD/plataformas de negociação/DRSP) — parâmetro operacional de mercado, fora de um manual transversal de engenharia de software. |
| DORA-11-1 | art. 11.º, n.º 1 | Gestão da continuidade do negócio/crise (BCM) de nível organizacional — o Manual trata resposta a incidentes cibernéticos e rollback, não BCM geral. |
| DORA-11-6-b | art. 11.º, n.º 6, al. b) | Gestão da continuidade do negócio/crise (BCM) de nível organizacional — o Manual trata resposta a incidentes cibernéticos e rollback, não BCM geral. Comunicação de crise. |
| DORA-11-7 | art. 11.º, n.º 7 | Gestão da continuidade do negócio/crise (BCM) de nível organizacional — o Manual trata resposta a incidentes cibernéticos e rollback, não BCM geral. Função de gestão de crises. |
| DORA-11-9 | art. 11.º, n.º 9 | Reporte/relação com a autoridade competente — plano jurídico-regulatório, não prescrição de engenharia de software. Obrigação exclusiva de CSD. |
| DORA-11-10 | art. 11.º, n.º 10 | Reporte/relação com a autoridade competente — plano jurídico-regulatório, não prescrição de engenharia de software. |
| DORA-12-3-p2 | art. 12.º, n.º 3, 2.º e 3.º parágrafos | Obrigação sectorial específica (CCP/CSD/plataformas de negociação/DRSP) — parâmetro operacional de mercado, fora de um manual transversal de engenharia de software. |
| DORA-12-5 | art. 12.º, n.º 5 | Obrigação sectorial específica (CCP/CSD/plataformas de negociação/DRSP) — parâmetro operacional de mercado, fora de um manual transversal de engenharia de software. |
| DORA-13-2-p2 | art. 13.º, n.º 2, 2.º parágrafo | Reporte/relação com a autoridade competente — plano jurídico-regulatório, não prescrição de engenharia de software. |
| DORA-14-1 | art. 14.º, n.º 1 | Gestão da continuidade do negócio/crise (BCM) de nível organizacional — o Manual trata resposta a incidentes cibernéticos e rollback, não BCM geral. Comunicação de crise e divulgação. |
| DORA-14-2 | art. 14.º, n.º 2 | Gestão da continuidade do negócio/crise (BCM) de nível organizacional — o Manual trata resposta a incidentes cibernéticos e rollback, não BCM geral. Políticas de comunicação interna/externa. |
| DORA-19-2 | art. 19.º, n.º 2 | Reporte/relação com a autoridade competente — plano jurídico-regulatório, não prescrição de engenharia de software. Notificação voluntária de ciberameaças. |
| DORA-19-3-p2 | art. 19.º, n.º 3, 2.º parágrafo | Reporte/relação com a autoridade competente — plano jurídico-regulatório, não prescrição de engenharia de software. |
| DORA-19-5 | art. 19.º, n.º 5 | Responsabilidade jurídica mantida na notificação subcontratada. |
| DORA-23 | art. 23.º | Aplicação a incidentes operacionais/de segurança de pagamento — âmbito jurídico sectorial. |
| DORA-26-3 | art. 26.º, n.º 3 | Processo TLPT regulado (Reg. Delegado (UE) 2025/1190) — o addon 14 do Cap. 10 declara-o expressamente fora do âmbito do Manual (compliance/GRC/supervisor). |
| DORA-26-4 | art. 26.º, n.º 4 | Processo TLPT regulado (Reg. Delegado (UE) 2025/1190) — o addon 14 do Cap. 10 declara-o expressamente fora do âmbito do Manual (compliance/GRC/supervisor). |
| DORA-26-6 | art. 26.º, n.º 6 | Processo TLPT regulado (Reg. Delegado (UE) 2025/1190) — o addon 14 do Cap. 10 declara-o expressamente fora do âmbito do Manual (compliance/GRC/supervisor). |
| DORA-26-7 | art. 26.º, n.º 7 | Processo TLPT regulado (Reg. Delegado (UE) 2025/1190) — o addon 14 do Cap. 10 declara-o expressamente fora do âmbito do Manual (compliance/GRC/supervisor). |
| DORA-26-8 | art. 26.º, n.º 8, 1.º e 2.º parágrafos | Processo TLPT regulado (Reg. Delegado (UE) 2025/1190) — o addon 14 do Cap. 10 declara-o expressamente fora do âmbito do Manual (compliance/GRC/supervisor). |
| DORA-27-1 | art. 27.º, n.º 1, als. a) a e) | Processo TLPT regulado (Reg. Delegado (UE) 2025/1190) — o addon 14 do Cap. 10 declara-o expressamente fora do âmbito do Manual (compliance/GRC/supervisor). |
| DORA-27-2 | art. 27.º, n.º 2 | Processo TLPT regulado (Reg. Delegado (UE) 2025/1190) — o addon 14 do Cap. 10 declara-o expressamente fora do âmbito do Manual (compliance/GRC/supervisor). |
| DORA-27-3 | art. 27.º, n.º 3 | Processo TLPT regulado (Reg. Delegado (UE) 2025/1190) — o addon 14 do Cap. 10 declara-o expressamente fora do âmbito do Manual (compliance/GRC/supervisor). |
| DORA-28-1-a | art. 28.º, n.º 1, al. a) | Princípio de responsabilidade jurídica mantida pela entidade financeira. |
| DORA-28-2-orgao | art. 28.º, n.º 2, última frase | Dever do órgão de administração / estrutura de governo interno; o Manual não fixa órgãos nem alçadas societárias. |
| DORA-28-3-p2 | art. 28.º, n.º 3, 2.º parágrafo | Registo de informações regulatório (art. 28.º, n.º 3; ITS 2024/2956) — modelos e reporte à autoridade; fora de âmbito: plano regulatório da entidade, não prescrição de engenharia de software. |
| DORA-28-3-p3 | art. 28.º, n.º 3, 3.º parágrafo | Registo de informações regulatório (art. 28.º, n.º 3; ITS 2024/2956) — modelos e reporte à autoridade; fora de âmbito: plano regulatório da entidade, não prescrição de engenharia de software. |
| DORA-28-3-p4 | art. 28.º, n.º 3, 4.º parágrafo | Registo de informações regulatório (art. 28.º, n.º 3; ITS 2024/2956) — modelos e reporte à autoridade; fora de âmbito: plano regulatório da entidade, não prescrição de engenharia de software. |
| DORA-28-3-p5 | art. 28.º, n.º 3, 5.º parágrafo | Reporte/relação com a autoridade competente — plano jurídico-regulatório, não prescrição de engenharia de software. |
| DORA-28-4-b | art. 28.º, n.º 4, al. b) | Verificação de condições de supervisão da subcontratação — plano jurídico-regulatório. |
| DORA-28-4-e | art. 28.º, n.º 4, al. e) | Conflitos de interesses no acordo — plano jurídico/compliance. |
| DORA-28-6-p2 | art. 28.º, n.º 6, 2.º parágrafo | Competência de auditores em contratos complexos — plano de auditoria/compliance. |
| DORA-28-8-p2 | art. 28.º, n.º 8, 2.º parágrafo | Gestão da continuidade do negócio/crise (BCM) de nível organizacional — o Manual trata resposta a incidentes cibernéticos e rollback, não BCM geral. Planeamento de saída de prestadores. |
| DORA-28-8-p3 | art. 28.º, n.º 8, 3.º parágrafo | Gestão da continuidade do negócio/crise (BCM) de nível organizacional — o Manual trata resposta a incidentes cibernéticos e rollback, não BCM geral. Planos de saída documentados e testados. |
| DORA-28-8-p5 | art. 28.º, n.º 8, 5.º parágrafo | Gestão da continuidade do negócio/crise (BCM) de nível organizacional — o Manual trata resposta a incidentes cibernéticos e rollback, não BCM geral. |
| DORA-29-1 | art. 29.º, n.º 1, 1.º parágrafo, al. a) e b) | Risco de concentração de terceiros TIC — análise regulatória; fora de âmbito: plano regulatório da entidade, não prescrição de engenharia de software. |
| DORA-29-1-p2 | art. 29.º, n.º 1, 2.º parágrafo | Idem 29-1. |
| DORA-29-2 | art. 29.º, n.º 2, 1.º parágrafo | Idem 29-1 (subcontratação em país terceiro). |
| DORA-29-2-p2 | art. 29.º, n.º 2, 2.º parágrafo | Conteúdo contratual/jurídico específico do DORA sem correspondente prescritivo no Manual. |
| DORA-29-2-p3 | art. 29.º, n.º 2, 3.º parágrafo | Conteúdo contratual/jurídico específico do DORA sem correspondente prescritivo no Manual. |
| DORA-29-2-p4 | art. 29.º, n.º 2, 4.º parágrafo | Idem 29-1. |
| DORA-30-2-g | art. 30.º, n.º 2, al. g) | Conteúdo contratual/jurídico específico do DORA sem correspondente prescritivo no Manual. Cooperação com as autoridades. |
| DORA-30-3-a | art. 30.º, n.º 3, al. a) | Conteúdo contratual/jurídico específico do DORA sem correspondente prescritivo no Manual. SLA completos com metas quantitativas/qualitativas. |
| DORA-30-3-d | art. 30.º, n.º 3, al. d) | Conteúdo contratual/jurídico específico do DORA sem correspondente prescritivo no Manual. Participação do prestador em TLPT. |
| DORA-30-3-f | art. 30.º, n.º 3, al. f) | Conteúdo contratual/jurídico específico do DORA sem correspondente prescritivo no Manual. Estratégias de saída com período de transição. |
| DORA-31-4 | art. 31.º, n.º 4 | Quadro de superintendência de terceiros prestadores críticos (arts. 31.º–44.º) — relação prestador/autoridade, fora de um manual de engenharia. |
| DORA-31-5-p2 | art. 31.º, n.º 5, 2.º parágrafo | Quadro de superintendência de terceiros prestadores críticos (arts. 31.º–44.º) — relação prestador/autoridade, fora de um manual de engenharia. |
| DORA-31-12 | art. 31.º, n.º 12 | Quadro de superintendência de terceiros prestadores críticos (arts. 31.º–44.º) — relação prestador/autoridade, fora de um manual de engenharia. |
| DORA-31-13 | art. 31.º, n.º 13 | Quadro de superintendência de terceiros prestadores críticos (arts. 31.º–44.º) — relação prestador/autoridade, fora de um manual de engenharia. |
| DORA-35-1-d-iv | art. 35.º, n.º 1, al. d), subal. iv), último parágrafo | Quadro de superintendência de terceiros prestadores críticos (arts. 31.º–44.º) — relação prestador/autoridade, fora de um manual de engenharia. |
| DORA-35-5 | art. 35.º, n.º 5 | Quadro de superintendência de terceiros prestadores críticos (arts. 31.º–44.º) — relação prestador/autoridade, fora de um manual de engenharia. |
| DORA-37-4 | art. 37.º, n.º 4 | Quadro de superintendência de terceiros prestadores críticos (arts. 31.º–44.º) — relação prestador/autoridade, fora de um manual de engenharia. |
| DORA-38-4 | art. 38.º, n.º 4 | Quadro de superintendência de terceiros prestadores críticos (arts. 31.º–44.º) — relação prestador/autoridade, fora de um manual de engenharia. |
| DORA-39-6 | art. 39.º, n.º 6 | Quadro de superintendência de terceiros prestadores críticos (arts. 31.º–44.º) — relação prestador/autoridade, fora de um manual de engenharia. |
| DORA-42-1 | art. 42.º, n.º 1 | Quadro de superintendência de terceiros prestadores críticos (arts. 31.º–44.º) — relação prestador/autoridade, fora de um manual de engenharia. |
| DORA-42-3-p2 | art. 42.º, n.º 3, 2.º parágrafo | Quadro de superintendência de terceiros prestadores críticos (arts. 31.º–44.º) — relação prestador/autoridade, fora de um manual de engenharia. |
| DORA-42-9-p2 | art. 42.º, n.º 9, 2.º parágrafo | Quadro de superintendência de terceiros prestadores críticos (arts. 31.º–44.º) — relação prestador/autoridade, fora de um manual de engenharia. |
| DORA-45-1 | art. 45.º, n.º 1, al. a) a c) | Acordos institucionais de partilha de informação sobre ciberameaças (faculdade condicionada); fora de âmbito: plano regulatório da entidade, não prescrição de engenharia de software. |
| DORA-45-2 | art. 45.º, n.º 2 | Conteúdo contratual/jurídico específico do DORA sem correspondente prescritivo no Manual. |
| DORA-45-3 | art. 45.º, n.º 3 | Reporte/relação com a autoridade competente — plano jurídico-regulatório, não prescrição de engenharia de software. |
| DORA-59 | art. 59.º (altera Reg. (CE) 1060/2009, anexo I, secção A, ponto 4) | Alteração a atos sectoriais (agências de notação, CCP, APA/CTP/ARM, índices) — remissão jurídica. |
| DORA-60 | art. 60.º (altera Reg. (UE) 648/2012, arts. 26.º, 34.º, 56.º, 79.º...) | Alteração a atos sectoriais (agências de notação, CCP, APA/CTP/ARM, índices) — remissão jurídica. |
| DORA-61 | art. 61.º (altera Reg. (UE) 909/2014, art. 45.º) | Obrigação sectorial específica (CCP/CSD/plataformas de negociação/DRSP) — parâmetro operacional de mercado, fora de um manual transversal de engenharia de software. Alteração ao regime das CSD (recuperação de transações). |
| DORA-62 | art. 62.º (altera Reg. (UE) 600/2014, arts. 27.º-G, 27.º-H, 27.º-I) | Alteração a atos sectoriais (agências de notação, CCP, APA/CTP/ARM, índices) — remissão jurídica. |
| DORA-63 | art. 63.º (adita art. 6.º, n.º 6, ao Reg. (UE) 2016/1011) | Alteração a atos sectoriais (agências de notação, CCP, APA/CTP/ARM, índices) — remissão jurídica. |
| DORA-RTS1773-2 | art. 2.º | Aplicação coerente no grupo — organização societária. |
| DORA-RTS1773-3-1 | art. 3.º, n.º 1 | Dever do órgão de administração / estrutura de governo interno; o Manual não fixa órgãos nem alçadas societárias. |
| DORA-RTS1773-3-4 | art. 3.º, n.º 4 | Avaliação da suficiência de recursos do prestador — gestão contratual. |
| DORA-RTS1773-3-5 | art. 3.º, n.º 5 | Dever do órgão de administração / estrutura de governo interno; o Manual não fixa órgãos nem alçadas societárias. |
| DORA-RTS1773-3-7 | art. 3.º, n.º 7 | Dever do órgão de administração / estrutura de governo interno; o Manual não fixa órgãos nem alçadas societárias. Revisão independente/plano de auditoria. |
| DORA-RTS1773-3-8 | art. 3.º, n.º 8, al. a) a d) | Conteúdo contratual/jurídico específico do DORA sem correspondente prescritivo no Manual. |
| DORA-RTS1773-5-1 | art. 5.º, n.º 1 | Definição de necessidades operacionais antes de contratar — procurement. |
| DORA-RTS1773-6-2 | art. 6.º, n.º 2 | Nível de garantia e continuidade do prestador — avaliação de procurement. |
| DORA-RTS1773-7-1 | art. 7.º, n.º 1 | Conflitos de interesses — compliance. |
| DORA-RTS1773-7-2 | art. 7.º, n.º 2 | Serviços intragrupo — organização societária. |
| DORA-RTS1773-8-4 | art. 8.º, n.º 4 | Conteúdo contratual/jurídico específico do DORA sem correspondente prescritivo no Manual. |
| DORA-RTS1773-10 | art. 10.º | Gestão da continuidade do negócio/crise (BCM) de nível organizacional — o Manual trata resposta a incidentes cibernéticos e rollback, não BCM geral. Plano de saída por acordo. |
| DORA-ITS2956-2 | art. 2.º | Registo de informações regulatório (art. 28.º, n.º 3; ITS 2024/2956) — modelos e reporte à autoridade; fora de âmbito: plano regulatório da entidade, não prescrição de engenharia de software. |
| DORA-ITS2956-3-1 | art. 3.º, n.º 1 | Registo de informações regulatório (art. 28.º, n.º 3; ITS 2024/2956) — modelos e reporte à autoridade; fora de âmbito: plano regulatório da entidade, não prescrição de engenharia de software. |
| DORA-ITS2956-3-2 | art. 3.º, n.º 2, al. a) e b) | Registo de informações regulatório (art. 28.º, n.º 3; ITS 2024/2956) — modelos e reporte à autoridade; fora de âmbito: plano regulatório da entidade, não prescrição de engenharia de software. |
| DORA-ITS2956-3-3 | art. 3.º, n.º 3 | Registo de informações regulatório (art. 28.º, n.º 3; ITS 2024/2956) — modelos e reporte à autoridade; fora de âmbito: plano regulatório da entidade, não prescrição de engenharia de software. |
| DORA-ITS2956-3-4 | art. 3.º, n.º 4, al. a) a f) | Registo de informações regulatório (art. 28.º, n.º 3; ITS 2024/2956) — modelos e reporte à autoridade; fora de âmbito: plano regulatório da entidade, não prescrição de engenharia de software. |
| DORA-ITS2956-3-5 | art. 3.º, n.º 5 | Registo de informações regulatório (art. 28.º, n.º 3; ITS 2024/2956) — modelos e reporte à autoridade; fora de âmbito: plano regulatório da entidade, não prescrição de engenharia de software. |
| DORA-ITS2956-3-6 | art. 3.º, n.º 6 | Registo de informações regulatório (art. 28.º, n.º 3; ITS 2024/2956) — modelos e reporte à autoridade; fora de âmbito: plano regulatório da entidade, não prescrição de engenharia de software. |
| DORA-ITS2956-4 | art. 4.º, n.os 2 e 3 | Registo de informações regulatório (art. 28.º, n.º 3; ITS 2024/2956) — modelos e reporte à autoridade; fora de âmbito: plano regulatório da entidade, não prescrição de engenharia de software. |
| DORA-ITS2956-5-1 | art. 5.º, n.º 1, al. a) a o); anexo I | Registo de informações regulatório (art. 28.º, n.º 3; ITS 2024/2956) — modelos e reporte à autoridade; fora de âmbito: plano regulatório da entidade, não prescrição de engenharia de software. |
| DORA-ITS2956-6 | art. 6.º, n.os 1 e 2 | Registo de informações regulatório (art. 28.º, n.º 3; ITS 2024/2956) — modelos e reporte à autoridade; fora de âmbito: plano regulatório da entidade, não prescrição de engenharia de software. |
| DORA-ITS2956-AnexoI | anexo I, parte 1 | Registo de informações regulatório (art. 28.º, n.º 3; ITS 2024/2956) — modelos e reporte à autoridade; fora de âmbito: plano regulatório da entidade, não prescrição de engenharia de software. |
| DORA-RTS532-1 | art. 1.º, al. a) a l) | Proporcionalidade na gestão da subcontratação — plano contratual. |
| DORA-RTS532-2 | art. 2.º | Coerência no grupo — organização societária. |
| DORA-RTS532-3-1-f | art. 3.º, n.º 1, al. f) | Avaliação de riscos de cadeias de subcontratação (capacidade, falha, localização, concentração, auditoria) — análise contratual/regulatória. |
| DORA-RTS532-3-1-g | art. 3.º, n.º 1, al. g) | Avaliação de riscos de cadeias de subcontratação (capacidade, falha, localização, concentração, auditoria) — análise contratual/regulatória. |
| DORA-RTS532-3-1-h | art. 3.º, n.º 1, al. h) | Avaliação de riscos de cadeias de subcontratação (capacidade, falha, localização, concentração, auditoria) — análise contratual/regulatória. |
| DORA-RTS532-3-1-i | art. 3.º, n.º 1, al. i) | Avaliação de riscos de cadeias de subcontratação (capacidade, falha, localização, concentração, auditoria) — análise contratual/regulatória. |
| DORA-RTS532-3-1-j | art. 3.º, n.º 1, al. j) | Avaliação de riscos de cadeias de subcontratação (capacidade, falha, localização, concentração, auditoria) — análise contratual/regulatória. |
| DORA-RTS532-4-1-a | art. 4.º, n.º 1, al. a) | Conteúdo contratual/jurídico específico do DORA sem correspondente prescritivo no Manual. Cláusulas sobre subcontratantes. |
| DORA-RTS532-4-1-b | art. 4.º, n.º 1, al. b) | Conteúdo contratual/jurídico específico do DORA sem correspondente prescritivo no Manual. Cláusulas sobre subcontratantes. |
| DORA-RTS532-4-1-c | art. 4.º, n.º 1, al. c) | Conteúdo contratual/jurídico específico do DORA sem correspondente prescritivo no Manual. Cláusulas sobre subcontratantes. |
| DORA-RTS532-4-1-d | art. 4.º, n.º 1, al. d) | Conteúdo contratual/jurídico específico do DORA sem correspondente prescritivo no Manual. Cláusulas sobre subcontratantes. |
| DORA-RTS532-4-1-e | art. 4.º, n.º 1, al. e) | Conteúdo contratual/jurídico específico do DORA sem correspondente prescritivo no Manual. Cláusulas sobre subcontratantes. |
| DORA-RTS532-4-1-f | art. 4.º, n.º 1, al. f) | Conteúdo contratual/jurídico específico do DORA sem correspondente prescritivo no Manual. Cláusulas sobre subcontratantes. |
| DORA-RTS532-4-1-g | art. 4.º, n.º 1, al. g) | Conteúdo contratual/jurídico específico do DORA sem correspondente prescritivo no Manual. Cláusulas sobre subcontratantes. |
| DORA-RTS532-4-1-h | art. 4.º, n.º 1, al. h) | Conteúdo contratual/jurídico específico do DORA sem correspondente prescritivo no Manual. Cláusulas sobre subcontratantes. |
| DORA-RTS532-4-1-j | art. 4.º, n.º 1, al. j) | Conteúdo contratual/jurídico específico do DORA sem correspondente prescritivo no Manual. Cláusulas sobre subcontratantes. |
| DORA-RTS532-4-1-k | art. 4.º, n.º 1, al. k) | Conteúdo contratual/jurídico específico do DORA sem correspondente prescritivo no Manual. Cláusulas sobre subcontratantes. |
| DORA-RTS532-4-1-l | art. 4.º, n.º 1, al. l) | Conteúdo contratual/jurídico específico do DORA sem correspondente prescritivo no Manual. Cláusulas sobre subcontratantes. |
| DORA-RTS532-4-2 | art. 4.º, n.º 2 | Conteúdo contratual/jurídico específico do DORA sem correspondente prescritivo no Manual. Cláusulas sobre subcontratantes. |
| DORA-RTS532-5-1 | art. 5.º, n.º 1 | Conteúdo contratual/jurídico específico do DORA sem correspondente prescritivo no Manual. Cláusulas sobre subcontratantes. |
| DORA-RTS532-5-2 | art. 5.º, n.º 2 | Conteúdo contratual/jurídico específico do DORA sem correspondente prescritivo no Manual. Cláusulas sobre subcontratantes. |
| DORA-RTS532-5-3 | art. 5.º, n.º 3 | Conteúdo contratual/jurídico específico do DORA sem correspondente prescritivo no Manual. Cláusulas sobre subcontratantes. |
| DORA-RTS532-5-4 | art. 5.º, n.º 4 | Conteúdo contratual/jurídico específico do DORA sem correspondente prescritivo no Manual. Cláusulas sobre subcontratantes. |
| DORA-RTS1774-2-2-e | art. 2.º, n.º 2, al. e) | Consequências disciplinares do incumprimento — regime de RH/compliance. |
| DORA-RTS1774-2-2-g | art. 2.º, n.º 2, al. g) | Dever do órgão de administração / estrutura de governo interno; o Manual não fixa órgãos nem alçadas societárias. Segregação de funções entre linhas de defesa. |
| DORA-RTS1774-4-1 | art. 4.º, n.º 1 | A gestão de activos da entidade como um todo (inventário e classificação de todos os activos, infraestrutura, equipamentos, licenças) fica fora de âmbito: o Manual é centrado na aplicação. O inventário e a classificação da aplicação e dos seus componentes (CLA-001, SBOM) dão evidência para a parte que lhe toca. |
| DORA-RTS1774-4-2-a | art. 4.º, n.º 2, al. a) | A gestão de activos da entidade como um todo (inventário e classificação de todos os activos, infraestrutura, equipamentos, licenças) fica fora de âmbito: o Manual é centrado na aplicação. O inventário e a classificação da aplicação e dos seus componentes (CLA-001, SBOM) dão evidência para a parte que lhe toca. |
| DORA-RTS1774-4-2-b | art. 4.º, n.º 2, al. b) | A gestão de activos da entidade como um todo (inventário e classificação de todos os activos, infraestrutura, equipamentos, licenças) fica fora de âmbito: o Manual é centrado na aplicação. O inventário e a classificação da aplicação e dos seus componentes (CLA-001, SBOM) dão evidência para a parte que lhe toca. |
| DORA-RTS1774-4-2-c | art. 4.º, n.º 2, al. c) | A gestão de activos da entidade como um todo (inventário e classificação de todos os activos, infraestrutura, equipamentos, licenças) fica fora de âmbito: o Manual é centrado na aplicação. O inventário e a classificação da aplicação e dos seus componentes (CLA-001, SBOM) dão evidência para a parte que lhe toca. |
| DORA-RTS1774-8-2-b-ii | art. 8.º, n.º 2, al. b), subal. ii) | Calendarização de processamento (scheduling) com interdependências — operação de TI. |
| DORA-RTS1774-9-2 | art. 9.º, n.º 2 | Sistemas com aquisição longa ou intensivos em recursos — planeamento de aquisição de TI. |
| DORA-RTS1774-11-2-e | art. 11.º, n.º 2, al. e) | Segurança de postos de trabalho/dispositivos e suportes físicos (TI corporativa) — fora do ciclo de vida de desenvolvimento seguro. |
| DORA-RTS1774-11-2-f | art. 11.º, n.º 2, al. f) | Segurança de postos de trabalho/dispositivos e suportes físicos (TI corporativa) — fora do ciclo de vida de desenvolvimento seguro. |
| DORA-RTS1774-11-2-h | art. 11.º, n.º 2, al. h) | Segurança de postos de trabalho/dispositivos e suportes físicos (TI corporativa) — fora do ciclo de vida de desenvolvimento seguro. |
| DORA-RTS1774-11-2-j | art. 11.º, n.º 2, al. j) | Segurança de postos de trabalho/dispositivos e suportes físicos (TI corporativa) — fora do ciclo de vida de desenvolvimento seguro. |
| DORA-RTS1774-13-d | art. 13.º, al. d) | Controlo de acesso à rede (NAC) de dispositivos — infraestrutura de rede corporativa. |
| DORA-RTS1774-13-k | art. 13.º, al. k) | Hardening de equipamentos de rede segundo o vendedor — infraestrutura de rede. |
| DORA-RTS1774-15-5 | art. 15.º, n.º 5 | Dever do órgão de administração / estrutura de governo interno; o Manual não fixa órgãos nem alçadas societárias. |
| DORA-RTS1774-16-2-p2 | art. 16.º, n.º 2, segundo e terceiro parágrafos | Obrigação sectorial específica (CCP/CSD/plataformas de negociação/DRSP) — parâmetro operacional de mercado, fora de um manual transversal de engenharia de software. |
| DORA-RTS1774-17-2 | art. 17.º, n.º 2 | Obrigação sectorial específica (CCP/CSD/plataformas de negociação/DRSP) — parâmetro operacional de mercado, fora de um manual transversal de engenharia de software. |
| DORA-RTS1774-18-1 | art. 18.º, n.º 1 | Segurança física e ambiental de instalações — fora do âmbito de um manual de engenharia de software. |
| DORA-RTS1774-18-2 | art. 18.º, n.º 2, als. a) a e) e parágrafos seguintes | Segurança física e ambiental de instalações — fora do âmbito de um manual de engenharia de software. |
| DORA-RTS1774-21-g | art. 21.º, al. g) e parágrafos finais | Segurança física e ambiental de instalações — fora do âmbito de um manual de engenharia de software. |
| DORA-RTS1774-24-1-a | art. 24.º, n.º 1, al. a) | Gestão da continuidade do negócio/crise (BCM) de nível organizacional — o Manual trata resposta a incidentes cibernéticos e rollback, não BCM geral. |
| DORA-RTS1774-24-2 | art. 24.º, n.º 2 | Obrigação sectorial específica (CCP/CSD/plataformas de negociação/DRSP) — parâmetro operacional de mercado, fora de um manual transversal de engenharia de software. |
| DORA-RTS1774-24-3 | art. 24.º, n.º 3 | Obrigação sectorial específica (CCP/CSD/plataformas de negociação/DRSP) — parâmetro operacional de mercado, fora de um manual transversal de engenharia de software. |
| DORA-RTS1774-24-4 | art. 24.º, n.º 4 | Obrigação sectorial específica (CCP/CSD/plataformas de negociação/DRSP) — parâmetro operacional de mercado, fora de um manual transversal de engenharia de software. |
| DORA-RTS1774-25-3 | art. 25.º, n.os 3 e 4 | Obrigação sectorial específica (CCP/CSD/plataformas de negociação/DRSP) — parâmetro operacional de mercado, fora de um manual transversal de engenharia de software. |
| DORA-RTS1774-26-3 | art. 26.º, n.º 3 | Gestão da continuidade do negócio/crise (BCM) de nível organizacional — o Manual trata resposta a incidentes cibernéticos e rollback, não BCM geral. Opções alternativas de recuperação. |
| DORA-RTS1774-27-1 | art. 27.º, n.º 1 | Reporte/relação com a autoridade competente — plano jurídico-regulatório, não prescrição de engenharia de software. |
| DORA-RTS1774-27-2 | art. 27.º, n.º 2 | Reporte/relação com a autoridade competente — plano jurídico-regulatório, não prescrição de engenharia de software. |
| DORA-RTS1774-28-2-e | art. 28.º, n.º 2, al. e) | Dever do órgão de administração / estrutura de governo interno; o Manual não fixa órgãos nem alçadas societárias. Orçamento. |
| DORA-RTS1774-28-3 | art. 28.º, n.º 3 | Responsabilidade jurídica mantida ao subcontratar verificação. |
| DORA-RTS1774-28-4 | art. 28.º, n.º 4 | Dever do órgão de administração / estrutura de governo interno; o Manual não fixa órgãos nem alçadas societárias. Segregação entre controlo e auditoria interna. |
| DORA-RTS1774-32 | art. 32.º, n.os 1 a 3 | Segurança física e ambiental de instalações — fora do âmbito de um manual de engenharia de software. |
| DORA-RTS1774-34-a | art. 34.º, al. a) | A gestão de activos da entidade como um todo (inventário e classificação de todos os activos, infraestrutura, equipamentos, licenças) fica fora de âmbito: o Manual é centrado na aplicação. O inventário e a classificação da aplicação e dos seus componentes (CLA-001, SBOM) dão evidência para a parte que lhe toca. |
| DORA-RTS1774-35-f | art. 35.º, al. f) | Segurança de postos de trabalho/dispositivos e suportes físicos (TI corporativa) — fora do ciclo de vida de desenvolvimento seguro. |
| DORA-RTS1774-35-g | art. 35.º, al. g) | Segurança de postos de trabalho/dispositivos e suportes físicos (TI corporativa) — fora do ciclo de vida de desenvolvimento seguro. |
| DORA-RTS1774-39-2-a | art. 39.º, n.º 2, als. a) a c) | Gestão da continuidade do negócio/crise (BCM) de nível organizacional — o Manual trata resposta a incidentes cibernéticos e rollback, não BCM geral. |
| DORA-RTS1774-39-2-h | art. 39.º, n.º 2, als. h) a j) | Gestão da continuidade do negócio/crise (BCM) de nível organizacional — o Manual trata resposta a incidentes cibernéticos e rollback, não BCM geral. |
| DORA-RTS1774-41-1 | art. 41.º, n.º 1 | Reporte/relação com a autoridade competente — plano jurídico-regulatório, não prescrição de engenharia de software. |
| DORA-RTS1774-41-2 | art. 41.º, n.º 2 | Reporte/relação com a autoridade competente — plano jurídico-regulatório, não prescrição de engenharia de software. |
| DORA-RTS301-1 | art. 1.º | Reporte/relação com a autoridade competente — plano jurídico-regulatório, não prescrição de engenharia de software. Conteúdo/modelos das notificações. |
| DORA-RTS301-2 | art. 2.º | Reporte/relação com a autoridade competente — plano jurídico-regulatório, não prescrição de engenharia de software. Conteúdo/modelos das notificações. |
| DORA-RTS301-3 | art. 3.º | Reporte/relação com a autoridade competente — plano jurídico-regulatório, não prescrição de engenharia de software. Conteúdo/modelos das notificações. |
| DORA-RTS301-4 | art. 4.º | Reporte/relação com a autoridade competente — plano jurídico-regulatório, não prescrição de engenharia de software. Conteúdo/modelos das notificações. |
| DORA-RTS301-5-3 | art. 5.º, n.º 3 | Reporte/relação com a autoridade competente — plano jurídico-regulatório, não prescrição de engenharia de software. Conteúdo/modelos das notificações. |
| DORA-RTS301-6 | art. 6.º | Reporte/relação com a autoridade competente — plano jurídico-regulatório, não prescrição de engenharia de software. Conteúdo/modelos das notificações. |
| DORA-ITS302-1-1 | art. 1.º, n.º 1, al. a) a c); anexo I | Reporte/relação com a autoridade competente — plano jurídico-regulatório, não prescrição de engenharia de software. Modelos, canais e procedimentos de comunicação (ITS 2025/302). |
| DORA-ITS302-1-2 | art. 1.º, n.º 2 | Reporte/relação com a autoridade competente — plano jurídico-regulatório, não prescrição de engenharia de software. Modelos, canais e procedimentos de comunicação (ITS 2025/302). |
| DORA-ITS302-1-3 | art. 1.º, n.º 3 | Reporte/relação com a autoridade competente — plano jurídico-regulatório, não prescrição de engenharia de software. Modelos, canais e procedimentos de comunicação (ITS 2025/302). |
| DORA-ITS302-1-4 | art. 1.º, n.º 4 | Reporte/relação com a autoridade competente — plano jurídico-regulatório, não prescrição de engenharia de software. Modelos, canais e procedimentos de comunicação (ITS 2025/302). |
| DORA-ITS302-1-5 | art. 1.º, n.º 5; anexo II | Reporte/relação com a autoridade competente — plano jurídico-regulatório, não prescrição de engenharia de software. Modelos, canais e procedimentos de comunicação (ITS 2025/302). |
| DORA-ITS302-3 | art. 3.º | Reporte/relação com a autoridade competente — plano jurídico-regulatório, não prescrição de engenharia de software. Modelos, canais e procedimentos de comunicação (ITS 2025/302). |
| DORA-ITS302-4-1 | art. 4.º, n.º 1 | Reporte/relação com a autoridade competente — plano jurídico-regulatório, não prescrição de engenharia de software. Modelos, canais e procedimentos de comunicação (ITS 2025/302). |
| DORA-ITS302-4-2 | art. 4.º, n.º 2 | Reporte/relação com a autoridade competente — plano jurídico-regulatório, não prescrição de engenharia de software. Modelos, canais e procedimentos de comunicação (ITS 2025/302). |
| DORA-ITS302-5 | art. 5.º | Reporte/relação com a autoridade competente — plano jurídico-regulatório, não prescrição de engenharia de software. Modelos, canais e procedimentos de comunicação (ITS 2025/302). |
| DORA-ITS302-6-1 | art. 6.º, n.º 1 | Reporte/relação com a autoridade competente — plano jurídico-regulatório, não prescrição de engenharia de software. Modelos, canais e procedimentos de comunicação (ITS 2025/302). |
| DORA-ITS302-6-2 | art. 6.º, n.º 2 | Reporte/relação com a autoridade competente — plano jurídico-regulatório, não prescrição de engenharia de software. Modelos, canais e procedimentos de comunicação (ITS 2025/302). |
| DORA-ITS302-6-3 | art. 6.º, n.º 3 | Reporte/relação com a autoridade competente — plano jurídico-regulatório, não prescrição de engenharia de software. Modelos, canais e procedimentos de comunicação (ITS 2025/302). |
| DORA-ITS302-7-1 | art. 7.º, n.º 1 | Reporte/relação com a autoridade competente — plano jurídico-regulatório, não prescrição de engenharia de software. Modelos, canais e procedimentos de comunicação (ITS 2025/302). |
| DORA-ITS302-7-2 | art. 7.º, n.º 2 | Reporte/relação com a autoridade competente — plano jurídico-regulatório, não prescrição de engenharia de software. Modelos, canais e procedimentos de comunicação (ITS 2025/302). |
| DORA-ITS302-7-3 | art. 7.º, n.º 3 | Reporte/relação com a autoridade competente — plano jurídico-regulatório, não prescrição de engenharia de software. Modelos, canais e procedimentos de comunicação (ITS 2025/302). |
| DORA-ITS302-8-1 | art. 8.º, n.º 1; anexos III e IV | Reporte/relação com a autoridade competente — plano jurídico-regulatório, não prescrição de engenharia de software. Modelos, canais e procedimentos de comunicação (ITS 2025/302). |
| DORA-ITS302-8-2 | art. 8.º, n.º 2 | Reporte/relação com a autoridade competente — plano jurídico-regulatório, não prescrição de engenharia de software. Modelos, canais e procedimentos de comunicação (ITS 2025/302). |
| DORA-RTS1190-4-1 | art. 4.º, n.º 1 | Processo TLPT regulado (Reg. Delegado (UE) 2025/1190) — o addon 14 do Cap. 10 declara-o expressamente fora do âmbito do Manual (compliance/GRC/supervisor). |
| DORA-RTS1190-4-2-b | art. 4.º, n.º 2, al. b) | Processo TLPT regulado (Reg. Delegado (UE) 2025/1190) — o addon 14 do Cap. 10 declara-o expressamente fora do âmbito do Manual (compliance/GRC/supervisor). |
| DORA-RTS1190-4-2-d | art. 4.º, n.º 2, al. d) | Processo TLPT regulado (Reg. Delegado (UE) 2025/1190) — o addon 14 do Cap. 10 declara-o expressamente fora do âmbito do Manual (compliance/GRC/supervisor). |
| DORA-RTS1190-4-2-e | art. 4.º, n.º 2, al. e) | Processo TLPT regulado (Reg. Delegado (UE) 2025/1190) — o addon 14 do Cap. 10 declara-o expressamente fora do âmbito do Manual (compliance/GRC/supervisor). |
| DORA-RTS1190-4-2-f | art. 4.º, n.º 2, al. f) | Processo TLPT regulado (Reg. Delegado (UE) 2025/1190) — o addon 14 do Cap. 10 declara-o expressamente fora do âmbito do Manual (compliance/GRC/supervisor). |
| DORA-RTS1190-6-2 | art. 6.º, n.º 2 | Processo TLPT regulado (Reg. Delegado (UE) 2025/1190) — o addon 14 do Cap. 10 declara-o expressamente fora do âmbito do Manual (compliance/GRC/supervisor). |
| DORA-RTS1190-7-1-a | art. 7.º, n.º 1, al. a) | Processo TLPT regulado (Reg. Delegado (UE) 2025/1190) — o addon 14 do Cap. 10 declara-o expressamente fora do âmbito do Manual (compliance/GRC/supervisor). |
| DORA-RTS1190-7-1-b | art. 7.º, n.º 1, al. b) | Processo TLPT regulado (Reg. Delegado (UE) 2025/1190) — o addon 14 do Cap. 10 declara-o expressamente fora do âmbito do Manual (compliance/GRC/supervisor). |
| DORA-RTS1190-7-1-cd | art. 7.º, n.º 1, al. c) e d) | Processo TLPT regulado (Reg. Delegado (UE) 2025/1190) — o addon 14 do Cap. 10 declara-o expressamente fora do âmbito do Manual (compliance/GRC/supervisor). |
| DORA-RTS1190-7-1-e | art. 7.º, n.º 1, al. e) | Processo TLPT regulado (Reg. Delegado (UE) 2025/1190) — o addon 14 do Cap. 10 declara-o expressamente fora do âmbito do Manual (compliance/GRC/supervisor). |
| DORA-RTS1190-7-1-f | art. 7.º, n.º 1, al. f) | Processo TLPT regulado (Reg. Delegado (UE) 2025/1190) — o addon 14 do Cap. 10 declara-o expressamente fora do âmbito do Manual (compliance/GRC/supervisor). |
| DORA-RTS1190-7-1-g | art. 7.º, n.º 1, al. g) | Processo TLPT regulado (Reg. Delegado (UE) 2025/1190) — o addon 14 do Cap. 10 declara-o expressamente fora do âmbito do Manual (compliance/GRC/supervisor). |
| DORA-RTS1190-7-1-h | art. 7.º, n.º 1, al. h) | Processo TLPT regulado (Reg. Delegado (UE) 2025/1190) — o addon 14 do Cap. 10 declara-o expressamente fora do âmbito do Manual (compliance/GRC/supervisor). |
| DORA-RTS1190-7-2 | art. 7.º, n.º 2 | Processo TLPT regulado (Reg. Delegado (UE) 2025/1190) — o addon 14 do Cap. 10 declara-o expressamente fora do âmbito do Manual (compliance/GRC/supervisor). |
| DORA-RTS1190-8-1 | art. 8.º, n.º 1 | Processo TLPT regulado (Reg. Delegado (UE) 2025/1190) — o addon 14 do Cap. 10 declara-o expressamente fora do âmbito do Manual (compliance/GRC/supervisor). |
| DORA-RTS1190-9-1 | art. 9.º, n.º 1 | Processo TLPT regulado (Reg. Delegado (UE) 2025/1190) — o addon 14 do Cap. 10 declara-o expressamente fora do âmbito do Manual (compliance/GRC/supervisor). |
| DORA-RTS1190-9-2 | art. 9.º, n.º 2; anexo I | Processo TLPT regulado (Reg. Delegado (UE) 2025/1190) — o addon 14 do Cap. 10 declara-o expressamente fora do âmbito do Manual (compliance/GRC/supervisor). |
| DORA-RTS1190-9-4 | art. 9.º, n.º 4 | Processo TLPT regulado (Reg. Delegado (UE) 2025/1190) — o addon 14 do Cap. 10 declara-o expressamente fora do âmbito do Manual (compliance/GRC/supervisor). |
| DORA-RTS1190-9-6-oa | art. 9.º, n.º 6, 2.º período | Processo TLPT regulado (Reg. Delegado (UE) 2025/1190) — o addon 14 do Cap. 10 declara-o expressamente fora do âmbito do Manual (compliance/GRC/supervisor). |
| DORA-RTS1190-9-8 | art. 9.º, n.º 8 | Processo TLPT regulado (Reg. Delegado (UE) 2025/1190) — o addon 14 do Cap. 10 declara-o expressamente fora do âmbito do Manual (compliance/GRC/supervisor). |
| DORA-RTS1190-9-9 | art. 9.º, n.º 9 | Processo TLPT regulado (Reg. Delegado (UE) 2025/1190) — o addon 14 do Cap. 10 declara-o expressamente fora do âmbito do Manual (compliance/GRC/supervisor). |
| DORA-RTS1190-9-10 | art. 9.º, n.º 10 | Processo TLPT regulado (Reg. Delegado (UE) 2025/1190) — o addon 14 do Cap. 10 declara-o expressamente fora do âmbito do Manual (compliance/GRC/supervisor). |
| DORA-RTS1190-9-11 | art. 9.º, n.º 11 | Processo TLPT regulado (Reg. Delegado (UE) 2025/1190) — o addon 14 do Cap. 10 declara-o expressamente fora do âmbito do Manual (compliance/GRC/supervisor). |
| DORA-RTS1190-10-2 | art. 10.º, n.º 2 | Processo TLPT regulado (Reg. Delegado (UE) 2025/1190) — o addon 14 do Cap. 10 declara-o expressamente fora do âmbito do Manual (compliance/GRC/supervisor). |
| DORA-RTS1190-10-3 | art. 10.º, n.º 3 | Processo TLPT regulado (Reg. Delegado (UE) 2025/1190) — o addon 14 do Cap. 10 declara-o expressamente fora do âmbito do Manual (compliance/GRC/supervisor). |
| DORA-RTS1190-10-4 | art. 10.º, n.º 4 | Processo TLPT regulado (Reg. Delegado (UE) 2025/1190) — o addon 14 do Cap. 10 declara-o expressamente fora do âmbito do Manual (compliance/GRC/supervisor). |
| DORA-RTS1190-10-5 | art. 10.º, n.º 5; anexo III | Processo TLPT regulado (Reg. Delegado (UE) 2025/1190) — o addon 14 do Cap. 10 declara-o expressamente fora do âmbito do Manual (compliance/GRC/supervisor). |
| DORA-RTS1190-10-6 | art. 10.º, n.º 6 | Processo TLPT regulado (Reg. Delegado (UE) 2025/1190) — o addon 14 do Cap. 10 declara-o expressamente fora do âmbito do Manual (compliance/GRC/supervisor). |
| DORA-RTS1190-11-1 | art. 11.º, n.º 1; anexo IV | Processo TLPT regulado (Reg. Delegado (UE) 2025/1190) — o addon 14 do Cap. 10 declara-o expressamente fora do âmbito do Manual (compliance/GRC/supervisor). |
| DORA-RTS1190-11-2 | art. 11.º, n.º 2 | Processo TLPT regulado (Reg. Delegado (UE) 2025/1190) — o addon 14 do Cap. 10 declara-o expressamente fora do âmbito do Manual (compliance/GRC/supervisor). |
| DORA-RTS1190-11-3 | art. 11.º, n.º 3 | Processo TLPT regulado (Reg. Delegado (UE) 2025/1190) — o addon 14 do Cap. 10 declara-o expressamente fora do âmbito do Manual (compliance/GRC/supervisor). |
| DORA-RTS1190-11-4 | art. 11.º, n.º 4 | Processo TLPT regulado (Reg. Delegado (UE) 2025/1190) — o addon 14 do Cap. 10 declara-o expressamente fora do âmbito do Manual (compliance/GRC/supervisor). |
| DORA-RTS1190-11-5 | art. 11.º, n.º 5 | Processo TLPT regulado (Reg. Delegado (UE) 2025/1190) — o addon 14 do Cap. 10 declara-o expressamente fora do âmbito do Manual (compliance/GRC/supervisor). |
| DORA-RTS1190-11-6 | art. 11.º, n.º 6 | Processo TLPT regulado (Reg. Delegado (UE) 2025/1190) — o addon 14 do Cap. 10 declara-o expressamente fora do âmbito do Manual (compliance/GRC/supervisor). |
| DORA-RTS1190-11-7 | art. 11.º, n.º 7 | Processo TLPT regulado (Reg. Delegado (UE) 2025/1190) — o addon 14 do Cap. 10 declara-o expressamente fora do âmbito do Manual (compliance/GRC/supervisor). |
| DORA-RTS1190-11-8 | art. 11.º, n.º 8 | Processo TLPT regulado (Reg. Delegado (UE) 2025/1190) — o addon 14 do Cap. 10 declara-o expressamente fora do âmbito do Manual (compliance/GRC/supervisor). |
| DORA-RTS1190-11-9 | art. 11.º, n.º 9 | Processo TLPT regulado (Reg. Delegado (UE) 2025/1190) — o addon 14 do Cap. 10 declara-o expressamente fora do âmbito do Manual (compliance/GRC/supervisor). |
| DORA-RTS1190-11-10 | art. 11.º, n.º 10 | Processo TLPT regulado (Reg. Delegado (UE) 2025/1190) — o addon 14 do Cap. 10 declara-o expressamente fora do âmbito do Manual (compliance/GRC/supervisor). |
| DORA-RTS1190-12-1 | art. 12.º, n.º 1 | Processo TLPT regulado (Reg. Delegado (UE) 2025/1190) — o addon 14 do Cap. 10 declara-o expressamente fora do âmbito do Manual (compliance/GRC/supervisor). |
| DORA-RTS1190-12-2 | art. 12.º, n.º 2; anexo V | Processo TLPT regulado (Reg. Delegado (UE) 2025/1190) — o addon 14 do Cap. 10 declara-o expressamente fora do âmbito do Manual (compliance/GRC/supervisor). |
| DORA-RTS1190-12-3 | art. 12.º, n.º 3 | Processo TLPT regulado (Reg. Delegado (UE) 2025/1190) — o addon 14 do Cap. 10 declara-o expressamente fora do âmbito do Manual (compliance/GRC/supervisor). |
| DORA-RTS1190-12-4 | art. 12.º, n.º 4; anexo VI | Processo TLPT regulado (Reg. Delegado (UE) 2025/1190) — o addon 14 do Cap. 10 declara-o expressamente fora do âmbito do Manual (compliance/GRC/supervisor). |
| DORA-RTS1190-12-5 | art. 12.º, n.º 5 | Processo TLPT regulado (Reg. Delegado (UE) 2025/1190) — o addon 14 do Cap. 10 declara-o expressamente fora do âmbito do Manual (compliance/GRC/supervisor). |
| DORA-RTS1190-12-6 | art. 12.º, n.º 6 | Processo TLPT regulado (Reg. Delegado (UE) 2025/1190) — o addon 14 do Cap. 10 declara-o expressamente fora do âmbito do Manual (compliance/GRC/supervisor). |
| DORA-RTS1190-12-7 | art. 12.º, n.º 7; anexo VII | Processo TLPT regulado (Reg. Delegado (UE) 2025/1190) — o addon 14 do Cap. 10 declara-o expressamente fora do âmbito do Manual (compliance/GRC/supervisor). |
| DORA-RTS1190-13-1 | art. 13.º, n.º 1 | Processo TLPT regulado (Reg. Delegado (UE) 2025/1190) — o addon 14 do Cap. 10 declara-o expressamente fora do âmbito do Manual (compliance/GRC/supervisor). |
| DORA-RTS1190-15-1-a | art. 15.º, n.º 1, 1.º par., al. a), e 2.º par. | Processo TLPT regulado (Reg. Delegado (UE) 2025/1190) — o addon 14 do Cap. 10 declara-o expressamente fora do âmbito do Manual (compliance/GRC/supervisor). |
| DORA-RTS1190-15-1-b | art. 15.º, n.º 1, al. b) | Processo TLPT regulado (Reg. Delegado (UE) 2025/1190) — o addon 14 do Cap. 10 declara-o expressamente fora do âmbito do Manual (compliance/GRC/supervisor). |
| DORA-RTS1190-15-1-c | art. 15.º, n.º 1, al. c) | Processo TLPT regulado (Reg. Delegado (UE) 2025/1190) — o addon 14 do Cap. 10 declara-o expressamente fora do âmbito do Manual (compliance/GRC/supervisor). |
| DORA-RTS1190-15-3 | art. 15.º, n.º 3 | Processo TLPT regulado (Reg. Delegado (UE) 2025/1190) — o addon 14 do Cap. 10 declara-o expressamente fora do âmbito do Manual (compliance/GRC/supervisor). |
