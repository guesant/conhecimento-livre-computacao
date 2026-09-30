# Autenticação sem senha

Autenticação sem senha prova que o solicitante controla uma credencial
criptográfica, em vez de pedir que ele transmita ou repita um segredo
compartilhado. O servidor armazena uma chave pública ou outro identificador
verificável, enquanto a chave privada fica no autenticador ou em um dispositivo
sob controle do usuário.

Isso não significa que toda autenticação sem senha prove uma identidade civil.
O protocolo prova posse da chave. A associação entre a chave, uma conta e uma
pessoa depende do processo de registro, da política do serviço e dos meios de
recuperação.

## A prova matemática

O servidor gera um desafio aleatório e o vincula ao contexto da operação. O
autenticador assina o desafio com a chave privada. O servidor verifica a
assinatura com a chave pública previamente registrada:

    desafio = random()
    mensagem = desafio + contexto
    assinatura = Sign(chave_privada, mensagem)
    válido = Verify(chave_pública, mensagem, assinatura)

A chave privada não atravessa a rede. Uma assinatura válida demonstra que quem
respondeu controla a chave correspondente, mas não revela a chave e não pode
ser reutilizada em outro desafio. A aplicação precisa rejeitar desafios
repetidos, expirados ou associados a outro domínio, usuário, sessão ou ação.

## Por que não é senha

Uma senha é um segredo que o usuário memoriza e que o serviço precisa verificar
por um mecanismo derivado. Ela pode ser reutilizada em sites falsos, observada
por phishing, adivinhada ou atacada a partir de um banco vazado.

Em uma credencial assimétrica, o servidor não precisa conhecer um segredo que
também poderia ser usado para autenticar. O autenticador responde somente ao
site ou serviço autorizado, com confirmação de presença ou verificação local
quando a política exigir.

Isso reduz phishing e replay, mas não elimina malware na sessão legítima,
roubo de sessão, recuperação de conta fraca, engenharia social ou perda do
dispositivo.

## Registro e autenticação

No registro, o servidor envia um desafio e metadados do serviço. O autenticador
gera uma credencial, protege a chave privada e devolve uma attestation ou
resposta contendo a chave pública e um identificador. O servidor valida a
origem, o escopo da credencial e o desafio antes de armazenar a chave pública.

Na autenticação, o servidor procura a credencial da conta, cria um novo
desafio e valida a resposta assinada. Também verifica origem, RP ID, contador,
presença do usuário e, quando solicitado, verificação do usuário.

## Recuperação

Uma política sem senha ainda precisa responder à perda do autenticador,
substituição do telefone, remoção de uma chave, uso em dispositivos
compartilhados e acesso de emergência. Registre múltiplas credenciais quando
apropriado, proteja a recuperação com um fator forte e audite alterações.
Um email isolado ou um suporte sem verificação pode reduzir toda a segurança
do método principal.

## Relações

- [FIDO2](fido2.md) compõe WebAuthn e CTAP.
- [WebAuthn](webauthn.md) é a API web para credenciais de chave pública.
- [Criptografia assimétrica](../criptografia/criptografia-assimetrica.md)
  explica chaves e assinaturas.
- [TPM](../hardware/tpm.md) e [Secure Enclave](../hardware/secure-enclave.md)
  protegem chaves em hardware ou em um processador isolado.

## Fontes

- [FIDO Alliance, FIDO2](https://fidoalliance.org/fido2/)
- [W3C, Web Authentication](https://www.w3.org/TR/webauthn-3/)
