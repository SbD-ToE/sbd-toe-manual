---
id: guia-voz-prosa
title: Guia de Voz e Prosa — SbD-ToE
description: Norma de tom e voz para homogeneidade da prosa do manual — serious mas warm, 3ª pessoa, rigor científico
tags: [voz, tom, prosa, norma editorial, curadoria, autoria]
---

# Guia de Voz e Prosa — SbD-ToE

Esta norma define a **voz** do manual *Security by Design — Theory of Everything*: o tom, a forma de tratamento e o ritmo da prosa. Existe para garantir homogeneidade entre capítulos escritos em momentos e por mãos diferentes.

Complementa o [`guia-editorial.md`](guia-editorial.md), que cobre estrutura, ficheiros obrigatórios e estilo normativo (RFC 2119, templates, emojis por secção). Onde o guia editorial define **o quê** e **como estruturar**, esta norma define **como soa**. Em caso de conflito aparente, o guia editorial prevalece na estrutura; esta norma prevalece na prosa.

Está sujeita ao `AGENTS.md` e ao `PROGRAMME-PRESERVATION-PROTOCOL.md`. Nenhuma regra de voz autoriza alterar conteúdo canon fora de scope.

---

## 0. A fronteira: autor da prosa, não do conteúdo

A voz é uma propriedade da forma, não da substância. Quem escreve ou revê prosa neste manual é **autor da prosa, não do conteúdo**.

- Nada entra no manual sem certeza absoluta de que é tecnicamente correto e cientificamente defensável.
- Nada entra fora do *bounded context* do manual. A ausência de uma afirmação é preferível a uma afirmação plausível mas não verificada.
- Afinar voz nunca justifica acrescentar factos, métricas, nomes de ferramentas ou claims. Reescrever para soar melhor não pode introduzir conteúdo que não existia.
- Métricas, citações e referências normativas exigem fonte. Números confiantes sem âncora (por exemplo, "redução de 70-80%") são uma falha de rigor, não um reforço de prosa.

O rigor é o primeiro pilar. A voz serve a leitura; não a antecede.

---

## 1. O alvo: sério e caloroso, na terceira pessoa

O manual é técnico, mas escrito para **humanos lerem**. O alvo de voz tem três tensões mantidas em equilíbrio:

- **Sério e caloroso ao mesmo tempo.** Engenharia sem formalismo burocrático, mas sem familiaridade. A clareza é a forma de calor — não o tom coloquial.
- **Terceira pessoa, impessoal.** O calor vem da precisão e do cuidado com o leitor, nunca de o tratar por tu, de o incluir num "nós", ou de conversar com ele.
- **Direto, claro, objetivo.** Leitura de uma passagem, sem reler. Frase curta. Um conceito por parágrafo.

A calibração é mais fácil de ver por contraste:

| Frio demais (burocrático) | Alvo (sério + caloroso) | Familiar demais ("à vontadinha") |
| --- | --- | --- |
| "A não implementação do controlo constitui não conformidade passível de sanção." | "Um controlo que não corre não protege. A sua ausência deve ser tratada como risco, não como detalhe." | "Convém mesmo não te esqueceres deste controlo, senão é chatice à frente." |
| "Proceder-se-á à validação anteriormente à operação de implantação." | "A validação deve ocorrer antes do deploy." | "Valida antes de fazeres deploy, ok?" |

O ponto central da coluna do meio: afirma com confiança, explica o porquê com economia, respeita o tempo do leitor. Não pratica abuso de confiança com o interlocutor.

---

## 2. Disciplina de pessoa

Esta é a regra mais mecânica e a mais violada. Vale para toda a prosa (`intro.md`, `recomendacoes-avancadas.md`, `aplicacao-lifecycle.md`, `addon/`), com a única exceção explícita de exemplos narrativos onde o guia editorial já o permite.

**Terceira pessoa impessoal. Sem primeira pessoa do plural. Sem segunda pessoa.**

O "tu" nunca é usado, sem exceção. Os casos que existem hoje no manual estão errados e são defeitos a corrigir, não precedentes a seguir.

| Evitar | Usar |
| --- | --- |
| "Trabalhamos com IDs MITRE ATLAS." | "O modelo usa os IDs MITRE ATLAS." |
| "Operacionalizamos os requisitos `DEP-011`." | "Esta secção operacionaliza os requisitos `DEP-011`." / "Os requisitos `DEP-011` são operacionalizados aqui." |
| "Nos últimos meses passámos a viver com uma classe diferente de ferramenta." | "Surgiu uma classe diferente de ferramenta." |
| "Ignorá-la é confiar cegamente em código fora do **teu** controlo." | "Ignorá-la é confiar em código executado fora do controlo da organização." |
| "Classifica o risco da aplicação e seleciona os testes." | "O risco da aplicação deve ser classificado, e os testes selecionados em função dele." |

### 2.1. O `se` impessoal — usar corretamente

Uma passagem anterior de despersonalização converteu "nós" em construções reflexivas mecanicamente, e algumas ficaram **agramaticais**. A correção não é trocar "nós" por "se" no mesmo lugar; é reconstruir a frase.

| Errado (agramatical) | Correto |
| --- | --- |
| "trata-se prompts como trata-se código" | "os prompts devem ser tratados como código" / "trata-se o prompt como se trata o código" |
| "Adopta-se estes mecanismos." | "Estes mecanismos devem ser adotados." / "Adotam-se estes mecanismos." |
| "Porque trata-se a inferência self-hosted como caso próprio" | "Porque a inferência self-hosted é tratada como caso próprio" |

Com pronome enclítico, o verbo concorda com o sujeito ("adotam-se os mecanismos", plural). Quando a frase fica pesada, a voz passiva normativa com "deve" é quase sempre mais limpa.

---

## 3. Marcas de geração automática a eliminar

O manual não deve carregar *tell-signs* de texto gerado. Estas marcas removem-se sempre que aparecem:

- **Aberturas ocas:** "Num mundo cada vez mais...", "Na era digital...".
- **Preâmbulos de ênfase vazios:** "É importante notar que", "Vale a pena mencionar", "De salientar que". Se é importante, afirma-se diretamente.
- **Conclusões ocas e promocionais:** "A abordagem é escalável e replicável noutras organizações", "Ao seguir estes passos...", "Em última análise...". Uma conclusão acrescenta algo ou não existe (ver §5).
- **Slogans e aforismos motivacionais:** "a segurança vive-se e respira", "não nasce com um documento, nasce com o exemplo", "desenhar com consciência é desenhar seguro". Espelhamento retórico (X não é A, é B) usado como ornamento.
- **Encadeamento mecânico:** "Além disso / Adicionalmente / Por outro lado" a ligar bullets sem argumento real entre eles.
- **Padding de tríade:** listas de três itens construídas pelo ritmo, não pela substância ("garantir, reduzir, suportar").
- **Hedge empilhado:** "pode eventualmente, em certos casos, dependendo do contexto, ser por vezes...".
- **Plugs de fornecedores como enchimento:** listas de nomes de ferramentas (Checkmarx / Snyk / Kiuwan ...) que não acrescentam decisão.

Algum tecido conjuntivo é necessário, e é desejado. O manual é prosa contínua, para humanos lerem e máquinas processarem — não uma bullet list seca, nem uma peça literária. Frases de ligação que dão ritmo, contexto ou transição têm função e devem existir; é o que separa um manual legível de um inventário.

O alvo é o **oco**, não toda a palavra apagável. O teste: a frase serve o ritmo, o contexto ou a transição? Fica. Apenas decora — slogan, conclusão que repete, ênfase vazia, tríade construída pelo som? Sai.

---

## 4. Emoji e títulos

O guia editorial permite emojis por secção (🛠️, 📅, 👥, …) como rótulos estruturais. Esta norma restringe o **excesso**, que é uma marca de blog, não de manual:

- Emoji como **rótulo de secção** (conforme tabela do guia editorial): aceitável.
- Emoji como **emoção ou ênfase** (🌟, 🏁, 🚀 em títulos genéricos como "🌟 Objetivo", "🏁 Conclusão"): remover.
- O aside **"👉"** a apontar para uma nota ao leitor: remover. Quebra o registo impessoal.
- Maiúsculas de alarme ("NÃO PODE", "CRÍTICO") como recurso de ênfase: usar o normativo ("não deve") em vez de gritar.

---

## 5. Disciplina de conclusão

Uma secção de fecho só existe se acrescentar. Restating do que já foi dito, com tríade e aforismo, é a forma mais comum de enchimento no manual.

- Fecho **bom:** uma consequência, um limite, ou uma decisão que ainda não tinha sido tornada explícita. Exemplo do corpus: *"A ausência de registo de change de emergência ou de notificação ao CISO invalida o emergency deploy como excepção — passa a ser um deploy não autorizado."*
- Fecho **a evitar:** *"A maturidade não depende apenas da ferramenta, mas da capacidade de tomar decisões seguras, justificadas e auditáveis."* — verdadeiro, mas não acrescenta nada ao que o capítulo já estabeleceu.

---

## 6. Correção de língua (PT-PT)

O rigor técnico estende-se à língua. Estes defeitos, todos observados no corpus, contam como falhas de qualidade:

- **Erros ortográficos:** "Governaça" (governança), "Manteído" (mantido), "integraidade" (integridade), "alarmistica" (alarmística), "ferrameta" (ferramenta).
- **Termos técnicos reconhecidos usam-se em inglês por omissão** — não são estrangeirismos, são o vocabulário do domínio: SBOM, pipeline, deploy, rollback, threat model, kill-switch, feature flag, container, hardening, fuzzing. Traduzi-los à força (por exemplo, "trilho de implantação" por *deploy*) prejudica a clareza e o processamento por máquina. O termo inglês reconhecido é a forma correta, não uma falha.
- **Traduz-se apenas prosa inglesa casual** que não é termo técnico e tem equivalente português corrente: "wasted effort" → esforço desperdiçado; "auditable trail" → trilho auditável. O teste: é vocabulário estabelecido do domínio, ou inglês solto a infiltrar-se na frase? Se é vocabulário do domínio, fica em inglês.
- **Brasileirismos:** "Em uma frase" → "Numa frase"; "time" → "equipa".
- **Frases truncadas ou corrompidas:** texto que termina a meio ("...list"), headers com encoding partido. Qualquer um destes invalida a passagem.

---

## 7. Corpus de referência

A voz alvo não é uma abstração — já existe em ficheiros concretos do manual. Estes substituem o antigo `.stylometry/baseline/` (que servia para um teste de autoria humana-vs-IA, hoje irrelevante) como referência viva.

**Escrever na direção destes (exemplares — leitura impessoal, prescritiva, sem decoração):**

- `000-teory-of-everything/intro.mdx`
- A família `excecoes-*`: `14/addon/12-processo-excecoes.md`, `11/addon/09-excecoes-deploy.md`, `12/addon/10-excecoes-operacoes.md`, `05/addon/09-excecoes-e-aceitacao-risco.md`
- A família `kpis-metricas`: `14/kpis-governanca.md`, `03/addon/11-kpis-metricas.md`, `12/addon/11-kpis-metricas.md`
- `03/addon/02-riscos-processo-threat-modeling.md`, `04/addon/09-decisao-evidencia-arquitetural.md`
- `10/addon/10-evidencia-reprodutibilidade.md`, `10/addon/14-tlpt-readiness.md`
- Os `intro.md` dos capítulos `06`, `07`, `08`, `09`
- `01/addon/10-atributos-risco.md`, `02/addon/03-taxonomia-rastreabilidade.md`

**Reescrever para o alvo (mais distantes, por ordem de prioridade):**

1. `achievable-maturity.md` (todos os capítulos) — provenance de máquina, não prosa humana. Se forem expostos a leitores, devem ser reescritos como prosa; caso contrário, ficam fora desta norma.
2. `recomendacoes-avancadas.md` (01, 02, 08, 10, 11) — inventários de bullets com conclusões ocas.
3. Capítulo `13` addons `01`–`05` (`trilho-formativo`, `programa-champions`, `catalogo-formativo`, `tecnicas-formativas`, `integracao-transversal`) — registo motivacional.
4. Secções agênticas/IA recentes: `04/recomendacoes-avancadas.md`, `06/addon/10-genia-e-seguranca.md`, `09/addon/12-self-hosted-inference.md`, `10/addon/13-ia-nos-testes.md`, `03/addon/01-metodologias-e-ferramentas.md` — primeira pessoa do plural e `se` impessoal partido.

---

## 8. Verificação antes de shippar prosa

Antes de dar uma passagem por terminada:

- [ ] Sem primeira pessoa do plural ("nós") e sem segunda pessoa ("tu/você"), exceto exemplo narrativo autorizado.
- [ ] Construções com `se` impessoal estão gramaticais (concordância com o sujeito).
- [ ] Nenhuma frase pode ser apagada sem perda de informação (sem enchimento, sem slogan, sem conclusão oca).
- [ ] Emoji só como rótulo de secção, nunca como emoção; sem "👉" ao leitor.
- [ ] Cada métrica, citação e referência normativa tem fonte.
- [ ] Sem erros de PT-PT, sem inglês infiltrado evitável, sem frase truncada.
- [ ] Nada acrescentado fora do *bounded context* nem sem certeza de correção.
