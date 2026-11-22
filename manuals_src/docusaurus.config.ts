import type {Config} from '@docusaurus/types';
import {themes as prismThemes} from 'prism-react-renderer';

const sidebarPath = './sidebars-sbd-toe.ts';

const config: Config = {
  title: 'Security by Design',
  tagline: 'Theory of Everything',
  favicon: 'img/brand/favicon-32.png',

  url: 'https://www.securitybydesign.dev',
  baseUrl: '/',
  organizationName: 'shiftleftpt',
  projectName: 'SbD-ToE-Manual',

  onBrokenLinks: 'warn',

  i18n: {
    defaultLocale: 'pt',
    locales: ['pt', 'en'],
    localeConfigs: {
      pt: {label: 'Português', htmlLang: 'pt-PT'},
      en: {label: 'English', htmlLang: 'en-GB'},
    },
  },

  markdown: {
    mermaid: true,
  },

  headTags: [
    {
      tagName: 'link',
      attributes: {rel: 'manifest', href: '/img/brand/site.webmanifest'},
    },
    {
      tagName: 'link',
      attributes: {rel: 'apple-touch-icon', href: '/img/brand/favicon-180.png'},
    },
    {
      tagName: 'meta',
      attributes: {
        name: 'algolia-site-verification',
        content: 'DC1E056DBDDFA537',
      },
    },
  ],

  scripts: [
    {
      src: 'https://plausible.io/js/pa-vrvyYynlF73FkPELUrY4w.js',
      async: true,
    },
  ],

  // Números e versão do manual para a faixa de prova da página inicial (M-41, H-04).
  // Atualizam-se à mão a cada release.
  customFields: {
    manualVersion: 'v1.17.1',
    counts: {chapters: 15, regulations: 6, policies: 39},
  },

  themes: ['@docusaurus/theme-mermaid'],

  // Mapa do ciclo de vida: índice das user stories e rota /ciclo-de-vida (SHI-152 §4).
  // Um nome de fase que não esteja em src/data/mapa-fases.json faz falhar o build ('warn' põe-no em Transversal).
  plugins: [['./src/plugins/ciclo-de-vida', {onUnknownPhase: 'throw'}]],

  presets: [
    [
      'classic',
      {
        docs: {
          path: 'docs/sbd-toe',
          routeBasePath: 'sbd-toe',
          sidebarPath,
          numberPrefixParser: true,
          showLastUpdateTime: false,
          showLastUpdateAuthor: false,
          admonitions: {
            keywords: ['userstory'],
            extendDefaults: true,
          },
        },
        pages: {
          path: 'src/pages',
        },
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
        sitemap: {
          changefreq: 'weekly',
          priority: 0.5,
          filename: 'sitemap.xml',
          // Etiquetas fora do sitemap (M-21, P-29). O padrão compara-se com o caminho
          // completo da rota, que no locale EN começa por /en: daí as duas entradas.
          ignorePatterns: ['/search', '/sbd-toe/tags/**', '/en/sbd-toe/tags/**'],
        },
      },
    ],
  ],

  themeConfig: {
    // Imagem de partilha (og:image, twitter:image), 1200×630, uma só para PT e EN (M-44, A-3).
    image: 'img/brand/social-card.png',

    navbar: {
      title: 'SbD–ToE',
      hideOnScroll: false,
      logo: {
        alt: 'Security by Design - Theory of Everything',
        src: 'img/brand/Shiftleft_LogoHorizontal_V5.png',
        srcDark: 'img/brand/Shiftleft_LogoHorizontal_V5.png',
      },
      // PROPOSTA SHI-29: as quatro secções juntas à esquerda, pela ordem de leitura;
      // utilidades à direita. Rótulos EN em i18n/en/docusaurus-theme-classic/navbar.json.
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'toeOverview',
          position: 'left',
          label: 'Visão geral',
        },
        {
          type: 'docSidebar',
          sidebarId: 'manualAtual',
          position: 'left',
          label: 'Manual',
        },
        {
          type: 'docSidebar',
          sidebarId: 'toeCrossCheck',
          position: 'left',
          label: 'Cross-check normativo',
        },
        {
          type: 'docSidebar',
          sidebarId: 'toeAssets',
          position: 'left',
          label: 'Assets',
        },
        // Mapa do ciclo de vida (entrada-navbar = A, SHI-152 §3.2): página que atravessa os capítulos,
        // sem sidebar. Cabe entre 997 e 1279 px com o espaçamento compacto de N-09 (custom.css).
        {to: '/ciclo-de-vida', label: 'Ciclo de vida', position: 'left'},
        // Pesquisa: só entra quando o Pedro decidir o motor (D-06). Com Algolia DocSearch
        // basta acrescentar themeConfig.algolia; o item {type: 'search'} fixa a posição.
        // {type: 'search', position: 'right'},
        {
          type: 'dropdown',
          label: 'Projeto',
          position: 'right',
          items: [
            {to: '/about', label: 'Sobre'},
            {to: '/faq', label: 'FAQ'},
            {to: '/licenciamento', label: 'Licença'},
          ],
        },
        {
          href: 'https://github.com/SbD-ToE/sbd-toe-manual',
          position: 'right',
          className: 'sl-navbar-github',
          'aria-label': 'GitHub',
        },
        {type: 'localeDropdown', position: 'right'},
      ],
    },

    footer: {
      style: 'dark',
      // PROPOSTA SHI-29: mapa do site em três colunas. Mesmo destino => mesmo rótulo
      // que na navbar (coluna "Secções") e que na sidebar (coluna "Atalhos").
      // Rótulos EN em i18n/en/docusaurus-theme-classic/footer.json.
      links: [
        {
          title: 'Secções',
          items: [
            {label: 'Visão geral', to: '/sbd-toe/teory-of-everything/intro'},
            {label: 'Manual', to: '/sbd-toe/sbd-manual/'},
            {label: 'Cross-check normativo', to: '/sbd-toe/cross-check-normativo/intro'},
            {label: 'Assets', to: '/sbd-toe/assets/intro'},
          ],
        },
        {
          title: 'Atalhos',
          items: [
            {label: 'Resumo executivo (TL;DR)', to: '/sbd-toe/tldr'},
            {label: 'Mapa do ciclo de vida', to: '/ciclo-de-vida'},
            {label: 'Políticas recomendadas', to: '/sbd-toe/assets/policies'},
            {label: 'MCP Server (SbD-ToE)', to: '/sbd-toe/assets/mcp/intro'},
          ],
        },
        {
          title: 'Projeto',
          items: [
            {label: 'Sobre', to: '/about'},
            {label: 'FAQ', to: '/faq'},
            {label: 'Licença', to: '/licenciamento'},
            {label: 'Estado da tradução', to: '/translation-status'},
            {label: 'GitHub', href: 'https://github.com/SbD-ToE/sbd-toe-manual'},
          ],
        },
      ],
      // Mantém-se como valor de recurso: o texto mostrado vem de src/theme/Footer/Copyright
      // (eject, "safe"), com a chave footer.copyright em code.json e o ano calculado.
      copyright: `© ${new Date().getFullYear()} Pedro Farinha e contribuidores.`,
    },

    colorMode: {
      respectPrefersColorScheme: true,
      defaultMode: 'dark',
    },

    docs: {
      sidebar: {
        autoCollapseCategories: true,
        hideable: true,
      },
    },

    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
      additionalLanguages: [
        'bash',
        'powershell',
        'java',
        'json',
        'yaml',
        'docker',
        'diff',
      ],
    },

    mermaid: {
      theme: {light: 'default', dark: 'dark'},
    },

    metadata: [
      {
        name: 'keywords',
        content: 'Security by Design, SbD, DevSecOps, SAMM, SSDF, SLSA, DSOMM',
      },
      {name: 'og:type', content: 'website'},
    ],
  },
};

export default config;