---
id: epss-kev-priorizacao
title: Priorização de Vulnerabilidades com EPSS e KEV
description: Camada de priorização de remediação assente em probabilidade de exploração (EPSS, FIRST.org) e exploração confirmada (CISA KEV), aplicada sobre os SLAs de patching baseados em CVSS. EPSS e KEV refinam a ordem de remediação; os SLAs por severidade mantêm-se como piso obrigatório.
tags: [EPSS, KEV, CVSS, priorizacao, vulnerabilidades, patching, SLA, remediacao, CISA, FIRST, L2, L3]
sidebar_position: 12
---

<!--template: sbdtoe-addon -->

# Priorização de Vulnerabilidades com EPSS e KEV

## Âmbito e propósito

O CVSS mede a **severidade** de uma vulnerabilidade — o impacto potencial se for explorada — mas não mede a **probabilidade** de essa exploração ocorrer, nem se já está a acontecer. Um SLA de patching assente apenas em CVSS trata todas as vulnerabilidades de severidade igual como igualmente urgentes, quando a evidência de exploração as separa de forma decisiva.

Este addon integra duas fontes que acrescentam essa dimensão em falta:

- **EPSS** (*Exploit Prediction Scoring System*), mantido pelo EPSS SIG da FIRST.org: estima a probabilidade de uma vulnerabilidade ser explorada *in the wild* nos 30 dias seguintes.
- **KEV** (*Known Exploited Vulnerabilities*), o catálogo da CISA: lista vulnerabilidades com evidência de exploração ativa confirmada.

EPSS e KEV entram como **camada de priorização sobre o CVSS**, não como substituição. Os SLAs de patching por severidade definidos no programa mantêm-se como **piso obrigatório**: EPSS e KEV podem **antecipar** a remediação de um item, nunca **adiá-la** para além do prazo que a severidade já impõe.

Aplicabilidade: **L2 e L3**. Sistemas L1 mantêm a priorização por severidade; a camada EPSS/KEV é recomendada onde o volume de vulnerabilidades excede a capacidade de remediação imediata e exige ordenação criteriosa.

> Esta integração segue o princípio de **referência ancorada**: EPSS e KEV são instrumentos de ordenação de risco, não uma autoridade que se sobrepõe ao CVSS, ao SLA contratual ou à decisão formal de aceitação de risco. Nenhum dos dois converte severidade em prioridade de forma automática.

---

## EPSS — probabilidade de exploração

O EPSS atribui a cada CVE um valor entre **0 e 1**, correspondente à probabilidade estimada de exploração nos 30 dias seguintes, e um **percentil** que posiciona esse CVE face a todos os outros. O modelo é atualizado **diariamente** a partir de dados de exploração observados e de características da própria vulnerabilidade.

Propriedades a reter na sua utilização:

- O EPSS é **preditivo e probabilístico**. Um valor alto indica risco elevado de exploração iminente; um valor baixo **não constitui garantia** de que a vulnerabilidade não será explorada.
- O EPSS é **complementar ao CVSS**, não alternativo. Mede uma dimensão diferente — likelihood, não impacto.
- O valor muda ao longo do tempo. A priorização deve consultar o EPSS **no momento da decisão**, não um valor capturado meses antes.

O threshold de EPSS que aciona escalonamento deve ser definido pela organização em função da sua capacidade de remediação. Um threshold de referência inicial situa-se no percentil ≥ 0,95 (entre os 5% de CVEs com maior probabilidade de exploração), a calibrar com a experiência operacional.

---

## KEV — exploração confirmada

O catálogo KEV da CISA, estabelecido pela *Binding Operational Directive* 22-01, lista vulnerabilidades para as quais existe **evidência de exploração ativa**. Cada entrada inclui um prazo de remediação vinculativo para as agências federais norte-americanas, e funciona como sinal autoritativo de exploração real para qualquer organização.

A presença de um CVE no KEV altera a natureza da decisão:

- Uma vulnerabilidade no KEV deixou de ser um risco hipotético — está a ser explorada. **Deve ser escalada para o prazo de remediação mais curto do programa, independentemente do seu CVSS ou EPSS.**
- A **ausência** de um CVE no KEV **não significa ausência de exploração** — significa apenas que não há, ainda, exploração confirmada e catalogada. A ausência do KEV não é prova de segurança.

---

## Integração na priorização de remediação

A ordem de remediação resulta da composição de três sinais: severidade (CVSS), probabilidade (EPSS) e exploração confirmada (KEV). O SLA por severidade fixa o prazo máximo; EPSS e KEV determinam o que se remedia **primeiro** dentro e abaixo desse prazo.

| Sinal | Condição | Efeito na priorização |
|-------|----------|-----------------------|
| KEV | CVE presente no catálogo | Escalonamento imediato para o prazo mais curto, qualquer que seja o CVSS |
| EPSS alto + CVSS alto | Acima do threshold definido | Topo da fila de remediação dentro do SLA |
| EPSS alto + CVSS baixo/médio | Acima do threshold | Antecipar face a outros itens de severidade igual |
| EPSS baixo + CVSS alto | Abaixo do threshold | Mantém o SLA por severidade como piso; não desprioriza abaixo dele |
| EPSS baixo + CVSS baixo | Abaixo do threshold | Remediação dentro do SLA normal, sem antecipação |

A regra de fecho é a que protege o piso: **a camada EPSS/KEV nunca atrasa uma remediação para além do prazo que a severidade já impõe.** Antecipa; não adia.

---

## Disciplina epistémica

- O EPSS é uma **estimativa**, não uma medição de certeza. Decisões de risco assentes nele devem registar que o valor é probabilístico e datado.
- O KEV é um sinal **incompleto por construção** — cataloga exploração *confirmada*, não toda a exploração existente.
- Nenhuma das fontes dispensa o **registo formal de exceção** quando uma vulnerabilidade não é remediada dentro do SLA (ver referências cruzadas). EPSS baixo não é, por si, justificação de exceção.

---

## Referências cruzadas

| Documento | Relação |
|-----------|---------|
| [Cap. 05 — Análise SCA](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/analise-sca) | Deteção de vulnerabilidades em dependências, fonte primária de CVEs a priorizar |
| [Cap. 05 — Excepções e aceitação de risco](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/excecoes-e-aceitacao-risco) | Processo formal quando a remediação excede o SLA |
| [Cap. 10 — Cobertura e priorização](/sbd-toe/sbd-manual/testes-seguranca/addon/cobertura-e-priorizacao) | Priorização de esforço de teste por risco |
| [Cap. 12 — Alertas e eventos críticos](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/alertas-eventos-criticos) | SLAs de resposta operacional onde a priorização se materializa |

> **Sobre a curadoria:** Consolidado a partir de EPSS (FIRST.org EPSS SIG), CISA KEV (*Binding Operational Directive* 22-01), CVSS (FIRST.org) e NIST SP 800-40 Rev. 4 (*Patch Management*). EPSS e KEV são fontes externas atualizadas continuamente; os valores devem ser consultados no momento da decisão de priorização. Esta integração é metodológica — não substitui os SLAs de patching nem a decisão formal de aceitação de risco do programa.
