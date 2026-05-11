---
id: recomendacoes-avancadas
title: Recomendações Avançadas - Desenvolvimento Seguro
description: Práticas reforçadas e recomendações opcionais para organizações com maior maturidade em desenvolvimento seguro
tags: [desenvolvimento, maturidade, práticas avançadas, DevSecOps, validação]
sidebar_position: 30
---

# 🧠 Recomendações Avançadas - Desenvolvimento Seguro

Este ficheiro apresenta um conjunto de práticas avançadas que **complementam e reforçam** as medidas prescritas neste capítulo.  
São especialmente relevantes para organizações com pipelines maduros, cultura de DevSecOps, e equipas com elevada autonomia técnica.

As recomendações aqui descritas **não substituem os controlos essenciais**, mas aumentam a profundidade, cobertura e automação das validações de segurança durante o desenvolvimento.

---

## 1. ✅ Regras Semgrep customizadas

Adotar regras específicas da organização usando **Semgrep** permite:

- Detetar padrões perigosos contextuais à aplicação (ex: bypasses lógicos, endpoints sensíveis expostos).
- Implementar **segurança baseada em domínio** (ex: regras aplicadas apenas a microserviços críticos).
- Criar baseline de segurança específico por repositório ou stack.

---

## 2. ✅ Linters semânticos

Para além da sintaxe, usar **linters semânticos** que verifiquem:

- Padrões perigosos de lógica de negócio.
- Uso inadequado de APIs críticas (ex: criptografia, serialização).
- Falta de estruturas defensivas (ex: fail-safes, timeouts, try/catch adequados).

---

## 3. ✅ Análise de fluxo de dados (Data Flow Analysis)

Integrar ferramentas que analisam **como dados sensíveis percorrem a aplicação**, permitindo:

- Detetar caminhos de dados não validados.
- Rastrear uso de input não sanitizado.
- Identificar falhas de autorização por propagação.

---

## 4. ✅ Feedback contínuo e visibilidade por pull request

Implementar mecanismos de:

- Alertas de segurança diretamente nos PRs (pull requests).
- Dashboards com findings por projeto, equipa e tipo de falha.
- Integração com ferramentas de qualidade e métricas de engenharia.

---

## 5. ✅ Análise assistida por AI (com validação humana)

Utilizar ferramentas baseadas em **LLM (Large Language Models)** para:

- Sugerir remediações a findings comuns.
- Validar existência de controlos em funções críticas.
- Detetar fragilidades não triviais - **sempre com revisão humana final**.

---

## 6. ✅ Anotação semântica de segurança no código

Adotar anotação leve no código com tags como:

```js
// @sec:input-validated
// @sec:auth-required
// @sec:logged-contextual
```

Permite reforçar a rastreabilidade, acelerar revisões e suportar validações automáticas.

---

## 7. ✅ Triagem automatizada e baseada em contexto

Automatizar a classificação de findings com base em:

- Severidade (ex: CVSS, CWE).
- Contexto de uso na aplicação.
- Histórico de falsos positivos por projeto.

Evita sobrecarga de findings e foca a atenção no que importa.

---

## 8. ✅ Políticas de bloqueio por tipo de falha

Definir regras automáticas para bloquear merges ou releases com falhas críticas:

- Ex: `merge blocked if CWE-078 detected and not justified`
- Integração com listas de falhas bloqueadoras definidas pela organização.

---

## 9. ✅ Playbooks e auto-patch

Manter playbooks para falhas frequentes com:

- Explicação técnica.
- Modelo de correção.
- Scripts ou links para patch automation.

Integrar como ações automáticas em findings repetidos.

---

## 10. ✅ Formação adaptativa orientada por findings

Usar os findings reais da equipa como base para:

- Microlearning individualizado.
- Reforço formativo adaptado à stack e perfil técnico.
- Históricos de melhoria contínua.

---

## 11. ✅ Defesa contra prompt injection em aplicações LLM

Aplicações que **integram LLMs** (interfaces conversacionais, RAG, agentes com tool invocation) têm uma superfície de ataque específica que não é coberta por validação de input tradicional. A secção 5 (Análise assistida por AI) trata de LLM como **ferramenta de análise estática**; esta secção trata do caso oposto — quando a **aplicação em produção usa LLMs** e processa input que pode conter prompts maliciosos.

### Princípios

- **Tratar todo o input que chega ao contexto do modelo como untrusted** — inclui input directo do utilizador, conteúdo retrieval-augmented (RAG retrievals), ficheiros uploadados, web content fetchado pelo agente e outputs de tools chamadas pelo agente.
- **Separar canalmente system prompt de user input** — usar APIs com mensagens estruturadas (`system` / `user` / `assistant` roles) em vez de string concatenation; em pipelines RAG, marcar explicitamente "início e fim de contexto retrieval" para o modelo poder distinguir.
- **Output filtering** — detectar e bloquear padrões de exfiltração de system prompt (`AML.T0069.002`), padrões de comando que indicam jailbreak bem-sucedido, conteúdo que excede o scope da pergunta original.

### Práticas operacionais

- **Validação de input pré-modelo**: tamanho máximo do prompt, padrões conhecidos de jailbreak attempts (DAN, role-playing prompts maliciosos), encoding tricks (Base64, Unicode obfuscation) — útil mas insuficiente isoladamente, é defesa em profundidade não controlo único.
- **Sanitização de output ao destino de renderização** — outputs LLM colocados em HTML são vector de XSS persistente; aplicar VAL-008 (codificação contextual; ver Cap. 02 §VAL) ao output do modelo como se fosse user input não confiável.
- **Rate limiting agressivo por sessão** — prompt injection requer múltiplas iterações em muitos casos; thresholds devem distinguir uso normal de tentativas de exploração.
- **Logging completo de inputs e outputs do modelo** — com sanitização de PII; ver Cap. 12 §OPS-011 para framing observability.
- **Aprovação humana out-of-band para tool calls com impacto crítico** — em agentes autónomos, qualquer acção write/mutativa (delete, transfer, send, deploy) deve exigir confirmação explícita; arquitectura associada em Cap. 04 §AI/ML.

### Catálogos relevantes

- **OWASP LLM Top 10 (2025)** — particularmente LLM01 (Prompt Injection) e LLM02 (Sensitive Information Disclosure); referenciados em Cap. 03 §AI/ML.
- **MITRE ATLAS** techniques relevantes: `AML.T0051.001` Indirect Prompt Injection, `AML.T0086` Exfiltration via AI Agent Tool Invocation, `AML.T0069.002` System Prompt extraction.

> Estas práticas complementam (não substituem) os requisitos VAL- (input validation) e ENC- (output encoding) do Cap. 02. Em particular, **VAL-008** (codificação de output em renderização anti-XSS) aplica-se a outputs LLM colocados em superfícies renderizadas (HTML, terminal, logs).

---

> 💡 Muitas das práticas avançadas aqui descritas são suportadas nativamente por ferramentas comerciais consolidadas no mercado.  
> Plataformas como **Checkmarx**, **Kiuwan**, **Xygeni**, **Snyk**, entre outras, integram funcionalidades que cobrem desde SAST, SCA, tagging semântico, enforcement de políticas, até feedback direto em pipelines e PRs.  
> Assim, **não é necessário recorrer a um ecossistema disperso de ferramentas open source** para aplicar estas recomendações - o importante é garantir **a função de segurança**, independentemente da ferramenta escolhida.
