# SCA

Software Composition Analysis identifica componentes de terceiros presentes em um projeto ou artefato e relaciona essas identidades e versões a informações como vulnerabilidades conhecidas, licenças e proveniência.

O problema central é transitividade. Um projeto pode não declarar diretamente o componente vulnerável; ele pode chegar por outra dependência. Por isso a qualidade do resultado depende da fidelidade com que a ferramenta consegue determinar o conjunto realmente resolvido.

## Casos de uso

SCA é útil para detectar uma versão vulnerável logo após uma atualização, responder rapidamente "quais sistemas contêm este componente?" quando uma nova vulnerabilidade é publicada e impedir a introdução de componentes que violam uma política definida.

[OSV-Scanner](osv-scanner.md) é uma implementação focada em identificar pacotes e relacioná-los ao ecossistema OSV.

## Manifesto, lockfile e artefato

Analisar apenas um manifesto com intervalos de versão pode produzir uma visão diferente daquilo que realmente foi instalado. Lockfiles normalmente aproximam a análise da resolução efetiva. Inspecionar o artefato final, como uma imagem, responde uma pergunta ainda diferente: o que efetivamente foi empacotado?

Nenhuma fonte deve ser chamada de universalmente superior; elas representam estágios diferentes da cadeia.

## Boas práticas

Prefira versões resolvidas quando a pergunta exige precisão de versão. Cubra dependências transitivas. Associe findings ao artefato ou commit analisado. Reanalise quando bases de vulnerabilidade recebem dados novos, porque um artefato imutável pode se tornar conhecido como vulnerável sem mudar um byte.

## Más práticas

É inadequado tratar todo CVE presente como automaticamente explorável, mas também é inadequado ignorá-lo sem análise. Outra má prática é escanear somente dependências diretas ou confiar exclusivamente no manifesto quando a build real pode divergir dele.

## Relação com SBOM

SCA e SBOM se sobrepõem na descoberta de componentes, mas respondem perguntas diferentes. Um [SBOM](../../../supply-chain-e-sbom.md) é uma representação da composição; SCA usa informação de composição para realizar análises como correspondência com vulnerabilidades conhecidas.

## Fontes

- OSV-Scanner documentation: https://google.github.io/osv-scanner/
- OWASP, Software Component Verification Standard: https://owasp.org/www-project-software-component-verification-standard/

## Continue por aqui

[OSV-Scanner](osv-scanner.md) mostra uma implementação concreta. [Supply chain e SBOM](../../../supply-chain-e-sbom.md) amplia o assunto para composição, integridade e proveniência.