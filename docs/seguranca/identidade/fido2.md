# FIDO2

FIDO2 é o conjunto de especificações formado pela API WebAuthn, padronizada
pelo W3C, e pelo CTAP, especificado pela FIDO Alliance. WebAuthn conecta uma
aplicação web ao browser e ao autenticador; CTAP define a comunicação entre o
cliente e um autenticador externo ou de plataforma.

O modelo usa credenciais assimétricas vinculadas a um serviço. O servidor
registra a chave pública. A chave privada permanece no autenticador, que pode
ser uma chave de segurança, um telefone, um computador ou outro dispositivo
compatível.

## Componentes

- Relying Party, o serviço que registra e verifica credenciais;
- client, normalmente o browser ou sistema operacional;
- authenticator, que cria e usa a chave privada;
- WebAuthn, a API que o site chama para registrar ou autenticar;
- CTAP, o protocolo que permite ao client conversar com autenticadores.

O autenticador pode exigir presença do usuário, como um toque, ou verificação
do usuário, como PIN ou biometria local. A biometria não precisa ser enviada
ao serviço: ela pode apenas liberar a operação local da chave.

## Cerimônias

Na criação, o serviço fornece um desafio, um RP ID, dados da conta e políticas
de uso. O autenticador gera a credencial e devolve uma resposta que inclui a
chave pública. Na autenticação, o serviço fornece um novo desafio e o
autenticador assina os dados de contexto.

O servidor deve validar desafio, origem, RP ID, tipo de operação, algoritmo,
identificador da credencial, assinatura, presença e verificação do usuário
conforme a política. Não aceite somente uma assinatura sem validar o contexto
que impede uso em outro site.

## Passkeys

Passkeys são credenciais FIDO que podem ser descobríveis pelo autenticador e,
em alguns ecossistemas, sincronizadas entre dispositivos. Uma chave de
segurança não sincronizável pode ser preferível quando a política exige uma
credencial física sob custódia individual. A escolha envolve recuperação,
portabilidade, governança e risco de conta, não somente conveniência.

Attestation pode informar propriedades do autenticador, mas não deve ser
exigida sem uma necessidade clara. Ela cria requisitos de privacidade,
validação e compatibilidade. Para a maioria das aplicações, a prova de posse
da credencial e a validação do contexto são mais importantes que identificar a
marca do dispositivo.

## Limites

FIDO2 resiste bem a replay e phishing de domínio porque o browser participa da
vinculação com a origem. Isso não impede que um malware use uma sessão já
autenticada, que uma recuperação fraca seja explorada ou que o usuário autorize
uma operação mal explicada.

## Fontes

- [FIDO Alliance, FIDO2](https://fidoalliance.org/fido2/)
- [FIDO Alliance, CTAP](https://fidoalliance.org/specifications/)
- [W3C, Web Authentication Level 3](https://www.w3.org/TR/webauthn-3/)
