// Rótulos das 7 fases do Mapa do ciclo de vida (00-especificacao.md §10, chaves lifecycleMap.phase.*).
// A página mostra estes rótulos, e não os do índice: os do índice servem para a Verificação conferir.
// As chamadas a translate() têm de ter ids literais, para o write-translations as encontrar.
import {translate} from '@docusaurus/Translate';

export type FaseId =
  | 'planeamento'
  | 'design'
  | 'desenvolvimento'
  | 'build-ci'
  | 'release'
  | 'operacao'
  | 'transversal';

export type Fase = {id: FaseId; ordem: number; transversal: boolean; nome: string; descricao: string};

export function fases(): Fase[] {
  return [
    {
      id: 'planeamento',
      ordem: 1,
      transversal: false,
      nome: translate({id: 'lifecycleMap.phase.planeamento', message: 'Planeamento'}),
      descricao: translate({
        id: 'lifecycleMap.phase.planeamento.desc',
        message: 'Kick-off, classificação da aplicação, requisitos, backlog e priorização.',
      }),
    },
    {
      id: 'design',
      ordem: 2,
      transversal: false,
      nome: translate({id: 'lifecycleMap.phase.design', message: 'Design'}),
      descricao: translate({
        id: 'lifecycleMap.phase.design.desc',
        message: 'Arquitetura e threat modeling, com as suas revisões e aprovações.',
      }),
    },
    {
      id: 'desenvolvimento',
      ordem: 3,
      transversal: false,
      nome: translate({id: 'lifecycleMap.phase.desenvolvimento', message: 'Desenvolvimento'}),
      descricao: translate({
        id: 'lifecycleMap.phase.desenvolvimento.desc',
        message: 'Código, dependências, validações locais, pull requests e revisão de código.',
      }),
    },
    {
      id: 'build-ci',
      ordem: 4,
      transversal: false,
      nome: translate({id: 'lifecycleMap.phase.build-ci', message: 'Build e CI'}),
      descricao: translate({
        id: 'lifecycleMap.phase.build-ci.desc',
        message: 'Build, pipeline de CI/CD, scanners automáticos, SBOM e runners.',
      }),
    },
    {
      id: 'release',
      ordem: 5,
      transversal: false,
      nome: translate({id: 'lifecycleMap.phase.release', message: 'Release'}),
      descricao: translate({
        id: 'lifecycleMap.phase.release.desc',
        message: 'Staging, pré-release, gates de promoção, deploy e go-live.',
      }),
    },
    {
      id: 'operacao',
      ordem: 6,
      transversal: false,
      nome: translate({id: 'lifecycleMap.phase.operacao', message: 'Operação'}),
      descricao: translate({
        id: 'lifecycleMap.phase.operacao.desc',
        message: 'Produção, runtime, monitorização, incidentes, patching e retirada de serviço.',
      }),
    },
    {
      id: 'transversal',
      ordem: 7,
      transversal: true,
      nome: translate({id: 'lifecycleMap.phase.transversal', message: 'Transversal'}),
      descricao: translate({
        id: 'lifecycleMap.phase.transversal.desc',
        message:
          'Não é um momento do ciclo: governação, auditoria e conformidade, onboarding e formação de pessoas, e o ciclo contínuo (revisões periódicas ou por evento, exceções, KPIs).',
      }),
    },
  ];
}
