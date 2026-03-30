---
id: processo-excecoes
title: Processo Canónico de Gestão de Excepções
sidebar_position: 12
description: Processo formal, transversal e autoritário de gestão de excepções a requisitos e controlos de segurança no SbD-ToE
tags: [excecoes, governanca, risco, aprovacao, rastreabilidade, lifecycle]
---

# Processo Canónico de Gestão de Excepções

Este documento define o processo canónico de gestão de excepções no SbD-ToE.

É o documento de referência para todos os capítulos do manual. Cada capítulo de domínio especifica os seus triggers próprios, campos adicionais e integração com ferramentas - mas o processo, as alçadas e o lifecycle são invariantes e definidos aqui.

Uma excepção é uma decisão de risco formal: reconhece que um controlo não está aplicado, documenta porquê, define o que compensa e estabelece quando é revista. O que não está neste modelo não é uma excepção - é uma falha silenciosa.

---

## Âmbito

Aplica-se a qualquer situação em que um requisito ou controlo prescrito no SbD-ToE não seja aplicado na totalidade. Causas típicas:

- limitação técnica demonstrável (ex: sistema legado, SaaS sem suporte ao controlo);
- dependência externa incontrolável a curto prazo;
- custo de implementação desproporcionado face ao risco efectivo do contexto;
- migração faseada com janela de não-conformidade conhecida e delimitada;
- conflito funcional ou contratual com evidência documentada.

A causa não tem de ser excepcional - mas o tratamento tem de o ser. Toda a não-aplicação de um controlo activa este processo, sem excepção.

---

## Processo

### 1. Identificação

Definir com precisão o que está em causa:

- ID canónico do requisito ou controlo (ex: `ARC-003`, `DEP-007`, `IAC-003`);
- sistema, componente ou ambiente afectado;
- nível de risco do contexto (`L1`, `L2` ou `L3`).

A identificação incompleta invalida o registo.

### 2. Justificação técnica

Responder explicitamente a três perguntas:

1. Qual o motivo objectivo que impede a aplicação do controlo?
2. A excepção é temporária (prazo) ou estrutural (sem solução previsível)?
3. Existe alternativa técnica viável? Se sim, porque não é aplicada?

Justificações vagas ou genéricas não são aceites como fundamento de aprovação.

### 3. Avaliação de impacto

Quantificar o risco residual criado:

- que ameaças deixam de estar mitigadas?
- o nível de risco do contexto é afectado pela ausência deste controlo?
- o risco residual é aceitável com as compensações previstas?

### 4. Medidas compensatórias

Identificar os controlos alternativos que reduzem o risco residual a um nível aceitável. A compensação não precisa de ser equivalente ao controlo em falta - precisa de ser proporcional ao risco residual e verificável.

Excepções sem compensação identificada são aprovadas apenas em L1 com justificação de risco negligenciável.

### 5. Aprovação formal

A aprovação é explícita, registada e atribuída nominalmente a um papel com autoridade formal, de acordo com as alçadas definidas abaixo. Aprovações tácitas ou implícitas são inválidas.

### 6. Registo e activação do ciclo de monitorização

Após aprovação, a excepção é registada com todos os campos obrigatórios e integrada no ciclo de validação continuada (ver `addon/06-validacao-continuada.md`). A partir deste momento está activa, tem prazo e gera obrigação de revisão.

---

## Campos obrigatórios

| Campo | Obrigatório | Notas |
|---|---|---|
| ID da excepção | Sim | Ex: `IAC-EXC-003-2025-07-10`; formato pode ser adaptado por domínio |
| Requisito afectado | Sim | ID canónico (ex: `ARC-003`) + tag operacional do projecto (ex: `SEC-L2-ARC-003`) |
| Sistema / componente / ambiente | Sim | |
| Nível de risco (L1–L3) | Sim | |
| Justificação técnica | Sim | Motivo objectivo; sem vagas generalidades |
| Impacto e risco residual | Sim | |
| Medida compensatória | Sim | Controlo alternativo aplicado ou comprometido |
| **Quem pediu** | Sim | Autor do pedido - nome, função, equipa |
| **Quem criou a avaliação de risco** | Sim | Responsável pela análise de impacto e risco residual - nome e função |
| **Quem aprovou** | Sim | Aprovador formal - nome, função; conforme alçadas abaixo |
| Data de aprovação | Sim | |
| **Cadeia de autoridade** | Sim | Ver secção abaixo |
| **Evidências técnicas** | Sim | Artefactos que suportam justificação e compensação - relatórios de scanner, tickets, logs, ADRs, evidência de testes; referência por URL ou caminho rastreável |
| Data de expiração | Sim | Máx. 90 dias; extensão exige reavaliação |
| Trigger de revisão | Sim | Data fixa ou condição (incidente, mudança arquitectural, etc.) |

Campos em falta invalidam o registo. Um registo inválido não produz aprovação.

---

## Cadeia de autoridade

O registo de excepção não é o repositório dos artefactos de aprovação - é o índice que os referencia e garante que a cadeia é completa e rastreável. Os artefactos em si ficam nos sistemas onde foram produzidos (sistema de tickets, email, GRC, wiki).

O que o registo tem de capturar é a **sequência de decisão**: quem identificou o problema, quem escalou, quem avaliou o risco, quem deu instrução de avançar e com que condições.

Estrutura mínima obrigatória:

| Passo | Papel | O que tem de ficar registado | Referência |
|---|---|---|---|
| Pedido de excepção | Dev / PM / Arquitecto | Descrição do problema, motivo da impossibilidade técnica e contexto | URL / ID |
| Instrução de escalada | Tech Lead / BAO | Contexto de negócio, indicação de escalada e condições conhecidas | URL / ID |
| Avaliação de risco | AppSec | Análise de impacto, risco residual e parecer sobre compensações | URL / ID |
| Aprovação formal | Conforme alçadas (L1/L2/L3) | Decisão explícita com condições e validade | URL / ID |

O meio não é prescrito - ticket, comentário num PR, nota num sistema GRC, registo em wiki, decisão num ADR. O que é prescrito é que **cada passo tem de ter uma acção registada, datada e atribuída a um papel**, com referência rastreável no campo correspondente.

> Uma aprovação verbal sem registo não conta. Uma cadeia com passos em falta não produz aprovação válida.

---

## Alçadas de aprovação

| Nível | Aprovação mínima |
|---|---|
| **L1** | Responsável técnico (Tech Lead ou equivalente) |
| **L2** | AppSec + responsável técnico |
| **L3** | AppSec + GRC/CISO; medida compensatória obrigatória |

Excepções L3 sem aprovação de AppSec e GRC/CISO são não conformes independentemente do conteúdo do registo.

---

## Validade, renovação e expiração

O prazo máximo por defeito é **90 dias**. Extensões exigem nova avaliação completa - não são automáticas nem concedidas por omissão.

Excepções expiradas sem renovação activa constituem **não conformidade** a partir da data de expiração. Devem ser tratadas como tal no ciclo de auditoria.

Triggers de revisão obrigatória fora do prazo normal:

- incidente de segurança com relação directa ao controlo em falta;
- alteração de arquitectura, risco ou classificação do sistema afectado;
- mudança de fornecedor, dependência ou ambiente com impacto no pressuposto da excepção.

---

## Indicadores de maturidade

O número e a qualidade das excepções activas num projecto são sinais directos de maturidade de segurança:

- muitas excepções abertas em L3 indicam dívida técnica de segurança não gerida;
- excepções com compensações verificáveis e prazo cumprido indicam processo funcionante;
- excepções expiradas sem renovação indicam ausência de governação efectiva.

Ver `kpis-governanca.md` para os indicadores organizacionais associados.

---

## Especificidades por domínio

Cada capítulo de domínio define num ficheiro próprio os triggers característicos, campos adicionais, templates e integração com ferramentas. O processo desta secção aplica-se sempre, sem substituição.

| Capítulo | Ficheiro de especificidades |
|---|---|
| Cap. 02 - Requisitos aplicacionais | `addon/08-gestao-excecoes.md` |
| Cap. 04 - Arquitectura Segura | `addon/03-excecoes.md` |
| Cap. 05 - Dependências e SBOM | `addon/09-excecoes-e-aceitacao-risco.md` |
| Cap. 06 - Desenvolvimento Seguro | `addon/05-excecoes-e-justificacoes.md` |
| Cap. 07 - CI/CD Seguro | `addon/09-controle-excecoes-visibilidade.md` |
| Cap. 08 - IaC | `addon/09-gestao-excecoes.md` |

---

## Referências cruzadas

| Documento | Relação |
|---|---|
| `addon/01-modelo-governancao.md` | Papéis, alçadas e ciclo de decisão de governação |
| `addon/06-validacao-continuada.md` | Ciclo de revalidação e gestão de expiração |
| `addon/05-exemplos-praticos.md` | Exemplos concretos de excepções aprovadas |
| `addon/08-diagramas-governanca.md` | Fluxograma do processo de aprovação |
| `kpis-governanca.md` | Indicadores de excepções activas e maturidade |
| SSDF GV.3 / RV.1 | Aprovação de excepções e gestão de desvios |
| ISO/IEC 27001 A.18.1.4 | Aceitação formal de riscos residuais |
| OWASP SAMM Governance | Registo e lifecycle de decisões excepcionais |

---
