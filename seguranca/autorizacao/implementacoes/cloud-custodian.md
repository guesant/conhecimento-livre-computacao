# Cloud Custodian

Cloud Custodian é um motor de policy as code para governar recursos em nuvens.
As policies selecionam recursos por filtros e executam ações, como marcar,
notificar, impedir uso indevido ou remover recursos fora da política.

## Risco operacional

Uma ação destrutiva exige escopo explícito, modo de teste, logs, aprovação e
rollback quando possível. Filtros devem ser avaliados contra contas e regiões
corretas antes de habilitar execução automática.

## Relações

Cloud Custodian governa recursos em runtime. Ele não substitui scanning de IaC
nem autorização de uma aplicação que opera sobre seus próprios objetos.

## Fonte

- [Documentação do Cloud Custodian](https://cloudcustodian.io/docs/)
