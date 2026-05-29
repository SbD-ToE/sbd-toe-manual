import React from 'react';

type UseCaseGridProps = {
  children: React.ReactNode;
};

export default function UseCaseGrid({children}: UseCaseGridProps) {
  return <div className="sl-usecase-grid">{children}</div>;
}
