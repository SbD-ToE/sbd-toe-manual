// src/components/Badge.tsx
// Usa a base única .sl-badge de custom.css (M-31); as cores vêm dos tokens do tema.
import React from 'react';

type BadgeProps = {
  children: React.ReactNode;
  color?: 'neutral' | 'info' | 'success' | 'warning' | 'danger';
};

export default function Badge({ children, color = 'info' }: BadgeProps) {
  const variant = color === 'neutral' ? '' : ` sl-badge--${color}`;
  return <span className={`sl-badge${variant}`}>{children}</span>;
}
