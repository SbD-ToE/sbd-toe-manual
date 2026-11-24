// Componente da rota /ciclo-de-vida (/en/ciclo-de-vida), criada pelo plugin src/plugins/ciclo-de-vida
// com addRoute; o «_» no nome impede o plugin de páginas de criar outra rota para este ficheiro.
// O índice chega por props.indice (createData). A página é a forma «mapa» de 00-especificacao.md §7–§9:
// barra de filtros, trilho das fases e uma faixa por papel; os filtros vivem no URL (§8).
// A vista ágil (00-especificacao-agil.md §4) usa a mesma página e o mesmo índice: muda as colunas (os eventos do
// Scrum e as duas colunas fora do Scrum), a entrada e a quebra do trilho; a vista vai no URL (?vista=agil).
import React, {useCallback, useEffect, useLayoutEffect, useMemo, useRef, useState, type ReactNode} from 'react';
import clsx from 'clsx';
import Layout from '@theme/Layout';
import {translate} from '@docusaurus/Translate';
import {useHistory, useLocation} from '@docusaurus/router';
import useIsBrowser from '@docusaurus/useIsBrowser';
import {usePluralForm} from '@docusaurus/theme-common';
import {
  VAZIO,
  cartoes,
  colunasDe as colunasDaVista,
  escrever,
  filtrar,
  ler,
  type Estado,
  type Indice,
  type Vista,
} from '@site/src/components/CicloDeVida/estado';
import {fases as rotulosFases} from '@site/src/components/CicloDeVida/fases';
import {eventos as rotulosEventos} from '@site/src/components/CicloDeVida/eventos';
import SeletorVista from '@site/src/components/CicloDeVida/SeletorVista';
import BarraFiltros from '@site/src/components/CicloDeVida/BarraFiltros';
import Trilho from '@site/src/components/CicloDeVida/Trilho';
import Faixa from '@site/src/components/CicloDeVida/Faixa';
import styles from '@site/src/components/CicloDeVida/CicloDeVida.module.css';

export default function CicloDeVida({indice}: {indice: Indice}): ReactNode {
  const isBrowser = useIsBrowser();
  const location = useLocation();
  const history = useHistory();
  const {selectMessage} = usePluralForm();

  // os cartões das duas vistas, calculados uma vez cada
  const porVista = useMemo(() => {
    const m = new Map<Vista, ReturnType<typeof cartoes>>();
    return (v: Vista) => {
      if (!m.has(v)) m.set(v, cartoes(indice, v));
      return m.get(v)!;
    };
  }, [indice]);
  const capitulo = useCallback((id: string) => indice.capitulos.find((c) => c.id === id), [indice]);

  // No SSR e no primeiro render do cliente o estado é o vazio (a vista do ciclo de vida); o do URL aplica-se
  // quando isBrowser passa a true. Assim o HTML do servidor e a hidratação coincidem (§8).
  const lido = useMemo(
    () => (isBrowser ? ler(location.search, indice, porVista) : {estado: VAZIO, query: ''}),
    [isBrowser, location.search, indice, porVista],
  );
  const estado = lido.estado;
  const agil = estado.vista === 'agil';
  const todos = porVista(estado.vista);
  const colunas = agil ? rotulosEventos() : rotulosFases();
  const nomeColuna = (id: string) => colunas.find((f) => f.id === id)?.nome ?? id;
  const colunasDe = colunasDaVista(estado.vista);

  // valores inválidos e formas não canónicas: corrige o URL sem deixar passo no histórico
  useEffect(() => {
    if (isBrowser && lido.query !== location.search)
      history.replace({pathname: location.pathname, search: lido.query, hash: location.hash});
  }, [isBrowser, lido.query, location.search, location.pathname, location.hash, history]);

  // uma escolha do leitor = um push com a query toda
  const mudar = useCallback(
    (mudanca: Partial<Estado>) => {
      const novo = {...estado, ...mudanca};
      history.push({pathname: location.pathname, search: escrever(novo, new URLSearchParams(location.search))});
    },
    [estado, history, location.pathname, location.search],
  );

  // faixas abertas à mão, antes de escolher o papel (decisão mapa-sem-papel = b)
  const [abertasMao, setAbertasMao] = useState<Set<string>>(() => new Set());
  const alternar = useCallback(
    (papel: string, aberta: boolean) => {
      const abrir = !aberta;
      setAbertasMao((s) => {
        const n = new Set(s);
        if (abrir) n.add(papel);
        else n.delete(papel);
        return n;
      });
      // recolher a faixa do cartão aberto fecha também o detalhe
      if (!abrir && estado.abrir.split('~')[1] === papel) mudar({abrir: ''});
    },
    [estado.abrir, mudar],
  );

  // altura da barra de filtros, para o trilho e os rótulos das faixas ficarem presos por baixo dela;
  // a largura volta a posicionar o detalhe. Mede-se já no layout (e outra vez antes de levar o detalhe
  // ao ecrã): só com o ResizeObserver, uma ligação com abrir= rolava com a altura de reserva da barra.
  const barra = useRef<HTMLDivElement>(null);
  const [largura, setLargura] = useState(0);
  const medirBarra = useCallback(() => {
    const el = barra.current;
    const main = el?.parentElement;
    if (!el || !main) return;
    main.style.setProperty('--ciclo-barra-h', `${el.offsetHeight}px`);
    const cab = main.querySelector<HTMLElement>('[data-cab]');
    if (cab?.offsetHeight) main.style.setProperty('--ciclo-cab-h', `${cab.offsetHeight}px`);
  }, []);
  useLayoutEffect(() => {
    const el = barra.current;
    if (!el) return undefined;
    medirBarra();
    const ro = new ResizeObserver(() => {
      medirBarra();
      setLargura(window.innerWidth);
    });
    ro.observe(el);
    return () => ro.disconnect();
  }, [medirBarra]);

  // mudar de vista é uma escolha do leitor: um push, mantém papel, nível e capítulo e tira o abrir,
  // porque a coluna do cartão aberto não existe na outra vista (§4.1). O foco fica no botão carregado.
  const mudarVista = useCallback((vista: Vista) => mudar({vista, abrir: ''}), [mudar]);

  // Foco nos botões dos controlos segmentados (Vista e Nível, [role=group]): o SkipToContent do Docusaurus põe o
  // foco no topo da página a cada push sem hash (ressalva R1 da SHI-219). Guarda-se o botão carregado (o clique
  // também chega pelo Enter e pelo Espaço) e devolve-se-lhe o foco depois da mudança de URL. O efeito é desta página,
  // que está acima do Layout, e por isso corre depois do do SkipToContent.
  const focoDepois = useRef<HTMLElement | null>(null);
  const guardarFoco = useCallback((ev: React.MouseEvent) => {
    focoDepois.current = (ev.target as HTMLElement).closest<HTMLElement>('[role="group"] > button');
  }, []);
  useEffect(() => {
    const el = focoDepois.current;
    focoDepois.current = null;
    if (el?.isConnected && document.activeElement !== el) el.focus({preventScroll: true});
  }, [location]);

  // fechar (botão, Esc ou voltar): o foco volta ao cartão; abrir: o foco vai para o detalhe.
  // Ao mudar de vista o cartão fechado já não está no mapa, e o foco fica onde estava.
  const anterior = useRef('');
  const vistaAnterior = useRef<Vista>(estado.vista);
  useEffect(() => {
    const antes = anterior.current;
    const mudouVista = vistaAnterior.current !== estado.vista;
    anterior.current = estado.abrir;
    vistaAnterior.current = estado.vista;
    if (antes === estado.abrir) return;
    if (estado.abrir) {
      const det = document.getElementById(`det-${estado.abrir}`);
      if (det) {
        medirBarra();
        det.focus({preventScroll: true});
        det.scrollIntoView({block: 'nearest'});
      }
    } else if (antes && !mudouVista) {
      document.querySelector<HTMLElement>(`[data-k="${CSS.escape(antes)}"]`)?.focus();
    }
  }, [estado.abrir, estado.vista, medirBarra]);

  useEffect(() => {
    if (!estado.abrir) return undefined;
    const tecla = (ev: KeyboardEvent) => {
      if (ev.key === 'Escape') mudar({abrir: ''});
    };
    document.addEventListener('keydown', tecla);
    return () => document.removeEventListener('keydown', tecla);
  }, [estado.abrir, mudar]);

  // o 0 vai à parte: em pt o Intl.PluralRules põe-no na forma «one», e sairia «Uma história» (D3 da SHI-160)
  const contaHistorias = (n: number) =>
    n === 0
      ? translate({id: 'lifecycleMap.count.stories.none', message: 'Nenhuma história'})
      : selectMessage(
          n,
          translate({id: 'lifecycleMap.count.stories', message: 'Uma história|{count} histórias'}, {count: n}),
        );
  const contaCartoes = (n: number) =>
    n === 0
      ? translate({id: 'lifecycleMap.count.cards.none', message: 'Nenhum cartão'})
      : selectMessage(n, translate({id: 'lifecycleMap.count.cards', message: 'Um cartão|{count} cartões'}, {count: n}));

  const doCap = filtrar(todos, {papel: '', cap: estado.cap});
  const visiveis = filtrar(doCap, {papel: estado.papel, cap: ''});
  const historiasDe = (lista: typeof todos) => new Set(lista.map((c) => c.h.id)).size;
  const porColuna: Record<string, number> = {};
  for (const f of colunas) porColuna[f.id] = historiasDe(visiveis.filter((c) => c.fase === f.id));
  const papeis = indice.papeis.map((p) => ({...p, n: historiasDe(doCap.filter((c) => c.papel === p.id))}));
  const noManual = (id: string) => todos.filter((c) => c.papel === id).length;
  const faixas = estado.papel ? indice.papeis.filter((p) => p.id === estado.papel) : indice.papeis;
  const papelAberto = estado.abrir.split('~')[1] ?? '';
  const momentos = indice.historias.reduce((n, h) => n + h.momentos.length, 0);

  return (
    <Layout
      title={translate({id: 'lifecycleMap.title', message: 'Mapa do ciclo de vida'})}
      description={translate({
        id: 'lifecycleMap.description',
        message: 'As user stories do manual ao longo do ciclo de vida: o que cabe a cada papel, em que fase e a que nível.',
      })}>
      <main
        className={clsx('sl-ciclo', styles.ciclo, agil && styles.agil)}
        data-vista={agil ? 'agil' : 'ciclo'}
        data-historias={indice.historias.length}
        data-momentos={momentos}
        data-cartoes={todos.length}
        onClickCapture={guardarFoco}>
        <header className={styles.cabecalho}>
          <p className="sl-eyebrow">
            <span>{translate({id: 'doc.eyebrow.manual', message: 'Manual'})}</span>
          </p>
          <h1 className={styles.titulo}>{translate({id: 'lifecycleMap.title', message: 'Mapa do ciclo de vida'})}</h1>
          <p className={styles.entrada}>
            {agil
              ? translate({
                  id: 'lifecycleMap.lead.agile',
                  message:
                    'Cada cartão é uma user story de um capítulo, no evento do Scrum em que acontece e na faixa do papel que a faz. Operação e Cadência organizacional ficam fora do sprint. Escolha o seu papel e o nível da aplicação.',
                })
              : translate({
                  id: 'lifecycleMap.lead',
                  message:
                    'Cada cartão é uma user story de um capítulo, na fase em que acontece e na faixa do papel que a faz. Escolha o seu papel e o nível da aplicação.',
                })}
          </p>
          <SeletorVista vista={estado.vista} onMudar={mudarVista} />
        </header>
        <div ref={barra} className={styles.barraFixa}>
          <BarraFiltros
            estado={estado}
            papeis={papeis}
            capitulos={indice.capitulos}
            contagem={`${contaHistorias(historiasDe(visiveis))} · ${contaCartoes(visiveis.length)}`}
            contaHistorias={contaHistorias}
            onMudar={mudar}
          />
        </div>
        <div className={styles.mapa}>
          <Trilho colunas={colunas} porColuna={porColuna} agil={agil} />
          {faixas.map((p) => (
            <Faixa
              key={p.id}
              papel={p}
              cartoes={visiveis.filter((c) => c.papel === p.id)}
              noManual={noManual(p.id)}
              colunas={colunas}
              agil={agil}
              aberta={Boolean(estado.papel) || abertasMao.has(p.id) || papelAberto === p.id}
              recolhivel={!estado.papel}
              nivel={estado.nivel}
              abrir={estado.abrir}
              largura={largura}
              capitulo={capitulo}
              colunasDe={colunasDe}
              nomeColuna={nomeColuna}
              contaHistorias={contaHistorias}
              onAlternar={alternar}
              onAbrir={(k) => mudar({abrir: estado.abrir === k ? '' : k})}
              onFechar={() => mudar({abrir: ''})}
            />
          ))}
        </div>
      </main>
    </Layout>
  );
}
