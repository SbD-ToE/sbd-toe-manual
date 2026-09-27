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

- **ART50** — Abrangido pelo art. 50.º (transparência) (declarável sozinho). Sistema de IA abrangido pelas obrigações de transparência do art. 50.º (interacção directa com pessoas singulares, conteúdo sintético, reconhecimento de emoções ou categorização biométrica, falsificações profundas), seja ou não de risco elevado.

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
| CTX-AIA-RE-P08 | `ARC-014` | — | obrigatório | Supervisão humana em qualquer nível, com interface que permita a quem supervisiona compreender as capacidades e limitações do sistema, detectar anomalias, interpretar o resultado, decidir não o usar ou anulá-lo e parar o sistema; medidas proporcionais aos riscos, à autonomia e ao contexto; quem supervisiona é advertido para o enviesamento da automatização. | Reg. (UE) 2024/1689, art. 14.º, n.os 1 a 4: «ser eficazmente supervisionados por pessoas singulares durante o período em que estão em utilização» (AIA-14-1, AIA-14-2, AIA-14-3, AIA-14-4) | não admitida |
| CTX-AIA-RE-P09 | `THR-008` | ART50 | obrigatório | Sistemas que geram ou manipulam imagem, vídeo ou áudio realistas, em qualquer nível: o threat model cobre a utilização indevida razoavelmente previsível do conteúdo gerado, e as salvaguardas são avaliadas com red-team e testes de segurança de conteúdo. | Reg. (UE) 2024/1689, art. 5.º, n.º 1, als. b-A) e b-B), e n.º 1-A (Reg. (UE) 2026/1744): «medidas técnicas de segurança razoáveis e adequadas e de outras garantias para prevenir de forma segura essa geração ou manipulação» (AIA-5-1-b-A, AIA-5-1-b-B, AIA-5-1A) | admitida |
| CTX-AIA-RE-P10 | `ARC-014` | ART50 | obrigatório | Sistemas que geram ou manipulam imagem, vídeo ou áudio realistas, em qualquer nível: filtros e classificadores de segurança de conteúdo na entrada e na saída, e correcção da utilização indevida observada ou assinalada. | Reg. (UE) 2024/1689, art. 5.º, n.º 1, als. b-A) e b-B), e n.º 1-A (Reg. (UE) 2026/1744): «medidas técnicas de segurança razoáveis e adequadas e de outras garantias para prevenir de forma segura essa geração ou manipulação» (AIA-5-1-b-A, AIA-5-1-b-B, AIA-5-1A) | admitida |
| CTX-AIA-RE-P11 | `ARC-009` | — | obrigatório | Em qualquer nível, o limiar de alteração significativa distingue as alterações predeterminadas (declaradas antecipadamente na documentação técnica, p. ex. aprendizagem contínua dentro de limites) das modificações substanciais; cada alteração é classificada e a classificação fica registada; uma modificação substancial é sinalizada para nova avaliação da conformidade; os registos permitem identificar situações de risco e modificações substanciais. | Reg. (UE) 2024/1689, art. 43.º, n.º 4, art. 12.º, n.º 2, e anexo IV, ponto 2, al. f): «devem ser sujeitos a um novo procedimento de avaliação da conformidade caso sejam substancialmente modificados» (AIA-43-4, AIA-AnxIV-2-f, AIA-12-2) | não admitida |

> **ART50.** O grau ART50 recebe os pisos CTX-AIA-RE-P09 e CTX-AIA-RE-P10 (salvaguardas de segurança de conteúdo em geradores de imagem, vídeo ou áudio realistas, art. 5.º, n.º 1-A) e os acrescentos CTX-AIA-RE-R01 (informar) e R02 (marcar conteúdo sintético).

## Requisitos acrescentados pelo regime {#acrescentos}

Estes requisitos só fazem sentido sob o regime e por isso não vivem nos catálogos do Manual; definem-se aqui, com a base legal de cada um.

| Requisito | Nome | Critério de aceitação | Base legal |
|---|---|---|---|
| `CTX-AIA-RE-R01` | Informar que se interage com IA | As pessoas que interagem directamente com o sistema são informadas de que estão a interagir com um sistema de IA, salvo se for óbvio pelo contexto; as pessoas expostas a reconhecimento de emoções ou a categorização biométrica são informadas desse funcionamento; o conteúdo de imagem, áudio ou vídeo que constitua falsificação profunda é divulgado como gerado ou manipulado. A informação é clara e perceptível, dada o mais tardar na primeira interacção ou exposição, e cumpre os requisitos de acessibilidade; a presença do aviso é verificada em teste. | Reg. (UE) 2024/1689, art. 50.º, n.os 1, 3, 4 (1.º parágrafo) e 5: «de forma clara e percetível o mais tardar aquando da primeira interação ou exposição» (AIA-50-1, AIA-50-3, AIA-50-4-a, AIA-50-5) |
| `CTX-AIA-RE-R02` | Marcação de conteúdo sintético | Os resultados de áudio, imagem, vídeo ou texto gerados ou manipulados pelo sistema são marcados num formato legível por máquina e detectáveis como artificiais (p. ex. metadados de proveniência, credenciais de conteúdo, marca de água), com uma solução eficaz, interoperável e sólida na medida do tecnicamente viável; a marcação é verificada em teste e não é removida pelos passos seguintes do pipeline; as excepções do art. 50.º, n.º 2 (apoio à edição normalizada, sem alteração substancial dos dados de entrada) ficam registadas. | Reg. (UE) 2024/1689, art. 50.º, n.º 2, e art. 111.º, n.º 4: «sejam marcados num formato legível por máquina e detetáveis como tendo sido artificialmente gerados ou manipulados» (AIA-50-2, AIA-111-4) |
| `CTX-AIA-RE-R03` | Informar e explicar às pessoas afectadas | Quando um sistema de IA de risco elevado do anexo III apoia decisões sobre pessoas singulares: as pessoas são informadas de que estão sujeitas à sua utilização; a aplicação regista, por decisão, o resultado do sistema e os principais elementos que o determinaram (OPS-011), de modo a poder dar à pessoa afectada explicações claras e pertinentes sobre o papel do sistema e os principais elementos da decisão. Quando a decisão é exclusivamente automatizada e há dados pessoais, aplica-se também CTX-RGPD-R05. | Reg. (UE) 2024/1689, art. 26.º, n.º 11, e art. 86.º, n.º 1: «explicações claras e pertinentes sobre o papel do sistema de IA no processo de tomada de decisão e sobre os principais elementos da decisão tomada» (AIA-26-11, AIA-86-1) |
| `CTX-AIA-RE-R04` | Plano de acompanhamento pós-comercialização | Quando a organização é o prestador: plano de acompanhamento pós-comercialização por sistema, integrado na documentação técnica (anexo IV, ponto 9), que nomeia os sinais recolhidos em produção (OPS-011) e os fornecidos pelos responsáveis pela implantação, os critérios de desempenho contra os quais são analisados, a cadência e o responsável da análise, e os gatilhos para acção correctiva (rollback, reclassificação, revisão do threat model, notificação de incidente grave); a análise é activa e sistemática ao longo da vida útil e inclui, se for caso disso, a interacção com outros sistemas de IA. As métricas de desvio do modelo ficam pendentes da ronda AISVS/SAIF do AppSec Core. | Reg. (UE) 2024/1689, art. 72.º, n.os 1 a 3, e anexo IV, ponto 9: «O sistema de acompanhamento pós-comercialização deve basear-se num plano de acompanhamento pós-comercialização» (AIA-72-1, AIA-72-2, AIA-72-3, AIA-AnxIV-9) |

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
| `THR-008` | Threat modeling estendido para sistemas com componentes AI/ML | ▲ | ▲ | ▲ | CTX-AIA-RE-P04 |
| `ARC-001` | Zonas de confiança identificadas e documentadas | ✔ | ✔ | ✔ | — |
| `ARC-002` | Exposição externa minimizada e justificada | ✔ | ✔ | ✔ | — |
| `ARC-003` | Revisão de arquitectura com foco em segurança | — | ✔ | ✔ | — |
| `ARC-004` | Decisões de arquitectura documentadas | — | ✔ | ✔ | — |
| `ARC-005` | Threat modeling integrado nos fluxos críticos | — | ✔ | ✔ | — |
| `ARC-006` | Controlos técnicos de isolamento entre domínios sensíveis | ✔ | ✔ | ✔ | — |
| `ARC-007` | Padrões de arquitectura reutilizáveis e aprovados | — | ✔ | ✔ | — |
| `ARC-008` | Fluxos de dados entre zonas de confiança protegidos | ✔ | ✔ | ✔ | — |
| `ARC-009` | Alterações significativas desencadeiam nova revisão | ▲ | ▲ | ▲ | CTX-AIA-RE-P11 |
| `ARC-010` | Diagramas de arquitectura versionados e acessíveis | ✔ | ✔ | ✔ | — |
| `ARC-011` | Segmentação lógica e física entre ambientes | — | — | ✔ | — |
| `ARC-012` | Critérios formais de aprovação para aplicações de risco elevado | — | — | ✔ | — |
| `ARC-013` | Validação automática de topologia em CI/CD ou como código | — | — | ✔ | — |
| `ARC-014` | Padrões arquitetónicos específicos para sistemas com componentes AI/ML | ▲ | ▲ | ▲ | CTX-AIA-RE-P05, CTX-AIA-RE-P08 |
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
| `GOV-015` | Divulgação coordenada de vulnerabilidades com canal de receção publicado | ✔ | ✔ | ✔ | — |
| `GOV-016` | Contas privilegiadas e de administração dos sistemas de suporte | ✔ | ✔ | ✔ | — |
| `GOV-017` | Ciclo de vida das identidades com acesso aos sistemas | ✔ | ✔ | ✔ | — |
| `CTX-AIA-RE-R03` | Informar e explicar às pessoas afectadas | ▲ | ▲ | ▲ | — |
| `CTX-AIA-RE-R04` | Plano de acompanhamento pós-comercialização | ▲ | ▲ | ▲ | — |

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
| `THR-008` | Threat modeling estendido para sistemas com componentes AI/ML | ▲ | ▲ | ▲ | CTX-AIA-RE-P09 |
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
| `ARC-014` | Padrões arquitetónicos específicos para sistemas com componentes AI/ML | ▲ | ▲ | ▲ | CTX-AIA-RE-P10 |
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
| `GOV-015` | Divulgação coordenada de vulnerabilidades com canal de receção publicado | ✔ | ✔ | ✔ | — |
| `GOV-016` | Contas privilegiadas e de administração dos sistemas de suporte | ✔ | ✔ | ✔ | — |
| `GOV-017` | Ciclo de vida das identidades com acesso aos sistemas | ✔ | ✔ | ✔ | — |
| `CTX-AIA-RE-R01` | Informar que se interage com IA | ▲ | ▲ | ▲ | — |
| `CTX-AIA-RE-R02` | Marcação de conteúdo sintético | ▲ | ▲ | ▲ | — |

## Mapa de evidência da documentação técnica {#mapa-evidencia}

Obrigações documentais do regime (art. 11.º, anexo IV e art. 13.º do AI Act) ligadas aos artefactos do Manual que as alimentam. «Apoia evidência»: o Manual produz a evidência de engenharia e a redacção do documento é de quem coloca o produto no mercado. As lacunas e o que fica fora de âmbito aparecem com a razão. Gerado da matriz `_matriz/aiact.yaml`.

| Obrigação | Referência | Força | Como o Manual responde | Nota |
|---|---|---|---|---|
| AIA-11-1-a | Art. 11.º, n.º 1, primeiro parágrafo | Apoia evidência | `ARC-004`; `ARC-010`; `THR-006`; `DEP-012`; `TST-004` | A redacção do documento é do prestador; o Manual fornece a evidência (ver o mapa de evidência da página «Requisitos aplicáveis»). |
| AIA-11-1-b | Art. 11.º, n.º 1, segundo parágrafo | Apoia evidência | `ARC-004`; `ARC-010`; `THR-006`; `DEP-012`; `TST-004` | Os pontos do anexo IV sem artefacto ficam como lacuna declarada no mapa de evidência. |
| AIA-AnxIV-1 | Anexo IV, ponto 1 | Apoia evidência | `ARC-001`; `ARC-010`; `ARC-014`; `DEP-011`; `DEP-012`; `DEP-013` | Lacuna declarada: finalidade prevista (al. a)), formas de colocação no mercado (al. d)), hardware fora da inferência própria (al. e)) e descrição da interface para o implantador (al. g)). Fora de âmbito: fotografias e marcações (al. f)). |
| AIA-AnxIV-2-a | Anexo IV, ponto 2, alínea a | Apoia evidência | `DEP-011`; `DEP-012`; `DEP-014`; `CIC-001` | A metodologia de treino fica fora de âmbito (governação de dados, art. 10.º). |
| AIA-AnxIV-2-b | Anexo IV, ponto 2, alínea b | Apoia evidência | `ARC-004` | Lacuna declarada: lógica geral, algoritmos e o que o sistema optimiza. Os pressupostos sobre grupos de pessoas ficam fora de âmbito (enviesamento). |
| AIA-AnxIV-2-c | Anexo IV, ponto 2, alínea c | Apoia evidência | `ARC-001`; `ARC-010`; `ARC-014` | Lacuna declarada: recursos computacionais de desenvolvimento, treino, teste e validação. |
| AIA-AnxIV-2-d | Anexo IV, ponto 2, alínea d | Fora de âmbito | — | Governação de dados de treino (art. 10.º) fora de âmbito por decisão do lead; DEP-011 e a Política 39 §4 dão só evidência incidental. |
| AIA-AnxIV-2-e | Anexo IV, ponto 2, alínea e | Apoia evidência | `ARC-014`; `REQ-AGN-003` | Avaliação das medidas de supervisão apoiada pela supervisão mínima do ARC-014 (piso CTX-AIA-RE-P08). |
| AIA-AnxIV-2-f | Anexo IV, ponto 2, alínea f | Cobre | `ARC-009`; `DEP-013` | — |
| AIA-AnxIV-2-g | Anexo IV, ponto 2, alínea g | Apoia evidência | `TST-004`; `DPL-010`; `CIC-007` | **Ronda AISVS/SAIF do AppSec Core.** Métricas de exactidão e solidez para sistemas não agênticos pendente da ronda AISVS/SAIF do AppSec Core; impactos discriminatórios fora de âmbito (enviesamento). |
| AIA-AnxIV-2-h | Anexo IV, ponto 2, alínea h | Cobre | `REQ-001`; `THR-008`; `ARC-014` | — |
| AIA-AnxIV-3 | Anexo IV, ponto 3 | Apoia evidência | `OPS-011`; `ARC-014`; `THR-008` | Lacuna declarada: capacidades e limitações de desempenho e especificações dos dados de entrada. A exactidão por grupos de pessoas fica fora de âmbito (enviesamento). |
| AIA-AnxIV-4 | Anexo IV, ponto 4 | Lacuna | — | **Ronda AISVS/SAIF do AppSec Core.** Lacuna declarada: adequação das métricas de desempenho, pendente da ronda AISVS/SAIF do AppSec Core. |
| AIA-AnxIV-5 | Anexo IV, ponto 5 | Fora de âmbito | — | Sistema de gestão de riscos do art. 9.º fora de âmbito por decisão do lead. |
| AIA-AnxIV-6 | Anexo IV, ponto 6 | Cobre | `THR-006`; `ARC-010`; `CIC-005` | — |
| AIA-AnxIV-7 | Anexo IV, ponto 7 | Fora de âmbito | — | Lista de normas harmonizadas/especificações comuns aplicadas: plano da conformidade. |
| AIA-AnxIV-8 | Anexo IV, ponto 8 | Fora de âmbito | — | Plano da avaliação da conformidade/mercado (declaração UE, marcação CE, organismos notificados, registo na base de dados da UE); fora de um manual de engenharia de segurança — o cross-check do próprio Manual declara-o fora («não substitui»). |
| AIA-AnxIV-9 | Anexo IV, ponto 9 | Cobre | `CTX-AIA-RE-R04`; `OPS-011` | — |
| AIA-13-1 | Art. 13.º, n.º 1 | Apoia evidência | `ARC-014`; `OPS-011` | A interpretação do output é apoiada pela supervisão mínima do ARC-014 (piso CTX-AIA-RE-P08). |
| AIA-13-2 | Art. 13.º, n.º 2 | Apoia evidência | `DEP-013`; `DEP-014`; `ARC-014`; `OPS-011` | **Ronda AISVS/SAIF do AppSec Core.** A redacção das instruções é do prestador. Lacuna declarada: finalidade prevista e descrição da interface; os níveis de exactidão e solidez ficam pendentes da ronda AISVS/SAIF do AppSec Core. |
| AIA-13-3 | Art. 13.º, n.º 3 | Apoia evidência | `DEP-013`; `DEP-014`; `ARC-014`; `OPS-011` | **Ronda AISVS/SAIF do AppSec Core.** A redacção das instruções é do prestador. Lacuna declarada: finalidade prevista e descrição da interface; os níveis de exactidão e solidez ficam pendentes da ronda AISVS/SAIF do AppSec Core. |
| AIA-13-3-b-ii | Art. 13.º, n.º 3, alínea b), subalínea ii) | Lacuna | — | **Ronda AISVS/SAIF do AppSec Core.** Declaração dos níveis de exactidão e solidez pendente da ronda AISVS/SAIF do AppSec Core. |
| AIA-13-3-e | Art. 13.º, n.º 3, alínea e) | Apoia evidência | `DEP-013` | — |
| AIA-13-3-f | Art. 13.º, n.º 3, alínea f) | Apoia evidência | `OPS-011` | — |

## Obrigações do regime por força de cobertura {#forca}

Contagem das obrigações da matriz `_matriz/aiact.yaml` (excluídas as dirigidas às autoridades). A secção [«O que este Manual cobre e o que fica de fora»](#cobertura) lista-as.

| Força | Obrigações |
|---|--:|
| Cobre | 41 |
| Parcial | 33 |
| Apoia evidência | 44 |
| Lacuna | 11 |
| Fora de âmbito | 116 |

## O que este Manual cobre e o que fica de fora {#cobertura}

Todas as obrigações da matriz `_matriz/aiact.yaml` em três categorias: o que o Manual **cobre**, e de que forma; as **lacunas declaradas** (o que não cobre por omissão); e o que fica **fora de âmbito**, com a razão. Gerado da matriz; nenhuma obrigação fica em silêncio. As 15 obrigações dirigidas às autoridades não criam dever para a organização e não entram nas listas.

### Cobre (85) {#cobre}

Força «cobre» ou «apoia evidência». A forma é a resposta do Manual: requisito do catálogo, política, secção, piso ou requisito acrescentado pelo regime.

| Obrigação | Referência | Força | Forma |
|---|---|---|---|
| AIA-4a-2 | Art. 4.º-A, n.º 2 | Apoia evidência | `PRI-002`; `ACC-001` |
| AIA-5-1-a | Art. 5.º, n.º 1, primeiro parágrafo, alínea a) | Apoia evidência | [Cap. 02 US-17](/sbd-toe/sbd-manual/requisitos-seguranca/aplicacao-lifecycle#us-17---incorporação-de-restrições-legais-normativas-e-contratuais) |
| AIA-5-1-b | Art. 5.º, n.º 1, primeiro parágrafo, alínea b) | Apoia evidência | [Cap. 02 US-17](/sbd-toe/sbd-manual/requisitos-seguranca/aplicacao-lifecycle#us-17---incorporação-de-restrições-legais-normativas-e-contratuais) |
| AIA-5-1-b-A | Art. 5.º, n.º 1, primeiro parágrafo, alínea b-A) | Cobre | `THR-008`; `ARC-014` |
| AIA-5-1-b-B | Art. 5.º, n.º 1, primeiro parágrafo, alínea b-B) | Cobre | `THR-008`; `ARC-014` |
| AIA-5-1-e | Art. 5.º, n.º 1, primeiro parágrafo, alínea e) | Apoia evidência | [Cap. 02 US-17](/sbd-toe/sbd-manual/requisitos-seguranca/aplicacao-lifecycle#us-17---incorporação-de-restrições-legais-normativas-e-contratuais); `DEP-011` |
| AIA-5-1A | Art. 5.º, n.º 1-A | Cobre | `THR-008`; `ARC-014`; [C5 - Eval suites contínuas para agentes em desenvolvimento e produção](/sbd-toe/sbd-manual/testes-seguranca/addon/ia-nos-testes#c5-eval-suites) |
| AIA-6-4 | Art. 6.º, n.º 4 | Apoia evidência | `CLA-001`; `GOV-009` |
| AIA-11-1-a | Art. 11.º, n.º 1, primeiro parágrafo | Apoia evidência | `ARC-004`; `ARC-010`; `THR-006`; `DEP-012`; `TST-004` |
| AIA-11-1-b | Art. 11.º, n.º 1, segundo parágrafo | Apoia evidência | `ARC-004`; `ARC-010`; `THR-006`; `DEP-012`; `TST-004` |
| AIA-AnxIV-1 | Anexo IV, ponto 1 | Apoia evidência | `ARC-001`; `ARC-010`; `ARC-014`; `DEP-011`; `DEP-012`; `DEP-013` |
| AIA-AnxIV-2-a | Anexo IV, ponto 2, alínea a | Apoia evidência | `DEP-011`; `DEP-012`; `DEP-014`; `CIC-001` |
| AIA-AnxIV-2-b | Anexo IV, ponto 2, alínea b | Apoia evidência | `ARC-004` |
| AIA-AnxIV-2-c | Anexo IV, ponto 2, alínea c | Apoia evidência | `ARC-001`; `ARC-010`; `ARC-014` |
| AIA-AnxIV-2-e | Anexo IV, ponto 2, alínea e | Apoia evidência | `ARC-014`; `REQ-AGN-003` |
| AIA-AnxIV-2-f | Anexo IV, ponto 2, alínea f | Cobre | `ARC-009`; `DEP-013` |
| AIA-AnxIV-2-g | Anexo IV, ponto 2, alínea g | Apoia evidência | `TST-004`; `DPL-010`; `CIC-007` |
| AIA-AnxIV-2-h | Anexo IV, ponto 2, alínea h | Cobre | `REQ-001`; `THR-008`; `ARC-014` |
| AIA-AnxIV-3 | Anexo IV, ponto 3 | Apoia evidência | `OPS-011`; `ARC-014`; `THR-008` |
| AIA-AnxIV-6 | Anexo IV, ponto 6 | Cobre | `THR-006`; `ARC-010`; `CIC-005` |
| AIA-AnxIV-9 | Anexo IV, ponto 9 | Cobre | `CTX-AIA-RE-R04`; `OPS-011` |
| AIA-12-1 | Art. 12.º, n.º 1 | Cobre | `LOG-001`; `OPS-011`; [Política 29 §7](/sbd-toe/assets/policies/policy-logging-estruturado#7-retenção-de-logs) |
| AIA-12-2 | Art. 12.º, n.º 2 | Cobre | `ARC-009`; `OPS-011` |
| AIA-13-1 | Art. 13.º, n.º 1 | Apoia evidência | `ARC-014`; `OPS-011` |
| AIA-13-2 | Art. 13.º, n.º 2 | Apoia evidência | `DEP-013`; `DEP-014`; `ARC-014`; `OPS-011` |
| AIA-13-3 | Art. 13.º, n.º 3 | Apoia evidência | `DEP-013`; `DEP-014`; `ARC-014`; `OPS-011` |
| AIA-13-3-e | Art. 13.º, n.º 3, alínea e) | Apoia evidência | `DEP-013` |
| AIA-13-3-f | Art. 13.º, n.º 3, alínea f) | Apoia evidência | `OPS-011` |
| AIA-14-1 | Art. 14.º, n.º 1 | Cobre | `ARC-014`; `ARC-015`; [Cap. 04 US-15](/sbd-toe/sbd-manual/arquitetura-segura/aplicacao-lifecycle#us-15---identificação-e-governação-de-componentes-não-determinísticos) |
| AIA-14-2 | Art. 14.º, n.º 2 | Cobre | `ARC-014`; `ARC-015`; `REQ-AGN-004` |
| AIA-14-3 | Art. 14.º, n.º 3 | Cobre | `ARC-014`; `REQ-AGN-002`; [Política 38 §2](/sbd-toe/assets/policies/policy-mandates-agentes#2-âmbito) |
| AIA-14-4 | Art. 14.º, n.º 4 | Cobre | `ARC-014`; `REQ-AGN-003`; `ARC-015`; [🎯 Âmbito e enquadramento](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#-âmbito-e-enquadramento) |
| AIA-15-5 | Art. 15.º, n.º 5 | Cobre | `THR-008`; `ARC-014`; `DEP-011`; `OPS-014`; [1. Os pesos do modelo são activo crítico](/sbd-toe/sbd-manual/containers-imagens/addon/self-hosted-inference#1-os-pesos-do-modelo-são-activo-crítico) |
| AIA-17-1-b | Art. 17.º, n.º 1, alínea b) | Cobre | `ARC-004`; `THR-006`; `REQ-005` |
| AIA-17-1-c | Art. 17.º, n.º 1, alínea c) | Cobre | `DEV-001`; `DEV-004`; `CIC-005` |
| AIA-17-1-i | Art. 17.º, n.º 1, alínea i) | Cobre | [Política 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória); [Política 32 §4.1](/sbd-toe/assets/policies/policy-irp#41-triagem-t0----15-minutos-de-detecção) |
| AIA-17-1-k | Art. 17.º, n.º 1, alínea k) | Cobre | `GOV-009`; [Política 06 §10](/sbd-toe/assets/policies/policy-rastreabilidade#10-prazos-de-retenção-mínimos) |
| AIA-17-1-m | Art. 17.º, n.º 1, alínea m) | Cobre | `GOV-001`; `GOV-002` |
| AIA-17-2 | Art. 17.º, n.º 2 | Apoia evidência | `CLA-001` |
| AIA-18-1 | Art. 18.º, n.º 1 | Apoia evidência | [Política 06 §10](/sbd-toe/assets/policies/policy-rastreabilidade#10-prazos-de-retenção-mínimos) |
| AIA-18-3 | Art. 18.º, n.º 3 | Apoia evidência | [Política 29 §7](/sbd-toe/assets/policies/policy-logging-estruturado#7-retenção-de-logs) |
| AIA-19-1 | Art. 19.º, n.º 1 | Cobre | [Política 29 §7](/sbd-toe/assets/policies/policy-logging-estruturado#7-retenção-de-logs); `OPS-003`; `LOG-005` |
| AIA-19-2 | Art. 19.º, n.º 2 | Apoia evidência | [Política 29 §7](/sbd-toe/assets/policies/policy-logging-estruturado#7-retenção-de-logs) |
| AIA-21-2 | Art. 21.º, n.º 2 | Apoia evidência | `LOG-003`; `OPS-003` |
| AIA-25-2 | Art. 25.º, n.º 2 | Apoia evidência | `DEP-012`; [Política 33 §10.6](/sbd-toe/assets/policies/policy-contratacao-segura#106-conformidade-regulatória-declarada) |
| AIA-26-6 | Art. 26.º, n.º 6 | Cobre | [Política 18 §10.5](/sbd-toe/assets/policies/policy-gestao-segredos#105-telemetria-sob-controlo-do-deployer); [Política 29 §7](/sbd-toe/assets/policies/policy-logging-estruturado#7-retenção-de-logs); `OPS-003` |
| AIA-26-9 | Art. 26.º, n.º 9 | Apoia evidência | [Cap. 03 US-08](/sbd-toe/sbd-manual/threat-modeling/aplicacao-lifecycle#us-08---aplicação-linddun-quando-existir-tratamento-de-dados-pessoais--novo) |
| AIA-26-11 | Art. 26.º, n.º 11 | Cobre | `CTX-AIA-RE-R03` |
| AIA-27-1 | Art. 27.º, n.º 1 | Apoia evidência | `THR-008`; [Cap. 03 US-08](/sbd-toe/sbd-manual/threat-modeling/aplicacao-lifecycle#us-08---aplicação-linddun-quando-existir-tratamento-de-dados-pessoais--novo) |
| AIA-27-2 | Art. 27.º, n.º 2 | Apoia evidência | `THR-006` |
| AIA-27-4 | Art. 27.º, n.º 4 | Apoia evidência | [Cap. 03 US-08](/sbd-toe/sbd-manual/threat-modeling/aplicacao-lifecycle#us-08---aplicação-linddun-quando-existir-tratamento-de-dados-pessoais--novo) |
| AIA-42-3 | Art. 42.º, n.º 3 | Apoia evidência | `THR-008`; `ARC-014` |
| AIA-43-4 | Art. 43.º, n.º 4 | Cobre | `ARC-009`; `CLA-006`; `DEP-013` |
| AIA-AnxVI | Anexo VI | Apoia evidência | `GOV-010`; `GOV-009` |
| AIA-AnxVII-4 | Anexo VII, pontos 4.1-4.5, 4.7 | Apoia evidência | `DEP-011`; `DEP-012` |
| AIA-50-1 | Art. 50.º, n.º 1 | Cobre | `CTX-AIA-RE-R01` |
| AIA-50-2 | Art. 50.º, n.º 2 | Cobre | `CTX-AIA-RE-R02` |
| AIA-50-3 | Art. 50.º, n.º 3 | Cobre | `CTX-AIA-RE-R01` |
| AIA-50-4-a | Art. 50.º, n.º 4, primeiro parágrafo | Cobre | `CTX-AIA-RE-R01` |
| AIA-50-5 | Art. 50.º, n.º 5 | Cobre | `CTX-AIA-RE-R01` |
| AIA-53-1-a | Art. 53.º, n.º 1, alínea a) | Apoia evidência | `DEP-012`; [Cap. 10 US-21](/sbd-toe/sbd-manual/testes-seguranca/aplicacao-lifecycle#us-21---governação-do-uso-de-ia-em-testes-e-eval-suites-para-agentes) |
| AIA-53-1-b | Art. 53.º, n.º 1, alínea b) | Apoia evidência | [Política 33 §10.6](/sbd-toe/assets/policies/policy-contratacao-segura#106-conformidade-regulatória-declarada); `DEP-014` |
| AIA-55-1-b | Art. 55.º, n.º 1, alínea b) | Apoia evidência | `THR-008` |
| AIA-55-1-c | Art. 55.º, n.º 1, alínea c) | Cobre | [Política 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória); [Política 32 §4.1](/sbd-toe/assets/policies/policy-irp#41-triagem-t0----15-minutos-de-detecção); [Política 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória) |
| AIA-55-1-d | Art. 55.º, n.º 1, alínea d) | Cobre | [1. Os pesos do modelo são activo crítico](/sbd-toe/sbd-manual/containers-imagens/addon/self-hosted-inference#1-os-pesos-do-modelo-são-activo-crítico); `ARC-014`; `DEP-011` |
| AIA-AnxXI-1 | Anexo XI, secção 1 | Apoia evidência | `DEP-012`; [Política 39 §4](/sbd-toe/assets/policies/policy-ai-bom-supply-chain#4-ai-bom--formato-e-conteúdo-mínimo) |
| AIA-AnxXI-2 | Anexo XI, secção 2 | Apoia evidência | [Cap. 10 US-21](/sbd-toe/sbd-manual/testes-seguranca/aplicacao-lifecycle#us-21---governação-do-uso-de-ia-em-testes-e-eval-suites-para-agentes) |
| AIA-AnxXII | Anexo XII | Apoia evidência | [Política 33 §10.6](/sbd-toe/assets/policies/policy-contratacao-segura#106-conformidade-regulatória-declarada) |
| AIA-59-1 | Art. 59.º, n.º 1 | Apoia evidência | `ENC-002`; `ACC-002`; `PRI-002` |
| AIA-60-7 | Art. 60.º, n.os 7-8 | Apoia evidência | [Política 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória); `DPL-005` |
| AIA-72-1 | Art. 72.º, n.º 1 | Cobre | `CTX-AIA-RE-R04`; `OPS-011` |
| AIA-72-2 | Art. 72.º, n.º 2 | Cobre | `CTX-AIA-RE-R04`; `OPS-011` |
| AIA-72-3 | Art. 72.º, n.º 3 | Cobre | `CTX-AIA-RE-R04`; `OPS-011` |
| AIA-73-1 | Art. 73.º, n.º 1 | Cobre | [Política 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória); [Política 32 §4.1](/sbd-toe/assets/policies/policy-irp#41-triagem-t0----15-minutos-de-detecção) |
| AIA-73-2 | Art. 73.º, n.º 2 | Cobre | [Política 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória) |
| AIA-73-3 | Art. 73.º, n.º 3 | Cobre | [Política 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória) |
| AIA-73-4 | Art. 73.º, n.º 4 | Cobre | [Política 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória) |
| AIA-73-5 | Art. 73.º, n.º 5 | Cobre | [Política 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória) |
| AIA-74-12 | Art. 74.º, n.º 12 | Apoia evidência | `DEP-011`; [Política 39 §4](/sbd-toe/assets/policies/policy-ai-bom-supply-chain#4-ai-bom--formato-e-conteúdo-mínimo) |
| AIA-74-13 | Art. 74.º, n.º 13 | Apoia evidência | `CIC-005` |
| AIA-75-1A | Art. 75.º, n.º 1-A | Cobre | [Política 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória); [Política 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória) |
| AIA-79-4 | Art. 79.º, n.os 2 e 4 | Apoia evidência | `DPL-005`; `GOV-010` |
| AIA-82-2 | Art. 82.º, n.º 2 | Apoia evidência | `DPL-005`; `GOV-010` |
| AIA-86-1 | Art. 86.º, n.º 1 | Cobre | `CTX-AIA-RE-R03`; [Cap. 04 US-15](/sbd-toe/sbd-manual/arquitetura-segura/aplicacao-lifecycle#us-15---identificação-e-governação-de-componentes-não-determinísticos); `OPS-011` |
| AIA-111-4 | Art. 111.º, n.º 4 | Cobre | `CTX-AIA-RE-R02` |

### Lacuna declarada (44) {#lacuna}

Força «parcial» ou «lacuna»: o Manual não cobre, ou cobre só em parte, e diz o que falta. As lacunas pendentes de uma ronda do AppSec Core estão marcadas com o nome da ronda.

| Obrigação | Referência | Força | Como o Manual responde | O que falta |
|---|---|---|---|---|
| AIA-4-1 | Art. 4.º, n.º 1 (substituído) | Parcial | [Política 37 §11](/sbd-toe/assets/policies/policy-formacao-seguranca#11-formação-em-agentes-ai-e-tooling-pervasivo-módulo-obrigatório); [Cap. 13 US-19](/sbd-toe/sbd-manual/formacao-onboarding/aplicacao-lifecycle#us-19---formação-em-uso-seguro-de-ia-e-tooling); `TRN-001` | Cobre papéis técnicos do SDLC (developer, AppSec, DevOps, GRC, PO, CISO) e o uso de IA como ferramenta/agentes; faltam o pessoal de negócio que opera ou utiliza sistemas de IA de produto em nome da organização e a ponderação do contexto de utilização e das pessoas visadas. |
| AIA-4a-1-b | Art. 4.º-A, n.º 1, alínea b) | Parcial | `ENC-002`; `PRI-001`; `ACC-002` | Encriptação em repouso (L2+) e minimização existem; faltam limitações técnicas à reutilização e pseudonimização exigida para estes conjuntos (a pseudonimização no Manual é só em logs, ERR-007). |
| AIA-4a-1-c | Art. 4.º-A, n.º 1, alínea c) | Parcial | `ACC-001`; `ACC-003`; `LOG-001` | Controlo de acesso RBAC e registo de acessos (L1+) cobrem o núcleo; falta documentação criteriosa por acesso a estes conjuntos e o dever de confidencialidade de quem acede. |
| AIA-4a-1-d | Art. 4.º-A, n.º 1, alínea d) | Parcial | [Política 18 §10.4](/sbd-toe/assets/policies/policy-gestao-segredos#104-training-opt-out-obrigatório-para-pii); `DEP-014` | Só há proibição de uso para treino/retenção pelo fornecedor de serviços de IA; não há proibição geral de transmissão ou consulta destes dados por terceiros. |
| AIA-4a-1-e | Art. 4.º-A, n.º 1, alínea e) | Parcial | `PRI-002` | PRI-002 impõe prazo e apagamento verificável, mas não o gatilho legal «logo que o enviesamento seja corrigido». |
| AIA-4a-1-f | Art. 4.º-A, n.º 1, alínea f) | Parcial | `PRI-004` | O inventário regista finalidade; não regista os motivos da estrita necessidade nem a impossibilidade de usar outros dados. |
| AIA-6-1 | Art. 6.º, n.os 1, 1-A, 1-B, 1-C | Lacuna | `CLA-004` | A determinação jurídica é de compliance, mas o Manual não recolhe o resultado («sistema de IA de risco elevado») como entrada da classificação nem lhe associa piso de nível e ativação dos requisitos de IA; CLA-004 só prevê reclassificação genérica por «novos contextos regulatórios». Aplica-se desde 2.8.2028. |
| AIA-6-2-3 | Art. 6.º, n.os 2 e 3 | Lacuna | `CLA-004`; [🧩 Critérios complementares em contextos de automação e apoio à decisão](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/modelo-classificacao-eixos#-critérios-complementares-em-contextos-de-automação-e-apoio-à-decisão) | Idem AIA-6-1 para o anexo III (aplica-se desde 2.12.2027). O Cap. 01 afirma que a IA não altera por si só a criticidade — não há ponte entre o estatuto legal de risco elevado e L2/L3. Raiz dos conflitos de nível. |
| AIA-8-1 | Art. 8.º, n.º 1 | Parcial | `THR-008`; `ARC-014`; `OPS-011` | Cibersegurança coberta (L2+); faltam exatidão, governação de dados, transparência/instruções e supervisão humana para sistemas não agênticos — ver arts. 10.º, 13.º, 14.º, 15.º. |
| AIA-9-1 | Art. 9.º, n.º 1 | Parcial | `CLA-001`; `THR-008`; [Cap. 03 US-12](/sbd-toe/sbd-manual/threat-modeling/aplicacao-lifecycle#us-12---threat-modeling-estendido-para-componentes-aiml-não-agentic) | Existe gestão de risco de segurança (classificação + threat modeling estendido a IA); falta um sistema de gestão de riscos para saúde, segurança e direitos fundamentais, documentado e mantido ao longo do ciclo de vida. |
| AIA-9-2 | Art. 9.º, n.º 2 | Parcial | `THR-008`; [Cap. 03 US-13](/sbd-toe/sbd-manual/threat-modeling/aplicacao-lifecycle#us-13---derivação-de-abusemisuse-cases-para-o-backlog); `OPS-011` | Identificação de ameaças e de abuso (misuse) e monitorização de drift existem; faltam estimativa de riscos para saúde/segurança/direitos fundamentais em uso previsto e a avaliação de riscos a partir de dados pós-comercialização. |
| AIA-9-4 | Art. 9.º, n.º 4 | Lacuna | — | Nenhuma prescrição sobre efeitos combinados dos requisitos da secção 2 (p. ex. conflito exatidão × supervisão × transparência). |
| AIA-9-5 | Art. 9.º, n.º 5 | Parcial | `CLA-007`; `GOV-004` | Risco residual com compensação, owner e TTL existe; faltam a hierarquia legal (eliminar por conceção → mitigar → informar o implantador → formar) e o critério de aceitabilidade do risco residual para pessoas afetadas. |
| AIA-9-9 | Art. 9.º, n.º 9 | Lacuna | [Cap. 03 US-08](/sbd-toe/sbd-manual/threat-modeling/aplicacao-lifecycle#us-08---aplicação-linddun-quando-existir-tratamento-de-dados-pessoais--novo) | O LINDDUN cobre privacidade; nenhuma prescrição sobre impacto em menores ou grupos vulneráveis. |
| AIA-10-1 | Art. 10.º, n.º 1 | Parcial | `DEP-011`; [Política 39 §4](/sbd-toe/assets/policies/policy-ai-bom-supply-chain#4-ai-bom--formato-e-conteúdo-mínimo) | Proveniência, versão e curadoria de datasets (L2+); faltam critérios de qualidade dos conjuntos de treino/validação/teste. |
| AIA-10-2 | Art. 10.º, n.º 2 | Parcial | `DEP-011`; `ARC-014`; [Política 39 §4](/sbd-toe/assets/policies/policy-ai-bom-supply-chain#4-ai-bom--formato-e-conteúdo-mínimo) | Cobre origem/recolha, proveniência e integridade; faltam escolhas de conceção, pressupostos, avaliação de disponibilidade, exame e mitigação de enviesamentos e identificação de lacunas. |
| AIA-10-3 | Art. 10.º, n.º 3 | Lacuna | — | Pertinência, representatividade, ausência de erros e propriedades estatísticas: nenhuma prescrição (abstenção declarada no cross-check). |
| AIA-10-4 | Art. 10.º, n.º 4 | Lacuna | — | Adequação ao contexto geográfico/comportamental/funcional: nenhuma prescrição. |
| AIA-10-6 | Art. 10.º, n.º 6 | Lacuna | — | Qualidade dos conjuntos de teste em sistemas sem treino (p. ex. LLM de terceiros): as eval suites (§C5) testam agentes quanto a regressão/abuso, sem critérios de representatividade dos dados de teste. |
| AIA-AnxIV-4 | Anexo IV, ponto 4 | Lacuna | — | **Ronda AISVS/SAIF do AppSec Core.** Lacuna declarada: adequação das métricas de desempenho, pendente da ronda AISVS/SAIF do AppSec Core. |
| AIA-13-3-b-ii | Art. 13.º, n.º 3, alínea b), subalínea ii) | Lacuna | — | **Ronda AISVS/SAIF do AppSec Core.** Declaração dos níveis de exactidão e solidez pendente da ronda AISVS/SAIF do AppSec Core. |
| AIA-15-1 | Art. 15.º, n.º 1 | Parcial | `ARC-014`; `OPS-011` | **Ronda AISVS/SAIF do AppSec Core.** Cibersegurança coberta (THR-008, ARC-014, DEP-011 a DEP-014, OPS-011 a OPS-014, DPL-010/011); exactidão e solidez pendente da ronda AISVS/SAIF do AppSec Core. |
| AIA-15-3 | Art. 15.º, n.º 3 | Lacuna | — | **Ronda AISVS/SAIF do AppSec Core.** Declaração dos níveis e parâmetros de exactidão pendente da ronda AISVS/SAIF do AppSec Core. |
| AIA-15-4 | Art. 15.º, n.º 4 | Parcial | [Considerações de design](/sbd-toe/sbd-manual/arquitetura-segura/recomendacoes-avancadas#considerações-de-design); [Política 09 §3](/sbd-toe/assets/policies/policy-arquitetura-segura#3-princípios-de-arquitetura-segura); [🧱 Structured outputs — validação do que o modelo devolve](/sbd-toe/sbd-manual/desenvolvimento-seguro/addon/genia-e-seguranca#structured-outputs) | Fallback, fail-secure e validação de output com falha fechada existem; faltam redundância/planos de segurança para desempenho e mitigação de enviesamento em circuitos de realimentação de sistemas que continuam a aprender. |
| AIA-16-a | Art. 16.º, alínea a) | Parcial | `THR-008`; `ARC-014`; `OPS-011` | Remete para a secção 2: ver AIA-9 a AIA-15 (cibersegurança sim; dados, transparência, supervisão e exatidão com lacunas). |
| AIA-16-c | Art. 16.º, alínea c) | Parcial | `GOV-001`; `TST-001` | Ver AIA-17-1-*: componentes operacionais de um SGQ existem; falta a estrutura formal do SGQ do art. 17.º. |
| AIA-16-d | Art. 16.º, alínea d) | Parcial | [Política 06 §10](/sbd-toe/assets/policies/policy-rastreabilidade#10-prazos-de-retenção-mínimos); [Política 06 §10](/sbd-toe/assets/policies/policy-rastreabilidade#10-prazos-de-retenção-mínimos) | Ver AIA-18-1: sem prazo de 10 anos para a documentação de sistemas de IA de risco elevado. |
| AIA-16-e | Art. 16.º, alínea e) | Parcial | [Política 29 §7](/sbd-toe/assets/policies/policy-logging-estruturado#7-retenção-de-logs); `OPS-003` | Ver AIA-19-1. |
| AIA-16-j | Art. 16.º, alínea j) | Parcial | `DPL-005`; [Política 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória) | Ver AIA-20-1/20-2. |
| AIA-17-1-a | Art. 17.º, n.º 1, alínea a) | Parcial | `GOV-001`; `CLA-006`; `THR-006` | Governação e gatilhos de reavaliação por mudança existem; falta estratégia de cumprimento regulamentar documentada, incluindo procedimentos de avaliação da conformidade e de gestão de modificações. |
| AIA-17-1-e | Art. 17.º, n.º 1, alínea e) | Parcial | `REQ-001`; `DEV-001` | Especificações técnicas próprias (catálogo, guidelines); falta a gestão de normas harmonizadas/especificações comuns (plano da conformidade). |
| AIA-17-1-f | Art. 17.º, n.º 1, alínea f) | Parcial | `DEP-011`; `PRI-004` | Inventário de datasets e registo de finalidades; falta procedimento de gestão de dados (aquisição, rotulagem, armazenamento, filtragem, agregação, conservação) para dados de treino. |
| AIA-17-1-g | Art. 17.º, n.º 1, alínea g) | Parcial | `CLA-001`; `THR-008` | Ver AIA-9-1. |
| AIA-17-1-j | Art. 17.º, n.º 1, alínea j) | Parcial | [Política 32 §4.1](/sbd-toe/assets/policies/policy-irp#41-triagem-t0----15-minutos-de-detecção) | Comunicação a autoridades via trilho regulatório do IRP; falta comunicação com organismos notificados, outros operadores, clientes e partes interessadas. |
| AIA-17-1-l | Art. 17.º, n.º 1, alínea l) | Parcial | `DEP-014`; [Política 39 §7](/sbd-toe/assets/policies/policy-ai-bom-supply-chain#7-resposta-a-incidentes-upstream); `GOV-007` | Segurança do aprovisionamento de modelos/fornecedores de IA coberta; falta a gestão de recursos (pessoal, meios). |
| AIA-20-1 | Art. 20.º, n.º 1 | Parcial | `DPL-005`; [Política 27 §3](/sbd-toe/assets/policies/policy-rollback#3-tipos-de-rollback-e-requisitos-específicos) | Rollback testado permite repor/desativar; faltam retirada/recolha do sistema e informação a distribuidores, implantadores, mandatário e importadores. |
| AIA-20-2 | Art. 20.º, n.º 2 | Parcial | [Política 32 §4.2](/sbd-toe/assets/policies/policy-irp#42-contenção-t1---início-imediato-após-confirmação); [Política 32 §4.1](/sbd-toe/assets/policies/policy-irp#41-triagem-t0----15-minutos-de-detecção) | Investigação de incidentes existe; faltam investigação conjunta com o implantador e informação à autoridade de fiscalização sobre a não conformidade (não só sobre incidentes graves). |
| AIA-25-4 | Art. 25.º, n.º 4, primeiro parágrafo | Parcial | [Política 33 §10.3](/sbd-toe/assets/policies/policy-contratacao-segura#103-audit-rights); [Política 33 §10.6](/sbd-toe/assets/policies/policy-contratacao-segura#106-conformidade-regulatória-declarada); `DEP-014`; [Cap. 14 US-21](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-21) | Cláusulas contratuais específicas para fornecedores de serviços de IA (retenção, auditoria, notificação, conformidade declarada); não especificam a informação, capacidades, acesso técnico e assistência necessários para o prestador cumprir o regulamento. |
| AIA-26-1 | Art. 26.º, n.º 1 | Parcial | [Política 38 §4](/sbd-toe/assets/policies/policy-mandates-agentes#4-conteúdo-mínimo-de-um-mandate); [Cap. 14 US-21](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-21) | Para agentes, o mandate define como se usa o sistema; para sistemas de IA adquiridos não há procedimento para operar conforme as instruções de utilização do prestador. |
| AIA-26-2 | Art. 26.º, n.º 2 | Parcial | [Política 38 §4](/sbd-toe/assets/policies/policy-mandates-agentes#4-conteúdo-mínimo-de-um-mandate); [Política 37 §11](/sbd-toe/assets/policies/policy-formacao-seguranca#11-formação-em-agentes-ai-e-tooling-pervasivo-módulo-obrigatório) | Owner humano nomeado e formação obrigatória para agentes; nada para supervisores de sistemas de IA de risco elevado não agênticos (competência, autoridade, apoio). |
| AIA-26-4 | Art. 26.º, n.º 4 | Lacuna | `VAL-001` | VAL-001 valida entradas por segurança; não há dever de assegurar que os dados de entrada são pertinentes e representativos para a finalidade. |
| AIA-26-5 | Art. 26.º, n.º 5 | Parcial | `OPS-011`; `REQ-AGN-003`; [Política 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória) | Monitorização (L2+), kill-switch de agentes e notificação à autoridade existem; faltam a informação ao prestador/distribuidor e a suspensão de sistemas não agênticos quando há risco. |
| AIA-55-1-a | Art. 55.º, n.º 1, alínea a) | Parcial | [Política 19 §7.1](/sbd-toe/assets/policies/policy-estrategia-testes#71-composição-mínima); [C5 - Eval suites contínuas para agentes em desenvolvimento e produção](/sbd-toe/sbd-manual/testes-seguranca/addon/ia-nos-testes#c5-eval-suites) | Red-team corpus e eval suites (agentes A2+/A3+); faltam protocolos normalizados de avaliação de modelos e testagem antagónica documentada ao nível do modelo. |
| AIA-73-6 | Art. 73.º, n.º 6 | Parcial | [Política 32 §4.2](/sbd-toe/assets/policies/policy-irp#42-contenção-t1---início-imediato-após-confirmação); `LOG-009` | Preservação de evidência e investigação existem; falta a proibição de alterar o sistema de modo que afete a análise de causas sem informar previamente as autoridades (o IRP privilegia contenção «quando possível»). |

### Fora de âmbito (116) {#fora-de-ambito}

Obrigações que o Manual declara fora de âmbito, com a razão.

| Obrigação | Referência | Razão |
|---|---|---|
| AIA-2-1 | Art. 2.º, n.º 1 | Disposição delimitadora de âmbito, definição ou qualificação jurídica; não cria dever de engenharia. |
| AIA-2-12 | Art. 2.º, n.º 12 | Disposição delimitadora de âmbito, definição ou qualificação jurídica; não cria dever de engenharia. |
| AIA-2-13 | Art. 2.º, n.º 13 | Disposição delimitadora de âmbito, definição ou qualificação jurídica; não cria dever de engenharia. |
| AIA-4a-1-a | Art. 4.º-A, n.º 1, alínea a) | Juízo de necessidade (eficácia de dados sintéticos/anonimizados para corrigir enviesamento) — decisão de ciência de dados e proteção de dados, não de engenharia de segurança. |
| AIA-5-1-c | Art. 5.º, n.º 1, primeiro parágrafo, alínea c) | Juízo de admissibilidade da finalidade (prática proibida) — qualificação jurídica e de produto; o Manual declara-o fora. Gancho genérico: Cap. 02 US-17 (obrigações legais mapeadas a requisitos). |
| AIA-5-1-d | Art. 5.º, n.º 1, primeiro parágrafo, alínea d) | Juízo de admissibilidade da finalidade (prática proibida) — qualificação jurídica e de produto; o Manual declara-o fora. Gancho genérico: Cap. 02 US-17 (obrigações legais mapeadas a requisitos). |
| AIA-5-1-f | Art. 5.º, n.º 1, primeiro parágrafo, alínea f) | Juízo de admissibilidade da finalidade (prática proibida) — qualificação jurídica e de produto; o Manual declara-o fora. Gancho genérico: Cap. 02 US-17 (obrigações legais mapeadas a requisitos). |
| AIA-5-1-g | Art. 5.º, n.º 1, primeiro parágrafo, alínea g) | Juízo de admissibilidade da finalidade (prática proibida) — qualificação jurídica e de produto; o Manual declara-o fora. Gancho genérico: Cap. 02 US-17 (obrigações legais mapeadas a requisitos). |
| AIA-5-1-h | Art. 5.º, n.º 1, primeiro parágrafo, alínea h) | Juízo de admissibilidade da finalidade (prática proibida) — qualificação jurídica e de produto; o Manual declara-o fora. Gancho genérico: Cap. 02 US-17 (obrigações legais mapeadas a requisitos). |
| AIA-5-1B | Art. 5.º, n.º 1-B | Disposição delimitadora de âmbito, definição ou qualificação jurídica; não cria dever de engenharia. |
| AIA-8-2 | Art. 8.º, n.º 2 | Conformidade integrada com legislação setorial do anexo I; plano da conformidade de produto. |
| AIA-9-6 | Art. 9.º, n.os 6-7 | O art. 9.º (sistema de gestão de riscos) fica fora de âmbito por decisão do lead. |
| AIA-9-8 | Art. 9.º, n.º 8 | O art. 9.º (sistema de gestão de riscos) fica fora de âmbito por decisão do lead. |
| AIA-9-10 | Art. 9.º, n.º 10 | Faculdade/presunção (não cria dever autónomo); plano da estratégia de conformidade. |
| AIA-11-2 | Art. 11.º, n.º 2 | Documentação técnica única com legislação setorial do anexo I; organização documental da conformidade. |
| AIA-AnxIV-2-d | Anexo IV, ponto 2, alínea d | Governação de dados de treino (art. 10.º) fora de âmbito por decisão do lead; DEP-011 e a Política 39 §4 dão só evidência incidental. |
| AIA-AnxIV-5 | Anexo IV, ponto 5 | Sistema de gestão de riscos do art. 9.º fora de âmbito por decisão do lead. |
| AIA-AnxIV-7 | Anexo IV, ponto 7 | Lista de normas harmonizadas/especificações comuns aplicadas: plano da conformidade. |
| AIA-AnxIV-8 | Anexo IV, ponto 8 | Plano da avaliação da conformidade/mercado (declaração UE, marcação CE, organismos notificados, registo na base de dados da UE); fora de um manual de engenharia de segurança — o cross-check do próprio Manual declara-o fora («não substitui»). |
| AIA-12-3 | Art. 12.º, n.º 3 | As especificidades dos sistemas de identificação biométrica (anexo III, ponto 1: registos do art. 12.º, n.º 3, e verificação por duas pessoas do art. 14.º, n.º 5) ficam fora de âmbito por decisão do lead; o desenvolvimento dessa aplicação segue o Manual como qualquer outra. A biometria como factor de autenticação pertence aos requisitos de autenticação (AUT-*). |
| AIA-14-5 | Art. 14.º, n.º 5 | As especificidades dos sistemas de identificação biométrica (anexo III, ponto 1: registos do art. 12.º, n.º 3, e verificação por duas pessoas do art. 14.º, n.º 5) ficam fora de âmbito por decisão do lead; o desenvolvimento dessa aplicação segue o Manual como qualquer outra. A biometria como factor de autenticação pertence aos requisitos de autenticação (AUT-*). |
| AIA-16-b | Art. 16.º, alínea b) | Identificação do prestador no sistema/embalagem: rotulagem de produto, plano da conformidade. |
| AIA-16-f | Art. 16.º, alínea f) | Plano da avaliação da conformidade/mercado (declaração UE, marcação CE, organismos notificados, registo na base de dados da UE); fora de um manual de engenharia de segurança — o cross-check do próprio Manual declara-o fora («não substitui»). |
| AIA-16-g | Art. 16.º, alínea g) | Plano da avaliação da conformidade/mercado (declaração UE, marcação CE, organismos notificados, registo na base de dados da UE); fora de um manual de engenharia de segurança — o cross-check do próprio Manual declara-o fora («não substitui»). |
| AIA-16-h | Art. 16.º, alínea h) | Plano da avaliação da conformidade/mercado (declaração UE, marcação CE, organismos notificados, registo na base de dados da UE); fora de um manual de engenharia de segurança — o cross-check do próprio Manual declara-o fora («não substitui»). |
| AIA-16-i | Art. 16.º, alínea i) | Plano da avaliação da conformidade/mercado (declaração UE, marcação CE, organismos notificados, registo na base de dados da UE); fora de um manual de engenharia de segurança — o cross-check do próprio Manual declara-o fora («não substitui»). |
| AIA-16-k | Art. 16.º, alínea k) | Relação com autoridades / regime sancionatório; plano jurídico, não de engenharia. |
| AIA-16-l | Art. 16.º, alínea l) | Requisitos de acessibilidade (Diretivas 2016/2102 e 2019/882): qualidade de produto, fora de um manual de engenharia de segurança. |
| AIA-17-1-d | Art. 17.º, n.º 1, alínea d) | O art. 17.º (sistema de gestão da qualidade) fica fora de âmbito por decisão do lead. |
| AIA-17-1-h | Art. 17.º, n.º 1, alínea h) | O art. 17.º (sistema de gestão da qualidade) fica fora de âmbito por decisão do lead. O plano do art. 72.º está em CTX-AIA-RE-R04. |
| AIA-17-3-4 | Art. 17.º, n.os 3 e 4 | Faculdade/presunção (não cria dever autónomo); plano da estratégia de conformidade. |
| AIA-21-1 | Art. 21.º, n.º 1 | Relação com autoridades / regime sancionatório; plano jurídico, não de engenharia. |
| AIA-22-1 | Art. 22.º, n.os 1-2 | Dever de outro operador económico (importador/distribuidor/mandatário), não do processo de engenharia do prestador ou do responsável pela implantação. |
| AIA-22-3 | Art. 22.º, n.º 3 | Dever de outro operador económico (importador/distribuidor/mandatário), não do processo de engenharia do prestador ou do responsável pela implantação. |
| AIA-22-4 | Art. 22.º, n.º 4 | Dever de outro operador económico (importador/distribuidor/mandatário), não do processo de engenharia do prestador ou do responsável pela implantação. |
| AIA-23-1 | Art. 23.º, n.º 1 | Dever de outro operador económico (importador/distribuidor/mandatário), não do processo de engenharia do prestador ou do responsável pela implantação. |
| AIA-23-2 | Art. 23.º, n.º 2 | Dever de outro operador económico (importador/distribuidor/mandatário), não do processo de engenharia do prestador ou do responsável pela implantação. |
| AIA-23-3 | Art. 23.º, n.º 3 | Dever de outro operador económico (importador/distribuidor/mandatário), não do processo de engenharia do prestador ou do responsável pela implantação. |
| AIA-23-4 | Art. 23.º, n.º 4 | Dever de outro operador económico (importador/distribuidor/mandatário), não do processo de engenharia do prestador ou do responsável pela implantação. |
| AIA-23-5 | Art. 23.º, n.º 5 | Dever de outro operador económico (importador/distribuidor/mandatário), não do processo de engenharia do prestador ou do responsável pela implantação. |
| AIA-23-6 | Art. 23.º, n.º 6 | Dever de outro operador económico (importador/distribuidor/mandatário), não do processo de engenharia do prestador ou do responsável pela implantação. |
| AIA-23-7 | Art. 23.º, n.º 7 | Dever de outro operador económico (importador/distribuidor/mandatário), não do processo de engenharia do prestador ou do responsável pela implantação. |
| AIA-24-1 | Art. 24.º, n.º 1 | Dever de outro operador económico (importador/distribuidor/mandatário), não do processo de engenharia do prestador ou do responsável pela implantação. |
| AIA-24-2 | Art. 24.º, n.º 2 | Dever de outro operador económico (importador/distribuidor/mandatário), não do processo de engenharia do prestador ou do responsável pela implantação. |
| AIA-24-3 | Art. 24.º, n.º 3 | Dever de outro operador económico (importador/distribuidor/mandatário), não do processo de engenharia do prestador ou do responsável pela implantação. |
| AIA-24-4 | Art. 24.º, n.º 4 | Dever de outro operador económico (importador/distribuidor/mandatário), não do processo de engenharia do prestador ou do responsável pela implantação. |
| AIA-24-5 | Art. 24.º, n.º 5 | Dever de outro operador económico (importador/distribuidor/mandatário), não do processo de engenharia do prestador ou do responsável pela implantação. |
| AIA-24-6 | Art. 24.º, n.º 6 | Dever de outro operador económico (importador/distribuidor/mandatário), não do processo de engenharia do prestador ou do responsável pela implantação. |
| AIA-25-1 | Art. 25.º, n.º 1 | Qualificação jurídica de quem se torna prestador. |
| AIA-25-3 | Art. 25.º, n.º 3 | Disposição delimitadora de âmbito, definição ou qualificação jurídica; não cria dever de engenharia. |
| AIA-25-5 | Art. 25.º, n.º 5 | Disposição delimitadora de âmbito, definição ou qualificação jurídica; não cria dever de engenharia. |
| AIA-26-7 | Art. 26.º, n.º 7 | Informação e consulta de trabalhadores: direito do trabalho/RH. |
| AIA-26-8 | Art. 26.º, n.º 8 | Plano da avaliação da conformidade/mercado (declaração UE, marcação CE, organismos notificados, registo na base de dados da UE); fora de um manual de engenharia de segurança — o cross-check do próprio Manual declara-o fora («não substitui»). |
| AIA-26-10 | Art. 26.º, n.º 10 | Autorização judicial/administrativa para biometria em diferido para aplicação da lei; plano jurídico. |
| AIA-26-12 | Art. 26.º, n.º 12 | Relação com autoridades / regime sancionatório; plano jurídico, não de engenharia. |
| AIA-27-3 | Art. 27.º, n.º 3 | Relação com autoridades / regime sancionatório; plano jurídico, não de engenharia. |
| AIA-41-5 | Art. 41.º, n.º 5 | Justificação de soluções alternativas a especificações comuns: plano da conformidade. |
| AIA-42-1 | Art. 42.º, n.º 1 | Faculdade/presunção (não cria dever autónomo); plano da estratégia de conformidade. |
| AIA-42-2 | Art. 42.º, n.º 2 | Faculdade/presunção (não cria dever autónomo); plano da estratégia de conformidade. |
| AIA-43-1 | Art. 43.º, n.º 1 | Plano da avaliação da conformidade/mercado (declaração UE, marcação CE, organismos notificados, registo na base de dados da UE); fora de um manual de engenharia de segurança — o cross-check do próprio Manual declara-o fora («não substitui»). |
| AIA-43-2 | Art. 43.º, n.º 2 | Plano da avaliação da conformidade/mercado (declaração UE, marcação CE, organismos notificados, registo na base de dados da UE); fora de um manual de engenharia de segurança — o cross-check do próprio Manual declara-o fora («não substitui»). |
| AIA-43-3 | Art. 43.º, n.º 3 | Plano da avaliação da conformidade/mercado (declaração UE, marcação CE, organismos notificados, registo na base de dados da UE); fora de um manual de engenharia de segurança — o cross-check do próprio Manual declara-o fora («não substitui»). |
| AIA-47-1 | Art. 47.º, n.º 1 | Plano da avaliação da conformidade/mercado (declaração UE, marcação CE, organismos notificados, registo na base de dados da UE); fora de um manual de engenharia de segurança — o cross-check do próprio Manual declara-o fora («não substitui»). |
| AIA-47-2 | Art. 47.º, n.º 2 | Plano da avaliação da conformidade/mercado (declaração UE, marcação CE, organismos notificados, registo na base de dados da UE); fora de um manual de engenharia de segurança — o cross-check do próprio Manual declara-o fora («não substitui»). |
| AIA-47-3 | Art. 47.º, n.º 3 | Plano da avaliação da conformidade/mercado (declaração UE, marcação CE, organismos notificados, registo na base de dados da UE); fora de um manual de engenharia de segurança — o cross-check do próprio Manual declara-o fora («não substitui»). |
| AIA-47-4 | Art. 47.º, n.º 4 | Plano da avaliação da conformidade/mercado (declaração UE, marcação CE, organismos notificados, registo na base de dados da UE); fora de um manual de engenharia de segurança — o cross-check do próprio Manual declara-o fora («não substitui»). |
| AIA-AnxV | Anexo V | Plano da avaliação da conformidade/mercado (declaração UE, marcação CE, organismos notificados, registo na base de dados da UE); fora de um manual de engenharia de segurança — o cross-check do próprio Manual declara-o fora («não substitui»). |
| AIA-48-2 | Art. 48.º, n.º 2 | Plano da avaliação da conformidade/mercado (declaração UE, marcação CE, organismos notificados, registo na base de dados da UE); fora de um manual de engenharia de segurança — o cross-check do próprio Manual declara-o fora («não substitui»). A implementação técnica da marcação CE digital é trivial face ao dever. |
| AIA-48-3 | Art. 48.º, n.os 3-5 | Plano da avaliação da conformidade/mercado (declaração UE, marcação CE, organismos notificados, registo na base de dados da UE); fora de um manual de engenharia de segurança — o cross-check do próprio Manual declara-o fora («não substitui»). |
| AIA-49-1 | Art. 49.º, n.º 1 | Plano da avaliação da conformidade/mercado (declaração UE, marcação CE, organismos notificados, registo na base de dados da UE); fora de um manual de engenharia de segurança — o cross-check do próprio Manual declara-o fora («não substitui»). |
| AIA-49-2 | Art. 49.º, n.º 2 | Plano da avaliação da conformidade/mercado (declaração UE, marcação CE, organismos notificados, registo na base de dados da UE); fora de um manual de engenharia de segurança — o cross-check do próprio Manual declara-o fora («não substitui»). |
| AIA-49-3 | Art. 49.º, n.º 3 | Plano da avaliação da conformidade/mercado (declaração UE, marcação CE, organismos notificados, registo na base de dados da UE); fora de um manual de engenharia de segurança — o cross-check do próprio Manual declara-o fora («não substitui»). |
| AIA-49-4 | Art. 49.º, n.º 4 | Plano da avaliação da conformidade/mercado (declaração UE, marcação CE, organismos notificados, registo na base de dados da UE); fora de um manual de engenharia de segurança — o cross-check do próprio Manual declara-o fora («não substitui»). |
| AIA-49-5 | Art. 49.º, n.º 5 | Plano da avaliação da conformidade/mercado (declaração UE, marcação CE, organismos notificados, registo na base de dados da UE); fora de um manual de engenharia de segurança — o cross-check do próprio Manual declara-o fora («não substitui»). |
| AIA-AnxVIII-A | Anexo VIII, secção A | Plano da avaliação da conformidade/mercado (declaração UE, marcação CE, organismos notificados, registo na base de dados da UE); fora de um manual de engenharia de segurança — o cross-check do próprio Manual declara-o fora («não substitui»). |
| AIA-AnxVIII-B | Anexo VIII, secção B | Plano da avaliação da conformidade/mercado (declaração UE, marcação CE, organismos notificados, registo na base de dados da UE); fora de um manual de engenharia de segurança — o cross-check do próprio Manual declara-o fora («não substitui»). |
| AIA-AnxVIII-C | Anexo VIII, secção C | Plano da avaliação da conformidade/mercado (declaração UE, marcação CE, organismos notificados, registo na base de dados da UE); fora de um manual de engenharia de segurança — o cross-check do próprio Manual declara-o fora («não substitui»). |
| AIA-AnxVII-3 | Anexo VII, pontos 3.1, 3.3, 3.4 | Plano da avaliação da conformidade/mercado (declaração UE, marcação CE, organismos notificados, registo na base de dados da UE); fora de um manual de engenharia de segurança — o cross-check do próprio Manual declara-o fora («não substitui»). |
| AIA-AnxVII-5 | Anexo VII, ponto 5.2 | Plano da avaliação da conformidade/mercado (declaração UE, marcação CE, organismos notificados, registo na base de dados da UE); fora de um manual de engenharia de segurança — o cross-check do próprio Manual declara-o fora («não substitui»). |
| AIA-AnxIII-1 | Anexo III, ponto 1 | Definição dos casos de uso de risco elevado; o dever operativo está em AIA-6-2-3 (lacuna: o Manual não liga o estatuto legal à classificação). |
| AIA-AnxIII-2 | Anexo III, ponto 2 | Definição dos casos de uso de risco elevado; o dever operativo está em AIA-6-2-3 (lacuna: o Manual não liga o estatuto legal à classificação). |
| AIA-AnxIII-3 | Anexo III, ponto 3 | Definição dos casos de uso de risco elevado; o dever operativo está em AIA-6-2-3 (lacuna: o Manual não liga o estatuto legal à classificação). |
| AIA-AnxIII-4 | Anexo III, ponto 4 | Definição dos casos de uso de risco elevado; o dever operativo está em AIA-6-2-3 (lacuna: o Manual não liga o estatuto legal à classificação). |
| AIA-AnxIII-5 | Anexo III, ponto 5 | Definição dos casos de uso de risco elevado; o dever operativo está em AIA-6-2-3 (lacuna: o Manual não liga o estatuto legal à classificação). |
| AIA-AnxIII-6 | Anexo III, ponto 6 | Definição dos casos de uso de risco elevado; o dever operativo está em AIA-6-2-3 (lacuna: o Manual não liga o estatuto legal à classificação). |
| AIA-AnxIII-7 | Anexo III, ponto 7 | Definição dos casos de uso de risco elevado; o dever operativo está em AIA-6-2-3 (lacuna: o Manual não liga o estatuto legal à classificação). |
| AIA-AnxIII-8 | Anexo III, ponto 8 | Definição dos casos de uso de risco elevado; o dever operativo está em AIA-6-2-3 (lacuna: o Manual não liga o estatuto legal à classificação). |
| AIA-50-4-b | Art. 50.º, n.º 4, segundo parágrafo | Divulgação de texto gerado por IA publicado sobre interesse público, com exceção de controlo editorial: processo editorial do responsável pela implantação. |
| AIA-52-1 | Art. 52.º, n.os 1-2 | Obrigação do prestador de modelo GPAI perante a Comissão/Serviço para a IA; plano jurídico e de domínio de IA. O Manual trata o lado do consumidor de GPAI (DEP-014, Política 33 §10.6). |
| AIA-53-1-c | Art. 53.º, n.º 1, alínea c) | Política de direitos de autor/opt-out TDM: plano jurídico. |
| AIA-53-1-d | Art. 53.º, n.º 1, alínea d) | Resumo público dos conteúdos de treino segundo modelo do Serviço para a IA: plano jurídico/domínio de IA. |
| AIA-53-3 | Art. 53.º, n.º 3 | Relação com autoridades / regime sancionatório; plano jurídico, não de engenharia. |
| AIA-53-4 | Art. 53.º, n.º 4 | Faculdade/presunção (não cria dever autónomo); plano da estratégia de conformidade. |
| AIA-54-1 | Art. 54.º, n.os 1-2 | Dever de outro operador económico (importador/distribuidor/mandatário), não do processo de engenharia do prestador ou do responsável pela implantação. |
| AIA-54-3 | Art. 54.º, n.os 3-5 | Dever de outro operador económico (importador/distribuidor/mandatário), não do processo de engenharia do prestador ou do responsável pela implantação. |
| AIA-55-2 | Art. 55.º, n.º 2 | Faculdade/presunção (não cria dever autónomo); plano da estratégia de conformidade. |
| AIA-91-5 | Art. 91.º, n.º 5 | Relação com autoridades / regime sancionatório; plano jurídico, não de engenharia. |
| AIA-92-5 | Art. 92.º, n.os 3 e 5 | Relação com autoridades / regime sancionatório; plano jurídico, não de engenharia. |
| AIA-57-12 | Art. 57.º, n.º 12 | Relação com autoridades / regime sancionatório; plano jurídico, não de engenharia. |
| AIA-60-4 | Art. 60.º, n.º 4 | Condições regulamentares da testagem em condições reais (plano aprovado, registo, consentimento): plano jurídico. |
| AIA-60-9 | Art. 60.º, n.º 9 | Relação com autoridades / regime sancionatório; plano jurídico, não de engenharia. |
| AIA-61-1 | Art. 61.º | Consentimento informado dos participantes: plano jurídico/ético. |
| AIA-72-4 | Art. 72.º, n.º 4 | Faculdade/presunção (não cria dever autónomo); plano da estratégia de conformidade. |
| AIA-73-9-10 | Art. 73.º, n.os 9-10 | Disposição delimitadora de âmbito, definição ou qualificação jurídica; não cria dever de engenharia. |
| AIA-75-1E | Art. 75.º, n.º 1-E, segundo parágrafo | Relação com autoridades / regime sancionatório; plano jurídico, não de engenharia. |
| AIA-75c-3 | Art. 75.º-C, n.º 3 | Relação com autoridades / regime sancionatório; plano jurídico, não de engenharia. |
| AIA-80-4 | Art. 80.º, n.os 4, 5 e 7 | Reclassificação pela autoridade e sanção por classificação errada: plano jurídico. |
| AIA-83-1 | Art. 83.º, n.º 1 | Plano da avaliação da conformidade/mercado (declaração UE, marcação CE, organismos notificados, registo na base de dados da UE); fora de um manual de engenharia de segurança — o cross-check do próprio Manual declara-o fora («não substitui»). |
| AIA-87 | Art. 87.º | Canais de denúncia (Diretiva 2019/1937): RH/jurídico. |
| AIA-99-3 | Art. 99.º, n.º 3 | Relação com autoridades / regime sancionatório; plano jurídico, não de engenharia. |
| AIA-99-4 | Art. 99.º, n.º 4 | Relação com autoridades / regime sancionatório; plano jurídico, não de engenharia. |
| AIA-99-5 | Art. 99.º, n.º 5 | Relação com autoridades / regime sancionatório; plano jurídico, não de engenharia. |
| AIA-101-1 | Art. 101.º, n.º 1 | Relação com autoridades / regime sancionatório; plano jurídico, não de engenharia. |
| AIA-111-2 | Art. 111.º, n.º 2 | Disposição delimitadora de âmbito, definição ou qualificação jurídica; não cria dever de engenharia. |
| AIA-111-3 | Art. 111.º, n.º 3 | Disposição delimitadora de âmbito, definição ou qualificação jurídica; não cria dever de engenharia. |
| AIA-113-3 | Art. 113.º, terceiro parágrafo | Disposição delimitadora de âmbito, definição ou qualificação jurídica; não cria dever de engenharia. |
