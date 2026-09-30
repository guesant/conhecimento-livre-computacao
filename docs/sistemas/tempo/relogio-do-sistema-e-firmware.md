# Relógio de tempo real

Um computador normalmente possui pelo menos dois relógios relevantes:

- RTC, Real-Time Clock, mantido por hardware e alimentado mesmo quando a máquina está
  desligada;
- relógio do sistema, mantido pelo kernel enquanto o sistema executa.

O firmware, historicamente chamado de BIOS e hoje frequentemente implementado como UEFI,
configura e lê o RTC. O sistema operacional importa esse valor no boot e depois o ajusta
com NTP, PTP ou outra fonte de tempo.

## O RTC não é um fuso

O RTC guarda um valor de data e hora. Em muitos equipamentos não existe um campo universal
que diga qual regra de timezone esse valor segue. A convenção é responsabilidade do sistema
operacional e da configuração de firmware.

Dois modelos são comuns:

| Modelo | Interpretação do RTC |
| --- | --- |
| UTC | O valor do hardware é uma referência global sem horário de verão |
| Localtime | O valor do hardware já está no horário local do host |

Usar UTC no RTC costuma simplificar servidores, viagens, horário de verão e dual boot. O
Windows tradicionalmente usa localtime em muitas instalações, enquanto Linux costuma usar
UTC, mas isso é uma convenção configurável, não uma lei do hardware.

## BIOS, UEFI e timezone

O menu de BIOS ou UEFI geralmente exibe e altera o relógio do firmware, mas não deve ser
tratado como uma base completa de fusos IANA. O sistema operacional pode aplicar timezone
somente depois de ler o RTC.

Por isso, ajustar a hora exibida no firmware não é o mesmo que configurar `America/Sao_Paulo`
no sistema. O diagnóstico precisa verificar valor do RTC, relógio do kernel, timezone da
sessão e sincronização NTP separadamente.

## Linux e `localtime`

Em Linux, a convenção do relógio de hardware pode ser consultada e alterada com ferramentas
como `timedatectl`. O arquivo `/etc/adjtime` pode registrar `UTC` ou `LOCAL` para a
interpretação do RTC, dependendo da distribuição e da configuração.

Exemplos de inspeção:

```text
timedatectl status
timedatectl show --property=Timezone --property=LocalRTC --property=NTPSynchronized
hwclock --show
date --iso-8601=seconds
```

Não altere `LocalRTC` em produção sem verificar o efeito no próximo boot, no NTP e em
outro sistema operacional que use a mesma máquina. O comando pode reescrever o valor do RTC
para manter a mesma hora instantânea ou mudar a interpretação conforme a opção usada.

## Dual boot

Um sistema que assume RTC em UTC e outro que assume localtime pode alternar a hora a cada
reinicialização. O problema parece um relógio que está sempre errado, mas a causa é uma
convenção diferente entre os sistemas.

As alternativas são:

- configurar ambos para RTC em UTC, quando os sistemas suportarem;
- configurar ambos para localtime, aceitando os custos de horário de verão;
- ajustar explicitamente a política de um dos sistemas e documentá-la.

Misturar as convenções sem declarar o estado produz drift aparente e pode quebrar TLS,
Kerberos, jobs, logs e validação de tokens.

## NTP e relógio monotônico

NTP corrige o relógio civil do host para aproximá-lo de uma referência. Esse relógio pode
ser ajustado para frente ou para trás; por isso, não use o relógio de parede para medir
duração de timeout, latência ou intervalo de retry.

Para medir duração, use um relógio monotônico. Ele não representa uma data útil para o
usuário, mas não deve voltar durante uma medição por causa de NTP ou ajuste manual. O sistema
normalmente oferece relógios monotônicos separados para boot, suspensão e processo.

## Diagnóstico

Quando uma aplicação mostra hora incorreta, verifique nesta ordem:

1. valor que o processo recebeu;
2. timezone e configuração do runtime;
3. timezone da sessão do banco;
4. relógio do sistema;
5. sincronização NTP e fonte escolhida;
6. RTC e convenção `UTC` ou `LOCAL`;
7. conversão feita por driver, serializer ou frontend.

Não corrija um problema de timezone alterando o relógio do host. Não corrija um relógio
desincronizado trocando somente o timezone. São camadas diferentes.

## Fontes primárias

- [systemd timedatectl](https://www.freedesktop.org/software/systemd/man/latest/timedatectl.html)
- [Linux adjtime](https://man7.org/linux/man-pages/man5/adjtime.5.html)
- [Linux time overview](https://man7.org/linux/man-pages/man7/time.7.html)
- [NTP e sincronização de tempo](../linux/ntp.md)
