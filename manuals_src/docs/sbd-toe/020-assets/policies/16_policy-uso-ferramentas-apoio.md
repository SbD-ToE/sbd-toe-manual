---
id: policy-uso-ferramentas-apoio
title: Política de Uso de Ferramentas de Apoio ao Desenvolvimento
description: Política organizacional que define os requisitos para o uso controlado de ferramentas de apoio ao desenvolvimento, incluindo assistentes de IA generativa (GenAI/Copilot), com foco em revisão obrigatória de output, rastreabilidade, validação de licenças e manutenção da responsabilidade humana, proporcional ao nível de criticidade (L1, L2, L3).
tags: [policy, GenAI, Copilot, ferramentas, assistentes IA, revisão, licenças, rastreabilidade, desenvolvimento seguro, cap06, L1, L2, L3, governance]
sidebar_position: 16
---

# Política de Uso de Ferramentas de Apoio ao Desenvolvimento

## 1. Objetivo

Esta política define os requisitos para o **uso controlado de ferramentas de apoio ao desenvolvimento**, com particular enfoque em assistentes de inteligência artificial generativa (GenAI), ferramentas de geração de código, autocompletion assistido e sistemas de sugestão automática.

A adoção de ferramentas GenAI no desenvolvimento de software é uma realidade crescente e, quando bem governada, pode aumentar a produtividade sem comprometer a segurança. O risco não está na ferramenta em si, mas na ausência de revisão e validação do output gerado — que pode conter vulnerabilidades conhecidas, violações de licença, ou desalinhamento com requisitos técnicos e de segurança que o modelo de linguagem desconhece.

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

O uso de ferramentas GenAI não transfere nem dilui a responsabilidade do developer pelo código produzido. O código gerado por IA é tratado como **código de terceiros não auditado** — deve ser lido, compreendido, validado e assumido pelo developer antes de ser incluído numa base de código.

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

## 11. Revisão e auditoria desta política

Esta política deve ser **revista semestralmente** dada a rápida evolução das ferramentas GenAI, ou após qualquer um dos seguintes eventos:

- Identificação de vulnerabilidade com origem em output GenAI não revisto
- Alteração significativa nas capacidades ou modelo de dados de uma ferramenta aprovada
- Alteração regulatória com impacto no uso de IA no desenvolvimento de software

---

## 12. Referências normativas e técnicas

| Referência | Relevância |
|---|---|
| SbD-ToE Cap. 06 — Desenvolvimento Seguro | Uso controlado de GenAI, rastreabilidade, constrangimentos |
| SbD-ToE Cap. 02 — Requisitos de Segurança | US-14: uso controlado de assistentes automatizados |
| Política de Revisão de Código (`15_policy-revisao-codigo.md`) | Revisão de PRs com output GenAI |
| Política de Guidelines de Desenvolvimento (`14_policy-guidelines-desenvolvimento.md`) | Constrangimentos técnicos derivados de guidelines |
| OWASP Top 10 LLM Application Security Risks | Riscos de segurança em aplicações baseadas em LLM |
| EU AI Act | Requisitos regulatórios para sistemas de IA em contextos de alto risco |
| ENISA — Cybersecurity of AI | Orientações de segurança para uso de IA em desenvolvimento |
| GitHub Copilot Trust Center | Modelo de dados e privacidade de ferramenta de referência |
