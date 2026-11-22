import React, {type ReactNode} from 'react';
import Link from '@docusaurus/Link';

type UseCaseCardProps = {
  // Emoji (casos de uso do MCP) ou SVG de traço (entradas da página inicial)
  icon?: ReactNode;
  title: string;
  summary: string;
  to: string;
  tags?: string[];
  // Destino escrito por baixo do resumo; com ele, a coluna da seta sai
  cta?: string;
};

export default function UseCaseCard({icon, title, summary, to, tags, cta}: UseCaseCardProps) {
  return (
    <Link to={to} className="sl-usecase-card">
      {icon && <div className="sl-usecase-card__icon" aria-hidden="true">{icon}</div>}
      <div className="sl-usecase-card__body">
        <h3 className="sl-usecase-card__title">{title}</h3>
        <p className="sl-usecase-card__summary">{summary}</p>
        {tags && tags.length > 0 && (
          <div className="sl-usecase-card__tags">
            {tags.map((t) => (
              <span key={t} className="sl-usecase-card__tag">{t}</span>
            ))}
          </div>
        )}
        {cta && (
          <span className="sl-usecase-card__cta">
            {cta}&nbsp;<span aria-hidden="true">→</span>
          </span>
        )}
      </div>
      {!cta && <div className="sl-usecase-card__arrow" aria-hidden="true">→</div>}
    </Link>
  );
}
