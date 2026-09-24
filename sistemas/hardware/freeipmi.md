# FreeIPMI

FreeIPMI é uma suíte de ferramentas e bibliotecas para IPMI 1.5 e 2.0. Ela suporta operações in-band e out-of-band e oferece comandos separados para sensores, eventos, energia, console e descoberta de hosts.

## Ferramentas

| Ferramenta | Papel |
| --- | --- |
| `ipmi-sensors` | Consulta sensores e limiares |
| `ipmi-sel` | Consulta e gerencia o System Event Log |
| `ipmipower` | Consulta e altera o estado de energia |
| `ipmiconsole` | Acessa Serial over LAN |
| `ipmiping` | Verifica resposta IPMI |
| `ipmi-locate` | Localiza interfaces IPMI locais |
| `ipmi-config` | Consulta ou altera configuração do BMC |

Os nomes e opções podem variar por versão. Sempre leia `--help` no ambiente em que o comando será executado.

## Consulta local

Uma primeira investigação in-band pode localizar a interface e consultar sensores:

```bash
ipmi-locate
ipmi-sensors
ipmi-sel
```

O comando local depende do driver disponível. Se o BMC não estiver acessível pelo sistema operacional, a consulta pode falhar mesmo quando a interface de rede do BMC funciona.

## Consulta remota

Para uma consulta out-of-band, forneça endereço, usuário e método de autenticação conforme a política do ambiente:

```bash
ipmi-sensors -h <BMC_IP> -u <USER> -p '<PASSWORD>' -I lanplus
ipmi-sel -h <BMC_IP> -u <USER> -p '<PASSWORD>' -I lanplus
```

Nunca coloque uma senha real no histórico do shell ou em script versionado. Use prompt, secret manager ou arquivo de configuração protegido.

O parâmetro `lanplus` seleciona RMCP+ quando suportado. Se o BMC exigir cipher suite, privilégio ou versão específica, ajuste a opção de acordo com o fabricante em vez de reduzir segurança silenciosamente.

## Energia e console

A operação de energia deve ser explícita e revisada:

```bash
ipmipower -h <BMC_IP> -u <USER> -p '<PASSWORD>' -I lanplus -o status
ipmipower -h <BMC_IP> -u <USER> -p '<PASSWORD>' -I lanplus -o on
ipmipower -h <BMC_IP> -u <USER> -p '<PASSWORD>' -I lanplus -o off
```

A ação de desligar ou reiniciar não deve ser automatizada sem confirmação do alvo, janela e impacto. Serial over LAN também pode receber entrada, portanto trate-o como console administrativo:

```bash
ipmiconsole -h <BMC_IP> -u <USER> -p '<PASSWORD>' -I lanplus
```

## Vários hosts

A suíte oferece recursos para consultar intervalos e grupos de hosts, mas o paralelismo deve respeitar os limites do BMC e da rede de gerenciamento. Comece com descoberta e leitura, aplique um limite pequeno e registre falhas por host.

A existência de uma resposta IPMI não prova que o sistema operacional está saudável. Combine sensores, SEL, console, estado do boot e métricas do host.

## Segurança e diagnóstico

FreeIPMI pode operar com credenciais administrativas e comandos de alto impacto. Proteja a rede, reduza privilégios, evite senhas na linha de comando e não habilite cifragem fraca para contornar um BMC antigo sem documentar o risco.

Use `ipmiping` para distinguir conectividade de autenticação:

```bash
ipmiping -h <BMC_IP>
ipmi-sensors -h <BMC_IP> -u <USER> -p '<PASSWORD>' -I lanplus
```

Se o ping IPMI responde e a consulta falha, investigue usuário, privilégio, cipher suite e versão. Se nada responde, verifique VLAN, rota, ACL, endereço do BMC e firmware.

## Fontes primárias

- [FreeIPMI overview](https://www.gnu.org/software/freeipmi/)
- [FreeIPMI manual](https://www.gnu.org/software/freeipmi/manpages/man7/freeipmi.7.html)
- [FreeIPMI documentation](https://www.gnu.org/s/freeipmi/documentation.html)
