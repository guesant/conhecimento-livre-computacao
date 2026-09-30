# RustConn

RustConn é um gerenciador de conexões para Linux com interface GTK4 e integração com múltiplos protocolos de acesso remoto. O projeto reúne SSH, RDP, VNC, SPICE, Mosh, Telnet, serial, Kubernetes e outros tipos de conexão em um catálogo único.

## O que ele é

RustConn é uma camada de organização e execução de clientes remotos, não um protocolo novo e não um servidor de administração. A segurança e as capacidades reais continuam vindo do transporte escolhido, do cliente integrado ou externo e das credenciais do destino.

O uso de uma interface única é útil quando um operador precisa alternar entre Linux por SSH, desktops por RDP ou VNC, consoles seriais e recursos Kubernetes. A mesma conveniência exige que o catálogo de hosts, as credenciais, os certificados e os arquivos de configuração sejam protegidos como material administrativo.

## Casos de uso

RustConn pode ser útil para:

- centralizar conexões heterogêneas em uma estação Linux;
- organizar sessões SSH, RDP, VNC, serial e Kubernetes por ambiente;
- combinar clientes nativos e ferramentas externas quando um protocolo não é implementado diretamente;
- reduzir a troca manual entre aplicativos durante diagnóstico e operação.

Para uma operação automatizada ou uma mudança que precisa ser revisada, prefira o cliente de linha de comando e a configuração declarativa correspondentes. O gerenciador não deve se tornar uma fonte paralela de inventário ou de autorização.

## Limites e segurança

Os recursos variam conforme a versão, o backend e a ferramenta externa instalada. Verifique qual processo realmente abre a conexão, onde as credenciais são armazenadas, como a chave do host é validada e qual escopo de encaminhamento é permitido.

Não trate a agregação de protocolos como agregação de confiança. Uma sessão VNC, uma sessão SSH e uma conexão Kubernetes têm superfícies, identidades e logs diferentes. A política de acesso deve continuar separando ambientes e privilégios mesmo quando a interface os apresenta na mesma lista.

## Fontes primárias

- [RustConn no GitHub](https://github.com/totoshko88/RustConn)
- [Documentação do OpenSSH](https://www.openssh.com/manual.html)
