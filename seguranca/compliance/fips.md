# FIPS

Federal Information Processing Standards, FIPS, são padrões publicados pelo
governo federal dos Estados Unidos para processamento de informação. Em
segurança, o termo costuma aparecer junto de módulos criptográficos validados
segundo FIPS 140-3. A validação é de um módulo e de um modo operacional
específico, não de um produto inteiro ou de qualquer configuração feita pelo
cliente.

## FIPS 140-3

FIPS 140-3 define requisitos para módulos criptográficos, incluindo interfaces,
papéis, autenticação, software e firmware, ambiente operacional, proteção de
chaves, self-tests e documentação. O CMVP publica certificados e políticas de
segurança. Um fornecedor pode ter um módulo validado sem que todos os algoritmos,
versões, plataformas ou integrações do produto estejam cobertos.

Os níveis de segurança expressam requisitos crescentes. Eles não formam uma
classificação simples de "seguro" e "inseguro"; a organização precisa confirmar
qual nível, módulo, versão, plataforma e configuração são exigidos pelo controle
ou contrato.

## Modo aprovado

Uma biblioteca que contém algoritmos aprovados não está automaticamente operando
em modo FIPS. É preciso confirmar o módulo validado, a versão binária, o sistema
operacional suportado, self-tests, configuração, cadeia de atualização e uso de
algoritmos permitidos. Ativar uma flag chamada `fips` sem essa evidência não
constitui conformidade.

Algoritmos, tamanhos de chave, modos e protocolos podem ter transições de
política. O inventário deve registrar o certificado aplicável e a data em que
ele ainda é aceito. Não copie uma lista antiga de algoritmos sem consultar a
política do programa e o requisito regulatório específico.

## FIPS e operação

FIPS não substitui threat modeling, gestão de chaves, controle de acesso,
hardening, logging ou resposta a incidentes. Ele fornece uma avaliação formal
de propriedades do módulo. A aplicação ainda precisa usar a API correta,
proteger chaves, validar certificados, configurar TLS e impedir downgrade.

Durante atualização, mantenha evidência do certificado, da versão anterior,
da nova validação e do teste em ambiente equivalente. Uma troca de biblioteca,
container base, arquitetura de CPU ou módulo de kernel pode mudar o escopo da
validação.

## Relações

- [Criptografia simétrica](../criptografia/criptografia-simetrica.md) explica primitivas e modos.
- [PKI](../pki/index.md) explica certificados e trust stores.
- [Supply chain](../supply-chain/index.md) trata provenance e integridade da versão.

## Fontes primárias

- [NIST FIPS 140-3](https://csrc.nist.gov/pubs/fips/140-3/final)
- [CMVP](https://csrc.nist.gov/projects/cryptographic-module-validation-program)
- [NIST Cryptographic Module Validation Program](https://www.nist.gov/itl/cryptographic-module-validation-program)
