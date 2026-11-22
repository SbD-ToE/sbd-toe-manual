// src/components/DocEyebrow.tsx
// Rótulo de secção acima do H1 (M-26, 05-leitura.md D-L4 e §5): diz em que parte
// do site se está ("MANUAL · 07 · CI/CD SEGURO", "ASSETS · MCP SERVER (SBD-TOE)").
// Renderizado pelo wrap de @theme/MDXContent; devolve null fora de /sbd-toe/,
// porque o MDXContent também envolve as páginas .md de src/pages (ex.: /about).
// Os segmentos não são ligações: o breadcrumb já liga.
import React, {type ReactNode} from 'react';
import {useLocation} from '@docusaurus/router';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import {translate} from '@docusaurus/Translate';

// slug da rota do capítulo -> número (o título vem de manualIndex.chapter.NN.title)
const chapters: Record<string, string> = {
  'fundamentos': '00',
  'classificacao-aplicacoes': '01',
  'requisitos-seguranca': '02',
  'threat-modeling': '03',
  'arquitetura-segura': '04',
  'dependencias-sbom-sca': '05',
  'desenvolvimento-seguro': '06',
  'cicd-seguro': '07',
  'iac-infraestrutura': '08',
  'containers-imagens': '09',
  'testes-seguranca': '10',
  'deploy-seguro': '11',
  'monitorizacao-operacoes': '12',
  'formacao-onboarding': '13',
  'governanca-contratacao': '14',
};

// Títulos PT dos capítulos, iguais aos de docs/sbd-toe/010-sbd-manual/index.mdx
const chapterTitles: Record<string, string> = {
  '01': 'Classificação das Aplicações',
  '02': 'Requisitos de Segurança',
  '03': 'Threat Modeling',
  '04': 'Arquitetura Segura',
  '05': 'Dependências, SBOM e SCA',
  '06': 'Desenvolvimento Seguro',
  '07': 'CI/CD Seguro',
  '08': 'Infraestrutura como Código (IaC)',
  '09': 'Containers e Imagens',
  '10': 'Testes de Segurança',
  '11': 'Deploy Seguro',
  '12': 'Monitorização e Operações',
  '13': 'Formação e Onboarding',
  '14': 'Governança e Contratação',
};

function chapterTitle(n: string): string {
  if (n === '00') {
    return translate({id: 'doc.eyebrow.chapter.00.title', message: 'Fundamentos'});
  }
  return translate({id: `manualIndex.chapter.${n}.title`, message: chapterTitles[n]});
}

function segments(path: string): string[] {
  const parts: string[] = [];
  const manual = path.match(/^\/sbd-toe\/sbd-manual\/([^/]+)\//);
  if (manual) {
    parts.push(translate({id: 'doc.eyebrow.manual', message: 'Manual'}));
    const n = chapters[manual[1]];
    if (n) {
      parts.push(
        /\/intro\/?$/.test(path)
          ? translate({id: 'doc.eyebrow.chapter', message: 'Capítulo {number}'}, {number: n})
          : `${n} · ${chapterTitle(n)}`,
      );
    }
    if (/\/addon\//.test(path)) {
      parts.push(translate({id: 'doc.eyebrow.supplement', message: 'Complemento Técnico'}));
    }
    if (/\/canon\/|achievable-maturity/.test(path)) {
      parts.push(translate({id: 'doc.eyebrow.verification', message: 'Verificação e rastreabilidade'}));
    }
  } else if (path.startsWith('/sbd-toe/cross-check-normativo/')) {
    parts.push(translate({id: 'doc.eyebrow.crossCheck', message: 'Cross-check normativo'}));
  } else if (path.startsWith('/sbd-toe/assets/')) {
    parts.push(translate({id: 'doc.eyebrow.assets', message: 'Assets'}));
    if (path.startsWith('/sbd-toe/assets/mcp/')) {
      parts.push(translate({id: 'doc.eyebrow.mcp', message: 'MCP Server (SbD-ToE)'}));
    } else if (path.startsWith('/sbd-toe/assets/policies/')) {
      parts.push(translate({id: 'doc.eyebrow.policies', message: 'Políticas recomendadas'}));
    }
  } else if (/^\/sbd-toe\/(teory-of-everything\/|tldr\/?$)/.test(path)) {
    parts.push(translate({id: 'doc.eyebrow.overview', message: 'Visão geral'}));
  }
  return parts;
}

export default function DocEyebrow(): ReactNode {
  const {pathname} = useLocation();
  const {siteConfig} = useDocusaurusContext();
  // tira o baseUrl do locale ("/en/" em EN) para decidir sobre o caminho PT
  const path = pathname.startsWith(siteConfig.baseUrl)
    ? `/${pathname.slice(siteConfig.baseUrl.length)}`
    : pathname;
  if (!path.startsWith('/sbd-toe/')) {
    return null;
  }
  const parts = segments(path);
  if (parts.length === 0) {
    return null;
  }
  return (
    <p className="sl-eyebrow" aria-label={translate({id: 'doc.eyebrow.ariaLabel', message: 'Secção'})}>
      {parts.map((text, i) => (
        <React.Fragment key={text}>
          {i > 0 && <span className="sl-eyebrow__sep" aria-hidden="true">·</span>}
          <span>{text}</span>
        </React.Fragment>
      ))}
    </p>
  );
}
