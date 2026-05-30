---
id: genia-e-seguranca
title: Uso de GenIA no Desenvolvimento Seguro
sidebar_position: 10
description: Boas práticas e controlos para uso seguro de ferramentas de IA generativa na escrita de código e revisão automática
tags: [genia, ai, código gerado, validação, segurança, revisão]
---


# 🤖 Uso de GenIA no Desenvolvimento Seguro

A integração de ferramentas de inteligência artificial generativa (GenIA) como **GitHub Copilot**, **ChatGPT**, **Claude**, **CodeWhisperer**, entre outras, tornou-se uma realidade no dia a dia do desenvolvimento - independentemente da existência de políticas formais.

Estas ferramentas passaram a atuar como **assistentes contínuos**, não apenas de produtividade, mas também de qualidade e segurança. Mesmo sem instruções explícitas, a sua presença **influencia a forma como código é escrito, estruturado e comentado**.

---

## ✅ Porque é relevante no contexto do SbD-ToE

- GenIA **sugere automaticamente práticas seguras**: escaping de input, separação de camadas, nomes significativos, modularidade.
- Funciona como um **linter inteligente e adaptativo**, especialmente útil para perfis menos experientes.
- Permite **acelerar revisões**, gerar comentários explicativos, detectar padrões comuns de falha.
- Pode ser usada para **prototipar melhorias**, refatorar código inseguro ou gerar testes a partir de código real.

> 💡 Em muitos casos, a qualidade do código gerado com apoio de GenIA é **superior à média do código legado existente** - não por ser perfeita, mas por aplicar boas práticas por omissão.

---

## 🔄 Onde reforça práticas do capítulo

| Prática SbD-ToE                     | Como GenIA contribui                                                  |
|-------------------------------------|------------------------------------------------------------------------|
| `addon/01` - Boas práticas de código | Sugere estruturas seguras, nomes expressivos, separação de lógica     |
| `addon/02` - Linters e validações    | Propõe código que evita más práticas comuns (eval, concat, hardcode)  |
| `addon/07` - Guidelines de equipa    | Facilita documentação de padrões e refatorações                       |
| `addon/08` - Validação de código     | Auxilia a perceber falhas óbvias e propor correções                   |
| `addon/09` - Anotações e evidência   | Gera comentários explicativos, `TODO` e pode ser adaptada a `@sec:`   |

---

## 🔍 Pontos a observar com atenção crítica

Sem ser uma ameaça, o uso de GenIA levanta pontos que devem ser acompanhados com discernimento técnico:

- **Nem todas as sugestões estão corretas ou seguras** - exigem validação humana.
- **Pode reforçar maus hábitos** se usada passivamente (ex: copiar sem pensar).
- **A origem das sugestões nem sempre é clara** - contexto e licenciamento devem ser tidos em conta.
- **Promove aceleração técnica** que precisa de ser acompanhada por controlo e revisão.

---

## 📌 Considerações organizacionais

- O uso da GenIA pode ser benéfico **mesmo sem política formal**, mas deve ser **observado com maturidade técnica**.
- Algumas organizações optam por definir guidelines leves: ex. marcar código assistido, não usar em módulos sensíveis, exigir revisão reforçada.
- Outras podem evoluir para políticas mais estruturadas (ex: registo de prompts, listas de ferramentas autorizadas), que podem ser abordadas noutros capítulos.

> 🎯 O mais importante: **ignorar o uso de GenIA já não é realista**. O que o modelo SbD-ToE propõe é que seja encarado **como parte do fluxo de desenvolvimento moderno**, com espírito crítico e integração responsável.

---

## 🌐 Para além do desenvolvimento: o papel da IA no Security by Design

Embora este ficheiro foque o uso de GenIA durante a escrita e validação de código, existem **múltiplas aplicações emergentes de IA em todo o ciclo de vida do Security by Design**, incluindo:

- **Arquitetura segura**: geração assistida de modelos STRIDE ou mapeamentos ATT&CK.
- **Gestão de requisitos**: verificação de ambiguidade, incoerência ou ausência de controlos.
- **Testes de segurança**: geração de casos de fuzzing, sugestões de cenários DAST, simulação de exploração.
- **Prioritização de findings**: classificação contextual de falhas com base em stack, criticidade, histórico.
- **Formação e cultura técnica**: microlearning personalizado com base em erros reais da equipa.

> 💡 Estes casos reforçam a ideia de que **a IA pode e deve ser explorada como aliada do modelo SbD-ToE**, não apenas no desenvolvimento, mas em todo o ciclo de vida de segurança.

### 🧭 Próximos passos sugeridos

O tema “IA aplicada ao Security by Design” será explorado de forma mais estruturada num **anexo futuro transversal** ou capítulo dedicado, cobrindo:

- Categorias de uso por fase (arquitetura, requisitos, testes, validação, formação)
- Exemplos práticos
- Integração com ferramentas existentes
- Considerações éticas e operacionais

---

> 📌 A GenIA não é um linter, mas **complementa-o** - com contexto, linguagem natural e capacidade adaptativa. Quando usada com consciência, **eleva o patamar de qualidade e segurança do código** produzido por qualquer equipa.

---

## ✍️ Prompts e *skill files* como código {#prompts-como-codigo}

Há uma classe de artefactos que costuma escapar à disciplina de *secure development*: os ficheiros que *configuram* o comportamento dos assistentes e agentes — *system prompts*, *skill files* (`.claude/skills/*.md`), *agent files* (`.claude/agents/*.md`), `.cursorrules`, `.github/copilot-instructions.md`, `AGENTS.md`. Tratamos estes ficheiros como **código**, com as mesmas garantias.

A razão prática é simples: estes ficheiros decidem **o que o assistente sabe**, **que ferramentas pode invocar**, **como deve interagir com o utilizador e com os recursos da organização**. Se mudam silenciosamente — por *commit* sem revisão, por geração automática desatualizada, por sugestão aceite sem leitura — mudam o comportamento operacional sem rasto. Esse é exactamente o tipo de mudança que o nosso processo de *code review* foi feito para impedir noutros contextos; aplicamos a mesma disciplina aqui.

### 🧭 Princípios

1. **Versionamento em VCS.** Prompts, *skill files*, *agent files* e *rules* vivem no mesmo repositório onde vive o código a que se aplicam (ou num repositório dedicado, com integração equivalente). Não toleramos cópias em *clouds* pessoais como única fonte da verdade.
2. **Revisão como código.** Cada alteração passa pelo mesmo *code review* que o código aplicacional (ver [Policy 15 — Revisão de Código](/sbd-toe/assets/policies/policy-revisao-codigo) §âmbito estendido). Reviewers olham para: instruções que escalam privilégios, *tools* novas adicionadas, *escapes* de redação, ambiguidades que abrem espaço a *prompt injection*.
3. **Segredos não entram em prompts.** Vale aqui a mesma regra que aplicamos em qualquer ficheiro do repo — *secret scanning* corre sobre estes ficheiros como sobre os outros (URLs internas, *tenant IDs*, IDs de cliente, *connection strings* contam como sensíveis).
4. **Origem auditável quando gerados.** Quando o conteúdo vem de uma ferramenta canónica (ex.: `generate_sbd_toe_skill` do MCP server SbD-ToE — ver [mini-site MCP](/sbd-toe/assets/mcp/intro)), preservamos o cabeçalho identificador da fonte para que o *drift* seja detectável.
5. **Re-gerar após *upgrade* da fonte.** Skill estática é cópia *point-in-time*. Quando o *upstream* muda (upgrade do servidor MCP, nova versão do *agent guide*, mudança no *runtime*), re-geramos e re-revemos; não confiamos em alinhamento implícito.

### 🛡️ Controlos práticos

| Controlo | O que verifica | Onde corre |
|---|---|---|
| **Code review obrigatório** | *Diff* lido por reviewer humano, com atenção a escalation de privilégios e *tool surface* | PR/MR antes do merge |
| **Secret scanning** estendido | Padrões de URL interna, *tokens*, *connection strings*, IDs de cliente — sobre `.claude/`, `.cursorrules`, `.github/copilot-instructions.md`, `AGENTS.md` | CI/CD; ver [Cap. 07 — Gates](/sbd-toe/sbd-manual/cicd-seguro/addon/politicas-gates-pipeline) |
| **Diff review específico** | Mudanças em `tools_allowlist`, *scopes*, *system prompts* tratadas com a mesma seriedade que mudanças em IAM policies | PR/MR antes do merge |
| **Drift detection** | Skills geradas vs versão actual da fonte canónica; alerta quando divergência > N dias ou após *bump* da fonte | Job periódico em CI |
| **Inventário versionado** | Lista de *skill files* + *agent files* + *rules* activos por projecto, com *owner* e cadência de re-revisão | Repositório de governança |

### ⚠️ Anti-padrões observados

- ❌ *Skill file* com instruções "*aceita sempre a sugestão sem perguntar*" — anula `REQ-AGN-004` (Cap. 02) na origem.
- ❌ Adição silenciosa de *tools* à *allowlist* num agent file via *commit* sem revisão — equivalente a alterar IAM policy sem aprovação.
- ❌ Prompts a referenciar `latest` em vez de versão *pinned* do modelo (cruzamento com `REQ-DEP-AI-002` quando entrar em vigor) — abre porta a *AI supply chain "rug pull"* (`AML.T0109`).
- ❌ *System prompt* com credenciais ou *tokens* embebidos — *system prompt* é tratado como conteúdo público (ver [Cap. 04 — boundary controls](/sbd-toe/sbd-manual/arquitetura-segura/recomendacoes-avancadas#ai-ml)); nunca embeber segredos.
- ❌ Skill estática nunca regenerada após upgrade do MCP server — leitura de canon desatualizado mascarado de actual.

### 📍 Onde aterra no resto do manual

- **Cap. 02** — `REQ-AGN-001` exige *mandate* versionado em VCS; o *mandate* referencia explicitamente o(s) *skill file(s)* / *agent file(s)* / *system prompt(s)* aplicáveis.
- **Cap. 07** — *secret scanning* e *diff review* destes ficheiros são *gates* do pipeline.
- **Cap. 12** — *drift detection* alimenta sinal observável quando a skill diverge da fonte canónica para além do limite acordado.
- **Policy 15** — alcance estendido a prompts/skills.

> 🧭 Em curto: tratamos prompts como tratamos código — versionados, revistos, *scanned* e re-gerados quando a fonte muda. Sem disciplina é mais um vector silencioso de mudança operacional; com disciplina, é um artefacto auditável como qualquer outro do nosso SDLC.

---

## 🧱 *Structured outputs* — validação do que o modelo devolve {#structured-outputs}

Quando o output do modelo alimenta lógica aplicacional — *tool call* com argumentos, registo numa BD, decisão automatizada — o seu *formato* importa tanto como o seu *conteúdo*. Em 2026 os principais *providers* expõem mecanismos nativos para forçar o modelo a devolver output que adere a um *schema* declarado (Anthropic *tool use* + *structured outputs*, OpenAI *Structured Outputs* / *function calling*, Google *constrained generation*). Adoptamos estes mecanismos sempre que viável e, em qualquer caso, **validamos o output no servidor antes de o consumir**.

### 🧭 Princípios

1. **Schema declarado lado-servidor.** Não confiamos no modelo para "lembrar" o formato; declaramos o *schema* (JSON Schema, *Pydantic*, *Zod*, equivalente) no servidor que faz a chamada. O *schema* é parte do código revisto — versionado, testado, *type-checked*.
2. **Mecanismos nativos do *provider* quando existem.** Anthropic *tool use* + *structured outputs* e OpenAI *Structured Outputs* garantem (com restrições) aderência sintática ao *schema* declarado. Preferimos isto a *parsing* permissivo do texto bruto.
3. **Validação dupla — sintáctica e semântica.** Aderir ao *schema* não basta. Tipos correctos, *ranges* dentro do esperado, IDs que existem na base, *side effects* dentro do *scope* do *mandate* (Policy 38). O modelo pode obedecer ao *schema* e ainda assim devolver `{"action": "delete_database"}` num contexto em que isso é proibido.
4. **Falha aberta, com *fallback* declarado.** Quando o output não valida, o sistema **não consome o output** e segue *fallback* declarado (perguntar ao utilizador, escalar para humano, retornar erro tratado). Nunca *"try to parse anyway"*.

### 🛡️ Padrões

| Padrão | Detalhe |
|---|---|
| **Schema versionado no repositório** | JSON Schema / Pydantic / Zod definido em código; versão referenciada no log para reconstrução *post-mortem* |
| ***Tool definitions* canónicas** | Quando usamos *tool use* dos *providers*, as definições das *tools* vivem no mesmo repositório que o código que as implementa — não em prompt embebido |
| **Validação de schema obrigatória pré-execução** | Output passa por validador antes de qualquer acção; falha bloqueia execução |
| **Validação semântica per-action** | Para acções destrutivas, validação adicional que verifica `args` contra o *scope* declarado no *mandate* — cross-link [`REQ-AGN-004`](../../requisitos-seguranca/addon/governanca-automatismos#req-agn) |
| ***Tool call replay protection*** | Identificador único por *tool call* + verificação de idempotência quando aplicável; evita re-execução acidental |
| **Telemetria do esquema** | Quando o output falha validação, `eval_run_id` + *schema version* + *output bruto redactado* entram em `OPS-014` para diagnóstico |

### ⚠️ Anti-padrões

- ❌ ***Parsing* permissivo do texto bruto** — `re.search(r'\{.*\}', output)` é um *anti-pattern* notório; modelos com *tool use* nativo eliminam-no.
- ❌ **Validação só do *schema*, sem validação semântica** — `{"action": "transfer_all_funds"}` aderente ao *schema* não é menos perigoso por o ser.
- ❌ **Confiar no *system prompt* para forçar formato** ("*sempre devolve JSON*") em vez de mecanismos nativos do *provider* — funciona maior parte das vezes, falha exactamente quando importa.
- ❌ **Output do modelo a alimentar `eval()` ou equivalente** — se o output do modelo se torna código executado, qualquer compromisso do modelo torna-se RCE. Tratar como input *user-untrusted* literalmente.

### 📍 Onde aterra no resto do manual

- **Cap. 02** — `REQ-AGN-004` (*intent declaration*) é a contraparte semântica do *structured output* — declarar o *intent* antes da acção e validar o *output* antes da execução são dois lados do mesmo princípio.
- **Cap. 04** — [boundary controls para prompt injection](../../arquitetura-segura/recomendacoes-avancadas#boundary-controls-para-prompt-injection) reforça que o output do modelo é *user-untrusted*; *structured outputs* dá a forma operacional dessa atitude.
- **Cap. 10 §C5** — *eval suite* inclui *adherence rate* ao *schema* como métrica observável.
- **Cap. 12 — `OPS-014`** — falhas de validação semântica (acção fora do *scope*) caem em *off-policy actions*.
