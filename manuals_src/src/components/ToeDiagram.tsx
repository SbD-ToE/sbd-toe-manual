import React from 'react';
import Link from '@docusaurus/Link';
import {translate} from '@docusaurus/Translate';
import styles from './ToeDiagram.module.css';

// Diagrama da Theory of Everything na página inicial (M-39, H-02): rótulos fora do anel,
// sem sobreposições. Abaixo de 997 px o desenho esconde-se e fica só a ligação.
// O diagrama do cânone (docs/sbd-toe/000-teory-of-everything/intro.mdx) é outro e não muda.
export default function ToeDiagram() {
  return (
    <Link to="/sbd-toe/teory-of-everything/intro" className={styles.diagram}>
      <svg
        viewBox="0 0 560 400"
        role="img"
        aria-label={translate({id: 'toe.chart.ariaLabel', message: 'Diagrama conceptual da Theory of Everything'})}
      >
        <circle className={styles.ring} cx="360" cy="200" r="135" />
        <line className={styles.spoke} x1="360" y1="91" x2="360" y2="120" />
        <line className={styles.spoke} x1="360" y1="280" x2="360" y2="309" />
        <line className={styles.spoke} x1="251" y1="200" x2="280" y2="200" />
        <circle className={styles.core} cx="360" cy="200" r="80" />
        <text className={styles.tCore} x="360" y="196" textAnchor="middle">Security by Design</text>
        <text className={styles.tCore2} x="360" y="217" textAnchor="middle">Theory of Everything</text>

        {/* Rótulos de cima e de baixo afastados do anel (diagrama-sobreposicao): a 1440 px, medidos
            por getBBox, ficam a ≥ 6 unidades do traço, como os que já não tocavam no anel. */}
        <circle className={styles.sat} cx="360" cy="65" r="26" />
        <text className={styles.tAxis} x="400" y="42">Top-Down</text>
        <text className={styles.tSub} x="400" y="60">
          {translate({id: 'toe.chart.topDown', message: 'Normas & Regulação'})}
        </text>

        <circle className={styles.sat} cx="360" cy="335" r="26" />
        <text className={styles.tAxis} x="400" y="352">Bottom-Up</text>
        <text className={styles.tSub} x="400" y="372">
          {translate({id: 'toe.chart.bottomUp', message: 'Ameaças & Incidentes'})}
        </text>

        <circle className={styles.sat} cx="225" cy="200" r="26" />
        <text className={styles.tAxis} x="186" y="195" textAnchor="end">Engineering</text>
        <text className={styles.tSub} x="186" y="215" textAnchor="end">
          {translate({id: 'toe.chart.engineering', message: 'Execução & Ciclo de vida'})}
        </text>
      </svg>
      <span className={styles.caption}>
        Theory of Everything <span aria-hidden="true">→</span>
      </span>
    </Link>
  );
}
