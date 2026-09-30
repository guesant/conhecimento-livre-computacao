# Autenticação

Autenticação é a verificação da identidade de uma pessoa, serviço ou dispositivo. A prova pode usar conhecimento, posse, uma característica biométrica ou uma combinação de fatores.

Senha, chave pública, token, certificado, passkey e credencial emitida por um provedor de identidade são mecanismos diferentes. O sistema precisa verificar validade, origem, audiência, tempo de vida, revogação e associação entre a credencial e a identidade.

Após autenticar, a aplicação pode criar uma sessão ou emitir um token. O transporte do resultado não transforma a autenticação em autorização: o recurso ainda precisa ser protegido por uma política própria.

## Protocolos relacionados

OpenID Connect acrescenta identidade ao OAuth 2.0. SAML transporta asserções de federação. LDAP fornece um diretório, mas não é, por si só, um fluxo completo de autenticação web. FIDO2 e WebAuthn permitem provar posse de uma chave sem enviar uma senha ao servidor.
