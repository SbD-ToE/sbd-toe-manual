---
id: policy-uso-ferramentas-apoio
title: Política de Uso de Ferramentas de Apoio ao Desenvolvimento
description: Política organizacional que define os requisitos para o uso controlado de ferramentas de apoio ao desenvolvimento, incluindo assistentes de IA generativa (GenAI/Copilot) e agentes autónomos com tool-use (A0–A4), com foco em revisão obrigatória de output, rastreabilidade, validação de licenças, mandates de autonomia e manutenção da responsabilidade humana, proporcional ao nível de criticidade (L1, L2, L3).
tags: [policy, GenAI, Copilot, ferramentas, assistentes IA, revisão, licenças, rastreabilidade, desenvolvimento seguro, cap06, L1, L2, L3, governance, agentic, autonomy]
grupo: desenvolvimento
sidebar_position: 16
---

# Política de Uso de Ferramentas de Apoio ao Desenvolvimento

## 1. Objetivo

Esta política define os requisitos para o **uso controlado de ferramentas de apoio ao desenvolvimento**, com particular enfoque em assistentes de inteligência artificial generativa (GenAI), ferramentas de geração de código, autocompletion assistido e sistemas de sugestão automática.

A adoção de ferramentas GenAI no desenvolvimento de software é uma realidade crescente e, quando bem governada, pode aumentar a produtividade sem comprometer a segurança. O risco não está na ferramenta em si, mas na ausência de revisão e validação do output gerado - que pode conter vulnerabilidades conhecidas, violações de licença, ou desalinhamento com requisitos técnicos e de segurança que o modelo de linguagem desconhece.

O objetivo desta política é garantir que:

- O uso de ferramentas de apoio ao desenvolvimento é registado e rastreável
- Todo o output gerado automaticamente é sujeito a revisão técnica humana antes de ser aceite
- Os constrangimentos técnicos e de segurança aplicáveis ao projeto são comunicados à ferramenta e verificados no output
- A responsabilidade pela qualidade e segurança do código permanece humana, independentemente da origem do código

---

## 2. Âmbito

Esta política aplica-se a qualquer ferramenta de apoio ao desenvolvimento que gere, sugira ou complete código, configuração, testes ou documentação técnica de forma automatizada, incluindo (sem carácter exclusivo):

- Assistentes GenAI integrados no IDE (GitHub Copilot, Amazon CodeWhisperer, Tabnine, Cursor, etc.)
- Assistentes GenAI conversacionais usados para geração de código (ChatGPT, Claude, Gemini, etc.)
- Ferramentas de geração de testes automatizados por IA
- Geradores de IaC, configuração ou scripts por IA

Não está no âmbito desta política o uso de ferramentas determinísticas de scaffolding ou de templates curados internamente (ex: `cookiecutter`, templates de projeto aprovados).

---

## 3. Princípio fundamental: a responsabilidade é sempre humana

O uso de ferramentas GenAI não transfere nem dilui a responsabilidade do developer pelo código produzido. O código gerado por IA é tratado como **código de terceiros não auditado** - deve ser lido, compreendido, validado e assumido pelo developer antes de ser incluído numa base de código.

:::warning
A aceitação de sugestões automáticas sem leitura e compreensão do código gerado é equivalente a copiar código de uma fonte desconhecida sem revisão. Esta prática é proibida em qualquer nível de criticidade.
:::

---

## 4. Regras de uso por nível

| Requisito | L1 | L2 | L3 |
|---|---|---|---|
| Registo de uso de GenAI em PRs | Opcional | Obrigatório | Obrigatório |
| Revisão técnica humana do output antes de submeter | Obrigatório | Obrigatório | Obrigatório |
| Constrangimentos técnicos do projeto comunicados à ferramenta | Recomendado | Obrigatório | Obrigatório |
| Validação de licença do output | Recomendado | Obrigatório | Obrigatório |
| Revisão de código com foco em output GenAI | Recomendado | Obrigatório | Obrigatório + AppSec |
| Ferramentas aprovadas pela organização | Recomendado | Obrigatório | Obrigatório |
| Proibição de envio de código confidencial para ferramentas externas | Obrigatório | Obrigatório | Obrigatório |

---

## 5. Aprovação de ferramentas

Antes de adotar uma nova ferramenta de apoio ao desenvolvimento, deve ser realizada uma avaliação que cubra:

- [ ] Modelo de dados: o código ou prompts enviados são usados para treino do modelo?
- [ ] Localização de processamento: os dados são processados em infraestrutura que cumpre os requisitos de privacidade aplicáveis?
- [ ] Licença do output: existe risco de output com licenças incompatíveis com o produto (ex: GPL contaminante)?
- [ ] Integração com repositório interno: a ferramenta acede a código confidencial? Com que controlos?
- [ ] Conformidade com requisitos regulatórios aplicáveis (GDPR, DORA, NIS2, etc.)

A aprovação deve ser registada e a lista de ferramentas aprovadas publicada internamente.

:::warning
O uso de ferramentas não aprovadas pela organização para gerar código de produção é proibido em L2/L3, independentemente de ser uso pessoal ou integrado no IDE.
:::

---

## 6. Constrangimentos técnicos

Antes de utilizar uma ferramenta GenAI para gerar código relacionado com um projeto, o developer deve comunicar à ferramenta os constrangimentos técnicos relevantes:

- Stack tecnológica, versões e frameworks em uso
- Bibliotecas proibidas ou aprovadas
- Padrões de segurança obrigatórios (ex: "não usar concatenação SQL", "usar ORM X", "seguir guideline Y")
- Requisitos de segurança aplicáveis ao contexto

Estes constrangimentos devem estar versionados por projeto (`constrangimentos-genia.md` ou equivalente) e ser referenciados nos PRs que incluam output GenAI.

---

## 7. Rastreabilidade do output GenAI

Em L2/L3, os PRs que incluam código gerado ou significativamente assistido por ferramentas GenAI devem indicá-lo explicitamente:

- [ ] Referência no corpo do PR à ferramenta utilizada (ex: "Secções X e Y geradas com Copilot, revistas manualmente")
- [ ] Constrangimentos aplicados documentados ou referenciados
- [ ] Registo em `uso-genia.md` (ou equivalente) quando aplicável ao projeto

O objetivo não é criar burocracia, mas assegurar que os reviewers sabem que o código foi gerado automaticamente e devem dar atenção redobrada à sua revisão.

---

## 8. Validação de licenças

Ferramentas GenAI podem sugerir código que reproduz parcialmente código com licenças restritivas (copyleft). Para mitigar este risco:

- [ ] Verificar se a ferramenta tem modo de filtragem de sugestões com correspondência em código público sob licenças incompatíveis (ex: GitHub Copilot "Duplication detection")
- [ ] Não aceitar sugestões de blocos de código extensos sem verificar se são derivações de código licenciado
- [ ] Em L3, submeter output extenso a análise de licença antes de inclusão

---

## 9. Proibição de envio de informação confidencial

É proibido enviar para ferramentas GenAI externas (não aprovadas para processamento de dados confidenciais):

- Código que contenha segredos, chaves, tokens ou credenciais
- Dados de produção, PII ou dados classificados como confidenciais
- Código de sistemas com informação sobre vulnerabilidades não divulgadas
- Documentação interna classificada

Em L3, antes de usar qualquer ferramenta GenAI em contexto do projeto, deve ser verificado se o contrato de serviço cobre os requisitos de confidencialidade aplicáveis.

---

## 10. Responsabilidades

| Role | Responsabilidade |
|---|---|
| Developer | Usar apenas ferramentas aprovadas; rever todo o output antes de submeter; registar uso em L2/L3; não enviar informação confidencial |
| Tech Lead | Garantir que a equipa conhece e segue esta política; rever PRs com output GenAI com atenção adicional |
| AppSec Engineer | Definir e publicar lista de ferramentas aprovadas; rever constrangimentos técnicos por projeto; avaliar novas ferramentas |
| GRC / Legal | Avaliar conformidade regulatória e de licenciamento das ferramentas candidatas |
| DevOps / SRE | Configurar, se aplicável, ferramentas aprovadas com acesso controlado ao repositório |

---

## 11. Agentes autónomos (A2+) com tool-use

As secções 1–10 cobrem o caso geral: a ferramenta **sugere** e o developer **decide**. Quando o que a ferramenta faz passa a ser **executar acções com efeito real** — abrir PRs, ler segredos, fazer deploys, escrever em sistemas externos — entramos em território de **agentes autónomos**, com graus variáveis de supervisão humana. O modelo de cinco níveis de autonomia (A0–A4) está definido no [Cap. 02 — Modelo de níveis de autonomia](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#niveis-autonomia); aplicam-se aqui sem reformulação.

### 11.1 Onde esta política se aplica vs. Policy 38

| Cenário | Coberto por |
|---|---|
| Uso assistido (A0–A1) — ferramenta sugere, developer decide | Secções 1–10 desta política |
| Uso autónomo (A2–A4) — agente executa acções reais | **Esta secção 11** (regras operacionais) + [Policy 38 — Mandates de agentes AI](./policy-mandates-agentes) (mandate, ownership, revisão) |

> 📌 **A separação importa.** As secções 1–10 são suficientes para Copilot/Cursor em modo *sugere*. A partir do momento em que o agente executa (`gh pr create`, `kubectl apply`, `terraform apply`, `npm publish`, qualquer ação fora do IDE), passa a aplicar-se a Policy 38 *além desta*.

### 11.2 Regras operacionais para A2+

| Regra | A2 | A3 | A4 |
|---|:--:|:--:|:--:|
| **Mandate registado e versionado em VCS** (Policy 38) | ✔ | ✔ | ✔ |
| **Identidade dedicada** com workload identity efémera (OIDC, TTL ≤ 1h) — ver [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015) | ✔ | ✔ | ✔ |
| **Scope mínimo por tool** declarado no mandate | ✔ | ✔ | ✔ |
| **Intent declaration** antes de tool call destrutivo ([`REQ-AGN-004`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn)) | ✔ | ✔ | ✔ |
| **Aprovação humana out-of-band** por acção destrutiva | ✔ | (substituída por revert auto + notificação) | (apenas auditoria periódica) |
| **Revert automático** demonstrado em testes | — | ✔ | ✔ |
| **Kill-switch** documentado e operacional ([`REQ-AGN-003`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn)) | ✔ | ✔ | ✔ |
| **Kill-switch exercitado** com cadência registada | Anual | Trimestral | Mensal |
| **Mandate assinado por `CISO`** (não apenas registado) | — | — | ✔ |
| **Auditoria periódica do mandate** | Anual | Semestral | Trimestral |

### 11.3 Proibições específicas em A2+

- ❌ **Reutilizar credenciais humanas** para autenticar o agente. Cada agente é um *principal* distinto.
- ❌ **Aprovar acções destrutivas dentro do canal do agente** (e.g. pedir confirmação no chat onde o agente opera) — viola o princípio out-of-band; resposta a prompt injection torna-se trivialmente aprovável.
- ❌ **Subir nível de autonomia (A1 → A2, A2 → A3, …) sem revisão e actualização do mandate.** Subida exige evidência operacional dos pré-requisitos.
- ❌ **Operar em produção em A3/A4 sem revert automático demonstrado em ambiente de teste.** Se não foi exercitado, é decorativo.
- ❌ **A4 em qualquer projecto sem mandate assinado pelo `CISO`.** Sem excepções.

### 11.4 Reporte de incidentes específicos a agentes

Constituem incidentes de segurança que devem ser reportados via processo IR (Cap. 12):

- *Off-policy action*: agente executou acção fora do scope declarado no mandate.
- *Intent-action divergence*: acção real difere materialmente do `intent` declarado.
- *Prompt injection bem-sucedida* que resultou em tool call não autorizada.
- *Kill-switch falhou* ou demorou > tempo acordado a fazer efeito.
- *Credential exposure*: identidade do agente reutilizada ou exposta fora do âmbito.

---

## 12. Revisão e auditoria desta política

Esta política deve ser **revista semestralmente** dada a rápida evolução das ferramentas GenAI, ou após qualquer um dos seguintes eventos:

- Identificação de vulnerabilidade com origem em output GenAI não revisto
- Alteração significativa nas capacidades ou modelo de dados de uma ferramenta aprovada
- Alteração regulatória com impacto no uso de IA no desenvolvimento de software

---

## 13. Referências normativas e técnicas

| Referência | Relevância |
|---|---|
| SbD-ToE Cap. 06 - Desenvolvimento Seguro | Uso controlado de GenAI, rastreabilidade, constrangimentos |
| SbD-ToE Cap. 02 - Requisitos de Segurança (addon `09-governaca-automatismos`) | Modelo de níveis de autonomia A0–A4; `REQ-AGN-001..004` |
| SbD-ToE Cap. 04 - Arquitetura Segura ([`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015)) | Agente como *principal* com workload identity efémera e least privilege |
| SbD-ToE Cap. 03 - Threat Modeling (playbook agentic) | Threat library para agentes com tool-use (MITRE ATLAS `AML.T*`, OWASP LLM Top 10) |
| Política 38 — Mandates de Agentes AI (`38_policy-mandates-agentes.md`) | Operacionalização de [`REQ-AGN-001`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn): mandate, ownership, revisão |
| Política de Revisão de Código (`15_policy-revisao-codigo.md`) | Revisão de PRs com output GenAI |
| Política de Guidelines de Desenvolvimento (`14_policy-guidelines-desenvolvimento.md`) | Constrangimentos técnicos derivados de guidelines |
| MITRE ATLAS | Catálogo canónico de tactics/techniques adversariais para AI systems |
| OWASP Top 10 for LLM Applications (2025) | Riscos de segurança em aplicações baseadas em LLM (LLM01–LLM10 2025) |
| NIST AI RMF 1.0 (2023) + Generative AI Profile (2024) | Risk Management Framework para AI: GOVERN / MAP / MEASURE / MANAGE |
| NIST SP 800-218A | Secure Software Development Framework Profile for GenAI |
| NIST SP 800-207 | Zero Trust Architecture — princípios aplicáveis a agentes como *principals* não-humanos |
| ISO/IEC 42001:2023 | AI Management System (alinha com [`REQ-AGN-001`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn) e revisão periódica) |
| EU AI Act (Reg. (UE) 2024/1689) | Requisitos regulatórios para sistemas de IA — ver [cross-check AI Act](/sbd-toe/cross-check-normativo/ai-act/intro) |
| ENISA - Cybersecurity of AI | Orientações de segurança para uso de IA em desenvolvimento |
| GitHub Copilot Trust Center | Modelo de dados e privacidade de ferramenta de referência |
