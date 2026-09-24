# Atualizações automáticas

Atualizações automáticas aplicam correções sem depender de uma intervenção
manual em cada ciclo. O escopo da automação precisa distinguir patches de
segurança, atualizações de funcionalidade e mudanças que exigem reboot.

## Decisão operacional

Aplicar automaticamente apenas o repositório de segurança reduz atraso de
correção, mas não elimina risco de incompatibilidade. A política deve definir
origem confiável, janela, retenção de logs e como uma falha será percebida.

Um pacote pode estar instalado e ainda não estar em uso até um processo ou o
kernel ser reiniciado. Reboots automáticos simplificam a conclusão do patch,
mas podem interromper workload, remover um nó do cluster ou quebrar uma janela
de manutenção.

## Diagnóstico

Verifique a versão instalada, o estado do gerenciador de pacotes, pacotes que
exigem reboot e o resultado da última execução. Separe falha de download,
falha de instalação, conflito de dependência e reboot pendente.

Em hosts que participam de um cluster, atualização e reboot precisam se
integrar ao procedimento de cordon, drain, quorum e validação posterior.

## Relações

- [systemd timer](../systemd/timer.md) agenda tarefas periódicas.
- [Journal persistente](journald.md) preserva evidência da execução.
- [Manutenção de nó Kubernetes](../../manutencao-de-no-cordon-drain-e-disco.md)
  cobre o caso de um host que participa de um cluster.

## Fontes primárias

- [unattended-upgrades](https://wiki.debian.org/UnattendedUpgrades)
- [dnf automatic](https://dnf.readthedocs.io/en/latest/automatic.html)
