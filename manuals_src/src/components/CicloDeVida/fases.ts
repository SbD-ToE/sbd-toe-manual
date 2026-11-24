// Rótulos das 7 fases do Mapa do ciclo de vida (00-especificacao.md §10, chaves lifecycleMap.phase.*).
// A página mostra estes rótulos, e não os do índice: os do índice servem para a Verificação conferir.
// As chamadas a translate() têm de ter ids literais, para o write-translations as encontrar.
// As fases e os eventos da vista ágil (eventos.ts) são colunas do mesmo tipo (00-especificacao-agil.md §4.3).
import {translate} from '@docusaurus/Translate';

// marca: o que se lê no círculo da coluna ('1'…'6', '∞' na Transversal, '' nas colunas fora do Scrum);
// fora: coluna à parte, tracejada (a Transversal; Operação e Cadência organizacional na vista ágil)
export type Coluna = {id: string; ordem: number; fora: boolean; marca: string; nome: string; descricao: string};

export type FaseId =
  | 'planeamento'
  | 'design'
  | 'desenvolvimento'
  | 'build-ci'
  | 'release'
  | 'operacao'
  | 'transversal';

export type Fase = Coluna & {id: FaseId};

export function fases(): Fase[] {
  return [
    {
      id: 'planeamento',
      ordem: 1,
      fora: false,
      marca: '1',
      nome: translate({id: 'lifecycleMap.phase.planeamento', message: 'Planeamento'}),
      descricao: translate({
        id: 'lifecycleMap.phase.planeamento.desc',
        message: 'Kick-off, classificação da aplicação, requisitos, backlog e priorização.',
      }),
    },
    {
      id: 'design',
      ordem: 2,
      fora: false,
      marca: '2',
      nome: translate({id: 'lifecycleMap.phase.design', message: 'Design'}),
      descricao: translate({
        id: 'lifecycleMap.phase.design.desc',
        message: 'Arquitetura e threat modeling, com as suas revisões e aprovações.',
      }),
    },
    {
      id: 'desenvolvimento',
      ordem: 3,
      fora: false,
      marca: '3',
      nome: translate({id: 'lifecycleMap.phase.desenvolvimento', message: 'Desenvolvimento'}),
      descricao: translate({
        id: 'lifecycleMap.phase.desenvolvimento.desc',
        message: 'Código, dependências, validações locais, pull requests e revisão de código.',
      }),
    },
    {
      id: 'build-ci',
      ordem: 4,
      fora: false,
      marca: '4',
      nome: translate({id: 'lifecycleMap.phase.build-ci', message: 'Build e CI'}),
      descricao: translate({
        id: 'lifecycleMap.phase.build-ci.desc',
        message: 'Build, pipeline de CI/CD, scanners automáticos, SBOM e runners.',
      }),
    },
    {
      id: 'release',
      ordem: 5,
      fora: false,
      marca: '5',
      nome: translate({id: 'lifecycleMap.phase.release', message: 'Release'}),
      descricao: translate({
        id: 'lifecycleMap.phase.release.desc',
        message: 'Staging, pré-release, gates de promoção, deploy e go-live.',
      }),
    },
    {
      id: 'operacao',
      ordem: 6,
      fora: false,
      marca: '6',
      nome: translate({id: 'lifecycleMap.phase.operacao', message: 'Operação'}),
      descricao: translate({
        id: 'lifecycleMap.phase.operacao.desc',
        message: 'Produção, runtime, monitorização, incidentes, patching e retirada de serviço.',
      }),
    },
    {
      id: 'transversal',
      ordem: 7,
      fora: true,
      marca: '∞',
      nome: translate({id: 'lifecycleMap.phase.transversal', message: 'Transversal'}),
      descricao: translate({
        id: 'lifecycleMap.phase.transversal.desc',
        message:
          'Não é um momento do ciclo: governação, auditoria e conformidade, onboarding e formação de pessoas, e o ciclo contínuo (revisões periódicas ou por evento, exceções, KPIs).',
      }),
    },
  ];
}
