---
id: lista-requisitos-base
title: Catálogo Base de Requisitos de Segurança
description: Catálogo canónico de requisitos de segurança aplicacional do SbD-ToE, organizado por domínio técnico, com aplicabilidade por nível de risco (L1–L3) e critérios de aceitação mínimos para validação, auditoria e integração em backlogs.
requirement_class: aplicacional
tags: [tipo:catalogo, classe:aplicacional, requisitos, segurança-aplicacional, rastreabilidade, L1, L2, L3, aceitacao, auditoria, ASVS, NIST-SSDF]
sidebar_position: 2
---

# 📋 Catálogo Base de Requisitos de Segurança

Este catálogo constitui a **referência canónica de requisitos de segurança aplicacional** do SbD-ToE. Cada requisito é identificado por um **ID canónico estável** (`CATEGORIA-NNN`), tem aplicabilidade definida por nível de risco (L1–L3) e um critério de aceitação mínimo que permite validação objectiva e integração directa em backlogs, definições de pronto e processos de auditoria.

---

## Âmbito: requisitos aplicacionais

Este catálogo cobre **requisitos de segurança intrínsecos ao software** - as propriedades que o sistema deve garantir em tempo de execução, independentemente de onde é deployed ou como a infraestrutura está definida. Incluem-se: autenticação e gestão de identidade, controlo de acesso, registo e monitorização, gestão de sessões, validação de dados, tratamento de erros, configuração segura de parâmetros da aplicação, segurança de APIs e integrações, e requisitos de processo como gestão de requisitos, distribuição de artefactos e ferramentas de desenvolvimento.

## Mapeamento de catálogos por domínio técnico {#mapeamento-de-catalogos}

O SbD-ToE organiza os requisitos de segurança em **catálogos canónicos por domínio técnico**, distribuídos pelos capítulos do manual. Cada catálogo tem prefixo próprio, responsável típico e artefacto de referência distinto. Este é o mapa completo:

| Cap. | Prefixo(s) | Domínio | Objecto | Responsável típico |
|------|-----------|---------|---------|-------------------|
| 01 | `CLA` | Classificação de aplicações | Classificação formal de criticidade, reclassificação, risco residual e proporcionalidade de controlos | Product Owner, Tech Lead, AppSec, GRC |
| 02 | `AUT` `ACC` `LOG` `SES` `VAL` `ERR` `CFG` `ENC` `API` `INT` `REQ` `DST` `IDE` | Requisitos aplicacionais | Propriedades de segurança do software em runtime | Equipa de desenvolvimento |
| 03 | `THR` | Threat modeling | Identificação de ameaças, disposição formal, derivação de requisitos e rastreabilidade | Arquitecto técnico, AppSec |
| 04 | `ARC` | Arquitectura segura | Design, estrutura e decisões do sistema | Arquitecto técnico, AppSec |
| 05 | `DEP` | Dependências, SBOM e SCA | Componentes de terceiros incorporados | Equipa de desenvolvimento, AppSec |
| 06 | `DEV` | Desenvolvimento seguro | Práticas e processos de desenvolvimento | Equipa de desenvolvimento, AppSec |
| 07 | `CIC` | CI/CD seguro | O pipeline como produto de engenharia | DevSecOps, plataforma |
| 08 | `IAC` | Infraestrutura como Código | O projecto IaC como software | Engenharia de plataforma, DevSecOps |
| 09 | `CNT` | Containers e imagens | O artefacto container e políticas de execução | DevSecOps, desenvolvimento |
| 10 | `TST` | Testes de segurança | O programa de testes de segurança | AppSec, DevSecOps |
| 11 | `DPL` | Deploy seguro | O processo de promoção a produção | DevSecOps, Release Management |
| 12 | `OPS` | Monitorização e operações | O programa de monitorização operacional | Operations, SOC, DevSecOps |
| 13 | `TRN` | Formação e onboarding | Capacitação, onboarding verificável, Security Champions e eficácia formativa | AppSec, PeopleOps, liderança técnica |
| 14 | `GOV` | Governação e contratação | Modelo de governação, excepções, contratação e maturidade organizacional | AppSec, GRC, CISO |

Cada capítulo contém o seu catálogo em `addon/00-catalogo-requisitos.md` (ou equivalente), com aplicabilidade por nível de risco (L1–L3) e critérios de aceitação no mesmo formato deste catálogo. A distinção entre catálogos é operacionalmente relevante: responsáveis, artefactos e ciclos de revisão diferem por domínio - um requisito do tipo `ARC-` é avaliado em revisão de arquitectura, não num PR de código.

---

> **Sobre a curadoria:** Este catálogo foi consolidado a partir de fontes reconhecidas - OWASP ASVS, NIST SSDF, IEC 62443, entre outras - e destina-se a ser **adaptado por cada organização e instanciado por cada projecto**. Não é imutável: deve ser mantido como documento vivo, revisto periodicamente e ajustado ao contexto técnico e de risco. Quando um projecto não tem catálogo próprio, este serve de ponto de partida directo.

Para a instanciação em projecto e a nomenclatura operacional de rastreabilidade (`SEC-Lx-DOMINIO-CODIGO`), ver [Taxonomia e Rastreabilidade](./taxonomia-rastreabilidade).

---

## Convenções

| Símbolo | Significado |
|---------|-------------|
| ✔ | Requisito obrigatório para este nível |
| - | Não aplicável ou não obrigatório a este nível |

Os níveis são cumulativos: L3 inclui todos os requisitos de L1 e L2; L2 inclui todos os de L1.

---

## Índice

- [AUT - Autenticação e Identidade](#aut)
- [ACC - Controlo de Acesso](#acc)
- [LOG - Registo e Monitorização](#log)
- [SES - Sessões e Estado](#ses)
- [VAL - Validação de Dados](#val)
- [ERR - Gestão de Erros](#err)
- [CFG - Configuração Segura](#cfg)
- [ENC - Dados Sensíveis e Criptografia](#enc)
- [API - Segurança de APIs](#api)
- [INT - Mensagens e Integrações](#int)
- [REQ - Definição de Requisitos](#req)
- [DST - Distribuição de Artefactos](#dst)
- [IDE - Ferramentas de Desenvolvimento](#ide)

---

## AUT - Autenticação e Identidade {#aut}

Requisitos que garantem que apenas entidades legítimas acedem ao sistema, com controlos proporcionais à sensibilidade das operações.

| ID | Nome | L1 | L2 | L3 | Critério de aceitação |
|----|------|:--:|:--:|:--:|----------------------|
| AUT-001 | MFA obrigatório | - | ✔ | ✔ | Login sem segundo factor é rejeitado; evidência de bloqueio em logs. |
| AUT-002 | Política de passwords | ✔ | ✔ | ✔ | Sistema rejeita passwords que não cumpram a política; bloqueio evidenciado em teste. |
| AUT-003 | Protecção contra brute force | ✔ | ✔ | ✔ | Conta bloqueada ou acesso atrasado após N tentativas falhadas; logs evidenciam o evento. |
| AUT-004 | Revogação activa de sessões | ✔ | ✔ | ✔ | Logout invalida token/sessão imediatamente; reutilização resulta em erro autenticado. |
| AUT-005 | Expiração automática de sessão | ✔ | ✔ | ✔ | Sessão termina após período de inactividade configurado; redirect para autenticação. |
| AUT-006 | Proibição de credenciais em claro | ✔ | ✔ | ✔ | Auditoria confirma hashing com salt; ausência de credenciais em claro em armazenamento e transmissão. |
| AUT-007 | Suporte a autenticação federada | - | ✔ | ✔ | Fluxo SAML/OIDC funcional e testado; log de autenticação via IdP externo disponível. |
| AUT-008 | Step-up para acções sensíveis | - | ✔ | ✔ | Operações críticas requerem factor adicional; teste evidencia bloqueio sem step-up. |
| AUT-009 | Reautenticação para alterações críticas | ✔ | ✔ | ✔ | Alterações de credenciais ou dados sensíveis exigem confirmação da identidade activa. |
| AUT-010 | Alerta de acessos suspeitos | - | ✔ | ✔ | Acessos anómalos geram alerta ou notificação ao utilizador; log do evento disponível. |

---

## ACC - Controlo de Acesso {#acc}

Requisitos que asseguram que cada entidade acede apenas aos recursos e operações que lhe são explicitamente permitidos.

| ID | Nome | L1 | L2 | L3 | Critério de aceitação |
|----|------|:--:|:--:|:--:|----------------------|
| ACC-001 | Controlo de acesso RBAC | ✔ | ✔ | ✔ | Perfis e permissões mapeados; role com privilégio reduzido não acede a recursos restritos. |
| ACC-002 | Princípio do menor privilégio | ✔ | ✔ | ✔ | Contas sem permissões desnecessárias; auditoria evidencia restrição efectiva. |
| ACC-003 | Bloqueio e auditoria de acessos ilegítimos | ✔ | ✔ | ✔ | Tentativas de acesso não autorizado são bloqueadas e registadas com contexto suficiente. |
| ACC-004 | Separação de perfis | ✔ | ✔ | ✔ | Perfis de utilizador, administrador e serviço são distintos; acções de cada perfil são rastreáveis. |
| ACC-005 | Controlo de acesso a APIs e serviços | ✔ | ✔ | ✔ | Endpoints rejeitam chamadas não autenticadas ou não autorizadas; logs registam rejeições. |
| ACC-006 | Protecção de recursos sensíveis | ✔ | ✔ | ✔ | Acesso não autorizado a dados críticos é impedido e registado; teste de bypasse falha. |
| ACC-007 | Validação do modelo de acesso | - | ✔ | ✔ | Modelo de permissões revisto e documentado; ameaças de controlo de acesso mapeadas. |
| ACC-008 | Revogação em tempo real | ✔ | ✔ | ✔ | Remoção de acesso reflecte-se imediatamente; teste de permissão falha após revogação. |
| ACC-009 | Autorização baseada em atributos (ABAC) | - | - | ✔ | Decisão de acesso depende de atributos dinâmicos; logs evidenciam avaliação de política. |
| ACC-010 | Revisão periódica de permissões | - | ✔ | ✔ | Auditorias periódicas removem permissões obsoletas; registos de revisão mantidos e datados. |

---

## LOG - Registo e Monitorização {#log}

Requisitos que garantem a existência de evidência auditável das operações do sistema, suportando detecção de incidentes e resposta forense.

| ID | Nome | L1 | L2 | L3 | Critério de aceitação |
|----|------|:--:|:--:|:--:|----------------------|
| LOG-001 | Registo de eventos críticos | ✔ | ✔ | ✔ | Acessos, alterações e falhas de segurança críticas são registados; logs verificados por amostragem. |
| LOG-002 | Atributos mínimos em logs | ✔ | ✔ | ✔ | Cada entrada inclui: quem, quando, o quê e onde; ausência de qualquer atributo falha auditoria. |
| LOG-003 | Protecção de integridade e acesso aos logs | ✔ | ✔ | ✔ | Logs não alteráveis por utilizadores comuns; protecção por permissões ou assinatura verificável. |
| LOG-004 | Análise periódica de logs | - | ✔ | ✔ | Processo de análise periódica documentado e evidenciado; frequência proporcional ao risco. |
| LOG-005 | Retenção mínima dos logs | ✔ | ✔ | ✔ | Logs mantidos pelo período definido em política; verificação de retenção efectiva. |
| LOG-006 | Envio para sistema centralizado | - | ✔ | ✔ | Eventos críticos enviados e registados em agregador central (SIEM ou equivalente). |
| LOG-007 | Classificação e detecção de anomalias | - | ✔ | ✔ | Política de severidade definida; anomalias disparam alertas configurados e testados. |
| LOG-008 | Alarme em falhas do mecanismo de logging | - | ✔ | ✔ | Falhas do sistema de logging geram alerta; ausência de logs é detectada e notificada. |
| LOG-009 | Logs suportam resposta a incidentes | - | ✔ | ✔ | Logs com detalhe suficiente para reconstrução de incidente; testado em exercício ou simulação. |
| LOG-010 | Logging de eventos críticos de negócio | - | - | ✔ | Eventos de impacto no negócio (transacções, autorizações críticas) registados e rastreáveis. |

---

## SES - Sessões e Estado {#ses}

Requisitos que controlam o ciclo de vida de sessões e tokens, prevenindo reutilização, fixação e persistência indevida.

| ID | Nome | L1 | L2 | L3 | Critério de aceitação |
|----|------|:--:|:--:|:--:|----------------------|
| SES-001 | Expiração automática por inactividade | ✔ | ✔ | ✔ | Sessão termina após período configurado de inactividade; redirect para autenticação. |
| SES-002 | Logout manual e após alteração de credenciais | ✔ | ✔ | ✔ | Logout termina todas as sessões activas; alteração de password invalida tokens anteriores. |
| SES-003 | Identificadores de sessão imprevisíveis | ✔ | ✔ | ✔ | Tokens/sessões com entropia adequada; análise de previsibilidade não revela padrão. |
| SES-004 | Transmissão segura dos tokens | ✔ | ✔ | ✔ | Tokens transmitidos apenas por canais TLS; cookies com flags Secure e HttpOnly. |
| SES-005 | Ligação da sessão ao contexto do cliente | - | ✔ | ✔ | Mudança de IP ou user-agent termina sessão ou exige revalidação; teste evidencia comportamento. |
| SES-006 | Revogação explícita da sessão | ✔ | ✔ | ✔ | Sessão pode ser terminada a pedido do utilizador ou do sistema; token fica inválido imediatamente. |
| SES-007 | Prevenção de sessões long-lived | - | ✔ | ✔ | TTL máximo configurado e aplicado; sessões com duração excessiva não são possíveis. |
| SES-008 | Scope, TTL e revogação de tokens JWT | - | ✔ | ✔ | JWTs incluem claims de âmbito e expiração; mecanismo de revogação implementado e testado. |

---

## VAL - Validação de Dados {#val}

Requisitos que garantem que apenas dados bem formados e esperados são processados pelo sistema, prevenindo injecções e comportamentos não determinísticos.

| ID | Nome | L1 | L2 | L3 | Critério de aceitação |
|----|------|:--:|:--:|:--:|----------------------|
| VAL-001 | Validação geral de entradas externas | ✔ | ✔ | ✔ | Inputs inválidos são rejeitados com código de erro adequado; logs evidenciam bloqueio. |
| VAL-002 | Uso de whitelists em vez de blacklists | ✔ | ✔ | ✔ | Apenas valores explicitamente aceites são permitidos; valores não previstos são rejeitados. |
| VAL-003 | Validadores de esquema (JSON/XML schema) | - | ✔ | ✔ | Payloads malformados são rejeitados automaticamente; logs de parsing disponíveis. |
| VAL-004 | Sanitização contra injecções | ✔ | ✔ | ✔ | Inputs potencialmente perigosos são neutralizados; ataques de injecção resultam em falha controlada. |
| VAL-005 | Validação antes do uso interno | ✔ | ✔ | ✔ | Dados são validados antes de uso em lógica de negócio ou persistência; não há caminhos não validados. |
| VAL-006 | Mensagens de erro seguras na validação | ✔ | ✔ | ✔ | Erros de validação não expõem lógica interna nem dados sensíveis ao cliente. |
| VAL-007 | Testes automáticos contra entradas maliciosas | - | ✔ | ✔ | Testes automatizados cobrem XSS, SQLi e outras injecções relevantes; resultados registados. |

---

## ERR - Gestão de Erros {#err}

Requisitos que asseguram que erros e excepções são tratados de forma controlada, sem exposição de informação sensível ou lógica interna.

| ID | Nome | L1 | L2 | L3 | Critério de aceitação |
|----|------|:--:|:--:|:--:|----------------------|
| ERR-001 | Erros não expõem dados sensíveis | ✔ | ✔ | ✔ | Mensagens ao cliente são abstractas; logs internos detalhados nunca expostos externamente. |
| ERR-002 | Mensagens genéricas no cliente | ✔ | ✔ | ✔ | Cliente recebe sempre mensagem genérica; stack traces e detalhes internos não transmitidos. |
| ERR-003 | Não revelar existência de recursos | ✔ | ✔ | ✔ | Respostas de erro são idênticas para recursos existentes e inexistentes (sem enumeração). |
| ERR-004 | Mensagens localizadas e seguras | ✔ | ✔ | ✔ | Mensagens traduzidas sem conteúdo executável ou referências a lógica interna. |
| ERR-005 | Gestão padronizada e centralizada | - | ✔ | ✔ | Framework de erros centraliza tratamento e logging; ausência de tratamento ad-hoc disperso. |
| ERR-006 | Testes automáticos para erros excessivos | - | ✔ | ✔ | Testes garantem que erros são tratados e não há fuga de informação; cobertura de casos limite. |
| ERR-007 | Logs de erro com contexto pseudonimizado | - | ✔ | ✔ | Logs incluem IDs contextuais; dados pessoais ou credenciais nunca registados em logs de erro. |

---

## CFG - Configuração Segura {#cfg}

Requisitos que garantem que o sistema é configurado e operado de forma que minimize a superfície de ataque e previna exposição acidental.

| ID | Nome | L1 | L2 | L3 | Critério de aceitação |
|----|------|:--:|:--:|:--:|----------------------|
| CFG-001 | Debug e flags desactivados em produção | ✔ | ✔ | ✔ | Parâmetros de debug, trace e dev_mode desligados em produção; verificação automática no pipeline. |
| CFG-002 | Separação de ambientes com validação automática | ✔ | ✔ | ✔ | Deploys e testes apenas em ambientes segregados; logs evidenciam segregação efectiva. |
| CFG-003 | Ausência de parâmetros hardcoded | ✔ | ✔ | ✔ | Código fonte não contém segredos nem parâmetros sensíveis em claro; scan automatizado confirma. |
| CFG-004 | Configuração externa com permissões controladas | ✔ | ✔ | ✔ | Configuração é externa ao código; permissões de acesso ao repositório de configuração são restritivas. |
| CFG-005 | Validação de configuração no arranque | - | ✔ | ✔ | Sistema falha arranque quando parâmetros obrigatórios estão em falta ou incorrectos; erro explícito. |
| CFG-006 | Uso de cofres e gestão segura de segredos | - | ✔ | ✔ | Segredos existem apenas em cofres seguros; auditoria evidencia ausência de segredos no repositório. |
| CFG-007 | Monitorização de drift de configuração | - | - | ✔ | Alterações inesperadas em configuração crítica disparam alertas; baseline documentada. |

---

## ENC - Dados Sensíveis e Criptografia {#enc}

Requisitos que garantem a protecção de dados sensíveis em trânsito e em repouso, o uso de primitivas criptográficas robustas e a prevenção de exposição acidental de segredos e dados pessoais.

| ID | Nome | L1 | L2 | L3 | Critério de aceitação |
|----|------|:--:|:--:|:--:|----------------------|
| ENC-001 | Encriptação de todas as comunicações em trânsito | ✔ | ✔ | ✔ | Toda a comunicação entre cliente e servidor e entre serviços internos usa TLS com versão mínima definida; versões inseguras (TLS 1.0, 1.1, SSLv3) desactivadas e verificáveis por configuração. |
| ENC-002 | Encriptação de dados sensíveis em repouso | - | ✔ | ✔ | Dados classificados como sensíveis (PII, credenciais, dados financeiros) encriptados em armazenamento persistente; chaves de encriptação geridas separadamente dos dados; evidência de aplicação a todos os datastores relevantes. |
| ENC-003 | Algoritmos e configurações criptográficas robustas | - | ✔ | ✔ | Apenas algoritmos aprovados e tamanhos de chave adequados em uso (ex: AES-256, RSA ≥ 2048, curvas elípticas aprovadas); algoritmos fracos ou deprecados (MD5, SHA-1 para integridade, DES) ausentes; lista de primitivas aprovadas documentada. |
| ENC-004 | Hashing adaptativo de passwords | ✔ | ✔ | ✔ | Passwords armazenadas com algoritmo adaptativo resistente a força bruta (bcrypt, Argon2, PBKDF2); factor de custo configurado e revisto periodicamente; ausência de hashing estático ou reversível confirmada. |
| ENC-005 | Mascaramento de dados sensíveis em logs, outputs e respostas API | ✔ | ✔ | ✔ | Passwords, tokens, números de cartão, dados pessoais sensíveis não aparecem em claro em logs, respostas de erro ou outputs de debugging; cobertura verificada por análise de logs e teste. |
| ENC-006 | Detecção e prevenção de segredos expostos em repositórios | ✔ | ✔ | ✔ | Ferramenta de detecção de segredos activa no pipeline (ex: truffleHog, gitleaks, detect-secrets); commits com segredos detectados bloqueados ou alertados; sem segredos em claro no histórico do repositório. |
| ENC-007 | Rotação periódica de chaves e segredos | - | ✔ | ✔ | Política de rotação definida por tipo de segredo; rotação executada nos prazos definidos; evidência de rotação auditável; ausência de chaves sem data de expiração para material crítico. |
| ENC-008 | Prevenção de caching de dados sensíveis no cliente | - | ✔ | ✔ | Respostas com dados sensíveis incluem cabeçalhos que inibem caching (Cache-Control: no-store, etc.); configuração verificável por análise de headers em ambiente de teste. |
| ENC-009 | Integridade verificável de dados críticos | - | - | ✔ | Dados críticos com mecanismo de verificação de integridade (MACs, assinaturas, checksums); adulterações detectadas e registadas; cobertura aplicada a dados com impacto de negócio ou regulatório. |

---

## API - Segurança de APIs {#api}

Requisitos específicos para superfícies de API, que constituem o vector de exposição mais frequente em aplicações modernas.

| ID | Nome | L1 | L2 | L3 | Critério de aceitação |
|----|------|:--:|:--:|:--:|----------------------|
| API-001 | Autenticação e autorização de chamadas API | ✔ | ✔ | ✔ | Endpoints rejeitam chamadas sem autenticação/autorização válida; chamadas anónimas falham. |
| API-002 | Endpoints desnecessários removidos ou ocultos | ✔ | ✔ | ✔ | Endpoints de debug ou legacy não expostos em produção; apenas em ambientes de teste controlados. |
| API-003 | Validação de input em APIs | ✔ | ✔ | ✔ | Inputs malformados são rejeitados; logs registam tentativa com contexto mínimo. |
| API-004 | Rate limiting e detecção de abusos | - | ✔ | ✔ | Limite configurado e activo; chamadas excessivas resultam em 429 ou bloqueio temporário. |
| API-005 | Protecção por TLS e certificados actualizados | ✔ | ✔ | ✔ | Canal TLS obrigatório; certificados válidos; cabeçalhos de segurança (HSTS, etc.) activos. |
| API-006 | Verificação de SDKs e wrappers utilizados | ✔ | ✔ | ✔ | Dependências e versões documentadas em SBOM; auditoria de licenças e vulnerabilidades conhecidas. |
| API-007 | Logging e auditoria de chamadas externas | - | ✔ | ✔ | Chamadas externas registadas com dados essenciais (origem, destino, resultado, timestamp). |

---

## INT - Mensagens e Integrações {#int}

Requisitos que asseguram a segurança nas comunicações entre sistemas, prevenindo intercepção, falsificação e injecção em canais de integração.

| ID | Nome | L1 | L2 | L3 | Critério de aceitação |
|----|------|:--:|:--:|:--:|----------------------|
| INT-001 | Validação de mensagens entre sistemas | ✔ | ✔ | ✔ | Mensagens malformadas são rejeitadas ou tratadas de forma controlada; sem processamento cego. |
| INT-002 | Autenticação mútua ou tokens seguros | ✔ | ✔ | ✔ | Integrações só aceites de fontes autenticadas; tokens verificados e com TTL definido. |
| INT-003 | Transmissão cifrada com TLS | ✔ | ✔ | ✔ | Todo o tráfego entre sistemas cifrado com TLS; versões inseguras desactivadas. |
| INT-004 | Proibição de protocolos inseguros | ✔ | ✔ | ✔ | Protocolos sem cifra (HTTP, FTP, Telnet) rejeitados ou redirecionados para equivalente seguro. |
| INT-005 | Assinatura e integridade de mensagens | - | ✔ | ✔ | Mensagens sensíveis assinadas e verificadas; logs evidenciam verificação de integridade. |
| INT-006 | Validação cruzada de origem e destino | - | ✔ | ✔ | Apenas origens e destinos autorizados aceites; logs de rejeição mantidos. |
| INT-007 | Monitorização e detecção de padrões anómalos | - | - | ✔ | Comportamento anómalo nos canais de integração dispara alertas; logs analisados periodicamente. |
| INT-008 | Revisão de segurança e contrato em integrações | - | - | ✔ | Integrações documentadas com cláusulas de segurança; checklist de revisão executada. |

---

## REQ - Definição de Requisitos {#req}

Requisitos que asseguram a incorporação sistemática da segurança no processo de definição e gestão de requisitos do ciclo de vida.

| ID | Nome | L1 | L2 | L3 | Critério de aceitação |
|----|------|:--:|:--:|:--:|----------------------|
| REQ-001 | Inclusão de requisitos de segurança | ✔ | ✔ | ✔ | Requisitos de segurança explícitos em backlog/documentação; marcados e rastreáveis. |
| REQ-002 | Revisão formal de segurança dos requisitos | ✔ | ✔ | ✔ | Processo de revisão documentado e evidenciado; responsável identificado. |
| REQ-003 | Alinhamento com classificação de risco | ✔ | ✔ | ✔ | Mapeamento entre requisitos e nível de criticidade disponível e actualizado. |
| REQ-004 | Versionamento e gestão de requisitos | ✔ | ✔ | ✔ | Histórico de alterações disponível; controlo de versões aplicado ao catálogo do projecto. |
| REQ-005 | Nova análise de ameaça após alteração de requisito | - | ✔ | ✔ | Alterações relevantes disparam revisão de threat modeling; registo da decisão disponível. |
| REQ-006 | Rastreabilidade requisito → ameaça → teste | - | ✔ | ✔ | Matriz ou ferramenta demonstra ligação entre requisitos, ameaças identificadas e testes. |
| REQ-007 | Revisão iterativa com equipas | - | ✔ | ✔ | Alterações de requisitos discutidas, revistas e registadas em ciclos definidos. |

---

## DST - Distribuição de Artefactos {#dst}

Requisitos que garantem a integridade e rastreabilidade dos artefactos ao longo do processo de build, publicação e distribuição.

| ID | Nome | L1 | L2 | L3 | Critério de aceitação |
|----|------|:--:|:--:|:--:|----------------------|
| DST-001 | Repositórios autenticados e auditáveis | ✔ | ✔ | ✔ | Autenticação obrigatória e logs activos para acesso a repositórios de artefactos. |
| DST-002 | Aprovação para publicação pública | - | ✔ | ✔ | Publicação em registry público requer aprovação e documentação formal do processo. |
| DST-003 | Assinatura digital ou checksum | - | ✔ | ✔ | Artefactos assinados ou validados por hash antes de publicação; verificação automatizada. |
| DST-004 | Inclusão de SBOM nos artefactos | - | ✔ | ✔ | SBOM gerado e anexado a cada release; rastreabilidade de dependências disponível. |
| DST-005 | Acesso segregado por role e ambiente | - | ✔ | ✔ | Apenas utilizadores e automações autorizados acedem a artefactos de produção. |
| DST-006 | Deploy apenas via pipeline validado | - | ✔ | ✔ | Artefactos só deployados por pipeline controlado e auditado; sem deploy manual em produção. |
| DST-007 | Revogação e limpeza de artefactos comprometidos | ✔ | ✔ | ✔ | Versões comprometidas são removidas prontamente; utilizadores e dependentes notificados. |

---

## IDE - Ferramentas de Desenvolvimento {#ide}

Requisitos que controlam o ambiente de desenvolvimento como superfície de risco, prevenindo introdução de vulnerabilidades por ferramentas ou extensões não controladas.

| ID | Nome | L1 | L2 | L3 | Critério de aceitação |
|----|------|:--:|:--:|:--:|----------------------|
| IDE-001 | Ferramentas e IDEs autorizadas | ✔ | ✔ | ✔ | Apenas ferramentas aprovadas são utilizadas; lista mantida e actualizada pela organização. |
| IDE-002 | Actualização e gestão de vulnerabilidades | ✔ | ✔ | ✔ | IDEs e ferramentas mantidas actualizadas; histórico de actualizações disponível. |
| IDE-003 | Auditoria de código gerado por ferramentas | - | ✔ | ✔ | Código gerado por ferramentas ou assistentes é revisto antes de integração em produção. |
| IDE-004 | Extensões e plugins de fontes confiáveis | ✔ | ✔ | ✔ | Apenas extensões de fontes reconhecidas e verificadas são instaladas; logs de instalação. |
| IDE-005 | Controlo de permissões de extensões | - | ✔ | ✔ | Permissões de extensões revistas; apenas as necessárias concedidas; execução sandboxed. |
| IDE-006 | Limitação de ambientes locais sem controlo | - | ✔ | ✔ | Utilização de ambientes locais controlada; logs de rede ou proxy disponíveis quando aplicável. |

---

> Para validação detalhada por requisito, métodos de teste e evidências esperadas, ver [Validação de Requisitos](./validacao-requisitos).
> Para o modelo de rastreabilidade e instanciação em projecto, ver [Taxonomia e Rastreabilidade](./taxonomia-rastreabilidade).
> Para a matriz de aplicabilidade por domínio e nível de risco, ver [Matriz de Controlos por Risco](./matriz-controlos-por-risco).
