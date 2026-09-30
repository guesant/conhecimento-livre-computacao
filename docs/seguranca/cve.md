# CVE

Common Vulnerabilities and Exposures, CVE, é um sistema de identificação para
vulnerabilidades de segurança divulgadas publicamente. Um identificador CVE
oferece uma referência estável para coordenar avisos, correções, scanners,
distribuições e inventários. Ele não é uma medida de severidade, uma garantia de
exploração ou uma instrução automática de atualização.

## O que o identificador representa

Um registro CVE descreve uma vulnerabilidade em um produto, componente ou versão
afetada, com referências e uma descrição. O registro pode ser enriquecido por
NVD, fornecedor, distribuição e outras fontes. CVE e CVSS têm funções diferentes:
CVE identifica o problema, enquanto CVSS estima severidade segundo um vetor e
um contexto definidos.

Uma aplicação pode estar vulnerável sem ainda possuir um CVE, especialmente
durante coordenação privada. Também pode possuir um CVE que não seja explorável
no ambiente real devido a configuração, versão compilada ou controles de
contenção. O identificador não substitui análise de exposição e impacto.

## Correção e backport

Distribuições estáveis podem aplicar a correção a uma versão antiga sem trocar
todo o número upstream. Por isso, compare a versão do pacote com o advisory da
distribuição e não apenas com a versão publicada pelo fornecedor original.

O tratamento deve relacionar o CVE ao componente realmente embarcado, à imagem
ou pacote utilizado, à exposição, à compensação e ao prazo de correção. Quando a
correção não é possível, registre a exceção, o risco aceito e a data de revisão.

## Relações

- [Ciclo de vida das distribuições](../sistemas/distribuicoes-linux/ciclo-de-vida-e-seguranca.md)
  explica backports, canais e suporte.
- [SCA](appsec/sca/index.md) identifica vulnerabilidades em dependências.
- [SBOM](supply-chain/sbom.md) ajuda a responder quais componentes estão
  presentes no artefato.
- [CVSS](https://www.first.org/cvss/) trata avaliação de severidade, não a
  identidade da vulnerabilidade.

## Fontes primárias

- [CVE Program](https://www.cve.org/)
- [NVD](https://nvd.nist.gov/)
- [FIRST CVSS](https://www.first.org/cvss/)
