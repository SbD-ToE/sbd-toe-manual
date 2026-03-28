# Introduzir controlos de governação de repositórios e plataformas de desenvolvimento no manual SbD-ToE

## Contexto

O manual SbD-ToE descreve práticas de engenharia segura e governação de segurança ao longo do ciclo de vida de desenvolvimento.

No entanto, atualmente o manual não contém uma prescrição canónica suficientemente explícita sobre **controlos de governação de repositórios e plataformas de desenvolvimento**, como GitHub, GitLab ou plataformas equivalentes.

Na prática, muitos dos controlos DevSecOps relevantes acontecem **antes mesmo do pipeline CI/CD**, ao nível do próprio repositório e da plataforma:

- branch protection
- pull requests obrigatórios
- resolução de conversas
- checks obrigatórios
- política de merge
- code scanning
- secret scanning
- dependabot / gestão de dependências
- permissões de Actions
- regras de release e tagging
- CODEOWNERS
- labels e templates

Estes controlos são hoje parte fundamental de qualquer prática moderna de engenharia segura e devem ser explicitamente tratados no SbD-ToE.

Além disso, o manual está a evoluir para suportar **operacionalização através de tools MCP**, o que exige que certas práticas estejam descritas de forma suficientemente clara e estruturada para poderem ser traduzidas em automação.

## Pedido

Atualizar o manual SbD-ToE para incluir um conjunto canónico de **controlos de governação de repositórios e plataformas de desenvolvimento**, incluindo:

1. definição dos controlos recomendados
2. aplicabilidade por tipo de repositório
3. proporcionalidade por nível de risco (`L1`, `L2`, `L3`)
4. papéis responsáveis
5. evidência esperada
6. artefactos/configurações correspondentes

Os controlos devem ser descritos de forma **plataforma-agnóstica**, com exemplos concretos (por exemplo GitHub) apenas como implementação.

Os controlos devem incluir, entre outros:

- proteção da branch principal
- pull requests obrigatórios
- resolução de conversas antes de merge
- checks obrigatórios
- branch atualizada antes de merge
- política de histórico (ex: linear history)
- proibição de force push
- proibição de delete da branch principal
- CODEOWNERS
- labels mínimas e templates
- dependabot / gestão de dependências
- code scanning
- secret scanning e push protection
- permissões prudentes de CI/CD
- política de releases e versionamento

O conteúdo deve indicar claramente:

- quando o controlo é **obrigatório**
- quando é **recomendado**
- quando pode ter **exceções justificadas**

## Artefactos relevantes

Manual localizado em:


manuals_src/docs/sbd-toe


Estrutura típica dos capítulos:

- `intro.md`
- `addon/`
- `canon/`

Especial atenção a:

- `canon/15-aplicacao-lifecycle.md`
- `canon/20-checklist-revisao.md`
- `canon/50-ameacas-mitigadas.md`
- `canon/60-policies-relevantes.md`

## Restrições

- Não introduzir conteúdo redundante com capítulos já existentes.
- Manter coerência com o modelo SbD-ToE (o quê, porquê, quem, quando, como, evidência).
- Manter separação entre prescrição canónica e exemplos.
- Não introduzir dependência exclusiva de uma plataforma específica.
- Garantir consistência com a classificação de risco `L1`, `L2`, `L3`.

## Resultado esperado

1. definição clara de controlos de governação de repositórios
2. integração coerente com o modelo SbD-ToE existente
3. identificação de evidência esperada para auditoria ou verificação
4. conteúdo adequado para posterior consumo por tools MCP