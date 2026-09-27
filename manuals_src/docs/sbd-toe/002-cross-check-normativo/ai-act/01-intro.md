---
id: intro
title: AI Act - Cross-Check Normativo
description: Análise de como o SbD-ToE responde às obrigações do Regulamento (UE) 2024/1689 (AI Act) - cibersegurança, registo de eventos, supervisão humana, transparência, acompanhamento pós-comercialização e incidentes graves de sistemas de IA, com a exatidão e a solidez pendentes de uma ronda futura
tags: [cross-check, ai-act, regulamento-ia, ia, machine-learning, robustez, ciberseguranca, gpai]
sidebar_position: 6
---

# AI Act: Cross-Check Normativo

> Para implementação prática, consulte o [Playbook SbD-ToE 4 AI Act](/sbd-toe/cross-check-normativo/ai-act/playbook).
>
> Para padrões aplicacionais universais, ver capítulos base do SbD-ToE (01–14).
>
> A resposta do Manual a cada obrigação (coberta, lacuna declarada ou fora de âmbito) está resumida em [«O que este Manual cobre e o que fica de fora»](#o-que-este-manual-cobre-e-o-que-fica-de-fora) e listada, obrigação a obrigação, em [Requisitos aplicáveis](./requisitos-aplicaveis#cobertura).

## Âmbito {#âmbito}

### 🤖 AI Act - Regulamento de Inteligência Artificial {#-ai-act---regulamento-de-inteligência-artificial}

O **AI Act** é o **Regulamento (UE) 2024/1689** (CELEX: [32024R1689](https://eur-lex.europa.eu/legal-content/PT/TXT/?uri=CELEX:32024R1689)), o primeiro quadro jurídico horizontal do mundo dedicado à inteligência artificial. Entrou em vigor a 1 de agosto de 2024 e aplica-se de forma faseada:

- **2 de fevereiro de 2025** - práticas proibidas (Art. 5) e literacia no domínio da IA (Art. 4; desde 27 de julho de 2026, na redacção dada pelo Reg. (UE) 2026/1744). Excetuam-se as novas proibições do art. 5.º, n.º 1, primeiro parágrafo, alíneas b-A) e b-B), e os n.ºs 1-A e 1-B do mesmo artigo, aditados pelo Reg. (UE) 2026/1744, que se aplicam a partir de **2 de dezembro de 2026** (art. 113.º, terceiro parágrafo, alínea a)).
- **2 de agosto de 2025** - modelos de IA de finalidade geral (GPAI, Capítulo V), autoridades notificadoras e organismos notificados (Capítulo III, secção 4), governação (Capítulo VII) e sanções (Capítulo XII), **com exceção do art. 101.º** (coimas aplicáveis aos prestadores de modelos de IA de finalidade geral).
- **2 de agosto de 2026** - aplicação geral do regulamento (art. 113.º, segundo parágrafo), incluindo as obrigações de transparência do Art. 50 e o art. 101.º; para sistemas que geram conteúdos sintéticos colocados no mercado antes desta data, o art. 50.º, n.º 2, deve ser cumprido até 2 de dezembro de 2026 (art. 111.º, n.º 4).
- **2 de dezembro de 2027** - capítulo III, secções 1 a 3 (com exceção do art. 6.º, n.º 5), para sistemas de IA de **risco elevado** do Anexo III (Reg. (UE) 2026/1744, que alterou o art. 113.º).
- **2 de agosto de 2028** - sistemas de IA de risco elevado abrangidos pela legislação de produto do Anexo I (Reg. (UE) 2026/1744).

> ℹ️ **Nota (2026):** O Regulamento (UE) 2026/1744 («Regulamento Omnibus Digital em matéria de IA»), publicado no JO L de 24.7.2026 e em vigor desde 27.7.2026, alterou o art. 113.º: as obrigações de alto risco (cap. III, secções 1–3) aplicam-se a partir de **2 de dezembro de 2027** (Anexo III / art. 6.º, n.º 2) e de **2 de agosto de 2028** (Anexo I / art. 6.º, n.º 1).

O AI Act adota uma **abordagem baseada no risco**, com quatro patamares: risco **inaceitável** (proibido, Art. 5), **risco elevado** (Art. 6 e Anexos I/III, sujeito ao grosso das obrigações técnicas), risco **limitado** (designação corrente; o Art. 50 fixa obrigações de transparência para «determinados sistemas de inteligência artificial») e risco **mínimo** (sem obrigações específicas além das horizontais, como a literacia do Art. 4). Sobre estes patamares incidem ainda regras próprias para **GPAI** (Art. 53) e GPAI com **risco sistémico** (Art. 55).

É essencial enquadrar a natureza do regulamento: o AI Act é, antes de tudo, **legislação de segurança de produto e de proteção de direitos fundamentais** aplicada a sistemas de IA, não uma norma de segurança aplicacional (AppSec). Contudo, as obrigações para sistemas de IA de risco elevado incorporam **requisitos técnicos substanciais** que cruzam diretamente com o SbD-ToE - em particular:

- **Art. 12 / Art. 19** - registo automático de eventos (logging) e conservação de logs;
- **Art. 14** - supervisão humana;
- **Art. 15** - **cibersegurança** (incluindo resistência a ataques antagónicos); a exatidão e a solidez do mesmo artigo estão pendentes de uma ronda futura;
- **Art. 50** - transparência para determinados sistemas de IA;
- **Art. 72** - acompanhamento pós-comercialização;
- **Art. 73** - comunicação de incidentes graves.

Os arts. 9.º (sistema de gestão de riscos) e 17.º (sistema de gestão da qualidade) ficam fora do âmbito do Manual: são sistemas de gestão da organização, não requisitos da aplicação. Os controlos do Manual servem-lhes de evidência.

No SbD-ToE, o AI Act é operacionalizado através das mesmas disciplinas técnicas que sustentam qualquer software seguro - engenharia segura (requisitos, arquitetura, desenvolvimento, IaC, pipelines, testes), cadeia de fornecimento e proveniência (dependências, containers, SBOM), processos de monitorização e resposta, e governação/contratação - aplicadas agora ao **ciclo de vida de sistemas de IA** (datasets, modelos, pipelines de treino e inferência, serviços de inferência).

> ⚖️ **Nota editorial.**
> Esta secção é uma **síntese operacional** dos artigos relevantes do AI Act, não uma citação literal do regulamento.
> Baseia-se, em particular, nos Artigos 9.º (gestão de risco), 10.º (dados e governação de dados), 11.º e Anexo IV (documentação técnica), 12.º e 19.º (registos/logs), 13.º–14.º (transparência e supervisão humana), 15.º (exatidão, solidez, cibersegurança), 17.º (QMS), 72.º (acompanhamento pós-comercialização), 73.º (incidentes graves) e 53.º/55.º (GPAI e risco sistémico).

> ⚖️ **Nota sobre referências técnicas.**
> O AI Act estabelece requisitos essenciais mas remete o detalhe técnico para **normas harmonizadas** (a desenvolver pelo CEN-CENELEC) e especificações comuns.
> Padrões como **ISO/IEC 42001** (sistema de gestão de IA), **ISO/IEC 23894** (gestão de risco de IA), **ISO/IEC 27090** (segurança de IA, em desenvolvimento), o **NIST AI Risk Management Framework (AI RMF 1.0)**, o **MITRE ATLAS** (táticas e técnicas adversariais contra ML), o **OWASP Machine Learning Security Top 10** e o **OWASP Top 10 for LLM Applications** são amplamente reconhecidos e fornecem base sólida para cumprir os requisitos técnicos e processuais.
> O SbD-ToE assume estes padrões como **boas práticas recomendadas**, não como requisitos legais em si mesmos.

## Aviso Regulatório {#aviso-regulatório}

O SbD-ToE cobre o **"como" técnico** de boa parte das obrigações de risco elevado, mas **não substitui** as dimensões jurídicas e de avaliação de conformidade do AI Act. Nas matérias que mais se confundem, a resposta é esta:

- **Classificação de risco** (Art. 6 e Anexos I/III): a determinação jurídica de se um sistema é de risco elevado é de compliance. O resultado declara-se por aplicação como contexto CTX-AIA-RE, com a qualificação jurídica anexada, e os pisos desse contexto aplicam-se em qualquer nível L1–L3. O nível L3 do Manual não equivale a risco elevado.
- **Governação de dados de treino, validação e teste** (Art. 10): representatividade, deteção e mitigação de enviesamento (*bias*) e qualidade estatística dos conjuntos de dados ficam **fora de âmbito**, por decisão do programa: são trabalho de ciência de dados. A proveniência e a integridade dos conjuntos de dados (`DEP-011`) dão-lhes evidência incidental.
- **Transparência** (Arts. 13 e 50): o Art. 50 está **coberto** por dois requisitos do regime (CTX-AIA-RE-R01 e R02). Para as instruções de utilização do Art. 13, o Manual fornece evidência, e a redacção é do prestador. Fica fora de âmbito a divulgação de texto gerado por IA publicado sobre matérias de interesse público (art. 50.º, n.º 4, segundo parágrafo): é decisão editorial, não de engenharia.
- **Supervisão humana** (Art. 14): os n.os 1 a 4 estão **cobertos** para qualquer sistema de risco elevado, com ou sem agentes, pelo `ARC-014` com o piso CTX-AIA-RE-P08. Ficam fora de âmbito as especificidades dos **sistemas de identificação biométrica** (anexo III, ponto 1): os registos do art. 12.º, n.º 3, e a verificação por duas pessoas do art. 14.º, n.º 5. Uma aplicação desse tipo desenvolve-se com o Manual como qualquer outra, e a biometria como factor de autenticação está no `AUT-012`.
- **Avaliação de impacto sobre os direitos fundamentais (FRIA)** (Art. 27): obrigação de certos responsáveis pela implantação (*deployers*): organismos de direito público, entidades privadas que prestam serviços públicos e responsáveis pela implantação dos sistemas do anexo III, ponto 5, alíneas b) e c), para sistemas de risco elevado do art. 6.º, n.º 2 (com exceção dos do anexo III, ponto 2) (art. 27.º, n.º 1). A FRIA é do responsável pela implantação; o threat model do Cap. 03 (incluindo o LINDDUN) fornece-lhe evidência. Fica fora de âmbito apenas a comunicação do resultado à autoridade (art. 27.º, n.º 3).
- **Avaliação de conformidade** (Art. 43), envolvimento de **organismos notificados**, **declaração UE de conformidade** (Art. 47), **marcação CE** (Art. 48) e **registo na base de dados da UE** (Art. 49/71): fora de âmbito.
- **Determinação de práticas proibidas** (Art. 5) e qualificação jurídica de papéis (prestador, responsável pela implantação, importador, distribuidor): fora de âmbito. As salvaguardas técnicas que o art. 5.º, n.º 1-A, exige a geradores de imagem, vídeo ou áudio realistas estão **cobertas** (pisos CTX-AIA-RE-P09 e P10).

O juízo jurídico nestas matérias é das equipas de compliance e jurídico e da relação com a autoridade competente. O SbD-ToE fornece os controlos técnicos e a evidência; não emite o juízo de conformidade.

## O que este Manual cobre e o que fica de fora {#o-que-este-manual-cobre-e-o-que-fica-de-fora}

O SbD-ToE é centrado na aplicação: requisitos, arquitetura, código, dependências, pipeline, deploy e operação do software. Para cada obrigação do AI Act, o Manual responde numa de três categorias, e nenhuma obrigação fica em silêncio:

- **Cobre**, e diz de que forma: requisito do catálogo, política, piso ou requisito acrescentado pelo regime, ou evidência de engenharia para um dever de outro plano.
- **Lacuna declarada**: o que o Manual não cobre por omissão, com o que falta.
- **Fora de âmbito**: o que o Manual não trata, com a razão.

A lista completa, obrigação a obrigação, é gerada da matriz de cobertura e está em [Requisitos aplicáveis — O que este Manual cobre e o que fica de fora](./requisitos-aplicaveis#cobertura). Quando esta página e a lista divergirem, prevalece a lista.

**Fora de âmbito, por decisão do programa:**
- Segurança da entidade como um todo (rede corporativa e canais de administração, EDR, patching de sistemas operativos e equipamentos, inventário e classificação de todos os ativos): o Manual é centrado na aplicação.
- Sistema de gestão de riscos (art. 9.º) e sistema de gestão da qualidade (art. 17.º): são sistemas de gestão da organização; os controlos do Manual servem-lhes de evidência.
- Governação de dados de treino e avaliação de enviesamento (art. 10.º): é trabalho de ciência de dados; a proveniência e a integridade dos conjuntos de dados (`DEP-011`) dão só evidência incidental.
- Avaliação da conformidade e redacção da declaração de conformidade: pertencem ao plano da conformidade do produto, a cargo do prestador.
- Especificidades dos sistemas de identificação biométrica (registos do art. 12.º, n.º 3, e verificação por duas pessoas do art. 14.º, n.º 5): a aplicação desenvolve-se com o Manual como qualquer outra, e a biometria como factor de autenticação está no `AUT-012`.

Lacuna declarada pendente da ronda AISVS/SAIF do AppSec Core: exatidão e solidez (art. 15.º). A documentação técnica (anexo IV) tem [mapa de evidência](./requisitos-aplicaveis#mapa-evidencia) na página gerada. A IA entra como qualquer outro tema; não há um manual de IA à parte.

---

## Matriz de Cross-Check (resumo) {#matriz-de-cross-check-resumo}

> ✏️ **Revisão 2026-09-27.** Esta tabela resume a matriz de cobertura do AI Act (`_matriz/aiact.yaml`), que incorpora o *release agentic* (Cap. 02 §A0–A4, Cap. 03 playbook agentic, [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015), `DEP-012..014`, `OPS-012..014`, Policy 38, Policy 39) e os pisos e requisitos do contexto CTX-AIA-RE. A coluna «Lacuna residual» só regista lacunas declaradas; o que fica fora de âmbito é assinalado como tal. A resposta obrigação a obrigação está em [Requisitos aplicáveis](./requisitos-aplicaveis#cobertura).

| Domínio AI Act | Referência (artigo) | Cobertura SbD-ToE | Lacuna residual | Ação de adaptação |
|---|---|---|---|---|
| Literacia no domínio da IA | Art. 4 | Cap. 13 (formação), Policy 37 §11 (matriz por *role*) | Parcial: pessoal de negócio que opera ou utiliza sistemas de IA de produto; ponderação do contexto de utilização e das pessoas visadas | Documentar conclusões dos trilhos formativos como evidência |
| Categorias especiais de dados para corrigir enviesamento | Art. 4.º-A | `ENC-002`, `PRI-001`, `ACC-001..003`, `LOG-001`, `PRI-002`, `PRI-004` | Parcial: limitação da reutilização e pseudonimização destes conjuntos; documentação por acesso; proibição geral de transmissão a terceiros; apagamento logo que o enviesamento seja corrigido; fundamentação da estrita necessidade | O juízo de necessidade (n.º 1, al. a)) fica fora de âmbito |
| Sistema de gestão de risco | Art. 9 | Fora de âmbito (decisão do programa): sistema de gestão da organização | — | Os artefactos dos Cap. 01, 03 e 12 servem de evidência |
| Dados e governação de dados | Art. 10 | Fora de âmbito (decisão do programa): governação de dados de treino e enviesamento | — | [`DEP-011`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-011) e [`DEP-012`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-012) dão evidência incidental de proveniência |
| Documentação técnica | Art. 11, Anexo IV | Cap. 02, Cap. 04 (arquitetura + [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015)), Cap. 05 ([`DEP-012`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-012) AI BOM), Cap. 06, Policy 38 (mandate) | Lacunas declaradas por ponto do Anexo IV (ver o [mapa de evidência](./requisitos-aplicaveis#mapa-evidencia)); adequação das métricas de desempenho (ponto 4) pendente da ronda AISVS/SAIF | Mapear artefactos SbD-ToE (incluindo mandate + AI BOM) para o índice do Anexo IV; a redacção é do prestador |
| Registo de eventos (logging) | Art. 12, Art. 19 | Cap. 12 (observabilidade), [`OPS-011`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes) (AI/ML), [`OPS-012`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-012) (audit per *tool invocation* com `mandate_ref`), Cap. 12 US-13 (telemetria agentic), Policy 30 §9 | — (esquema do *model output* configurável por sistema, com os mínimos dos pisos CTX-AIA-RE-P01 a P03 e P11; registos da identificação biométrica, art. 12.º, n.º 3: fora de âmbito) | Documentar esquema de inferência por sistema |
| Transparência aos deployers | Art. 13 | Cap. 02, Cap. 04 (parcial), Policy 38 (mandate como fonte estruturada de *capabilities*, limitações e supervisão) | Níveis de exatidão e solidez nas instruções: lacuna declarada, pendente da ronda AISVS/SAIF do AppSec Core; finalidade prevista e descrição da interface | Derivar "instruções de utilização" a partir do mandate + artefactos Cap. 04/06; a redacção é do prestador |
| Supervisão humana | Art. 14 ⚡ | [`ARC-014`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-014) com o piso CTX-AIA-RE-P08 (qualquer sistema de risco elevado); para agentes, Cap. 02 §A0–A4 + `REQ-AGN-001..004` (mandate, classificação de nível, *kill-switch*, *intent declaration*), Cap. 04 [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015) (OOB approval + *kill-switch* arquitectónico), Policy 38 (ciclo de vida do mandate) | — (art. 14.º, n.º 5, identificação biométrica: fora de âmbito) | Interface de supervisão em qualquer sistema de risco elevado (a UX concreta é do produto); *kill-switch*, *intent declaration* e OOB approval nos agentes |
| Exatidão, solidez e cibersegurança | Art. 15 | Cap. 03 playbook agentic + MITRE ATLAS, Cap. 04 ([`ARC-014`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-014)+[`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015)), Cap. 05 (AI BOM), Cap. 10 §C5 (*eval suites*), Cap. 12 + [`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014) (*jailbreak* / *off-policy*) | Exatidão e solidez: lacuna declarada, pendente da ronda AISVS/SAIF do AppSec Core; redundância e mitigação de enviesamento em circuitos de realimentação (art. 15.º, n.º 4, parcial) | Aguardar a ronda; até lá, registar as métricas obtidas como evidência, sem as apresentar como cumprimento |
| Sistema de gestão da qualidade | Art. 17 | Fora de âmbito (decisão do programa): sistema de gestão da organização | — | Os gates (Cap. 06, 07, 11, 14) e as Policies 38/39 servem de evidência |
| Cadeia de fornecimento | Art. 25 | [`DEP-013`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-013) (*pinning*), [`DEP-014`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-014) (lista de fornecedores de serviços de IA aprovados), Policy 39, Cap. 14 US-21 | Parcial: o acordo escrito não especifica informação, capacidades, acesso técnico e assistência (art. 25.º, n.º 4) | Rever as cláusulas da Policy 33 §10 com o jurídico |
| Obrigações do *deployer* | Art. 26 | Policy 38 (mandate + ownership), Cap. 02 §A0–A4, Cap. 12 US-13 (logs sob controlo do *deployer*) | Operação conforme as instruções do prestador em sistemas adquiridos; supervisores de sistemas não agênticos; pertinência e representatividade dos dados de entrada; informação ao prestador e suspensão de sistemas não agênticos | Estender mandate com obrigações específicas quando organização é *deployer* |
| Conformidade e marcação CE | Art. 43, 47–49 | — (DEP-014 regista a conformidade declarada contratualmente pelo fornecedor de serviços de IA; não é a declaração UE de conformidade do Art. 47 nem substitui a avaliação de conformidade e a marcação CE a cargo do prestador do sistema) | — (fora de âmbito: plano da conformidade, a cargo do prestador) | Estabelecer swimlane GRC + jurídico para o circuito de avaliação |
| GPAI e risco sistémico | Art. 53, Art. 55 | Cap. 03 playbook + Cap. 05 (AI BOM), Cap. 10 §C5 (*eval suites* + *red teaming*), Cap. 12 US-13 + [`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014), Policy 19 §7, Policy 30 §9 | Parcial: avaliação do modelo com protocolos normalizados e testagem antagónica documentada (art. 55.º, n.º 1, al. a)) | Anexos XI/XII redigidos pelo prestador do modelo, com evidência do Manual; política de *copyright* e resumo dos dados de treino fora de âmbito (plano jurídico) |
| Acompanhamento pós-comercialização | Art. 72 | Cap. 12 (monitorização, *drift*), `OPS-011..014`, Cap. 12 US-13 + plano por sistema ([CTX-AIA-RE-R04](./requisitos-aplicaveis#acrescentos), integrado no anexo IV, ponto 9) | — | Aplicar o R04 quando a organização é o prestador |
| Incidentes graves | Art. 73 | Cap. 12, Cap. 14, [`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014) (*off-policy* → IR), Policy 30 §9.3, Policy 16 §11.4 (incidentes agentic-específicos), Política 32 §4.1 e [Política 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória) (definição e prazos) | Parcial: não alterar o sistema de forma que afecte a análise de causas sem informar previamente a autoridade (art. 73.º, n.º 6) | Configurar exportadores SIEM/ITSM para a notificação |
| Salvaguardas de geradores de conteúdo realista | Art. 5.º, n.º 1-A | `THR-008` e `ARC-014` com os pisos CTX-AIA-RE-P09 e P10 (grau ART50) | — (fora de âmbito: juízo de admissibilidade da finalidade, art. 5.º) | Threat model do conteúdo gerado, red-team e filtros de entrada e de saída |
| Transparência para determinados sistemas de IA | Art. 50 | CTX-AIA-RE-R01 (informar) e R02 (marcar conteúdo sintético), grau ART50 | — (fora de âmbito: texto de interesse público, art. 50.º, n.º 4, segundo parágrafo) | Declarar o grau ART50 na aplicação e verificar o aviso e a marcação em teste |
| Modificação substancial | Art. 43.º, n.º 4; anexo IV, ponto 2, al. f) | `ARC-009` com o piso CTX-AIA-RE-P11 | — | Classificar e registar cada alteração; sinalizar a modificação substancial |
| Explicação às pessoas afectadas | Art. 26.º, n.º 11; Art. 86 | CTX-AIA-RE-R03 + `OPS-011` | — | Registar, por decisão, o resultado e os principais elementos que o determinaram |
| Medidas corretivas e dever de informação | Art. 20 | `DPL-005` (rollback), Política 32 | Parcial: retirada ou recolha do sistema; informação a distribuidores, implantadores, mandatário e importadores; investigação conjunta com o implantador | — |
| Conservação da documentação | Art. 16, al. d); Art. 18 | Política 06 §10 | Parcial: sem prazo de 10 anos para a documentação de sistemas de IA de risco elevado | — |

---

## PARTE I: ANÁLISE NORMATIVA {#parte-i-análise-normativa}

### Artigo 4 - Literacia no domínio da IA {#artigo-4---literacia-em-ia}

**Conteúdo normativo**

O Art. 4, na redacção do Reg. (UE) 2026/1744 (em vigor desde 27 de julho de 2026), dispõe: «Os prestadores e responsáveis pela implantação de sistemas de IA adotam medidas para promover a literacia no domínio da IA do seu pessoal e de outras pessoas envolvidas na operação e utilização de sistemas de IA em seu nome, tendo em conta os seus conhecimentos técnicos, experiência, educação e formação e o contexto em que os sistemas de IA serão utilizados, bem como as pessoas ou grupos de pessoas visadas por essa utilização. Esta obrigação não exige que os prestadores ou responsáveis pela implantação garantam que as pessoas atinjam qualquer nível específico de literacia no domínio da IA.» (art. 4.º, n.º 1). Na leitura do Manual, trata-se de uma obrigação de meios. Entre 2 de fevereiro de 2025 e 26 de julho de 2026 vigorou a redacção original, que exigia medidas para garantir, «na medida do possível», um «nível suficiente de literacia no domínio da IA».

**Cobertura SbD-ToE**

| Requisito AI Act | Capítulo SbD-ToE | Cobertura |
|---|---|---|
| Formação proporcional por papel | Cap. 13 + Policy 37 §11 | Matriz de cobertura por *role* (developer, appsec, devops, grc, tech lead, PO/SM, CISO) + exercícios práticos |
| Atualização periódica | Policy 37 §11 | Cadências: onboarding + actualização anual ou semestral conforme *role* |
| Trilhos para uso assistido vs autónomo | Cap. 13 (addon 12) + Policy 16 + Policy 38 | Diferenciação entre uso assistido (A0–A1) e operação autónoma (A2+) |

**O que o SbD-ToE cobre**

- **Matriz de cobertura formativa por *role*** (Policy 37 §11) — define conteúdos mínimos, cadência e exercícios práticos por papel.
- **Distinção entre uso assistido e autónomo** — quem opera agentes A2+ tem trilho formativo específico (modelo A0–A4, `REQ-AGN-*`, *kill-switch*, OOB approval), além do trilho de uso assistido.
- **Exercícios práticos** — *tabletops* de *off-policy action*, *red team* contra agente em sandbox, exercício de classificação de *mandate* (Policy 37 §11.2).
- **Activação automática** — quando a organização adopta agentes AI em A1+, o módulo agentic da Policy 37 §11 passa a ser **obrigatório** (em vez de recomendado).

**Lacuna declarada (parcial)**

O Manual cobre os papéis técnicos do SDLC e o uso de IA como ferramenta ou agente, mas não o pessoal de negócio que opera ou utiliza sistemas de IA de produto em nome da organização, nem a ponderação do contexto de utilização e das pessoas visadas. O art. 4.º não exige que se atinja um nível específico de literacia; a avaliação individual de competência, quando a organização a queira, é trabalho de RH e da função de capacitação.

**Como cumprir**

A Policy 37 §11 é directamente operacionalizável para os papéis técnicos. Enquanto a lacuna não estiver fechada no Manual, a organização inclui por si o pessoal de negócio que opera sistemas de IA de produto e regista as conclusões dos trilhos como evidência para o Art. 4.

---

### Artigo 9 - Sistema de gestão de risco {#artigo-9---sistema-de-gestão-de-risco}

**Conteúdo normativo**

O Art. 9 exige um sistema de gestão de risco **contínuo e iterativo** ao longo de todo o ciclo de vida do sistema de IA de risco elevado: identificação e análise dos riscos conhecidos e razoavelmente previsíveis para a saúde, segurança e direitos fundamentais; estimativa dos riscos em uso previsto e em utilização indevida razoavelmente previsível; adoção de medidas de gestão de risco adequadas; e teste para identificar as medidas mais apropriadas.

**Cobertura SbD-ToE**

| Requisito AI Act | Capítulo SbD-ToE | Cobertura |
|---|---|---|
| Identificação e análise de riscos | Cap. 03 | Threat modeling (STRIDE, MITRE ATT&CK) + [playbook agentic](/sbd-toe/sbd-manual/threat-modeling/addon/metodologias-e-ferramentas#playbook-agentic) com MITRE ATLAS já incluído |
| Proporcionalidade ao risco | Cap. 01 + Cap. 02 §A0–A4 | Classificação L1–L3 + níveis de autonomia agentic A0–A4 ([`REQ-AGN-002`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn)) |
| Medidas de gestão de risco | Cap. 02 | Catálogo de requisitos por nível + `REQ-AGN-001..004` |
| Avaliação iterativa e contínua | Cap. 12 | Monitorização contínua, melhoria + `OPS-011..014` |

> ℹ️ **Nota:** L3 é a classificação de risco do Manual; não equivale a sistema de IA de risco elevado na acepção do AI Act (art. 6.º).

**O que o SbD-ToE cobre**

- Identificação estruturada de ameaças via threat modeling (Cap. 03), com o **playbook agentic** já incorporado e MITRE ATLAS como catálogo activo (não apenas extensível).
- Classificação de criticidade aplicacional (Cap. 01), base para proporcionalidade de controlos, **complementada pelos níveis de autonomia A0–A4** para sistemas que incluem agentes AI com *tool-use* ([`REQ-AGN-002`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn)).
- Catálogo de requisitos de segurança e respetivas medidas (Cap. 02), incluindo o subconjunto agentic `REQ-AGN-001..004`.
- Reavaliação contínua, em ciclo, com métricas operacionais (Cap. 12), incluindo sinais agentic-específicos (`OPS-011..014`).

**Fora de âmbito**

O sistema de gestão de riscos do art. 9.º (saúde, segurança e direitos fundamentais ao longo do ciclo de vida) é um sistema de gestão da organização e fica fora do âmbito do Manual por decisão do programa. O threat model, a classificação e a monitorização descritos acima servem-lhe de evidência; o Manual não prescreve a análise de riscos para a saúde, a segurança e os direitos fundamentais (p. ex., risco de discriminação, impacto societal).

**Como cumprir**

A organização conduz o sistema de gestão de riscos no seu próprio enquadramento (p. ex., **NIST AI RMF** ou **ISO/IEC 23894**) e referencia como evidência o threat model do Cap. 03, que já usa o **MITRE ATLAS** para o vetor adversarial, e a monitorização do Cap. 12.

---

### Artigo 10 - Dados e governação de dados {#artigo-10---dados-e-governação-de-dados}

**Conteúdo normativo**

O Art. 10 exige que os conjuntos de dados de treino, validação e teste obedeçam a práticas de governação de dados adequadas: relevância, representatividade, ausência de erros e completude na medida do possível, propriedades estatísticas apropriadas, e exame de possíveis enviesamentos suscetíveis de afetar saúde, segurança ou direitos fundamentais (art. 10.º, n.ºs 2 e 3). Com o Reg. (UE) 2026/1744, o tratamento excecional de categorias especiais de dados pessoais para deteção e correção de enviesamentos saiu do art. 10.º, n.º 5 (suprimido) para o novo art. 4.º-A.

**Cobertura SbD-ToE**

| Requisito AI Act | Capítulo SbD-ToE | Cobertura |
|---|---|---|
| Proveniência e integridade de dados | Cap. 05 + [`DEP-011`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-011) (inventário AI) + [`DEP-012`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-012) (AI BOM CycloneDX 1.6 *ml-bom*) | Proveniência, integridade e *pinning* de *datasets* e modelos |
| Requisitos de tratamento de dados | Cap. 02 | Requisitos de segurança de dados |
| Controlo de acesso e proteção | Cap. 04 | Arquitetura segura, classificação de dados |
| *Pinning* + lista de fornecedores de serviços de IA aprovados | `DEP-013/014` + Policy 39 | Versão fixa explícita; fornecedores de serviços de IA aprovados com cláusulas contratuais |

**O que o SbD-ToE cobre**

- Proveniência e integridade de artefactos da cadeia de fornecimento, aplicável a *datasets*, modelos, MCP *tools* e prompts embebidos (Cap. 05 §`DEP-011..014`).
- **AI BOM por *build*** em formato standardizado (CycloneDX 1.6 *ml-bom*) — operacionaliza a *AI-BOM* que estava sugerida na primeira versão deste cross-check (Policy 39, Cap. 05 US-14).
- Requisitos de proteção, classificação e controlo de acesso a dados (Cap. 02, Cap. 04).

**Fora de âmbito**

A governação dos dados de treino, validação e teste (qualidade estatística, representatividade, deteção e mitigação de enviesamento) fica fora do âmbito do Manual por decisão do programa: é trabalho de ciência de dados. O Manual não prescreve métricas de *fairness*, técnicas de *debiasing* nem critérios de representatividade; a proveniência e a integridade dos conjuntos de dados (`DEP-011`, `DEP-012`) dão-lhe evidência incidental.

**Art. 4.º-A: cobertura parcial**

O tratamento excepcional de categorias especiais de dados pessoais para corrigir enviesamentos (art. 4.º-A) tem cobertura parcial: há encriptação em repouso, controlo de acessos com registo, e prazo e apagamento verificável (`ENC-002`, `ACC-001`, `ACC-003`, `LOG-001`, `PRI-002`). Faltam as limitações técnicas à reutilização e a pseudonimização destes conjuntos, a documentação por acesso e o dever de confidencialidade de quem acede, a proibição geral de transmissão a terceiros, o apagamento logo que o enviesamento seja corrigido e o registo da fundamentação da estrita necessidade. O juízo de necessidade (n.º 1, al. a)) fica fora de âmbito: é decisão de ciência de dados e de proteção de dados.

**Como cumprir**

A *AI-BOM* que estava sugerida em versões anteriores deste documento **já está implementada** ([`DEP-012`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-012), Policy 39, Cap. 05 US-14). A governação de dados de treino (linhagem de dados, *datasheets for datasets*, *data cards*, avaliação de enviesamento) segue o processo de ciência de dados da organização, fora do Manual.

---

### Artigo 11 e Anexo IV - Documentação técnica {#artigo-11-e-anexo-iv---documentação-técnica}

**Conteúdo normativo**

O Art. 11 exige documentação técnica elaborada **antes** da colocação no mercado ou colocação em serviço e mantida atualizada, demonstrando conformidade; desde o Reg. (UE) 2026/1744, as PME (incluindo empresas em fase de arranque) e as pequenas empresas de média capitalização podem facultar os elementos do Anexo IV de forma simplificada, num formulário da Comissão (art. 11.º, n.º 1, segundo parágrafo). O Anexo IV detalha o índice mínimo: descrição geral do sistema, elementos de desenvolvimento e conceção, monitorização e controlo, gestão de risco, alterações ao longo do ciclo de vida, e lista de normas aplicadas.

**Cobertura SbD-ToE**

| Requisito AI Act | Capítulo SbD-ToE | Cobertura |
|---|---|---|
| Descrição técnica e de arquitetura | Cap. 04 + `ARC-014/015` | Documentação de arquitetura segura, incluindo padrões agentic |
| Requisitos e medidas de segurança | Cap. 02 + `REQ-AGN-001..004` | Catálogo de requisitos (incluindo subconjunto agentic) |
| Processo de desenvolvimento | Cap. 06, Cap. 07 | Desenvolvimento seguro, CI/CD com gates |
| Gestão de risco e alterações | Cap. 03, Cap. 12 | Threat model + playbook agentic; monitorização e melhoria |
| Inventário de componentes e modelos | Cap. 05 + [`DEP-012`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-012) AI BOM + Policy 39 | Evidência para o Anexo IV (ponto 2, alíneas a) e c): sistemas/ferramentas de terceiros e arquitetura de componentes; ponto 1, alínea c): versões de software) incluindo modelos, datasets, *tools* e prompts |
| Operação sob mandate | Policy 38 | *Mandate* documentado e versionado por agente AI |

**O que o SbD-ToE cobre**

- Documentação de arquitetura e decisões de segurança (Cap. 04), incluindo padrões agentic [`ARC-014`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-014) e [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015).
- Requisitos e medidas por nível de criticidade (Cap. 02), incluindo os requisitos `REQ-AGN-*` para agentes AI.
- Evidência de processo de desenvolvimento e pipeline (Cap. 06, Cap. 07).
- **AI BOM** como artefacto auditável que materializa parte da lista de componentes exigida pelo Anexo IV §2(a) ([`DEP-012`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-012), Policy 39).
- ***Mandate*** de cada agente AI como artefacto operacional rastreável (Policy 38) — entra no índice Anexo IV §2(b) (elementos de desenvolvimento e conceção) sempre que o sistema inclui agentes.

**Lacunas declaradas e fora de âmbito**

O SbD-ToE não gera a documentação **na estrutura formal do Anexo IV** nem um **model card** normalizado: a redacção é do prestador, e o Manual fornece a evidência de engenharia. O [mapa de evidência](./requisitos-aplicaveis#mapa-evidencia) da página gerada liga cada ponto do anexo IV aos artefactos e lista as lacunas por ponto. A adequação das métricas de desempenho (anexo IV, ponto 4) é lacuna declarada, pendente da ronda AISVS/SAIF do AppSec Core. Os pontos 2, al. d), e 5 remetem para os arts. 10.º e 9.º, que ficam fora de âmbito, tal como a lista de normas aplicadas e a declaração UE (pontos 7 e 8). O plano de acompanhamento (ponto 9) e as alterações predeterminadas (ponto 2, al. f)) estão cobertos por CTX-AIA-RE-R04 e pelo piso CTX-AIA-RE-P11.

**Como cumprir**

Sugere-se construir um "índice Anexo IV" que aponte para os artefactos SbD-ToE existentes (arquitetura, requisitos, threat model, evidência de pipeline e testes), complementado por um *model card* (finalidade, dados de treino, métricas de desempenho, limitações) redigido pelo prestador; as métricas de desempenho não têm ainda critério no Manual (ronda AISVS/SAIF).

---

### Artigo 12 e Artigo 19 - Registo de eventos (logging) e conservação de logs {#artigo-12-e-artigo-19---registo-de-eventos-logging-e-conservação-de-logs}

**Conteúdo normativo**

O Art. 12 exige capacidade de **registo automático de eventos** (logs) ao longo do ciclo de vida, com nível de rastreabilidade adequado à finalidade, permitindo identificar situações de risco e suportar a monitorização pós-comercialização. O Art. 19 obriga os prestadores a **conservar os logs** gerados automaticamente, na medida em que estejam sob o seu controlo, «por um período adequado à finalidade prevista do sistema de IA de risco elevado, de pelo menos seis meses» (art. 19.º, n.º 1); o art. 26.º, n.º 6, impõe o mesmo mínimo aos responsáveis pela implantação.

**Cobertura SbD-ToE**

| Requisito AI Act | Capítulo SbD-ToE | Cobertura |
|---|---|---|
| Logging "by design" | Cap. 12 | Observabilidade, logging estruturado |
| Rastreabilidade de eventos | Cap. 12 + [`OPS-011`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes) (AI/ML) + [`OPS-012`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-012) (audit per *tool invocation*) | Trilho auditável e correlação, com agente identificado por `agent_id` + `session_id` + `mandate_ref` |
| *Tool invocation audit* | [`OPS-012`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-012) + Cap. 12 US-13 | Cada *tool call* gera *audit event* estruturado (com `intent_event_ref` em A2+) |
| Detecção de *off-policy* e *jailbreak* | [`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014) + Policy 30 §9.3 | Sinais accionáveis ligados a IR |
| Conservação e retenção | Cap. 12 + `OPS-003` | Políticas de retenção e imutabilidade |

**O que o SbD-ToE cobre**

- Logging estruturado e observabilidade "by design" (Cap. 12).
- **Audit completo por *tool invocation*** quando há agentes AI ([`OPS-012`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-012)) — cada chamada gera evento com `timestamp`, `agent_id`, `session_id`, `mandate_ref`, `autonomy_level`, `tool`, `tool_version`, `args` (PII redactada), `intent_event_ref`, `outcome`, `external_effect`. Granular numa dimensão **complementar** (operacional) ao registo de eventos de inferência que cada sistema deve definir para cumprir o Art. 12 — não o substitui.
- Trilho auditável e correlação de eventos, com orientação para retenção e imutabilidade (Cap. 12).
- **Telemetria operacional agentic** (Cap. 12 US-13) que sustenta a base evidencial para Art. 72 (acompanhamento pós-comercialização) e Art. 73 (incidentes graves).
- **Pisos do contexto CTX-AIA-RE**: em sistemas de risco elevado, e em qualquer nível, a observabilidade AI/ML (`OPS-011`, piso P01), o audit per *tool invocation* quando há agentes (`OPS-012`, piso P02) e a retenção dos registos por pelo menos seis meses, sem exceção abaixo do piso legal (`OPS-003`, piso P03).

**Configuração por sistema e fora de âmbito**

O esquema do *model output* (versão de modelo, *features* relevantes, decisão, confiança) continua **configurável por sistema**, com dois mínimos: o registo que permite identificar modificações substanciais (piso CTX-AIA-RE-P11) e, quando um sistema do anexo III apoia decisões sobre pessoas, o resultado e os principais elementos de cada decisão (CTX-AIA-RE-R03). O Cap. 12 fixa o esquema *operacional* (quem invocou, com que mandate, sobre que recurso); o esquema *epistémico* (porquê este output) é declarado por sistema. Os registos próprios da identificação biométrica (art. 12.º, n.º 3) ficam fora de âmbito.

**Como cumprir**

A camada operacional já está implementada (`OPS-011..014` + Cap. 12 US-13). Resta declarar o esquema do *model output* por sistema, garantindo retenção por um período adequado à finalidade prevista do sistema, de pelo menos seis meses (art. 19.º, n.º 1, e art. 26.º, n.º 6), e compatível com o RGPD. Documentar o período de conservação como evidência para Art. 12/19.

---

### Artigo 13 - Transparência e prestação de informações aos responsáveis pela implantação {#artigo-13---transparência-e-prestação-de-informação-aos-utilizadores-implementadores}

**Conteúdo normativo**

O Art. 13 exige que os sistemas de IA de risco elevado sejam suficientemente transparentes para que os responsáveis pela implantação (*deployers*) interpretem e usem o output adequadamente, acompanhados de **instruções de utilização** com a identidade e os dados de contacto do prestador, características, capacidades, limitações de desempenho, riscos conhecidos e medidas de supervisão humana.

**Cobertura SbD-ToE**

| Requisito AI Act | Capítulo SbD-ToE | Cobertura |
|---|---|---|
| Documentação de capacidades e limitações | Cap. 02, Cap. 04, Policy 38 (mandate) | Requisitos, arquitetura e *mandate* com `capabilities` + `scope` + `risk_residual` |
| Identidade do fornecedor de serviços de IA e *runtime* | Policy 38 (`agent_runtime` no mandate) + [`DEP-014`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-014) (lista de fornecedores de serviços de IA) | Identidade do fornecedor de serviços de IA + versão *pinned* do modelo |
| Supervisão humana exigida | Cap. 02 §A0–A4 + Policy 38 | Nível de autonomia A0–A4 declarado por uso/contexto |

**O que o SbD-ToE cobre**

- Base documental de requisitos e arquitetura que alimenta parte das instruções de utilização (Cap. 02, Cap. 04).
- ***Mandate*** (Policy 38) como **fonte estruturada** de *capabilities*, *scope*, *autonomy_level*, *risk_residual* e procedimentos de supervisão — directamente extractável para "instruções de utilização" do *deployer*.

**Lacunas declaradas**

A declaração dos níveis de exatidão e solidez nas instruções de utilização (art. 13.º, n.º 3, al. b), subal. ii)) é lacuna declarada, pendente da ronda AISVS/SAIF do AppSec Core. A matriz declara também como lacunas a finalidade prevista e a descrição da interface. A redacção das instruções é do prestador; o Manual fornece a evidência, e a interpretação do output é apoiada pela supervisão mínima do `ARC-014` (piso CTX-AIA-RE-P08).

**Como cumprir**

Sugere-se derivar um documento de "instruções de utilização" a partir do ***mandate*** (Policy 38), dos artefactos do Cap. 04 (arquitetura, fronteiras de confiança) e Cap. 06, complementado pelas métricas de desempenho e limitações que o prestador declara; até à ronda AISVS/SAIF, essas métricas não têm critério no Manual.

---

### Artigo 14 - Supervisão humana {#artigo-14---supervisão-humana}

> ⚡ **Revisão 2026-09-27.** A primeira versão deste cross-check tratava o Art. 14 como largamente fora de AppSec. Com a camada agentic — A0–A4, `REQ-AGN-*`, [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015), Policy 38 — e o piso CTX-AIA-RE-P08, os n.os 1 a 4 do Art. 14 estão **cobertos** para qualquer sistema de risco elevado, com ou sem agentes. A interface de supervisão é requisito do Manual; o desenho concreto da UX que a cumpre é do produto.

**Conteúdo normativo**

O Art. 14 exige que os sistemas de IA de risco elevado sejam concebidos para permitir **supervisão humana efetiva**, incluindo a capacidade de compreender as capacidades e limitações, detetar e interpretar o output, decidir não usar ou anular o sistema, e interromper o seu funcionamento (*stop*).

**Cobertura SbD-ToE**

| Requisito AI Act | Capítulo SbD-ToE | Cobertura |
|---|---|---|
| Interface de supervisão em qualquer sistema de risco elevado | [`ARC-014`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-014) + piso CTX-AIA-RE-P08 | Compreender capacidades e limitações, detetar anomalias, interpretar o resultado, decidir não o usar ou anulá-lo, parar o sistema; advertência a quem supervisiona sobre o enviesamento da automatização |
| Definir nível de supervisão proporcional | Cap. 02 §A0–A4 + [`REQ-AGN-002`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn) | Cinco níveis de autonomia (A0 leitura → A4 autónomo); classificação por contexto |
| Mandate operacional com supervisão declarada | Policy 38 (mandate) + [`REQ-AGN-001`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn) | *Owner*, *approver*, `review_cadence`, *kill-switch*, *intent audit sink* |
| Capacidade arquitectónica de interrupção (*stop*) | [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015) + [`REQ-AGN-003`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn) (*kill-switch*) | Revogação de credenciais + terminação de *runtime* + isolamento de *namespace* + alerta on-call, em segundos |
| Anulação consciente de acção destrutiva | [`REQ-AGN-004`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn) (*intent declaration*) + [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015) (OOB approval) | Agente declara intenção antes de *tool call* destrutivo; aprovação humana *out-of-band* exigida em A2+ |
| Exercício periódico do *stop* | Policy 38 + Policy 18 §9.3 | *Kill-switch* exercitado em sandbox/staging (anual A2, trimestral A3, mensal A4: cadências do Manual) com cronómetro registado |
| Auditoria de *off-policy actions* | [`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014) + Policy 30 §9.3 + Policy 16 §11.4 | Divergência entre `intent` declarado e acção real gera alerta accionável + entra em IR |

**O que o SbD-ToE cobre**

- **Modelo normativo de níveis de supervisão** (Cap. 02 §A0–A4). A escolha *human-in-the-loop* / *human-on-the-loop* / *autonomous* é declarada explicitamente por contexto, com critérios de promoção e descida; subir nível exige evidência operacional dos pré-requisitos.
- ***Mandate*** (Policy 38) — operacionaliza Art. 14 declarando, para cada agente em uso, **quem supervisiona**, **com que cadência**, **com que *kill-switch*** e **sob que mandato assinado**.
- ***Kill-switch* arquitectónico** ([`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015) + [`REQ-AGN-003`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn)) — não é um botão simbólico: revoga credenciais OIDC + termina sessões + isola *namespace* + alerta on-call, com tempo medido. Exercitado periodicamente conforme nível de autonomia.
- ***Intent declaration*** ([`REQ-AGN-004`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn)) — em A2+, antes de cada *tool call* destrutivo o agente declara à infraestrutura *o que vai fazer e porquê*; o gate cruza intent vs acção real a posteriori ([`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014)).
- **Aprovação humana *out-of-band*** — fora do canal do agente (Slack, GitHub review, webhook assinado), para que *prompt injection* no canal principal não consiga "auto-aprovar".

**Sistemas sem agentes e fora de âmbito**

A Policy 38 e o `REQ-AGN` aplicam-se a agentes com uso de ferramentas. Para sistemas de risco elevado sem agentes, o piso CTX-AIA-RE-P08 eleva o `ARC-014` em qualquer nível: a interface de supervisão permite compreender as capacidades e limitações do sistema, detetar anomalias, interpretar o resultado, decidir não o usar ou anulá-lo e parar o sistema, e quem supervisiona é advertido para o enviesamento da automatização. Na matriz de cobertura, os n.os 1 a 4 do Art. 14 estão cobertos. O desenho concreto da UX (que informação mostrar, em que momento pedir confirmação) é do produto; o requisito que essa UX tem de cumprir é do Manual.

A verificação por duas pessoas antes de uma decisão com base em identificação biométrica (Art. 14, n.º 5) fica fora de âmbito, com as restantes especificidades desses sistemas.

**Como cumprir**

A maior parte do trabalho técnico está agora dentro do manual: declarar o nível A0–A4 no *mandate* (Policy 38), instrumentar *kill-switch* exercitado ([`REQ-AGN-003`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn)) e *intent declaration* ([`REQ-AGN-004`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn)) conforme [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015), e configurar [`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014) para detetar divergência. Para sistemas sem agentes, aplica-se o `ARC-014` com o âmbito do piso P08, e a equipa de produto desenha a UX que o cumpre. Para sistemas de IA de risco elevado com componente agentic, a US-15 (Cap. 02) + US-16 (Cap. 04) constituem o checklist operacional.

---

### Artigo 15 - Exatidão, solidez e cibersegurança {#artigo-15---exatidão-robustez-e-cibersegurança}

> 🎯 **Núcleo do cross-check.** É na cibersegurança do Art. 15 que o SbD-ToE oferece a cobertura mais forte e direta. A cibersegurança de sistemas de IA é, em grande medida, a disciplina central do manual aplicada a um novo tipo de artefacto (modelos e pipelines de ML). A exatidão e a solidez do mesmo artigo estão pendentes de uma ronda futura.

**Conteúdo normativo**

O Art. 15 exige que os sistemas de IA de risco elevado atinjam um nível apropriado de **exatidão, solidez e cibersegurança** e tenham desempenho consistente ao longo do ciclo de vida. O n.º 5 é explícito quanto ao vetor adversarial: os sistemas devem ser resilientes a tentativas de terceiros não autorizados de alterar o uso, output ou desempenho explorando vulnerabilidades, e as medidas técnicas devem prevenir, detetar, responder, resolver e controlar ataques que visem manipular o conjunto de dados de treino (**contaminação de dados**, *data poisoning*) ou componentes pré-treinados utilizados no treino (**contaminação de modelos**, *model poisoning*), dados de entrada concebidos para fazer com que o modelo de IA cometa um erro (**exemplos antagónicos ou evasão de modelos**, *adversarial examples / model evasion*), **ataques de confidencialidade** ou **falhas do modelo** (*model flaws*) — medidas a incluir «se for caso disso» (art. 15.º, n.º 5, terceiro parágrafo).

**Cobertura SbD-ToE**

| Requisito AI Act | Capítulo SbD-ToE | Cobertura |
|---|---|---|
| Identificação de ameaças adversariais | Cap. 03 + [playbook agentic](/sbd-toe/sbd-manual/threat-modeling/addon/metodologias-e-ferramentas#playbook-agentic) | MITRE ATLAS + OWASP LLM Top 10 2025 já incorporados como catálogos activos |
| Defesa em profundidade e isolamento | Cap. 04 ([`ARC-014`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-014)/[`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015)) | Trust boundaries (incl. *agentic boundary*); agente como *principal* isolado |
| Integridade da cadeia (dados/modelos) | Cap. 05 (`DEP-011..014`) + Policy 39 | Proveniência + AI BOM + *pinning* + fornecedores de serviços de IA aprovados |
| Testes de robustez e *red teaming* | Cap. 10 §C5 + Policy 19 §7 | *Eval suites* contínuas (regression de prompt, abuse corpus, *A/B*, drift) |
| Deteção e resposta em *runtime* | Cap. 12 + [`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014) + Policy 30 §9 | Detecção de *jailbreak* / *off-policy*; *audit per tool invocation* |
| Hardening do serviço de inferência | Cap. 04, Cap. 09 + [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015) | Arquitetura, containers/runtime, identidade efémera |

**O que o SbD-ToE cobre**

- **Modelação de ameaças** (Cap. 03), com o **playbook agentic** (DFD + threat library MITRE ATLAS + OWASP LLM Top 10 2025) já incluído como catálogo activo — não apenas extensível.
- **Arquitetura defensiva** (Cap. 04): fronteiras de confiança (incluindo a *agentic boundary* em [`ARC-014`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-014) e o agente como *principal* em [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015)), segregação, validação de input, limitação de exposição do serviço de inferência.
- **Integridade da cadeia de fornecimento** (Cap. 05 `DEP-011..014`): proveniência, AI BOM ([`DEP-012`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-012) CycloneDX 1.6 *ml-bom*), *pinning* de versão ([`DEP-013`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-013) — mitiga `AML.T0109` *Supply Chain Rug Pull*), lista de fornecedores de serviços de IA aprovados ([`DEP-014`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-014)).
- **Testes de segurança** (Cap. 10 §C5 *eval suites*): regression tests de prompt/skill, *abuse* / *red-team corpus* (LLM01-2025 prompt injection, LLM06-2025 excessive agency), *drift detection*, *A/B testing*.
- **Monitorização em runtime** (Cap. 12 + `OPS-011..014`): deteção de anomalias, *model drift*, *audit per tool invocation* ([`OPS-012`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-012)), *budget / runaway* ([`OPS-013`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-013)), *jailbreak* / *off-policy actions* ([`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014)).
- **Hardening de runtime** (Cap. 09 + [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015)): isolamento do serviço de inferência em containers; agente AI com *workload identity* efémera OIDC + *scope* mínimo por *tool*.

**Lacuna declarada**

A exatidão e a solidez (níveis, parâmetros e métricas; art. 15.º, n.os 1 e 3) são lacuna declarada, pendente da ronda AISVS/SAIF do AppSec Core. A cibersegurança do art. 15.º, n.º 5, está coberta. Do n.º 4, existem o *fallback*, o *fail-secure* e a validação de output com falha fechada; faltam a redundância e os planos de segurança para o desempenho, e a mitigação de enviesamento em circuitos de realimentação de sistemas que continuam a aprender. O *adversarial training* não é prescrito na versão base; os filtros de segurança de conteúdo na entrada e na saída são exigidos para geradores de conteúdo realista (piso CTX-AIA-RE-P10).

**Como cumprir**

Sugere-se: (1) estender o threat model (Cap. 03) com o **MITRE ATLAS** e o **OWASP ML/LLM Top 10**; (2) adicionar ao catálogo de testes (Cap. 10) **testes de robustez adversarial** e um programa de **AI red teaming**; (3) tratar a proveniência de dados e modelos como cadeia de fornecimento crítica (Cap. 05); (4) configurar a monitorização (Cap. 12) para *drift* e padrões de ataque; (5) registar as métricas de exatidão obtidas como evidência, sem as apresentar como cumprimento, até à ronda AISVS/SAIF.

---

### Artigo 17 - Sistema de gestão da qualidade (QMS) {#artigo-17---sistema-de-gestão-da-qualidade-qms}

**Conteúdo normativo**

O Art. 17 obriga os prestadores de sistemas de IA de risco elevado a um sistema de gestão da qualidade documentado (cuja aplicação, desde o Reg. (UE) 2026/1744, «deve ser proporcionada à dimensão da organização do prestador», sem baixar o grau de rigor exigido — art. 17.º, n.º 2), abrangendo estratégia de conformidade, procedimentos de conceção e desenvolvimento, controlo de qualidade, testes e validação, gestão de risco, monitorização pós-comercialização e comunicação de incidentes.

**Cobertura SbD-ToE**

| Requisito AI Act | Capítulo SbD-ToE | Cobertura |
|---|---|---|
| Procedimentos de desenvolvimento | Cap. 06, Cap. 07 (incl. US-19) | Desenvolvimento seguro, CI/CD com gates, agentes como *principals* na pipeline |
| Controlo de qualidade e validação | Cap. 10 §C5 (*eval suites*) + Cap. 11 | Testes, gate de release, regression de prompts |
| Gestão de risco | Cap. 03 + playbook agentic | Threat modeling + threat library MITRE ATLAS |
| Governação e responsabilidades | Cap. 14 + Policy 38 (mandates) + Policy 39 (AI BOM lifecycle) | RACI, políticas, aprovações; ciclo de vida formal para agentes e supply chain AI |
| Monitorização e incidentes | Cap. 12 + `OPS-012..014` + Policy 30 §9 | Monitorização agentic + IR para *off-policy* / *jailbreak* |

**O que o SbD-ToE cobre**

- Procedimentos de desenvolvimento e pipeline com gates auditáveis (Cap. 06, Cap. 07), incluindo agentes AI como *principals* (US-19).
- Controlo de qualidade técnico e validação pré-release (Cap. 10, Cap. 11), incluindo *eval suites* contínuas para agentes (§C5).
- Estrutura de governação, papéis e aprovações (Cap. 14).
- **Ciclo de vida formal de governação para agentes AI** (Policy 38) — *mandate* com proposta → avaliação → aprovação → ativação → operação → revisão / revogação. Serve de evidência para elementos do QMS do art. 17.º, n.º 1 (p. ex., a manutenção de registos da alínea k)).
- **Ciclo de vida formal para *supply chain* AI** (Policy 39) — formato AI BOM, *pinning*, lista aprovada de fornecedores de serviços de IA, resposta a incidentes *upstream* por classe.

**Fora de âmbito**

O sistema de gestão da qualidade do art. 17.º é um sistema de gestão da organização e fica fora do âmbito do Manual por decisão do programa. Os componentes descritos acima servem-lhe de evidência: a matriz regista-os como evidência de engenharia para a conceção, o desenvolvimento, a comunicação de incidentes graves, a manutenção de registos e a responsabilização (art. 17.º, n.º 1, als. b), c), i), k) e m)).

**Como cumprir**

A organização que tenha de manter o QMS pode referenciar os gates e processos SbD-ToE (Cap. 06/07/10/11/14) como evidência, reaproveitando, quando aplicável, um sistema **ISO/IEC 42001** já existente.

---

### Artigo 25 - Cadeia de fornecimento e responsabilidades ao longo da cadeia {#artigo-25---cadeia-de-fornecimento-e-responsabilidades-ao-longo-da-cadeia}

**Conteúdo normativo**

O Art. 25 (alterado pelo Reg. (UE) 2026/1744) trata das responsabilidades ao longo da cadeia de valor da IA: um distribuidor, importador, responsável pela implantação ou outro terceiro passa a ser considerado prestador, com as obrigações do art. 16.º, se colocar o seu nome ou marca num sistema de IA de risco elevado, lhe introduzir uma modificação substancial ou lhe modificar a finalidade prevista de forma que se torne de risco elevado (n.º 1); o prestador inicial deve então cooperar com os novos prestadores (n.º 2); e o prestador de um sistema de IA de risco elevado e o terceiro que forneça «um sistema de IA, um modelo de IA, ferramentas, serviços, componentes ou processos» nele utilizados ou integrados devem, «mediante acordo escrito», especificar as informações, capacidades, acesso técnico e assistência necessários (n.º 4). O incumprimento dos n.ºs 2 e 4 passou a estar sujeito a coima (art. 99.º, n.º 4, alínea d-A)).

**Cobertura SbD-ToE**

| Requisito AI Act | Capítulo SbD-ToE | Cobertura |
|---|---|---|
| Versão *pinned* de modelos e componentes AI | [`DEP-013`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-013) | Versão fixa explícita; sem `latest` / ranges / aliases dinâmicos |
| Lista de fornecedores de serviços de IA aprovados | [`DEP-014`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-014) + Policy 39 | Lista versionada com `risk_classification`, `contract_ref`, cláusulas críticas |
| AI BOM por *build* | [`DEP-012`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-012) + Policy 39 | CycloneDX 1.6 *ml-bom* gerado por *release* |
| Cláusulas contratuais com fornecedores de serviços de IA | Cap. 14 US-21 + Policy 33 §10 | Cláusulas de retention, localização, audit, notificação, conformidade |
| Resposta a incidentes *upstream* | Policy 39 §7 | Triagem por classe (`AML.T0019` *data poisoning*, `AML.T0109` *rug pull*, `AML.T0110` *tool poisoning*, *provider outage*) |

**O que o SbD-ToE cobre**

- **Materialização da cadeia de fornecimento AI** como inventário auditável: *pinning*, lista de fornecedores de serviços de IA aprovados, AI BOM por *release*.
- **Cláusulas contratuais** específicas para fornecedores de serviços de IA (Policy 33 §10) — data retention, training opt-out, localização (RGPD Art. 44–49), *audit rights*, SLA de notificação prévia de mudanças, declaração de conformidade Art. 53/55 quando GPAI.
- **Resposta a incidentes *upstream*** por classe — `AML.T0019` *Publish Poisoned Datasets*, `AML.T0109` *AI Supply Chain Rug Pull*, `AML.T0110` *AI Agent Tool Poisoning*, *provider outage* — com *runbooks* específicos.
- **Reclassificação por mudança material** — Cap. 03 US-11 e Cap. 04 US-16 obrigam a revisão do *threat model* e da arquitectura quando o fornecedor de serviços de IA muda versão maior do modelo ou quando a `tools_allowlist` muda.

**Lacuna declarada (parcial)**

As cláusulas da Policy 33 §10 não especificam ainda a informação, as capacidades, o acesso técnico e a assistência que o art. 25.º, n.º 4, exige no acordo escrito. A qualificação de quem passa a ser prestador (n.º 1) fica fora de âmbito: é qualificação jurídica. A redacção jurídica das responsabilidades ao longo da cadeia é do jurídico; o SbD-ToE fornece a estrutura técnica e operacional.

**Como cumprir**

A base operacional existe (Policy 39 + `DEP-013/014` + Cap. 14 US-21). Falta completar as cláusulas com o conteúdo do art. 25.º, n.º 4, em articulação com o jurídico — em particular para sistemas em que a organização é simultaneamente *provider* e *deployer*.

---

### Artigo 26 - Obrigações dos *deployers* {#artigo-26---obrigações-dos-deployers}

**Conteúdo normativo**

O Art. 26 define obrigações específicas dos responsáveis pela implantação (*deployers*) de sistemas de IA de risco elevado: usar o sistema conforme as instruções de utilização, atribuir supervisão humana qualificada, assegurar input data adequado, monitorizar o funcionamento, conservar os registos sob o seu controlo durante pelo menos seis meses (Art. 26.º, n.º 6), e cooperar com autoridades.

**Cobertura SbD-ToE**

| Requisito AI Act | Capítulo SbD-ToE | Cobertura |
|---|---|---|
| Uso conforme instruções; supervisão atribuída | Policy 38 (mandate com `owner`, `approver`, `autonomy_level`) | *Mandate* declara *quem supervisiona*, *com que cadência*, *sob que mandato* |
| Atribuição de supervisão qualificada | Cap. 00 (nota AI Reliability Engineer) + Policy 37 §11 | Função composta + literacia obrigatória por *role* |
| Monitorização do funcionamento | Cap. 12 US-13 + `OPS-011..014` | Telemetria agentic em produção |
| Conservação de logs (Art. 26.º, n.º 6) | Cap. 12 + `OPS-003` (retention) + [`OPS-012`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-012) (audit per tool) | *Audit trail* completo sob controlo do *deployer* |
| Comunicação a autoridades | Cap. 12 + Cap. 14 + Policy 30 §9.3 + Policy 32 (IRP) | IR alimenta notificação a autoridades |

**O que o SbD-ToE cobre**

- **Mandate como artefacto de *deployer*** (Policy 38) — quando a organização opera (e não fornece) um sistema de IA de risco elevado, o *mandate* é a evidência formal de "como se usa este sistema, sob que supervisão, com que *kill-switch*". Directamente extractável para auditoria do Art. 26.
- **Função composta para supervisão qualificada** (Cap. 00 nota *AI Reliability Engineer*) — `appsec` + `devops` + `grc` sob mandate do `CISO`, com literacia obrigatória (Policy 37 §11).
- **Monitorização operacional** (Cap. 12 US-13, `OPS-011..014`) — logs e sinais sob controlo do *deployer*, conservados conforme política (`OPS-003`).
- **Resposta a incidentes** ligada à notificação a autoridades (Cap. 12 + Policy 30 §9.3 + Policy 32) — *off-policy actions* e *jailbreak* em produção entram no fluxo IR que alimenta Art. 73.

**Lacunas declaradas**

A matriz declara: operar sistemas de IA adquiridos conforme as instruções de utilização do prestador (n.º 1, parcial); competência, autoridade e apoio de quem supervisiona sistemas não agênticos do lado do responsável pela implantação (n.º 2, parcial); pertinência e representatividade dos dados de entrada para a finalidade (n.º 4, lacuna); informação ao prestador e suspensão de sistemas não agênticos quando há risco (n.º 5, parcial). Estão cobertos a conservação dos registos (n.º 6, piso CTX-AIA-RE-P03) e a informação às pessoas afectadas (n.º 11, CTX-AIA-RE-R03). A informação e a consulta dos trabalhadores (n.º 7) ficam fora de âmbito: são matéria de direito do trabalho.

Quando a organização é simultaneamente prestador (*provider*) e responsável pela implantação (*deployer*) (caso comum em desenvolvimento *first-party*), a separação de obrigações entre os dois papéis fica diluída — convém clarificar internamente (e contratualmente quando há sub-deployers) qual papel se assume em cada uso.

**Como cumprir**

Para usos em que a organização é *deployer*, o *mandate* (Policy 38) é o artefacto central. Sugere-se um *template* específico para *deployer mandate* que documente explicitamente a referência ao fornecedor de serviços de IA (`contract_ref` + [`DEP-014`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-014)), as instruções de utilização recebidas, e o alinhamento com os requisitos do Art. 26.

---

### Artigo 72 - Acompanhamento pós-comercialização {#artigo-72---monitorização-pós-comercialização}

**Conteúdo normativo**

O Art. 72 exige que os prestadores criem e documentem um sistema de acompanhamento pós-comercialização proporcionado, que recolha, documente e analise dados sobre o desempenho do sistema ao longo da sua vida útil, permitindo avaliar a conformidade contínua. O sistema deve basear-se num plano de acompanhamento pós-comercialização que, desde o Reg. (UE) 2026/1744, «deve fazer parte da documentação técnica a que se refere o anexo IV»; a Comissão adota orientações, incluindo um modelo, até 2 de setembro de 2027 (art. 72.º, n.º 3).

**Cobertura SbD-ToE**

| Requisito AI Act | Capítulo SbD-ToE | Cobertura |
|---|---|---|
| Recolha contínua de telemetria | Cap. 12 + `OPS-011..014` + Cap. 12 US-13 | Observabilidade AI/ML + sinais agentic-específicos |
| Análise de desempenho e degradação | Cap. 12 + [`OPS-011`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes) | Deteção de *drift*, anomalias, degradação de precisão |
| *Audit per tool invocation* | [`OPS-012`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-012) | Reconstrução *post-mortem* de qualquer sessão agentic |
| *Token budget* e *runaway* | [`OPS-013`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-013) | Detecção de consumo descontrolado e mudanças de eficiência |
| *Off-policy actions* e *jailbreak* | [`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014) + Policy 30 §9.3 | Sinais accionáveis ligados a IR |
| Melhoria contínua | Cap. 12 + Cap. 10 §C5 (*eval suites*) | Ciclo pós-incidente realimenta *eval suite* offline |

**O que o SbD-ToE cobre**

- Recolha e análise contínua de telemetria operacional (Cap. 12), com sinais agentic-específicos completos (`OPS-011..014`).
- **Telemetria agentic** (Cap. 12 US-13) que materializa a base evidencial para o plano de acompanhamento pós-comercialização: *tool invocation audit events*, *intent events*, *budget metrics*, *off-policy / jailbreak detection*.
- Deteção de degradação de desempenho e *model drift* (Cap. 12, [`OPS-011`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes)).
- **Ciclo de realimentação para *eval suites*** (Cap. 10 §C5) — incidentes detectados em produção alimentam a suite offline, fortalecendo a regressão futura.

**Cobertura pelo regime**

Quando a organização é o prestador, o plano de acompanhamento por sistema é requisito do regime ([CTX-AIA-RE-R04](./requisitos-aplicaveis#acrescentos)): integra a documentação técnica (anexo IV, ponto 9) e nomeia os sinais recolhidos em produção (`OPS-011`) e os fornecidos pelos responsáveis pela implantação, os critérios de desempenho, a cadência e o responsável da análise, e os gatilhos para ação corretiva. As métricas de desvio do modelo ficam pendentes da ronda AISVS/SAIF do AppSec Core.

**Como cumprir**

Aplicar o R04 sobre a observabilidade do Cap. 12, com *dashboards* de desempenho, *drift* e estado de vulnerabilidades, e gatilhos que desencadeiam rollback, reclassificação, revisão do threat model ou notificação de incidente grave.

---

### Artigo 73 - Comunicação de incidentes graves {#artigo-73---comunicação-de-incidentes-graves}

**Conteúdo normativo**

O Art. 73 obriga os prestadores a comunicar **incidentes graves** às autoridades de fiscalização do mercado dos Estados-Membros onde ocorreram, **imediatamente** após determinarem uma relação causal (ou a probabilidade razoável de que exista) entre o sistema de IA e o incidente e, em qualquer caso, **o mais tardar 15 dias** após o prestador ou, se for caso disso, o responsável pela implantação ter tomado conhecimento; **até 10 dias** em caso de morte de uma pessoa; e **até 2 dias** em caso de infração generalizada ou de incidente grave na aceção do art. 3.º, ponto 49, alínea b). Pode ser apresentado um relatório inicial incompleto, seguido de um completo (n.º 5). Segue-se a investigação e a tomada de medidas corretivas (n.º 6).

**Cobertura SbD-ToE**

| Requisito AI Act | Capítulo SbD-ToE | Cobertura |
|---|---|---|
| Deteção e resposta a incidentes | Cap. 12 + [`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014) (*jailbreak* / *off-policy*) + Policy 30 §9.3 | Processo de deteção, resposta, pós-incidente; sinais agentic accionáveis |
| Classes de incidente agentic-específicas | Policy 16 §11.4 | *Off-policy action*, *intent-action divergence*, *prompt injection* bem-sucedida, falha de *kill-switch*, *credential exposure* |
| Resposta a incidentes *upstream* | Policy 39 §7 | *Rug pull*, *dataset poisoning*, *tool poisoning*, *provider outage* |
| Escalonamento e responsabilidades | Cap. 14 + Policy 38 | Papéis e responsabilidades; *owner* + *approver* declarados no *mandate* |
| Classificação de severidade | Cap. 01, Cap. 12 | Critérios de impacto, classificação |
| Definição e prazos de notificação | Política 32 §4.1 e [Política 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória) | Definição de incidente grave e prazos do art. 73.º |

**O que o SbD-ToE cobre**

- Processo de deteção, resposta e pós-incidente (Cap. 12).
- **Classes de incidente agentic-específicas** definidas (Policy 16 §11.4): *off-policy action*, *intent-action divergence*, *prompt injection* bem-sucedida que resultou em *tool call* não autorizada, falha do *kill-switch*, *credential exposure*.
- **Resposta a incidentes *upstream*** (Policy 39 §7) — quando o incidente origina no fornecedor (de serviços de IA) do modelo, do *dataset* ou do MCP server, e não na operação interna.
- Papéis de escalonamento e responsabilidades (Cap. 14, Policy 38).
- Critérios de impacto que suportam a classificação de severidade (Cap. 01, Cap. 12).

**Lacuna declarada (parcial)**

A definição de incidente grave e os prazos estão na Política 32 (§4.1 e " + "§6), e a matriz dá os n.os 1 a 5 do art. 73.º como cobertos. Os prazos são os do art. 73.º (15 dias / 10 dias / 2 dias, a contar do conhecimento). Falta a regra de não alterar o sistema, de forma que afecte a análise de causas, sem informar previamente a autoridade (art. 73.º, n.º 6): o IRP privilegia a contenção «quando possível».

**Como cumprir**

Configurar o esquema de incidente do Cap. 12 e os exportadores do SIEM/ITSM para produzir a notificação prevista na " + POL32 + ", e acrescentar ao runbook a informação prévia à autoridade antes de qualquer alteração ao sistema que afecte a análise de causas.

---

### Modelos de IA de finalidade geral - Artigos 53 e 55 (GPAI) {#modelos-de-ia-de-finalidade-geral---artigos-53-e-55-gpai}

**Conteúdo normativo**

O Art. 53 impõe aos prestadores de **modelos de IA de finalidade geral** (GPAI) documentação técnica do modelo (Anexo XI), informação e documentação para os prestadores de sistemas de IA que integrem o modelo (Anexo XII), uma política de cumprimento do direito de autor e um «resumo suficientemente pormenorizado sobre os conteúdos utilizados para o treino». O Art. 55 acresce, para modelos com **risco sistémico**, a avaliação do modelo incluindo «testagens antagónicas» (*adversarial testing* / *red teaming*), avaliação e mitigação de riscos sistémicos, comunicação de incidentes graves e garantia de **cibersegurança adequada do modelo e da infraestrutura física**.

**Cobertura SbD-ToE**

| Requisito AI Act | Capítulo SbD-ToE | Cobertura |
|---|---|---|
| Avaliação adversarial / *red teaming* | Cap. 10 §C5 + Policy 19 §7 + Cap. 03 playbook agentic | *Eval suites* contínuas (regression de prompt, *abuse corpus*, *A/B*, *drift*) + threat library MITRE ATLAS |
| Cibersegurança do modelo e infraestrutura | Cap. 04 ([`ARC-014`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-014)/[`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015)), Cap. 08, Cap. 09 | Arquitetura agentic, IaC, containers/runtime |
| Proteção de pesos e artefactos | Cap. 05 (`DEP-011..014`) + Policy 39 + Cap. 04 | Integridade, proveniência, AI BOM, *pinning*, controlo de acesso |
| Monitorização e incidentes | Cap. 12 + `OPS-011..014` + Policy 30 §9 | Detecção de *off-policy* / *jailbreak* / *exfiltration* via tool |
| Cláusulas contratuais para GPAI | Cap. 14 US-21 + Policy 33 §10 + [`DEP-014`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-014) | Declaração contratual de conformidade Art. 53/55 dos fornecedores de serviços de IA |

**O que o SbD-ToE cobre**

- **AI red teaming contínuo** materializado (Cap. 10 §C5 + Policy 19 §7) — não apenas como recomendação. *Eval suites* incluem *abuse corpus* (LLM01-2025 *prompt injection*, LLM06-2025 *excessive agency*) com cadência mensal em A4 (escolha do Manual).
- **Cibersegurança da infraestrutura** que serve o modelo (Cap. 04 incl. [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015), Cap. 08, Cap. 09).
- **Proteção de integridade e acesso** a pesos, *checkpoints* e *datasets* — agora com AI BOM auditável e *pinning* exigido (`DEP-012/013`, Policy 39). Resposta a `AML.T0109` *Supply Chain Rug Pull* documentada em Policy 39 §7.
- **Monitorização e resposta** (Cap. 12 + [`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014)) — detecção activa de *jailbreak* (LLM01-2025) e *off-policy actions* em produção; corpus de detecção actualizado conforme cadência do *mandate*.
- **Conformidade contratual declarada pelos fornecedores de serviços de IA GPAI** ([`DEP-014`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-014), Cap. 14 US-21, Policy 33 §10) — exigida no processo de aprovação do fornecedor de serviços de IA.

**Lacunas declaradas e fora de âmbito**

A documentação dos anexos XI e XII apoia-se em evidência do Manual (AI BOM, *eval suites*), mas a sua redacção é do prestador do modelo; o Manual está escrito do lado de quem consome o modelo. A avaliação do modelo com protocolos normalizados e testagem antagónica documentada ao nível do modelo (art. 55.º, n.º 1, al. a)) tem cobertura parcial. A comunicação de incidentes graves e a cibersegurança do modelo e da infraestrutura (art. 55.º, n.º 1, als. c) e d)) estão cobertas. A política de direitos de autor e o resumo dos conteúdos de treino (art. 53.º, n.º 1, als. c) e d)) ficam fora de âmbito: são plano jurídico. A avaliação dos riscos sistémicos à escala da União (art. 55.º, n.º 1, al. b)) é de domínio de IA; o threat model adversarial dá-lhe evidência.

**Como cumprir**

Sugere-se: tratar pesos, *checkpoints* e *datasets* como ativos de cadeia de fornecimento com proveniência e controlo de acesso (Cap. 05); instituir AI red teaming contínuo (Cap. 10) alinhado com o MITRE ATLAS; aplicar hardening de infraestrutura (Cap. 04/08/09); e remeter documentação GPAI, copyright e avaliação de risco sistémico para as equipas de IA, jurídico e compliance.

---

### Práticas proibidas e transparência (Artigos 5 e 50) {#práticas-proibidas-e-transparência-artigos-5-e-50}

**Conteúdo normativo**

O Art. 5 proíbe um conjunto de práticas (p. ex., manipulação subliminar prejudicial, classificação social — *social scoring* —, a utilização de sistemas de identificação biométrica à distância em «tempo real» em espaços acessíveis ao público para efeitos de aplicação da lei, salvo exceções); a partir de 2 de dezembro de 2026, também a geração ou manipulação de imagens, vídeos, áudios realistas ou material similar íntimos de pessoa identificável sem o seu consentimento e de material de abuso sexual de crianças (art. 5.º, n.º 1, primeiro parágrafo, alíneas b-A) e b-B), com as condições dos n.ºs 1-A e 1-B, aditados pelo Reg. (UE) 2026/1744; art. 113.º, terceiro parágrafo, alínea a)). O Art. 50 impõe deveres de transparência a «determinados sistemas de inteligência artificial» (informar que se interage com IA; marcar conteúdo sintético / *deepfakes*).

**Cobertura SbD-ToE**

O Art. 50 está **coberto** por dois requisitos do regime, declarados com o grau ART50 do contexto CTX-AIA-RE (que se declara também sozinho, para sistemas que não são de risco elevado): informar as pessoas de que interagem com um sistema de IA ou de que estão expostas a reconhecimento de emoções ou a categorização biométrica, e divulgar as falsificações profundas (CTX-AIA-RE-R01); e marcar o conteúdo sintético num formato legível por máquina, com a marcação verificada em teste (CTX-AIA-RE-R02).

Para as alíneas b-A) e b-B) do art. 5.º, a colocação no mercado de um sistema cuja finalidade prevista não é essa geração só é proibida se, entre outras condições, o sistema não dispuser de «medidas técnicas de segurança razoáveis e adequadas e de outras garantias para prevenir de forma segura essa geração ou manipulação» (art. 5.º, n.º 1-A, alínea a), subalínea ii)). Essas salvaguardas estão **cobertas** pelos pisos CTX-AIA-RE-P09 (threat model da utilização indevida do conteúdo gerado, avaliado com red-team e testes de segurança de conteúdo) e P10 (filtros e classificadores de segurança de conteúdo na entrada e na saída), sem substituir a qualificação jurídica.

**Fora de âmbito**

O juízo de admissibilidade de uma finalidade (Art. 5) é qualificação jurídica e de produto e fica fora de âmbito; para as alíneas a), b) e e) do n.º 1, o Manual dá evidência (Cap. 02 US-17, `DEP-011`). Fica também fora de âmbito a divulgação de texto gerado por IA publicado sobre matérias de interesse público (art. 50.º, n.º 4, segundo parágrafo): é decisão editorial do responsável pela implantação.

**Como cumprir**

Declarar o grau ART50 na aplicação quando o sistema está abrangido pelo Art. 50 e aplicar os requisitos R01 e R02 e, em geradores de imagem, vídeo ou áudio realistas, os pisos P09 e P10. A determinação de proibições e a qualificação jurídica dos deveres de transparência ficam com o jurídico e o produto.

---

## PARTE II: SÍNTESE E REFERÊNCIAS {#parte-ii-síntese-e-referências}

### Síntese da cobertura AI Act / SbD-ToE {#síntese-da-cobertura-ai-act--sbd-toe}

O AI Act pede sistemas de IA **seguros, robustos, documentados e supervisionáveis**, com responsabilidade do prestador ao longo de todo o ciclo de vida. O SbD-ToE oferece o **coração técnico-operacional** desse esforço: gestão de risco técnico (Cap. 01, 03), arquitetura defensiva (Cap. 04), integridade da cadeia de dados e modelos (Cap. 05), pipelines e gates de qualidade (Cap. 06, 07, 11), testes e robustez adversarial (Cap. 10), logging e acompanhamento pós-comercialização (Cap. 12) e governação (Cap. 14).

A cobertura mais **forte e direta** está na **cibersegurança do Art. 15** e nos seus correlatos operacionais (Art. 12 e 19 registo, Art. 14 supervisão humana, Art. 50 transparência, Art. 72 acompanhamento pós-comercialização, Art. 73 incidentes) - é aqui que a evidência técnica do SbD-ToE é mais directamente reutilizável — sem que isso equivalha a cumprir o AI Act, que exige todos os requisitos da secção 2 e a avaliação de conformidade.

A matriz separa três respostas. **Coberto:** cibersegurança, registo, supervisão humana, transparência do art. 50.º, modificação substancial, explicação às pessoas afectadas, acompanhamento pós-comercialização, incidentes graves e a declaração do estatuto de risco elevado como contexto da aplicação. **Lacuna declarada:** a exatidão e a solidez (pendentes da ronda AISVS/SAIF do AppSec Core) e as lacunas pontuais listadas por artigo. **Fora de âmbito, com razão:** gestão de riscos (art. 9.º), governação de dados de treino (art. 10.º), gestão da qualidade (art. 17.º), especificidades da identificação biométrica, avaliação da conformidade, marcação CE, declaração UE e o juízo sobre práticas proibidas. Nestas, o SbD-ToE fornece evidência técnica às equipas próprias, não o juízo de conformidade.

O resultado é coerente com a filosofia do manual:

- **Hoje**, o SbD-ToE permite construir e operar o software de um sistema de IA com segurança por desenho.
- **Amanhã**, quando a organização tiver de cumprir o AI Act, declara o contexto CTX-AIA-RE na aplicação, aplica os pisos e requisitos que ele eleva e trata com as equipas próprias o que fica fora de âmbito.

### Âmbito, papéis e sanções {#âmbito-papéis-e-sanções}

O AI Act distingue **prestadores (providers)**, **responsáveis pela implantação (deployers)**, importadores e distribuidores, com obrigações distintas. O grosso das obrigações técnicas (e da cobertura SbD-ToE) recai sobre o **prestador de sistemas de IA de risco elevado**; o *deployer* tem obrigações próprias (uso conforme às instruções, supervisão humana, em certos casos FRIA - Art. 26, 27).

Em termos sancionatórios (Art. 99), o regulamento estabelece patamares máximos (para PME, incluindo empresas em fase de arranque, cada coima não pode exceder a percentagem ou o montante, «consoante o que for mais baixo» — art. 99.º, n.º 6; o mesmo vale para as pequenas empresas de média capitalização quanto às coimas dos n.ºs 4 e 5 — art. 99.º, n.º 6-A, aditado pelo Reg. (UE) 2026/1744):

- **Práticas proibidas (Art. 5)**: até **35 M€** ou **7%** do volume de negócios anual mundial (o que for mais elevado).
- **Incumprimento das obrigações enumeradas no art. 99.º, n.º 4** — prestadores (art. 16.º), mandatários (art. 22.º), importadores (art. 23.º), distribuidores (art. 24.º), prestadores e operadores nos termos do art. 25.º, n.ºs 2 e 4 (alínea d-A), aditada pelo Reg. (UE) 2026/1744), responsáveis pela implantação (art. 26.º), organismos notificados (art. 31.º, art. 33.º, n.ºs 1, 3 e 4, e art. 34.º) e transparência (art. 50.º): até **15 M€** ou **3%**.
- **Informação incorreta, incompleta ou enganosa** aos organismos notificados ou às autoridades nacionais competentes em resposta a um pedido: até **7,5 M€** ou **1%**.
- Para prestadores de **modelos de IA de finalidade geral** (Art. 101): coimas aplicadas pela Comissão, até **15 M€** ou **3%** (o que for mais elevado), aplicáveis a partir de 2 de agosto de 2026 (o art. 113.º, terceiro parágrafo, alínea b), exceciona o art. 101.º da data de 2 de agosto de 2025).

### Referências {#referências}

- **AI Act**: Regulamento (UE) 2024/1689 (CELEX: [32024R1689](https://eur-lex.europa.eu/legal-content/PT/TXT/?uri=CELEX:32024R1689)), alterado pelo Regulamento (UE) 2026/1744 («Omnibus Digital em matéria de IA», CELEX: [32026R1744](https://eur-lex.europa.eu/legal-content/PT/TXT/?uri=CELEX:32026R1744)); texto consolidado de 27.7.2026 (CELEX: [02024R1689-20260727](https://eur-lex.europa.eu/legal-content/PT/TXT/?uri=CELEX:02024R1689-20260727)).
- **Art. 9** - Sistema de gestão de risco (ciclo de vida).
- **Art. 10** - Dados e governação de dados (representatividade, enviesamento).
- **Art. 11 e Anexo IV** - Documentação técnica.
- **Art. 12 / Art. 19** - Registo de eventos e conservação de logs.
- **Art. 13 / Art. 14** - Transparência aos deployers e supervisão humana.
- **Art. 15** - Exatidão, solidez e cibersegurança (resistência a ataques, incl. exemplos antagónicos).
- **Art. 17** - Sistema de gestão da qualidade.
- **Art. 72 / Art. 73** - Acompanhamento pós-comercialização e comunicação de incidentes graves.
- **Art. 53 / Art. 55** - Obrigações GPAI e GPAI com risco sistémico.
- **Art. 99 / Art. 101** - Regime sancionatório.
- **ISO/IEC 42001** - Sistema de gestão de inteligência artificial.
- **ISO/IEC 23894** - Gestão de risco de IA.
- **ISO/IEC 27090** (em desenvolvimento) - Cibersegurança de IA.
- **NIST AI Risk Management Framework (AI RMF 1.0)**.
- **MITRE ATLAS** - Adversarial Threat Landscape for Artificial-Intelligence Systems.
- **OWASP Machine Learning Security Top 10** e **OWASP Top 10 for LLM Applications**.

---

:::note Exceções e evidência de controlo

A aplicação do SbD-ToE em contexto AI Act, tal como em NIS2 e DORA, beneficia de um processo formal de exceções internas a requisitos técnicos. Uma exceção interna não altera nenhuma obrigação legal do AI Act; apenas documenta um risco técnico aceite para o dossiê de evidência. Casos em que um requisito não é aplicável, ou em que se aceita um risco residual temporário (p. ex., um vetor adversarial mitigado por compensação enquanto se prepara o *retraining*), devem ser documentados, aprovados ao nível adequado e revistos periodicamente.

O Cap. 14 (Governança e Contratação) do SbD-ToE fornece os artefactos necessários: registo de exceções, critérios de aceitação de risco, cadeia de aprovação e plano de remediação. Note-se que certos desvios **não são exceptuáveis** no contexto AI Act - desde logo, qualquer uso que recaia nas práticas proibidas do Art. 5. A existência de um processo formal de exceções não é sinal de fragilidade: é evidência de governação madura e de controlo consciente sobre o perfil de risco.

:::

---

**Versão:** 1.1
**Data:** Setembro 2026
**Próxima revisão:** com a próxima revisão da matriz de cobertura do AI Act
