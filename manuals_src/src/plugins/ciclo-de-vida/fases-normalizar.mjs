// Normalização dos nomes de fase e consulta do mapa (SHI-150).
// Sem dependências: é para ir tal como está para src/ (o plugin ou a página importam-no com mapa-fases.json).
//
// Regra (por esta ordem):
//   1. Unicode NFC (o «é» composto e o decomposto ficam iguais).
//   2. Todos os hífenes e travessões (U+2010–U+2015, U+2212, U+FE58, U+FE63, U+FF0D) passam a «-».
//   3. Todos os espaços Unicode (incluindo o não separável U+00A0 e U+202F) passam a espaço simples,
//      e as sequências de espaços passam a um só.
//   4. Tiram-se os espaços à volta de «/», «+» e «-» («Deploy / Operação» = «Deploy/Operação»).
//   5. Tiram-se os espaços no início e no fim.
//   6. Minúsculas (toLowerCase, sem locale: o resultado não depende do sistema).
// Os acentos ficam: «Revisão» e «Revisao» seriam nomes diferentes, e não há nenhum caso no cânone.

const HIFENES = /[‐-―−﹘﹣－]/g;
const ESPACOS = /[\s  -   　]+/g;
const SEPARADORES = / ?([/+-]) ?/g;

export function normalizarNome(nome) {
  return String(nome ?? '')
    .normalize('NFC')
    .replace(HIFENES, '-')
    .replace(ESPACOS, ' ')
    .replace(SEPARADORES, '$1')
    .trim()
    .toLowerCase();
}

// Fases (ids) de um nome original, num idioma ('pt' ou 'en'). Devolve [] se o nome não estiver no mapa.
export function fasesDoNome(mapa, idioma, nome) {
  return mapa.nomes[idioma]?.[normalizarNome(nome)] ?? [];
}

// Fases de uma história: a união das fases de todas as linhas da tabela «Integração no SDLC»,
// pela ordem de leitura de mapa.fases (decisão provisória fase-linhas).
export function fasesDaHistoria(mapa, idioma, linhas) {
  const ids = new Set(linhas.flatMap((l) => fasesDoNome(mapa, idioma, l.fase)));
  return mapa.fases.map((f) => f.id).filter((id) => ids.has(id));
}
