# Criptografia assimétrica

Criptografia assimétrica usa um par relacionado de chaves: uma chave pública
que pode ser distribuída e uma chave privada que deve permanecer sob controle
do titular. O par permite construir protocolos de criptografia, assinatura,
autenticação e acordo de chaves, mas cada algoritmo possui operações e
garantias próprias.

## Assinatura

Para assinar, o titular usa a chave privada. O verificador usa a chave pública
para confirmar que a assinatura corresponde aos dados e à chave. Isso prova
posse da chave privada no momento da assinatura, mas não define sozinho quem
é o titular. O vínculo entre chave e identidade exige registro, certificado,
política ou outro mecanismo confiável.

Assinatura não é cifra. Ela não esconde o conteúdo. Também não deve ser
confundida com um hash: a assinatura normalmente assina um digest usando um
algoritmo e uma chave, enquanto o hash não tem chave.

## Criptografia e acordo de chaves

Em um esquema de criptografia assimétrica, o remetente usa a chave pública do
destinatário e somente a chave privada correspondente deve recuperar o segredo.
Na prática, o conteúdo costuma ser cifrado com uma cifra simétrica e a chave
de sessão é protegida por um mecanismo assimétrico.

Um acordo de chaves permite que duas partes derivem um segredo compartilhado
sem transmitir esse segredo diretamente. O protocolo precisa de autenticação
ou de uma infraestrutura de chaves para evitar que um atacante substitua as
chaves e intercepte a sessão.

## Distribuição e confiança

Uma chave pública pode ser alterada em trânsito sem que suas propriedades
matemáticas deixem de funcionar. O problema é fazer o cliente aceitar a chave
errada. Certificados, fingerprints, transparência, registros de confiança,
TOFU e chaves previamente distribuídas resolvem esse problema com trade-offs
diferentes.

PKI organiza autoridades que assinam certificados e políticas que definem
usos. SSH usa mecanismos próprios de confiança de host e chaves autorizadas.
FIDO2 registra chaves vinculadas a um domínio e usa desafios assinados para
autenticação.

## Custo e limites

Operações assimétricas são mais custosas que cifras simétricas e têm formatos,
curvas, tamanhos de chave e requisitos de validação específicos. Use uma
biblioteca mantida e um protocolo definido. Não escolha um algoritmo somente
porque ele possui uma implementação disponível.

Chaves privadas precisam de backup quando a recuperação é necessária, ou de
um procedimento explícito de substituição quando não podem ser copiadas.
Proteger a chave com TPM, Secure Enclave, token ou agente pode reduzir a
exposição, mas introduz dependências de hardware, autorização e recuperação.

## Relações

- [Hash](hash.md) trata funções sem chave.
- [Criptografia simétrica](criptografia-simetrica.md) protege grandes volumes.
- [Prova de posse de chave](../identidade/autenticacao-sem-senha.md) aplica
  assinaturas a uma autenticação sem senha.
- [PKI](../pki/index.md) organiza certificados e autoridades.

## Fontes

- [NIST, Digital Signature Standard, FIPS 186-5](https://csrc.nist.gov/pubs/fips/186-5/final)
- [NIST, Key Management Guidelines, SP 800-57](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final)
- [RFC 5280, Internet X.509 PKI](https://www.rfc-editor.org/rfc/rfc5280)
