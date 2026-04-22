---
id: rastreabilidade
title: "Rastreabilidade — Capítulo 04: Arquitetura Segura"
description: Rastreabilidade das práticas de arquitetura segura face a frameworks normativos com pilot formal
tags: [rastreabilidade, arquitetura, ssdf, asvs, slsa, cis]
sidebar_position: 25

---


> **Método:** Ver [Metodologia de Validação de Claims](../../00-fundamentos/canon/26-metodologia-validacao-claims.md) para a baseline empírica dos autores, validação por índices semânticos, ontology backtrace e comparação com fontes externas.

# Rastreabilidade — Capítulo 04: Arquitetura Segura

Este capítulo define **padrões de arquitetura segura** — zonas de confiança, separação de funções, controlo de acesso por design — como fundação técnica verificável e rastreável.

---

## Camada AppSec Core

| Slice AppSec Core | Relevância |
|-------------------|-----------|
| ACO-ATB — Architecture & Trust Boundaries | Zonas de confiança, fronteiras e superfícies de ataque por design (primário) |
| ACO-ITS — Integration Trust & Service-to-Service Security | Integrações entre serviços e padrões de confiança inter-serviço (secundário) |
| ACO-IAT — Identity, Access & Session Trust | Autenticação e autorização por design; princípio do menor privilégio |

---

## Frameworks normativos — cobertura verificada

> Inclui apenas frameworks com pilot formal publicado no ExternalSourcesInventory.

> **Metodologia:** Cobertura verificada contra `ontology_discovery_units.jsonl` (4139 units, manual completo). "Explícito" = unit normative_weight strong/medium com heading directo. "Semântico" = conteúdo confirmado em addon ou via mapeamento de requisito canónico. "Parcial" = sem unit dedicado no capítulo.

| Framework | Requisito / Prática | Cobertura | Fonte verificada | Nota |
|-----------|--------------------|-----------|-----------------|----|
| SSDF PW.2 | Review the Software Design | ✅ Semântico | aplicacao_lifecycle (strong): US-03 — Revisão formal do design arquitetural | Revisão de arquitetura como disciplina de security review |
| ASVS authorization_and_least_privilege | Authorization & least privilege | ⚠️ Parcial | requirements_catalog (strong): Catálogo ARC — Arquitectura Segura | Presente; não embalado explicitamente como family ASVS |
| ASVS backend_component_authentication | Backend component auth | ⚠️ Parcial | requirements_catalog (strong): Catálogo ARC — Arquitectura Segura | Architecture e infra semantics |
| ASVS backend_least_privilege | Backend least privilege | ⚠️ Parcial | requirements_catalog (strong): Catálogo ARC — Arquitectura Segura | Presente; não embalado |
| ASVS architecture_and_dependency_hardening | Architecture hardening | ⚠️ Parcial | addon (medium): Modelos de Arquitetura Segura Reutilizáveis | Presente; embalagem mais específica necessária |
| ASVS identity_provider_and_federated_auth | Federated authentication | ⚠️ Parcial | addon (medium): Rastreabilidade Arquitetural | OAuth/OIDC semantics presentes |
| ASVS oauth_and_oidc_service_trust | OAuth & OIDC trust | ⚠️ Parcial | addon (medium): Rastreabilidade Arquitetural | Architecture e deploy semantics |
| ASVS secure_transport | Secure transport | ⚠️ Parcial | requirements_catalog (strong): Catálogo ARC — Arquitectura Segura | Architecture e deploy semantics |
| ASVS service_to_service_auth | Service-to-service auth | ⚠️ Parcial | requirements_catalog (strong): Catálogo ARC — Arquitectura Segura | Architecture e IaC |
| ASVS session_and_token_trust | Session & token trust | ⚠️ Parcial | addon (medium): Rastreabilidade Arquitetural | Architecture e deploy |
| ASVS frontend_browser_security | Frontend/browser security | ⚠️ Parcial | addon (medium): Modelos de Arquitetura Segura Reutilizáveis | Requirements e architecture |
| ASVS api_protocol_specific | API protocol specifics | ⚠️ Parcial | requirements_catalog (strong): Catálogo ARC — Arquitectura Segura | Architecture e deploy |
| ASVS v4 | ASVS4-REQ-V1.4.1 | ✅ Semântico | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Enforcement de acesso concentrado no servidor e fora do cliente |
| ASVS v4 | ASVS4-REQ-V1.4.2 | ✅ Semântico | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Modelo de acesso ajustável aos fluxos, papéis e contextos do sistema |
| ASVS v4 | ASVS4-REQ-V1.4.3 | ✅ Semântico | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Privilégio mínimo aplicado por função, recurso e serviço |
| ASVS v4 | ASVS4-REQ-V1.4.4 | ✅ Semântico | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Canal único de autorização para recursos protegidos |
| ASVS v4 | ASVS4-REQ-V1.10.1 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Versionamento e revisão formal deixam trilho das mudanças estruturais |
| ASVS v4 | ASVS4-REQ-V2.3.3 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Renovação de autenticadores temporários tratada como política de sessão |
| ASVS v4 | ASVS4-REQ-V2.7.4 | ✅ Semântico | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Canal fora de banda segregado nas fronteiras de confiança |
| ASVS v4 | ASVS4-REQ-V2.8.1 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Validade de OTP definida no desenho do fator de autenticação |
| ASVS v4 | ASVS4-REQ-V2.8.4 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | OTP de uso único alinhado com proteção contra replay |
| ASVS v4 | ASVS4-REQ-V2.8.7 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Biometria restringida a MFA real e não a fator isolado |
| ASVS v4 | ASVS4-REQ-V2.9.2 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Nonce desafiante com unicidade e robustez criptográfica |
| ASVS v4 | ASVS4-REQ-V4.2.2 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Funções autenticadas protegidas contra pedidos forjados |
| ASVS v4 | ASVS4-REQ-V4.3.2 | ✅ Semântico | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Exposição de diretórios e metadados reduzida por design |
| ASVS v4 | ASVS4-REQ-V5.1.1 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Entradas de múltiplas origens tratadas como uma só fronteira |
| ASVS v4 | ASVS4-REQ-V5.1.3 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Allow-lists aplicadas na fronteira de entrada do sistema |
| ASVS v4 | ASVS4-REQ-V6.1.3 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Dados financeiros tratados como domínio sensível protegido |
| ASVS v4 | ASVS4-REQ-V7.2.2 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Decisões de acesso com evidência útil para investigação |
| ASVS v4 | ASVS4-REQ-V7.4.2 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Falha controlada prevista na arquitetura de tratamento de erro |
| ASVS v4 | ASVS4-REQ-V8.1.3 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Superfície de pedido minimizada em parâmetros, headers e cookies |
| ASVS v4 | ASVS4-REQ-V8.2.3 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Dados autenticados removidos do lado cliente no fim da sessão |
| ASVS v4 | ASVS4-REQ-V10.2.1 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Capacidades de recolha remota sujeitas a controlo e consentimento |
| ASVS v4 | ASVS4-REQ-V10.2.2 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Permissões invasivas reduzidas ao mínimo justificável |
| ASVS v4 | ASVS4-REQ-V10.2.3 | ✅ Semântico | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Funcionalidade oculta e debug inseguro excluídos do baseline |
| ASVS v4 | ASVS4-REQ-V12.4.1 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Ficheiros não confiáveis isolados fora da raiz pública |
| ASVS v4 | ASVS4-REQ-V13.4.2 | ✅ Semântico | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Autorização aplicada na lógica de negócio e não na camada GraphQL |
| ASVS v5 | ASVS-REQ-V6.1.1 — V6.1.1 | ✅ Semântico | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Defesa adaptativa contra brute force documentada na arquitetura de autenticação |
| ASVS v5 | ASVS-REQ-V6.1.2 — V6.1.2 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Vocabulário proibido contextual ainda sem regra explícita no catálogo |
| ASVS v5 | ASVS-REQ-V6.1.3 — V6.1.3 | ✅ Semântico | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Múltiplos caminhos de autenticação revistos sob a mesma baseline |
| ASVS v5 | ASVS-REQ-V6.2.1 — V6.2.1 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Comprimento mínimo de password tratado como política e não como estrutura |
| ASVS v5 | ASVS-REQ-V6.2.2 — V6.2.2 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Mudança voluntária de password fica fora do detalhe arquitetural publicado |
| ASVS v5 | ASVS-REQ-V6.2.3 — V6.2.3 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Troca de password com prova do segredo atual não está embalada |
| ASVS v5 | ASVS-REQ-V6.2.4 — V6.2.4 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Bloqueio das passwords mais comuns requer regra operacional adicional |
| ASVS v5 | ASVS-REQ-V6.2.5 — V6.2.5 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Liberdade de composição da password não aparece como decisão de arquitetura |
| ASVS v5 | ASVS-REQ-V6.2.6 — V6.2.6 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Mascaramento do campo pertence mais à interface do que ao capítulo |
| ASVS v5 | ASVS-REQ-V6.2.7 — V6.2.7 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Compatibilidade com gestores de passwords não surge como decisão estrutural |
| ASVS v5 | ASVS-REQ-V6.2.8 — V6.2.8 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Verificação sem truncar ou normalizar não está explicitada no catálogo |
| ASVS v5 | ASVS-REQ-V6.2.9 — V6.2.9 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Suporte a passwords longas carece de requisito publicado próprio |
| ASVS v5 | ASVS-REQ-V6.2.10 — V6.2.10 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Sem rotação periódica obrigatória continua fora da superfície publicada |
| ASVS v5 | ASVS-REQ-V6.2.11 — V6.2.11 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Lista contextual de palavras proibidas pede regra operacional dedicada |
| ASVS v5 | ASVS-REQ-V6.2.12 — V6.2.12 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Verificação contra passwords comprometidas ainda não tem row própria |
| ASVS v5 | ASVS-REQ-V6.3.1 — V6.3.1 | ✅ Semântico | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Travões a credential stuffing e brute force entram na arquitetura de acesso |
| ASVS v5 | ASVS-REQ-V6.3.2 — V6.3.2 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Contas por defeito desativadas dependem mais do baseline operacional |
| ASVS v5 | ASVS-REQ-V6.3.3 — V6.3.3 | ✅ Semântico | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | MFA proporcional ao risco já é pressuposto da confiança de autenticação |
| ASVS v5 | ASVS-REQ-V6.3.4 — V6.3.4 | ✅ Semântico | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Canais de autenticação documentados e consistentes com a mesma confiança |
| ASVS v5 | ASVS-REQ-V6.3.5 — V6.3.5 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Alerta de tentativas suspeitas cruza autenticação e logging, não só arquitetura |
| ASVS v5 | ASVS-REQ-V6.3.6 — V6.3.6 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Email como fator de autenticação não está tratado de forma explícita |
| ASVS v5 | ASVS-REQ-V6.3.7 — V6.3.7 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Notificação de mudanças credenciais depende de fluxo operacional complementar |
| ASVS v5 | ASVS-REQ-V6.3.8 — V6.3.8 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Proteção contra enumeração de utilizadores não está publicada por si só |
| ASVS v5 | ASVS-REQ-V6.4.1 — V6.4.1 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Segredos iniciais efémeros ainda não têm regra canónica própria |
| ASVS v5 | ASVS-REQ-V6.4.2 — V6.4.2 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Perguntas secretas ausentes do modelo, mas sem declaração formal dedicada |
| ASVS v5 | ASVS-REQ-V6.4.3 — V6.4.3 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Recuperação de password sem contornar MFA pede publicação específica |
| ASVS v5 | ASVS-REQ-V6.4.4 — V6.4.4 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Perda de fator exige prova de identidade acima do que o canon mostra |
| ASVS v5 | ASVS-REQ-V6.4.5 — V6.4.5 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Renovação atempada de autenticadores expirados continua implícita apenas |
| ASVS v5 | ASVS-REQ-V6.4.6 — V6.4.6 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Admin pode iniciar reset sem escolher segredo ainda não está descrito |
| ASVS v5 | ASVS-REQ-V6.5.1 — V6.5.1 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | OTP e códigos descartáveis pedem semântica de uso único mais explícita |
| ASVS v5 | ASVS-REQ-V6.5.2 — V6.5.2 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Hash de segredos fracos não surge como requisito estrutural publicado |
| ASVS v5 | ASVS-REQ-V6.5.3 — V6.5.3 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Geração CSPRNG de seeds e códigos ainda não está visível no canon |
| ASVS v5 | ASVS-REQ-V6.5.4 — V6.5.4 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Entropia mínima de códigos fora de banda requer regra mais específica |
| ASVS v5 | ASVS-REQ-V6.5.5 — V6.5.5 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Vida útil curta de TOTP e códigos não aparece isolada |
| ASVS v5 | ASVS-REQ-V6.5.6 — V6.5.6 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Revogação de fatores perdidos fica mais operacional do que arquitetural |
| ASVS v5 | ASVS-REQ-V6.5.7 — V6.5.7 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Biometria como fator secundário continua implícita e não nomeada |
| ASVS v5 | ASVS-REQ-V6.5.8 — V6.5.8 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Fonte temporal confiável para TOTP ainda não tem ligação explícita |
| ASVS v5 | ASVS-REQ-V6.6.1 — V6.6.1 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | OTP por PSTN só com salvaguardas não está publicado como decisão |
| ASVS v5 | ASVS-REQ-V6.6.2 — V6.6.2 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Vinculação do código fora de banda ao pedido original carece de row |
| ASVS v5 | ASVS-REQ-V6.6.3 — V6.6.3 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Rate limiting para códigos externos não está separado no canon |
| ASVS v5 | ASVS-REQ-V6.6.4 — V6.6.4 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Proteção contra push bombing ainda não foi embalada no capítulo |
| ASVS v5 | ASVS-REQ-V6.7.1 — V6.7.1 | ✅ Semântico | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Certificados de verificação protegidos como material crítico de confiança |
| ASVS v5 | ASVS-REQ-V6.7.2 — V6.7.2 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Nonce criptográfico robusto continua implícito e não publicado isoladamente |
| ASVS v5 | ASVS-REQ-V6.8.1 — V6.8.1 | ✅ Semântico | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Namespace por IdP evita colisões e spoofing entre provedores |
| ASVS v5 | ASVS-REQ-V6.8.2 — V6.8.2 | ✅ Semântico | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Assinaturas de assertions validadas antes de aceitar identidade federada |
| ASVS v5 | ASVS-REQ-V6.8.3 — V6.8.3 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Replay de assertions SAML ainda precisa de regra dedicada |
| ASVS v5 | ASVS-REQ-V6.8.4 — V6.8.4 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Força e recenticidade devolvidas pelo IdP não estão publicadas por critério |
| ASVS v5 | ASVS-REQ-V7.1.1 — V7.1.1 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Limites de sessão documentados e justificados ainda não têm row própria |
| ASVS v5 | ASVS-REQ-V7.1.2 — V7.1.2 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Número de sessões paralelas não aparece como decisão publicada |
| ASVS v5 | ASVS-REQ-V7.1.3 — V7.1.3 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Ecossistema SSO e coordenação de sessão exigem detalhe adicional |
| ASVS v5 | ASVS-REQ-V7.2.1 — V7.2.1 | ✅ Semântico | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Verificação de sessão concentrada em serviço backend confiável |
| ASVS v5 | ASVS-REQ-V7.2.2 — V7.2.2 | ✅ Semântico | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Sessões emitidas por tokens dinâmicos, nunca por segredos estáticos |
| ASVS v5 | ASVS-REQ-V7.2.3 — V7.2.3 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Entropia forte do token de referência ainda não está publicada isolada |
| ASVS v5 | ASVS-REQ-V7.2.4 — V7.2.4 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Rotação do token na autenticação pede regra de sessão mais precisa |
| ASVS v5 | ASVS-REQ-V7.3.1 — V7.3.1 | ✅ Semântico | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Inatividade e reautenticação seguem decisão de risco documentada |
| ASVS v5 | ASVS-REQ-V7.3.2 — V7.3.2 | ✅ Semântico | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Vida máxima da sessão alinhada com decisão formal de risco |
| ASVS v5 | ASVS-REQ-V7.4.1 — V7.4.1 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Logout e expiração sem reutilização da sessão não estão explicitados |
| ASVS v5 | ASVS-REQ-V7.4.2 — V7.4.2 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Desativação de conta com fecho global de sessões carece de row |
| ASVS v5 | ASVS-REQ-V7.4.3 — V7.4.3 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Encerrar outras sessões após mudar fatores ainda não está publicado |
| ASVS v5 | ASVS-REQ-V7.4.4 — V7.4.4 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Logout visível em páginas autenticadas pertence mais à superfície UX |
| ASVS v5 | ASVS-REQ-V7.4.5 — V7.4.5 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Administração de sessões ativas ainda não é controlo exposto no canon |
| ASVS v5 | ASVS-REQ-V7.5.1 — V7.5.1 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Reautenticação forte antes de mudar atributos sensíveis não está isolada |
| ASVS v5 | ASVS-REQ-V7.5.2 — V7.5.2 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Utilizador ver e terminar sessões atuais pede publicação operacional |
| ASVS v5 | ASVS-REQ-V7.5.3 — V7.5.3 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Step-up para operações críticas ainda não está explicitado |
| ASVS v5 | ASVS-REQ-V7.6.1 — V7.6.1 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Vida de sessão entre RP e IdP precisa de alinhamento mais visível |
| ASVS v5 | ASVS-REQ-V7.6.2 — V7.6.2 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Criação de sessão por ação explícita do utilizador não está nomeada |
| ASVS v5 | ASVS-REQ-V8.1.1 — V8.1.1 | ✅ Semântico | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Regras de acesso por função e dado assentam em permissões explícitas |
| ASVS v5 | ASVS-REQ-V8.1.2 — V8.1.2 | ✅ Semântico | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Leitura e escrita por campo dependem de autorização específica |
| ASVS v5 | ASVS-REQ-V8.1.3 — V8.1.3 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Atributos contextuais ainda não aparecem inventariados no canon |
| ASVS v5 | ASVS-REQ-V8.1.4 — V8.1.4 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Uso combinado de contexto e autorização precisa publicação dedicada |
| ASVS v5 | ASVS-REQ-V8.2.1 — V8.2.1 | ✅ Semântico | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Permissões explícitas barram acesso funcional indevido |
| ASVS v5 | ASVS-REQ-V8.2.2 — V8.2.2 | ✅ Semântico | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Permissões por objeto mitigam IDOR e BOLA |
| ASVS v5 | ASVS-REQ-V8.2.3 — V8.2.3 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Restrições por campo ainda não estão nomeadas ao nível de propriedade |
| ASVS v5 | ASVS-REQ-V8.2.4 — V8.2.4 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Controlo adaptativo contínuo durante a sessão ainda não está exposto |
| ASVS v5 | ASVS-REQ-V8.3.1 — V8.3.1 | ✅ Semântico | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Decisão de autorização fica na camada confiável de serviço |
| ASVS v5 | ASVS-REQ-V8.3.2 — V8.3.2 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Revogação imediata após mudança de atributos não está detalhada |
| ASVS v5 | ASVS-REQ-V8.3.3 — V8.3.3 | ✅ Semântico | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Autorização preserva a identidade de origem e não a do intermediário |
| ASVS v5 | ASVS-REQ-V8.4.1 — V8.4.1 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Isolamento entre tenants requer row própria de multi-tenancy |
| ASVS v5 | ASVS-REQ-V8.4.2 — V8.4.2 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Interfaces admin com verificação contínua pedem publicação específica |
| ASVS v5 | ASVS-REQ-V9.1.1 — V9.1.1 | ✅ Semântico | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Tokens autocontidos validados antes de confiar no conteúdo |
| ASVS v5 | ASVS-REQ-V9.1.2 — V9.1.2 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Allowlist de algoritmos ainda não surge como regra editorial isolada |
| ASVS v5 | ASVS-REQ-V9.1.3 — V9.1.3 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Chaves de validação a partir de fontes confiáveis pedem detalhe extra |
| ASVS v5 | ASVS-REQ-V9.2.1 — V9.2.1 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Janela temporal do token validada continua implícita apenas |
| ASVS v5 | ASVS-REQ-V9.2.2 — V9.2.2 | ✅ Semântico | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Cada token só serve o propósito de autenticação para que foi emitido |
| ASVS v5 | ASVS-REQ-V9.2.3 — V9.2.3 | ✅ Semântico | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Audiência do token limitada ao serviço destinatário |
| ASVS v5 | ASVS-REQ-V9.2.4 — V9.2.4 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Restrição inequívoca de audiência ainda não está publicada em detalhe |
| ASVS v5 | ASVS-REQ-V10.1.1 — V10.1.1 | ✅ Semântico | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Tokens ficam apenas nos componentes que realmente os consomem |
| ASVS v5 | ASVS-REQ-V10.1.2 — V10.1.2 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Fluxo OAuth ligado à mesma sessão do agente utilizador ainda não é explícito |
| ASVS v5 | ASVS-REQ-V10.2.1 — V10.2.1 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | CSRF no code flow pede controlo publicado para PKCE ou state |
| ASVS v5 | ASVS-REQ-V10.2.2 — V10.2.2 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Defesa contra mix-up entre authorization servers não está isolada |
| ASVS v5 | ASVS-REQ-V10.2.3 — V10.2.3 | ✅ Semântico | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Scopes pedidos limitados ao mínimo necessário pelo cliente |
| ASVS v5 | ASVS-REQ-V10.3.1 — V10.3.1 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Audience do access token no resource server ainda carece de row |
| ASVS v5 | ASVS-REQ-V10.3.2 — V10.3.2 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Claims delegadas participam na decisão mas não estão publicadas por nome |
| ASVS v5 | ASVS-REQ-V10.3.3 — V10.3.3 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Identidade única por issuer e subject não está descrita explicitamente |
| ASVS v5 | ASVS-REQ-V10.3.4 — V10.3.4 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Exigir força de autenticação do token requer detalhe adicional |
| ASVS v5 | ASVS-REQ-V10.3.5 — V10.3.5 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Sender-constrained access tokens ainda não aparecem como padrão publicado |
| ASVS v5 | ASVS-REQ-V10.4.1 — V10.4.1 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Redirect URIs em allowlist exata não estão declaradas no capítulo |
| ASVS v5 | ASVS-REQ-V10.4.2 — V10.4.2 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Código de autorização de uso único requer regra operacional própria |
| ASVS v5 | ASVS-REQ-V10.4.3 — V10.4.3 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Vida curta do authorization code não está embalada no surface atual |
| ASVS v5 | ASVS-REQ-V10.4.4 — V10.4.4 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Grants permitidos por cliente ainda não têm row editorial dedicada |
| ASVS v5 | ASVS-REQ-V10.4.5 — V10.4.5 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Replay de refresh token precisa de tratamento mais específico |
| ASVS v5 | ASVS-REQ-V10.4.6 — V10.4.6 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | PKCE obrigatório ainda não está nomeado na arquitetura reutilizável |
| ASVS v5 | ASVS-REQ-V10.4.7 — V10.4.7 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Dynamic client registration maliciosa continua fora da superfície publicada |
| ASVS v5 | ASVS-REQ-V10.4.8 — V10.4.8 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Expiração absoluta de refresh token pede regra independente |
| ASVS v5 | ASVS-REQ-V10.4.9 — V10.4.9 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Revogação de refresh tokens via UI ainda não está documentada |
| ASVS v5 | ASVS-REQ-V10.4.10 — V10.4.10 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Autenticação forte do cliente em backchannel não é row publicada |
| ASVS v5 | ASVS-REQ-V10.4.11 — V10.4.11 | ✅ Semântico | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Scoping por cliente segue princípio do menor privilégio |
| ASVS v5 | ASVS-REQ-V10.4.12 — V10.4.12 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Response modes autorizados por cliente ainda não são decisão exposta |
| ASVS v5 | ASVS-REQ-V10.4.13 — V10.4.13 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Code flow com PAR continua sem publicação específica no capítulo |
| ASVS v5 | ASVS-REQ-V10.4.14 — V10.4.14 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Access tokens proof-of-possession ainda não estão nomeados explicitamente |
| ASVS v5 | ASVS-REQ-V10.4.15 — V10.4.15 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Integridade do authorization_details vindo do backend pede detalhe extra |
| ASVS v5 | ASVS-REQ-V10.4.16 — V10.4.16 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Métodos fortes de client authentication não surgem isolados no canon |
| ASVS v5 | ASVS-REQ-V10.5.1 — V10.5.1 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Mitigação de replay de ID Token com nonce ainda não está detalhada |
| ASVS v5 | ASVS-REQ-V10.5.2 — V10.5.2 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Identidade única a partir de claims do ID Token pede row dedicada |
| ASVS v5 | ASVS-REQ-V10.5.3 — V10.5.3 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Metadados de authorization server maliciosos não estão cobertos explicitamente |
| ASVS v5 | ASVS-REQ-V10.5.4 — V10.5.4 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Audience do ID Token igual ao client_id não aparece por si só |
| ASVS v5 | ASVS-REQ-V10.5.5 — V10.5.5 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Logout back-channel resistente a abuso continua fora da superfície atual |
| ASVS v5 | ASVS-REQ-V10.6.1 — V10.6.1 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Response modes do OpenID Provider ainda não estão publicados em detalhe |
| ASVS v5 | ASVS-REQ-V10.6.2 — V10.6.2 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Logout forçado no OpenID Provider não tem controlo canónico próprio |
| ASVS v5 | ASVS-REQ-V10.7.1 — V10.7.1 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Consentimento por pedido de autorização ainda não está exposto no capítulo |
| ASVS v5 | ASVS-REQ-V10.7.2 — V10.7.2 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Clareza do ecrã de consentimento precisa de superfície editorial própria |
| ASVS v5 | ASVS-REQ-V10.7.3 — V10.7.3 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Revisão e revogação de consentimentos carecem de publicação específica |
| ASVS v5 | ASVS-REQ-V13.2.2 — V13.2.2 | ✅ Semântico | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Contas técnicas entre componentes operam com privilégio mínimo |
| CIS-4 | Secure Configuration of Enterprise Assets | ⚠️ Parcial | addon (medium): Plano de Validação Arquitetural | Semantics presentes; CIS inclui hardening empresarial além do âmbito |
| CIS-5 | Account Management | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Contas e privilégios entram no desenho, mas o controlo CIS é mais operacional |
| CIS-5.1 | Establish and Maintain an Inventory of Accounts | ⚠️ Parcial | aplicacao_lifecycle (strong): 🏛️ Aplicação de Arquitetura Segura no Ciclo de Vida > 📝 User Stories reutilizáveis > US-05 - Revisão de fronteiras de confiança e integrações | Identidades relevantes são mapeadas, sem inventário corporativo completo de contas |
| CIS-5.5 | Establish and Maintain an Inventory of Service Accounts | ⚠️ Parcial | addon (medium): 🧹 Modelos de Arquitetura Segura Reutilizáveis > ☁️ Modelo 2 - Microserviços com APIs Externas (Risco L2) > 🖼️ Diagrama sugerido | Contas técnicas por ambiente são previstas, sem registo formal de inventário |
| CIS-6.6 | Establish and Maintain an Inventory of Authentication and Authorization Systems | ⚠️ Parcial | aplicacao_lifecycle (strong): 🏛️ Aplicação de Arquitetura Segura no Ciclo de Vida > 📝 User Stories reutilizáveis > US-05 - Revisão de fronteiras de confiança e integrações | Revisão de integrações cobre autenticação e autorização, sem catálogo próprio publicado |
| CIS-12.5 | Centralize Network Authentication, Authorization, and Auditing (AAA) | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | AAA centralizado é assumido nas fronteiras, sem row arquitetural dedicada |
| CIS v8.1.2 | CIS-13.5 — Manage Access Control for Remote Assets | 🔧 Reparação | aplicacao_lifecycle (strong): 🏛️ Aplicação de Arquitetura Segura no Ciclo de Vida > 📝 User Stories reutilizáveis > US-02 - Ficha de solução com controlos e rastreabilidade arquitetural | Source: Manage Access Control for Remote Assets; Manual: 🏛️ Aplicação de Arquitetura Segura no Ciclo de Vida > 📝 User Stories reutilizáveis > US-02 - Ficha de solução com controlos e rastreabilidade arquitetural |
| HIPAA | HIPAA-164-308a4 — Information Access Management | ⚠️ Parcial | addon (medium): 🧹 Modelos de Arquitetura Segura Reutilizáveis > 🧱 Modelo 1 - Monólito Web com Backend Interno (Risco L1) > 🔑 Ameaças mitigadas | Controlo de acesso entra no modelo, sem política HIPAA isolada |
| HIPAA | HIPAA-164-312a1 — Access Control | ✅ Semântico | aplicacao_lifecycle (strong): 🏛️ Aplicação de Arquitetura Segura no Ciclo de Vida > 📝 User Stories reutilizáveis > US-02 - Ficha de solução com controlos e rastreabilidade arquitetural | Controlos de acesso ficam explícitos na ficha de solução arquitetural |
| HIPAA | HIPAA-164-312d — Person or Entity Authentication | ✅ Semântico | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Autenticação de utilizadores e serviços é tratada como fronteira de confiança |
| MCP Official | MCP-AUTH-SCOPE-NEGOTIATION | ✅ Semântico | addon (medium): 🧹 Modelos de Arquitetura Segura Reutilizáveis > ☁️ Modelo 2 - Microserviços com APIs Externas (Risco L2) > 🔑 Ameaças mitigadas | Scopes negociados com step-up seguem privilégio mínimo por serviço |
| MCP Official | MCP-SCOPE-MINIMIZATION | ⚠️ Parcial | maturity (weak): 📈 Maturidade - Arquitetura Segura > ✅ Conclusão | Minimização progressiva de scopes é coerente, mas não aparece como padrão isolado |
| OWASP MCP 3P | OWASP-MCP-3P-AUTH-AUTHZ-REGISTRATION | ✅ Semântico | addon (medium): 🧹 Modelos de Arquitetura Segura Reutilizáveis > ☁️ Modelo 2 - Microserviços com APIs Externas (Risco L2) > 🔑 Ameaças mitigadas | Registo protegido e autorização por ação seguem o modelo de confiança entre serviços |
| SLSA-BUILD-L3 | Hardened builds | ⚠️ Parcial | aplicacao_lifecycle (strong): US-07 — Validação arquitetural automatizável no CI/CD | Isolation semantics de arquitetura |
| SSDF | SSDF-PRACTICE-PS.1 | ⚠️ Parcial | addon (medium): 🧹 Modelos de Arquitetura Segura Reutilizáveis > 🧱 Modelo 1 - Monólito Web com Backend Interno (Risco L1) > 🔑 Ameaças mitigadas | Integridade do código é favorecida pelo desenho restritivo, sem controlo dedicado publicado |
| PCI DSS | PCI-REQ-7 | ✅ Semântico | aplicacao_lifecycle (strong): 🏛️ Aplicação de Arquitetura Segura no Ciclo de Vida > 📝 User Stories reutilizáveis > US-03 - Revisão formal do design arquitetural | Necessidade de saber já orienta a revisão formal do desenho de acesso |
| PCI DSS | PCI-REQ-8 | ✅ Semântico | aplicacao_lifecycle (strong): 🏛️ Aplicação de Arquitetura Segura no Ciclo de Vida > 📝 User Stories reutilizáveis > US-01 - Definição de princípios e baseline de arquitetura segura | Identidade e autenticação entram na baseline arquitetural desde a origem |
| PCI DSS | PCI-7.1.2 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Papéis existem na baseline, sem decomposição PCI por atividade |
| PCI DSS | PCI-7.2.1 | ✅ Semântico | aplicacao_lifecycle (strong): 🏛️ Aplicação de Arquitetura Segura no Ciclo de Vida > 📝 User Stories reutilizáveis > US-09 - Sincronização Threat Modeling ↔ Arquitetura | Modelo de controlo de acesso nasce ligado à arquitetura e às ameaças |
| PCI DSS | PCI-7.2.2 | ⚠️ Parcial | aplicacao_lifecycle (strong): 🏛️ Aplicação de Arquitetura Segura no Ciclo de Vida > 📝 User Stories reutilizáveis > US-01 - Definição de princípios e baseline de arquitetura segura | Atribuição de acessos por função existe, sem workflow PCI completo |
| PCI DSS | PCI-7.2.3 | ⚠️ Parcial | intro (strong): Arquitetura Segura > 📜 Políticas Organizacionais Relevantes | Aprovação de privilégios aparece como governação e não como passo isolado |
| PCI DSS | PCI-7.2.4 | ⚠️ Parcial | aplicacao_lifecycle (strong): 🏛️ Aplicação de Arquitetura Segura no Ciclo de Vida > 📝 User Stories reutilizáveis | Revisão de contas e acessos fica implícita no lifecycle, sem cadência própria |
| PCI DSS | PCI-7.2.5 | ⚠️ Parcial | intro (strong): Arquitetura Segura > 📜 Políticas Organizacionais Relevantes | Contas técnicas são consideradas, sem recertificação formal publicada |
| PCI DSS | PCI-7.2.6 | ⚠️ Parcial | aplicacao_lifecycle (strong): 🏛️ Aplicação de Arquitetura Segura no Ciclo de Vida > 📝 User Stories reutilizáveis | Consulta a repositórios sensíveis depende de autorização, sem row específica |
| PCI DSS | PCI-7.3.1 | ✅ Semântico | aplicacao_lifecycle (strong): 🏛️ Aplicação de Arquitetura Segura no Ciclo de Vida > 📝 User Stories reutilizáveis > US-02 - Ficha de solução com controlos e rastreabilidade arquitetural | Sistema de acesso fica explicitado na ficha arquitetural da solução |
| PCI DSS | PCI-7.3.2 | ✅ Semântico | aplicacao_lifecycle (strong): 🏛️ Aplicação de Arquitetura Segura no Ciclo de Vida > 📝 User Stories reutilizáveis > US-02 - Ficha de solução com controlos e rastreabilidade arquitetural | Permissões aprovadas são tratadas como decisão configurada por desenho |
| PCI DSS | PCI-7.3.3 | ✅ Semântico | aplicacao_lifecycle (strong): 🏛️ Aplicação de Arquitetura Segura no Ciclo de Vida > 📝 User Stories reutilizáveis > US-02 - Ficha de solução com controlos e rastreabilidade arquitetural | Default deny já aparece como princípio de exposição mínima |
| PCI DSS | PCI-8.1.2 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Responsabilidades existem no capítulo, sem matriz PCI por controlo |
| PCI DSS | PCI-8.2.1 | ✅ Semântico | aplicacao_lifecycle (strong): 🏛️ Aplicação de Arquitetura Segura no Ciclo de Vida > 📝 User Stories reutilizáveis > US-01 - Definição de princípios e baseline de arquitetura segura | Identificador único sustenta responsabilização de utilizadores e serviços |
| PCI DSS | PCI-8.2.2 | ⚠️ Parcial | aplicacao_lifecycle (strong): 🏛️ Aplicação de Arquitetura Segura no Ciclo de Vida > 📝 User Stories reutilizáveis | Identidades partilhadas são desencorajadas, sem regra operacional dedicada |
| PCI DSS | PCI-8.2.3 | ⚠️ Parcial | maturity (weak): 📈 Maturidade - Arquitetura Segura > 🧱 OWASP DSOMM - Architecture, Requirements, Risk | Contas de serviço pedem detalhe adicional além do capítulo de arquitetura |
| PCI DSS | PCI-8.2.4 | ⚠️ Parcial | aplicacao_lifecycle (strong): 🏛️ Aplicação de Arquitetura Segura no Ciclo de Vida > 📝 User Stories reutilizáveis | Ciclo de vida de contas é referido, sem trilho completo de autorização |
| PCI DSS | PCI-8.2.5 | ⚠️ Parcial | aplicacao_lifecycle (strong): 🏛️ Aplicação de Arquitetura Segura no Ciclo de Vida > 📝 User Stories reutilizáveis > US-01 - Definição de princípios e baseline de arquitetura segura | Revogação após saída exige processo operacional mais explícito |
| PCI DSS | PCI-8.2.6 | ⚠️ Parcial | aplicacao_lifecycle (strong): 🏛️ Aplicação de Arquitetura Segura no Ciclo de Vida > 📝 User Stories reutilizáveis | Higiene de contas inativas não surge como controlo canónico próprio |
| PCI DSS | PCI-8.2.7 | ⚠️ Parcial | legacy_canon (historical): Rastreabilidade — Capítulo 04: Arquitetura Segura > Camada AppSec Core | Acesso de terceiros entra nas trust boundaries, sem gestão contratual detalhada |
| PCI DSS | PCI-8.2.8 | ⚠️ Parcial | aplicacao_lifecycle (strong): 🏛️ Aplicação de Arquitetura Segura no Ciclo de Vida > 📝 User Stories reutilizáveis | Timeout de sessão é assumido no desenho, sem parâmetro PCI publicado |
| PCI DSS | PCI-8.3.1 | ✅ Semântico | aplicacao_lifecycle (strong): 🏛️ Aplicação de Arquitetura Segura no Ciclo de Vida > 📝 User Stories reutilizáveis | Autenticação forte protege o acesso a componentes críticos e dados |
| PCI DSS | PCI-8.3.2 | ✅ Semântico | legacy_canon (historical): Rastreabilidade — Capítulo 04: Arquitetura Segura > Frameworks normativos — cobertura verificada | Fatores de autenticação seguem transporte e armazenamento criptográficos |
| PCI DSS | PCI-8.3.3 | ⚠️ Parcial | aplicacao_lifecycle (strong): 🏛️ Aplicação de Arquitetura Segura no Ciclo de Vida > 📝 User Stories reutilizáveis | Alteração de fatores com revalidação de identidade não está isolada |
| PCI DSS | PCI-8.3.4 | ✅ Semântico | addon (medium): 🛠️ Decisão e Evidência Arquitetural > 5. Invalidação e revisão de decisões | Travões a tentativas inválidas fazem parte da arquitetura de autenticação |
| PCI DSS | PCI-8.3.5 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Reset seguro de passwords não aparece como regra editorial própria |
| PCI DSS | PCI-8.3.6 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Complexidade de passwords fica fora do detalhe arquitetural publicado |
| PCI DSS | PCI-8.3.7 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Reutilização de passwords requer política específica fora do chapter scope |
| PCI DSS | PCI-8.3.8 | ⚠️ Parcial | intro (strong): Arquitetura Segura > 📜 Políticas Organizacionais Relevantes | Política de autenticação existe em anexo, sem decomposição PCI dedicada |
| PCI DSS | PCI-8.3.9 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Rotação condicionada de passwords não está explicitada neste surface |
| PCI DSS | PCI-8.3.10 | ⚠️ Parcial | maturity (weak): 📈 Maturidade - Arquitetura Segura > 🧱 OWASP DSOMM - Architecture, Requirements, Risk | Exigências acrescidas para service providers pertencem mais à maturidade |
| PCI DSS | PCI-8.3.11 | ⚠️ Parcial | intro (strong): Arquitetura Segura > 📜 Políticas Organizacionais Relevantes | Gestão de fatores existe por alto, sem row canónica dedicada |
| PCI DSS | PCI-8.4.1 | ✅ Semântico | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | MFA cobre acesso administrativo não-console como fronteira de confiança |
| PCI DSS | PCI-8.4.2 | ✅ Semântico | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | MFA reforça acessos sensíveis não-console no desenho de autenticação |
| PCI DSS | PCI-8.4.3 | ✅ Semântico | legacy_canon (historical): Rastreabilidade — Capítulo 04: Arquitetura Segura > Camada AppSec Core | Acesso remoto fica protegido com MFA e segregação de contexto |
| PCI DSS | PCI-8.5.1 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Arquitetura assume MFA robusto, sem checklist técnica PCI publicada |
| PCI DSS | PCI-8.6.1 | ✅ Semântico | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Contas de aplicação operam com owner definido e privilégio mínimo |
| PCI DSS | PCI-8.6.2 | ⚠️ Parcial | requirements_catalog (strong): Catálogo de Requisitos de Arquitectura Segura | Segredos de contas técnicas pedem gestão operacional além da arquitetura |
| PCI DSS | PCI-8.6.3 | ⚠️ Parcial | intro (strong): Arquitetura Segura > 📜 Políticas Organizacionais Relevantes | Política para contas de aplicação existe por alto, sem regra PCI isolada |

**Legenda:** ✅ Explícito · ✅ Semântico · ⚠️ Parcial · 🔧 Reparação · 🔴 Gap

> **Nota:** Este capítulo é o mais referenciado pelos pilots MCP e ASVS em cobertura parcial. Não há gap de conteúdo — a pressão é de embalagem e referenciação cruzada mais explícita.

---

## Maturidade — referência separada

A leitura de maturidade deste capítulo é tratada em [achievable-maturity.md](../achievable-maturity.md).

Neste documento, os modelos de maturidade surgem apenas como contexto editorial complementar. A sua normalização formal é apresentada no documento dedicado do capítulo.

---

## Ligações com outros capítulos

- **Cap. 01** — zonas de confiança e validações proporcionais ao risco
- **Cap. 02** — requisitos de arquitetura derivados dos REQ-XXX
- **Cap. 03** — arquitetura segura como output primário de threat modeling
- **Cap. 09** — arquitetura lógica sustenta modelo de segmentação de containers
- **Cap. 10** — arquitetura é input principal de testes estruturais
