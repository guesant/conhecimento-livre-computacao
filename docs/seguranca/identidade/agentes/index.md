# Agentes de chave

Agente de chave é um processo que realiza operações criptográficas em nome de
outros processos sem entregar diretamente a chave privada a cada consumidor.
Ele pode manter uma chave em memória, encaminhar a operação para um token ou
delegar a uma máquina ou serviço protegido.

O agente não torna uma operação automaticamente segura. Quem pode acessar seu
socket ou API pode pedir assinaturas ou decifragem permitidas pelo agente.
A fronteira de acesso, a autorização da operação, o ciclo de vida da sessão e
a auditoria são parte do desenho.

## Famílias

- [SSH agent](ssh-agent.md) assina autenticações SSH.
- [GnuPG agent](gpg-agent.md) gerencia operações do ecossistema OpenPGP.
- [Agente remoto](remote-agent.md) executa ou delega operações fora do processo
  cliente.

O [SOPS keyservice](../../secrets/sops-keyservice.md) é uma implementação de
delegação para operações usadas pelo SOPS, não um substituto genérico para
todos os agentes.
