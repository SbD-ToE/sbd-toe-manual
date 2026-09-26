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
- Expectativas de **all-hazards approach** ajudam a justificar amplitude dos controlos (já presentes no SbD-ToE).
- Requisitos nacionais sobre **pontos de contacto** ou **registos de dependências críticas** podem exigir harmonização documental.

## Riscos de Duplicação (Evitar) {#riscos-de-duplicação-evitar}

| Duplicação potencial | Porque evitar | Forma única recomendada |
|----------------------|---------------|--------------------------|
| Dois fluxos de reporte (incidentes) | Risco de inconsistência de prazos/dados | Adotar fluxo DORA; mapear campos NIS2 como subset |
| Dois catálogos de controlos | Overhead, divergência textual | Usar catálogo SbD-ToE + marcar origem (DORA/NIS2/ISO) |
| Duas classificações de criticidade | Confusão em matrizes de risco | Manter L1–L3 SbD-ToE; documentar que atende classes DORA & NIS2 |
| Logs com retenções diferentes | Custos e ambiguidade | Definir e documentar o período de conservação por tipo de registo com base na avaliação do risco TIC (DORA: Reg. Delegado (UE) 2024/1774, art. 12.º, n.º 2, al. a); NIS2: Reg. de Execução (UE) 2024/2690, anexo, ponto 3.2.5, quando aplicável; legislação nacional/setorial), aplicando um prazo único que satisfaça ambos e respeite a limitação da conservação do RGPD quando haja dados pessoais |

## Estratégia de Implementação Única (SbD-ToE) {#estratégia-de-implementação-única-sbd-toe}

1. **Política mestra de Resiliência Digital** - Integra governação, testes, reporte e fornecedores (referencia DORA Art. 5–6, 17–20, 24–27, 28–30; nota que, nos termos do art. 4.º da NIS2 e do art. 1.º, n.º 2, do DORA, as obrigações NIS2 de gestão de riscos e notificação não se aplicam às entidades financeiras abrangidas).
2. **Matriz de origem regulatória** - Para cada requisito técnico ([Cap. 02](/sbd-toe/sbd-manual/requisitos-seguranca/intro)), nova coluna `Fonte` com enum: `DORA`, `NIS2`, `Ambas`, `Outras`.
3. **Esquema de incidente** - Base = DORA RTS/ITS; marcar campos adicionais NIS2 (ex.: impacto significativo na prestação dos serviços) como opcionais.
4. **Processo de exceções** - Escalonamento L3 sempre com supervisão board (cobre governance DORA & NIS2 simultaneamente).
5. **Inventário de fornecedores** - Unificar: SBOM (componentes), contractors ([Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro)), terceiros prestadores de serviços de TIC que apoiam funções críticas ou importantes (marcar se exigidos por DORA ou por clientes NIS2).
6. **Formação** - Módulo anual board (DORA governance) + módulo ciber all-hazards (NIS2) integrados; uma trilha, duas etiquetas.

## Checklist de Convergência (SIM = pronto) {#checklist-de-convergência-sim--pronto}

- [ ] Catálogo de requisitos SbD-ToE tem coluna `Fonte` preenchida.
- [ ] Política mestra inclui secção "Lex Specialis: DORA como ato setorial (NIS2 art. 4.º; DORA art. 1.º, n.º 2) — obrigações NIS2 de gestão de riscos e notificação (e respetiva supervisão) não aplicáveis".
- [ ] Esquema de incidentes baseado em RTS/ITS DORA, com campos NIS2 opcionais.
- [ ] Retenção de logs definida ≥3 anos (justificada como cobrindo ambas).
- [ ] Inventário de fornecedores indica criticidade + origem regulatória.
- [ ] Formação anual da gestão registada (conteúdos DORA + NIS2 integrados).
- [ ] Processo formal de exceções com aprovação board para L3.
- [ ] Não existem playbooks paralelos divergentes (apenas anotações de diferenças).

## Perguntas Frequentes {#perguntas-frequentes}

**Q1. Preciso reportar incidente duas vezes?**  
Não. Segue circuito DORA. Se autoridade nacional exigir visão agregada NIS2, reutiliza export do formato DORA.

**Q2. E se fornecedor não financeiro invoca NIS2?**  
Mapeia exigência do fornecedor a controlo já satisfeito por DORA; envia SoA com origem regulatória.

**Q3. Logs de 1 ano bastam para NIS2?**  
Para convergência, manter 3+ anos (DORA) reduz discussões. Documentar racional.

**Q4. TLPT vs. testes NIS2?**  
Executar TLPT (se aplicável) satisfaz e supera a exigência genérica NIS2 de avaliação de eficácia.

## Referências {#referências}

- Regulamento (UE) 2022/2554 (DORA)
- Diretiva (UE) 2022/2555 (NIS2) Anexos I/II
- ENISA - Orientações técnicas NIS2 (2024/2025)
- SbD-ToE Manual ([Cap. 01](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)–[Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro))

## Nota Final {#nota-final}

SbD-ToE já abstrai controlos técnicos. A convergência DORA/NIS2 concretiza-se ao **anotar origem regulatória** e usar sempre a forma **mais exigente** como baseline - evitando redundância e mantendo elegância operacional.
