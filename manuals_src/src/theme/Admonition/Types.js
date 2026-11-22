// src/theme/Admonition/Types.js
import React from 'react';
import DefaultAdmonitionTypes from '@theme-original/Admonition/Types';

function UserStoryAdmonition(props) {
  // props: {title?: string, children: ReactNode}
  // Estilos em custom.css (.sl-userstory*), no molde dos callouts (M-29).
  const {title, children} = props;
  return (
    <div className="sl-userstory" role="note" aria-label={title || 'User Story'}>
      <div className="sl-userstory__title">
        <span aria-hidden="true">📝</span>
        <span>{title || 'User Story'}</span>
      </div>
      <div className="sl-userstory__body">
        {children}
      </div>
    </div>
  );
}

const AdmonitionTypes = {
  ...DefaultAdmonitionTypes,
  // adiciona (ou substitui) tipos aqui
  userstory: UserStoryAdmonition,
};

export default AdmonitionTypes;
