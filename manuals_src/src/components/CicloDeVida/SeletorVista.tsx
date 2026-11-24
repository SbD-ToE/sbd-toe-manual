// Seletor de vista (00-especificacao-agil.md §4.1): «Vista  [Ciclo de vida] [Ágil]», no cabeçalho e fora da barra fixa.
// O mesmo controlo segmentado do Nível (.seg, botões com aria-pressed): cada botão muda o URL com um history.push.
import React, {type ReactNode} from 'react';
import {translate} from '@docusaurus/Translate';
import type {Vista} from './estado';
import styles from './CicloDeVida.module.css';

export default function SeletorVista({vista, onMudar}: {vista: Vista; onMudar: (v: Vista) => void}): ReactNode {
  const rot = translate({id: 'lifecycleMap.view', message: 'Vista'});
  return (
    <div className={styles.vista}>
      <span className={styles.campoRot} aria-hidden="true">
        {rot}
      </span>
      <span className={styles.seg} role="group" aria-label={rot}>
        <button type="button" aria-pressed={vista === ''} onClick={() => onMudar('')}>
          {translate({id: 'lifecycleMap.view.lifecycle', message: 'Ciclo de vida'})}
        </button>
        <button
          type="button"
          aria-pressed={vista === 'agil'}
          title={translate({id: 'lifecycleMap.view.agile.title', message: 'Vista ágil, com os eventos do Scrum'})}
          onClick={() => onMudar('agil')}>
          {translate({id: 'lifecycleMap.view.agile', message: 'Ágil'})}
        </button>
      </span>
    </div>
  );
}
