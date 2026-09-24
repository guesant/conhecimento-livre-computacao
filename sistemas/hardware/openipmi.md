# OpenIPMI

OpenIPMI é uma implementação Linux que oferece um driver de kernel, uma biblioteca em espaço de usuário e ferramentas para conversar com dispositivos IPMI. Ele é uma ponte entre o sistema operacional e o BMC, não um BMC virtual e não uma interface web de administração.

## Como funciona

O kernel expõe o controlador por uma interface de dispositivo, frequentemente `/dev/ipmi0`. A biblioteca e os utilitários usam essa interface para enviar comandos ao BMC local. A comunicação in-band depende de firmware com IPMI habilitado, driver carregado, dispositivo criado e permissões adequadas.

Se o objetivo é acessar um BMC pela rede, OpenIPMI pode participar da pilha do cliente, mas não transforma a máquina em um servidor de gerenciamento remoto. O endereço de rede é o do BMC, não o endereço comum do sistema operacional.

## Inicialização no Linux

Em uma distribuição que empacota o projeto, verifique os módulos e o dispositivo antes de interpretar uma falha como problema de hardware:

```bash
lsmod | grep ipmi
ls -l /dev/ipmi*
dmesg | grep -i ipmi
```

Os nomes dos módulos variam por kernel e plataforma. Carregar um módulo sem entender o BMC pode apenas produzir uma interface vazia; consulte a documentação da distribuição e do fabricante.

## Casos de uso

OpenIPMI é adequado para consultas in-band durante diagnóstico, integração com ferramentas que esperam o driver Linux IPMI, leitura de sensores e eventos por processos locais e desenvolvimento contra a API da biblioteca.

Não é a melhor abstração para padronizar todo o ciclo de vida de servidores heterogêneos. Para inventário e automação de várias marcas, compare FreeIPMI, ipmitool, Redfish e os SDKs do fabricante.

## Limitações

O driver não corrige sensores mal descritos pelo firmware. Leituras podem ter unidades, limiares ou nomes inesperados. O BMC pode limitar sessões, responder lentamente ou travar depois de uma atualização mal sucedida.

Permissões locais também importam. Dar acesso irrestrito ao dispositivo IPMI permite operações de plataforma com impacto maior que o acesso comum de leitura do sistema.

## Diagnóstico

Compare a presença do dispositivo, os logs do kernel e a resposta de uma consulta simples. Se a consulta in-band falhar, investigue driver ausente, BMC desabilitado no firmware, permissão insuficiente, dispositivo ocupado e firmware incompatível.

Evite resetar o BMC como primeiro passo. Um reset pode interromper console, monitoramento e operações de recuperação em andamento.

## Relações

- [IPMI](ipmi.md) explica o protocolo e o modelo de plataforma.
- [FreeIPMI](freeipmi.md) explica uma suíte de ferramentas alternativa.
- [iDRAC](idrac.md) mostra uma implementação de fabricante.

## Fontes primárias

- [OpenIPMI](https://openipmi.sourceforge.io/)
- [OpenIPMI IPMI guide](https://openipmi.sourceforge.io/IPMI.pdf)
