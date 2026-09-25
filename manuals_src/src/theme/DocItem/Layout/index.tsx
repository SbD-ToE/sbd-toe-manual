// manuals_src/src/theme/DocItem/Layout/index.tsx
// Swizzle em modo *wrap* de @theme/DocItem/Layout (frente 1, i18n).
// Quando a página é servida no locale de destino da tradução mas o documento
// ainda não está traduzido (estado `untranslated` em translation/state/sync-state.json,
// ou ausente do ficheiro), mostra uma faixa a declarar que se lê o original PT.
// O site só LÊ o estado: nada de lógica de tradução aqui (brief §2).
import React, {type ReactNode} from 'react';
import Layout from '@theme-original/DocItem/Layout';
import type LayoutType from '@theme/DocItem/Layout';
import type {WrapperProps} from '@docusaurus/types';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import {useDoc} from '@docusaurus/plugin-content-docs/client';
import syncState from '@site/../translation/state/sync-state.json';

type Props = WrapperProps<typeof LayoutType>;

// `metadata.source` vem no formato `@site/docs/sbd-toe/<caminho>`; a chave do
// estado é o caminho relativo a `docs/sbd-toe` (translation/README.md).
const SOURCE_PREFIX = '@site/docs/sbd-toe/';

type FileState = {state: string};
const files = syncState.files as Record<string, FileState | undefined>;

export function docKeyFromSource(source: string): string | null {
  // NFC: as chaves do estado seguem o git (NFC); em macOS o sistema de
  // ficheiros devolve NFD, e o caminho chegaria aqui nessa forma.
  return source.startsWith(SOURCE_PREFIX)
    ? source.slice(SOURCE_PREFIX.length).normalize('NFC')
    : null;
}

export function isUntranslated(source: string): boolean {
  const key = docKeyFromSource(source);
  if (key === null) {
    return false;
  }
  const entry = files[key];
  return entry === undefined || entry.state === 'untranslated';
}

function UntranslatedBanner(): ReactNode {
  return (
    <div className="sl-i18n-fallback" role="note" lang="en">
      This page has not been translated yet. You are reading the Portuguese
      original.
    </div>
  );
}

export default function LayoutWrapper(props: Props): ReactNode {
  const {i18n} = useDocusaurusContext();
  const {metadata} = useDoc();
  const showBanner =
    i18n.currentLocale === syncState.target_locale &&
    isUntranslated(metadata.source);

  return (
    <>
      {showBanner && <UntranslatedBanner />}
      <Layout {...props} />
    </>
  );
}
