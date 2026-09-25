// manuals_src/src/pages/translation-status.tsx
// Página de estado da tradução (frente 1, i18n). Servida em todos os locales,
// sempre em EN. Lê translation/state/sync-state.json por import estático —
// zero fetch em runtime; o site nunca deriva estados (translation/README.md).
import React, {type ReactNode} from 'react';
import Layout from '@theme/Layout';
import Heading from '@theme/Heading';
import syncState from '@site/../translation/state/sync-state.json';

const STATES = [
  'untranslated',
  'synced',
  'partial',
  'pt-ahead',
  'en-ahead',
  'drift',
  'stale-terms',
] as const;

type FileEntry = {
  state: string;
  source_sha256: string | null;
  translated_at: string | null;
  pending_blocks: number;
};

const files = Object.entries(
  syncState.files as Record<string, FileEntry>,
).sort(([a], [b]) => (a < b ? -1 : a > b ? 1 : 0));
const totals = syncState.totals as Record<string, number>;
const total = files.length;

function shortHash(h: string | null): ReactNode {
  return h ? <code title={h}>{h.slice(0, 12)}</code> : '—';
}

export default function TranslationStatus(): ReactNode {
  return (
    <Layout
      title="Translation status"
      description="Per-file translation state of the SbD-ToE Manual, derived from source hashes.">
      <main className="container margin-vert--lg" lang="en">
        <Heading as="h1">Translation status</Heading>
        <p>
          Source locale <code>{syncState.source_locale}</code> → target locale{' '}
          <code>{syncState.target_locale}</code>. States are derived from
          content hashes, never declared by hand; the canonical text in this
          phase is the Portuguese original.
        </p>
        <p>
          Generated at{' '}
          <time dateTime={syncState.generated_at}>{syncState.generated_at}</time>
          {' · '}
          terms registry SHA-256: {shortHash(syncState.terms_sha256)}
          {' · '}
          {total} files
        </p>

        <Heading as="h2" id="totals">
          Totals
        </Heading>
        <table>
          <thead>
            <tr>
              <th>State</th>
              <th>Files</th>
              <th>Share</th>
            </tr>
          </thead>
          <tbody>
            {STATES.map((s) => {
              const n = totals[s] ?? 0;
              const pct = total === 0 ? 0 : (100 * n) / total;
              return (
                <tr key={s}>
                  <td>
                    <code>{s}</code>
                  </td>
                  <td>{n}</td>
                  <td>{pct.toFixed(1)}%</td>
                </tr>
              );
            })}
          </tbody>
        </table>

        <Heading as="h2" id="files">
          Files
        </Heading>
        <p>Paths are relative to <code>manuals_src/docs/sbd-toe</code>.</p>
        <table>
          <thead>
            <tr>
              <th>File</th>
              <th>State</th>
              <th>Translated at</th>
              <th>Source hash</th>
            </tr>
          </thead>
          <tbody>
            {files.map(([path, f]) => (
              <tr key={path}>
                <td>
                  <code>{path}</code>
                </td>
                <td>
                  <code>{f.state}</code>
                  {f.pending_blocks > 0 ? ` (${f.pending_blocks} pending)` : ''}
                </td>
                <td>
                  {f.translated_at ? (
                    <time dateTime={f.translated_at}>{f.translated_at}</time>
                  ) : (
                    '—'
                  )}
                </td>
                <td>{shortHash(f.source_sha256)}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </main>
    </Layout>
  );
}
