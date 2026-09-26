# Termius

Termius é um cliente multiplataforma para conexões SSH e outros protocolos de administração remota. Ele organiza hosts, credenciais, chaves, sessões e transferências de arquivos em uma interface que pode ser usada em desktop e dispositivos móveis.

## O que ele é

Termius é um cliente, não um servidor SSH nem um sistema de gerenciamento de identidade. A conexão ainda depende do `sshd`, da chave do host, da autenticação configurada e das permissões do destino. Recursos como SFTP, Mosh, Telnet, serial, jump host, proxy e port forwarding dependem do protocolo, da plataforma e da edição utilizada.

O valor principal do cliente está na organização das conexões e na experiência de uso em múltiplos dispositivos. Isso pode reduzir erros operacionais quando há muitos hosts, mas também torna a proteção do catálogo de conexões, das chaves e da sincronização entre dispositivos parte do modelo de ameaça.

## Quando usar

Termius é uma opção razoável quando o operador precisa:

- manter sessões SSH organizadas em vários sistemas operacionais;
- alternar entre terminal, SFTP e encaminhamento de portas;
- usar um cliente móvel ou desktop com sincronização de configurações;
- trabalhar com jump hosts e perfis de conexão sem repetir parâmetros manualmente.

Para automação, scripts, revisão e reprodução exata, o cliente OpenSSH e arquivos de configuração versionáveis continuam sendo mais transparentes. Um perfil salvo no aplicativo não deve ser confundido com uma configuração auditada no repositório.

## Segurança

Proteja o cofre do aplicativo, o sistema operacional e qualquer mecanismo de sincronização. Não reutilize uma chave pessoal ampla para todas as máquinas, não desative a verificação da chave do host para contornar um alerta e não armazene segredos em descrições, snippets ou nomes de hosts.

Quando o cliente oferece agent forwarding, jump host ou port forwarding, aplique as mesmas restrições do OpenSSH. A interface simplifica a configuração, mas não reduz o impacto de encaminhar um agente para um servidor não confiável nem o risco de publicar uma porta em uma interface acessível por terceiros.

## Alternativa nativa

O OpenSSH, com `ssh_config`, `ssh-agent`, `ProxyJump`, SFTP e encaminhamento explícito, é a alternativa mais auditável em sistemas Unix. Termius pode ser uma camada de conveniência sobre os mesmos conceitos, não uma substituição para compreendê-los.

## Fontes primárias

- [Termius](https://termius.com/)
- [Termius para Linux](https://termius.com/download/linux)
- [Recursos e planos do Termius](https://www.termius.com/pricing)
- [SSH, manual do OpenBSD](https://man.openbsd.org/ssh)
