// Cartão do mapa (00-especificacao.md §7.2): «Cap. 05 · US-14», Resp., título, os nomes de fase originais,
// o SLA, o que o nível escolhido exige e «também em» (as outras colunas da vista). É um botão que abre o detalhe no sítio.
// O cartão de uma cerimónia inferida (vista ágil, 00-especificacao-agil.md §10.2) leva a marca «inferido» e não tem
// Fase nem SLA, que são das linhas do capítulo.
import React, {type ReactNode} from 'react';
import clsx from 'clsx';
import {translate} from '@docusaurus/Translate';
import {doNivel, type Cartao as TCartao, type Momento, type Nivel} from './estado';
import styles from './CicloDeVida.module.css';

// O texto não muda (Q-1 da SHI-207): depois de «/» e «→» entra um <wbr>, para a linha poder partir aí e não a meio
// de uma palavra («Planeamento/Release», «seccomp/AppArmor»).
function Quebras({texto}: {texto: string}): ReactNode {
  return texto.split(/(?<=[/→])/).map((p, i) => (
    <React.Fragment key={i}>
      {i > 0 && <wbr />}
      {p}
    </React.Fragment>
  ));
}

// Linha Fase (ressalva da SHI-209): o Chromium não hifeniza a palavra colada a uma «/» («Desenvolvimento/Deploy»)
// nem a que tem um hífen não separável (U+2011, «Pré‑release»), e o overflow-wrap partia-a a meio, sem hífen.
// Cada parte fica num inline-block («Desenvolvimento/», «Deploy»; «Pré‑», «release»), onde a hifenização volta a
// valer; entre as partes entra o <wbr>, e a «/» ou o hífen ficam sempre no fim da parte de antes. O texto não muda.
function QuebrasFase({texto}: {texto: string}): ReactNode {
  return texto.split(/([^\s/\u2011]+(?:[/\u2011][^\s/\u2011]+)+)/).map((pedaco, i) =>
    i % 2 === 0 ? (
      pedaco
    ) : (
      <React.Fragment key={i}>
        {pedaco.split(/(?<=[/\u2011])/).map((p, j) => (
          <React.Fragment key={j}>
            {j > 0 && <wbr />}
            <span className={styles.parte}>{p}</span>
          </React.Fragment>
        ))}
      </React.Fragment>
    ),
  );
}

type Props = {
  c: TCartao;
  nivel: Nivel | '';
  aberto: boolean;
  colunasDe: (m: Momento) => string[];
  nomeColuna: (id: string) => string;
  onAbrir: (k: string) => void;
};

export default function Cartao({c, nivel, aberto, colunasDe, nomeColuna, onAbrir}: Props): ReactNode {
  const {h} = c;
  const mo = c.momentos.map((i) => h.momentos[i]);
  const slas = mo.map((m) => m.sla).filter(Boolean);
  const nv = doNivel(h, nivel);
  const semNiveis = h.nivel.forma === 'sem-niveis' || h.nivel.forma === 'ausente';
  // outras colunas da vista com a mesma história nesta faixa (todos os momentos em que o papel aparece),
  // e na vista ágil também as cerimónias inferidas da história
  const outras = [
    ...new Set([...h.momentos.filter((m) => m.papeis.includes(c.papel)).flatMap(colunasDe), ...c.inferidas]),
  ].filter((f) => f !== c.fase);
  return (
    <button
      type="button"
      className={clsx(styles.cartao, nv?.leve && styles.cartaoLeve)}
      data-k={c.k}
      data-historia={h.id}
      data-papel={c.papel}
      data-fase={c.fase}
      data-inferido={c.inferida ? 'true' : undefined}
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
        {c.inferida && (
          <span
            className={clsx(styles.tag, styles.tagInferido)}
            title={translate({
              id: 'lifecycleMap.card.inferred.title',
              message: 'Cerimónia inferida pela atividade da história, e não pelo trigger',
            })}>
            {translate({id: 'lifecycleMap.card.inferred', message: 'inferido'})}
          </span>
        )}
      </span>
      <span className={styles.cartaoTitulo} data-conteudo="">
        <Quebras texto={h.titulo} />
      </span>
      {!c.inferida && (
        <span className={styles.cartaoMeta}>
          <b>{translate({id: 'lifecycleMap.card.phase', message: 'Fase'})}</b>
          {/* cada nome de fase uma só vez, pela ordem da primeira ocorrência (SHI-205) */}
          <span data-conteudo="">
            <QuebrasFase texto={[...new Set(mo.map((m) => m.fase))].join(' · ')} />
          </span>
        </span>
      )}
      {slas.length > 0 && (
        <span className={styles.cartaoMeta}>
          <b>{translate({id: 'lifecycleMap.card.sla', message: 'SLA'})}</b>
          <span data-conteudo="">
            <Quebras texto={slas.join(' · ')} />
          </span>
        </span>
      )}
      {outras.length > 0 && (
        <span className={styles.cartaoTambem}>
          {translate(
            {id: 'lifecycleMap.card.alsoIn', message: 'também em {phases}'},
            {phases: outras.map(nomeColuna).join(', ')},
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
