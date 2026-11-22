import React from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import Translate, {translate} from '@docusaurus/Translate';
import HomeEntries from '@site/src/components/HomeEntries';
import ToeDiagram from '@site/src/components/ToeDiagram';
import ChapterGrid from '@site/src/components/ChapterGrid';
import styles from './index.module.css';

// Página inicial (SHI-31, M-35…M-47): herói, por onde começar, faixa de prova,
// grelha de capítulos e faixa de fecho.

const githubUrl = 'https://github.com/SbD-ToE/sbd-toe-manual';

type ManualFacts = {
  manualVersion: string;
  counts: {chapters: number; regulations: number; policies: number};
};

/* ===================== HERÓI (M-36, M-43, M-47) ===================== */

function HomeHero() {
  return (
    <header className={styles.hero}>
      <div className={clsx(styles.container, styles.heroGrid)}>
        <div>
          {/* M-47: o "·" é um separador à parte, que se esconde abaixo de 997 px */}
          <p className={clsx('sl-eyebrow', styles.heroEyebrow)}>
            <span>SbD-ToE</span>
            <span className="sl-eyebrow__sep" aria-hidden="true">·</span>
            <span>
              <Translate id="homepage.hero.eyebrow">Manual aberto de segurança de software</Translate>
            </span>
          </p>
          <h1 className={styles.heroTitle}>Security by Design – Theory of Everything</h1>
          <p className={styles.heroLead}>
            <Translate id="homepage.hero.subtitle">
              O SbD–ToE liga regulamentos europeus, normas técnicas, frameworks de maturidade, ameaças reais e engenharia de software num manual prescritivo, reutilizável e proporcional ao risco.
            </Translate>
          </p>
          <div className={styles.actions}>
            <Link className={clsx(styles.btn, styles.btnPrimary)} to="/sbd-toe/sbd-manual/">
              <Translate id="homepage.hero.cta.manual">Ler o Manual</Translate> <span aria-hidden="true">→</span>
            </Link>
            <Link className={clsx(styles.btn, styles.btnSecondary)} to="/sbd-toe/sbd-manual/fundamentos/como-usar">
              <Translate id="homepage.hero.cta.howTo">Como usar este manual</Translate>
            </Link>
          </div>
        </div>
        <ToeDiagram />
      </div>
    </header>
  );
}

/* ===================== FAIXA DE PROVA (M-40, S-08) ===================== */

function FactsStrip({manualVersion, counts}: ManualFacts) {
  return (
    <ul
      className={styles.facts}
      aria-label={translate({id: 'homepage.facts.ariaLabel', message: 'O manual em números'})}
    >
      <li>
        <Translate id="homepage.facts.chapters" values={{count: <b>{counts.chapters}</b>}}>
          {'{count} capítulos'}
        </Translate>
      </li>
      <li>
        <Translate id="homepage.facts.regulations" values={{count: <b>{counts.regulations}</b>}}>
          {'{count} regulamentos no cross-check'}
        </Translate>
      </li>
      <li>
        <Translate id="homepage.facts.policies" values={{count: <b>{counts.policies}</b>}}>
          {'{count} políticas recomendadas'}
        </Translate>
      </li>
      <li>
        <b>PT · EN</b>
      </li>
      <li>
        <Translate id="homepage.facts.version" values={{version: <b>{manualVersion}</b>}}>
          {'versão {version}'}
        </Translate>
      </li>
    </ul>
  );
}

/* ===================== FAIXA DE FECHO (M-45, S-13) ===================== */

function ClosingBand() {
  return (
    <section className={styles.band} aria-labelledby="home-band-title">
      <div className={styles.container}>
        <p className="sl-eyebrow">
          <span>
            <Translate id="homepage.band.eyebrow">Projeto aberto</Translate>
          </span>
        </p>
        <h2 className={styles.h2} id="home-band-title">
          <Translate id="homepage.band.title">Aberto, versionado e público no GitHub.</Translate>
        </h2>
        <p>
          <Translate id="homepage.band.text">
            O conteúdo está sob licença CC BY-SA 4.0: pode lê-lo, reutilizá-lo e propor alterações.
          </Translate>
        </p>
        <div className={styles.actions}>
          <Link className={clsx(styles.btn, styles.btnOnBand)} href={githubUrl}>
            <Translate id="homepage.band.github">Ver no GitHub</Translate> <span aria-hidden="true">↗</span>
          </Link>
          <Link className={clsx(styles.btn, styles.btnOnBandOutline)} to="/licenciamento">
            <Translate id="homepage.band.licence">Licença</Translate>
          </Link>
        </div>
      </div>
    </section>
  );
}

/* ===================== PÁGINA (M-35, M-37) ===================== */

export default function Home(): JSX.Element {
  const {siteConfig} = useDocusaurusContext();
  const facts = siteConfig.customFields as ManualFacts;
  return (
    <Layout
      title={translate({id: 'homepage.title', message: 'Início'})}
      description={translate({id: 'homepage.description', message: 'Security by Design - Theory of Everything. Manual prático, aberto e prescritivo para aplicar segurança por desenho em organizações modernas.'})}
    >
      <main className={styles.home}>
        <HomeHero />
        <section className={styles.start} aria-labelledby="home-start-title">
          <div className={styles.container}>
            <HomeEntries labelId="home-start-title" />
            <FactsStrip manualVersion={facts.manualVersion} counts={facts.counts} />
          </div>
        </section>
        <section className={clsx(styles.section, styles.sectionAlt)} aria-labelledby="home-chapters-title">
          <div className={styles.container}>
            <ChapterGrid count={facts.counts.chapters} labelId="home-chapters-title" />
          </div>
        </section>
        <ClosingBand />
      </main>
    </Layout>
  );
}
