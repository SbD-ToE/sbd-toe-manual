---
id: governanca-automatismos
title: Governação do Uso de Automatismos e Assistentes no SSDLC
description: Prescrição para o uso controlado de ferramentas de geração automatizada (incluindo IA) no desenvolvimento, sem alteração dos requisitos aplicacionais
tags: [governanca, automatizacao, ia, sdlc, requisitos, validacao, rastreabilidade, agentic, mandates]
---

# 🛠️ Governação do Uso de Automatismos no Desenvolvimento

Este anexo define **princípios, regras e obrigações mínimas** para o uso de **ferramentas de automatização e geração assistida** (incluindo assistentes baseados em IA, low-code/no-code e geração automática de código) no contexto do *Secure Software Development Lifecycle* (SSDLC).

O seu objetivo é **assegurar que a adoção destas ferramentas não compromete**:
- a validade dos **requisitos de segurança** definidos no Capítulo 2;
- a **rastreabilidade** entre risco, requisito, controlo e evidência;
- a **verificabilidade prática** e a responsabilização humana.

> ⚠️ Este anexo **não define novos requisitos aplicacionais** nem altera o catálogo T01–T20.  
> Define apenas **condições de governação e validação** para a correta aplicação dos requisitos existentes quando são usados automatismos.

---

## 🎯 Âmbito e enquadramento

Este anexo aplica-se sempre que, no processo de desenvolvimento, sejam utilizados:

- Assistentes de código baseados em IA (ex.: *code assistants*, *copilots*);
- Plataformas *low-code / no-code*;
- Ferramentas de geração automática de código, configurações ou testes;
- Automatismos que produzam *artefactos executáveis* ou logicamente relevantes.

Não se aplica:
- a sistemas cujo **produto final seja um sistema de IA** (ver manual SbD-AI-ToE);
- a ferramentas puramente informativas sem impacto no código, configuração ou lógica.

---

## 🧠 Princípios fundamentais (normativos)

As regras seguintes são **invariantes** no modelo SbD-ToE:

1. **A responsabilidade é sempre humana**  
   Nenhuma decisão técnica ou de segurança pode ser atribuída a uma ferramenta.

2. **Output automatizado não é evidência**  
   Código, testes ou configurações geradas automaticamente **não constituem evidência de cumprimento** de requisitos.

3. **Código gerado é tratado como código de terceiros**  
   Está sujeito às mesmas validações, revisões e controlos.

4. **A validação é obrigatória e explícita**  
   Todo o output relevante deve ser validado por mecanismos humanos e/ou automatizados.

5. **A rastreabilidade não é opcional**  
   A utilização de automatismos **não quebra nem simplifica** as exigências de rastreabilidade.

---

## 🔗 Impacto nos temas de requisitos existentes

O uso de automatismos **reforça** (não substitui) as obrigações nos seguintes temas do catálogo:

| Tema | Impacto específico |
|---|---|
| **T11 – Segurança do Código e Build** | Revisão humana obrigatória de código gerado |
| **T12 – Dependências e SBOM** | Identificação de dependências implícitas introduzidas |
| **T13 – CI/CD Seguro** | Gates automáticos tornam-se críticos |
| **T17 – Testes de Segurança** | Testes não podem assumir confiança implícita |
| **T20 – Governação e Conformidade** | Uso deve ser conhecido, autorizado e auditável |

> Estes impactos são operacionalizados no ficheiro `aplicacao-lifecycle.md` através de user stories e gates específicos.

---

## ⚙️ Regras mínimas de governação

### 1. Uso autorizado e conhecido
- A organização **deve saber** que ferramentas são usadas;
- O uso deve estar coberto por política interna (ver Cap. 14).

### 2. Proteção de informação
- É **proibido** introduzir segredos, chaves, dados sensíveis ou informação confidencial em prompts;
- A violação constitui incidente de segurança.

### 3. Revisão humana obrigatória
- Todo o código/configuração gerada deve ser:
  - revisto por um developer qualificado;
  - sujeito aos mesmos critérios de *code review*.

### 4. Validação técnica independente
- SAST, SCA, testes e validações **não podem ser desativados** por “confiança na ferramenta”.

### 5. Gestão de exceções
- Qualquer atalho ou não aplicação de controlo segue o **processo formal de exceções** do Capítulo 14, com TTL.

---

---

## 🤖 Modelo de níveis de autonomia para agentes AI {#niveis-autonomia}

Até aqui falámos de **automatismos assistidos** — ferramentas que sugerem, mas onde a decisão e a execução são humanas. Nos últimos meses passámos a viver com uma classe diferente de ferramenta: **agentes** que recebem um objectivo, decidem por que passos avançar, invocam *tools* reais (criar PR, correr testes, ler segredos, fazer deploy), e podem fazê-lo com graus variáveis de supervisão humana. *Copilot Workspace*, *Claude Code*, *Cursor agent mode*, *Devin*, agentes construídos sobre SDKs próprios — todos cabem aqui.

Quando passamos de "ferramenta que sugere" para "agente que executa", a pergunta deixa de ser *"foi revisto?"* e passa a ser *"foi autorizado a fazer isto, neste contexto, com este alcance?"*. Adoptamos por isso um **modelo de cinco níveis de autonomia (A0–A4)** que torna essa autorização explícita, classificável e auditável.

> 📌 Os níveis A0–A4 **não substituem** os princípios fundamentais (responsabilidade humana, output não é evidência, código gerado é código de terceiros). Especializam-nos para o caso em que o agente *executa* e não apenas *sugere*.

### Níveis A0–A4

| Nível | Designação | O que o agente pode fazer | Aprovação humana exigida | Onde aplica tipicamente |
|---|---|---|---|---|
| **A0** | *Read-only / consulta* | Lê código, docs, logs; responde perguntas; sugere em janela de chat | Não exigida; output não é actuado | Sessões exploratórias, debug assistido, perguntas sobre o manual |
| **A1** | *Propõe alterações* | Gera *patches*, abre PRs em estado *draft*, escreve testes, propõe configurações | Sim, **no momento de merge / aplicar**; revisão humana clássica do output | Uso quotidiano de *Copilot* / *Claude Code* em modo "propõe-só" |
| **A2** | *Executa com confirmação por acção destrutiva* | Executa acções idempotentes/leves sem confirmar (correr testes, listar recursos, ler config); pede confirmação explícita antes de cada acção destrutiva ou *side-effectful* (apagar, escrever em sistemas externos, rodar segredos, fazer *commit/push*, abrir PR fora de *draft*) | Sim, **por acção** destrutiva ou de impacto | Workflows automatizados com humano de plantão (auditoria de PR, *codegen grounded*, *threat modeling* assistido) |
| **A3** | *Executa autonomamente com revert automático* | Executa cadeias completas sem confirmação intermédia, dentro de um *scope* previamente acordado, com mecanismo de *revert* automático em falha detectada (testes, *health checks*, *anomaly detection*) | **Pós-facto**: notificação obrigatória ao humano responsável; revisão periódica obrigatória do log de sessões | Automações de manutenção (*dependabot* AI-driven, *autofix* de *findings* SAST de baixa criticidade, geração e merge de testes de regressão) |
| **A4** | *Autónomo total em produção* | Opera continuamente em produção, dentro de mandate registado, sem aprovação por acção; *kill-switch* operacional disponível 24/7 | Auditoria periódica obrigatória (cadência ≤ trimestral); *kill-switch* exercitado pelo menos uma vez por trimestre | *SRE* assistido, agentes de remediação de alertas, *moderation* automatizada — apenas com *mandate* formal e *guardrails* multi-camada |

> 🧭 **Como ler a tabela.** A classificação é feita **por agente e por contexto** (não por organização). O mesmo agente pode ser A1 num projecto L1 interno e A2 num L2 público; nunca A4 em qualquer projecto sem *mandate* formal (ver `REQ-AGN-001`).

### Critérios para escolher o nível certo

Subir de nível **adiciona** obrigações, nunca as remove. A regra prática é a mais conservadora compatível com o trabalho real:

1. Começamos em **A1** sempre que o agente ainda é novo ao projecto ou à equipa.
2. Subimos a **A2** quando temos auditoria operacional fiável das *tool invocations* e *guardrails* per-tool.
3. **A3** exige *revert automático* demonstrado em ambiente de teste e cobertura de testes que detecta o tipo de falha que o agente pode introduzir.
4. **A4** exige *mandate* assinado pelo `CISO` (ou equivalente), *kill-switch* exercitado, e auditoria periódica calendarizada.

Descida de nível (e.g. A2 → A1) é sempre legítima e não exige justificação formal. Subida exige *mandate* (ver `REQ-AGN-001`) e evidência operacional dos pré-requisitos.

---

## 📋 Requisitos REQ-AGN — agentes AI no SDLC

Estes requisitos são **transversais** aos capítulos 03 (Threat Modeling), 04 (Arquitetura), 06 (Desenvolvimento), 07 (CI/CD), 10 (Testes), 12 (Monitorização) e 14 (Governança). Não substituem requisitos existentes — adicionam a camada agentic específica.

| ID | Requisito | L1 | L2 | L3 | Descrição |
|---|---|:--:|:--:|:--:|---|
| **REQ-AGN-001** | *Mandate registado e versionado* | ✔ | ✔ | ✔ | Cada agente em uso operacional (A1+) tem *mandate* documentado e versionado em VCS contendo: identidade, nível de autonomia, escopo de *tools* permitidas, ambientes onde opera, *owner* humano, periodicidade de revisão. Sem *mandate* válido o agente não opera além de A0. Operacionalizado por [Policy 38 — Mandates de agentes AI](/sbd-toe/assets/policies/policy-mandates-agentes). |
| **REQ-AGN-002** | *Nível de autonomia classificado por contexto* | ✔ | ✔ | ✔ | Cada uso de agente declara o nível A0–A4 aplicável ao contexto específico (projecto × ambiente × tarefa). Mudança de contexto re-avalia o nível. A4 só com *mandate* assinado pelo `CISO` e auditoria calendarizada. |
| **REQ-AGN-003** | *Kill-switch operacional documentado e testado* | — | ✔ | ✔ | Para agentes A2+, existe mecanismo documentado para interromper a operação imediatamente (revogar credenciais, terminar sessão, isolar runtime). O *kill-switch* é exercitado em sandbox/staging pelo menos uma vez por trimestre (A3) ou por mês (A4); resultado registado. |
| **REQ-AGN-004** | *Intent declaration antes de tool-call destrutivo* | — | ✔ | ✔ | Em agentes A2+, antes de cada *tool call* com efeito destrutivo ou *side-effectful* (apagar, escrever externo, rotacionar segredos, *commit/push*, *deploy*), o agente declara à infraestrutura (log estruturado, *audit event*) **o que vai fazer e porquê**, antes de o fazer. O gate audita *intent* vs *acção real* a posteriori. |

> 💡 **Onde aterram estes requisitos.** `REQ-AGN-001` é instrumentado pela Policy 38 e referenciado em Cap. 14. `REQ-AGN-002` é declarado no *mandate* (Policy 38) e validado por *guardrails* em Cap. 04 (`ARC-015`). `REQ-AGN-003` aterra no Cap. 04 (arquitetura do *kill-switch*) e Cap. 12 (telemetria que o dispara). `REQ-AGN-004` aterra no Cap. 04 (mecanismo) e Cap. 12 (sinal audit).

### Proporcionalidade por criticidade

| Nível de risco | Requisitos mínimos | Notas operacionais |
|---|---|---|
| **L1** | `REQ-AGN-001`, `REQ-AGN-002` | A2+ permitido apenas em ambientes não-produtivos; em produção limitar a A0/A1 |
| **L2** | `REQ-AGN-001`, `REQ-AGN-002`, `REQ-AGN-003`, `REQ-AGN-004` | A3 em produção apenas para tarefas com *revert* demonstrado; A4 fora de scope típico |
| **L3** | Todos + auditoria trimestral do registo de *mandates* | A4 apenas com *mandate* assinado pelo `CISO` e revisão GRC; preferência por A2 mesmo em automações maduras |

### Como classificar um uso concreto — fluxo decisório

1. **Identificar o uso**: que agente, em que projecto/ambiente, para que tarefa.
2. **Mapear *tools* invocadas** e marcar as destrutivas/*side-effectful*.
3. **Mapear o efeito da pior acção** que o agente pode tomar nesse escopo.
4. **Escolher o nível mais baixo** compatível com o trabalho real.
5. **Registar o *mandate*** (Policy 38) com nível, *tools*, *owner*, revisão.
6. **Operacionalizar `REQ-AGN-003/004`** se A2+, antes de o agente operar.

> 🛑 Quando ficamos em dúvida entre dois níveis, escolhemos sempre o mais baixo. Subir é sempre mais fácil que reparar consequências de ter subido cedo demais.

---

## 🧪 Evidência e auditoria

A evidência **não é o uso da ferramenta**, mas sim:

- Resultados de testes;
- Logs de pipelines CI/CD;
- Aprovações humanas documentadas;
- Rastreabilidade entre:
  - risco → requisito → controlo → validação.

Quando relevante, deve existir referência explícita de que **foi usado automatismo**, sem necessidade de detalhar prompts ou modelos.

---

## 📚 Alinhamento normativo e referências

Este anexo está alinhado com as seguintes referências:

- **NIST SP 800-218A** - Secure Software Development Framework Profile for GenAI  
- **NIST AI Risk Management Framework 1.0**  
- **ISO/IEC 42001:2023** - AI Management System  
- **OpenSSF – Secure Use of AI Code Assistants**

Estas referências **não criam novos requisitos aplicacionais**, mas reforçam princípios de governação, responsabilização e validação já existentes no SbD-ToE.

---

## 🧭 Relação com outros capítulos

- Capítulo 1 - Classificação de risco: o uso de automatismos **não altera L1–L3**;
- Capítulo 2 - Requisitos de Segurança: requisitos mantêm-se inalterados;
- Capítulo 7 - CI/CD Seguro: gates automáticos tornam-se críticos;
- Capítulo 14 - Governação e Exceções: políticas, formação e controlo formal.

---

## ✅ Conclusão

O SbD-ToE **compreende e aceita a IA como ferramenta poderosa**, mas rejeita qualquer modelo onde:
- a confiança substitua validação;
- a automação substitua responsabilidade;
- a conveniência comprometa evidência.

Este anexo assegura que a adoção de automatismos **reforça** - e nunca fragiliza - a aplicação rigorosa dos requisitos de segurança definidos neste manual.

