// Plugin local do Mapa do ciclo de vida (SHI-152, 00-especificacao.md §4–§6).
// Lê no build o cânone PT, a tradução EN e _roles.yaml, gera o índice do idioma do build com createData
// e cria a rota /ciclo-de-vida (/en/ciclo-de-vida no EN) com addRoute. O componente da rota é
// src/pages/_ciclo-de-vida.tsx: o «_» impede o plugin de páginas de criar outra rota para o mesmo ficheiro.
// O índice chega à página como props.indice e só se descarrega nessa rota (não vai para os dados globais).
import fs from 'node:fs';
import path from 'node:path';
import logger from '@docusaurus/logger';
import {normalizeUrl, getPluginI18nPath} from '@docusaurus/utils';
import {fasesDoNome} from './fases-normalizar.mjs';
import {capitulos, parseFile, carregarRoles, criarResolvedor} from './extrair.js';
import {urlCap, inline, plano, bloco, seccoes, lista, bdd, proporcionalidade, limparCache} from './texto.js';

const TIPOS_PAPEL = new Set(['canonical', 'specialisation', 'composite']);

function caminhos(siteDir) {
  const PT = path.join(siteDir, 'docs/sbd-toe/010-sbd-manual');
  const EN = path.join(
    getPluginI18nPath({localizationDir: path.join(siteDir, 'i18n/en'), pluginName: 'docusaurus-plugin-content-docs', subPaths: ['current']}),
    '010-sbd-manual',
  );
  return {
    PT,
    EN,
    ROLES: path.join(PT, '00-fundamentos/roles-responsabilidades/_roles.yaml'),
    MAPA: path.join(siteDir, 'src/data/mapa-fases.json'),
  };
}

const tituloIntro = (dir) =>
  fs
    .readFileSync(path.join(dir, 'intro.md'), 'utf8')
    .match(/^title:\s*(.*)$/m)[1]
    .trim()
    .replace(/^["']|["']$/g, '');

// Gera os índices PT e EN (o EN precisa do par PT para os papéis). Junta todos os erros e lança um só no fim.
export function gerarIndices({siteDir, onUnknownPhase = 'throw'}) {
  const {PT, EN, ROLES, MAPA} = caminhos(siteDir);
  const mapa = JSON.parse(fs.readFileSync(MAPA, 'utf8'));
  const doc = carregarRoles(siteDir, ROLES);
  const resolver = criarResolvedor(doc);
  const canonIds = new Set(doc.roles.map((r) => r.id));
  const erros = [];
  const avisos = [];
  const onde = (s, linha) => `${s.idioma} · cap. ${s.capitulo.slice(0, 2)} · ${s.us} · ${path.relative(siteDir, s.ficheiro)}:${linha ?? s.linha}`;

  limparCache();
  const pastas = capitulos(PT);
  const todas = {pt: [], en: []};
  const titulos = {};
  for (const ch of pastas) {
    const fen = path.join(EN, ch, 'aplicacao-lifecycle.md');
    todas.pt.push(...parseFile(path.join(PT, ch, 'aplicacao-lifecycle.md'), 'pt', ch));
    if (fs.existsSync(fen)) todas.en.push(...parseFile(fen, 'en', ch));
    else erros.push(`en · cap. ${ch.slice(0, 2)}: capítulo sem tradução EN (${path.relative(siteDir, fen)})`);
    titulos[ch] = {pt: tituloIntro(path.join(PT, ch)), en: fs.existsSync(path.join(EN, ch, 'intro.md')) ? tituloIntro(path.join(EN, ch)) : ch};
  }

  // erros estruturais, âncoras repetidas e par PT ↔ EN (mesmo capítulo, mesma âncora)
  const chave = (s) => `${s.capitulo}|${s.ancora}`;
  const porChave = {pt: new Map(), en: new Map()};
  for (const idioma of ['pt', 'en'])
    for (const s of todas[idioma]) {
      for (const e of s.erros) erros.push(`${onde(s)}: ${e}`);
      for (const a of s.avisos) avisos.push(`${onde(s)}: ${a}`);
      if (porChave[idioma].has(chave(s))) erros.push(`${onde(s)}: âncora #${s.ancora} repetida no ficheiro`);
      else porChave[idioma].set(chave(s), s);
    }
  for (const idioma of ['pt', 'en']) {
    const outro = idioma === 'pt' ? 'en' : 'pt';
    for (const s of todas[idioma]) if (!porChave[outro].has(chave(s))) erros.push(`${onde(s)}: sem par ${outro.toUpperCase()} com a âncora #${s.ancora}`);
  }

  // papéis da história PT: voz e responsáveis de cada linha, só pelas formas de _roles.yaml (§6.4)
  const exatos = (atomos) => atomos.filter((a) => a.id && TIPOS_PAPEL.has(a.tipo));
  const idsCanon = (atomos) => [...new Set(atomos.flatMap((a) => String(a.id).split('+')).map((id) => id.split(':')[0]).filter((id) => canonIds.has(id)))];
  const papeisPT = new Map();
  for (const s of todas.pt) {
    const vozAt = exatos(s.papeis_escritos.flatMap(resolver));
    papeisPT.set(chave(s), {vozAt, respAt: s.sdlc.map((l) => (l.responsavel ? exatos(resolver(l.responsavel)) : []))});
  }

  const indices = {};
  for (const idioma of ['pt', 'en']) {
    const historias = [];
    for (const s of todas[idioma]) {
      const par = papeisPT.get(chave(s));
      if (!par) continue; // já registado como «sem par»
      const pt = porChave.pt.get(chave(s));
      if (pt.sdlc.length !== s.sdlc.length) {
        erros.push(`${onde(s)}: ${s.sdlc.length} linha(s) SDLC, e ${pt.sdlc.length} no par PT`);
        continue;
      }
      const cap = s.capitulo.slice(0, 2);
      const voz = idsCanon(par.vozAt);
      const especializacoes = [];
      const momentos = s.sdlc.map((l, i) => {
        const respAt = par.respAt[i];
        const responsaveis = idsCanon(respAt);
        for (const a of [...par.vozAt, ...respAt])
          if (a.tipo === 'specialisation' && !especializacoes.some((e) => e.id === a.id)) especializacoes.push({id: a.id, rotulo: a[idioma]});
        // Normalização do nome de fase (fases-normalizar.mjs) e consulta do mapa. O nome já vem sem ênfase
        // markdown: extrair.js passa a célula por stripMd antes (ressalva da SHI-153 / SHI-25, F-1), por isso
        // 03 US-11 «Alteração de *tools*» / «Change of *tools*» cai na chave «alteração de tools» / «change of tools».
        let fases = fasesDoNome(mapa, idioma, l.fase);
        if (!fases.length) {
          const msg = `${onde(s, l.linha)}: nome de fase fora do mapa «${l.fase}»`;
          if (onUnknownPhase === 'warn') {
            avisos.push(`${msg} (fica em Transversal)`);
            fases = ['transversal'];
          } else erros.push(msg);
        }
        return {
          fase: l.fase,
          fases,
          trigger: inline(l.trigger || '', s.capitulo, idioma),
          responsavel: plano(l.responsavel),
          sla: plano(l.sla),
          responsaveis,
          papeis: [...new Set([...voz, ...responsaveis])],
        };
      });
      if (!momentos.some((m) => m.papeis.length)) erros.push(`${onde(s)}: nenhum papel canónico na voz nem nos responsáveis`);

      const S = seccoes(bloco(s.ficheiro, s.linha));
      const acha = (re) => S.find((x) => re.test(x.rotulo));
      const sHist = acha(/^(hist[óo]ria|story)\.?$/i);
      const sCtx = acha(/^(contexto|context)\.?$/i);
      const sBdd = acha(/bdd/i);
      const sCheck = acha(/^(Checklist|Critérios de aceitação \(DoD\)|Acceptance criteria \(DoD\))\.?$/);
      // o campo é o bloco «Artefactos & evidências.»; o «… adicionais» só se não houver outro (13 US-10)
      const sEvid = S.find((x) => /artef|evid/i.test(x.rotulo) && !/adiciona|additional/i.test(x.rotulo)) ?? acha(/artef|evid/i);
      const sProp = acha(/proporcional|proportional/i);
      historias.push({
        id: `${cap}-${s.us}`,
        cap,
        us: s.us,
        titulo: plano(s.tituloMd),
        url: `${urlCap(s.capitulo)}#${s.ancora}`,
        voz: plano(s.voz),
        papeisVoz: voz,
        especializacoes,
        momentos,
        contexto: sCtx ? inline(sCtx.linhas.join(' '), s.capitulo, idioma) : null,
        historia: sHist ? inline(sHist.linhas.join(' '), s.capitulo, idioma) : null,
        bdd: sBdd ? bdd(sBdd.linhas, s.capitulo, idioma) : [],
        checklist: sCheck ? lista(sCheck.linhas, s.capitulo, idioma) : [],
        evidencias: sEvid ? lista(sEvid.linhas, s.capitulo, idioma) : [],
        rotulos: {
          bdd: sBdd?.rotulo.replace(/[.:]$/, '') ?? null,
          checklist: sCheck?.rotulo.replace(/[.:]$/, '') ?? null,
          evidencias: sEvid?.rotulo.replace(/^🧾\s*/, '').replace(/[.:]$/, '') ?? null,
        },
        nivel: proporcionalidade(sProp, s.capitulo, idioma),
      });
    }
    indices[idioma] = {
      versao: 1,
      idioma,
      fontes: {roles: {schema: doc.schema, version: doc.version, decided: doc.decided}, mapaFases: 'src/data/mapa-fases.json'},
      fases: mapa.fases.map(({id, ordem, faixa, pt, en, descricao}) => ({id, ordem, faixa, rotulo: idioma === 'pt' ? pt : en, descricao: descricao[idioma]})),
      papeis: doc.roles.map((r) => ({
        id: r.id,
        rotulo: r.name[idioma],
        especializacoes: (r.specialisations || []).map((x) => ({id: `${r.id}:${x.id}`, rotulo: x.name[idioma]})),
      })),
      capitulos: pastas.map((p) => ({id: p.slice(0, 2), titulo: titulos[p][idioma], url: urlCap(p)})),
      historias,
    };
  }

  if (erros.length) {
    const fase = erros.some((e) => e.includes('fora do mapa')) ? '\nNome de fase novo: acrescentar o nome a src/data/mapa-fases.json.' : '';
    throw new Error(`Plugin ciclo-de-vida: ${erros.length} erro(s) no índice das user stories.\n${erros.map((e) => `- ${e}`).join('\n')}${fase}`);
  }
  return {indices, avisos};
}

export default function cicloDeVida(context, options = {}) {
  const {siteDir, baseUrl, i18n} = context;
  const {PT, EN, ROLES, MAPA} = caminhos(siteDir);
  return {
    name: 'sbd-ciclo-de-vida',
    getPathsToWatch() {
      return [`${PT}/*/aplicacao-lifecycle.md`, `${EN}/*/aplicacao-lifecycle.md`, ROLES, MAPA];
    },
    async loadContent() {
      const {indices, avisos} = gerarIndices({siteDir, onUnknownPhase: options.onUnknownPhase ?? 'throw'});
      for (const a of avisos) logger.warn(`Plugin ciclo-de-vida: ${a}`);
      return indices[i18n.currentLocale === 'en' ? 'en' : 'pt'];
    },
    async contentLoaded({content, actions}) {
      // uma string, para o JSON não ir indentado; um ficheiro por idioma
      const indice = await actions.createData(`indice-${content.idioma}.json`, JSON.stringify(content));
      actions.addRoute({
        path: normalizeUrl([baseUrl, 'ciclo-de-vida']), // '/ciclo-de-vida' ou '/en/ciclo-de-vida'
        component: '@site/src/pages/_ciclo-de-vida.tsx',
        modules: {indice}, // chega à página como props.indice
        exact: true,
      });
    },
  };
}
