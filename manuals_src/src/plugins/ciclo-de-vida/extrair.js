// Leitura das user stories dos aplicacao-lifecycle.md (PT e EN) e dos papéis de _roles.yaml.
// Portado de design/iteracao-2/scripts/extrair-user-stories.mjs (SHI-149), com as mesmas regras de parsing
// (00-especificacao.md §6, SHI-152). Diferenças em relação ao inventário:
//   - não há o ramo de aproximação dos papéis (palavras soltas, singular): só as formas de _roles.yaml (§6.4);
//   - não se recolhem as irregularidades, só os erros estruturais, que fazem falhar o build (§6.3).
import fs from 'node:fs';
import path from 'node:path';
import {createRequire} from 'node:module';
import {parseMarkdownHeadingId, createSlugger} from '@docusaurus/utils';

// O js-yaml é o que o Docusaurus traz (dependência de @docusaurus/utils); este é o único sítio que o importa (§4.3).
function carregarYaml(siteDir) {
  try {
    return createRequire(path.join(siteDir, 'package.json'))('js-yaml');
  } catch {
    throw new Error('js-yaml não encontrado: o plugin ciclo-de-vida usa o que o Docusaurus traz');
  }
}

// ---------------------------------------------------------------- rótulos

const LABELS = {
  pt: {
    contexto: [/^\*\*Contexto\.?\*\*/],
    historia: [/^\*\*História\.?\*\*/],
    sdlc: [/^\*\*Integração no SDLC\.?\*\*/],
    voz: {abre: /^Como\s+/, fecha: /,?\s+quero\b/},
  },
  en: {
    contexto: [/^\*\*Context\.?\*\*/],
    historia: [/^\*\*Story\.?\*\*/],
    sdlc: [/^\*\*Integration into the SDLC\.?\*\*/],
    voz: {abre: /^As\s+(?:an?\s+)?/, fecha: /,?\s+I\s+want\b/},
  },
};

// Título de user story: nível 3 ou 4, com «US-nn» no início do texto.
const STORY_RE = /^(#{3,4})\s+(?:[^\sA-Za-z*]+\s+)?(\*\*)?(US-?\d+[A-Za-z]?)\b\s*[-–—:]?\s*(.*?)\s*(?:\{#([^}]+)\})?\s*$/;
const HEADING_RE = /^(#{1,6})\s+(.*)$/;
const FENCE_RE = /^\s*(```|~~~)/;

// ---------------------------------------------------------------- utilitários

export const stripMd = (s) =>
  s
    .replace(/\*\*(.+?)\*\*/g, '$1')
    .replace(/(^|[^*])\*(?!\s)(.+?)\*/g, '$1$2')
    .replace(/`([^`]*)`/g, '$1')
    .replace(/\[([^\]]+)\]\([^)]*\)/g, '$1')
    .replace(/<br\s*\/?>/gi, ' ')
    .replace(/\s+/g, ' ')
    .trim();

export const splitRow = (line) => {
  let t = line.trim();
  if (t.startsWith('|')) t = t.slice(1);
  if (t.endsWith('|')) t = t.slice(0, -1);
  // separa por «|» que não estejam escapados nem dentro de `código`
  const cells = [];
  let cur = '';
  let inCode = false;
  for (let i = 0; i < t.length; i++) {
    const c = t[i];
    if (c === '`') inCode = !inCode;
    if (c === '|' && !inCode && t[i - 1] !== '\\') {
      cells.push(cur.trim());
      cur = '';
    } else cur += c;
  }
  cells.push(cur.trim());
  return cells;
};
const isSepRow = (line) => /^\s*\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?\s*$/.test(line);

// Lê uma tabela markdown a partir da linha i (salta linhas em branco iniciais).
function readTable(lines, i, stop) {
  while (i < stop && lines[i].trim() === '') i++;
  if (i >= stop || !lines[i].trim().startsWith('|')) return null;
  const start = i;
  const rows = [];
  while (i < stop && lines[i].trim().startsWith('|')) {
    rows.push(lines[i]);
    i++;
  }
  if (rows.length < 2 || !isSepRow(rows[1])) return {start, header: splitRow(rows[0]), rows: [], malformed: true};
  return {start, header: splitRow(rows[0]), rows: rows.slice(2).map(splitRow), malformed: false};
}

function findLabel(lines, from, to, regexes) {
  for (let i = from; i < to; i++) {
    for (const re of regexes) {
      const m = lines[i].trim().match(re);
      if (m) return {i, rotulo: m[0].replace(/\*\*/g, ''), resto: lines[i].trim().slice(m[0].length).trim()};
    }
  }
  return null;
}

// ---------------------------------------------------------------- parsing de uma página

export function capitulos(ptRoot) {
  return fs
    .readdirSync(ptRoot)
    .filter((d) => fs.existsSync(path.join(ptRoot, d, 'aplicacao-lifecycle.md')))
    .sort();
}

// Devolve as histórias do ficheiro e, para o texto dos cartões, as linhas com as de código em branco.
export function parseFile(file, lang, chapter) {
  const lines = fs.readFileSync(file, 'utf8').split(/\r?\n/);

  // Marca as linhas dentro de blocos de código (não contam como títulos nem campos).
  const inFence = new Array(lines.length).fill(false);
  let fence = null;
  for (let i = 0; i < lines.length; i++) {
    const m = lines[i].match(FENCE_RE);
    if (fence) {
      inFence[i] = true;
      if (m && lines[i].trim().startsWith(fence)) fence = null;
    } else if (m) {
      fence = m[1];
      inFence[i] = true;
    }
  }

  const heads = [];
  for (let i = 0; i < lines.length; i++) {
    if (inFence[i]) continue;
    const h = lines[i].match(HEADING_RE);
    if (h) heads.push({i, level: h[1].length, text: h[2]});
  }

  const stories = [];
  heads.forEach((h, k) => {
    const m = lines[h.i].match(STORY_RE);
    if (!m) return;
    // a história acaba no próximo título de nível <= ao seu (ou ao fim do ficheiro)
    let end = lines.length;
    for (let j = k + 1; j < heads.length; j++) {
      if (heads[j].level <= h.level) {
        end = heads[j].i;
        break;
      }
    }
    const body = [];
    for (let i = h.i + 1; i < end; i++) body.push(inFence[i] ? '' : lines[i]);
    stories.push(parseStory({lines: body, off: h.i + 1, m, heading: lines[h.i], lang, chapter, file}));
  });
  return stories;
}

function parseStory({lines, off, m, heading, lang, chapter, file}) {
  const L = LABELS[lang];
  const [, , negrito, us, rawTitle0] = m;
  const rawTitle = negrito ? rawTitle0.replace(/\*\*\s*$/, '') : rawTitle0;
  const titulo = stripMd(rawTitle);
  const n = lines.length;
  const erros = [];
  const avisos = [];

  // Âncora: o {#id} explícito do título (§6.2); sem ele, o slugger do Docusaurus, com aviso.
  let ancora = parseMarkdownHeadingId(heading.replace(/^#+\s+/, '')).id;
  if (!ancora) {
    ancora = createSlugger().slug(stripMd(`${us} - ${rawTitle}`));
    avisos.push(`título sem {#id}; âncora calculada «${ancora}»`);
  }

  const fHist = findLabel(lines, 0, n, L.historia);
  const fSdlc = findLabel(lines, 0, n, L.sdlc);

  // Voz: «Como **X** e **Y**, quero …»
  let voz = null;
  let papeis = [];
  if (fHist) {
    let j = fHist.i + 1;
    let txt = fHist.resto;
    while (!txt && j < n && lines[j].trim() === '') j++;
    if (!txt) {
      // a voz pode ocupar várias linhas até à linha em branco
      const acc = [];
      while (j < n && lines[j].trim() !== '') acc.push(lines[j++].trim());
      txt = acc.join(' ');
    }
    const a = txt.match(L.voz.abre);
    const f = txt.match(L.voz.fecha);
    if (a && f && f.index > a.index) {
      voz = txt.slice(a.index + a[0].length, f.index).trim();
      papeis = [...voz.matchAll(/\*\*(.+?)\*\*/g)].map((x) => x[1].trim());
      if (!papeis.length) papeis = [stripMd(voz)];
    } else {
      erros.push('sem papel na frase da história');
    }
  } else {
    erros.push('sem «História»');
  }

  // Integração no SDLC: Fase | Trigger | Responsável | SLA, por posição
  const sdlc = [];
  if (fSdlc) {
    const t = readTable(lines, fSdlc.i + 1, n);
    if (!t || t.malformed) {
      erros.push('«Integração no SDLC» sem tabela');
    } else {
      t.rows.forEach((r, k) => {
        sdlc.push({
          // stripMd tira a ênfase markdown das células antes de tudo o resto: a fase só se normaliza depois
          // (ver index.js), por isso «Alteração de *tools*» chega ao mapa como «Alteração de tools».
          fase: stripMd(r[0] || ''),
          trigger: stripMd(r[1] || ''),
          responsavel: stripMd(r[2] || ''),
          sla: stripMd(r[3] || ''),
          // linha do ficheiro (1 = primeira): título + cabeçalho + separador + k
          linha: off + t.start + 2 + k + 1,
        });
      });
      if (!sdlc.length) erros.push('tabela «Integração no SDLC» vazia');
      sdlc.forEach((r, k) => {
        if (!r.fase) erros.push(`linha SDLC ${k + 1} (linha ${r.linha}): fase vazia`);
      });
    }
  } else {
    erros.push('sem «Integração no SDLC»');
  }

  // Campos que aparecem duas vezes (sinal de duas histórias fundidas)
  for (const [k, res] of Object.entries({historia: L.historia, sdlc: L.sdlc})) {
    const c = lines.filter((l) => res.some((re) => re.test(l.trim()))).length;
    if (c > 1) erros.push(`campo «${k}» repetido (${c}×)`);
  }

  return {
    idioma: lang,
    capitulo: chapter,
    ficheiro: file,
    linha: off,
    us,
    ancora,
    titulo,
    // título com a marcação do cânone, para index.js o passar a texto sem perder o que está em `código`
    tituloMd: rawTitle,
    papeis_escritos: papeis,
    voz: voz ? stripMd(voz) : null,
    sdlc,
    erros,
    avisos,
  };
}

// ---------------------------------------------------------------- papéis (_roles.yaml)

export function carregarRoles(siteDir, ficheiro) {
  return carregarYaml(siteDir).load(fs.readFileSync(ficheiro, 'utf8'));
}

const slug = (s) =>
  s
    .normalize('NFD')
    .replace(/[̀-ͯ]/g, '')
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-|-$/g, '');

export function buildRoleIndex(doc) {
  const idx = new Map(); // slug -> {tipo, id, pt, en}
  const put = (form, entry) => {
    const k = slug(form);
    if (k && !idx.has(k)) idx.set(k, entry);
  };
  for (const r of doc.roles) {
    const base = {tipo: 'canonical', id: r.id, pt: r.name.pt, en: r.name.en};
    put(r.name.pt, base);
    put(r.name.en, base);
    for (const a of r.aliases || []) put(a, base);
    for (const s of r.specialisations || []) {
      const sb = {tipo: 'specialisation', id: `${r.id}:${s.id}`, pt: s.name.pt, en: s.name.en};
      put(s.name.pt, sb);
      put(s.name.en, sb);
      for (const f of s.forms || []) put(f, sb);
    }
  }
  for (const c of doc.composites || [])
    for (const f of c.forms) put(f, {tipo: 'composite', id: c.members.join('+'), pt: c.name.pt, en: c.name.en});
  for (const cr of doc.context_rules || []) for (const f of cr.forms) put(f, {tipo: 'context_rule', id: `context:${cr.id}`});
  for (const nr of doc.non_roles || []) for (const f of nr.forms) put(f, {tipo: nr.kind, id: `non-role:${nr.kind}`});
  return idx;
}

// Parte um rótulo em átomos pelas regras de _roles.yaml (composição, alternativa, participação).
// Antes de partir, protege as formas da lista que já contêm separadores («DevOps / SRE»,
// «GRC / Compliance», «Scrum Master / Team Lead»…), e não parte dentro de parênteses.
function formasProtegidas(doc, seps) {
  const forms = [];
  for (const r of doc.roles) {
    forms.push(r.name.pt, r.name.en, ...(r.aliases || []));
    for (const s of r.specialisations || []) forms.push(s.name.pt, s.name.en, ...(s.forms || []));
  }
  for (const c of doc.composites || []) forms.push(...c.forms);
  return [...new Set(forms)]
    .filter((f) => seps.some((s) => f.includes(s.trim()) && s.trim()))
    .sort((a, b) => b.length - a.length)
    .map((f) => {
      const esc = (x) => x.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
      const src = f
        .split(/(\s*[/+]\s*)/)
        .map((x, k) => (k % 2 ? `\\s*${esc(x.trim())}\\s*` : esc(x)))
        .join('');
      return new RegExp(`(?<![\\p{L}\\p{N}])${src}(?![\\p{L}\\p{N}])`, 'giu');
    });
}

function atomize(label, doc, protegidas, seps) {
  const keep = [];
  let s = label;
  for (const re of protegidas) s = s.replace(re, (m) => `\u0000${keep.push(m) - 1}\u0000`);
  // parte só ao nível 0 de parênteses
  const parts = [];
  let cur = '';
  let depth = 0;
  for (let i = 0; i < s.length; ) {
    const c = s[i];
    if (c === '(') depth++;
    if (c === ')') depth = Math.max(0, depth - 1);
    const sep = depth === 0 ? seps.find((x) => s.startsWith(x, i)) : null;
    if (sep) {
      parts.push(cur);
      cur = '';
      i += sep.length;
    } else {
      cur += c;
      i++;
    }
  }
  parts.push(cur);
  return parts.map((p) => p.replace(/\u0000(\d+)\u0000/g, (_, k) => keep[+k]).trim()).filter(Boolean);
}

// Procura uma forma na lista, só por correspondência exata (slug), depois de tirar um qualificador no fim.
// «X (anotação)» procura X, também só exato. O ramo de aproximação do inventário não existe aqui (§6.4).
function lookup(a, q, idx) {
  let s = slug(a);
  for (const qq of q) if (s.endsWith('-' + qq)) s = s.slice(0, -qq.length - 1);
  if (idx.get(s)) return {...idx.get(s), forma: a};
  if (q.has(s)) return {forma: a, tipo: 'qualificador', id: null};
  const par = a.match(/^(.*?)\s*\(([^)]*)\)\s*$/);
  if (par) {
    const r = lookup(par[1], q, idx);
    if (r.id) return {...r, forma: a, anotacao: par[2]};
  }
  return {forma: a, tipo: 'sem-correspondencia', id: null};
}

export function criarResolvedor(doc) {
  const idx = buildRoleIndex(doc);
  const seps = [...new Set([...doc.separators.composition, ...doc.separators.alternative, ...doc.separators.participation])].sort(
    (a, b) => b.length - a.length,
  );
  const protegidas = formasProtegidas(doc, seps);
  const q = new Set(doc.qualifiers.map(slug));
  return function resolveRole(label) {
    const whole = idx.get(slug(label));
    if (whole) return [{forma: label, ...whole}];
    const atomos = [];
    for (const a of atomize(label, doc, protegidas, seps)) {
      // «X (Y)»: Y é papel/especialização se estiver na lista (e conta como papel); senão é anotação de função
      const p = a.match(/^(.*?)\s*\(([^)]*)\)\s*$/);
      if (p && !idx.get(slug(a))) {
        const inner = idx.get(slug(p[2]));
        if (inner && inner.tipo !== 'context_rule' && !String(inner.id).startsWith('non-role')) {
          atomos.push({forma: a, ...inner});
          const outer = lookup(p[1], q, idx);
          if (outer.id && outer.id !== inner.id) atomos.push(outer);
          continue;
        }
      }
      const r = lookup(a, q, idx);
      if (r.tipo !== 'qualificador') atomos.push(r);
    }
    return atomos;
  };
}
