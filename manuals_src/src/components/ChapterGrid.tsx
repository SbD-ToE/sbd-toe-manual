import React from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import {translate} from '@docusaurus/Translate';
import styles from './ChapterGrid.module.css';

// Grelha dos 15 capítulos na página inicial (M-42, H-05). Títulos, descrições e tipos são as
// chaves manualIndex.* do Índice do Manual (docs/sbd-toe/010-sbd-manual/index.mdx), com o
// mesmo texto PT; os ids ficam escritos por extenso para o write-translations os encontrar.

type Kind = 'basilar' | 'operacional' | 'organizacional';

type Chapter = {
  n: string;
  slug: string;
  kind?: Kind;
  title: string;
  desc: string;
};

function chapters(): Chapter[] {
  return [
    {n: '00', slug: 'fundamentos',
      title: translate({id: 'doc.eyebrow.chapter.00.title', message: 'Fundamentos'}),
      desc: translate({id: 'homepage.chapters.00.desc', message: 'Como usar o manual, papéis, baseline e macro-processos'})},
    {n: '01', slug: 'classificacao-aplicacoes', kind: 'basilar',
      title: translate({id: 'manualIndex.chapter.01.title', message: 'Classificação das Aplicações'}),
      desc: translate({id: 'manualIndex.chapter.01.desc', message: 'Critérios de criticidade (exposição, dados, impacto) para controlos proporcionais e rastreabilidade'})},
    {n: '02', slug: 'requisitos-seguranca', kind: 'basilar',
      title: translate({id: 'manualIndex.chapter.02.title', message: 'Requisitos de Segurança'}),
      desc: translate({id: 'manualIndex.chapter.02.desc', message: 'Catálogo prescritivo e validações por nível de risco, alinhado com DSOMM/SSDF/SAMM'})},
    {n: '03', slug: 'threat-modeling', kind: 'basilar',
      title: translate({id: 'manualIndex.chapter.03.title', message: 'Threat Modeling'}),
      desc: translate({id: 'manualIndex.chapter.03.desc', message: 'Identificação de ameaças e cenários de abuso com STRIDE/LINDDUN, ligação a requisitos e testes'})},
    {n: '04', slug: 'arquitetura-segura', kind: 'basilar',
      title: translate({id: 'manualIndex.chapter.04.title', message: 'Arquitetura Segura'}),
      desc: translate({id: 'manualIndex.chapter.04.desc', message: 'Padrões e decisões de arquitetura (ADR) alinhadas a riscos e requisitos'})},
    {n: '05', slug: 'dependencias-sbom-sca', kind: 'operacional',
      title: translate({id: 'manualIndex.chapter.05.title', message: 'Dependências, SBOM e SCA'}),
      desc: translate({id: 'manualIndex.chapter.05.desc', message: 'Gestão de componentes, SBOM e SCA com exceções governadas e rastreáveis'})},
    {n: '06', slug: 'desenvolvimento-seguro', kind: 'operacional',
      title: translate({id: 'manualIndex.chapter.06.title', message: 'Desenvolvimento Seguro'}),
      desc: translate({id: 'manualIndex.chapter.06.desc', message: 'Práticas de codificação segura, revisões de código e validações no fluxo de trabalho'})},
    {n: '07', slug: 'cicd-seguro', kind: 'operacional',
      title: translate({id: 'manualIndex.chapter.07.title', message: 'CI/CD Seguro'}),
      desc: translate({id: 'manualIndex.chapter.07.desc', message: 'Pipeline como produto: isolamento, assinaturas, promoções e integridade ponta-a-ponta'})},
    {n: '08', slug: 'iac-infraestrutura', kind: 'operacional',
      title: translate({id: 'manualIndex.chapter.08.title', message: 'Infraestrutura como Código (IaC)'}),
      desc: translate({id: 'manualIndex.chapter.08.desc', message: 'Aplicação do SbD a infraestrutura e ambientes com automação rastreável'})},
    {n: '09', slug: 'containers-imagens', kind: 'operacional',
      title: translate({id: 'manualIndex.chapter.09.title', message: 'Containers e Imagens'}),
      desc: translate({id: 'manualIndex.chapter.09.desc', message: 'Endurecimento, registos confiáveis, política de publicação e execução segura'})},
    {n: '10', slug: 'testes-seguranca', kind: 'operacional',
      title: translate({id: 'manualIndex.chapter.10.title', message: 'Testes de Segurança'}),
      desc: translate({id: 'manualIndex.chapter.10.desc', message: 'Estratégia de verificação L1–L3: SAST, DAST, IAST, fuzzing, análise semântica'})},
    {n: '11', slug: 'deploy-seguro', kind: 'operacional',
      title: translate({id: 'manualIndex.chapter.11.title', message: 'Deploy Seguro'}),
      desc: translate({id: 'manualIndex.chapter.11.desc', message: 'Lançamentos controlados, reversibilidade, feature flags e evidências de segurança'})},
    {n: '12', slug: 'monitorizacao-operacoes', kind: 'operacional',
      title: translate({id: 'manualIndex.chapter.12.title', message: 'Monitorização e Operações'}),
      desc: translate({id: 'manualIndex.chapter.12.desc', message: 'Observabilidade, deteção/alerta, playbooks de resposta e cobertura pós-deploy'})},
    {n: '13', slug: 'formacao-onboarding', kind: 'organizacional',
      title: translate({id: 'manualIndex.chapter.13.title', message: 'Formação e Onboarding'}),
      desc: translate({id: 'manualIndex.chapter.13.desc', message: 'Capacitação contínua por papel, secure coding dojos e trilhos formativos'})},
    {n: '14', slug: 'governanca-contratacao', kind: 'organizacional',
      title: translate({id: 'manualIndex.chapter.14.title', message: 'Governança e Contratação'}),
      desc: translate({id: 'manualIndex.chapter.14.desc', message: 'Modelos de governação, KPIs, cláusulas contratuais e validação de fornecedores'})},
  ];
}

function kinds(): Record<Kind, {label: string; desc: string}> {
  return {
    basilar: {
      label: translate({id: 'manualIndex.type.basilar.label', message: 'Basilar'}),
      desc: translate({id: 'manualIndex.type.basilar.desc', message: 'Aplicável a todos os níveis (L1-L3)'}),
    },
    operacional: {
      label: translate({id: 'manualIndex.type.operacional.label', message: 'Operacional'}),
      desc: translate({id: 'manualIndex.type.operacional.desc', message: 'Implementação e automação (L2-L3)'}),
    },
    organizacional: {
      label: translate({id: 'manualIndex.type.organizacional.label', message: 'Organizacional'}),
      desc: translate({id: 'manualIndex.type.organizacional.desc', message: 'Governação e gestão (Transversal)'}),
    },
  };
}

type ChapterGridProps = {
  count: number;
  labelId: string;
};

export default function ChapterGrid({count, labelId}: ChapterGridProps) {
  const kindInfo = kinds();
  return (
    <>
      <p className="sl-eyebrow">
        <span>{translate({id: 'doc.eyebrow.manual', message: 'Manual'})}</span>
      </p>
      <h2 className={styles.title} id={labelId}>
        {translate({id: 'homepage.chapters.title', message: 'O Manual em {count} capítulos'}, {count})}
      </h2>
      <p className={styles.intro}>
        {translate({
          id: 'homepage.chapters.intro',
          message: 'Do risco da aplicação à operação. Cada capítulo diz o que fazer, que políticas adotar e como verificar.',
        })}
      </p>
      <ul className={styles.chapters}>
        {chapters().map((c) => (
          <li key={c.n}>
            <Link className={styles.chapter} to={`/sbd-toe/sbd-manual/${c.slug}/intro`}>
              <span className={styles.number} aria-hidden="true">{c.n}</span>
              <span className={styles.chapterTitle}>
                <span className={styles.srOnly}>{c.n} · </span>
                {c.title}
              </span>
              <span className={styles.desc}>{c.desc}</span>
              {c.kind ? (
                <span className={clsx('sl-badge', `sl-badge--${c.kind}`)}>{kindInfo[c.kind].label}</span>
              ) : (
                <span className="sl-badge">
                  {translate({id: 'homepage.chapters.startHere', message: 'Ponto de partida'})}
                </span>
              )}
            </Link>
          </li>
        ))}
      </ul>
      <p className={styles.legend}>
        {(Object.keys(kindInfo) as Kind[]).map((k) => (
          <span key={k}>
            <span className={clsx('sl-badge', `sl-badge--${k}`)}>{kindInfo[k].label}</span>
            {kindInfo[k].desc}
          </span>
        ))}
      </p>
    </>
  );
}
