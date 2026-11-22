// Texto dos cartões: markdown em linha → HTML restrito, secções da história, listas, BDD e Proporcionalidade.
// Portado de design/iteracao-2/scripts/gerar-indice.mjs (SHI-152, 00-especificacao.md §5.1, §6.3 e §6.5).
// O HTML só tem <strong>, <em>, <code>, <a href> e <br>; todo o resto do texto vai escapado.
import fs from 'node:fs';
import path from 'node:path';
import {splitRow} from './extrair.js';

const NIVEIS = ['L1', 'L2', 'L3'];

// caminho da página do capítulo, sem idioma (o prefixo numérico sai, como no numberPrefixParser)
const capSlug = (pasta) => pasta.replace(/^\d+-/, '');
export const urlCap = (pasta) => `/sbd-toe/sbd-manual/${capSlug(pasta)}/aplicacao-lifecycle`;

const esc = (s) => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
function href(url, pasta, idioma) {
  let u = url;
  if (u.startsWith('#')) u = urlCap(pasta) + u; // âncora da própria página → página do capítulo
  else if (u.startsWith('./') || u.startsWith('../')) u = path.posix.normalize(`/sbd-toe/sbd-manual/${capSlug(pasta)}/${u}`);
  if (u.startsWith('/') && idioma === 'en' && !u.startsWith('/en/')) u = '/en' + u; // o HTML não passa pelo <Link>
  return u;
}
export function inline(s, pasta, idioma) {
  const codes = [];
  let t = String(s).trim().replace(/<br\s*\/?>/gi, '\u0001');
  t = esc(t).replace(/`([^`]+)`/g, (_, c) => {
    codes.push(c);
    return `\u0000${codes.length - 1}\u0000`;
  });
  // escape markdown fora de código (10 US-13, «\>70%»): fica só o carácter, como na página do capítulo
  const escs = [];
  t = t.replace(/\\(&(?:amp|lt|gt|quot);|[!-/:-@[-`{-~])/g, (_, c) => {
    escs.push(c);
    return `\u0002${escs.length - 1}\u0002`;
  });
  t = t.replace(/\[([^\]]+)\]\(([^)\s]+)\)/g, (_, txt, url) => `<a href="${href(url.replace(/&amp;/g, '&'), pasta, idioma)}">${txt}</a>`);
  t = t.replace(/\*\*(.+?)\*\*(?!\*)/g, '<strong>$1</strong>').replace(/(^|[^*\w])\*([^*\s][^*]*?)\*(?=[^*\w]|$)/g, '$1<em>$2</em>');
  t = t.replace(/\u0002(\d+)\u0002/g, (_, i) => escs[+i]);
  t = t.replace(/\u0000(\d+)\u0000/g, (_, i) => `<code>${codes[+i]}</code>`).replace(/\u0001/g, '<br>');
  return t.replace(/\s{2,}$/, '');
}
// o que está entre `…` fica tal como está: só se tira a marcação de fora (02 US-12, «`SEC-Lx-*`»)
export const plano = (s) => {
  const codes = [];
  return String(s ?? '')
    .replace(/`([^`]*)`/g, (_, c) => {
      codes.push(c);
      return `\u0000${codes.length - 1}\u0000`;
    })
    .replace(/<br\s*\/?>/gi, ' ')
    .replace(/\*\*|`|\*/g, '')
    .replace(/\[([^\]]+)\]\([^)]+\)/g, '$1')
    .replace(/\u0000(\d+)\u0000/g, (_, i) => codes[+i])
    .replace(/\s+/g, ' ')
    .trim();
};

// ---------- bloco da história: do título ao próximo título de nível ≤, fora de código ----------
const cacheFich = new Map();
function linhasDe(ficheiro) {
  if (!cacheFich.has(ficheiro)) {
    const L = fs.readFileSync(ficheiro, 'utf8').split(/\r?\n/);
    const dentro = new Array(L.length).fill(false);
    let f = null;
    for (let i = 0; i < L.length; i++) {
      const m = L[i].match(/^\s*(```|~~~)/);
      if (f) {
        dentro[i] = true;
        if (m && L[i].trim().startsWith(f)) f = null;
      } else if (m) {
        f = m[1];
        dentro[i] = true;
      }
    }
    cacheFich.set(ficheiro, {L, dentro});
  }
  return cacheFich.get(ficheiro);
}
export function limparCache() {
  cacheFich.clear();
}
// `inicio` é a linha (1 = primeira) do título da história, como `linha` em extrair.js
export function bloco(ficheiro, inicio) {
  const {L, dentro} = linhasDe(ficheiro);
  const nivel = L[inicio - 1].match(/^(#+)/)[1].length;
  const out = [];
  for (let i = inicio; i < L.length; i++) {
    const h = !dentro[i] && L[i].match(/^(#{1,6})\s/);
    if (h && h[1].length <= nivel) break;
    if (/^---\s*$/.test(L[i]) && !dentro[i]) continue;
    out.push(dentro[i] ? '' : L[i]);
  }
  return out;
}
const RE_ROTULO = /^\*\*([^*]+?)\*\*\s*(.*)$/;
export function seccoes(linhas) {
  const s = [];
  let cur = null;
  for (const l of linhas) {
    if (/^:::/.test(l.trim())) continue;
    const m = l.trim().match(RE_ROTULO);
    if (m && /[.:]$/.test(m[1].trim())) {
      cur = {rotulo: m[1].trim(), linhas: m[2].trim() ? [m[2]] : []};
      s.push(cur);
      continue;
    }
    if (cur) cur.linhas.push(l);
  }
  return s;
}
export function lista(linhas, pasta, idioma) {
  const itens = [];
  let ult = null;
  for (const l of linhas) {
    if (!l.trim()) continue;
    const m = l.match(/^(\s*)[-*]\s+(\[[ xX]\]\s+)?(.*)$/);
    if (m) {
      const it = {html: inline(m[3], pasta, idioma), sub: [], ...(m[2] ? {caixa: true} : {})};
      if (m[1].length >= 2 && ult) ult.sub.push(it);
      else {
        itens.push(it);
        ult = it;
      }
    } else if (ult) {
      const alvo = ult.sub.length ? ult.sub[ult.sub.length - 1] : ult;
      alvo.html += '<br>' + inline(l, pasta, idioma);
    } else itens.push({html: inline(l, pasta, idioma), sub: []});
  }
  return itens;
}
export function bdd(linhas, pasta, idioma) {
  const cen = [];
  let cur = null;
  for (const l of linhas) {
    const t = l.replace(/^\s*[-*]\s+/, '').trim();
    if (!t) continue;
    if (/^\*\*(Dado|Given)\b/i.test(t) || !cur) {
      cur = [];
      cen.push(cur);
    }
    cur.push(inline(t, pasta, idioma));
  }
  return cen;
}
function tabela(linhas) {
  let i = 0;
  while (i < linhas.length && !linhas[i].trim()) i++;
  const t = [];
  while (i < linhas.length && linhas[i].trim().startsWith('|')) t.push(linhas[i++]);
  if (t.length < 2 || !/^\s*\|?\s*:?-{2,}/.test(t[1])) return null;
  return {cab: splitRow(t[0]), linhas: t.slice(2).map(splitRow)};
}

// ---------- Proporcionalidade: colunas, linhas, texto, sem níveis ou ausente; saída aspetos × níveis ----------
const RE_LEVE = /^(não|no\b|not\b|opcional|optional|recomendado|recommended|n\/a)/i;
export function proporcionalidade(sec, pasta, idioma) {
  if (!sec) return {forma: 'ausente'};
  const r = {rotulo: sec.rotulo.replace(/^⚖️\s*/, '').replace(/[.:]$/, ''), aspetos: [], niveis: {}};
  const tb = tabela(sec.linhas);
  if (tb) {
    const hdr = tb.cab.map(plano);
    const col = NIVEIS.map((n) => hdr.findIndex((c) => new RegExp(`^${n}\\b`).test(c)));
    const lin = NIVEIS.map((n) => tb.linhas.findIndex((row) => new RegExp(`^${n}\\b`).test(plano(row[0] || ''))));
    if (col.every((x) => x >= 0)) {
      r.forma = 'colunas';
      const temAspeto = col[0] > 0 && !/^L\d/.test(hdr[0]);
      r.aspetos = tb.linhas.map((row) => (temAspeto ? plano(row[0]) : ''));
      NIVEIS.forEach((n, k) => {
        r.niveis[n] = tb.linhas.map((row) => inline(row[col[k]] ?? '', pasta, idioma));
      });
    } else if (lin.every((x) => x >= 0)) {
      r.forma = 'linhas';
      r.aspetos = hdr.slice(1);
      NIVEIS.forEach((n, k) => {
        r.niveis[n] = tb.linhas[lin[k]].slice(1).map((c) => inline(c, pasta, idioma));
      });
    } else {
      r.forma = 'sem-niveis';
      r.aspetos = hdr;
      r.tabela = tb.linhas.map((row) => row.map((c) => inline(c, pasta, idioma)));
    }
  } else {
    const txt = sec.linhas
      .map((l) => l.trim())
      .filter(Boolean)
      .map((l) => l.replace(/^[-*]\s+/, ''))
      .join(' ; ');
    for (const m of txt.matchAll(/\b(L[123])\s*:\s*(.*?)(?=\s*;?\s*\bL[123]\s*:|$)/g)) r.niveis[m[1]] = [inline(m[2].replace(/[;\s]+$/, ''), pasta, idioma)];
    if (NIVEIS.every((n) => r.niveis[n])) {
      r.forma = 'texto';
      r.aspetos = [''];
    } else return {forma: 'sem-niveis', rotulo: r.rotulo};
  }
  // etiqueta «leve»: o texto do aspeto «Obrigatório?» desse nível quando diz Opcional, Recomendado, Não…
  if (r.niveis.L1) {
    const io = r.aspetos.findIndex((a) => /obrigat|mandatory/i.test(a));
    r.leve = {};
    for (const n of NIVEIS) {
      const ref = plano((r.niveis[n] || [])[io >= 0 ? io : 0] || '').replace(/<[^>]+>/g, '');
      if (io >= 0 && RE_LEVE.test(ref)) r.leve[n] = ref.split(/[;(,]/)[0].trim();
    }
    if (!Object.keys(r.leve).length) delete r.leve;
  }
  return r;
}
