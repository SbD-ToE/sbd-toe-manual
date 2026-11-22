// Swizzle eject (safe, Docusaurus 3.10.1) de Footer/Copyright (M-16, SHI-29 D-16).
// O copyright da config é traduzido por footer.json como texto fixo e o ano EN fica
// congelado; com Translate + {year}, PT e EN têm o ano calculado.
import React, {type ReactNode} from 'react';
import Translate from '@docusaurus/Translate';
import type {Props} from '@theme/Footer/Copyright';

export default function FooterCopyright(_props: Props): ReactNode {
  return (
    <div className="footer__copyright">
      <Translate
        id="footer.copyright"
        description="Linha de copyright do rodapé"
        values={{year: new Date().getFullYear()}}>
        {'© {year} Pedro Farinha e contribuidores. Conteúdo sob licença CC BY-SA 4.0.'}
      </Translate>
    </div>
  );
}
