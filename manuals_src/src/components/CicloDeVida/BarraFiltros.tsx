// Barra de filtros (00-especificacao.md §7.1 e §8): «Sou…», Nível, Capítulo, «Limpar filtros» e a contagem.
// Cada escolha chama onMudar uma vez, e a página faz um só history.push com a query toda.
import React, {type ReactNode} from 'react';
import clsx from 'clsx';
import {translate} from '@docusaurus/Translate';
import {NIVEIS, VAZIO, escrever, type Capitulo, type Estado, type Nivel} from './estado';
import styles from './CicloDeVida.module.css';

type Props = {
  estado: Estado;
  papeis: {id: string; rotulo: string; n: number}[];
  capitulos: Capitulo[];
  contagem: string;
  contaHistorias: (n: number) => string;
  onMudar: (mudanca: Partial<Estado>) => void;
};

export default function BarraFiltros({estado, papeis, capitulos, contagem, contaHistorias, onMudar}: Props): ReactNode {
  const comFiltros = Boolean(estado.papel || estado.nivel || estado.cap);
  const rotNivel = translate({id: 'lifecycleMap.filter.level', message: 'Nível'});
  return (
    <div className={styles.barra} role="search" aria-label={translate({id: 'lifecycleMap.filters.ariaLabel', message: 'Filtros do mapa'})}>
      <div className={styles.barraIn}>
        <label className={clsx(styles.campo, styles.campoPapel)}>
          <span className={styles.campoRot}>{translate({id: 'lifecycleMap.filter.role', message: 'Sou…'})}</span>
          <select
            className={clsx(styles.sel, estado.papel && styles.ativo)}
            value={estado.papel}
            onChange={(ev) => onMudar({papel: ev.target.value, abrir: ''})}>
            <option value="">{translate({id: 'lifecycleMap.filter.role.all', message: 'Todos os papéis'})}</option>
            {papeis.map((p) => (
              <option key={p.id} value={p.id}>
                {p.rotulo} ({contaHistorias(p.n)})
              </option>
            ))}
          </select>
        </label>
        <span className={styles.campo}>
          <span className={styles.campoRot} aria-hidden="true">
            {rotNivel}
          </span>
          <span className={styles.seg} role="group" aria-label={rotNivel}>
            {(['', ...NIVEIS] as (Nivel | '')[]).map((n) => (
              <button key={n || 'todos'} type="button" aria-pressed={estado.nivel === n} onClick={() => onMudar({nivel: n})}>
                {n || translate({id: 'lifecycleMap.filter.level.all', message: 'Todos'})}
              </button>
            ))}
          </span>
        </span>
        <label className={clsx(styles.campo, styles.campoCap)}>
          <span className={styles.campoRot}>{translate({id: 'lifecycleMap.filter.chapter', message: 'Capítulo'})}</span>
          <select
            className={clsx(styles.sel, estado.cap && styles.ativo)}
            value={estado.cap}
            onChange={(ev) => onMudar({cap: ev.target.value, abrir: ''})}>
            <option value="">{translate({id: 'lifecycleMap.filter.chapter.all', message: 'Todos os capítulos'})}</option>
            {capitulos.map((c) => (
              <option key={c.id} value={c.id}>
                {c.id} · {c.titulo}
              </option>
            ))}
          </select>
        </label>
        <span className={styles.conta}>
          <span aria-live="polite">{contagem}</span>
          {comFiltros && (
            <a
              className={styles.limpar}
              href={escrever(VAZIO) || '?'}
              onClick={(ev) => {
                ev.preventDefault();
                onMudar(VAZIO);
              }}>
              {translate({id: 'lifecycleMap.filter.clear', message: 'Limpar filtros'})}
            </a>
          )}
        </span>
      </div>
    </div>
  );
}
