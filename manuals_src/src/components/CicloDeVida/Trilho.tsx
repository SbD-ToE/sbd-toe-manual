// Trilho das fases (00-especificacao.md §7.1): as 6 fases numeradas em linha e a Transversal à parte,
// com círculo tracejado. Fica preso por baixo da barra de filtros a partir de 997 px; abaixo disso
// esconde-se, e cada faixa mostra as fases de cima para baixo (Faixa.tsx).
import React, {type ReactNode} from 'react';
import clsx from 'clsx';
import {translate} from '@docusaurus/Translate';
import type {Fase} from './fases';
import styles from './CicloDeVida.module.css';

export default function Trilho({fases, porFase}: {fases: Fase[]; porFase: Record<string, number>}): ReactNode {
  return (
    <div className={styles.cab} data-cab="">
      <span className={styles.canto} aria-hidden="true" />
      <ol className={styles.trilho} aria-label={translate({id: 'lifecycleMap.trail.ariaLabel', message: 'Fases do ciclo de vida'})}>
        {fases.map((f) => (
          <li key={f.id} className={clsx(styles.trilhoFase, f.transversal && styles.transv)} data-trilho-fase={f.id}>
            <span className={styles.trilhoN} aria-hidden="true">
              {f.transversal ? '∞' : f.ordem}
            </span>
            <span className={styles.trilhoNome}>
              {f.nome} <span className={styles.trilhoConta}>{porFase[f.id] ?? 0}</span>
            </span>
            <span className={styles.trilhoDesc} title={f.descricao}>
              {f.descricao}
            </span>
          </li>
        ))}
      </ol>
    </div>
  );
}
