# OSV-Scanner

OSV-Scanner é uma ferramenta open source para identificar componentes e relacioná-los a vulnerabilidades conhecidas. Na versão 2, o modelo é explicitamente dividido em extração de pacotes e correspondência de vulnerabilidades.

## Como funciona

Primeiro a ferramenta extrai informações sobre pacotes a partir do alvo, que pode ser código-fonte, lockfiles ou uma imagem. Depois compara essas identidades com bases de vulnerabilidade suportadas. Essa separação é importante: um resultado só pode ser tão correto quanto a identificação do pacote e da versão que o antecedeu.

## Casos de uso

Use OSV-Scanner para verificar um repositório durante CI, reavaliar lockfiles quando novas vulnerabilidades são publicadas, examinar uma imagem de container ou apoiar remediação de dependências vulneráveis.

Um exemplo mínimo de source scanning é:

```bash
osv-scanner scan -r .
```

Para uma imagem, o alvo muda:

```bash
osv-scanner scan image minha-imagem:tag
```

Esses exemplos demonstram superfícies diferentes; não significam que escanear o source torne desnecessário examinar o artefato final.

## Boas práticas

Execute sobre entradas reproduzíveis, preserve lockfiles, fixe a versão da própria ferramenta na CI e trate atualização da base de vulnerabilidades como parte do modelo operacional. Para findings relevantes, investigue se o componente está presente, qual versão foi identificada e se existe correção antes de decidir a remediação.

## Más práticas

Evite concluir que "zero findings" significa software seguro. OSV-Scanner procura vulnerabilidades conhecidas relacionadas aos componentes que conseguiu identificar; ele não analisa vulnerabilidades inéditas no código próprio. Também é inadequado ignorar diferenças entre source scanning e image scanning.

## Alternativas

Outras ferramentas podem combinar SCA com scanning de imagens, IaC, secrets ou SBOM. A escolha deve considerar ecossistemas suportados, fonte dos dados de vulnerabilidade, qualidade da resolução de dependências, formatos de saída e necessidade de uma ferramenta especializada ou multifuncional.

## Fontes

- OSV-Scanner: <https://google.github.io/osv-scanner/>
- Uso do OSV-Scanner v2: <https://google.github.io/osv-scanner/usage/>
- OSV: <https://osv.dev/>

## Continue por aqui

[SCA](index.md) explica a categoria. [Supply chain e SBOM](../../../supply-chain-e-sbom.md) mostra por que inventário de componentes é útil além do gate imediato de CI.
