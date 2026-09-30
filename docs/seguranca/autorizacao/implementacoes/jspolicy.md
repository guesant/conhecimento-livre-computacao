# jsPolicy

jsPolicy é um sistema de políticas para Kubernetes que permite escrever regras
em JavaScript. As políticas são executadas no admission e podem validar ou
alterar recursos conforme o contrato definido.

## Uso

JavaScript pode reduzir a barreira para equipes que já usam a linguagem, mas o
código continua sendo política de segurança e precisa de revisão, testes,
limites de tempo e distribuição controlada.

## Limites

jsPolicy não substitui RBAC nem políticas de rede. Uma regra de admission não
impede todo comportamento possível de um workload depois que ele entra no
cluster.

## Fonte

- [jsPolicy](https://www.jspolicy.com/)
