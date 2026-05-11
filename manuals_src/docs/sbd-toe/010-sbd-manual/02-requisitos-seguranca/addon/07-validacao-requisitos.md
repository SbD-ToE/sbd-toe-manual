---
id: validacao-requisitos
title: Validação de Requisitos de Segurança
description: Modelo completo de validação dos requisitos do catálogo SbD-ToE - princípios, métodos por tipo de requisito, momentos do ciclo de vida e plano detalhado por domínio com tag operacional, método recomendado e evidência esperada.
tags: [validação, requisitos, segurança-aplicacional, evidência, SAST, DAST, auditoria, rastreabilidade, ciclo-de-vida, CI-CD]
sidebar_position: 7
---

# ✅ Validação de Requisitos de Segurança

A validação é o mecanismo que converte requisitos definidos em garantia observável. Não basta que um requisito exista no catálogo - é necessário confirmar que foi implementado, que funciona conforme esperado e que existe evidência auditável disso. Este documento prescreve como fazê-lo de forma sistemática, proporcional ao risco e integrada no ciclo de desenvolvimento.

---

## 1) Princípios orientadores

A validação de requisitos de segurança deve ser:

- **Sistemática** - associada a momentos bem definidos do ciclo de vida, não ad-hoc;
- **Proporcional ao risco** - requisitos de maior criticidade exigem validação mais profunda e independente;
- **Rastreável** - cada validação produz ligação explícita entre requisito, método, resultado e evidência;
- **Repetível** - automatizável ou documentada com suficiente detalhe para replicação;
- **Independente** - sempre que possível, realizada por alguém fora da linha de implementação directa.

---

## 2) Métodos de validação

A escolha do método depende do tipo de requisito e da fase em que é aplicado. Os métodos não são mutuamente exclusivos - para requisitos críticos, a combinação de dois ou mais é a abordagem correcta.

### Análise Estática (SAST)

Aplica-se a requisitos que se traduzem em padrões de código, configurações ou estruturas previsíveis. Deve ser executada durante o desenvolvimento e no pipeline de build, e deve verificar:

- Presença de validações de entrada;
- Uso de bibliotecas e algoritmos criptográficos aprovados;
- Ausência de segredos hardcoded;
- Controlo de fluxo de autenticação e autorização.

Os resultados devem ser correlacionados com os identificadores de requisitos do projecto (`SEC-Lx-*`).

### Análise Dinâmica (DAST)

Aplica-se a requisitos que se manifestam no comportamento em execução. Deve ser usada em ambiente de teste ou pré-produção. Permite validar:

- Exposição de endpoints e cabeçalhos de segurança;
- Comportamento perante entradas maliciosas;
- Ausência de erros ou divulgações indevidas;
- Resposta a falhas de autenticação ou autorização mal configurada.

### Testes funcionais de segurança

Complementam a análise dinâmica com verificação explícita dos critérios de aceitação de cada requisito. Devem incluir:

- Verificação do comportamento esperado (caso positivo);
- Tentativa de contornar o controlo (caso negativo);
- Cobertura de casos-limite, restrições e falhas previstas.

### Revisão técnica estruturada

Realizada por analistas, arquitectos ou elementos de segurança. Adequada para requisitos cujo controlo é distribuído ou implícito - segregação lógica, dependências externas, controlo de sessão transversal. Deve ocorrer após marcos relevantes: release candidate, pull request crítico, auditoria interna.

### Validação contínua em CI/CD

Requisitos críticos devem estar ligados a mecanismos de bloqueio no pipeline:

- Avaliações automáticas de código e configuração;
- Rejeição de builds que violem critérios mínimos (ausência de MFA, logging, segredos expostos);
- Revalidação com cada alteração de risco (nova funcionalidade, nova integração).

---

## 3) Quando validar

| Fase SDLC | Objectivo da validação | Método primário |
|-----------|------------------------|-----------------|
| Planeamento e definição | Confirmação da aplicabilidade dos requisitos | Análise técnica + validação manual |
| Desenvolvimento | Detecção precoce de incumprimento | SAST + revisão de código |
| Testes | Verificação do comportamento previsto | Testes funcionais + DAST |
| Pré-release / entrega | Validação de conformidade total | Validação cruzada + CI/CD gates |
| Produção / operação | Monitorização contínua de requisitos activos | Revalidação, logging, alertas |

---

## 4) Plano de validação por domínio

Para cada requisito do catálogo canónico são indicados: a tag operacional de referência, o nível mínimo de aplicação, o método de validação recomendado e a evidência esperada.

> **Nota:** A tag operacional usa `SEC-Lx-*` com `Lx` substituído pelo nível efectivo do projecto. Exemplo: `SEC-Lx-AUT-MFA` → `SEC-L2-AUT-MFA` num projecto L2.

---

### AUT - Autenticação e Identidade

| ID | Tag operacional | Nível | Método de validação | Evidência esperada |
|----|-----------------|:-----:|---------------------|-------------------|
| AUT-001 | SEC-Lx-AUT-MFA | L2+ | Tentar login sem segundo factor. Confirmar rejeição e logs de falha. | Log de autenticação falhada sem MFA. Captura do bloqueio. |
| AUT-002 | SEC-Lx-AUT-PWD | L1+ | Rever política activa. Tentar definir password inválida. Confirmar rejeição. | Política documentada. Log de erro ou rejeição. |
| AUT-003 | SEC-Lx-AUT-BRUTE | L1+ | Simular tentativas repetidas falhadas. Confirmar bloqueio, CAPTCHA ou atraso progressivo. | Log com contagem de falhas. Evidência de bloqueio ou atraso. |
| AUT-004 | SEC-Lx-AUT-LOGOUT | L1+ | Efectuar logout. Tentar reutilizar sessão ou token. Confirmar rejeição. | Log de sessão revogada. Erro de autenticação na reutilização. |
| AUT-005 | SEC-Lx-AUT-IDLE | L1+ | Simular inactividade pelo período configurado. Confirmar expiração e redirect. | Log de timeout. Captura de expiração automática. |
| AUT-006 | SEC-Lx-AUT-CRED | L1+ | Validar hashing com salt. Verificar ausência de credenciais em claro em armazenamento e transmissão. | Output de configuração. Resultado de scan. Ausência em repositório. |
| AUT-007 | SEC-Lx-AUT-FED | L2+ | Simular login federado via SAML/OIDC. Confirmar fluxo completo e logging. | Log de autenticação via IdP externo. Captura de login bem-sucedido. |
| AUT-008 | SEC-Lx-AUT-STEPUP | L2+ | Simular acção sensível. Confirmar exigência de factor adicional. | Captura de step-up. Log associado à acção crítica. |
| AUT-009 | SEC-Lx-AUT-CHANGE | L1+ | Tentar alterar credenciais sem reautenticação. Confirmar bloqueio. | Log da tentativa bloqueada. Evidência de verificação da sessão activa. |
| AUT-010 | SEC-Lx-AUT-ALERT | L2+ | Simular login anómalo. Confirmar notificação ao utilizador e registo. | Exemplo de notificação enviada. Log do evento crítico detectado. |

---

### ACC - Controlo de Acesso

| ID | Tag operacional | Nível | Método de validação | Evidência esperada |
|----|-----------------|:-----:|---------------------|-------------------|
| ACC-001 | SEC-Lx-ACC-RBAC | L1+ | Testar acesso com role de privilégio reduzido a recurso restrito. Confirmar rejeição. | Log de rejeição. Mapeamento de roles documentado. |
| ACC-002 | SEC-Lx-ACC-PRIV | L1+ | Auditar permissões de contas de utilizador e serviço. Confirmar ausência de privilégios desnecessários. | Relatório de auditoria de permissões. |
| ACC-003 | SEC-Lx-ACC-BLOCK | L1+ | Tentar acesso não autorizado. Confirmar bloqueio e registo com contexto suficiente. | Log de rejeição com dados de contexto. |
| ACC-004 | SEC-Lx-ACC-SEP | L1+ | Verificar separação efectiva de perfis. Confirmar que acções de cada perfil são rastreáveis. | Logs com perfil identificado. Teste cruzado de perfis. |
| ACC-005 | SEC-Lx-ACC-API | L1+ | Testar endpoints sem autenticação/autorização. Confirmar rejeição com código adequado. | Log de rejeição. Testes automatizados de endpoints. |
| ACC-006 | SEC-Lx-ACC-DATA | L1+ | Tentar acesso a dados críticos com role não autorizado. Confirmar bloqueio e log. | Evidência de controlo efectivo. Log do evento. |
| ACC-007 | SEC-Lx-ACC-MODEL | L2+ | Verificar existência de modelo de permissões revisto e documentado. | Documentação do modelo. Registo de revisão datada. |
| ACC-008 | SEC-Lx-ACC-REVOKE | L1+ | Revogar acesso. Testar imediatamente após revogação. Confirmar falha. | Log de tentativa falhada após revogação. Timestamp de revogação. |
| ACC-009 | SEC-Lx-ACC-ABAC | L3 | Testar decisão de acesso com atributos distintos. Confirmar aplicação de política dinâmica. | Logs com avaliação de atributos. Teste com variação de contexto. |
| ACC-010 | SEC-Lx-ACC-REVIEW | L2+ | Verificar existência de processo de revisão periódica. Confirmar remoção de permissões obsoletas. | Registos de revisão datados. Evidência de limpeza de permissões. |

---

### LOG - Registo e Monitorização

| ID | Tag operacional | Nível | Método de validação | Evidência esperada |
|----|-----------------|:-----:|---------------------|-------------------|
| LOG-001 | SEC-Lx-LOG-EVENTS | L1+ | Rever configuração de logging. Confirmar cobertura de acessos, alterações e falhas críticas. | Logs auditáveis com eventos mapeados por tipo e contexto. |
| LOG-002 | SEC-Lx-LOG-ATTRS | L1+ | Analisar estrutura de logs. Confirmar presença de quem, quando, o quê e onde em cada entrada. | Amostras de log com todos os atributos obrigatórios. |
| LOG-003 | SEC-Lx-LOG-INTEG | L1+ | Tentar alterar log em disco. Verificar mecanismos de protecção (hash, write-once, syslog remoto). | Evidência de WORM, syslog remoto ou mecanismo de detecção de tamper. |
| LOG-004 | SEC-Lx-LOG-REVIEW | L2+ | Confirmar existência de processo de análise periódica documentado e executado. | Registo de análise datado. Procedimento documentado. |
| LOG-005 | SEC-Lx-LOG-RETAIN | L1+ | Verificar período de retenção efectivo contra política definida. | Configuração de retenção. Evidência de logs no período exigido. |
| LOG-006 | SEC-Lx-LOG-CENTRAL | L2+ | Confirmar envio para agregador central. Verificar configuração de forwarding. | Visualização centralizada com logs por aplicação. |
| LOG-007 | SEC-Lx-LOG-ALERT | L2+ | Gerar evento anómalo. Confirmar disparo de alerta com threshold e canal configurados. | Log do alerta disparado com timestamp e detalhe. |
| LOG-008 | SEC-Lx-LOG-FAIL | L2+ | Desactivar ou bloquear o sistema de logging. Confirmar que falha é detectada e alertada. | Alerta de falha de logging. Log da detecção. |
| LOG-009 | SEC-Lx-LOG-IR | L2+ | Simular incidente ou revisão forense. Confirmar que logs têm detalhe suficiente para reconstrução. | Capacidade demonstrada de reconstrução de timeline de evento. |
| LOG-010 | SEC-Lx-LOG-BIZ | L3 | Verificar registo de eventos críticos de negócio (transacções, autorizações de alto impacto). | Logs com eventos de negócio identificados e rastreáveis. |

---

### SES - Sessões e Estado

| ID | Tag operacional | Nível | Método de validação | Evidência esperada |
|----|-----------------|:-----:|---------------------|-------------------|
| SES-001 | SEC-Lx-SES-IDLE | L1+ | Simular inactividade pelo período configurado. Confirmar expiração e redirect. | Log de timeout. Captura de sessão terminada. |
| SES-002 | SEC-Lx-SES-LOGOUT | L1+ | Efectuar logout. Tentar reutilizar token. Alterar password e tentar usar token anterior. | Erro de autenticação na reutilização. Log de invalidação. |
| SES-003 | SEC-Lx-SES-ENTROPY | L1+ | Analisar tokens gerados. Confirmar entropia adequada e ausência de padrão previsível. | Análise de tokens. Ausência de previsibilidade demonstrada. |
| SES-004 | SEC-Lx-SES-TLS | L1+ | Interceptar tráfego com proxy. Confirmar que tokens apenas transitam por TLS. Verificar flags de cookies. | Headers de resposta. Flags Secure e HttpOnly confirmados. |
| SES-005 | SEC-Lx-SES-BIND | L2+ | Alterar IP ou user-agent durante sessão activa. Confirmar terminação ou exigência de revalidação. | Log de terminação de sessão por mudança de contexto. |
| SES-006 | SEC-Lx-SES-REVOKE | L1+ | Revogar sessão via interface de gestão. Testar imediatamente após revogação. | Erro de autenticação imediato. Log de revogação explícita. |
| SES-007 | SEC-Lx-SES-TTL | L2+ | Verificar TTL máximo configurado. Tentar manter sessão para além do limite. | Configuração de TTL. Evidência de expiração forçada. |
| SES-008 | SEC-Lx-SES-JWT | L2+ | Inspecionar JWTs. Confirmar claims de âmbito e expiração. Testar token após revogação. | JWT decoded com claims correctos. Falha após revogação. |

---

### VAL - Validação de Dados

| ID | Tag operacional | Nível | Método de validação | Evidência esperada |
|----|-----------------|:-----:|---------------------|-------------------|
| VAL-001 | SEC-Lx-VAL-INPUT | L1+ | Rever código de validação. Enviar inputs inválidos (tipo, tamanho, formato). Confirmar rejeição. | Testes de input inválido. Código com validações. Logs de rejeição. |
| VAL-002 | SEC-Lx-VAL-WLIST | L1+ | Tentar enviar valores fora da lista permitida. Confirmar rejeição e ausência de tratamento implícito. | Código com whitelist explícita. Testes com valores não previstos. |
| VAL-003 | SEC-Lx-VAL-SCHEMA | L2+ | Enviar payloads malformados ou com campos em falta. Confirmar rejeição automática. | Rejeições consistentes. Testes de contrato. |
| VAL-004 | SEC-Lx-VAL-SQLI | L1+ | Rever uso de prepared statements. Executar SAST e testes de injecção SQL. | Relatórios de scanner. Ausência de concatenação em queries. |
| VAL-005 | SEC-Lx-VAL-PREUSE | L1+ | Rastrear caminhos entre input layer e lógica de negócio/persistência. Confirmar que validação precede uso interno; identificar caminhos não validados. | Análise de fluxo de dados com pontos de validação evidenciados. Code review confirma ausência de caminhos não validados. |
| VAL-006 | SEC-Lx-VAL-SAFE | L1+ | Forçar erro de validação. Confirmar que mensagem ao cliente não expõe lógica interna. | Mensagens de erro genéricas. Ausência de detalhe técnico no cliente. |
| VAL-007 | SEC-Lx-VAL-AUTO | L2+ | Executar testes automatizados com payloads maliciosos (XSS, SQLi, path traversal). | Relatórios de execução. Cobertura de casos documentada. |
| VAL-008 | SEC-Lx-VAL-XSS | L1+ | Testar output em superfícies renderizadas (HTML, atributo, JS, SQL via prepared statements, shell, logs). Confirmar encoding contextual correcto. | Testes com payloads XSS/SQLi/log injection. Encoding observável conforme contexto de renderização. |

> Nota editorial: VAL-005 cobre validação **pré-uso** de dados (caminho input → lógica/persistência; anchor ACO-IVF-004); VAL-008 cobre **codificação de output** em renderização (anchor ACO-IVF-008). Os controlos são complementares — entrada e saída.

---

### ERR - Gestão de Erros

| ID | Tag operacional | Nível | Método de validação | Evidência esperada |
|----|-----------------|:-----:|---------------------|-------------------|
| ERR-001 | SEC-Lx-ERR-LEAK | L1+ | Provocar erros intencionais. Confirmar que cliente recebe mensagem abstrata sem dados internos. | Resposta genérica ao cliente. Log interno detalhado separado. |
| ERR-002 | SEC-Lx-ERR-MSG | L1+ | Verificar todas as superfícies de erro. Confirmar ausência de stack trace ou informação técnica. | Captura de mensagens de erro em diferentes cenários. |
| ERR-003 | SEC-Lx-ERR-ENUM | L1+ | Testar recursos existentes e inexistentes. Confirmar respostas de erro idênticas (sem enumeração). | Respostas iguais para recursos existentes e inexistentes. |
| ERR-004 | SEC-Lx-ERR-I18N | L1+ | Verificar mensagens em diferentes locales. Confirmar ausência de conteúdo executável. | Mensagens traduzidas sem referências técnicas ou executáveis. |
| ERR-005 | SEC-Lx-ERR-CENTRAL | L2+ | Rever arquitectura de tratamento de erros. Confirmar centralização. | Código com handler centralizado. Ausência de tratamento ad-hoc disperso. |
| ERR-006 | SEC-Lx-ERR-TEST | L2+ | Executar testes automáticos de cenários de erro. Confirmar que erros são tratados sem fuga. | Cobertura de testes de erro. Relatório de execução. |
| ERR-007 | SEC-Lx-ERR-LOG | L2+ | Rever logs de erro. Confirmar ausência de dados pessoais, tokens ou credenciais. | Logs sem dados sensíveis. IDs contextuais pseudonimizados. |

---

### CFG - Configuração Segura

| ID | Tag operacional | Nível | Método de validação | Evidência esperada |
|----|-----------------|:-----:|---------------------|-------------------|
| CFG-001 | SEC-Lx-CFG-DEBUG | L1+ | Tentar aceder a endpoints de debug, tracing ou interfaces admin. Confirmar desactivação ou protecção. | Resposta 403/404 ou exigência de autenticação. |
| CFG-002 | SEC-Lx-CFG-ENV | L1+ | Verificar separação de ambientes. Confirmar que deploys e testes só ocorrem em ambientes segregados. | Logs com ambiente identificado. Confirmação de segregação. |
| CFG-003 | SEC-Lx-CFG-HARD | L1+ | Executar scan de segredos no repositório e no código. Confirmar ausência de hardcoded secrets. | Relatório de scan limpo. Ausência de segredos no histórico. |
| CFG-004 | SEC-Lx-CFG-EXT | L1+ | Verificar que configuração é externa ao código. Confirmar permissões restritivas no repositório de configuração. | Configuração externa e versionada. Permissões auditadas. |
| CFG-005 | SEC-Lx-CFG-START | L2+ | Remover parâmetro obrigatório. Confirmar que arranque falha com erro explícito. | Log de falha de arranque com causa identificada. |
| CFG-006 | SEC-Lx-CFG-VAULT | L2+ | Rever gestão de segredos. Confirmar uso de cofre e ausência local. | Configuração do cofre. Políticas de acesso. Ausência de segredos locais. |
| CFG-007 | SEC-Lx-CFG-DRIFT | L3 | Alterar configuração crítica fora do processo normal. Confirmar detecção e alerta. | Alerta de drift. Log de alteração inesperada. |

---

### API - Segurança de APIs

| ID | Tag operacional | Nível | Método de validação | Evidência esperada |
|----|-----------------|:-----:|---------------------|-------------------|
| API-001 | SEC-Lx-API-AUTH | L1+ | Testar endpoints sem credenciais. Confirmar rejeição 401/403. | Logs de rejeição. Testes automatizados de endpoints. |
| API-002 | SEC-Lx-API-EXPOSE | L1+ | Inventariar endpoints expostos em produção. Confirmar ausência de debug ou legacy. | Inventário de endpoints activos. Ausência de endpoints não intencionais. |
| API-003 | SEC-Lx-API-INPUT | L1+ | Enviar payloads inválidos. Confirmar rejeição com código adequado. | Logs de rejeição. Testes com payloads malformados. |
| API-004 | SEC-Lx-API-RATE | L2+ | Executar burst de chamadas. Confirmar resposta 429 ou bloqueio temporário. | Evidência de rate limiting em runtime ou logs. |
| API-005 | SEC-Lx-API-TLS | L1+ | Verificar certificados e versão TLS. Confirmar cabeçalhos de segurança activos. | Scanner TLS. Headers de resposta. |
| API-006 | SEC-Lx-API-DEPS | L1+ | Verificar SBOM e dependências documentadas. Confirmar auditoria de vulnerabilidades conhecidas. | SBOM. Relatório de auditoria de dependências. |
| API-007 | SEC-Lx-API-LOG | L2+ | Verificar logs de chamadas externas. Confirmar presença de dados essenciais. | Logs com origem, destino, resultado e timestamp. |

---

### INT - Mensagens e Integrações

| ID | Tag operacional | Nível | Método de validação | Evidência esperada |
|----|-----------------|:-----:|---------------------|-------------------|
| INT-001 | SEC-Lx-INT-VAL | L1+ | Enviar mensagem malformada a integração. Confirmar rejeição ou tratamento controlado. | Evidência de rejeição. Sem processamento cego de mensagens inválidas. |
| INT-002 | SEC-Lx-INT-AUTH | L1+ | Testar integração sem token ou com token inválido. Confirmar rejeição. | Log de rejeição. Teste de token expirado. |
| INT-003 | SEC-Lx-INT-TLS | L1+ | Interceptar tráfego entre sistemas. Confirmar cifra TLS activa. Verificar versões suportadas. | Scanner de TLS. Logs de conexão cifrada. |
| INT-004 | SEC-Lx-INT-PROTO | L1+ | Tentar comunicação por protocolo inseguro. Confirmar rejeição ou redirect. | Erro ou redirect para protocolo seguro. Log de rejeição. |
| INT-005 | SEC-Lx-INT-SIGN | L2+ | Enviar mensagem com assinatura inválida ou em falta. Confirmar rejeição e log. | Evidência de verificação de integridade. Log de falha de validação. |
| INT-006 | SEC-Lx-INT-ORIGIN | L2+ | Enviar mensagem de origem não autorizada. Confirmar rejeição. | Log de rejeição com origem identificada. Lista de origens autorizadas. |
| INT-007 | SEC-Lx-INT-ANOMALY | L3 | Simular padrão de comunicação anómalo. Confirmar alerta. | Alerta disparado. Log com contexto do padrão detectado. |
| INT-008 | SEC-Lx-INT-REVIEW | L3 | Verificar documentação de integrações e cláusulas de segurança nos contratos. | Documentação de integração. Cláusulas contratuais de segurança. |

---

### REQ - Definição de Requisitos

| ID | Tag operacional | Nível | Método de validação | Evidência esperada |
|----|-----------------|:-----:|---------------------|-------------------|
| REQ-001 | SEC-Lx-REQ-INC | L1+ | Verificar existência de requisitos de segurança em backlog/documentação. | Requisitos marcados e rastreáveis no backlog. |
| REQ-002 | SEC-Lx-REQ-REV | L1+ | Verificar existência de processo de revisão executado e documentado. | Registo de revisão com responsável identificado. |
| REQ-003 | SEC-Lx-REQ-RISK | L1+ | Confirmar mapeamento entre requisitos e nível de criticidade. | Matriz de aplicabilidade actualizada. |
| REQ-004 | SEC-Lx-REQ-VER | L1+ | Verificar histórico de alterações ao catálogo do projecto. | Controlo de versões activo. Histórico disponível. |
| REQ-005 | SEC-Lx-REQ-TM | L2+ | Confirmar que alterações relevantes desencadeiam revisão de threat model. | Registo de decisão associado à alteração. |
| REQ-006 | SEC-Lx-REQ-TRACE | L2+ | Verificar rastreabilidade requisito → ameaça → teste. | Matriz ou ferramenta com ligações explícitas. |
| REQ-007 | SEC-Lx-REQ-ITER | L2+ | Confirmar existência de ciclos de revisão com equipas. | Registos de revisão iterativa datados. |

---

### DST - Distribuição de Artefactos

| ID | Tag operacional | Nível | Método de validação | Evidência esperada |
|----|-----------------|:-----:|---------------------|-------------------|
| DST-001 | SEC-Lx-DST-REPO | L1+ | Testar acesso a repositório sem autenticação. Confirmar rejeição e logs activos. | Rejeição de acesso anónimo. Logs de acesso. |
| DST-002 | SEC-Lx-DST-PUB | L2+ | Verificar processo de aprovação para publicação pública. Confirmar documentação. | Registo de aprovação. Documentação do processo. |
| DST-003 | SEC-Lx-DST-SIGN | L2+ | Verificar assinatura ou checksum dos artefactos. Confirmar verificação automatizada. | Artefactos assinados. Script ou pipeline de verificação. |
| DST-004 | SEC-Lx-DST-SBOM | L2+ | Confirmar geração e anexação de SBOM por release. | SBOM disponível e rastreável por versão. |
| DST-005 | SEC-Lx-DST-ACCESS | L2+ | Verificar que apenas utilizadores e automações autorizados acedem a artefactos de produção. | Políticas de acesso. Auditoria de permissões. |
| DST-006 | SEC-Lx-DST-PIPE | L2+ | Tentar deploy manual em produção. Confirmar bloqueio. | Evidência de pipeline como único caminho de deploy. |
| DST-007 | SEC-Lx-DST-REVOKE | L1+ | Verificar processo de remoção e notificação para artefactos comprometidos. | Registo de revogação. Evidência de notificação. |

---

### IDE - Ferramentas de Desenvolvimento

| ID | Tag operacional | Nível | Método de validação | Evidência esperada |
|----|-----------------|:-----:|---------------------|-------------------|
| IDE-001 | SEC-Lx-IDE-AUTH | L1+ | Verificar lista de ferramentas e IDEs autorizadas e se está actualizada. | Lista mantida. Evidência de aprovação das ferramentas em uso. |
| IDE-002 | SEC-Lx-IDE-UPD | L1+ | Verificar versões de IDEs e ferramentas em uso. Confirmar actualizações aplicadas. | Histórico de actualizações. Versões actuais documentadas. |
| IDE-003 | SEC-Lx-IDE-GEN | L2+ | Rever amostras de código gerado. Confirmar existência de processo de revisão antes de integração. | Evidência de revisão de código gerado. Pull request com revisão documentada. |
| IDE-004 | SEC-Lx-IDE-EXT | L1+ | Verificar lista de extensões instaladas. Confirmar que são de fontes reconhecidas. | Lista de extensões com origem documentada. |
| IDE-005 | SEC-Lx-IDE-PERM | L2+ | Verificar permissões concedidas a extensões. Confirmar que apenas as necessárias estão activas. | Permissões revistas. Execução sandboxed confirmada. |
| IDE-006 | SEC-Lx-IDE-LOCAL | L2+ | Verificar controlo sobre uso de ambientes locais. Confirmar existência de logs ou proxy quando aplicável. | Política de uso de ambientes locais. Logs de rede ou proxy. |

---

## 5) Resultados esperados da validação

Cada requisito validado deve produzir:

- **Evidência de execução** - relatório, log, artefacto de validação, captura de ecrã;
- **Resultado** - conforme / não conforme / parcial, com contexto suficiente para decisão;
- **Ligação ao identificador** - tag operacional do projecto (`SEC-L2-AUT-MFA`) e ID canónico (`AUT-001`);
- **Medida correctiva**, quando aplicável - acção, responsável, prazo.

---

## 6) Melhoria contínua

A validação deve ser incorporada num ciclo de melhoria contínua, com os métodos:

- **Revistos com base em incidentes ou findings reais** - um finding recorrente indica lacuna no método, não apenas no controlo;
- **Actualizados com novas técnicas** ou alterações ao catálogo;
- **Automatizados sempre que possível**, para garantir cobertura consistente e escalável;
- **Monitorizados com indicadores** - percentagem de requisitos validados por release, tempo médio de detecção de não conformidade.

---

## Referências cruzadas

| Documento | Relação |
|-----------|---------|
| [Catálogo Base de Requisitos](./lista-requisitos-base) | Define os requisitos e critérios de aceitação a validar |
| [Taxonomia e Rastreabilidade](./taxonomia-rastreabilidade) | Define IDs canónicos e tags operacionais usadas neste documento |
| [Matriz de Controlos por Risco](./matriz-controlos-por-risco) | Indica aplicabilidade por domínio e nível de risco |
| [Rastreabilidade e Controlos](./rastreabilidade-controlo) | Modelo de matriz risco → requisito → controlo → evidência |
| [Gestão de Excepções](./gestao-excecoes) | Processo para requisitos que não podem ser validados ou cumpridos |
