// Eventos Scrum de um momento do Mapa do ciclo de vida (SHI-215, 00-especificacao-agil.md §3).
// Sem dependências: é para ir tal como está para src/plugins/ciclo-de-vida/agil.mjs, ao lado de
// fases-normalizar.mjs, e o plugin chama eventosDoMomento para cada linha «Integração no SDLC».
//
// Regra (por esta ordem):
//   1. O nome original da fase, normalizado como no mapa de fases, dá uma lista em mapa.nomes[idioma].
//   2. Cada elemento da lista é um id de evento, ou «@conjunto»: o conjunto de regras com esse nome
//      (mapa.conjuntos) lê o texto do trigger (e do SLA, se a regra o pedir) e dá os eventos da
//      primeira regra que casar; se nenhuma casar, os eventos de «omissao» do conjunto.
//   3. Os eventos ficam pela ordem de mapa.eventos, sem repetidos.
// Devolve também as regras que decidiram, para o script de verificação e para o aviso no build.
import {normalizarNome} from './fases-normalizar.mjs';

// texto simples e minúsculo para as regras: sem HTML, entidades básicas, espaços normalizados
export function textoRegra(s) {
  return String(s ?? '')
    .replace(/<[^>]+>/g, '')
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .replace(/&quot;/g, '"')
    .replace(/&#39;/g, "'")
    .replace(/&amp;/g, '&')
    .normalize('NFC')
    .replace(/\s+/g, ' ')
    .trim()
    .toLowerCase();
}

const cache = new WeakMap();
function regex(mapa, id, idioma) {
  let porMapa = cache.get(mapa);
  if (!porMapa) cache.set(mapa, (porMapa = new Map()));
  const k = `${id}|${idioma}`;
  if (!porMapa.has(k)) {
    const p = mapa.regras[id].padrao;
    porMapa.set(k, new RegExp(typeof p === 'string' ? p : p[idioma], 'u'));
  }
  return porMapa.get(k);
}

// {eventos: string[], regras: string[]} de uma linha (fase, trigger e sla originais, num idioma).
// eventos = [] se o nome não estiver no mapa (o plugin trata isso como erro, como no mapa de fases).
export function eventosDoMomento(mapa, idioma, {fase, trigger, sla}) {
  const lista = mapa.nomes[idioma]?.[normalizarNome(fase)];
  if (!lista) return {eventos: [], regras: []};
  const ids = new Set();
  const regras = [];
  const texto = {trigger: textoRegra(trigger), sla: textoRegra(sla)};
  for (const el of lista) {
    if (!el.startsWith('@')) {
      ids.add(el);
      continue;
    }
    const nome = el.slice(1);
    const conj = mapa.conjuntos[nome];
    const casou = conj.regras.find((id) => {
      const r = mapa.regras[id];
      return regex(mapa, id, idioma).test(r.campos.map((c) => texto[c]).join(' · '));
    });
    for (const ev of casou ? mapa.regras[casou].eventos : conj.omissao) ids.add(ev);
    regras.push(`${nome}:${casou ?? 'omissao'}`);
  }
  return {eventos: mapa.eventos.map((e) => e.id).filter((id) => ids.has(id)), regras};
}

// Eventos de uma história: a união dos eventos das suas linhas, pela ordem de mapa.eventos
// (a mesma regra da história no mapa de fases: decisão us-varias-fases = a).
export function eventosDaHistoria(mapa, momentos) {
  const ids = new Set(momentos.flatMap((m) => m.eventos));
  return mapa.eventos.map((e) => e.id).filter((id) => ids.has(id));
}
