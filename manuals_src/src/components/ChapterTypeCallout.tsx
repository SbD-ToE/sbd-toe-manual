type ChapterKind = 'basilar' | 'operacional' | 'organizacional';

const chapterIcons: Record<ChapterKind, string> = {
  basilar: '🧱',
  operacional: '⚙️',
  organizacional: '🏛️',
};

type ChapterTypeCalloutProps = {
  kind: ChapterKind;
  title: string;
  children: React.ReactNode;
};

export default function ChapterTypeCallout({kind, title, children}: ChapterTypeCalloutProps) {
  return (
    <details className={`sl-chapter-callout sl-chapter-callout--${kind}`}>
      <summary>
        <span className="sl-chapter-callout__icon" aria-hidden="true">{chapterIcons[kind]}</span>
        <span>{title}</span>
      </summary>
      <div className="sl-chapter-callout__content">{children}</div>
    </details>
  );
}