# Agente remoto

Agente remoto é um modelo em que a operação de chave acontece fora do
processo cliente, em outra máquina, em um token acessível por um relay ou em
um serviço de assinatura. O termo não define um protocolo único. A segurança
depende da API, do transporte, da autenticação, da política da operação e do
domínio de falha.

## Modelos diferentes

No forwarding do SSH, o agente permanece na máquina de origem e o socket é
representado na sessão remota. A chave não é copiada, mas o host remoto pode
pedir assinaturas enquanto o socket encaminhado estiver acessível.

Em um agente de assinatura remoto, a chave ou o hardware pode estar no serviço
remoto e o cliente envia uma requisição autenticada. O serviço pode impor
política por usuário, chave, finalidade, quantidade, contexto e aprovação.

No SOPS keyservice, um cliente delega operações de chaves para um processo local
ou remoto. Isso é uma forma de delegação para um fluxo específico e não deve
ser confundida com forwarding de autenticação SSH.

## Decisões de segurança

Um agente remoto precisa definir:

- como o cliente se autentica;
- como a mensagem e o contexto da operação são protegidos;
- quais chaves e operações cada identidade pode usar;
- como impedir replay e duplicidade;
- como registrar sem armazenar o material secreto;
- como limitar taxa, tamanho e duração;
- como revogar o cliente ou a chave;
- como operar quando a rede, o agente ou o hardware estão indisponíveis.

TLS protege o transporte, mas não substitui autorização. Um serviço que assina
qualquer digest apresentado pelo cliente pode virar um oráculo de assinatura.
Sempre que possível, a política deve conhecer a finalidade, o formato e o
contexto da mensagem.

## Disponibilidade e recuperação

Mover a chave para um agente remoto reduz exposição local, mas adiciona rede,
latência, dependência de DNS, autenticação e disponibilidade. Defina se a
operação deve falhar fechada quando o agente não responde. Para chaves de
recuperação, mantenha um caminho independente do mesmo agente ou documente que
a perda do serviço impede a recuperação.

## Relações

- [SSH agent](ssh-agent.md) trata o agente e o socket de autenticação.
- [SOPS keyservice](../../secrets/sops-keyservice.md) trata delegação de chaves.
- [Prova de posse de chave](../autenticacao-sem-senha.md) usa assinaturas em
  um desafio.

## Fonte

- [SOPS, keyservice](https://getsops.io/docs/keyservice/)
