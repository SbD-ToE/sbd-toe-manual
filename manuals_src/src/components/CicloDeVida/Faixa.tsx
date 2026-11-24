// Faixa de um papel (00-especificacao.md §7.1): uma coluna por fase e a coluna Transversal; na vista ágil, uma por
// evento do Scrum e as duas fora do Scrum (00-especificacao-agil.md §4.2).
// Recolhida (decisão mapa-sem-papel = b), mostra só a contagem por coluna e não põe os cartões no HTML.
// Abaixo da quebra do mapa (997 px; 1120 px na vista ágil, §4.4) as colunas empilham-se num trilho vertical (só CSS),
// e o detalhe abre por baixo do cartão. A partir da quebra o detalhe fica por cima dos cartões seguintes, preso ao
// cartão (posição calculada aqui).
import React, {useLayoutEffect, useRef, type ReactNode} from 'react';
import clsx from 'clsx';
import {translate} from '@docusaurus/Translate';
import type {Capitulo, Cartao as TCartao, Momento, Nivel, Papel} from './estado';
import type {Coluna} from './fases';
import Cartao from './Cartao';
import Detalhe from './Detalhe';
import styles from './CicloDeVida.module.css';

type Props = {
  papel: Papel;
  cartoes: TCartao[];
  noManual: number;
  colunas: Coluna[];
  agil: boolean;
  aberta: boolean;
  recolhivel: boolean;
  nivel: Nivel | '';
  abrir: string;
  largura: number;
  capitulo: (id: string) => Capitulo | undefined;
  colunasDe: (m: Momento) => string[];
  nomeColuna: (id: string) => string;
  contaHistorias: (n: number) => string;
  onAlternar: (papel: string, aberta: boolean) => void;
  onAbrir: (k: string) => void;
  onFechar: () => void;
};

const LARGO = '(min-width: 997px)';
const LARGO_AGIL = '(min-width: 1120px)';

export default function Faixa(props: Props): ReactNode {
  const {papel, cartoes, colunas, agil, aberta, nivel, abrir} = props;
  const ref = useRef<HTMLElement>(null);
  const n = new Set(cartoes.map((c) => c.h.id)).size;
  const porFase = (f: string) => cartoes.filter((c) => c.fase === f);
  const nFase = (f: string) => new Set(porFase(f).map((c) => c.h.id)).size;
  const temAberto = aberta && cartoes.some((c) => c.k === abrir);
  const idRot = `faixa-${papel.id}`;

  // posição do detalhe a partir da quebra do mapa: por baixo do cartão, com a seta para ele, sem sair da faixa.
  // Os cartões que o detalhe tapa (metade ou mais) saem da ordem de Tab enquanto ele está aberto (F-C da SHI-27).
  useLayoutEffect(() => {
    const fx = ref.current;
    const det = fx?.querySelector<HTMLElement>('[role="region"][id^="det-"]');
    if (!fx) return;
    fx.style.paddingBottom = '';
    fx.querySelectorAll<HTMLElement>('[data-tapado]').forEach((c) => {
      c.removeAttribute('data-tapado');
      c.removeAttribute('tabindex');
    });
    if (!det) return;
    if (!window.matchMedia(agil ? LARGO_AGIL : LARGO).matches) {
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
    const rD = det.getBoundingClientRect();
    fx.querySelectorAll<HTMLElement>('button[data-k]').forEach((c) => {
      const r = c.getBoundingClientRect();
      const x = Math.min(r.right, rD.right) - Math.max(r.left, rD.left);
      const y = Math.min(r.bottom, rD.bottom) - Math.max(r.top, rD.top);
      if (x > 0 && y > 0 && x * y >= (r.width * r.height) / 2) {
        c.tabIndex = -1;
        c.dataset.tapado = '';
      }
    });
  }, [abrir, nivel, aberta, props.largura, temAberto, agil]);

  // a marca ↻ depois do último evento do Scrum: só no trilho vertical (escondida no horizontal, onde está no Trilho)
  const ultimaDoCiclo = agil ? colunas.filter((f) => !f.fora).pop()?.id : undefined;
  const volta = translate({id: 'lifecycleMap.agile.loop', message: 'O ciclo repete-se em cada sprint.'});

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
    corpo = colunas.map((f) => {
      const k = nFase(f.id);
      return (
        <React.Fragment key={f.id}>
          <div className={clsx(styles.cel, styles.celConta, f.fora && styles.transv)} data-coluna={f.id}>
            <span className={styles.contaN} aria-hidden="true">
              {f.marca}
            </span>
            <span className={styles.sr}>{f.nome}: </span>
            <span className={clsx(k === 0 && styles.zero)}>{k}</span>
          </div>
          {f.id === ultimaDoCiclo && (
            <span className={styles.voltaConta} aria-hidden="true" title={volta}>
              ↻
            </span>
          )}
        </React.Fragment>
      );
    });
  } else {
    corpo = colunas.map((f) => {
      const daFase = porFase(f.id);
      return (
        <React.Fragment key={f.id}>
          <div className={clsx(styles.cel, f.fora && styles.transv)} data-coluna={f.id}>
            <div className={styles.celCab}>
              <span className={styles.trilhoN} aria-hidden="true">
                {f.marca}
              </span>
              <h3 className={styles.celNome}>
                {f.nome} <span className={styles.trilhoConta}>{nFase(f.id)}</span>
              </h3>
            </div>
            <p className={styles.celDesc}>{f.descricao}</p>
            {daFase.length === 0 && (
              <p className={styles.celVazia}>
                {agil
                  ? translate({id: 'lifecycleMap.column.empty', message: 'Nenhuma história nesta coluna com estes filtros.'})
                  : translate({id: 'lifecycleMap.phase.empty', message: 'Nenhuma história nesta fase com estes filtros.'})}
              </p>
            )}
            {daFase.map((c) => (
              <React.Fragment key={c.k}>
                <Cartao
                  c={c}
                  nivel={nivel}
                  aberto={c.k === abrir}
                  colunasDe={props.colunasDe}
                  nomeColuna={props.nomeColuna}
                  onAbrir={props.onAbrir}
                />
                {c.k === abrir && (
                  <Detalhe
                    c={c}
                    cap={props.capitulo(c.h.cap)}
                    nivel={nivel}
                    agil={agil}
                    colunasDe={props.colunasDe}
                    nomeColuna={props.nomeColuna}
                    onFechar={props.onFechar}
                  />
                )}
              </React.Fragment>
            ))}
          </div>
          {f.id === ultimaDoCiclo && (
            <p className={styles.voltaLinha}>
              <span aria-hidden="true">↻ </span>
              {volta}
            </p>
          )}
        </React.Fragment>
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
