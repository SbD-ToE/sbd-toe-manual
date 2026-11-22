// manuals_src/src/theme/DocPaginator/index.tsx
// Wrap de @theme-original/DocPaginator (F-1 da SHI-40, SHI-53).
// O Docusaurus calcula `previous`/`next` em loadContent com o `label` explícito
// do item da sidebar, antes de aplicar a tradução de current.json; em EN, os
// itens com `label` em sidebars-sbd-toe.ts ficavam com o rótulo PT. Aqui o
// título passa a vir da sidebar já traduzida, pelo item com o mesmo href; se
// não houver sidebar ou item, fica o título original. O resto das props passa
// tal como chega.
import React, {type ReactNode} from 'react';
import DocPaginator from '@theme-original/DocPaginator';
import type {Props} from '@theme/DocPaginator';
import {useDocsSidebar} from '@docusaurus/plugin-content-docs/client';
import type {
  PropNavigationLink,
  PropSidebarItem,
} from '@docusaurus/plugin-content-docs';

// Itens `link` (os `doc` da sidebar chegam ao cliente como `link`), por href.
// As categorias ficam de fora: a paginação delas usa o título do documento.
function collectLinkLabels(
  items: readonly PropSidebarItem[],
  labels: Map<string, string>,
): Map<string, string> {
  for (const item of items) {
    if (item.type === 'link') {
      labels.set(item.href, item.label);
    } else if (item.type === 'category') {
      collectLinkLabels(item.items, labels);
    }
  }
  return labels;
}

function translated(
  link: PropNavigationLink | undefined,
  labels: Map<string, string>,
): PropNavigationLink | undefined {
  if (!link) {
    return link;
  }
  const label = labels.get(link.permalink);
  return label === undefined ? link : {...link, title: label};
}

export default function DocPaginatorWrapper(props: Props): ReactNode {
  const sidebar = useDocsSidebar();
  const labels = collectLinkLabels(sidebar?.items ?? [], new Map());
  return (
    <DocPaginator
      {...props}
      previous={translated(props.previous, labels)}
      next={translated(props.next, labels)}
    />
  );
}
