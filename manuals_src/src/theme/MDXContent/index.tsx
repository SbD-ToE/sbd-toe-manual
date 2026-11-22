// manuals_src/src/theme/MDXContent/index.tsx
// Swizzle em modo *wrap* (safe) de @theme/MDXContent (M-26): põe o rótulo de
// secção (DocEyebrow) antes do conteúdo, e por isso acima do H1 do documento.
import React, {type ReactNode} from 'react';
import MDXContent from '@theme-original/MDXContent';
import type MDXContentType from '@theme/MDXContent';
import type {WrapperProps} from '@docusaurus/types';
import DocEyebrow from '@site/src/components/DocEyebrow';

type Props = WrapperProps<typeof MDXContentType>;

export default function MDXContentWrapper(props: Props): ReactNode {
  return (
    <>
      <DocEyebrow />
      <MDXContent {...props} />
    </>
  );
}
