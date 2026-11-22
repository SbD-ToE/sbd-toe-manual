// Detalhe de um cartão, aberto no sítio (00-especificacao.md §7.3). Os rótulos das secções 4 a 8 vêm do
// próprio cânone (rotulos.*, nivel.rotulo), por isso no EN são os da tradução. O texto é HTML restrito do
// índice (§5.1): só <strong>, <em>, <code>, <a href> e <br>, com o resto escapado pelo plugin.
import React, {type ReactNode} from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import {translate} from '@docusaurus/Translate';
import {NIVEIS, type Capitulo, type Cartao, type Item, type Nivel} from './estado';
import styles from './CicloDeVida.module.css';

type Props = {
  c: Cartao;
  cap: Capitulo | undefined;
  nivel: Nivel | '';
  nomeFase: (id: string) => string;
  onFechar: () => void;
};

const html = (s: string) => ({dangerouslySetInnerHTML: {__html: s}});
const ponto = (s: string) => s.replace(/[.:]\s*$/, '');

function Lista({itens, caixa}: {itens: Item[]; caixa?: boolean}): ReactNode {
  return (
    <ul className={clsx(caixa && styles.check)}>
      {itens.map((it, i) => (
        <li key={i}>
          <span {...html(it.html)} />
          {it.sub.length > 0 && <Lista itens={it.sub} />}
        </li>
      ))}
    </ul>
  );
}

function Proporcionalidade({c, nivel}: {c: Cartao; nivel: Nivel | ''}): ReactNode {
  const p = c.h.nivel;
  if (p.forma === 'ausente')
    return (
      <p className={styles.detalheNota}>
        {translate({
          id: 'lifecycleMap.detail.noProportionality',
          message: 'Esta história não tem tabela de proporcionalidade no capítulo.',
        })}
      </p>
    );
  const aspetos = p.aspetos ?? [];
  const titulo = p.rotulo ? <h4>{ponto(p.rotulo)}</h4> : null;
  if (p.forma === 'sem-niveis')
    return (
      <>
        {titulo}
        <div className={clsx(styles.tabela, aspetos.length > 3 && styles.tabelaLarga)}>
          <table>
            <thead>
              <tr>
                {aspetos.map((a, i) => (
                  <th key={i} scope="col">
                    {a}
                  </th>
                ))}
              </tr>
            </thead>
            <tbody>
              {(p.tabela ?? []).map((linha, i) => (
                <tr key={i}>
                  {linha.map((cel, j) => (
                    <td key={j} {...html(cel)} />
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </>
    );
  return (
    <>
      {titulo}
      <div className={clsx(styles.tabela, aspetos.length + 1 > 3 && styles.tabelaLarga)}>
        <table>
          <thead>
            <tr>
              <th scope="col">{translate({id: 'lifecycleMap.filter.level', message: 'Nível'})}</th>
              {aspetos.map((a, i) => (
                <th key={i} scope="col">
                  {a}
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {NIVEIS.map((n) => (
              <tr key={n} className={clsx(nivel === n && styles.linhaMarcada)}>
                <th scope="row">
                  {n}
                  {nivel === n && (
                    <span className={styles.sr}>
                      {' '}
                      ({translate({id: 'lifecycleMap.detail.levelSelected', message: 'Nível {level} escolhido'}, {level: n})})
                    </span>
                  )}
                </th>
                {(p.niveis?.[n] ?? aspetos.map(() => '')).map((v, i) => (
                  <td key={i} {...html(v || '—')} />
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </>
  );
}

export default function Detalhe({c, cap, nivel, nomeFase, onFechar}: Props): ReactNode {
  const {h} = c;
  const esp = h.especializacoes.filter((s) => s.id.startsWith(`${c.papel}:`)).map((s) => s.rotulo);
  return (
    <div
      className={styles.detalhe}
      id={`det-${c.k}`}
      role="region"
      aria-label={`${h.us} ${h.titulo}`}
      tabIndex={-1}
      data-conteudo="">
      <button type="button" className={styles.fechar} onClick={onFechar}>
        <span aria-hidden="true">✕ </span>
        {translate({id: 'lifecycleMap.detail.close', message: 'Fechar'})}
      </button>
      <p className={clsx('sl-eyebrow', styles.detalheEyebrow)}>
        <span>{translate({id: 'lifecycleMap.card.chapter', message: 'Cap. {number}'}, {number: h.cap})}</span>
        {cap && (
          <>
            <span className="sl-eyebrow__sep" aria-hidden="true">·</span>
            <span>{cap.titulo}</span>
          </>
        )}
        <span className="sl-eyebrow__sep" aria-hidden="true">·</span>
        <span>{h.us}</span>
      </p>
      <h3 className={styles.detalheTitulo}>{h.titulo}</h3>

      <p className={styles.detalheNota}>
        <span className={styles.mono}>{translate({id: 'lifecycleMap.detail.voice', message: 'Voz da história'})}</span>{' '}
        {h.voz}
        {esp.length > 0 && (
          <>
            {' · '}
            <span className={styles.mono}>
              {translate({id: 'lifecycleMap.detail.specialisation', message: 'Especialização'})}
            </span>{' '}
            {esp.join(', ')}
          </>
        )}
      </p>

      <div className={clsx(styles.tabela, styles.tabelaLarga)}>
        <table>
          <thead>
            <tr>
              <th scope="col">{translate({id: 'lifecycleMap.card.phase', message: 'Fase'})}</th>
              <th scope="col">{translate({id: 'lifecycleMap.detail.phaseOnMap', message: 'Fase no mapa'})}</th>
              <th scope="col">{translate({id: 'lifecycleMap.detail.trigger', message: 'Trigger'})}</th>
              <th scope="col">{translate({id: 'lifecycleMap.detail.responsible', message: 'Responsável'})}</th>
              <th scope="col">{translate({id: 'lifecycleMap.card.sla', message: 'SLA'})}</th>
            </tr>
          </thead>
          <tbody>
            {h.momentos.map((m, i) => {
              const deste = c.momentos.includes(i);
              return (
                <tr key={i} className={clsx(deste && styles.linhaMarcada)}>
                  <th scope="row">
                    {m.fase}
                    {deste && (
                      <span className={styles.esteCartao}>
                        {translate({id: 'lifecycleMap.detail.thisCard', message: 'este cartão'})}
                      </span>
                    )}
                  </th>
                  <td>{m.fases.map(nomeFase).join(' + ')}</td>
                  <td {...html(m.trigger)} />
                  <td>{m.responsavel}</td>
                  <td>{m.sla || '—'}</td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>

      {h.contexto && <p className={styles.detalheContexto} {...html(h.contexto)} />}
      {h.historia && <p className={styles.detalheHistoria} {...html(h.historia)} />}

      <div className={styles.detalheColunas}>
        <div>
          {h.bdd.length > 0 && (
            <>
              {h.rotulos.bdd && <h4>{ponto(h.rotulos.bdd)}</h4>}
              {h.bdd.map((cenario, i) => (
                <div key={i} className={styles.cenario}>
                  {cenario.map((l, j) => (
                    <p key={j} {...html(l)} />
                  ))}
                </div>
              ))}
            </>
          )}
          {h.checklist.length > 0 && (
            <>
              {h.rotulos.checklist && <h4>{ponto(h.rotulos.checklist)}</h4>}
              <Lista itens={h.checklist} caixa />
            </>
          )}
        </div>
        <div>
          {h.evidencias.length > 0 && (
            <>
              {h.rotulos.evidencias && <h4>{ponto(h.rotulos.evidencias)}</h4>}
              <Lista itens={h.evidencias} />
            </>
          )}
          <Proporcionalidade c={c} nivel={nivel} />
        </div>
      </div>

      <Link className={styles.ler} to={h.url}>
        {translate({id: 'lifecycleMap.detail.readInChapter', message: 'Ler no capítulo'})}
        <span aria-hidden="true"> →</span>
      </Link>
    </div>
  );
}
