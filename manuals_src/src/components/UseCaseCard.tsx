import React from 'react';
import Link from '@docusaurus/Link';

type UseCaseCardProps = {
  icon: string;
  title: string;
  summary: string;
  to: string;
  tags?: string[];
};

export default function UseCaseCard({icon, title, summary, to, tags}: UseCaseCardProps) {
  return (
    <Link to={to} className="sl-usecase-card">
      <div className="sl-usecase-card__icon" aria-hidden="true">{icon}</div>
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
      </div>
      <div className="sl-usecase-card__arrow" aria-hidden="true">→</div>
    </Link>
  );
}
