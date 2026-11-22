// Cartão do mapa (00-especificacao.md §7.2): «Cap. 05 · US-14», Resp., título, os nomes de fase originais,
// o SLA, o que o nível escolhido exige e «também em». É um botão que abre o detalhe no sítio.
import React, {type ReactNode} from 'react';
import clsx from 'clsx';
import {translate} from '@docusaurus/Translate';
import {doNivel, type Cartao as TCartao, type Nivel} from './estado';
import styles from './CicloDeVida.module.css';

type Props = {
  c: TCartao;
  nivel: Nivel | '';
  aberto: boolean;
  nomeFase: (id: string) => string;
  onAbrir: (k: string) => void;
};

export default function Cartao({c, nivel, aberto, nomeFase, onAbrir}: Props): ReactNode {
  const {h} = c;
  const mo = c.momentos.map((i) => h.momentos[i]);
  const slas = mo.map((m) => m.sla).filter(Boolean);
  const nv = doNivel(h, nivel);
  const semNiveis = h.nivel.forma === 'sem-niveis' || h.nivel.forma === 'ausente';
  // outras fases da mesma história nesta faixa (todos os momentos em que o papel aparece)
  const outras = [
    ...new Set(h.momentos.filter((m) => m.papeis.includes(c.papel)).flatMap((m) => m.fases)),
  ].filter((f) => f !== c.fase);
  return (
    <button
      type="button"
      className={clsx(styles.cartao, nv?.leve && styles.cartaoLeve)}
      data-k={c.k}
      data-historia={h.id}
      data-papel={c.papel}
      data-fase={c.fase}
      aria-expanded={aberto}
      aria-controls={`det-${c.k}`}
      aria-label={`${translate({id: 'lifecycleMap.card.open', message: 'Abrir a história'})}: ${h.titulo}`}
      onClick={() => onAbrir(c.k)}>
      <span className={styles.cartaoTopo}>
        <span className={styles.mono}>
          {translate({id: 'lifecycleMap.card.chapter', message: 'Cap. {number}'}, {number: h.cap})} · {h.us}
        </span>
        {c.resp && (
          <span
            className={clsx(styles.tag, styles.tagResp)}
            title={translate({
              id: 'lifecycleMap.card.responsible.title',
              message: 'Responsável nesta fase (coluna Responsável do capítulo)',
            })}>
            {translate({id: 'lifecycleMap.card.responsible', message: 'Resp.'})}
          </span>
        )}
      </span>
      <span className={styles.cartaoTitulo} data-conteudo="">
        {h.titulo}
      </span>
      <span className={styles.cartaoMeta}>
        <b>{translate({id: 'lifecycleMap.card.phase', message: 'Fase'})}</b>
        {/* cada nome de fase uma só vez, pela ordem da primeira ocorrência (SHI-205) */}
        <span data-conteudo="">{[...new Set(mo.map((m) => m.fase))].join(' · ')}</span>
      </span>
      {slas.length > 0 && (
        <span className={styles.cartaoMeta}>
          <b>{translate({id: 'lifecycleMap.card.sla', message: 'SLA'})}</b>
          <span data-conteudo="">{slas.join(' · ')}</span>
        </span>
      )}
      {outras.length > 0 && (
        <span className={styles.cartaoTambem}>
          {translate(
            {id: 'lifecycleMap.card.alsoIn', message: 'também em {phases}'},
            {phases: outras.map(nomeFase).join(', ')},
          )}
        </span>
      )}
      {nivel && (
        <span className={styles.cartaoNivel}>
          <b>{translate({id: 'lifecycleMap.card.level', message: 'Nível {level}'}, {level: nivel})}</b>
          {nv?.leve && <span className={clsx(styles.tag, styles.tagLeve)} data-conteudo="">{nv.leve}</span>}{' '}
          {nv ? (
            <span data-conteudo="" dangerouslySetInnerHTML={{__html: nv.html}} />
          ) : semNiveis ? (
            <i>{translate({id: 'lifecycleMap.card.level.none', message: 'O capítulo não distingue níveis.'})}</i>
          ) : null}
        </span>
      )}
    </button>
  );
}
