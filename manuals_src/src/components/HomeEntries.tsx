import React from 'react';
import Link from '@docusaurus/Link';
import {translate} from '@docusaurus/Translate';
import UseCaseCard from './UseCaseCard';

// "Por onde começar" na página inicial (M-38, H-03): 4 entradas por perfil, cada uma com o
// destino escrito. Os rótulos dos destinos são os da navegação (SHI-29).
// Na mesma linha do rótulo, à direita, a ligação ao Mapa do ciclo de vida (SHI-152 §3.2, opção H1).

// Ícones de traço (S-11: sem emoji na moldura); a cor vem de .sl-usecase-card__icon
const iconProps = {
  viewBox: '0 0 24 24',
  fill: 'none',
  stroke: 'currentColor',
  strokeWidth: 2,
  strokeLinecap: 'round' as const,
  strokeLinejoin: 'round' as const,
  'aria-hidden': true,
};

const icons = {
  management: (
    <svg {...iconProps}>
      <rect x="3" y="7" width="18" height="13" rx="2" />
      <path d="M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2" />
      <path d="M3 13h18" />
    </svg>
  ),
  engineering: (
    <svg {...iconProps}>
      <path d="m16 18 6-6-6-6" />
      <path d="m8 6-6 6 6 6" />
    </svg>
  ),
  grc: (
    <svg {...iconProps}>
      <path d="M12 3v18" />
      <path d="M5 21h14" />
      <path d="M3 7h18" />
      <path d="m6 7-3 7a3 3 0 0 0 6 0z" />
      <path d="m18 7-3 7a3 3 0 0 0 6 0z" />
    </svg>
  ),
  ai: (
    <svg {...iconProps}>
      <path d="M12 22v-5" />
      <path d="M9 8V2" />
      <path d="M15 8V2" />
      <path d="M18 8v5a6 6 0 0 1-12 0V8z" />
    </svg>
  ),
};

type HomeEntriesProps = {
  labelId: string;
};

export default function HomeEntries({labelId}: HomeEntriesProps) {
  const entries = [
    {
      key: 'management',
      title: translate({id: 'homepage.start.management.title', message: 'Gestão e CISO'}),
      summary: translate({
        id: 'homepage.start.management.summary',
        message: 'O modelo, o que pede à organização e por onde começar, numa leitura curta.',
      }),
      cta: translate({id: 'homepage.start.management.cta', message: 'Resumo executivo (TL;DR)'}),
      to: '/sbd-toe/tldr',
    },
    {
      key: 'engineering',
      title: translate({id: 'homepage.start.engineering.title', message: 'Engenharia'}),
      summary: translate({
        id: 'homepage.start.engineering.summary',
        message: 'Classificar a aplicação (L1⁠–⁠L3) e ver os controlos que se aplicam a cada nível.',
      }),
      cta: `01 · ${translate({id: 'manualIndex.chapter.01.title', message: 'Classificação das Aplicações'})}`,
      to: '/sbd-toe/sbd-manual/classificacao-aplicacoes/intro',
    },
    {
      key: 'grc',
      title: translate({id: 'homepage.start.grc.title', message: 'GRC e Jurídico'}),
      summary: translate({
        id: 'homepage.start.grc.summary',
        message: 'O que o SbD-ToE cobre em NIS2, DORA, CRA, AI Act, RGPD e CSA, e as lacunas declaradas.',
      }),
      cta: translate({id: 'homepage.card.crossCheck.title', message: 'Cross-check normativo'}),
      to: '/sbd-toe/cross-check-normativo/intro',
    },
    {
      key: 'ai',
      title: translate({id: 'homepage.start.ai.title', message: 'IA e Plataforma'}),
      summary: translate({
        id: 'homepage.start.ai.summary',
        message: 'Levar os controlos do manual para o assistente de código, com citações.',
      }),
      cta: 'MCP Server (SbD-ToE)',
      to: '/sbd-toe/assets/mcp/intro',
    },
  ] as const;

  return (
    <>
      <div className="sl-home-start">
        <p className="sl-eyebrow" id={labelId}>
          <span>{translate({id: 'homepage.start.eyebrow', message: 'Por onde começar'})}</span>
        </p>
        <Link className="sl-home-lifecycle" to="/ciclo-de-vida">
          {translate({id: 'homepage.start.lifecycle', message: 'Mapa do ciclo de vida'})}{' '}
          <span aria-hidden="true">→</span>
        </Link>
      </div>
      <div className="sl-usecase-grid">
        {entries.map((e) => (
          <UseCaseCard
            key={e.key}
            icon={icons[e.key]}
            title={e.title}
            summary={e.summary}
            cta={e.cta}
            to={e.to}
          />
        ))}
      </div>
    </>
  );
}
