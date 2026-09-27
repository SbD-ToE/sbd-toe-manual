---
id: convergencia-dora
title: Nota - Convergência DORA & NIS2
description: Orientação para organizações potencialmente enquadradas simultaneamente por DORA e NIS2
sidebar_position: 4
tags: [dora, nis2, convergencia, lex-specialis, governação]
---

# Nota: Organizações abrangidas por DORA e NIS2

## Âmbito {#âmbito}

Esta nota destina-se a organizações do setor financeiro (bancos, seguradoras, infraestruturas de mercado, intermediários) que surgem listadas em transposições NIS2 mas são reguladas primariamente por DORA (Regulamento UE 2022/2554). Resume princípios de **lex specialis**, evita duplicação e orienta a integração no SbD-ToE.

O que o Manual cobre, as lacunas que declara e o que fica fora de âmbito, obrigação a obrigação, estão nas listas geradas de cada regime: [DORA — O que este Manual cobre e o que fica de fora](/sbd-toe/cross-check-normativo/dora/requisitos-aplicaveis#cobertura) e [NIS2 — O que este Manual cobre e o que fica de fora](/sbd-toe/cross-check-normativo/nis2/requisitos-aplicaveis#cobertura).

## Princípio Lex Specialis {#princípio-lex-specialis}

DORA é lex specialis para gestão de risco TIC, testes de resiliência e reporte de incidentes em entidades financeiras reguladas. Onde há sobreposição temática:

| Tema | NIS2 Artigos | DORA Artigos | Qual prevalece |
|------|--------------|--------------|----------------|
| Governação TIC | 20 | 5 | DORA (mais específico financeiro) |
| Gestão de risco técnico | 21 | 6–16 | DORA |
| Testes/Resiliência | 21 (genérico) | 24–27 (testes, incl. TLPT nos art. 26–27); 11 (continuidade) | DORA |
| Reporte de incidentes | 23 (24h/72h/1M) | 17–20 (classificação no art. 18; comunicação no art. 19; modelos RTS/ITS no art. 20) | DORA (formato / circuito supervisor) |
| Cadeia de fornecimento | 21 | 28–30 | DORA para terceiros prestadores de serviços de TIC (reforçado quando apoiam funções críticas ou importantes); NIS2 pode complementar requisitos gerais |
| Partilha de ameaças | 29 | 45 | DORA |

## O que continua relevante da NIS2 {#o-que-continua-relevante-da-nis2}

Mesmo sob DORA, aspetos NIS2 podem manter valor:
- Linguagem comum para interação com entidades essenciais/importantes não financeiras (ex.: saúde, energia) que dependem de serviços bancários.
- Expectativas de **all-hazards approach** ajudam a justificar a amplitude dos controlos. O SbD-ToE cobre a parte aplicacional; o ambiente físico, a continuidade do negócio e a gestão de crises ficam fora do seu âmbito.
- Requisitos nacionais sobre **pontos de contacto** ou **registos de dependências críticas** podem exigir harmonização documental.

## Riscos de Duplicação (Evitar) {#riscos-de-duplicação-evitar}

| Duplicação potencial | Porque evitar | Forma única recomendada |
|----------------------|---------------|--------------------------|
| Dois fluxos de reporte (incidentes) | Risco de inconsistência de prazos/dados | Adotar fluxo DORA; mapear campos NIS2 como subset |
| Dois catálogos de controlos | Overhead, divergência textual | Usar o catálogo SbD-ToE; a origem regulatória de cada piso e de cada requisito acrescentado está no overlay regulatório (`_contextos-regulatorios.yaml`) e nas páginas «Requisitos aplicáveis» |
| Duas classificações de criticidade | Confusão em matrizes de risco | Manter L1–L3 por aplicação (eixos do Cap. 01). Os regimes não criam classes paralelas: acrescentam pisos por contexto (CTX-DORA, CTX-NIS2) e por grau (FCI no DORA; PERTINENTE na NIS2). L1–L3 não equivale a função crítica ou importante nem a entidade essencial ou importante |
| Logs com retenções diferentes | Custos e ambiguidade | Definir e documentar o período de conservação por tipo de registo com base na avaliação do risco TIC (DORA: Reg. Delegado (UE) 2024/1774, art. 12.º, n.º 2, al. a); NIS2: Reg. de Execução (UE) 2024/2690, anexo, ponto 3.2.5, quando aplicável; legislação nacional/setorial), aplicando um prazo único que satisfaça ambos e respeite a limitação da conservação do RGPD quando haja dados pessoais |

## Estratégia de Implementação Única (SbD-ToE) {#estratégia-de-implementação-única-sbd-toe}

1. **Política mestra de Resiliência Digital** - Integra governação, testes, reporte e fornecedores (referencia DORA Art. 5–6, 17–20, 24–27, 28–30; nota que, nos termos do art. 4.º da NIS2 e do art. 1.º, n.º 2, do DORA, as obrigações NIS2 de gestão de riscos e notificação não se aplicam às entidades financeiras abrangidas).
2. **Origem regulatória** - O catálogo de requisitos ([Cap. 02](/sbd-toe/sbd-manual/requisitos-seguranca/intro)) não tem coluna de origem regulatória: a origem de cada piso e de cada requisito acrescentado está no overlay regulatório (`_contextos-regulatorios.yaml`) e nas páginas «Requisitos aplicáveis» de cada regime, geradas dele.
3. **Registo de incidente** - Dados de impacto comuns (Política 32 §4.3); o critério e o conteúdo seguem o DORA (CTX-DORA-R02; Política 32 §6.1, com os modelos do Reg. de Execução (UE) 2025/302); os campos NIS2 ficam como anotação para os clientes que os peçam.
4. **Processo de exceções** - Alçadas da Política 05 §6 (no Manual, o topo é o CISO, e o Critical não é aceitável em L3). A supervisão das exceções L3 pelo órgão de administração é formalização da entidade: fica fora do âmbito do Manual no DORA (art. 5.º) e é lacuna declarada face à NIS2.
5. **Inventário de fornecedores** - Unificar: SBOM (componentes), contractors ([Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro)), terceiros prestadores de serviços de TIC que apoiam funções críticas ou importantes (marcar se exigidos por DORA ou por clientes NIS2).
6. **Formação** - A Política 37 cobre as funções técnicas. A formação do órgão de administração (DORA art. 5.º, n.º 4; NIS2 art. 20.º, n.º 2) e a do pessoal não técnico são da entidade: fora do âmbito do Manual no DORA e lacuna declarada na NIS2. Uma trilha, duas etiquetas.

## Checklist de Convergência (SIM = pronto) {#checklist-de-convergência-sim--pronto}

- [ ] Origem regulatória de cada piso e requisito acrescentado confirmada no overlay (páginas «Requisitos aplicáveis» do DORA e da NIS2).
- [ ] Política mestra inclui secção "Lex Specialis: DORA como ato setorial (NIS2 art. 4.º; DORA art. 1.º, n.º 2) — obrigações NIS2 de gestão de riscos e notificação (e respetiva supervisão) não aplicáveis".
- [ ] Registo de incidentes com os dados de impacto da Política 32 §4.3 e o conteúdo DORA da §6.1; campos NIS2 como anotação.
- [ ] Retenção de logs definida por tipo de registo, com um prazo único que satisfaça DORA e NIS2 e fundamentado na avaliação de risco (no SbD-ToE, em L3: 2 anos para logs de segurança e 3 anos para auditoria, escolha do Manual).
- [ ] Inventário de fornecedores indica criticidade + origem regulatória.
- [ ] Formação anual da gestão registada pela entidade (conteúdos DORA e NIS2 integrados; fora do Manual).
- [ ] Processo formal de exceções (Política 05), com reporte periódico das exceções L3 ao órgão de administração definido pela entidade.
- [ ] Não existem playbooks paralelos divergentes (apenas anotações de diferenças).

## Perguntas Frequentes {#perguntas-frequentes}

**Q1. Preciso reportar incidente duas vezes?**  
Não. Segue circuito DORA. Se autoridade nacional exigir visão agregada NIS2, reutiliza export do formato DORA.

**Q2. E se fornecedor não financeiro invoca NIS2?**  
Mapeia exigência do fornecedor a controlo já satisfeito por DORA; envia SoA com origem regulatória.

**Q3. Logs de 1 ano bastam para NIS2?**  
Nem o DORA nem a NIS2 fixam um número: no DORA, a entidade estabelece o período de conservação tendo em conta a avaliação do risco associado às TIC (Reg. Delegado (UE) 2024/1774, art. 12.º, n.º 2); o Reg. de Execução (UE) 2024/2690 pede que os registos sejam mantidos «durante um período predefinido» (anexo, ponto 3.2.5). Para convergência, um prazo único por tipo de registo reduz discussões — no SbD-ToE, 2 anos para logs de segurança e 3 anos para auditoria em L3 (escolha do Manual). Documentar o racional.

**Q4. TLPT vs. testes NIS2?**  
Executar o TLPT, quando a autoridade o exija, é evidência forte da avaliação da eficácia, mas não a esgota: a NIS2 (art. 21.º, n.º 2, al. f)) pede a avaliação das medidas no seu conjunto. Para a entidade financeira abrangida, conta o programa de testes do DORA (arts. 24.º–27.º), como ato setorial.

## Referências {#referências}

- Regulamento (UE) 2022/2554 (DORA)
- Diretiva (UE) 2022/2555 (NIS2) Anexos I/II
- ENISA - Orientações técnicas NIS2 (2024/2025)
- SbD-ToE Manual ([Cap. 01](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)–[Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro))

## Nota Final {#nota-final}

SbD-ToE já abstrai controlos técnicos. A convergência DORA/NIS2 concretiza-se ao **anotar origem regulatória** e usar sempre a forma **mais exigente** como baseline - evitando redundância e mantendo elegância operacional.
