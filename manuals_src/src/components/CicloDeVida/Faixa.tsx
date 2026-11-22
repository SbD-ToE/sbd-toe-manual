// Faixa de um papel (00-especificacao.md §7.1): uma coluna por fase e a coluna Transversal.
// Recolhida (decisão mapa-sem-papel = b), mostra só a contagem por fase e não põe os cartões no HTML.
// Abaixo de 997 px as colunas empilham-se num trilho vertical (só CSS), e o detalhe abre por baixo do cartão.
// A partir de 997 px o detalhe fica por cima dos cartões seguintes, preso ao cartão (posição calculada aqui).
import React, {useLayoutEffect, useRef, type ReactNode} from 'react';
import clsx from 'clsx';
import {translate} from '@docusaurus/Translate';
import type {Capitulo, Cartao as TCartao, Nivel, Papel} from './estado';
import type {Fase} from './fases';
import Cartao from './Cartao';
import Detalhe from './Detalhe';
import styles from './CicloDeVida.module.css';

type Props = {
  papel: Papel;
  cartoes: TCartao[];
  noManual: number;
  fases: Fase[];
  aberta: boolean;
  recolhivel: boolean;
  nivel: Nivel | '';
  abrir: string;
  largura: number;
  capitulo: (id: string) => Capitulo | undefined;
  nomeFase: (id: string) => string;
  contaHistorias: (n: number) => string;
  onAlternar: (papel: string, aberta: boolean) => void;
  onAbrir: (k: string) => void;
  onFechar: () => void;
};

const LARGO = '(min-width: 997px)';

export default function Faixa(props: Props): ReactNode {
  const {papel, cartoes, fases, aberta, nivel, abrir} = props;
  const ref = useRef<HTMLElement>(null);
  const n = new Set(cartoes.map((c) => c.h.id)).size;
  const porFase = (f: string) => cartoes.filter((c) => c.fase === f);
  const nFase = (f: string) => new Set(porFase(f).map((c) => c.h.id)).size;
  const temAberto = aberta && cartoes.some((c) => c.k === abrir);
  const idRot = `faixa-${papel.id}`;

  // posição do detalhe a partir de 997 px: por baixo do cartão, com a seta para ele, sem sair da faixa
  useLayoutEffect(() => {
    const fx = ref.current;
    const det = fx?.querySelector<HTMLElement>('[role="region"][id^="det-"]');
    if (!fx) return;
    fx.style.paddingBottom = '';
    if (!det) return;
    if (!window.matchMedia(LARGO).matches) {
      det.removeAttribute('style');
      return;
    }
    const card = fx.querySelector<HTMLElement>(`[data-k="${CSS.escape(abrir)}"]`);
    if (!card) return;
    const rF = fx.getBoundingClientRect();
    const rC = card.getBoundingClientRect();
    const rotulo = fx.querySelector<HTMLElement>('[data-rotulo]')?.getBoundingClientRect().width ?? 0;
    const w = Math.min(rF.width - rotulo - 8, 920);
    let left = rC.left - rF.left;
    if (left + w > rF.width) left = rF.width - w;
    const top = rC.bottom - rF.top + 10;
    Object.assign(det.style, {top: `${top}px`, left: `${left}px`, width: `${w}px`});
    det.style.setProperty('--seta', `${rC.left - rF.left - left + Math.min(rC.width / 2, 40)}px`);
    const falta = top + det.offsetHeight + 16 - fx.offsetHeight;
    if (falta > 0) fx.style.paddingBottom = `${falta}px`;
  }, [abrir, nivel, aberta, props.largura, temAberto]);

  let corpo: ReactNode;
  if (props.noManual === 0 || cartoes.length === 0) {
    corpo = (
      <p className={styles.faixaVazia}>
        {props.noManual === 0
          ? translate({id: 'lifecycleMap.lane.none', message: 'Nenhuma história do manual tem este papel.'})
          : translate({id: 'lifecycleMap.lane.empty', message: 'Sem histórias para este papel com estes filtros.'})}
      </p>
    );
  } else if (!aberta) {
    corpo = fases.map((f) => {
      const k = nFase(f.id);
      return (
        <div key={f.id} className={clsx(styles.cel, styles.celConta, f.transversal && styles.transv)} data-coluna={f.id}>
          <span className={styles.contaN} aria-hidden="true">
            {f.transversal ? '∞' : f.ordem}
          </span>
          <span className={styles.sr}>{f.nome}: </span>
          <span className={clsx(k === 0 && styles.zero)}>{k}</span>
        </div>
      );
    });
  } else {
    corpo = fases.map((f) => {
      const daFase = porFase(f.id);
      return (
        <div key={f.id} className={clsx(styles.cel, f.transversal && styles.transv)} data-coluna={f.id}>
          <div className={styles.celCab}>
            <span className={styles.trilhoN} aria-hidden="true">
              {f.transversal ? '∞' : f.ordem}
            </span>
            <h3 className={styles.celNome}>
              {f.nome} <span className={styles.trilhoConta}>{nFase(f.id)}</span>
            </h3>
          </div>
          <p className={styles.celDesc}>{f.descricao}</p>
          {daFase.length === 0 && (
            <p className={styles.celVazia}>
              {translate({id: 'lifecycleMap.phase.empty', message: 'Nenhuma história nesta fase com estes filtros.'})}
            </p>
          )}
          {daFase.map((c) => (
            <React.Fragment key={c.k}>
              <Cartao c={c} nivel={nivel} aberto={c.k === abrir} nomeFase={props.nomeFase} onAbrir={props.onAbrir} />
              {c.k === abrir && (
                <Detalhe
                  c={c}
                  cap={props.capitulo(c.h.cap)}
                  nivel={nivel}
                  nomeFase={props.nomeFase}
                  onFechar={props.onFechar}
                />
              )}
            </React.Fragment>
          ))}
        </div>
      );
    });
  }

  const vazia = props.noManual === 0 || cartoes.length === 0;
  return (
    <section
      ref={ref}
      className={clsx(styles.faixa, vazia && styles.faixaSemCartoes, !aberta && !vazia && styles.faixaRecolhida)}
      data-faixa={papel.id}
      aria-labelledby={idRot}>
      <div className={styles.faixaRot} data-rotulo="">
        <h2 id={idRot} className={styles.faixaTitulo}>
          {papel.rotulo}{' '}
          <span className={styles.faixaN}>
            <span aria-hidden="true">{n}</span>
            <span className={styles.sr}>{props.contaHistorias(n)}</span>
          </span>
        </h2>
        {props.recolhivel && !vazia && (
          <button
            type="button"
            className={styles.alternar}
            aria-expanded={aberta}
            aria-controls={`${idRot}-corpo`}
            onClick={() => props.onAlternar(papel.id, aberta)}>
            {aberta
              ? translate({id: 'lifecycleMap.lane.collapse', message: 'Recolher'})
              : translate({id: 'lifecycleMap.lane.expand', message: 'Mostrar as histórias'})}
          </button>
        )}
      </div>
      <div id={`${idRot}-corpo`} className={styles.faixaCorpo}>
        {corpo}
      </div>
    </section>
  );
}
