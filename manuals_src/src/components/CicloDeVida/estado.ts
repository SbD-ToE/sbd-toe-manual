// Estado do Mapa do ciclo de vida: tipos do índice (00-especificacao.md §5.1), filtros e vista no URL (§8;
// 00-especificacao-agil.md §4.1) e cartões (§7.2). Sem React: a página lê o estado do location e escreve-o com history.push/replace.

export type Nivel = 'L1' | 'L2' | 'L3';
export const NIVEIS: Nivel[] = ['L1', 'L2', 'L3'];

export type Momento = {
  fase: string;
  fases: string[];
  trigger: string;
  responsavel: string;
  sla: string;
  responsaveis: string[];
  papeis: string[];
  eventos: string[]; // ids de indice.eventos: as colunas da vista ágil (00-especificacao-agil.md §3.1)
};
export type Item = {html: string; sub: Item[]; caixa?: boolean};
export type Proporcionalidade = {
  forma: 'colunas' | 'linhas' | 'texto' | 'sem-niveis' | 'ausente';
  rotulo?: string;
  aspetos?: string[];
  niveis?: Partial<Record<Nivel, string[]>>;
  leve?: Partial<Record<Nivel, string>>;
  tabela?: string[][];
};
export type Historia = {
  id: string;
  cap: string;
  us: string;
  titulo: string;
  url: string;
  voz: string | null;
  papeisVoz: string[];
  especializacoes: {id: string; rotulo: string}[];
  momentos: Momento[];
  // cerimónias inferidas pela atividade da história, só na vista ágil (00-especificacao-agil.md §10.1); o plugin
  // omite o campo quando não há nenhuma
  inferidas?: Inferida[];
  contexto: string | null;
  historia: string | null;
  bdd: string[][];
  checklist: Item[];
  evidencias: Item[];
  rotulos: {bdd: string | null; checklist: string | null; evidencias: string | null};
  nivel: Proporcionalidade;
};
export type Inferida = {evento: string; motivo: string; provisorio: string | null};
export type Papel = {id: string; rotulo: string; especializacoes: {id: string; rotulo: string}[]};
export type Capitulo = {id: string; titulo: string; url: string};
export type Indice = {
  versao: number;
  idioma: 'pt' | 'en';
  fases: {id: string; ordem: number; faixa: string; rotulo: string; descricao: string}[];
  eventos: {id: string; ordem: number; faixa: string; rotulo: string; descricao: string}[];
  papeis: Papel[];
  capitulos: Capitulo[];
  historias: Historia[];
};

// A vista: '' é a do ciclo de vida (por omissão, não se escreve no URL), 'agil' a dos eventos do Scrum
export type Vista = '' | 'agil';
export type Estado = {vista: Vista; papel: string; nivel: Nivel | ''; cap: string; abrir: string};
export const VAZIO: Estado = {vista: '', papel: '', nivel: '', cap: '', abrir: ''};

// Colunas de um momento na vista: as fases (ciclo de vida) ou os eventos (ágil)
export const colunasDe = (vista: Vista) => (m: Momento): string[] => (vista === 'agil' ? m.eventos : m.fases);

// Um cartão = (história, papel, coluna), com os momentos da história que caem nessa coluna e nessa faixa.
// A coluna é uma fase na vista do ciclo de vida e um evento na vista ágil; fica em «fase» (o data-fase do cartão).
// Na vista ágil, «inferidas» são os eventos inferidos da história (para «também em») e «inferida» marca o cartão
// que nasce de uma inferência, sem momentos (§10.2); na vista do ciclo de vida, [] e sem «inferida».
export type Cartao = {
  k: string;
  h: Historia;
  papel: string;
  fase: string;
  momentos: number[];
  resp: boolean;
  inferidas: string[];
  inferida?: {motivo: string; provisorio: string | null};
};

export const chave = (historia: string, papel: string, fase: string): string => `${historia}~${papel}~${fase}`;

// Todos os cartões do índice na vista, pela ordem do cânone. Os filtros aplicam-se depois (filtrar).
// Na vista ágil, cada inferência da história dá mais um cartão em cada faixa onde a história já tem cartões
// (a união de momentos[].papeis), logo a seguir aos da história.
export function cartoes(indice: Indice, vista: Vista = ''): Cartao[] {
  const m = new Map<string, Cartao>();
  const colunas = colunasDe(vista);
  for (const h of indice.historias) {
    const inferidas = vista === 'agil' ? h.inferidas ?? [] : [];
    const evInferidos = inferidas.map((x) => x.evento);
    h.momentos.forEach((mo, i) => {
      for (const f of colunas(mo))
        for (const p of mo.papeis) {
          const k = chave(h.id, p, f);
          let c = m.get(k);
          if (!c) {
            c = {k, h, papel: p, fase: f, momentos: [], resp: false, inferidas: evInferidos};
            m.set(k, c);
          }
          c.momentos.push(i);
          if (mo.responsaveis.includes(p)) c.resp = true;
        }
    });
    const papeis = [...new Set(h.momentos.flatMap((mo) => mo.papeis))];
    for (const {evento, motivo, provisorio} of inferidas)
      for (const p of papeis) {
        const k = chave(h.id, p, evento);
        if (!m.has(k))
          m.set(k, {k, h, papel: p, fase: evento, momentos: [], resp: false, inferidas: evInferidos, inferida: {motivo, provisorio}});
      }
  }
  return [...m.values()];
}

export const filtrar = (todos: Cartao[], e: Pick<Estado, 'papel' | 'cap'>): Cartao[] =>
  todos.filter((c) => (!e.papel || c.papel === e.papel) && (!e.cap || c.h.cap === e.cap));

// ---------- URL ----------

const ORDEM = ['vista', 'papel', 'nivel', 'cap', 'abrir'] as const;

// Lê a query: devolve o estado válido e a query canónica. Se a canónica for diferente da que veio,
// a página corrige o URL com replace (valores inválidos, minúsculas, «5» → «05», prefixo de papel, «ágil» → «agil»).
// O «abrir» confere-se com os cartões da vista do URL (cartoesDe).
export function ler(search: string, indice: Indice, cartoesDe: (v: Vista) => Cartao[]): {estado: Estado; query: string} {
  const q = new URLSearchParams(search);
  const e: Estado = {...VAZIO};

  const vista = (q.get('vista') ?? '').trim().toLowerCase().normalize('NFC');
  if (vista === 'agil' || vista === 'ágil') e.vista = 'agil';

  const papel = (q.get('papel') ?? '').trim().toLowerCase();
  if (papel) {
    const ids = indice.papeis.map((p) => p.id);
    const exato = ids.find((id) => id === papel);
    const prefixo = ids.filter((id) => id.startsWith(papel));
    e.papel = exato ?? (prefixo.length === 1 ? prefixo[0] : '');
  }

  const nivel = (q.get('nivel') ?? '').trim().toUpperCase();
  if ((NIVEIS as string[]).includes(nivel)) e.nivel = nivel as Nivel;

  const cap = (q.get('cap') ?? '').trim();
  if (/^\d{1,2}$/.test(cap)) {
    const id = cap.padStart(2, '0');
    if (indice.capitulos.some((c) => c.id === id)) e.cap = id;
  }

  const abrir = (q.get('abrir') ?? '').trim();
  if (abrir && filtrar(cartoesDe(e.vista), e).some((c) => c.k === abrir)) e.abrir = abrir;

  return {estado: e, query: escrever(e, q)};
}

// Query canónica: vista, papel, nivel, cap, abrir, só os que têm valor, com «~» sem codificar.
// Outros parâmetros (por exemplo o docusaurus-theme) ficam no fim, como vieram.
export function escrever(e: Estado, antes?: URLSearchParams): string {
  const partes: string[] = [];
  for (const nome of ORDEM) if (e[nome]) partes.push(`${nome}=${encodeURIComponent(e[nome])}`);
  if (antes)
    antes.forEach((v, nome) => {
      if (!(ORDEM as readonly string[]).includes(nome))
        partes.push(`${encodeURIComponent(nome)}=${encodeURIComponent(v)}`);
    });
  return partes.length ? `?${partes.join('&')}` : '';
}

// ---------- texto dos cartões ----------

// O que o nível exige, numa linha: «Obrigatório?: Recomendado · Ajustes: …» (HTML restrito do índice).
export function doNivel(h: Historia, n: Nivel | ''): {html: string; leve: string} | null {
  const p = h.nivel;
  if (!n || !p.niveis || !p.niveis[n]) return null;
  const aspetos = p.aspetos ?? [];
  const partes = p.niveis[n]!.map((cel, i) => {
    const v = semLigacoes(cel).trim();
    if (!v) return '';
    return aspetos.length > 1 && aspetos[i] ? `${esc(aspetos[i])}: ${v}` : v;
  }).filter(Boolean);
  return {html: partes.join(' · '), leve: p.leve?.[n] ?? ''};
}

const esc = (s: string): string =>
  s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');

// Dentro de um botão não pode haver ligações: tira <a> e passa <br> a espaço, e deixa <em>, <strong> e <code>.
export const semLigacoes = (html: string): string =>
  html.replace(/<\/?a\b[^>]*>/g, '').replace(/<br\s*\/?>/g, ' ');
