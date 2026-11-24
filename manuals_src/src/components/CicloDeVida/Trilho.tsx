// Trilho das colunas (00-especificacao.md §7.1; 00-especificacao-agil.md §4.2): as 6 fases numeradas em linha e a
// Transversal à parte, com círculo tracejado; na vista ágil, os 6 eventos do Scrum, a marca ↻ depois do 6.º, e
// Operação e Cadência organizacional à parte, tracejadas e sem número. Fica preso por baixo da barra de filtros
// a partir da quebra do mapa; abaixo dela esconde-se, e cada faixa mostra as colunas de cima para baixo (Faixa.tsx).
import React, {type ReactNode} from 'react';
import clsx from 'clsx';
import {translate} from '@docusaurus/Translate';
import type {Coluna} from './fases';
import styles from './CicloDeVida.module.css';

type Props = {colunas: Coluna[]; porColuna: Record<string, number>; agil: boolean};

export default function Trilho({colunas, porColuna, agil}: Props): ReactNode {
  const ultimaDoCiclo = colunas.filter((c) => !c.fora).pop()?.id;
  const volta = translate({id: 'lifecycleMap.agile.loop', message: 'O ciclo repete-se em cada sprint.'});
  return (
    <div className={styles.cab} data-cab="">
      <span className={styles.canto} aria-hidden="true" />
      <ol
        className={styles.trilho}
        aria-label={
          agil
            ? translate({id: 'lifecycleMap.trail.agile.ariaLabel', message: 'Eventos do Scrum e colunas fora do sprint'})
            : translate({id: 'lifecycleMap.trail.ariaLabel', message: 'Fases do ciclo de vida'})
        }>
        {colunas.map((f) => (
          <li key={f.id} className={clsx(styles.trilhoFase, f.fora && styles.transv)} data-trilho-fase={f.id}>
            <span className={styles.trilhoN} aria-hidden="true">
              {f.marca}
            </span>
            {agil && f.id === ultimaDoCiclo && (
              <>
                <span className={styles.volta} aria-hidden="true" title={volta}>
                  ↻
                </span>
                <span className={styles.sr}>{volta}</span>
              </>
            )}
            <span className={styles.trilhoNome}>
              {f.nome} <span className={styles.trilhoConta}>{porColuna[f.id] ?? 0}</span>
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
