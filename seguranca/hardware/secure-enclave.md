# Secure Enclave

Secure Enclave é o processador de segurança isolado presente em plataformas
Apple compatíveis. Ele possui código, memória e mecanismos criptográficos
separados do processador principal, com APIs do sistema para criar e usar
chaves protegidas.

A finalidade é manter operações e material sensível fora do alcance direto do
processo comum. Uma aplicação pode pedir uma assinatura ou uma operação
criptográfica, mas a chave privada criada para o Secure Enclave não precisa
ser exportável para o espaço da aplicação.

## Relação com autenticação local

Face ID, Touch ID, código do dispositivo e políticas do Keychain podem liberar
uma operação protegida. A biometria é tratada localmente; a aplicação recebe
o resultado da operação autorizada, não os dados biométricos usados pelo
sensor.

Uma chave protegida pelo Secure Enclave pode ser útil para autenticação,
assinatura e armazenamento de credenciais. A política deve definir se ela pode
ser usada sem presença do usuário, depois de reinício, em backup ou em outro
dispositivo.

## Limites

Secure Enclave não é um TPM genérico e não substitui uma autoridade de
identidade, um secret store ou uma política de autorização. A API disponível,
o ciclo de vida da chave, o backup e a migração dependem da plataforma Apple e
da classe de chave utilizada.

Um malware que controla uma sessão legítima pode tentar pedir operações que a
aplicação já está autorizada a realizar. Proteger a chave não torna a lógica
de autorização correta. Também é preciso planejar recuperação para perda,
reset, troca de dispositivo e revogação.

## Relações

- [TPM](tpm.md) descreve um módulo de confiança definido pelo TCG.
- [FIDO2](../identidade/fido2.md) descreve credenciais para autenticação.
- [age](../secrets/age.md) pode usar plugins que delegam a operação de chave
  para hardware.

## Fontes primárias

- [Apple Platform Security](https://support.apple.com/guide/security/welcome/web)
- [Apple, Protecting keys with the Secure Enclave](https://developer.apple.com/documentation/security/protecting-keys-with-the-secure-enclave)
