# WebAuthn

WebAuthn é uma API web para criar e usar credenciais de chave pública. Ela
permite que uma aplicação peça ao browser uma cerimônia de registro ou de
autenticação sem receber a chave privada. O browser aplica a associação com a
origem e conversa com o autenticador por meio do sistema operacional ou de um
protocolo FIDO.

WebAuthn não é um diretório, um provedor de identidade ou um banco de usuários.
É uma interface para uma credencial que o serviço deve registrar, autorizar,
revogar e relacionar a uma conta.

## Registro

O servidor cria opções com desafio, RP, usuário e políticas de autenticador.
O browser chama navigator.credentials.create. O autenticador cria o par,
protege a chave privada e devolve uma resposta de criação. O servidor valida
o desafio, a origem, o RP ID, o algoritmo e a attestation conforme a política,
depois armazena a chave pública e o credential ID.

O servidor não deve confiar em dados de usuário enviados pelo browser sem
validar sua relação com a sessão e com o processo de registro.

## Autenticação

O servidor cria um desafio novo e informa quais credenciais são aceitas. O
browser chama navigator.credentials.get. O autenticador assina o desafio e
os dados de contexto com a chave privada. O servidor valida a assinatura com a
chave pública registrada e verifica origem, RP ID, contador, presença e
verificação do usuário.

Desafios precisam ser aleatórios, de uso único, associados à sessão correta e
expirar rapidamente. A resposta deve ser rejeitada se for repetida, deslocada
para outra origem ou usada fora do contexto esperado.

## RP ID, origem e escopo

Origin inclui esquema, host e porta. RP ID define o domínio efetivo que pode
usar a credencial dentro das regras da especificação. Uma configuração
incorreta de subdomínios pode permitir associação mais ampla que a pretendida
ou impedir o login legítimo.

O servidor deve tratar a mudança de domínio, ambiente de homologação, iframe,
proxy e redirecionamento como decisões de segurança. Não compartilhe uma
credencial entre serviços apenas porque eles usam o mesmo provedor de login.

## Implementação

Use uma biblioteca de servidor que valide o formato e as regras da
especificação. Não implemente a verificação de assinatura, flags e campos
binários manualmente sem uma necessidade excepcional. Teste browsers,
autenticadores de plataforma, chaves externas, recuperação, revogação e
múltiplas credenciais por conta.

## Relação com FIDO2

WebAuthn é a parte web do modelo FIDO2. CTAP trata a comunicação com o
autenticador. Uma aplicação pode usar WebAuthn sem conhecer os detalhes de USB,
NFC ou Bluetooth, mas ainda precisa entender a semântica de credenciais,
desafios, origem e autorização.

## Fontes

- [W3C, Web Authentication Level 3](https://www.w3.org/TR/webauthn-3/)
- [MDN, Web Authentication API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Authentication_API)
- [FIDO Alliance, FIDO2](https://fidoalliance.org/fido2/)
