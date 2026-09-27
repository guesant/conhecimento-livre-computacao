# System Configuration

System Configuration, acessado pelo comando `msconfig`, é uma ferramenta de diagnóstico do Windows. Ela permite selecionar modos de inicialização, observar serviços e controlar opções de boot para isolar problemas. Não é o substituto geral do Gerenciador de Serviços, do Task Manager, do Registro ou de uma política de gerenciamento.

## Uso correto

Use `msconfig` para uma investigação temporária e documentada. Registre o estado original, altere uma variável por vez, reinicie quando necessário e reverta a mudança depois do teste. Desabilitar serviços indiscriminadamente pode remover atualizações, segurança, drivers, rede ou mecanismos de recuperação.

O controle permanente de serviços deve ser feito pelo sistema de serviços, Group Policy, MDM ou pelo instalador da aplicação. A configuração de boot deve ser alterada somente quando o diagnóstico justificar, porque opções inadequadas podem impedir a inicialização.

## Relação com outras ferramentas

| Ferramenta | Responsabilidade |
| --- | --- |
| `msconfig` | Diagnóstico de boot e isolamento temporário. |
| Services | Lifecycle de serviços Windows. |
| Task Manager | Processos, desempenho e inicialização de usuário. |
| `regedit` | Registro e configurações de baixo nível. |
| Group Policy | Políticas administrativas por usuário, máquina ou domínio. |
| Event Viewer | Eventos e logs operacionais. |

## Diagnóstico

Depois de uma alteração, observe Event Viewer, status do serviço, código de saída e impacto em outros componentes. O fato de o Windows iniciar em `Safe boot` ou em `Selective startup` não identifica automaticamente a causa; ele apenas reduz o conjunto de componentes carregados.

## Fonte primária

- [Microsoft Support, System Configuration](https://support.microsoft.com/en-us/windows/system-configuration-tools-in-windows-2f8f9a2a-41d6-4f8c-9f9d-6d3e4a1d2e18)
