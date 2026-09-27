# SELinux

SELinux é um mecanismo de Mandatory Access Control, MAC, integrado ao Linux
Security Modules. Ele associa contextos a sujeitos e objetos, organiza processos
em domínios e recursos em tipos e avalia regras que podem permitir ou negar
classes específicas de operação.

## Modelo

Uma operação pode ser permitida pelas permissões tradicionais e ainda ser negada
pelo SELinux. A decisão considera o domínio do processo, o tipo do recurso, a
classe da operação e a política carregada. Type enforcement e, quando aplicável,
MLS ou categorias permitem expressar relações que não cabem em uma ACL simples.

O modo enforcing bloqueia violações. Permissive registra negações e permite a
operação, servindo para diagnóstico controlado. Desligar o mecanismo para fazer
um serviço funcionar remove a evidência necessária para escrever uma regra
estreita e transforma uma falha de integração em uma lacuna de contenção.

## Operação

O troubleshooting começa pelo contexto efetivo do processo e do arquivo, pelo
evento de negação e pela política que deveria permitir o fluxo. Não copie uma
regra de allow apenas para eliminar um alerta. Confirme que a operação é legítima,
limite o domínio e o tipo e teste caminhos que devem permanecer bloqueados.

RHEL e Fedora usam SELinux como componente central de suas políticas de segurança
e normalmente iniciam com a política targeted em enforcing. Outras distribuições
podem oferecer SELinux, mas o default depende da edição, imagem e configuração.
Presença de pacotes ou de uma política no filesystem não prova enforcement.

## Relações

- [Mandatory Access Control](autorizacao/modelos/mac.md) explica MAC e suas
  fronteiras.
- [AppArmor](mac-apparmor.md) usa perfis centrados em programas e outro modelo
  de operação.
- [LSM](../sistemas/linux/lsm.md) descreve a infraestrutura do kernel que pode
  hospedar mecanismos de segurança.

## Fontes primárias

- [SELinux Project](https://selinuxproject.org/page/Main_Page)
- [Red Hat SELinux guide](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/using_selinux/index)
