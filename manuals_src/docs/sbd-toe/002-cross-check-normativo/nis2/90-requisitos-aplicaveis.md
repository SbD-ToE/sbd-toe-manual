---
id: requisitos-aplicaveis
title: "Requisitos aplicáveis — Entidade essencial ou importante (NIS2)"
description: "Vista gerada: requisitos do Manual que se aplicam sob o contexto CTX-NIS2, por nível e grau, com os pisos que o regime eleva e a base legal de cada um."
sidebar_position: 90
tags: [cross-check, nis2, requisitos, overlay, gerado]
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
  - 002-cross-check-normativo/_matriz/nis2.yaml
---

# Requisitos aplicáveis: Entidade essencial ou importante (NIS2)

> **Página gerada** por `scripts/gen_reg_views.py` a partir dos catálogos de requisitos e de `002-cross-check-normativo/_contextos-regulatorios.yaml`. Não se edita à mão: o catálogo de cada requisito é a fonte canónica, e esta página é uma vista do overlay regulatório.

Esta página junta, para o contexto **CTX-NIS2**, a selecção base do Manual por nível e os **pisos** que o regime eleva, cada um com a obrigação que o fundamenta. Um contexto nunca baixa um mínimo do Manual.

## Quando se aplica {#quando-se-aplica}

A entidade é essencial ou importante nos termos do art. 3.º da Diretiva (UE) 2022/2555, tal como transposta (em Portugal, o regime jurídico da cibersegurança). O contexto declara-se por entidade e é herdado por todas as aplicações. Declara-se por entidade e é herdado por todas as aplicações.

> Diretiva (UE) 2022/2555, art. 3.º, n.os 1 e 2: «Para efeitos da presente diretiva, consideram-se entidades essenciais as seguintes entidades»

## Graus {#graus}

- **PERTINENTE** — Entidade pertinente do Reg. de Execução (UE) 2024/2690 (cumulativo com o contexto). A entidade é de um dos tipos enumerados no art. 1.º do Reg. de Execução (UE) 2024/2690 (prestadores de DNS, registos de TLD, computação em nuvem, centros de dados, redes de distribuição de conteúdos, serviços geridos e de segurança gerida, mercados em linha, motores de pesquisa, redes sociais, serviços de confiança).

## Pisos do contexto {#pisos}

| Piso | Alvo | Grau | Piso exigido | Âmbito | Base legal | Justificação de não aplicabilidade |
|---|---|---|---|---|---|---|
| CTX-NIS2-P01 | [Política 32 §2](/sbd-toe/assets/policies/policy-irp#2-âmbito-e-obrigatoriedade) | — | obrigatório | Processo de resposta a incidentes (IRP) obrigatório em qualquer nível, incluindo o registo dos incidentes e o post-mortem dos incidentes significativos, com a revisão dos artefactos afectados (§4.6). | Diretiva (UE) 2022/2555, art. 21.º, n.º 2, al. b); Reg. de Execução (UE) 2024/2690, anexo, ponto 3.1.1: «Tratamento de incidentes» (NIS2-21-2-b, NIS2-IR2690-3.1.1) | não admitida |
| CTX-NIS2-P02 | `OPS-007` | — | obrigatório | — | Diretiva (UE) 2022/2555, art. 21.º, n.º 2, al. b); Reg. de Execução (UE) 2024/2690, anexo, ponto 3.1.1: «Tratamento de incidentes» (NIS2-21-2-b, NIS2-IR2690-3.1.1) | não admitida |
| CTX-NIS2-P03 | `LOG-004` | PERTINENTE | obrigatório | — | Reg. de Execução (UE) 2024/2690, anexo, ponto 3.2.4: «Os registos devem ser analisados regularmente para detetar eventuais tendências invulgares ou indesejadas.» (NIS2-IR2690-3.2.4) | não admitida |
| CTX-NIS2-P04 | `LOG-007` | PERTINENTE | obrigatório | — | Reg. de Execução (UE) 2024/2690, anexo, ponto 3.2.4: «Se os valores fixados para um limiar de alerta forem excedidos, o alerta é acionado automaticamente, se for caso disso.» (NIS2-IR2690-3.2.4) | não admitida |
| CTX-NIS2-P05 | `OPS-005` | PERTINENTE | obrigatório | — | Reg. de Execução (UE) 2024/2690, anexo, ponto 3.2.4: «Cumpre às entidades pertinentes assegurar que, em caso de alerta, seja dada uma resposta qualificada e adequada em tempo útil.» (NIS2-IR2690-3.2.4) | não admitida |
| CTX-NIS2-P06 | `LOG-005` | PERTINENTE | obrigatório | Inclui cópias de segurança dos registos, protegidas do acesso e de alterações não autorizados. | Reg. de Execução (UE) 2024/2690, anexo, ponto 3.2.5: «As entidades pertinentes mantêm registos — bem como cópias de segurança dos mesmos — durante um período predefinido e protegem-nos do acesso ou de alterações não autorizados.» (NIS2-IR2690-3.2.5) | não admitida |
| CTX-NIS2-P07 | [Política 33 §2](/sbd-toe/assets/policies/policy-contratacao-segura#2-âmbito-e-obrigatoriedade) | PERTINENTE | obrigatório | Política de segurança da cadeia de abastecimento que rege as relações com fornecedores e prestadores de serviços directos, em qualquer nível. | Reg. de Execução (UE) 2024/2690, anexo, ponto 5.1.1: «as entidades pertinentes estabelecem, executam e aplicam uma política de segurança da cadeia de abastecimento que reja as relações com os seus fornecedores e prestadores de serviços diretos» (NIS2-IR2690-5.1.1) | não admitida |
| CTX-NIS2-P08 | `GOV-006` | PERTINENTE | obrigatório | — | Reg. de Execução (UE) 2024/2690, anexo, ponto 5.1.1: «as entidades pertinentes estabelecem, executam e aplicam uma política de segurança da cadeia de abastecimento que reja as relações com os seus fornecedores e prestadores de serviços diretos» (NIS2-IR2690-5.1.1) | não admitida |
| CTX-NIS2-P09 | `GOV-007` | PERTINENTE | obrigatório | — | Reg. de Execução (UE) 2024/2690, anexo, ponto 5.1.1: «as entidades pertinentes estabelecem, executam e aplicam uma política de segurança da cadeia de abastecimento que reja as relações com os seus fornecedores e prestadores de serviços diretos» (NIS2-IR2690-5.1.1) | não admitida |
| CTX-NIS2-P10 | `DPL-007` | PERTINENTE | obrigatório | Alterações testadas e avaliadas antes de aplicadas, incluindo alterações de emergência e de configuração. | Reg. de Execução (UE) 2024/2690, anexo, ponto 6.4.2: «Os procedimentos devem assegurar que tais alterações são documentadas e, antes de serem aplicadas, são testadas e avaliadas tendo em conta o impacto potencial, com base na avaliação dos riscos realizada nos termos do ponto 2.1.» (NIS2-IR2690-6.4.2) | não admitida |
| CTX-NIS2-P11 | `IAC-007` | PERTINENTE | obrigatório | — | Reg. de Execução (UE) 2024/2690, anexo, ponto 6.4.2: «Os procedimentos devem assegurar que tais alterações são documentadas e, antes de serem aplicadas, são testadas e avaliadas tendo em conta o impacto potencial, com base na avaliação dos riscos realizada nos termos do ponto 2.1.» (NIS2-IR2690-6.4.2) | admitida |
| CTX-NIS2-P12 | `ACC-010` | PERTINENTE | obrigatório | Inclui os direitos de acesso das contas privilegiadas e de administração do sistema, a intervalos planeados, com os resultados documentados. | Reg. de Execução (UE) 2024/2690, anexo, ponto 11.2.3: «As entidades pertinentes analisam os direitos de acesso a intervalos planeados e alteram-nos com base em alterações organizacionais.» (NIS2-IR2690-11.2.3) | não admitida |
| CTX-NIS2-P13 | `GOV-016` | PERTINENTE | obrigatório | Contas privilegiadas e contas de administração do sistema. | Reg. de Execução (UE) 2024/2690, anexo, pontos 11.3.1, 11.3.2, al. a), e 11.4.1: «Estabelecem fortes procedimentos de identificação, autenticação (autenticação multifatores, por exemplo) e autorização para as contas privilegiadas e as contas de administração do sistema» (NIS2-IR2690-11.3.1, NIS2-IR2690-11.3.2, NIS2-IR2690-11.4.1) | não admitida |
| CTX-NIS2-P14 | `GOV-015` | — | obrigatório | Tratamento e divulgação de vulnerabilidades, incluindo as comunicadas por fontes externas. | Diretiva (UE) 2022/2555, art. 21.º, n.º 2, al. e): «incluindo o tratamento e a divulgação de vulnerabilidades» (NIS2-21-2-e) | não admitida |
| CTX-NIS2-P15 | `GOV-015` | PERTINENTE | obrigatório | O procedimento de divulgação segue a política nacional de divulgação coordenada de vulnerabilidades. | Reg. de Execução (UE) 2024/2690, anexo, ponto 6.10.2, al. e): «procedimento para a divulgação de vulnerabilidades em conformidade com a política nacional aplicável em matéria de divulgação coordenada de vulnerabilidades» (NIS2-IR2690-6.10.2) | não admitida |
| CTX-NIS2-P16 | `OPS-016` | PERTINENTE | obrigatório | Cópias completas e exactas, incluindo dados de configuração e dados em nuvem, guardadas em local seguro fora da rede do sistema; integridade verificada e recuperação testada, em qualquer nível. | Reg. de Execução (UE) 2024/2690, anexo, pontos 4.2.1 a 4.2.3 e 4.2.6: «as entidades pertinentes estabelecem planos de reserva» (NIS2-IR2690-4.2.1, NIS2-IR2690-4.2.2, NIS2-IR2690-4.2.3, NIS2-IR2690-4.2.6) | não admitida |
| CTX-NIS2-P17 | `OPS-017` | PERTINENTE | obrigatório | Plano de recuperação com condições de activação e desactivação e ordem de recuperação, também em L1. | Reg. de Execução (UE) 2024/2690, anexo, pontos 4.1.1 e 4.1.2: «As operações das entidades pertinentes devem ser restabelecidas de acordo com o plano de continuidade das atividades e de recuperação de desastres.» (NIS2-IR2690-4.1.1, NIS2-IR2690-4.1.2) | não admitida |
| CTX-NIS2-P18 | `GOV-014` | PERTINENTE | obrigatório | Revisão a intervalos planeados das identidades e das contas privilegiadas e de administração nos sistemas de suporte, com resultados documentados. | Reg. de Execução (UE) 2024/2690, anexo, pontos 11.2.3, 11.3.3 e 11.5.4: «As entidades pertinentes analisam os direitos de acesso a intervalos planeados e alteram-nos com base em alterações organizacionais.» (NIS2-IR2690-11.2.3, NIS2-IR2690-11.3.3, NIS2-IR2690-11.5.4) | não admitida |
| CTX-NIS2-P19 | `GOV-017` | PERTINENTE | obrigatório | Concessão, alteração, retirada e documentação dos direitos de acesso; identidades únicas, associadas a uma pessoa e supervisionadas; registo da gestão de identidades. | Reg. de Execução (UE) 2024/2690, anexo, pontos 11.2.1 e 11.5.1 a 11.5.3: «As entidades pertinentes concedem, alteram, retiram e documentam os direitos de acesso aos sistemas de rede e informação em conformidade com a política de controlo do acesso a que se refere o ponto 11.1.» (NIS2-IR2690-11.2.1, NIS2-IR2690-11.5.1, NIS2-IR2690-11.5.2, NIS2-IR2690-11.5.3) | não admitida |
| CTX-NIS2-P20 | `ENC-007` | PERTINENTE | obrigatório | Gestão de chaves e de certificados em qualquer nível, com os métodos do ponto 9.2, al. c). | Reg. de Execução (UE) 2024/2690, anexo, ponto 9.2: «A abordagem das entidades pertinentes no que toca à gestão de chaves» (NIS2-IR2690-9.2) | admitida |
| CTX-NIS2-P21 | `ENC-003` | PERTINENTE | obrigatório | Primitivas e protocolos aprovados, com agilidade criptográfica quando adequado, revistos a intervalos planeados perante o progresso técnico, em qualquer nível. | Reg. de Execução (UE) 2024/2690, anexo, pontos 9.2 e 9.3: «seguindo, se for caso disso, uma abordagem de agilidade criptográfica» (NIS2-IR2690-9.2, NIS2-IR2690-9.3) | admitida |

## Requisitos acrescentados pelo regime {#acrescentos}

Estes requisitos só fazem sentido sob o regime e por isso não vivem nos catálogos do Manual; definem-se aqui, com a base legal de cada um.

| Requisito | Nome | Critério de aceitação | Base legal |
|---|---|---|---|
| `CTX-NIS2-R01` | Redundância pelo menos parcial | Com base na avaliação de riscos e no plano de continuidade, disponibilidade suficiente de recursos através de redundância, pelo menos parcial, dos sistemas de rede e informação e dos canais de comunicação de que a aplicação depende; recursos acompanhados e ajustados em função dos requisitos de cópias de segurança e de redundância. | Reg. de Execução (UE) 2024/2690, anexo, pontos 4.2.4 e 4.2.5: «asseguram a disponibilidade suficiente de recursos através, no mínimo, da redundância parcial dos seguintes elementos» (NIS2-IR2690-4.2.4, NIS2-IR2690-4.2.5) |
| `CTX-NIS2-R02` | Critério de incidente significativo | Um incidente é avaliado como significativo, a partir dos dados de impacto do registo (Política 32 §4.3), quando causou ou pode causar graves perturbações operacionais dos serviços ou perdas financeiras à entidade, ou danos materiais ou imateriais consideráveis a outras pessoas; a avaliação e a decisão ficam registadas. | Diretiva (UE) 2022/2555, art. 23.º, n.º 3: «Considera-se que um incidente é significativo se» (NIS2-23-3) |
| `CTX-NIS2-R03` | Limiares de incidente significativo e agregação dos recorrentes | Nas entidades pertinentes, aplicam-se os critérios do art. 3.º do Reg. de Execução (UE) 2024/2690 (perdas financeiras directas acima de 500 000 EUR ou 5 % do volume de negócios, o que for menor; fuga de segredos comerciais; morte ou danos consideráveis à saúde; acesso malicioso com risco de perturbação grave; e os critérios específicos por tipo de entidade). Trimestralmente, avalia-se a existência de incidentes recorrentes: os que ocorreram pelo menos duas vezes em seis meses, com a mesma causa primária aparente, e cumprem em conjunto o critério financeiro contam como um incidente significativo. | Reg. de Execução (UE) 2024/2690, arts. 3.º e 4.º e anexo, ponto 3.4.2: «Ocorreram pelo menos duas vezes num período de seis meses» (NIS2-IR2690-art3, NIS2-IR2690-art4, NIS2-IR2690-3.4.2) |

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
| `OPS-007` | Integração com processo formal de resposta a incidentes | ▲ | ▲ | ▲ | CTX-NIS2-P02 |
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
| `GOV-015` | Divulgação coordenada de vulnerabilidades com canal de receção publicado | ▲ | ▲ | ▲ | CTX-NIS2-P14 |
| `GOV-016` | Contas privilegiadas e de administração dos sistemas de suporte | ✔ | ✔ | ✔ | — |
| `GOV-017` | Ciclo de vida das identidades com acesso aos sistemas | ✔ | ✔ | ✔ | — |
| `CTX-NIS2-R02` | Critério de incidente significativo | ▲ | ▲ | ▲ | — |

## Lista de requisitos — PERTINENTE {#lista-pertinente}

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
| `ACC-010` | Revisão periódica de permissões | ▲ | ▲ | ▲ | CTX-NIS2-P12 |
| `LOG-001` | Registo de eventos críticos | ✔ | ✔ | ✔ | — |
| `LOG-002` | Atributos mínimos em logs | ✔ | ✔ | ✔ | — |
| `LOG-003` | Protecção de integridade e acesso aos logs | ✔ | ✔ | ✔ | — |
| `LOG-004` | Análise periódica de logs | ▲ | ▲ | ▲ | CTX-NIS2-P03 |
| `LOG-005` | Retenção mínima dos logs | ▲ | ▲ | ▲ | CTX-NIS2-P06 |
| `LOG-006` | Envio para sistema centralizado | — | ✔ | ✔ | — |
| `LOG-007` | Classificação e detecção de anomalias | ▲ | ▲ | ▲ | CTX-NIS2-P04 |
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
| `ENC-003` | Algoritmos e configurações criptográficas robustas | ▲ | ▲ | ▲ | CTX-NIS2-P21 |
| `ENC-004` | Hashing adaptativo de passwords | ✔ | ✔ | ✔ | — |
| `ENC-005` | Mascaramento de dados sensíveis em logs, outputs e respostas API | ✔ | ✔ | ✔ | — |
| `ENC-006` | Detecção e prevenção de segredos expostos em repositórios | ✔ | ✔ | ✔ | — |
| `ENC-007` | Ciclo de vida de chaves, segredos e certificados | ▲ | ▲ | ▲ | CTX-NIS2-P20 |
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
| `IAC-007` | Plan rastreável e aprovado antes de qualquer apply | ▲ | ▲ | ▲ | CTX-NIS2-P11 |
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
| `DPL-007` | Validação em staging antes de promoção a produção | ▲ | ▲ | ▲ | CTX-NIS2-P10 |
| `DPL-008` | Monitorização activa durante e após deploy | — | ✔ | ✔ | — |
| `DPL-009` | Deploy progressivo com contenção de impacto para aplicações críticas | — | — | ✔ | — |
| `DPL-010` | Release gates para sistemas com agentes AI | — | ✔ | ✔ | — |
| `DPL-011` | Canary e demoção de autonomia no release de modelos | — | — | ✔ | — |
| `OPS-001` | Logging estruturado e persistente para todos os componentes em produção | ✔ | ✔ | ✔ | — |
| `OPS-002` | Catálogo de eventos críticos de segurança definido e verificado | ✔ | ✔ | ✔ | — |
| `OPS-003` | Retenção de logs conforme política e requisitos regulatórios | — | ✔ | ✔ | — |
| `OPS-004` | Centralização de logs em sistema SIEM ou equivalente | — | ✔ | ✔ | — |
| `OPS-005` | Alertas automáticos para eventos de segurança críticos | ▲ | ▲ | ▲ | CTX-NIS2-P05 |
| `OPS-006` | SLA de resposta a alertas definido e medido | — | ✔ | ✔ | — |
| `OPS-007` | Integração com processo formal de resposta a incidentes | ▲ | ▲ | ▲ | CTX-NIS2-P02 |
| `OPS-008` | Correlação de eventos entre múltiplas fontes | — | — | ✔ | — |
| `OPS-009` | Deteção comportamental e baseline de actividade normal | — | — | ✔ | — |
| `OPS-010` | Métricas de eficácia da monitorização medidas e revistas | — | — | ✔ | — |
| `OPS-011` | Observabilidade dedicada a componentes AI/ML em produção | — | ✔ | ✔ | — |
| `OPS-012` | Audit completo por tool invocation de agente AI | — | ✔ | ✔ | — |
| `OPS-013` | Budget e detecção de runaway em consumo de modelo (token spend) | — | ✔ | ✔ | — |
| `OPS-014` | Detecção de jailbreak / off-policy actions em produção | — | — | ✔ | — |
| `OPS-015` | Sinais contínuos de saúde e disponibilidade operacional | — | ✔ | ✔ | — |
| `OPS-016` | Cópias de segurança com restauro testado | ▲ | ▲ | ▲ | CTX-NIS2-P16 |
| `OPS-017` | Objectivos e procedimento de recuperação da aplicação | ▲ | ▲ | ▲ | CTX-NIS2-P17 |
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
| `GOV-006` | Cláusulas de segurança proporcionais ao risco em contratos com terceiros | ▲ | ▲ | ▲ | CTX-NIS2-P08 |
| `GOV-007` | Validação formal de fornecedores antes de onboarding | ▲ | ▲ | ▲ | CTX-NIS2-P09 |
| `GOV-008` | Rastreabilidade organizacional de decisões de segurança por aplicação | — | ✔ | ✔ | — |
| `GOV-009` | Evidência de decisões rastreável, referenciável e retida | ✔ | ✔ | ✔ | — |
| `GOV-010` | Ciclo de validação contínua e revisão periódica de conformidade | — | ✔ | ✔ | — |
| `GOV-011` | KPIs de governação definidos, recolhidos e reportados | — | ✔ | ✔ | — |
| `GOV-012` | Modelo de maturidade activo com evolução medida e planeada | — | — | ✔ | — |
| `GOV-013` | Onboarding técnico e formação obrigatória pré-acesso de terceiros | — | ✔ | ✔ | — |
| `GOV-014` | Revisão periódica de acesso aos sistemas de suporte (least privilege) | ▲ | ▲ | ▲ | CTX-NIS2-P18 |
| `GOV-015` | Divulgação coordenada de vulnerabilidades com canal de receção publicado | ▲ | ▲ | ▲ | CTX-NIS2-P14, CTX-NIS2-P15 |
| `GOV-016` | Contas privilegiadas e de administração dos sistemas de suporte | ▲ | ▲ | ▲ | CTX-NIS2-P13 |
| `GOV-017` | Ciclo de vida das identidades com acesso aos sistemas | ▲ | ▲ | ▲ | CTX-NIS2-P19 |
| `CTX-NIS2-R01` | Redundância pelo menos parcial | ▲ | ▲ | ▲ | — |
| `CTX-NIS2-R02` | Critério de incidente significativo | ▲ | ▲ | ▲ | — |
| `CTX-NIS2-R03` | Limiares de incidente significativo e agregação dos recorrentes | ▲ | ▲ | ▲ | — |

## Obrigações do regime por força de cobertura {#forca}

Contagem das obrigações da matriz `_matriz/nis2.yaml` (excluídas as dirigidas às autoridades). A secção [«O que este Manual cobre e o que fica de fora»](#cobertura) lista-as.

| Força | Obrigações |
|---|--:|
| Cobre | 98 |
| Parcial | 57 |
| Apoia evidência | 12 |
| Lacuna | 10 |
| Fora de âmbito | 43 |

## O que este Manual cobre e o que fica de fora {#cobertura}

Todas as obrigações da matriz `_matriz/nis2.yaml` em três categorias: o que o Manual **cobre**, e de que forma; as **lacunas declaradas** (o que não cobre por omissão); e o que fica **fora de âmbito**, com a razão. Gerado da matriz; nenhuma obrigação fica em silêncio. As 8 obrigações dirigidas às autoridades não criam dever para a organização e não entram nas listas.

### Cobre (110) {#cobre}

Força «cobre» ou «apoia evidência». A forma é a resposta do Manual: requisito do catálogo, política, secção, piso ou requisito acrescentado pelo regime.

| Obrigação | Referência | Força | Forma |
|---|---|---|---|
| NIS2-21-2-a | Art. 21.º, n.º 2, al. a) | Cobre | `CLA-001`; [Política 02 §3](/sbd-toe/assets/policies/policy-classificacao-risco#3-modelo-de-classificação---eixos-edi); `THR-001`; [Política 03 §5](/sbd-toe/assets/policies/policy-aceitacao-risco#5-limiares-de-aceitação-por-nível) |
| NIS2-21-2-b | Art. 21.º, n.º 2, al. b) | Cobre | [Política 32 §2](/sbd-toe/assets/policies/policy-irp#2-âmbito-e-obrigatoriedade); [Política 32 §2](/sbd-toe/assets/policies/policy-irp#2-âmbito-e-obrigatoriedade); [Política 32 §3](/sbd-toe/assets/policies/policy-irp#3-critérios-de-activação-do-irp); [Política 32 §5](/sbd-toe/assets/policies/policy-irp#5-playbooks-de-resposta); `OPS-007` |
| NIS2-21-2-d | Art. 21.º, n.º 2, al. d) | Cobre | `GOV-006`; `GOV-007`; [Política 33 §3.2](/sbd-toe/assets/policies/policy-contratacao-segura#32-resultado-da-due-diligence); `DEP-006`; `DEP-001` |
| NIS2-21-2-e | Art. 21.º, n.º 2, al. e) | Cobre | `REQ-001`; `DEV-001`; `TST-001`; `DEP-002`; [Política 19 §4.3](/sbd-toe/assets/policies/policy-estrategia-testes#43-slas-de-triagem-e-resolução); `GOV-015` |
| NIS2-21-2-f | Art. 21.º, n.º 2, al. f) | Cobre | [Política 35 §7](/sbd-toe/assets/policies/policy-kpis-governacao#7-avaliação-de-maturidade); `OPS-010`; `GOV-011`; [Política 34 §5.2](/sbd-toe/assets/policies/policy-rastreabilidade-organizacional#52-processo-de-validação) |
| NIS2-21-2-h | Art. 21.º, n.º 2, al. h) | Cobre | `ENC-001`; `ENC-003`; [Política 18 §4](/sbd-toe/assets/policies/policy-gestao-segredos#4-armazenamento-centralizado); [Política 18 §6.1](/sbd-toe/assets/policies/policy-gestao-segredos#61-ttl-por-tipo-de-segredo) |
| NIS2-21-4 | Art. 21.º, n.º 4 | Cobre | `GOV-010`; [Política 34 §5.2](/sbd-toe/assets/policies/policy-rastreabilidade-organizacional#52-processo-de-validação); `GOV-004` |
| NIS2-23-1-1 | Art. 23.º, n.º 1, 1.º par. (1.º per.) | Cobre | [Política 32 §2](/sbd-toe/assets/policies/policy-irp#2-âmbito-e-obrigatoriedade); [Política 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória); [Política 32 §4.1](/sbd-toe/assets/policies/policy-irp#41-triagem-t0----15-minutos-de-detecção) |
| NIS2-23-1-3 | Art. 23.º, n.º 1, 1.º par. (3.º per.) | Cobre | [Política 32 §6.1](/sbd-toe/assets/policies/policy-irp#61-critério-e-conteúdo-mínimo-por-regime) |
| NIS2-23-3 | Art. 23.º, n.º 3 | Cobre | `CTX-NIS2-R02`; [Política 32 §4.3](/sbd-toe/assets/policies/policy-irp#43-investigação); [Política 32 §4.1](/sbd-toe/assets/policies/policy-irp#41-triagem-t0----15-minutos-de-detecção); [Política 32 §4.1](/sbd-toe/assets/policies/policy-irp#41-triagem-t0----15-minutos-de-detecção) |
| NIS2-23-4-a | Art. 23.º, n.º 4, al. a) | Cobre | [Política 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória); [Política 32 §6.1](/sbd-toe/assets/policies/policy-irp#61-critério-e-conteúdo-mínimo-por-regime) |
| NIS2-23-4-b | Art. 23.º, n.º 4, al. b) | Cobre | [Política 32 §6.1](/sbd-toe/assets/policies/policy-irp#61-critério-e-conteúdo-mínimo-por-regime); [Política 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória); [Política 32 §4.3](/sbd-toe/assets/policies/policy-irp#43-investigação) |
| NIS2-23-4-c | Art. 23.º, n.º 4, al. c) | Cobre | [Política 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória) |
| NIS2-23-4-d | Art. 23.º, n.º 4, al. d) | Cobre | [Política 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória); [Política 32 §4.3](/sbd-toe/assets/policies/policy-irp#43-investigação); [Política 32 §4.6](/sbd-toe/assets/policies/policy-irp#46-post-mortem); [Política 32 §6.1](/sbd-toe/assets/policies/policy-irp#61-critério-e-conteúdo-mínimo-por-regime) |
| NIS2-23-4-e | Art. 23.º, n.º 4, al. e) | Cobre | [Política 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória) |
| NIS2-23-4-2par | Art. 23.º, n.º 4, 2.º par. | Cobre | [Política 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória) |
| NIS2-32-2-eg | Art. 32.º, n.º 2, als. e)–g); art. 33.º, n.º 2, als. d)–f) | Apoia evidência | [Política 34 §7](/sbd-toe/assets/policies/policy-rastreabilidade-organizacional#7-evidência-auditável); `GOV-009`; [Política 06 §10](/sbd-toe/assets/policies/policy-rastreabilidade#10-prazos-de-retenção-mínimos) |
| NIS2-32-4-d | Art. 32.º, n.º 4, als. b), d), f); art. 33.º, n.º 4, als. b), d), f) | Apoia evidência | `GOV-010`; [Política 34 §5.2](/sbd-toe/assets/policies/policy-rastreabilidade-organizacional#52-processo-de-validação) |
| NIS2-IR2690-art3 | Reg. Exec. (UE) 2024/2690, art. 3.º | Cobre | `CTX-NIS2-R03`; [Política 32 §4.1](/sbd-toe/assets/policies/policy-irp#41-triagem-t0----15-minutos-de-detecção) |
| NIS2-IR2690-art4 | Reg. Exec. (UE) 2024/2690, art. 4.º | Cobre | `CTX-NIS2-R03` |
| NIS2-IR2690-art5 | Reg. Exec. (UE) 2024/2690, art. 5.º | Apoia evidência | `OPS-015`; [Política 32 §4.1](/sbd-toe/assets/policies/policy-irp#41-triagem-t0----15-minutos-de-detecção) |
| NIS2-IR2690-art6 | Reg. Exec. (UE) 2024/2690, art. 6.º | Apoia evidência | `OPS-015`; [Política 32 §4.1](/sbd-toe/assets/policies/policy-irp#41-triagem-t0----15-minutos-de-detecção) |
| NIS2-IR2690-art7 | Reg. Exec. (UE) 2024/2690, art. 7.º | Apoia evidência | `OPS-015`; [Política 32 §4.1](/sbd-toe/assets/policies/policy-irp#41-triagem-t0----15-minutos-de-detecção) |
| NIS2-IR2690-art8 | Reg. Exec. (UE) 2024/2690, art. 8.º | Apoia evidência | `OPS-015`; [Política 32 §4.1](/sbd-toe/assets/policies/policy-irp#41-triagem-t0----15-minutos-de-detecção) |
| NIS2-IR2690-art9 | Reg. Exec. (UE) 2024/2690, art. 9.º | Apoia evidência | `OPS-015`; [Política 32 §4.1](/sbd-toe/assets/policies/policy-irp#41-triagem-t0----15-minutos-de-detecção) |
| NIS2-IR2690-art10 | Reg. Exec. (UE) 2024/2690, art. 10.º | Apoia evidência | `OPS-015`; [Política 32 §4.1](/sbd-toe/assets/policies/policy-irp#41-triagem-t0----15-minutos-de-detecção) |
| NIS2-IR2690-art11 | Reg. Exec. (UE) 2024/2690, art. 11.º | Apoia evidência | `OPS-015`; [Política 32 §4.1](/sbd-toe/assets/policies/policy-irp#41-triagem-t0----15-minutos-de-detecção) |
| NIS2-IR2690-art12 | Reg. Exec. (UE) 2024/2690, art. 12.º | Apoia evidência | `OPS-015`; [Política 32 §4.1](/sbd-toe/assets/policies/policy-irp#41-triagem-t0----15-minutos-de-detecção) |
| NIS2-IR2690-art13 | Reg. Exec. (UE) 2024/2690, art. 13.º | Apoia evidência | `OPS-015`; [Política 32 §4.1](/sbd-toe/assets/policies/policy-irp#41-triagem-t0----15-minutos-de-detecção) |
| NIS2-IR2690-art14 | Reg. Exec. (UE) 2024/2690, art. 14.º | Apoia evidência | `OPS-015`; [Política 32 §4.1](/sbd-toe/assets/policies/policy-irp#41-triagem-t0----15-minutos-de-detecção) |
| NIS2-IR2690-1.2.1 | Reg. Exec. (UE) 2024/2690, anexo, ponto 1.2.1 (artigo 21.o, n.o 2, alínea a), da Diretiva (UE) 2022/2555) | Cobre | `GOV-001`; `GOV-002` |
| NIS2-IR2690-1.2.2 | Reg. Exec. (UE) 2024/2690, anexo, ponto 1.2.2 (artigo 21.o, n.o 2, alínea a), da Diretiva (UE) 2022/2555) | Cobre | `TRN-002`; `GOV-006`; `TRN-007` |
| NIS2-IR2690-1.2.4 | Reg. Exec. (UE) 2024/2690, anexo, ponto 1.2.4 (artigo 21.o, n.o 2, alínea a), da Diretiva (UE) 2022/2555) | Cobre | `GOV-002`; `TRN-008` |
| NIS2-IR2690-1.2.6 | Reg. Exec. (UE) 2024/2690, anexo, ponto 1.2.6 (artigo 21.o, n.o 2, alínea a), da Diretiva (UE) 2022/2555) | Cobre | [Política 32 §4.6](/sbd-toe/assets/policies/policy-irp#46-post-mortem); `GOV-001` |
| NIS2-IR2690-2.1.4 | Reg. Exec. (UE) 2024/2690, anexo, ponto 2.1.4 (artigo 21.o, n.o 2, alínea a), da Diretiva (UE) 2022/2555) | Cobre | [Política 32 §4.6](/sbd-toe/assets/policies/policy-irp#46-post-mortem); `CLA-005`; [Política 04 §3.1](/sbd-toe/assets/policies/policy-revisao-periodica-risco#31-cadências-mínimas-obrigatórias); [Política 04 §4.1](/sbd-toe/assets/policies/policy-revisao-periodica-risco#41-triggers-que-obrigam-a-revisão-imediata); `THR-006` |
| NIS2-IR2690-2.2.1 | Reg. Exec. (UE) 2024/2690, anexo, ponto 2.2.1 (artigo 21.o, n.o 2, alínea a), da Diretiva (UE) 2022/2555) | Cobre | [Política 34 §5.2](/sbd-toe/assets/policies/policy-rastreabilidade-organizacional#52-processo-de-validação); `GOV-011`; [Política 35 §5](/sbd-toe/assets/policies/policy-kpis-governacao#5-cadência-de-recolha-e-reporte) |
| NIS2-IR2690-2.2.2 | Reg. Exec. (UE) 2024/2690, anexo, ponto 2.2.2 (artigo 21.o, n.o 2, alínea a), da Diretiva (UE) 2022/2555) | Cobre | [Política 35 §5](/sbd-toe/assets/policies/policy-kpis-governacao#5-cadência-de-recolha-e-reporte); `GOV-011` |
| NIS2-IR2690-2.2.3 | Reg. Exec. (UE) 2024/2690, anexo, ponto 2.2.3 (artigo 21.o, n.o 2, alínea a), da Diretiva (UE) 2022/2555) | Cobre | [Política 32 §4.6](/sbd-toe/assets/policies/policy-irp#46-post-mortem); [Política 34 §5.1](/sbd-toe/assets/policies/policy-rastreabilidade-organizacional#51-cadência-de-validação) |
| NIS2-IR2690-3.1.1 | Reg. Exec. (UE) 2024/2690, anexo, ponto 3.1.1 (artigo 21.o, n.o 2, alínea b), da Diretiva (UE) 2022/2555) | Cobre | [Política 32 §2](/sbd-toe/assets/policies/policy-irp#2-âmbito-e-obrigatoriedade); [Política 32 §2](/sbd-toe/assets/policies/policy-irp#2-âmbito-e-obrigatoriedade); [Política 32 §3](/sbd-toe/assets/policies/policy-irp#3-critérios-de-activação-do-irp); [Política 32 §9](/sbd-toe/assets/policies/policy-irp#9-responsabilidades) |
| NIS2-IR2690-3.1.3 | Reg. Exec. (UE) 2024/2690, anexo, ponto 3.1.3 (artigo 21.o, n.o 2, alínea b), da Diretiva (UE) 2022/2555) | Cobre | [Política 32 §8](/sbd-toe/assets/policies/policy-irp#8-testes-periódicos-do-irp); [Política 32 §10](/sbd-toe/assets/policies/policy-irp#10-revisão-e-auditoria-desta-política) |
| NIS2-IR2690-3.2.1 | Reg. Exec. (UE) 2024/2690, anexo, ponto 3.2.1 (artigo 21.o, n.o 2, alínea b), da Diretiva (UE) 2022/2555) | Cobre | `LOG-001`; `OPS-001`; `OPS-002`; [Política 29 §4](/sbd-toe/assets/policies/policy-logging-estruturado#4-eventos-de-segurança-obrigatórios) |
| NIS2-IR2690-3.2.2 | Reg. Exec. (UE) 2024/2690, anexo, ponto 3.2.2 (artigo 21.o, n.o 2, alínea b), da Diretiva (UE) 2022/2555) | Cobre | `OPS-005`; [Política 30 §7](/sbd-toe/assets/policies/policy-monitorizacao-seguranca#7-validação-e-tuning-de-regras-de-detecção) |
| NIS2-IR2690-3.2.7 | Reg. Exec. (UE) 2024/2690, anexo, ponto 3.2.7 (artigo 21.o, n.o 2, alínea b), da Diretiva (UE) 2022/2555) | Cobre | [Política 29 §10](/sbd-toe/assets/policies/policy-logging-estruturado#10-revisão-e-auditoria-desta-política); `OPS-002`; [Política 30 §8](/sbd-toe/assets/policies/policy-monitorizacao-seguranca#8-revisão-periódica-de-cobertura) |
| NIS2-IR2690-3.4.1 | Reg. Exec. (UE) 2024/2690, anexo, ponto 3.4.1 (artigo 21.o, n.o 2, alínea b), da Diretiva (UE) 2022/2555) | Cobre | [Política 32 §3](/sbd-toe/assets/policies/policy-irp#3-critérios-de-activação-do-irp); [Política 32 §4.1](/sbd-toe/assets/policies/policy-irp#41-triagem-t0----15-minutos-de-detecção) |
| NIS2-IR2690-3.4.2 | Reg. Exec. (UE) 2024/2690, anexo, ponto 3.4.2 (artigo 21.o, n.o 2, alínea b), da Diretiva (UE) 2022/2555) | Cobre | `CTX-NIS2-R03`; [Política 31 §3](/sbd-toe/assets/policies/policy-gestao-alertas#3-classificação-de-alertas); [Política 32 §4.3](/sbd-toe/assets/policies/policy-irp#43-investigação); `OPS-008` |
| NIS2-IR2690-3.5.1 | Reg. Exec. (UE) 2024/2690, anexo, ponto 3.5.1 (artigo 21.o, n.o 2, alínea b), da Diretiva (UE) 2022/2555) | Cobre | [Política 32 §5](/sbd-toe/assets/policies/policy-irp#5-playbooks-de-resposta); `OPS-006` |
| NIS2-IR2690-3.5.2 | Reg. Exec. (UE) 2024/2690, anexo, ponto 3.5.2 (artigo 21.o, n.o 2, alínea b), da Diretiva (UE) 2022/2555) | Cobre | [Política 32 §4.2](/sbd-toe/assets/policies/policy-irp#42-contenção-t1---início-imediato-após-confirmação); [Política 32 §4.4](/sbd-toe/assets/policies/policy-irp#44-erradicação); [Política 32 §4.5](/sbd-toe/assets/policies/policy-irp#45-recuperação) |
| NIS2-IR2690-3.5.3 | Reg. Exec. (UE) 2024/2690, anexo, ponto 3.5.3 (artigo 21.o, n.o 2, alínea b), da Diretiva (UE) 2022/2555) | Cobre | [Política 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória); [Política 32 §7](/sbd-toe/assets/policies/policy-irp#7-comunicação-durante-o-incidente); [Política 32 §9](/sbd-toe/assets/policies/policy-irp#9-responsabilidades) |
| NIS2-IR2690-3.5.4 | Reg. Exec. (UE) 2024/2690, anexo, ponto 3.5.4 (artigo 21.o, n.o 2, alínea b), da Diretiva (UE) 2022/2555) | Cobre | [Política 32 §4.2](/sbd-toe/assets/policies/policy-irp#42-contenção-t1---início-imediato-após-confirmação); [Política 32 §4.2](/sbd-toe/assets/policies/policy-irp#42-contenção-t1---início-imediato-após-confirmação); `DPL-004` |
| NIS2-IR2690-3.5.5 | Reg. Exec. (UE) 2024/2690, anexo, ponto 3.5.5 (artigo 21.o, n.o 2, alínea b), da Diretiva (UE) 2022/2555) | Cobre | [Política 32 §8](/sbd-toe/assets/policies/policy-irp#8-testes-periódicos-do-irp); `OPS-007`; [Cap. 12 US-17](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle#us-17---exercícios-de-resposta-a-incidentes-end-to-end) |
| NIS2-IR2690-3.6.1 | Reg. Exec. (UE) 2024/2690, anexo, ponto 3.6.1 (artigo 21.o, n.o 2, alínea b), da Diretiva (UE) 2022/2555) | Cobre | [Política 32 §4.6](/sbd-toe/assets/policies/policy-irp#46-post-mortem); [Política 32 §4.3](/sbd-toe/assets/policies/policy-irp#43-investigação) |
| NIS2-IR2690-3.6.2 | Reg. Exec. (UE) 2024/2690, anexo, ponto 3.6.2 (artigo 21.o, n.o 2, alínea b), da Diretiva (UE) 2022/2555) | Cobre | [Política 32 §4.6](/sbd-toe/assets/policies/policy-irp#46-post-mortem); `CLA-006`; `TRN-006`; [Política 32 §10](/sbd-toe/assets/policies/policy-irp#10-revisão-e-auditoria-desta-política) |
| NIS2-IR2690-3.6.3 | Reg. Exec. (UE) 2024/2690, anexo, ponto 3.6.3 (artigo 21.o, n.o 2, alínea b), da Diretiva (UE) 2022/2555) | Cobre | [Política 35 §3.3](/sbd-toe/assets/policies/policy-kpis-governacao#33-operações-e-resposta-a-incidentes) |
| NIS2-IR2690-4.1.2 | Reg. Exec. (UE) 2024/2690, anexo, ponto 4.1.2 (artigo 21.o, n.o 2, alínea c), da Diretiva (UE) 2022/2555) | Cobre | `OPS-017` |
| NIS2-IR2690-4.2.1 | Reg. Exec. (UE) 2024/2690, anexo, ponto 4.2.1 (artigo 21.o, n.o 2, alínea c), da Diretiva (UE) 2022/2555) | Cobre | `OPS-016`; `CTX-NIS2-R01` |
| NIS2-IR2690-4.2.2 | Reg. Exec. (UE) 2024/2690, anexo, ponto 4.2.2 (artigo 21.o, n.o 2, alínea c), da Diretiva (UE) 2022/2555) | Cobre | `OPS-016` |
| NIS2-IR2690-4.2.3 | Reg. Exec. (UE) 2024/2690, anexo, ponto 4.2.3 (artigo 21.o, n.o 2, alínea c), da Diretiva (UE) 2022/2555) | Cobre | `OPS-016` |
| NIS2-IR2690-4.2.4 | Reg. Exec. (UE) 2024/2690, anexo, ponto 4.2.4 (artigo 21.o, n.o 2, alínea c), da Diretiva (UE) 2022/2555) | Cobre | `CTX-NIS2-R01` |
| NIS2-IR2690-4.2.5 | Reg. Exec. (UE) 2024/2690, anexo, ponto 4.2.5 (artigo 21.o, n.o 2, alínea c), da Diretiva (UE) 2022/2555) | Cobre | `CTX-NIS2-R01` |
| NIS2-IR2690-4.2.6 | Reg. Exec. (UE) 2024/2690, anexo, ponto 4.2.6 (artigo 21.o, n.o 2, alínea c), da Diretiva (UE) 2022/2555) | Cobre | `OPS-016` |
| NIS2-IR2690-5.1.5 | Reg. Exec. (UE) 2024/2690, anexo, ponto 5.1.5 (artigo 21.o, n.o 2, alínea d), da Diretiva (UE) 2022/2555) | Cobre | [Política 33 §3.2](/sbd-toe/assets/policies/policy-contratacao-segura#32-resultado-da-due-diligence) |
| NIS2-IR2690-5.1.6 | Reg. Exec. (UE) 2024/2690, anexo, ponto 5.1.6 (artigo 21.o, n.o 2, alínea d), da Diretiva (UE) 2022/2555) | Cobre | [Política 33 §6.2](/sbd-toe/assets/policies/policy-contratacao-segura#62-reavaliação-periódica); `GOV-010` |
| NIS2-IR2690-5.1.7 | Reg. Exec. (UE) 2024/2690, anexo, ponto 5.1.7 (artigo 21.o, n.o 2, alínea d), da Diretiva (UE) 2022/2555) | Cobre | [Política 33 §6.1](/sbd-toe/assets/policies/policy-contratacao-segura#61-indicadores-de-conformidade-a-monitorizar); [Política 33 §6.1](/sbd-toe/assets/policies/policy-contratacao-segura#61-indicadores-de-conformidade-a-monitorizar); `GOV-010`; [Política 33 §10.4](/sbd-toe/assets/policies/policy-contratacao-segura#104-sla-de-notificação-prévia) |
| NIS2-IR2690-6.1.3 | Reg. Exec. (UE) 2024/2690, anexo, ponto 6.1.3 (artigo 21.o, n.o 2, alínea e), da Diretiva (UE) 2022/2555) | Cobre | [Política 32 §4.6](/sbd-toe/assets/policies/policy-irp#46-post-mortem); [Política 33 §4.3](/sbd-toe/assets/policies/policy-contratacao-segura#43-modelo-contratual-de-referência) |
| NIS2-IR2690-6.2.1 | Reg. Exec. (UE) 2024/2690, anexo, ponto 6.2.1 (artigo 21.o, n.o 2, alínea e), da Diretiva (UE) 2022/2555) | Cobre | `REQ-001`; `DEV-001`; `TST-001`; `CIC-001` |
| NIS2-IR2690-6.2.2 | Reg. Exec. (UE) 2024/2690, anexo, ponto 6.2.2 (artigo 21.o, n.o 2, alínea e), da Diretiva (UE) 2022/2555) | Cobre | `REQ-002`; [Política 09 §3](/sbd-toe/assets/policies/policy-arquitetura-segura#3-princípios-de-arquitetura-segura); `DEV-001`; `IDE-006`; `CIC-006`; `TST-001`; [Política 25 §6](/sbd-toe/assets/policies/policy-deploy-seguro#6-separação-de-ambientes-e-dados); [Cap. 10 US-19](/sbd-toe/sbd-manual/testes-seguranca/aplicacao-lifecycle#us-19---proteção-dos-ativos-do-processo-de-teste) |
| NIS2-IR2690-6.2.4 | Reg. Exec. (UE) 2024/2690, anexo, ponto 6.2.4 (artigo 21.o, n.o 2, alínea e), da Diretiva (UE) 2022/2555) | Cobre | `DEV-001` |
| NIS2-IR2690-6.3.1 | Reg. Exec. (UE) 2024/2690, anexo, ponto 6.3.1 (artigo 21.o, n.o 2, alínea e), da Diretiva (UE) 2022/2555) | Cobre | `CFG-001`; `IAC-003`; `CNT-009`; [Política 21 §3](/sbd-toe/assets/policies/policy-iac-seguro#3-princípios-de-iac-seguro) |
| NIS2-IR2690-6.4.1 | Reg. Exec. (UE) 2024/2690, anexo, ponto 6.4.1 (artigo 21.o, n.o 2, alínea e), da Diretiva (UE) 2022/2555) | Cobre | `DPL-001`; `IAC-007`; `CIC-001` |
| NIS2-IR2690-6.4.3 | Reg. Exec. (UE) 2024/2690, anexo, ponto 6.4.3 (artigo 21.o, n.o 2, alínea e), da Diretiva (UE) 2022/2555) | Cobre | [Emergency deploy - break glass](/sbd-toe/sbd-manual/deploy-seguro/addon/excecoes-deploy#emergency-deploy---break-glass); [Política 26 §7](/sbd-toe/assets/policies/policy-aprovacao-release#7-releases-de-emergência) |
| NIS2-IR2690-6.4.4 | Reg. Exec. (UE) 2024/2690, anexo, ponto 6.4.4 (artigo 21.o, n.o 2, alínea e), da Diretiva (UE) 2022/2555) | Cobre | [Política 26 §9](/sbd-toe/assets/policies/policy-aprovacao-release#9-revisão-e-auditoria-desta-política) |
| NIS2-IR2690-6.5.1 | Reg. Exec. (UE) 2024/2690, anexo, ponto 6.5.1 (artigo 21.o, n.o 2, alínea e), da Diretiva (UE) 2022/2555) | Cobre | `TST-001` |
| NIS2-IR2690-6.5.2 | Reg. Exec. (UE) 2024/2690, anexo, ponto 6.5.2 (artigo 21.o, n.o 2, alínea e), da Diretiva (UE) 2022/2555) | Cobre | `TST-001`; `TST-004`; `TST-003`; `TST-008` |
| NIS2-IR2690-6.5.3 | Reg. Exec. (UE) 2024/2690, anexo, ponto 6.5.3 (artigo 21.o, n.o 2, alínea e), da Diretiva (UE) 2022/2555) | Cobre | `TST-001` |
| NIS2-IR2690-6.6.2 | Reg. Exec. (UE) 2024/2690, anexo, ponto 6.6.2 (artigo 21.o, n.o 2, alínea e), da Diretiva (UE) 2022/2555) | Cobre | [Política 12 §4](/sbd-toe/assets/policies/policy-excecoes-cve#4-tipos-de-exceção); `GOV-004` |
| NIS2-IR2690-6.7.1 | Reg. Exec. (UE) 2024/2690, anexo, ponto 6.7.1 (artigo 21.o, n.o 2, alínea e), da Diretiva (UE) 2022/2555) | Cobre | `ARC-006`; `ACC-005`; `ENC-001`; `CLA-003` |
| NIS2-IR2690-6.7.3 | Reg. Exec. (UE) 2024/2690, anexo, ponto 6.7.3 (artigo 21.o, n.o 2, alínea e), da Diretiva (UE) 2022/2555) | Cobre | [Política 32 §4.6](/sbd-toe/assets/policies/policy-irp#46-post-mortem); `ARC-009`; `ARC-010` |
| NIS2-IR2690-6.8.1 | Reg. Exec. (UE) 2024/2690, anexo, ponto 6.8.1 (artigo 21.o, n.o 2, alínea e), da Diretiva (UE) 2022/2555) | Cobre | `ARC-001`; `ARC-006`; [Política 09 §3](/sbd-toe/assets/policies/policy-arquitetura-segura#3-princípios-de-arquitetura-segura) |
| NIS2-IR2690-6.8.3 | Reg. Exec. (UE) 2024/2690, anexo, ponto 6.8.3 (artigo 21.o, n.o 2, alínea e), da Diretiva (UE) 2022/2555) | Cobre | [Política 32 §4.6](/sbd-toe/assets/policies/policy-irp#46-post-mortem); `ARC-009`; `ARC-010` |
| NIS2-IR2690-6.10.1 | Reg. Exec. (UE) 2024/2690, anexo, ponto 6.10.1 (artigo 21.o, n.o 2, alínea e), da Diretiva (UE) 2022/2555) | Cobre | `DEP-002`; `CNT-002`; [Política 11 §7](/sbd-toe/assets/policies/policy-sbom#7-inventário-em-produção); [Política 10 §8](/sbd-toe/assets/policies/policy-dependencias#8-alertas-de-vulnerabilidades-em-produção) |
| NIS2-IR2690-6.10.2 | Reg. Exec. (UE) 2024/2690, anexo, ponto 6.10.2 (artigo 21.o, n.o 2, alínea e), da Diretiva (UE) 2022/2555) | Cobre | [Política 10 §8](/sbd-toe/assets/policies/policy-dependencias#8-alertas-de-vulnerabilidades-em-produção); [KEV — exploração confirmada](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/epss-kev-priorizacao#kev--exploração-confirmada); [Política 19 §4.3](/sbd-toe/assets/policies/policy-estrategia-testes#43-slas-de-triagem-e-resolução); `DEP-010`; `GOV-015`; `DEP-010` |
| NIS2-IR2690-6.10.3 | Reg. Exec. (UE) 2024/2690, anexo, ponto 6.10.3 (artigo 21.o, n.o 2, alínea e), da Diretiva (UE) 2022/2555) | Cobre | [Política 12 §4](/sbd-toe/assets/policies/policy-excecoes-cve#4-tipos-de-exceção); `DEP-010`; `GOV-004` |
| NIS2-IR2690-7.1 | Reg. Exec. (UE) 2024/2690, anexo, ponto 7.1 (artigo 21.o, n.o 2, alínea f), da Diretiva (UE) 2022/2555) | Cobre | [Política 35 §7](/sbd-toe/assets/policies/policy-kpis-governacao#7-avaliação-de-maturidade); `OPS-010`; `GOV-011` |
| NIS2-IR2690-7.2 | Reg. Exec. (UE) 2024/2690, anexo, ponto 7.2 (artigo 21.o, n.o 2, alínea f), da Diretiva (UE) 2022/2555) | Cobre | [Política 35 §4](/sbd-toe/assets/policies/policy-kpis-governacao#4-fontes-de-dados-e-recolha); [Política 35 §5](/sbd-toe/assets/policies/policy-kpis-governacao#5-cadência-de-recolha-e-reporte) |
| NIS2-IR2690-7.3 | Reg. Exec. (UE) 2024/2690, anexo, ponto 7.3 (artigo 21.o, n.o 2, alínea f), da Diretiva (UE) 2022/2555) | Cobre | [Política 32 §4.6](/sbd-toe/assets/policies/policy-irp#46-post-mortem); [Política 35 §10](/sbd-toe/assets/policies/policy-kpis-governacao#10-revisão-e-auditoria-desta-política) |
| NIS2-IR2690-8.1.3 | Reg. Exec. (UE) 2024/2690, anexo, ponto 8.1.3 (artigo 21.o, n.o 2, alínea g), da Diretiva (UE) 2022/2555) | Cobre | `TRN-003`; `TRN-009`; [Política 37 §7](/sbd-toe/assets/policies/policy-formacao-seguranca#7-actualização-de-conteúdos-formativos) |
| NIS2-IR2690-8.2.1 | Reg. Exec. (UE) 2024/2690, anexo, ponto 8.2.1 (artigo 21.o, n.o 2, alínea g), da Diretiva (UE) 2022/2555) | Cobre | `TRN-001`; `TRN-001`; `TRN-005` |
| NIS2-IR2690-8.2.2 | Reg. Exec. (UE) 2024/2690, anexo, ponto 8.2.2 (artigo 21.o, n.o 2, alínea g), da Diretiva (UE) 2022/2555) | Cobre | `TRN-001` |
| NIS2-IR2690-8.2.3 | Reg. Exec. (UE) 2024/2690, anexo, ponto 8.2.3 (artigo 21.o, n.o 2, alínea g), da Diretiva (UE) 2022/2555) | Cobre | `TRN-003`; [Política 37 §3.1](/sbd-toe/assets/policies/policy-formacao-seguranca#31-conteúdos-mínimos-de-onboarding); [Política 37 §8](/sbd-toe/assets/policies/policy-formacao-seguranca#8-kpis-de-eficácia-formativa) |
| NIS2-IR2690-8.2.5 | Reg. Exec. (UE) 2024/2690, anexo, ponto 8.2.5 (artigo 21.o, n.o 2, alínea g), da Diretiva (UE) 2022/2555) | Cobre | `TRN-006`; [Política 37 §7](/sbd-toe/assets/policies/policy-formacao-seguranca#7-actualização-de-conteúdos-formativos) |
| NIS2-IR2690-9.1 | Reg. Exec. (UE) 2024/2690, anexo, ponto 9.1 (artigo 21.o, n.o 2, alínea h), da Diretiva (UE) 2022/2555) | Cobre | `ENC-001`; `ENC-003`; `ENC-009`; [Política 18 §4](/sbd-toe/assets/policies/policy-gestao-segredos#4-armazenamento-centralizado) |
| NIS2-IR2690-9.2 | Reg. Exec. (UE) 2024/2690, anexo, ponto 9.2 (artigo 21.o, n.o 2, alínea h), da Diretiva (UE) 2022/2555) | Cobre | `ENC-007`; `ENC-003`; `ENC-003`; `ENC-002`; `ENC-007`; [Política 18 §6.1](/sbd-toe/assets/policies/policy-gestao-segredos#61-ttl-por-tipo-de-segredo); [Política 18 §6.3](/sbd-toe/assets/policies/policy-gestao-segredos#63-revogação-por-exposição-suspeita) |
| NIS2-IR2690-9.3 | Reg. Exec. (UE) 2024/2690, anexo, ponto 9.3 (artigo 21.o, n.o 2, alínea h), da Diretiva (UE) 2022/2555) | Cobre | `ENC-003`; [Política 18 §11](/sbd-toe/assets/policies/policy-gestao-segredos#11-revisão-e-auditoria-desta-política) |
| NIS2-IR2690-11.1.2 | Reg. Exec. (UE) 2024/2690, anexo, ponto 11.1.2 (artigo 21.o, n.o 2, alíneas i) e j), da Diretiva (UE) 2022/2555) | Cobre | `ACC-005`; `INT-002`; `ARC-015` |
| NIS2-IR2690-11.2.1 | Reg. Exec. (UE) 2024/2690, anexo, ponto 11.2.1 (artigo 21.o, n.o 2, alíneas i) e j), da Diretiva (UE) 2022/2555) | Cobre | `ACC-008`; `GOV-014`; [Política 33 §7.1](/sbd-toe/assets/policies/policy-contratacao-segura#71-checklist-de-offboarding); `GOV-017` |
| NIS2-IR2690-11.2.2 | Reg. Exec. (UE) 2024/2690, anexo, ponto 11.2.2 (artigo 21.o, n.o 2, alíneas i) e j), da Diretiva (UE) 2022/2555) | Cobre | `ACC-002`; `ACC-004`; `GOV-014`; [Política 33 §7.1](/sbd-toe/assets/policies/policy-contratacao-segura#71-checklist-de-offboarding); `ACC-003` |
| NIS2-IR2690-11.2.3 | Reg. Exec. (UE) 2024/2690, anexo, ponto 11.2.3 (artigo 21.o, n.o 2, alíneas i) e j), da Diretiva (UE) 2022/2555) | Cobre | `ACC-010`; `GOV-014`; `ACC-010`; `GOV-014` |
| NIS2-IR2690-11.3.1 | Reg. Exec. (UE) 2024/2690, anexo, ponto 11.3.1 (artigo 21.o, n.o 2, alíneas i) e j), da Diretiva (UE) 2022/2555) | Cobre | `GOV-016` |
| NIS2-IR2690-11.3.2 | Reg. Exec. (UE) 2024/2690, anexo, ponto 11.3.2 (artigo 21.o, n.o 2, alíneas i) e j), da Diretiva (UE) 2022/2555) | Cobre | `ACC-004`; `AUT-001`; [🛡️ Requisitos de segurança por ambiente](/sbd-toe/sbd-manual/deploy-seguro/addon/08-segregacao-e-validacao-operacional#️-requisitos-de-segurança-por-ambiente); `GOV-016` |
| NIS2-IR2690-11.3.3 | Reg. Exec. (UE) 2024/2690, anexo, ponto 11.3.3 (artigo 21.o, n.o 2, alíneas i) e j), da Diretiva (UE) 2022/2555) | Cobre | `ACC-010`; `GOV-014` |
| NIS2-IR2690-11.4.1 | Reg. Exec. (UE) 2024/2690, anexo, ponto 11.4.1 (artigo 21.o, n.o 2, alíneas i) e j), da Diretiva (UE) 2022/2555) | Cobre | `GOV-016`; `GOV-016` |
| NIS2-IR2690-11.5.1 | Reg. Exec. (UE) 2024/2690, anexo, ponto 11.5.1 (artigo 21.o, n.o 2, alíneas i) e j), da Diretiva (UE) 2022/2555) | Cobre | `ACC-008`; [Política 33 §7.1](/sbd-toe/assets/policies/policy-contratacao-segura#71-checklist-de-offboarding); `ARC-015`; `GOV-017`; `GOV-017` |
| NIS2-IR2690-11.5.2 | Reg. Exec. (UE) 2024/2690, anexo, ponto 11.5.2 (artigo 21.o, n.o 2, alíneas i) e j), da Diretiva (UE) 2022/2555) | Cobre | `LOG-002`; `CIC-011`; [Cap. 07 US-20](/sbd-toe/sbd-manual/cicd-seguro/aplicacao-lifecycle#us-20); `ARC-015`; `GOV-017` |
| NIS2-IR2690-11.5.3 | Reg. Exec. (UE) 2024/2690, anexo, ponto 11.5.3 (artigo 21.o, n.o 2, alíneas i) e j), da Diretiva (UE) 2022/2555) | Cobre | [Cap. 07 US-20](/sbd-toe/sbd-manual/cicd-seguro/aplicacao-lifecycle#us-20); `GOV-017` |
| NIS2-IR2690-11.5.4 | Reg. Exec. (UE) 2024/2690, anexo, ponto 11.5.4 (artigo 21.o, n.o 2, alíneas i) e j), da Diretiva (UE) 2022/2555) | Cobre | `GOV-014`; `ACC-010`; [Política 33 §7.1](/sbd-toe/assets/policies/policy-contratacao-segura#71-checklist-de-offboarding); `GOV-014`; `GOV-017` |
| NIS2-IR2690-11.6.1 | Reg. Exec. (UE) 2024/2690, anexo, ponto 11.6.1 (artigo 21.o, n.o 2, alíneas i) e j), da Diretiva (UE) 2022/2555) | Cobre | `AUT-002`; `AUT-003`; `AUT-006`; `ACC-005` |
| NIS2-IR2690-11.6.2 | Reg. Exec. (UE) 2024/2690, anexo, ponto 11.6.2 (artigo 21.o, n.o 2, alíneas i) e j), da Diretiva (UE) 2022/2555) | Cobre | `AUT-002`; `AUT-003`; `AUT-005`; `AUT-006`; `SES-002`; [Política 18 §6.3](/sbd-toe/assets/policies/policy-gestao-segredos#63-revogação-por-exposição-suspeita); `ACC-004`; `AUT-011` |
| NIS2-IR2690-11.7.1 | Reg. Exec. (UE) 2024/2690, anexo, ponto 11.7.1 (artigo 21.o, n.o 2, alíneas i) e j), da Diretiva (UE) 2022/2555) | Cobre | `AUT-001`; `AUT-008`; `CLA-003` |
| NIS2-IR2690-11.7.2 | Reg. Exec. (UE) 2024/2690, anexo, ponto 11.7.2 (artigo 21.o, n.o 2, alíneas i) e j), da Diretiva (UE) 2022/2555) | Cobre | `AUT-001`; `AUT-008`; `CLA-003` |
| NIS2-IR2690-12.1.3 | Reg. Exec. (UE) 2024/2690, anexo, ponto 12.1.3 (artigo 21.o, n.o 2, alínea i), da Diretiva (UE) 2022/2555) | Cobre | `CLA-005`; `CLA-006` |

### Lacuna declarada (67) {#lacuna}

Força «parcial» ou «lacuna»: o Manual não cobre, ou cobre só em parte, e diz o que falta. As lacunas pendentes de uma ronda do AppSec Core estão marcadas com o nome da ronda.

| Obrigação | Referência | Força | Como o Manual responde | O que falta |
|---|---|---|---|---|
| NIS2-20-1 | Art. 20.º, n.º 1 | Parcial | `GOV-001`; [Cap. 14 US-22](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-22); `GOV-011`; [Política 35 §5](/sbd-toe/assets/policies/policy-kpis-governacao#5-cadência-de-recolha-e-reporte) | O Manual exige aprovação «pela direcção» do modelo de governação e das políticas e reporte de KPIs à gestão, mas não atribui ao órgão de direção a aprovação das medidas do art. 21.º como um todo, a supervisão da sua aplicação nem a responsabilização pessoal; o cross-check reconhece que «não fixa ex ante a forma jurídica exata da cadeia de aprovação». |
| NIS2-20-2 | Art. 20.º, n.º 2 | Parcial | [Política 37 §4.1](/sbd-toe/assets/policies/policy-formacao-seguranca#41-matriz-de-trilhos-por-perfil-e-nível-de-risco); `TRN-001` | Não há formação obrigatória dos membros do órgão de direção em gestão de riscos de cibersegurança: a Política 37 abrange «colaboradores com funções técnicas» e para «Gestão / Tech Lead» prevê apenas «Awareness executivo» em L1; a formação regular dos restantes trabalhadores (não técnicos) não é prescrita. |
| NIS2-21-1 | Art. 21.º, n.º 1 | Parcial | `CLA-003`; [Política 02 §3](/sbd-toe/assets/policies/policy-classificacao-risco#3-modelo-de-classificação---eixos-edi); `REQ-001` | A proporcionalidade do Manual é por aplicação (L1–L3) e cobre o ciclo de vida do software; não cobre o conjunto dos sistemas de rede e informação da entidade (rede corporativa, postos de trabalho, instalações, continuidade). |
| NIS2-21-2 | Art. 21.º, n.º 2, proémio | Parcial | `CLA-003`; [Política 09 §3](/sbd-toe/assets/policies/policy-arquitetura-segura#3-princípios-de-arquitetura-segura); `OPS-016`; `OPS-017` | Abordagem a todos os riscos: as cópias e a recuperação da aplicação estão cobertas (OPS-016, OPS-017); o ambiente físico e a continuidade da entidade ficam fora de âmbito; a ciber-higiene geral é parcial. |
| NIS2-21-2-c | Art. 21.º, n.º 2, al. c) | Parcial | `OPS-016`; `OPS-017` | A continuidade das actividades e a gestão de crises da entidade ficam fora do âmbito do Manual; a recuperação da aplicação está prescrita (OPS-016, OPS-017). |
| NIS2-21-2-g | Art. 21.º, n.º 2, al. g) | Parcial | [Política 37 §2](/sbd-toe/assets/policies/policy-formacao-seguranca#2-âmbito-e-obrigatoriedade); `TRN-002`; `TRN-007` | Formação de segurança prescrita para funções técnicas e terceiros com acesso; faltam práticas de ciber-higiene e sensibilização para todo o pessoal (não técnico) e para os órgãos de direção. |
| NIS2-21-2-i | Art. 21.º, n.º 2, al. i) | Parcial | `ACC-001`; `ACC-002`; `CLA-008`; `TRN-002` | Controlo de acessos coberto; gestão de ativos limitada ao inventário de aplicações e componentes (sem inventário de todos os ativos nem política de tratamento de ativos); segurança dos RH fora de âmbito salvo onboarding/offboarding. |
| NIS2-21-2-j | Art. 21.º, n.º 2, al. j) | Parcial | `AUT-001`; `AUT-008`; [🛡️ Requisitos de segurança por ambiente](/sbd-toe/sbd-manual/deploy-seguro/addon/08-segregacao-e-validacao-operacional#️-requisitos-de-segurança-por-ambiente); `GOV-016` | Comunicações seguras de voz, vídeo e texto e sistemas seguros de comunicações de emergência não são tratados (segurança da entidade, fora do âmbito do Manual); a MFA está prescrita para a aplicação (AUT-001) e para o acesso privilegiado aos sistemas de suporte (GOV-016). |
| NIS2-21-3 | Art. 21.º, n.º 3 | Parcial | [Política 33 §3.1](/sbd-toe/assets/policies/policy-contratacao-segura#31-critérios-de-avaliação); [Política 33 §3.1](/sbd-toe/assets/policies/policy-contratacao-segura#31-critérios-de-avaliação); `DEP-006`; `GOV-007` | A due diligence avalia o processo de gestão de vulnerabilidades e relatórios de testes do fornecedor (L2/L3), mas não a qualidade global dos produtos nem os procedimentos de desenvolvimento seguro como critério explícito, e ignora as avaliações coordenadas de riscos da UE (art. 22.º). |
| NIS2-23-1-2 | Art. 23.º, n.º 1, 1.º par. (2.º per.) | Parcial | [Política 32 §7](/sbd-toe/assets/policies/policy-irp#7-comunicação-durante-o-incidente) | Há comunicação genérica «a utilizadores afectados quando aplicável», mas a linha NIS2 da Política 32 §6 não inclui a notificação dos destinatários dos serviços (ao contrário das linhas DORA e CRA), sem prazo nem critério «suscetível de afetar negativamente a prestação». |
| NIS2-23-2 | Art. 23.º, n.º 2 | Lacuna | — | Não há dever de comunicar aos destinatários do serviço ciberameaças significativas nem as medidas que podem adotar; a Política 32 só trata incidentes. |
| NIS2-23-7 | Art. 23.º, n.º 7 | Parcial | [Política 32 §9](/sbd-toe/assets/policies/policy-irp#9-responsabilidades); [Política 32 §7](/sbd-toe/assets/policies/policy-irp#7-comunicação-durante-o-incidente) | Existe controlo de quem autoriza comunicações públicas, mas não o procedimento de informar o público quando a CSIRT/autoridade o exija. |
| NIS2-24-1 | Art. 24.º, n.º 1 | Lacuna | — | Os critérios de aquisição e de due diligence (Política 33 §3.1) não contemplam a exigência de produtos, serviços ou processos TIC certificados ao abrigo de sistemas europeus de certificação (CSA) quando o Estado-Membro o imponha. |
| NIS2-IR2690-art2 | Reg. Exec. (UE) 2024/2690, art. 2.º | Parcial | `GOV-004`; [Política 05 §3](/sbd-toe/assets/policies/policy-gestao-excecoes#3-princípios-fundamentais); `CLA-003` | A não-aplicação de controlos passa por exceção formal documentada, mas as isenções por nível (requisitos marcados «-» ou «Recomendado» em L1/L2) não são exceções e não geram a fundamentação documentada, requisito a requisito, que o art. 2.º, n.º 2, exige quando se considere não aplicável um requisito modulado. |
| NIS2-IR2690-1.1.1 | Reg. Exec. (UE) 2024/2690, anexo, ponto 1.1.1 (artigo 21.o, n.o 2, alínea a), da Diretiva (UE) 2022/2555) | Parcial | `GOV-001`; [Cap. 14 US-22](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-22); `GOV-012` | Não existe uma política de segurança dos SRI com o conteúdo mínimo do ponto 1.1.1 (abordagem, objetivos, compromisso de recursos, documentação a conservar, lista de políticas temáticas, indicadores de maturidade); há modelo de governação e corpo de políticas aprovados pela direção, com maturidade só em L3 (GOV-012). |
| NIS2-IR2690-1.1.2 | Reg. Exec. (UE) 2024/2690, anexo, ponto 1.1.2 (artigo 21.o, n.o 2, alínea a), da Diretiva (UE) 2022/2555) | Parcial | [Política 32 §4.6](/sbd-toe/assets/policies/policy-irp#46-post-mortem); `GOV-001`; [Cap. 14 US-22](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-22) | Revisão anual e após incidente significativo prescritas; falta a revisão após alterações significativas das operações ou dos riscos e a documentação do resultado pela direção. |
| NIS2-IR2690-1.2.3 | Reg. Exec. (UE) 2024/2690, anexo, ponto 1.2.3 (artigo 21.o, n.o 2, alínea a), da Diretiva (UE) 2022/2555) | Lacuna | — | O Manual refere o CISO como alçada de decisão, mas não exige designar uma pessoa que responda diretamente perante os órgãos de direção em matéria de segurança dos SRI. |
| NIS2-IR2690-1.2.5 | Reg. Exec. (UE) 2024/2690, anexo, ponto 1.2.5 (artigo 21.o, n.o 2, alínea a), da Diretiva (UE) 2022/2555) | Parcial | `CIC-008`; [Política 22 §5](/sbd-toe/assets/policies/policy-aprovacao-plan-iac#5-separação-de-funções-sod) | Separação de deveres técnica em pipelines e apply de IaC (L2/L3); não há regra organizacional de separação de áreas de responsabilidade conflituantes. |
| NIS2-IR2690-2.1.1 | Reg. Exec. (UE) 2024/2690, anexo, ponto 2.1.1 (artigo 21.o, n.o 2, alínea a), da Diretiva (UE) 2022/2555) | Parcial | `CLA-001`; `CLA-007`; [Política 03 §7](/sbd-toe/assets/policies/policy-aceitacao-risco#7-alçadas-de-aprovação) | Quadro de risco por aplicação com risco residual documentado; a aceitação do risco residual sobe no máximo ao CISO — não aos órgãos de direção — e não há plano de tratamento de riscos da entidade. |
| NIS2-IR2690-2.1.2 | Reg. Exec. (UE) 2024/2690, anexo, ponto 2.1.2 (artigo 21.o, n.o 2, alínea a), da Diretiva (UE) 2022/2555) | Parcial | [Política 02 §3](/sbd-toe/assets/policies/policy-classificacao-risco#3-modelo-de-classificação---eixos-edi); `THR-001`; `THR-004`; [Política 03 §5](/sbd-toe/assets/policies/policy-aceitacao-risco#5-limiares-de-aceitação-por-nível) | Metodologia (eixos E/D/I, STRIDE) e disposição de ameaças existem, mas o processo é por aplicação: faltam tolerância ao risco da entidade, identificação de riscos de terceiros e de pontos únicos de falha, e threat modeling em L1. |
| NIS2-IR2690-2.1.3 | Reg. Exec. (UE) 2024/2690, anexo, ponto 2.1.3 (artigo 21.o, n.o 2, alínea a), da Diretiva (UE) 2022/2555) | Parcial | [Política 19 §4.3](/sbd-toe/assets/policies/policy-estrategia-testes#43-slas-de-triagem-e-resolução); [KEV — exploração confirmada](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/epss-kev-priorizacao#kev--exploração-confirmada); `CLA-003` | Priorização por severidade, exploração (KEV/EPSS) e nível; sem custo-benefício nem ligação à análise de impacto na atividade. |
| NIS2-IR2690-2.3.1 | Reg. Exec. (UE) 2024/2690, anexo, ponto 2.3.1 (artigo 21.o, n.o 2, alínea a), da Diretiva (UE) 2022/2555) | Parcial | [Cap. 12 US-12](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle#us-12---rastreabilidade-e-conformidade-com-regulações-ssdf-nis2-iso-27001); [Cap. 14 US-22](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-22); `THR-007` | Auditorias internas e de aderência previstas; não é exigida análise independente da abordagem de gestão da segurança como um todo (pessoas, processos, tecnologias). |
| NIS2-IR2690-2.3.2 | Reg. Exec. (UE) 2024/2690, anexo, ponto 2.3.2 (artigo 21.o, n.o 2, alínea a), da Diretiva (UE) 2022/2555) | Lacuna | — | Não há requisito de competências de auditoria nem de independência hierárquica dos revisores face à área analisada (a independência só aparece no threat model — THR-007 — e em testes). |
| NIS2-IR2690-2.3.3 | Reg. Exec. (UE) 2024/2690, anexo, ponto 2.3.3 (artigo 21.o, n.o 2, alínea a), da Diretiva (UE) 2022/2555) | Parcial | [Cap. 14 US-22](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-22); `GOV-010` | Desvios geram ação corretiva; não se exige comunicar os resultados aos órgãos de direção nem a alternativa formal de aceitação do risco residual por estes. |
| NIS2-IR2690-2.3.4 | Reg. Exec. (UE) 2024/2690, anexo, ponto 2.3.4 (artigo 21.o, n.o 2, alínea a), da Diretiva (UE) 2022/2555) | Parcial | [Política 32 §4.6](/sbd-toe/assets/policies/policy-irp#46-post-mortem); [Cap. 12 US-12](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle#us-12---rastreabilidade-e-conformidade-com-regulações-ssdf-nis2-iso-27001) | Auditoria interna anual e revisão após incidente significativo; sem gatilho após alterações significativas. |
| NIS2-IR2690-3.1.2 | Reg. Exec. (UE) 2024/2690, anexo, ponto 3.1.2 (artigo 21.o, n.o 2, alínea b), da Diretiva (UE) 2022/2555) | Parcial | [Política 32 §6.1](/sbd-toe/assets/policies/policy-irp#61-critério-e-conteúdo-mínimo-por-regime); [Política 32 §3](/sbd-toe/assets/policies/policy-irp#3-critérios-de-activação-do-irp); [Política 31 §3](/sbd-toe/assets/policies/policy-gestao-alertas#3-classificação-de-alertas); [Política 32 §5](/sbd-toe/assets/policies/policy-irp#5-playbooks-de-resposta); [Política 31 §5](/sbd-toe/assets/policies/policy-gestao-alertas#5-escalonamento-automático); [Política 32 §9](/sbd-toe/assets/policies/policy-irp#9-responsabilidades) | Categorização, playbooks, escalada, funções, contactos e conteúdo mínimo das notificações existem; a coerência com o plano de continuidade da entidade fica fora de âmbito. |
| NIS2-IR2690-3.2.3 | Reg. Exec. (UE) 2024/2690, anexo, ponto 3.2.3 (artigo 21.o, n.o 2, alínea b), da Diretiva (UE) 2022/2555) | Parcial | `OPS-001`; `OPS-002`; [Política 29 §4](/sbd-toe/assets/policies/policy-logging-estruturado#4-eventos-de-segurança-obrigatórios); `LOG-002` | Catálogo de eventos e cobertura por inventário existem; o conteúdo exigido não inclui tráfego de rede de entrada e saída, execução de utilitários de sistema nem acessos a sistemas de rede (o Manual é centrado na aplicação). |
| NIS2-IR2690-3.2.4 | Reg. Exec. (UE) 2024/2690, anexo, ponto 3.2.4 (artigo 21.o, n.o 2, alínea b), da Diretiva (UE) 2022/2555) | Parcial | `LOG-004`; `LOG-007`; `OPS-005`; [6️⃣ Registo e Monitorização Essencial (Cap. 12)](/sbd-toe/sbd-manual/fundamentos/baseline#6️⃣-registo-e-monitorização-essencial-cap-12) | Análise regular de registos e alarmes automáticos com limiares só obrigatórios em L2/L3. |
| NIS2-IR2690-3.2.5 | Reg. Exec. (UE) 2024/2690, anexo, ponto 3.2.5 (artigo 21.o, n.o 2, alínea b), da Diretiva (UE) 2022/2555) | Parcial | `LOG-005`; `LOG-003`; [Política 29 §7](/sbd-toe/assets/policies/policy-logging-estruturado#7-retenção-de-logs); [Política 29 §8](/sbd-toe/assets/policies/policy-logging-estruturado#8-integridade-e-imutabilidade) | Retenção por período definido e proteção contra alteração estão no catálogo; não se prescreve cópia de segurança dos registos. |
| NIS2-IR2690-3.2.6 | Reg. Exec. (UE) 2024/2690, anexo, ponto 3.2.6 (artigo 21.o, n.o 2, alínea b), da Diretiva (UE) 2022/2555) | Parcial | [🛠️ Requisitos funcionais da integração](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/integracao-siem#️-requisitos-funcionais-da-integração); `OPS-001` | Sincronização NTP referida na integração SIEM (addon, L2+) e inventário de cobertura; não se exige redundância dos sistemas de monitorização e registo. |
| NIS2-IR2690-3.3.1 | Reg. Exec. (UE) 2024/2690, anexo, ponto 3.3.1 (artigo 21.o, n.o 2, alínea b), da Diretiva (UE) 2022/2555) | Parcial | [Política 37 §3.1](/sbd-toe/assets/policies/policy-formacao-seguranca#31-conteúdos-mínimos-de-onboarding); [Política 33 §4.1](/sbd-toe/assets/policies/policy-contratacao-segura#41-cláusulas-universais-todos-os-níveis) | Canal de reporte para colaboradores técnicos e notificação contratual por fornecedores; não há mecanismo para clientes nem para trabalhadores não técnicos. |
| NIS2-IR2690-3.3.2 | Reg. Exec. (UE) 2024/2690, anexo, ponto 3.3.2 (artigo 21.o, n.o 2, alínea b), da Diretiva (UE) 2022/2555) | Parcial | [Política 37 §3.1](/sbd-toe/assets/policies/policy-formacao-seguranca#31-conteúdos-mínimos-de-onboarding) | Formação dos colaboradores técnicos no canal de reporte; não se prevê divulgar o mecanismo a fornecedores e clientes. |
| NIS2-IR2690-4.1.1 | Reg. Exec. (UE) 2024/2690, anexo, ponto 4.1.1 (artigo 21.o, n.o 2, alínea c), da Diretiva (UE) 2022/2555) | Parcial | `OPS-017`; `OPS-017` | A continuidade das actividades e a gestão de crises da entidade ficam fora do âmbito do Manual; a recuperação da aplicação está prescrita (OPS-016, OPS-017). |
| NIS2-IR2690-4.1.3 | Reg. Exec. (UE) 2024/2690, anexo, ponto 4.1.3 (artigo 21.o, n.o 2, alínea c), da Diretiva (UE) 2022/2555) | Parcial | `CLA-001`; [🎯 Objetivo](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/adopcao-drp-bia#-objetivo) | O eixo de impacto da classificação e a reutilização de DRP/BIA existentes apoiam a análise de impacto, mas o Manual não exige BIA nem deriva dela requisitos de continuidade. |
| NIS2-IR2690-4.1.4 | Reg. Exec. (UE) 2024/2690, anexo, ponto 4.1.4 (artigo 21.o, n.o 2, alínea c), da Diretiva (UE) 2022/2555) | Parcial | `OPS-017` | O exercício do procedimento de recuperação só é obrigatório em L3 (OPS-017); a actualização do plano de continuidade da entidade fica fora do âmbito. |
| NIS2-IR2690-4.3.3 | Reg. Exec. (UE) 2024/2690, anexo, ponto 4.3.3 (artigo 21.o, n.o 2, alínea c), da Diretiva (UE) 2022/2555) | Parcial | [Política 10 §8](/sbd-toe/assets/policies/policy-dependencias#8-alertas-de-vulnerabilidades-em-produção); [KEV — exploração confirmada](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/epss-kev-priorizacao#kev--exploração-confirmada) | Consome feeds de vulnerabilidades (NVD/OSV/GitHub) e KEV; não há processo para gerir e utilizar informação recebida de CSIRT ou autoridades sobre incidentes, ameaças e medidas de atenuação. |
| NIS2-IR2690-5.1.1 | Reg. Exec. (UE) 2024/2690, anexo, ponto 5.1.1 (artigo 21.o, n.o 2, alínea d), da Diretiva (UE) 2022/2555) | Parcial | [Política 33 §2](/sbd-toe/assets/policies/policy-contratacao-segura#2-âmbito-e-obrigatoriedade); `GOV-006`; `GOV-007` | A política de contratação segura (Política 33) é obrigatória em todos os níveis, mas não define o papel da entidade na cadeia de abastecimento nem o comunica aos fornecedores. |
| NIS2-IR2690-5.1.2 | Reg. Exec. (UE) 2024/2690, anexo, ponto 5.1.2 (artigo 21.o, n.o 2, alínea d), da Diretiva (UE) 2022/2555) | Parcial | [Política 33 §3.1](/sbd-toe/assets/policies/policy-contratacao-segura#31-critérios-de-avaliação); [Política 33 §3.1](/sbd-toe/assets/policies/policy-contratacao-segura#31-critérios-de-avaliação); `GOV-007` | Critérios de due diligence (L2/L3) cobrem práticas de segurança e gestão de vulnerabilidades; faltam capacidade de cumprir especificações, qualidade e resiliência dos produtos e diversificação de fontes. |
| NIS2-IR2690-5.1.3 | Reg. Exec. (UE) 2024/2690, anexo, ponto 5.1.3 (artigo 21.o, n.o 2, alínea d), da Diretiva (UE) 2022/2555) | Lacuna | — | As avaliações coordenadas de riscos da UE (art. 22.º, n.º 1) não entram nos critérios de seleção. |
| NIS2-IR2690-5.1.4 | Reg. Exec. (UE) 2024/2690, anexo, ponto 5.1.4 (artigo 21.o, n.o 2, alínea d), da Diretiva (UE) 2022/2555) | Parcial | [Política 33 §4.1](/sbd-toe/assets/policies/policy-contratacao-segura#41-cláusulas-universais-todos-os-níveis); [Política 33 §4.1](/sbd-toe/assets/policies/policy-contratacao-segura#41-cláusulas-universais-todos-os-níveis); [Política 33 §4.1](/sbd-toe/assets/policies/policy-contratacao-segura#41-cláusulas-universais-todos-os-níveis); [Política 33 §4.2](/sbd-toe/assets/policies/policy-contratacao-segura#42-cláusulas-adicionais-por-nível-de-risco); [Política 33 §4.2](/sbd-toe/assets/policies/policy-contratacao-segura#42-cláusulas-adicionais-por-nível-de-risco); [Política 33 §4.2](/sbd-toe/assets/policies/policy-contratacao-segura#42-cláusulas-adicionais-por-nível-de-risco); [Política 33 §7.1](/sbd-toe/assets/policies/policy-contratacao-segura#71-checklist-de-offboarding) | Cláusulas universais (confidencialidade, notificação ≤ 24 h, subcontratação, rescisão) e por nível; faltam verificação de antecedentes do pessoal do fornecedor e, em L1/L2, direito de auditoria e (L1) tratamento de vulnerabilidades — apesar de a baseline pedir «direito de auditoria» sempre. |
| NIS2-IR2690-6.1.1 | Reg. Exec. (UE) 2024/2690, anexo, ponto 6.1.1 (artigo 21.o, n.o 2, alínea e), da Diretiva (UE) 2022/2555) | Parcial | `DEP-006`; [Política 33 §3.2](/sbd-toe/assets/policies/policy-contratacao-segura#32-resultado-da-due-diligence); `GOV-007` | Aquisição de bibliotecas e contratação de fornecedores com acesso são geridas por risco; não há processo para aquisição de produtos e serviços TIC (hardware, software de prateleira, serviços) para componentes críticos ao longo do ciclo de vida. |
| NIS2-IR2690-6.1.2 | Reg. Exec. (UE) 2024/2690, anexo, ponto 6.1.2 (artigo 21.o, n.o 2, alínea e), da Diretiva (UE) 2022/2555) | Parcial | [Política 33 §4.2](/sbd-toe/assets/policies/policy-contratacao-segura#42-cláusulas-adicionais-por-nível-de-risco); [💽 Contratos de licenciamento (software externo)](/sbd-toe/sbd-manual/governanca-contratacao/addon/clausulas-contratuais#-contratos-de-licenciamento-software-externo); `DEP-001` | Exige correção de vulnerabilidades e SBOM (L3) a fornecedores; faltam requisitos de atualizações de segurança durante toda a vida útil, informação sobre componentes de hardware, configuração segura por defeito e garantia de conformidade. |
| NIS2-IR2690-6.2.3 | Reg. Exec. (UE) 2024/2690, anexo, ponto 6.2.3 (artigo 21.o, n.o 2, alínea e), da Diretiva (UE) 2022/2555) | Parcial | [Política 33 §2](/sbd-toe/assets/policies/policy-contratacao-segura#2-âmbito-e-obrigatoriedade); [Política 33 §3.2](/sbd-toe/assets/policies/policy-contratacao-segura#32-resultado-da-due-diligence) | O desenvolvimento externalizado cai no âmbito da Política 33, mas herda as lacunas de aquisição (6.1). |
| NIS2-IR2690-6.3.2 | Reg. Exec. (UE) 2024/2690, anexo, ponto 6.3.2 (artigo 21.o, n.o 2, alínea e), da Diretiva (UE) 2022/2555) | Parcial | `IAC-003`; [Política 21 §3](/sbd-toe/assets/policies/policy-iac-seguro#3-princípios-de-iac-seguro); `IAC-012`; `CFG-007` | Configurações seguras impostas em sistemas novos via pipeline; em sistemas em funcionamento a deteção de drift só é obrigatória em L2/L3 (IaC) e L3 (aplicação). |
| NIS2-IR2690-6.3.3 | Reg. Exec. (UE) 2024/2690, anexo, ponto 6.3.3 (artigo 21.o, n.o 2, alínea e), da Diretiva (UE) 2022/2555) | Parcial | [Política 32 §4.6](/sbd-toe/assets/policies/policy-irp#46-post-mortem); `IAC-013`; `CNT-010` | Revisão das configurações após incidente significativo prescrita; a revisão formal de módulos continua só em L3. |
| NIS2-IR2690-6.4.2 | Reg. Exec. (UE) 2024/2690, anexo, ponto 6.4.2 (artigo 21.o, n.o 2, alínea e), da Diretiva (UE) 2022/2555) | Parcial | `DPL-001`; `DPL-003`; `DPL-007`; `IAC-007`; [Política 26 §2](/sbd-toe/assets/policies/policy-aprovacao-release#2-âmbito-e-obrigatoriedade) | Aprovação e gates antes da produção em todos os níveis (DPL-001/003); validação em staging e plan aprovado só L2/L3; avaliação de impacto não explícita. |
| NIS2-IR2690-6.6.1 | Reg. Exec. (UE) 2024/2690, anexo, ponto 6.6.1 (artigo 21.o, n.o 2, alínea e), da Diretiva (UE) 2022/2555) | Parcial | `DEP-007`; `DEP-003`; `DEP-005`; `CNT-010`; [Política 12 §4](/sbd-toe/assets/policies/policy-excecoes-cve#4-tipos-de-exceção); [Política 24 §6](/sbd-toe/assets/policies/policy-golden-base-images#6-sla-de-patching) | Correcções de dependências e imagens com SLA, integridade verificada e controlos compensatórios estão prescritas; a gestão de correcções de sistemas operativos e equipamentos da entidade fica fora de âmbito por decisão do lead (segurança da entidade). |
| NIS2-IR2690-6.7.2 | Reg. Exec. (UE) 2024/2690, anexo, ponto 6.7.2 (artigo 21.o, n.o 2, alínea e), da Diretiva (UE) 2022/2555) | Parcial | `ARC-001`; `ARC-002`; `ARC-006`; `ARC-008`; `INT-004`; `INT-006` | Zonas, exposição, isolamento e protocolos seguros cobertos; faltam: só dispositivos autorizados na rede, ligações de prestadores autorizadas e limitadas no tempo, restrição dos sistemas de gestão de segurança, planos de transição para protocolos de nova geração, normas de segurança do correio eletrónico e boas práticas de DNS e encaminhamento. |
| NIS2-IR2690-6.8.2 | Reg. Exec. (UE) 2024/2690, anexo, ponto 6.8.2 (artigo 21.o, n.o 2, alínea e), da Diretiva (UE) 2022/2555) | Parcial | `ARC-006`; `CFG-002`; `IAC-002`; `ARC-011`; `CNT-012`; [📝 Descrição](/sbd-toe/sbd-manual/arquitetura-segura/addon/diagramas-referencia#-descrição-2) | Separação produção/desenvolvimento e isolamento de domínios existem; DMZ só num diagrama de referência L3; segregação de rede entre ambientes só L3 (ARC-011); falta separar a rede e os canais de administração do tráfego operacional e as cópias de segurança de produção. |
| NIS2-IR2690-6.9.1 | Reg. Exec. (UE) 2024/2690, anexo, ponto 6.9.1 (artigo 21.o, n.o 2, alínea e), da Diretiva (UE) 2022/2555) | Parcial | `FIL-007`; `IDE-001`; `CNT-001`; `CNT-009`; `DEP-005` | Controla software não autorizado na cadeia (imagens, bibliotecas, ferramentas) e rastreio de ficheiros (L2/L3); não cobre proteção antimalware dos sistemas em operação. |
| NIS2-IR2690-6.9.2 | Reg. Exec. (UE) 2024/2690, anexo, ponto 6.9.2 (artigo 21.o, n.o 2, alínea e), da Diretiva (UE) 2022/2555) | Parcial | `FIL-007` | Sem software de deteção e resposta (EDR) nos sistemas; a deteção de malware limita-se a ficheiros carregados (L2/L3). |
| NIS2-IR2690-6.10.4 | Reg. Exec. (UE) 2024/2690, anexo, ponto 6.10.4 (artigo 21.o, n.o 2, alínea e), da Diretiva (UE) 2022/2555) | Parcial | `DEP-010` | A revisão periódica das fontes de informação sobre vulnerabilidades é obrigatória em L2/L3 (DEP-010); em L1 não. |
| NIS2-IR2690-8.1.1 | Reg. Exec. (UE) 2024/2690, anexo, ponto 8.1.1 (artigo 21.o, n.o 2, alínea g), da Diretiva (UE) 2022/2555) | Parcial | [Política 37 §2](/sbd-toe/assets/policies/policy-formacao-seguranca#2-âmbito-e-obrigatoriedade); `TRN-007`; [Política 37 §4.1](/sbd-toe/assets/policies/policy-formacao-seguranca#41-matriz-de-trilhos-por-perfil-e-nível-de-risco) | Sensibilização para técnicos e terceiros com acesso; faltam trabalhadores não técnicos, órgãos de direção (só «Awareness executivo») e práticas de ciber-higiene explícitas. |
| NIS2-IR2690-8.1.2 | Reg. Exec. (UE) 2024/2690, anexo, ponto 8.1.2 (artigo 21.o, n.o 2, alínea g), da Diretiva (UE) 2022/2555) | Parcial | `TRN-002`; `TRN-001` | Onboarding e renovação para funções técnicas; não há programa de sensibilização calendarizado para todo o pessoal. |
| NIS2-IR2690-8.2.4 | Reg. Exec. (UE) 2024/2690, anexo, ponto 8.2.4 (artigo 21.o, n.o 2, alínea g), da Diretiva (UE) 2022/2555) | Parcial | `TRN-002` | Onboarding antes de trabalho autónomo; não há gatilho explícito de formação na mudança para novo cargo com requisitos de segurança. |
| NIS2-IR2690-10.1.1 | Reg. Exec. (UE) 2024/2690, anexo, ponto 10.1.1 (artigo 21.o, n.o 2, alínea i), da Diretiva (UE) 2022/2555) | Parcial | `TRN-002`; [Política 33 §5.1](/sbd-toe/assets/policies/policy-contratacao-segura#51-processo-de-onboarding); `TRN-007` | Responsabilidades comunicadas no onboarding e termo individual para contractors; sem declaração de responsabilidades para trabalhadores em geral. |
| NIS2-IR2690-10.1.2 | Reg. Exec. (UE) 2024/2690, anexo, ponto 10.1.2 (artigo 21.o, n.o 2, alínea i), da Diretiva (UE) 2022/2555) | Parcial | `TRN-002`; `ACC-004` | Ciber-higiene geral e contratação de pessoal qualificado não tratadas. |
| NIS2-IR2690-10.3.1 | Reg. Exec. (UE) 2024/2690, anexo, ponto 10.3.1 (artigo 21.o, n.o 2, alínea i), da Diretiva (UE) 2022/2555) | Parcial | [Política 33 §4.1](/sbd-toe/assets/policies/policy-contratacao-segura#41-cláusulas-universais-todos-os-níveis); [Política 33 §7.1](/sbd-toe/assets/policies/policy-contratacao-segura#71-checklist-de-offboarding) | Confidencialidade e offboarding para fornecedores/contractors; deveres pós-cessação de trabalhadores são matéria laboral fora de âmbito. |
| NIS2-IR2690-10.3.2 | Reg. Exec. (UE) 2024/2690, anexo, ponto 10.3.2 (artigo 21.o, n.o 2, alínea i), da Diretiva (UE) 2022/2555) | Parcial | [Política 33 §5.1](/sbd-toe/assets/policies/policy-contratacao-segura#51-processo-de-onboarding); [Política 33 §4.1](/sbd-toe/assets/policies/policy-contratacao-segura#41-cláusulas-universais-todos-os-níveis) | Termos de confidencialidade para contractors; contratos de trabalho fora de âmbito. |
| NIS2-IR2690-11.1.1 | Reg. Exec. (UE) 2024/2690, anexo, ponto 11.1.1 (artigo 21.o, n.o 2, alíneas i) e j), da Diretiva (UE) 2022/2555) | Parcial | `ACC-001`; `ACC-005` | Controlo de acesso lógico prescrito; o acesso físico está fora de âmbito. |
| NIS2-IR2690-11.1.3 | Reg. Exec. (UE) 2024/2690, anexo, ponto 11.1.3 (artigo 21.o, n.o 2, alíneas i) e j), da Diretiva (UE) 2022/2555) | Parcial | [Política 32 §4.6](/sbd-toe/assets/policies/policy-irp#46-post-mortem); `ACC-007` | Revisão do modelo de acessos após incidente significativo prescrita; a revisão periódica do modelo de permissões (ACC-007) continua só em L2/L3. |
| NIS2-IR2690-11.4.2 | Reg. Exec. (UE) 2024/2690, anexo, ponto 11.4.2 (artigo 21.o, n.o 2, alíneas i) e j), da Diretiva (UE) 2022/2555) | Lacuna | — | Não se exige uso exclusivo dos sistemas de administração, separação lógica do software aplicacional nem proteção dedicada do seu acesso. |
| NIS2-IR2690-11.6.3 | Reg. Exec. (UE) 2024/2690, anexo, ponto 11.6.3 (artigo 21.o, n.o 2, alíneas i) e j), da Diretiva (UE) 2022/2555) | Parcial | `AUT-007`; `AUT-001`; `AUT-012`; `AUT-013` | Os métodos sem password e FIDO2 estão prescritos (AUT-001, AUT-012); a federação e o MFA continuam só em L2/L3 no núcleo. |
| NIS2-IR2690-11.6.4 | Reg. Exec. (UE) 2024/2690, anexo, ponto 11.6.4 (artigo 21.o, n.o 2, alíneas i) e j), da Diretiva (UE) 2022/2555) | Lacuna | — | Não há revisão periódica dos procedimentos e tecnologias de autenticação. |
| NIS2-IR2690-12.2.1 | Reg. Exec. (UE) 2024/2690, anexo, ponto 12.2.1 (artigo 21.o, n.o 2, alínea i), da Diretiva (UE) 2022/2555) | Lacuna | `PRI-002` | Não há política de tratamento de ativos (utilização, armazenamento, transporte, eliminação segura); só retenção/apagamento de dados pessoais (PRI-002, L2/L3). |
| NIS2-IR2690-12.2.2 | Reg. Exec. (UE) 2024/2690, anexo, ponto 12.2.2 (artigo 21.o, n.o 2, alínea i), da Diretiva (UE) 2022/2555) | Lacuna | [Política 33 §7.1](/sbd-toe/assets/policies/policy-contratacao-segura#71-checklist-de-offboarding) | Sem regras de ciclo de vida dos ativos, transporte e destruição segura; a eliminação de dados só aparece no offboarding de fornecedores. |
| NIS2-IR2690-12.2.3 | Reg. Exec. (UE) 2024/2690, anexo, ponto 12.2.3 (artigo 21.o, n.o 2, alínea i), da Diretiva (UE) 2022/2555) | Lacuna | — | Sem política a rever. |

### Fora de âmbito (43) {#fora-de-ambito}

Obrigações que o Manual declara fora de âmbito, com a razão.

| Obrigação | Referência | Razão |
|---|---|---|
| NIS2-3-4-a_d | Art. 3.º, n.º 4, 1.º par., als. a)–d) | Relação administrativa com a autoridade competente/ENISA (registo, notificação de dados de identificação, supervisão ou regime sancionatório); plano jurídico-administrativo, não de engenharia de segurança. |
| NIS2-3-4-2par | Art. 3.º, n.º 4, 2.º par. | Relação administrativa com a autoridade competente/ENISA (registo, notificação de dados de identificação, supervisão ou regime sancionatório); plano jurídico-administrativo, não de engenharia de segurança. |
| NIS2-26-3 | Art. 26.º, n.º 3 | Designação de representante na União: obrigação jurídica de estabelecimento, não de engenharia. |
| NIS2-27-2 | Art. 27.º, n.º 2 | Relação administrativa com a autoridade competente/ENISA (registo, notificação de dados de identificação, supervisão ou regime sancionatório); plano jurídico-administrativo, não de engenharia de segurança. |
| NIS2-27-3 | Art. 27.º, n.º 3 | Relação administrativa com a autoridade competente/ENISA (registo, notificação de dados de identificação, supervisão ou regime sancionatório); plano jurídico-administrativo, não de engenharia de segurança. |
| NIS2-28-1 | Art. 28.º, n.º 1 | Dever funcional específico dos registos de TLD e das entidades que prestam serviços de registo de nomes de domínio (conteúdo e acesso à base de dados de registo); é requisito de negócio do serviço, não prática de engenharia de segurança que um manual SbD genérico deva prescrever. |
| NIS2-28-2 | Art. 28.º, n.º 2 | Dever funcional específico dos registos de TLD e das entidades que prestam serviços de registo de nomes de domínio (conteúdo e acesso à base de dados de registo); é requisito de negócio do serviço, não prática de engenharia de segurança que um manual SbD genérico deva prescrever. |
| NIS2-28-3 | Art. 28.º, n.º 3 | Dever funcional específico dos registos de TLD e das entidades que prestam serviços de registo de nomes de domínio (conteúdo e acesso à base de dados de registo); é requisito de negócio do serviço, não prática de engenharia de segurança que um manual SbD genérico deva prescrever. |
| NIS2-28-4 | Art. 28.º, n.º 4 | Dever funcional específico dos registos de TLD e das entidades que prestam serviços de registo de nomes de domínio (conteúdo e acesso à base de dados de registo); é requisito de negócio do serviço, não prática de engenharia de segurança que um manual SbD genérico deva prescrever. |
| NIS2-28-5 | Art. 28.º, n.º 5 | Dever funcional específico dos registos de TLD e das entidades que prestam serviços de registo de nomes de domínio (conteúdo e acesso à base de dados de registo); é requisito de negócio do serviço, não prática de engenharia de segurança que um manual SbD genérico deva prescrever. |
| NIS2-28-6 | Art. 28.º, n.º 6 | Dever funcional específico dos registos de TLD e das entidades que prestam serviços de registo de nomes de domínio (conteúdo e acesso à base de dados de registo); é requisito de negócio do serviço, não prática de engenharia de segurança que um manual SbD genérico deva prescrever. |
| NIS2-29-4 | Art. 29.º, n.º 4 | Relação administrativa com a autoridade competente/ENISA (registo, notificação de dados de identificação, supervisão ou regime sancionatório); plano jurídico-administrativo, não de engenharia de segurança. |
| NIS2-30-1 | Art. 30.º, n.º 1, al. a) | Faculdade (notificação voluntária), não dever; a Política 32 não a impede. |
| NIS2-32-2-2par | Art. 32.º, n.º 2, 3.º par.; art. 33.º, n.º 2, 3.º par. | Relação administrativa com a autoridade competente/ENISA (registo, notificação de dados de identificação, supervisão ou regime sancionatório); plano jurídico-administrativo, não de engenharia de segurança. |
| NIS2-32-6 | Art. 32.º, n.º 6 | Relação administrativa com a autoridade competente/ENISA (registo, notificação de dados de identificação, supervisão ou regime sancionatório); plano jurídico-administrativo, não de engenharia de segurança. |
| NIS2-34-4_5 | Art. 34.º, n.os 4 e 5 | Relação administrativa com a autoridade competente/ENISA (registo, notificação de dados de identificação, supervisão ou regime sancionatório); plano jurídico-administrativo, não de engenharia de segurança. |
| NIS2-IR2690-art1 | Reg. Exec. (UE) 2024/2690, art. 1.º | Disposição de âmbito pessoal; não cria dever de engenharia. |
| NIS2-IR2690-4.3.1 | Reg. Exec. (UE) 2024/2690, anexo, ponto 4.3.1 (artigo 21.o, n.o 2, alínea c), da Diretiva (UE) 2022/2555) | Gestão de crises institucional (BCM corporativo para além do software); o próprio cross-check NIS2 do Manual declara-a fora («gestão de crise institucional … fora do manual base»). A War room P1 da Política 32 é resposta a incidentes, não gestão de crises. |
| NIS2-IR2690-4.3.2 | Reg. Exec. (UE) 2024/2690, anexo, ponto 4.3.2 (artigo 21.o, n.o 2, alínea c), da Diretiva (UE) 2022/2555) | Gestão de crises institucional (BCM corporativo para além do software); o próprio cross-check NIS2 do Manual declara-a fora («gestão de crise institucional … fora do manual base»). A War room P1 da Política 32 é resposta a incidentes, não gestão de crises. |
| NIS2-IR2690-4.3.4 | Reg. Exec. (UE) 2024/2690, anexo, ponto 4.3.4 (artigo 21.o, n.o 2, alínea c), da Diretiva (UE) 2022/2555) | Gestão de crises institucional (BCM corporativo para além do software); o próprio cross-check NIS2 do Manual declara-a fora («gestão de crise institucional … fora do manual base»). A War room P1 da Política 32 é resposta a incidentes, não gestão de crises. |
| NIS2-IR2690-10.1.3 | Reg. Exec. (UE) 2024/2690, anexo, ponto 10.1.3 (artigo 21.o, n.o 2, alínea i), da Diretiva (UE) 2022/2555) | Gestão de recursos humanos (verificação de antecedentes, regime disciplinar, afetação de pessoal); fora do âmbito de um manual de engenharia de segurança de software. |
| NIS2-IR2690-10.2.1 | Reg. Exec. (UE) 2024/2690, anexo, ponto 10.2.1 (artigo 21.o, n.o 2, alínea i), da Diretiva (UE) 2022/2555) | Gestão de recursos humanos (verificação de antecedentes, regime disciplinar, afetação de pessoal); fora do âmbito de um manual de engenharia de segurança de software. |
| NIS2-IR2690-10.2.2 | Reg. Exec. (UE) 2024/2690, anexo, ponto 10.2.2 (artigo 21.o, n.o 2, alínea i), da Diretiva (UE) 2022/2555) | Gestão de recursos humanos (verificação de antecedentes, regime disciplinar, afetação de pessoal); fora do âmbito de um manual de engenharia de segurança de software. |
| NIS2-IR2690-10.2.3 | Reg. Exec. (UE) 2024/2690, anexo, ponto 10.2.3 (artigo 21.o, n.o 2, alínea i), da Diretiva (UE) 2022/2555) | Gestão de recursos humanos (verificação de antecedentes, regime disciplinar, afetação de pessoal); fora do âmbito de um manual de engenharia de segurança de software. |
| NIS2-IR2690-10.4.1 | Reg. Exec. (UE) 2024/2690, anexo, ponto 10.4.1 (artigo 21.o, n.o 2, alínea i), da Diretiva (UE) 2022/2555) | Gestão de recursos humanos (verificação de antecedentes, regime disciplinar, afetação de pessoal); fora do âmbito de um manual de engenharia de segurança de software. |
| NIS2-IR2690-10.4.2 | Reg. Exec. (UE) 2024/2690, anexo, ponto 10.4.2 (artigo 21.o, n.o 2, alínea i), da Diretiva (UE) 2022/2555) | Gestão de recursos humanos (verificação de antecedentes, regime disciplinar, afetação de pessoal); fora do âmbito de um manual de engenharia de segurança de software. |
| NIS2-IR2690-12.1.1 | Reg. Exec. (UE) 2024/2690, anexo, ponto 12.1.1 (artigo 21.o, n.o 2, alínea i), da Diretiva (UE) 2022/2555) | A gestão de activos da entidade como um todo (inventário e classificação de todos os activos, infraestrutura, equipamentos, licenças) fica fora de âmbito por decisão do lead: o Manual é centrado na aplicação. O inventário e a classificação da aplicação e dos seus componentes (CLA-001, SBOM) dão evidência para a parte que lhe toca. |
| NIS2-IR2690-12.1.2 | Reg. Exec. (UE) 2024/2690, anexo, ponto 12.1.2 (artigo 21.o, n.o 2, alínea i), da Diretiva (UE) 2022/2555) | A gestão de activos da entidade como um todo (inventário e classificação de todos os activos, infraestrutura, equipamentos, licenças) fica fora de âmbito por decisão do lead: o Manual é centrado na aplicação. O inventário e a classificação da aplicação e dos seus componentes (CLA-001, SBOM) dão evidência para a parte que lhe toca. |
| NIS2-IR2690-12.3.1 | Reg. Exec. (UE) 2024/2690, anexo, ponto 12.3.1 (artigo 21.o, n.o 2, alínea i), da Diretiva (UE) 2022/2555) | Controlo de endpoints/posto de trabalho (suportes amovíveis, autoexecução, dispositivos portáteis); operação de TI fora do âmbito de um manual de engenharia de segurança de software. |
| NIS2-IR2690-12.3.2 | Reg. Exec. (UE) 2024/2690, anexo, ponto 12.3.2 (artigo 21.o, n.o 2, alínea i), da Diretiva (UE) 2022/2555) | Controlo de endpoints/posto de trabalho (suportes amovíveis, autoexecução, dispositivos portáteis); operação de TI fora do âmbito de um manual de engenharia de segurança de software. |
| NIS2-IR2690-12.3.3 | Reg. Exec. (UE) 2024/2690, anexo, ponto 12.3.3 (artigo 21.o, n.o 2, alínea i), da Diretiva (UE) 2022/2555) | Controlo de endpoints/posto de trabalho (suportes amovíveis, autoexecução, dispositivos portáteis); operação de TI fora do âmbito de um manual de engenharia de segurança de software. |
| NIS2-IR2690-12.4.1 | Reg. Exec. (UE) 2024/2690, anexo, ponto 12.4.1 (artigo 21.o, n.o 2, alínea i), da Diretiva (UE) 2022/2555) | A gestão de activos da entidade como um todo (inventário e classificação de todos os activos, infraestrutura, equipamentos, licenças) fica fora de âmbito por decisão do lead: o Manual é centrado na aplicação. O inventário e a classificação da aplicação e dos seus componentes (CLA-001, SBOM) dão evidência para a parte que lhe toca. |
| NIS2-IR2690-12.4.2 | Reg. Exec. (UE) 2024/2690, anexo, ponto 12.4.2 (artigo 21.o, n.o 2, alínea i), da Diretiva (UE) 2022/2555) | A gestão de activos da entidade como um todo (inventário e classificação de todos os activos, infraestrutura, equipamentos, licenças) fica fora de âmbito por decisão do lead: o Manual é centrado na aplicação. O inventário e a classificação da aplicação e dos seus componentes (CLA-001, SBOM) dão evidência para a parte que lhe toca. |
| NIS2-IR2690-12.4.3 | Reg. Exec. (UE) 2024/2690, anexo, ponto 12.4.3 (artigo 21.o, n.o 2, alínea i), da Diretiva (UE) 2022/2555) | A gestão de activos da entidade como um todo (inventário e classificação de todos os activos, infraestrutura, equipamentos, licenças) fica fora de âmbito por decisão do lead: o Manual é centrado na aplicação. O inventário e a classificação da aplicação e dos seus componentes (CLA-001, SBOM) dão evidência para a parte que lhe toca. |
| NIS2-IR2690-13.1.1 | Reg. Exec. (UE) 2024/2690, anexo, ponto 13.1.1 (artigo 21.o, n.o 2, alíneas c), e) e i), da Diretiva (UE) 2022/2555) | Segurança física e ambiental das instalações (perímetros, energia, climatização, acesso físico); fora do âmbito de um manual de engenharia de segurança de software. |
| NIS2-IR2690-13.1.2 | Reg. Exec. (UE) 2024/2690, anexo, ponto 13.1.2 (artigo 21.o, n.o 2, alíneas c), e) e i), da Diretiva (UE) 2022/2555) | Segurança física e ambiental das instalações (perímetros, energia, climatização, acesso físico); fora do âmbito de um manual de engenharia de segurança de software. |
| NIS2-IR2690-13.1.3 | Reg. Exec. (UE) 2024/2690, anexo, ponto 13.1.3 (artigo 21.o, n.o 2, alíneas c), e) e i), da Diretiva (UE) 2022/2555) | Segurança física e ambiental das instalações (perímetros, energia, climatização, acesso físico); fora do âmbito de um manual de engenharia de segurança de software. |
| NIS2-IR2690-13.2.1 | Reg. Exec. (UE) 2024/2690, anexo, ponto 13.2.1 (artigo 21.o, n.o 2, alíneas c), e) e i), da Diretiva (UE) 2022/2555) | Segurança física e ambiental das instalações (perímetros, energia, climatização, acesso físico); fora do âmbito de um manual de engenharia de segurança de software. |
| NIS2-IR2690-13.2.2 | Reg. Exec. (UE) 2024/2690, anexo, ponto 13.2.2 (artigo 21.o, n.o 2, alíneas c), e) e i), da Diretiva (UE) 2022/2555) | Segurança física e ambiental das instalações (perímetros, energia, climatização, acesso físico); fora do âmbito de um manual de engenharia de segurança de software. |
| NIS2-IR2690-13.2.3 | Reg. Exec. (UE) 2024/2690, anexo, ponto 13.2.3 (artigo 21.o, n.o 2, alíneas c), e) e i), da Diretiva (UE) 2022/2555) | Segurança física e ambiental das instalações (perímetros, energia, climatização, acesso físico); fora do âmbito de um manual de engenharia de segurança de software. |
| NIS2-IR2690-13.3.1 | Reg. Exec. (UE) 2024/2690, anexo, ponto 13.3.1 (artigo 21.o, n.o 2, alíneas c), e) e i), da Diretiva (UE) 2022/2555) | Segurança física e ambiental das instalações (perímetros, energia, climatização, acesso físico); fora do âmbito de um manual de engenharia de segurança de software. |
| NIS2-IR2690-13.3.2 | Reg. Exec. (UE) 2024/2690, anexo, ponto 13.3.2 (artigo 21.o, n.o 2, alíneas c), e) e i), da Diretiva (UE) 2022/2555) | Segurança física e ambiental das instalações (perímetros, energia, climatização, acesso físico); fora do âmbito de um manual de engenharia de segurança de software. |
| NIS2-IR2690-13.3.3 | Reg. Exec. (UE) 2024/2690, anexo, ponto 13.3.3 (artigo 21.o, n.o 2, alíneas c), e) e i), da Diretiva (UE) 2022/2555) | Segurança física e ambiental das instalações (perímetros, energia, climatização, acesso físico); fora do âmbito de um manual de engenharia de segurança de software. |
