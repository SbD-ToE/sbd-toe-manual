---
id: intro
title: AI Act - Cross-Check Normativo
description: Análise de como o SbD-ToE cobre os requisitos técnicos do Regulamento (UE) 2024/1689 (AI Act) - exatidão, robustez, cibersegurança, logging, gestão de risco e monitorização pós-comercialização de sistemas de IA
tags: [cross-check, ai-act, regulamento-ia, ia, machine-learning, robustez, ciberseguranca, gpai]
sidebar_position: 6
---

# AI Act: Cross-Check Normativo

> Para implementação prática, consulte o [Playbook SbD-ToE 4 AI Act](/sbd-toe/cross-check-normativo/ai-act/playbook).
>
> Para padrões aplicacionais universais, ver capítulos base do SbD-ToE (01–14).

## Âmbito

### 🤖 AI Act - Regulamento de Inteligência Artificial

O **AI Act** é o **Regulamento (UE) 2024/1689** (CELEX: [32024R1689](https://eur-lex.europa.eu/legal-content/PT/TXT/?uri=CELEX:32024R1689)), o primeiro quadro jurídico horizontal do mundo dedicado à inteligência artificial. Entrou em vigor a 1 de agosto de 2024 e aplica-se de forma faseada:

- **2 de fevereiro de 2025** - práticas proibidas (Art. 5) e literacia em IA (Art. 4).
- **2 de agosto de 2025** - modelos de IA de finalidade geral (GPAI, Capítulo V), governação e regime sancionatório.
- **2 de agosto de 2026** - generalidade das obrigações para sistemas de IA de **alto risco** do Anexo III.
- **2 de agosto de 2027** - sistemas de alto risco abrangidos pela legislação de produto do Anexo I.

O AI Act adota uma **abordagem baseada no risco**, com quatro patamares: risco **inaceitável** (proibido, Art. 5), **alto risco** (Art. 6 e Anexos I/III, sujeito ao grosso das obrigações técnicas), risco **limitado** (deveres de transparência, Art. 50) e risco **mínimo** (sem obrigações específicas). Sobre estes patamares incidem ainda regras próprias para **GPAI** (Art. 53) e GPAI com **risco sistémico** (Art. 55).

É essencial enquadrar a natureza do regulamento: o AI Act é, antes de tudo, **legislação de segurança de produto e de proteção de direitos fundamentais** aplicada a sistemas de IA, não uma norma de segurança aplicacional (AppSec). Contudo, as obrigações para sistemas de alto risco incorporam **requisitos técnicos substanciais** que cruzam diretamente com o SbD-ToE - em particular:

- **Art. 9** - sistema de gestão de risco ao longo do ciclo de vida;
- **Art. 12 / Art. 19** - registo automático de eventos (logging) e conservação de logs;
- **Art. 15** - exatidão, robustez e **cibersegurança** (incluindo resiliência a ataques adversariais);
- **Art. 17** - sistema de gestão da qualidade (QMS);
- **Art. 72** - monitorização pós-comercialização;
- **Art. 73** - comunicação de incidentes graves.

No SbD-ToE, o AI Act é operacionalizado através das mesmas disciplinas técnicas que sustentam qualquer software seguro - engenharia segura (requisitos, arquitetura, desenvolvimento, IaC, pipelines, testes), cadeia de fornecimento e proveniência (dependências, containers, SBOM), processos de monitorização e resposta, e governação/contratação - aplicadas agora ao **ciclo de vida de sistemas de IA** (datasets, modelos, pipelines de treino e inferência, serviços de inferência).

> ⚖️ **Nota editorial.**
> Esta secção é uma **síntese operacional** dos artigos relevantes do AI Act, não uma citação literal do regulamento.
> Baseia-se, em particular, nos Artigos 9.º (gestão de risco), 10.º (dados e governação de dados), 11.º e Anexo IV (documentação técnica), 12.º e 19.º (registos/logs), 13.º–14.º (transparência e supervisão humana), 15.º (exatidão, robustez, cibersegurança), 17.º (QMS), 72.º (monitorização pós-comercialização), 73.º (incidentes graves) e 53.º/55.º (GPAI e risco sistémico).

> ⚖️ **Nota sobre referências técnicas.**
> O AI Act estabelece requisitos essenciais mas remete o detalhe técnico para **normas harmonizadas** (a desenvolver pelo CEN-CENELEC) e especificações comuns.
> Padrões como **ISO/IEC 42001** (sistema de gestão de IA), **ISO/IEC 23894** (gestão de risco de IA), **ISO/IEC 27090** (segurança de IA, em desenvolvimento), o **NIST AI Risk Management Framework (AI RMF 1.0)**, o **MITRE ATLAS** (táticas e técnicas adversariais contra ML), o **OWASP Machine Learning Security Top 10** e o **OWASP Top 10 for LLM Applications** são amplamente reconhecidos e fornecem base sólida para cumprir os requisitos técnicos e processuais.
> O SbD-ToE assume estes padrões como **boas práticas recomendadas**, não como requisitos legais em si mesmos.

## Aviso Regulatório

O SbD-ToE cobre o **"como" técnico** dos requisitos de alto risco, mas **não substitui** as dimensões jurídicas, de domínio de IA e de avaliação de conformidade do AI Act. Em concreto, ficam **fora do âmbito** do manual:

- **Classificação de risco** (Art. 6 e Anexos I/III) - determinação jurídica de se um sistema é de alto risco.
- **Governação de dados de treino, validação e teste** (Art. 10) - representatividade, deteção e mitigação de enviesamento (*bias*), qualidade estatística dos conjuntos de dados. Estas são questões de **domínio de IA/ciência de dados**, não de AppSec.
- **Transparência e informação ao utilizador implementador** (Art. 13) e a pessoas singulares (Art. 50).
- **Supervisão humana** (Art. 14) - conceção de mecanismos de *human-in-the-loop* / *human-on-the-loop*.
- **Avaliação de impacto sobre os direitos fundamentais (FRIA)** (Art. 27) - obrigação dos utilizadores implementadores (*deployers*).
- **Avaliação de conformidade** (Art. 43), envolvimento de **organismos notificados**, **declaração UE de conformidade** (Art. 47), **marcação CE** (Art. 48) e **registo na base de dados da UE** (Art. 49/71).
- **Determinação de práticas proibidas** (Art. 5) e qualificação jurídica de papéis (provider, deployer, importador, distribuidor).

Estas dimensões são da competência de equipas de compliance, jurídico, ciência de dados e da relação com a autoridade competente. O SbD-ToE fornece os controlos técnicos e a evidência; não emite o juízo de conformidade.

---

## Matriz de Cross-Check (resumo)

| Domínio AI Act | Referência (artigo) | Cobertura SbD-ToE | Lacuna Intencional | Ação de Adaptação |
|---|---|---|---|---|
| Sistema de gestão de risco | Art. 9 | Cap. 01 (classificação), Cap. 03 (threat modeling), Cap. 02 (requisitos), Cap. 12 (monitorização) | Risco para saúde, segurança e direitos fundamentais ao longo do uso previsto | Estender threat model com taxonomia de risco de IA (ATLAS) e impacto societal |
| Dados e governação de dados | Art. 10 | Cap. 05 (proveniência), Cap. 02 (requisitos de dados) | Representatividade, enviesamento, qualidade estatística (domínio IA) | Processo de *data governance* de ciência de dados; *datasheets*/*data cards* |
| Documentação técnica | Art. 11, Anexo IV | Cap. 02, Cap. 04 (arquitetura), Cap. 06 | Estrutura formal do Anexo IV; *model cards* | Mapear artefactos SbD-ToE para o índice do Anexo IV |
| Registo de eventos (logging) | Art. 12, Art. 19 | Cap. 12 (observabilidade, retenção) | Campos específicos de rastreabilidade de IA (inputs, versão de modelo) | Estender esquema de logs com metadados de inferência |
| Transparência aos deployers | Art. 13 | Cap. 02, Cap. 04 (parcial) | Instruções de uso, limitações, métricas de desempenho | Gerar "instruções de utilização" a partir de Cap. 04/06 |
| Supervisão humana | Art. 14 | (parcial) Cap. 04 | Mecanismos *human-in/on-the-loop*, *stop button* | Desenho de controlos de supervisão (domínio IA/UX) |
| Exatidão, robustez e cibersegurança | Art. 15 | Cap. 03, Cap. 04, Cap. 05, Cap. 10, Cap. 12 | Métricas de exatidão declaradas; limiares regulamentares | Adicionar testes de robustez adversarial e *AI red teaming* |
| Sistema de gestão da qualidade | Art. 17 | Cap. 07 (CI/CD), Cap. 11 (release), Cap. 06, Cap. 14 | Estrutura formal de QMS conforme Art. 17 | Mapear gates SbD-ToE para os elementos do QMS |
| Monitorização pós-comercialização | Art. 72 | Cap. 12 (monitorização, drift) | Plano formal de monitorização pós-mercado | Formalizar plano e *dashboards* de desempenho/drift |
| Incidentes graves | Art. 73 | Cap. 12, Cap. 14 | Definição de "incidente grave"; prazos e templates | Parametrizar runbook e esquema de incidente para Art. 73 |
| GPAI e risco sistémico | Art. 53, Art. 55 | Cap. 05, Cap. 10, Cap. 12 | Documentação técnica GPAI; política de *copyright* | Adicionar *AI red teaming* contínuo e proteção do modelo/pesos |
| Conformidade e marcação CE | Art. 43, 47–49 | (não coberto) | Avaliação de conformidade e processo jurídico | Estabelecer swimlane GRC + jurídico |

---

## PARTE I: ANÁLISE NORMATIVA

### Artigo 9 - Sistema de gestão de risco

**Conteúdo normativo**

O Art. 9 exige um sistema de gestão de risco **contínuo e iterativo** ao longo de todo o ciclo de vida do sistema de IA de alto risco: identificação e análise dos riscos conhecidos e razoavelmente previsíveis para a saúde, segurança e direitos fundamentais; estimativa dos riscos em uso previsto e em utilização indevida razoavelmente previsível; adoção de medidas de gestão de risco adequadas; e teste para identificar as medidas mais apropriadas.

**Cobertura SbD-ToE**

| Requisito AI Act | Capítulo SbD-ToE | Cobertura |
|---|---|---|
| Identificação e análise de riscos | Cap. 03 | Threat modeling (STRIDE, MITRE ATT&CK; extensível a ATLAS) |
| Proporcionalidade ao risco | Cap. 01 | Classificação de criticidade L1–L3 |
| Medidas de gestão de risco | Cap. 02 | Catálogo de requisitos por nível |
| Avaliação iterativa e contínua | Cap. 12 | Monitorização contínua, melhoria |

**O que o SbD-ToE cobre**

- Identificação estruturada de ameaças via threat modeling (Cap. 03), com metodologias extensíveis ao domínio de IA.
- Classificação de criticidade aplicacional (Cap. 01), base para proporcionalidade de controlos.
- Catálogo de requisitos de segurança e respetivas medidas (Cap. 02).
- Reavaliação contínua, em ciclo, com métricas operacionais (Cap. 12).

**Lacunas intencionais**

O threat modeling do SbD-ToE é, por construção, **agnóstico ao domínio**: cobre ameaças de segurança ao sistema, mas não prescreve a análise de riscos para **saúde, segurança e direitos fundamentais** específica do AI Act (p. ex., risco de discriminação, impacto societal). Esta dimensão é própria do AI Act e exige envolvimento de equipas de domínio, ética e jurídico.

**Como cumprir**

Sugere-se estender o threat model do Cap. 03 com uma taxonomia de risco de IA - usando o **MITRE ATLAS** para o vetor adversarial e o **NIST AI RMF** / **ISO/IEC 23894** para o enquadramento de risco - e ligar a iteração ao ciclo de melhoria contínua do Cap. 12. Documentar o risco residual e as medidas, mantendo o registo auditável que o Art. 9 pressupõe.

---

### Artigo 10 - Dados e governação de dados

**Conteúdo normativo**

O Art. 10 exige que os conjuntos de dados de treino, validação e teste obedeçam a práticas de governação de dados adequadas: relevância, representatividade, ausência de erros e completude na medida do possível, propriedades estatísticas apropriadas, e exame de possíveis enviesamentos suscetíveis de afetar saúde, segurança ou direitos fundamentais.

**Cobertura SbD-ToE**

| Requisito AI Act | Capítulo SbD-ToE | Cobertura |
|---|---|---|
| Proveniência e integridade de dados | Cap. 05 | Proveniência de artefactos, integridade da cadeia |
| Requisitos de tratamento de dados | Cap. 02 | Requisitos de segurança de dados |
| Controlo de acesso e proteção | Cap. 04 | Arquitetura segura, classificação de dados |

**O que o SbD-ToE cobre**

- Proveniência e integridade de artefactos da cadeia de fornecimento, aplicável a *datasets* e modelos (Cap. 05).
- Requisitos de proteção, classificação e controlo de acesso a dados (Cap. 02, Cap. 04).

**Lacunas intencionais**

A **qualidade estatística, representatividade e deteção/mitigação de enviesamento** são problemas de **ciência de dados e do domínio de aplicação**, não de segurança aplicacional. O SbD-ToE não prescreve métricas de fairness, técnicas de *debiasing* nem critérios de representatividade - corretamente, pois variam por caso de uso e são da competência das equipas de IA/dados.

**Como cumprir**

Sugere-se complementar o SbD-ToE com um processo de *data governance* de ciência de dados (linhagem de dados, *datasheets for datasets*, *data cards*, avaliação de enviesamento), tratando a **integridade e proveniência** dos *datasets* como uma extensão do inventário do Cap. 05 (uma "AI-BOM" que estende a SBOM a dados e modelos).

---

### Artigo 11 e Anexo IV - Documentação técnica

**Conteúdo normativo**

O Art. 11 exige documentação técnica elaborada **antes** da colocação no mercado e mantida atualizada, demonstrando conformidade. O Anexo IV detalha o índice mínimo: descrição geral do sistema, elementos de desenvolvimento e conceção, monitorização e controlo, gestão de risco, alterações ao longo do ciclo de vida, e lista de normas aplicadas.

**Cobertura SbD-ToE**

| Requisito AI Act | Capítulo SbD-ToE | Cobertura |
|---|---|---|
| Descrição técnica e de arquitetura | Cap. 04 | Documentação de arquitetura segura |
| Requisitos e medidas de segurança | Cap. 02 | Catálogo de requisitos |
| Processo de desenvolvimento | Cap. 06, Cap. 07 | Desenvolvimento seguro, CI/CD |
| Gestão de risco e alterações | Cap. 03, Cap. 12 | Threat model, monitorização e melhoria |

**O que o SbD-ToE cobre**

- Documentação de arquitetura e decisões de segurança (Cap. 04).
- Requisitos e medidas por nível de criticidade (Cap. 02).
- Evidência de processo de desenvolvimento e pipeline (Cap. 06, Cap. 07).

**Lacunas intencionais**

O SbD-ToE não gera a documentação **na estrutura formal do Anexo IV** nem um **model card** normalizado. A organização dos artefactos segundo o índice regulamentar é trabalho de mapeamento, não de produção técnica nova.

**Como cumprir**

Sugere-se construir um "índice Anexo IV" que aponte para os artefactos SbD-ToE existentes (arquitetura, requisitos, threat model, evidência de pipeline e testes), complementado por um *model card* (finalidade, dados de treino, métricas de desempenho, limitações) da responsabilidade da equipa de IA.

---

### Artigo 12 e Artigo 19 - Registo de eventos (logging) e conservação de logs

**Conteúdo normativo**

O Art. 12 exige capacidade de **registo automático de eventos** (logs) ao longo do ciclo de vida, com nível de rastreabilidade adequado à finalidade, permitindo identificar situações de risco e suportar a monitorização pós-comercialização. O Art. 19 obriga os fornecedores a **conservar os logs** gerados automaticamente, na medida em que estejam sob o seu controlo.

**Cobertura SbD-ToE**

| Requisito AI Act | Capítulo SbD-ToE | Cobertura |
|---|---|---|
| Logging "by design" | Cap. 12 | Observabilidade, logging estruturado |
| Rastreabilidade de eventos | Cap. 12 | Trilho auditável, correlação |
| Conservação e retenção | Cap. 12 | Políticas de retenção, imutabilidade |

**O que o SbD-ToE cobre**

- Logging estruturado e observabilidade "by design" (Cap. 12).
- Trilho auditável e correlação de eventos, com orientação para retenção e imutabilidade (Cap. 12).

**Lacunas intencionais**

O SbD-ToE define "logs com campos obrigatórios" mas mantém o esquema **genérico**. Os campos específicos de **rastreabilidade de IA** - versão do modelo, *prompt*/input (quando admissível e em conformidade com o RGPD), pontuações de confiança, deteção de *drift* - não são fixados, por dependerem do caso de uso e do equilíbrio com a proteção de dados pessoais.

**Como cumprir**

Sugere-se estender o esquema de logs do Cap. 12 com metadados de inferência (identificador e versão do modelo, *features* relevantes, decisão e confiança, *correlation id*), garantindo retenção alinhada com a vida útil do sistema e com requisitos do RGPD. Documentar o período de conservação como evidência para Art. 12/19.

---

### Artigo 13 - Transparência e prestação de informação aos utilizadores implementadores

**Conteúdo normativo**

O Art. 13 exige que os sistemas de alto risco sejam suficientemente transparentes para que os *deployers* interpretem e usem o output adequadamente, acompanhados de **instruções de utilização** com identidade do fornecedor, características, capacidades, limitações de desempenho, riscos conhecidos e medidas de supervisão humana.

**Cobertura SbD-ToE**

| Requisito AI Act | Capítulo SbD-ToE | Cobertura |
|---|---|---|
| Documentação de capacidades e limitações | Cap. 02, Cap. 04 | Requisitos e arquitetura (parcial) |

**O que o SbD-ToE cobre**

- Base documental de requisitos e arquitetura que alimenta parte das instruções de utilização (Cap. 02, Cap. 04).

**Lacunas intencionais**

O SbD-ToE não produz **instruções de utilização orientadas ao deployer**, nem declara métricas de desempenho ou níveis de exatidão. Estes elementos dependem do modelo concreto e do domínio, ficando fora do âmbito AppSec.

**Como cumprir**

Sugere-se derivar um documento de "instruções de utilização" a partir dos artefactos do Cap. 04 (arquitetura, fronteiras de confiança) e Cap. 06, complementado pelas métricas de desempenho e limitações fornecidas pela equipa de IA.

---

### Artigo 14 - Supervisão humana

**Conteúdo normativo**

O Art. 14 exige que os sistemas de alto risco sejam concebidos para permitir **supervisão humana efetiva**, incluindo a capacidade de compreender as capacidades e limitações, detetar e interpretar o output, decidir não usar ou anular o sistema, e interromper o seu funcionamento (*stop*).

**Cobertura SbD-ToE**

| Requisito AI Act | Capítulo SbD-ToE | Cobertura |
|---|---|---|
| Capacidade técnica de interrupção | Cap. 04 | Arquitetura (controlos de fronteira, kill-switch técnico) |

**O que o SbD-ToE cobre**

- Padrões arquiteturais que tornam tecnicamente possível interromper, isolar ou degradar com segurança um componente (Cap. 04).

**Lacunas intencionais**

A **conceção dos mecanismos de supervisão humana** (*human-in-the-loop*, *human-on-the-loop*, pontos de intervenção, UX de decisão) é um problema de desenho de sistema de IA e de fatores humanos, não de AppSec. O SbD-ToE garante que a interrupção é *implementável*, não *desenha* o fluxo de supervisão.

**Como cumprir**

Sugere-se que a equipa de IA e de produto especifique os pontos de supervisão e a UX de intervenção, apoiando-se nos padrões arquiteturais do Cap. 04 para garantir que o *stop* e a anulação são tecnicamente fiáveis e auditáveis.

---

### Artigo 15 - Exatidão, robustez e cibersegurança

> 🎯 **Núcleo do cross-check.** É no Art. 15 que o SbD-ToE oferece a cobertura mais forte e direta. A cibersegurança de sistemas de IA é, em grande medida, a disciplina central do manual aplicada a um novo tipo de artefacto (modelos e pipelines de ML).

**Conteúdo normativo**

O Art. 15 exige que os sistemas de alto risco atinjam um nível adequado de **exatidão, robustez e cibersegurança** e tenham desempenho consistente ao longo do ciclo de vida. O n.º 5 é explícito quanto ao vetor adversarial: os sistemas devem ser resilientes a tentativas de terceiros não autorizados de alterar o uso, output ou desempenho explorando vulnerabilidades, e as medidas técnicas devem prevenir, detetar, responder, resolver e controlar ataques que visem o **envenenamento de dados (*data poisoning*)**, o **envenenamento de modelo (*model poisoning*)**, os **exemplos adversariais ou evasão de modelo (*adversarial examples / model evasion*)**, os **ataques à confidencialidade** e as **falhas do modelo (*model flaws*)**.

**Cobertura SbD-ToE**

| Requisito AI Act | Capítulo SbD-ToE | Cobertura |
|---|---|---|
| Identificação de ameaças adversariais | Cap. 03 | Threat modeling (extensível a MITRE ATLAS) |
| Defesa em profundidade e isolamento | Cap. 04 | Arquitetura segura, fronteiras de confiança |
| Integridade da cadeia (dados/modelos) | Cap. 05 | Proveniência, SBOM/AI-BOM, integridade |
| Testes de robustez e *red teaming* | Cap. 10 | SAST/DAST/fuzzing; extensível a testes adversariais |
| Deteção e resposta em runtime | Cap. 12 | Monitorização, deteção de anomalias e *drift* |
| Hardening do serviço de inferência | Cap. 04, Cap. 09 | Arquitetura, containers/runtime |

**O que o SbD-ToE cobre**

- **Modelação de ameaças** (Cap. 03), enquadramento natural para o vetor adversarial de ML quando estendido com o MITRE ATLAS.
- **Arquitetura defensiva** (Cap. 04): fronteiras de confiança, segregação, validação de input, limitação de exposição do serviço de inferência.
- **Integridade da cadeia de fornecimento** (Cap. 05): proveniência de *datasets* e modelos, verificação de integridade (mitiga *data/model poisoning* e modelos comprometidos de repositórios públicos).
- **Testes de segurança** (Cap. 10): base para incorporar testes de robustez adversarial, *fuzzing* de input e *AI red teaming*.
- **Monitorização em runtime** (Cap. 12): deteção de anomalias, *model drift*, padrões de *evasion* e exfiltração (ataques à confidencialidade / *model inversion* / *membership inference*).
- **Hardening de runtime** (Cap. 09): isolamento do serviço de inferência em containers, redução de superfície.

**Lacunas intencionais**

O SbD-ToE não fixa **métricas de exatidão** nem limiares regulamentares de desempenho (são específicos do modelo e do caso de uso). Não prescreve, na versão base, técnicas adversariais concretas (*adversarial training*, *input sanitization* específica de ML, *output filtering* de LLM) - estas são adições de domínio que o manual enquadra mas não impõe, para preservar universalidade.

**Como cumprir**

Sugere-se: (1) estender o threat model (Cap. 03) com o **MITRE ATLAS** e o **OWASP ML/LLM Top 10**; (2) adicionar ao catálogo de testes (Cap. 10) **testes de robustez adversarial** e um programa de **AI red teaming**; (3) tratar a proveniência de dados e modelos como cadeia de fornecimento crítica (Cap. 05); (4) configurar a monitorização (Cap. 12) para *drift* e padrões de ataque; (5) declarar as métricas de exatidão obtidas e os limiares aceitáveis, em articulação com a equipa de IA.

---

### Artigo 17 - Sistema de gestão da qualidade (QMS)

**Conteúdo normativo**

O Art. 17 obriga os fornecedores a um sistema de gestão da qualidade documentado, abrangendo estratégia de conformidade, procedimentos de conceção e desenvolvimento, controlo de qualidade, testes e validação, gestão de risco, monitorização pós-comercialização e comunicação de incidentes.

**Cobertura SbD-ToE**

| Requisito AI Act | Capítulo SbD-ToE | Cobertura |
|---|---|---|
| Procedimentos de desenvolvimento | Cap. 06, Cap. 07 | Desenvolvimento seguro, CI/CD com gates |
| Controlo de qualidade e validação | Cap. 10, Cap. 11 | Testes, gate de release |
| Gestão de risco | Cap. 03 | Threat modeling |
| Governação e responsabilidades | Cap. 14 | RACI, políticas, aprovações |
| Monitorização e incidentes | Cap. 12 | Monitorização, resposta a incidentes |

**O que o SbD-ToE cobre**

- Procedimentos de desenvolvimento e pipeline com gates auditáveis (Cap. 06, Cap. 07).
- Controlo de qualidade técnico e validação pré-release (Cap. 10, Cap. 11).
- Estrutura de governação, papéis e aprovações (Cap. 14).

**Lacunas intencionais**

O SbD-ToE fornece os **componentes operacionais** de um QMS técnico, mas não a sua **estrutura formal e documental** conforme o Art. 17 (procedimentos escritos, responsabilidades de gestão, manual da qualidade). Esta formalização é trabalho de organização documental.

**Como cumprir**

Sugere-se mapear os gates e processos SbD-ToE (Cap. 06/07/10/11/14) para os elementos do Art. 17, produzindo um documento de QMS que referencie estes controlos como evidência - reaproveitando, quando aplicável, um sistema **ISO/IEC 42001** já existente.

---

### Artigo 72 - Monitorização pós-comercialização

**Conteúdo normativo**

O Art. 72 exige um sistema de monitorização pós-comercialização proporcional, com um plano documentado, que recolha e analise dados sobre o desempenho do sistema ao longo da sua vida, permitindo avaliar a conformidade contínua.

**Cobertura SbD-ToE**

| Requisito AI Act | Capítulo SbD-ToE | Cobertura |
|---|---|---|
| Recolha contínua de telemetria | Cap. 12 | Observabilidade, métricas |
| Análise de desempenho e degradação | Cap. 12 | Deteção de *drift* e anomalias |
| Melhoria contínua | Cap. 12 | Ciclo de melhoria, pós-incidente |

**O que o SbD-ToE cobre**

- Recolha e análise contínua de telemetria operacional (Cap. 12).
- Deteção de degradação de desempenho e *model drift* (Cap. 12).
- Ciclo de melhoria contínua e revisão (Cap. 12).

**Lacunas intencionais**

O SbD-ToE não define o **plano formal de monitorização pós-mercado** com a estrutura do Art. 72 nem os indicadores específicos de desempenho de IA a reportar à autoridade.

**Como cumprir**

Sugere-se formalizar um plano de monitorização pós-mercado assente na observabilidade do Cap. 12, com *dashboards* de desempenho, *drift* e estado de vulnerabilidades, e gatilhos de reavaliação que alimentem o ciclo do Art. 9.

---

### Artigo 73 - Comunicação de incidentes graves

**Conteúdo normativo**

O Art. 73 obriga os fornecedores a comunicar **incidentes graves** às autoridades de fiscalização do mercado, em prazos definidos — em regra **até 15 dias** após conhecimento; **até 10 dias** em caso de morte de uma pessoa; e **até 2 dias** em caso de infração generalizada ou de perturbação grave e irreversível de infraestrutura crítica (Art. 3.º, n.º 49, al. b)) — e a tomar medidas corretivas.

**Cobertura SbD-ToE**

| Requisito AI Act | Capítulo SbD-ToE | Cobertura |
|---|---|---|
| Deteção e resposta a incidentes | Cap. 12 | Processo de deteção, resposta, pós-incidente |
| Escalonamento e responsabilidades | Cap. 14 | Papéis e responsabilidades |
| Classificação de severidade | Cap. 01, Cap. 12 | Critérios de impacto, classificação |

**O que o SbD-ToE cobre**

- Processo de deteção, resposta e pós-incidente (Cap. 12).
- Papéis de escalonamento e responsabilidades (Cap. 14).
- Critérios de impacto que suportam a classificação de severidade (Cap. 01, Cap. 12).

**Lacunas intencionais**

O SbD-ToE não fixa a **definição regulamentar de "incidente grave"** do AI Act, nem os prazos (15 dias / 10 dias / 2 dias consoante a gravidade), templates de submissão ou o circuito para a autoridade competente. À semelhança de NIS2 e DORA, estes campos são deixados configuráveis.

**Como cumprir**

Sugere-se parametrizar o runbook e o esquema de incidente do Cap. 12 com a tipologia e prazos do Art. 73, e configurar exportadores do SIEM/ITSM para gerar a notificação pronta a submeter à autoridade de fiscalização do mercado.

---

### Modelos de IA de finalidade geral - Artigos 53 e 55 (GPAI)

**Conteúdo normativo**

O Art. 53 impõe aos fornecedores de **GPAI** documentação técnica do modelo, informação para integradores a jusante, política de respeito pelo direito de autor e um resumo dos dados de treino. O Art. 55 acresce, para GPAI com **risco sistémico**, a obrigação de **avaliação adversarial (*adversarial testing* / *red teaming*)**, avaliação e mitigação de riscos sistémicos, comunicação de incidentes graves e garantia de **cibersegurança adequada do modelo e da infraestrutura física**.

**Cobertura SbD-ToE**

| Requisito AI Act | Capítulo SbD-ToE | Cobertura |
|---|---|---|
| Avaliação adversarial / red teaming | Cap. 10 | Catálogo de testes (extensível a AI red teaming) |
| Cibersegurança do modelo e infraestrutura | Cap. 04, Cap. 08, Cap. 09 | Arquitetura, IaC, containers/runtime |
| Proteção de pesos e artefactos | Cap. 05, Cap. 04 | Integridade/proveniência, controlo de acesso |
| Monitorização e incidentes | Cap. 12 | Deteção, resposta |

**O que o SbD-ToE cobre**

- Base para **AI red teaming** contínuo (Cap. 10).
- **Cibersegurança da infraestrutura** que serve o modelo (Cap. 04, Cap. 08, Cap. 09).
- **Proteção de integridade e acesso** a pesos e artefactos do modelo, tratados como ativos críticos da cadeia (Cap. 05, Cap. 04).
- Monitorização e resposta (Cap. 12).

**Lacunas intencionais**

O SbD-ToE não prescreve a **documentação técnica GPAI** (Anexo XI/XII), a **política de copyright** nem o **resumo dos dados de treino** - são obrigações de domínio e jurídicas. A avaliação de **riscos sistémicos** (capacidades de impacto à escala) é igualmente externa ao AppSec.

**Como cumprir**

Sugere-se: tratar pesos, *checkpoints* e *datasets* como ativos de cadeia de fornecimento com proveniência e controlo de acesso (Cap. 05); instituir AI red teaming contínuo (Cap. 10) alinhado com o MITRE ATLAS; aplicar hardening de infraestrutura (Cap. 04/08/09); e remeter documentação GPAI, copyright e avaliação de risco sistémico para as equipas de IA, jurídico e compliance.

---

### Práticas proibidas e transparência (Artigos 5 e 50)

**Conteúdo normativo**

O Art. 5 proíbe um conjunto de práticas (p. ex., manipulação subliminar prejudicial, *social scoring* por entidades públicas, certa identificação biométrica remota em tempo real). O Art. 50 impõe deveres de transparência para sistemas de risco limitado (informar que se interage com IA; marcar conteúdo sintético / *deepfakes*).

**Cobertura SbD-ToE**

Ambos os artigos são **essencialmente de natureza jurídica e de conceção de produto**, fora do âmbito técnico-AppSec do SbD-ToE.

**Lacunas intencionais (por desenho)**

O SbD-ToE não determina a admissibilidade de uma finalidade (Art. 5) nem desenha os mecanismos de divulgação ao utilizador (Art. 50). Tecnicamente, pode suportar a **marcação de proveniência de conteúdo** (p. ex., *watermarking*/credenciais de conteúdo) quando essa decisão de produto for tomada.

**Como cumprir**

A determinação de proibições e os deveres de transparência devem ser conduzidos por jurídico e produto. O SbD-ToE entra apenas na **implementação técnica fiável** dos mecanismos escolhidos (integridade da marcação, registo auditável).

---

## PARTE II: SÍNTESE E REFERÊNCIAS

### Síntese da cobertura AI Act / SbD-ToE

O AI Act pede sistemas de IA **seguros, robustos, documentados e supervisionáveis**, com responsabilidade do fornecedor ao longo de todo o ciclo de vida. O SbD-ToE oferece o **coração técnico-operacional** desse esforço: gestão de risco técnico (Cap. 01, 03), arquitetura defensiva (Cap. 04), integridade da cadeia de dados e modelos (Cap. 05), pipelines e gates de qualidade (Cap. 06, 07, 11), testes e robustez adversarial (Cap. 10), logging e monitorização pós-mercado (Cap. 12) e governação (Cap. 14).

A cobertura mais **forte e direta** está no **Art. 15** (exatidão, robustez, cibersegurança) e nos seus correlatos operacionais (Art. 12 logging, Art. 72 monitorização, Art. 73 incidentes, Art. 17 QMS) - é aqui que "implementar SbD-ToE" se aproxima de "cumprir o AI Act".

As lacunas observadas **não são falhas do modelo**, mas **abstenções deliberadas**: dimensões próprias do domínio de IA (governação de dados/enviesamento, exatidão estatística, supervisão humana, transparência) e dimensões jurídicas (classificação de risco, FRIA, avaliação de conformidade, marcação CE, práticas proibidas). Estas exigem equipas de ciência de dados, ética, produto, jurídico e compliance - o SbD-ToE fornece-lhes a evidência técnica, não o juízo de conformidade.

O resultado é coerente com a filosofia do manual:

- **Hoje**, o SbD-ToE permite construir e operar o software de um sistema de IA com segurança por desenho.
- **Amanhã**, quando a organização tiver de cumprir o AI Act, liga os detalhes - estende o threat model ao vetor adversarial (ATLAS), formaliza o QMS (Art. 17), parametriza incidentes (Art. 73) e a monitorização pós-mercado (Art. 72), e articula com as equipas de domínio as dimensões de dados, supervisão e transparência.

### Âmbito, papéis e sanções

O AI Act distingue **fornecedores (providers)**, **utilizadores implementadores (deployers)**, importadores e distribuidores, com obrigações distintas. O grosso das obrigações técnicas (e da cobertura SbD-ToE) recai sobre o **fornecedor de sistema de alto risco**; o *deployer* tem obrigações próprias (uso conforme às instruções, supervisão humana, em certos casos FRIA - Art. 26, 27).

Em termos sancionatórios (Art. 99), o regulamento estabelece patamares máximos:

- **Práticas proibidas (Art. 5)**: até **35 M€** ou **7%** do volume de negócios anual mundial (o que for mais elevado).
- **Incumprimento de outras obrigações** (incluindo as do fornecedor de alto risco, Art. 16): até **15 M€** ou **3%**.
- **Informação incorreta, incompleta ou enganosa** a organismos notificados ou autoridades: até **7,5 M€** ou **1%**.
- Para fornecedores de **GPAI** (Art. 101): até **15 M€** ou **3%**.

### Referências

- **AI Act**: Regulamento (UE) 2024/1689 (CELEX: [32024R1689](https://eur-lex.europa.eu/legal-content/PT/TXT/?uri=CELEX:32024R1689)).
- **Art. 9** - Sistema de gestão de risco (ciclo de vida).
- **Art. 10** - Dados e governação de dados (representatividade, enviesamento).
- **Art. 11 e Anexo IV** - Documentação técnica.
- **Art. 12 / Art. 19** - Registo de eventos e conservação de logs.
- **Art. 13 / Art. 14** - Transparência aos deployers e supervisão humana.
- **Art. 15** - Exatidão, robustez e cibersegurança (resiliência a ataques adversariais).
- **Art. 17** - Sistema de gestão da qualidade.
- **Art. 72 / Art. 73** - Monitorização pós-comercialização e incidentes graves.
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

O AI Act, tal como NIS2 e DORA, beneficia de um processo formal de exceções à conformidade. Casos em que um requisito não é aplicável, ou em que se aceita um risco residual temporário (p. ex., um vetor adversarial mitigado por compensação enquanto se prepara o *retraining*), devem ser documentados, aprovados ao nível adequado e revistos periodicamente.

O Cap. 14 (Governança e Contratação) do SbD-ToE fornece os artefactos necessários: registo de exceções, critérios de aceitação de risco, cadeia de aprovação e plano de remediação. Note-se que certos desvios **não são exceptuáveis** no contexto AI Act - desde logo, qualquer uso que recaia nas práticas proibidas do Art. 5. A existência de um processo formal de exceções não é sinal de fragilidade: é evidência de governação madura e de controlo consciente sobre o perfil de risco.

:::

---

**Versão:** 1.0
**Data:** Maio 2026
**Próxima revisão:** Novembro 2026
