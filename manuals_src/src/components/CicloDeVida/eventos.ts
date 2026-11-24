// Colunas da vista ágil do Mapa do ciclo de vida (00-especificacao-agil.md §4.2 e §5, chaves lifecycleMap.event.*):
// os 6 eventos do Scrum, numerados, e Operação e Cadência organizacional, fora do Scrum (tracejadas, sem número).
// Como em fases.ts, a página mostra estes rótulos e não os do índice, e as chamadas a translate() têm ids literais.
import {translate} from '@docusaurus/Translate';
import type {Coluna} from './fases';

export type EventoId =
  | 'refinamento'
  | 'sprint-planning'
  | 'sprint'
  | 'dod'
  | 'sprint-review'
  | 'retrospetiva'
  | 'operacao'
  | 'cadencia';

export type Evento = Coluna & {id: EventoId};

export function eventos(): Evento[] {
  return [
    {
      id: 'refinamento',
      ordem: 1,
      fora: false,
      marca: '1',
      nome: translate({id: 'lifecycleMap.event.refinamento', message: 'Refinamento do backlog'}),
      descricao: translate({
        id: 'lifecycleMap.event.refinamento.desc',
        message:
          'Preparar os itens antes de entrarem num sprint: arranque e classificação da aplicação, requisitos de segurança nos cartões, threat modeling e arquitetura, e a reavaliação quando algo muda.',
      }),
    },
    {
      id: 'sprint-planning',
      ordem: 2,
      fora: false,
      marca: '2',
      nome: translate({id: 'lifecycleMap.event.sprint-planning', message: 'Sprint Planning'}),
      descricao: translate({
        id: 'lifecycleMap.event.sprint-planning.desc',
        message:
          'Escolher o trabalho do sprint com os critérios de segurança e a capacidade para os cumprir: requisitos prontos, stack e ferramentas definidas.',
      }),
    },
    {
      id: 'sprint',
      ordem: 3,
      fora: false,
      marca: '3',
      nome: translate({id: 'lifecycleMap.event.sprint', message: 'Sprint'}),
      descricao: translate({
        id: 'lifecycleMap.event.sprint.desc',
        message:
          'Desenvolvimento e CI, com o Daily Scrum: código, dependências, pull requests e revisão de código, pipeline, scanners, SBOM e findings.',
      }),
    },
    {
      id: 'dod',
      ordem: 4,
      fora: false,
      marca: '4',
      nome: translate({id: 'lifecycleMap.event.dod', message: 'Definition of Done'}),
      descricao: translate({
        id: 'lifecycleMap.event.dod.desc',
        message:
          'O que o Increment tem de cumprir para estar feito e poder ir para produção: gates de segurança, staging e pré-release, aprovação da promoção e deploy.',
      }),
    },
    {
      id: 'sprint-review',
      ordem: 5,
      fora: false,
      marca: '5',
      nome: translate({id: 'lifecycleMap.event.sprint-review', message: 'Sprint Review'}),
      descricao: translate({
        id: 'lifecycleMap.event.sprint-review.desc',
        message:
          'Mostrar o resultado do sprint e verificar, com os stakeholders, os critérios de segurança e a evidência recolhida. Não é um gate de release.',
      }),
    },
    {
      id: 'retrospetiva',
      ordem: 6,
      fora: false,
      marca: '6',
      nome: translate({id: 'lifecycleMap.event.retrospetiva', message: 'Retrospetiva'}),
      descricao: translate({
        id: 'lifecycleMap.event.retrospetiva.desc',
        message:
          'Rever como correu o sprint, com os processos, as ferramentas e a Definition of Done: as revisões da equipa com período até mensal.',
      }),
    },
    {
      id: 'operacao',
      ordem: 7,
      fora: true,
      marca: '',
      nome: translate({id: 'lifecycleMap.event.operacao', message: 'Operação'}),
      descricao: translate({
        id: 'lifecycleMap.event.operacao.desc',
        message:
          'Fora do Scrum: produção e runtime, monitorização, incidentes, drift, patching, revogação e retirada de serviço.',
      }),
    },
    {
      id: 'cadencia',
      ordem: 8,
      fora: true,
      marca: '',
      nome: translate({id: 'lifecycleMap.event.cadencia', message: 'Cadência organizacional'}),
      descricao: translate({
        id: 'lifecycleMap.event.cadencia.desc',
        message:
          'Fora do Scrum: o que corre ao ritmo da organização e não do sprint, como governação e políticas, auditoria e conformidade, exceções, fornecedores e contratos, formação e onboarding, e revisões trimestrais a anuais.',
      }),
    },
  ];
}
