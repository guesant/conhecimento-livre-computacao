# Tunelamento de portas SSH

O encaminhamento SSH transporta conexões TCP por um canal autenticado e cifrado. A conexão SSH não torna automaticamente o serviço final seguro: ela protege o caminho entre os endpoints SSH, enquanto a autorização do serviço, a exposição da porta e a confiança no host intermediário continuam sendo responsabilidades separadas.

Há três modos clássicos de port forwarding e um modo adicional de encaminhamento de fluxo usado para composição de conexões. A diferença principal está em onde o socket de escuta é criado e em qual lado inicia a conexão com o destino.

## Encaminhamento local, `-L`

O cliente cria uma porta local. Quando uma aplicação se conecta a essa porta, o servidor SSH abre a conexão para o destino visto a partir do servidor.

```bash
ssh -N -L 127.0.0.1:15432:db.internal:5432 bastion.example
```

Nesse exemplo, o cliente local acessa `127.0.0.1:15432`; o bastion acessa `db.internal:5432`. A forma local é apropriada para alcançar um banco, painel ou API que só existe na rede acessível pelo bastion.

O endereço de bind deve ser restrito quando apenas o próprio computador precisa usar o túnel. Usar `0.0.0.0` ou um endereço de interface compartilhada transforma o encaminhamento em uma porta acessível por outros clientes da rede.

## Encaminhamento remoto ou reverso, `-R`

O servidor SSH cria uma porta de escuta no lado remoto. Quando alguém se conecta a essa porta, o cliente SSH local abre a conexão para o destino visto a partir da máquina local.

```bash
ssh -N -R 127.0.0.1:18080:127.0.0.1:8080 bastion.example
```

Esse modo é útil quando a máquina local está atrás de NAT ou firewall e precisa oferecer temporariamente um serviço a alguém que alcança o servidor SSH. A política `GatewayPorts` do servidor controla se a porta remota pode escutar fora do loopback, e a configuração `AllowTcpForwarding` pode bloquear ou restringir o recurso.

## Encaminhamento dinâmico, `-D`

O cliente cria uma porta local que fala SOCKS. Cada aplicação configurada para usar esse proxy pode solicitar ao servidor SSH uma conexão para destinos diferentes.

```bash
ssh -N -D 127.0.0.1:1080 bastion.example
```

O modo dinâmico é mais flexível que `-L`, mas também torna menos óbvio quais destinos podem ser alcançados. Use-o somente quando o cliente e a política aceitarem SOCKS, e restrinja o bind local para evitar transformar a estação em um proxy involuntário.

## Encaminhamento de fluxo, `-W`

`-W host:port` não cria uma porta de escuta local ou remota. Ele conecta a entrada e a saída padrão do SSH diretamente a um destino TCP visto pelo servidor intermediário.

```bash
ssh -o ProxyCommand='ssh -W %h:%p bastion.example' target.internal
```

Esse modo é usado principalmente para compor um salto, inclusive por `ProxyJump`. Ele é diferente de `-L`, `-R` e `-D` porque a aplicação final fala com o cliente SSH como um fluxo já conectado, sem que uma porta adicional fique aguardando conexões.

## Variante com sockets Unix

OpenSSH também permite encaminhar sockets Unix com as formas `StreamLocalForward` e opções relacionadas. Isso é uma variante do encaminhamento de fluxo local ou remoto, não um quinto modelo conceitual de port forwarding TCP. Ela é útil quando o serviço só expõe um socket Unix e não deve abrir uma porta TCP.

## Operação segura

Use `-N` quando o objetivo for somente o túnel e `-o ExitOnForwardFailure=yes` para falhar imediatamente se o encaminhamento não puder ser criado. Defina timeouts, mantenha o processo supervisionado quando o túnel for necessário por mais tempo e remova o encaminhamento ao terminar.

Não encaminhe o agente SSH apenas porque o túnel existe. Agent forwarding e port forwarding resolvem problemas diferentes. Registre qual usuário pode criar o túnel, qual destino ele alcança, em qual interface a porta escuta e qual evento encerra a sessão.

## Fontes primárias

- [OpenSSH `ssh(1)`](https://man.openbsd.org/ssh)
- [OpenSSH manual](https://www.openssh.com/manual.html)
- [OpenSSH `ssh_config(5)`](https://man.openbsd.org/ssh_config)
- [OpenSSH `sshd_config(5)`](https://man.openbsd.org/sshd_config)
