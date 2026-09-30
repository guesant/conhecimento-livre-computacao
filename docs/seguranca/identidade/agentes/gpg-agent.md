# GnuPG agent

gpg-agent é o agente do GnuPG para operações com chaves privadas do
ecossistema OpenPGP. Ele pode manter material protegido, chamar o pinentry,
usar smartcards e responder a operações de assinatura ou decifragem por
meio de sockets definidos pelo GnuPG.

O agente separa a aplicação que precisa assinar da leitura direta da chave.
Isso reduz exposição acidental em processos, mas o processo que consegue
pedir uma operação autorizada ainda pode produzir uma assinatura ou solicitar
uma decifragem.

## OpenPGP e SSH

O GnuPG pode oferecer compatibilidade para autenticação SSH em configurações
específicas. Isso não transforma OpenPGP em SSH nem faz os formatos de chave
serem iguais. O consumidor deve saber qual socket, protocolo e finalidade estão
sendo usados.

Quando um smartcard é utilizado, a operação pode ocorrer no dispositivo sem
exportar a chave privada. A segurança depende também do PIN, da política de
uso, da proteção física e do procedimento de substituição.

## Pinentry e cache

O pinentry coleta a passphrase ou autorização em uma interface separada.
Cachear a autorização reduz atrito, mas aumenta a janela em que processos com
acesso ao agente podem pedir operações. O tempo de cache deve refletir a
sensibilidade da chave e a duração da sessão de trabalho.

## Operação

Use sockets com permissões restritas, mantenha o GnuPG atualizado e não copie
o diretório de chaves para servidores remotos sem uma decisão explícita.
Audite quais subchaves podem assinar, cifrar ou autenticar. Separe chaves por
finalidade quando o impacto de comprometimento exigir isso.

## Relações

- [Agentes de chave](index.md) explica a fronteira comum.
- [Criptografia assimétrica](../../criptografia/criptografia-assimetrica.md)
  explica assinaturas e chaves públicas.
- [Criptografia de segredos no Git](../../../criptografia-de-segredos-no-git.md)
  aparece em fluxos de cifragem e assinatura, mas não é sinônimo de gpg-agent.

## Fonte

- [GnuPG, documentação do gpg-agent](https://gnupg.org/documentation/manuals/gnupg/Agent-Options.html)
