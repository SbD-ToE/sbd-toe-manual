// Estado do Mapa do ciclo de vida: tipos do índice (00-especificacao.md §5.1), filtros no URL (§8)
// e cartões (§7.2). Sem React: a página lê o estado do location e escreve-o com history.push/replace.

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
  contexto: string | null;
  historia: string | null;
  bdd: string[][];
  checklist: Item[];
  evidencias: Item[];
  rotulos: {bdd: string | null; checklist: string | null; evidencias: string | null};
  nivel: Proporcionalidade;
};
export type Papel = {id: string; rotulo: string; especializacoes: {id: string; rotulo: string}[]};
export type Capitulo = {id: string; titulo: string; url: string};
export type Indice = {
  versao: number;
  idioma: 'pt' | 'en';
  fases: {id: string; ordem: number; faixa: string; rotulo: string; descricao: string}[];
  papeis: Papel[];
  capitulos: Capitulo[];
  historias: Historia[];
};

export type Estado = {papel: string; nivel: Nivel | ''; cap: string; abrir: string};
export const VAZIO: Estado = {papel: '', nivel: '', cap: '', abrir: ''};

// Um cartão = (história, papel, fase), com os momentos da história que caem nessa fase e nessa faixa.
export type Cartao = {
  k: string;
  h: Historia;
  papel: string;
  fase: string;
  momentos: number[];
  resp: boolean;
};

export const chave = (historia: string, papel: string, fase: string): string => `${historia}~${papel}~${fase}`;

// Todos os cartões do índice, pela ordem do cânone. Os filtros aplicam-se depois (filtrar).
export function cartoes(indice: Indice): Cartao[] {
  const m = new Map<string, Cartao>();
  for (const h of indice.historias)
    h.momentos.forEach((mo, i) => {
      for (const f of mo.fases)
        for (const p of mo.papeis) {
          const k = chave(h.id, p, f);
          let c = m.get(k);
          if (!c) {
            c = {k, h, papel: p, fase: f, momentos: [], resp: false};
            m.set(k, c);
          }
          c.momentos.push(i);
          if (mo.responsaveis.includes(p)) c.resp = true;
        }
    });
  return [...m.values()];
}

export const filtrar = (todos: Cartao[], e: Pick<Estado, 'papel' | 'cap'>): Cartao[] =>
  todos.filter((c) => (!e.papel || c.papel === e.papel) && (!e.cap || c.h.cap === e.cap));

// ---------- URL ----------

const ORDEM = ['papel', 'nivel', 'cap', 'abrir'] as const;

// Lê a query: devolve o estado válido e a query canónica. Se a canónica for diferente da que veio,
// a página corrige o URL com replace (valores inválidos, minúsculas, «5» → «05», prefixo de papel).
export function ler(search: string, indice: Indice, todos: Cartao[]): {estado: Estado; query: string} {
  const q = new URLSearchParams(search);
  const e: Estado = {...VAZIO};

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
  if (abrir && filtrar(todos, e).some((c) => c.k === abrir)) e.abrir = abrir;

  return {estado: e, query: escrever(e, q)};
}

// Query canónica: papel, nivel, cap, abrir, só os que têm valor, com «~» sem codificar.
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
