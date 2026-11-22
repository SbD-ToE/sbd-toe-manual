import {translate} from '@docusaurus/Translate';

type ChapterKind = 'basilar' | 'operacional' | 'organizacional';

const chapterIcons: Record<ChapterKind, string> = {
  basilar: '🧱',
  operacional: '⚙️',
  organizacional: '🏛️',
};

// Rótulos PT iguais aos do Índice (docs/sbd-toe/010-sbd-manual/index.mdx);
// o EN vem das chaves manualIndex.type.<kind>.* que já existem em code.json.
const chapterTypes: Record<ChapterKind, {label: string; desc: string}> = {
  basilar: {label: 'Basilar', desc: 'Aplicável a todos os níveis (L1-L3)'},
  operacional: {label: 'Operacional', desc: 'Implementação e automação (L2-L3)'},
  organizacional: {label: 'Organizacional', desc: 'Governação e gestão (Transversal)'},
};

type ChapterTypeCalloutProps = {
  kind: ChapterKind;
  // O cânone passa um title ("Capítulo Basilar"); o selo ignora-o e usa o rótulo do Índice (M-27).
  title?: string;
  children: React.ReactNode;
};

export default function ChapterTypeCallout({kind, children}: ChapterTypeCalloutProps) {
  const type = chapterTypes[kind];
  return (
    <details className={`sl-chapter-callout sl-chapter-callout--${kind}`}>
      <summary>
        <span className={`sl-badge sl-badge--${kind}`}>
          <span aria-hidden="true">{chapterIcons[kind]}</span>
          {translate({id: `manualIndex.type.${kind}.label`, message: type.label})}
        </span>
        <span className="sl-chapter-callout__desc">
          {translate({id: `manualIndex.type.${kind}.desc`, message: type.desc})}
        </span>
      </summary>
      <div className="sl-chapter-callout__content">{children}</div>
    </details>
  );
}
