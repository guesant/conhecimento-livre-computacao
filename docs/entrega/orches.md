# orches

orches é uma implementação mínima de GitOps para um host que executa Podman e
systemd. Um agente consulta um repositório Git, copia os Quadlets desejados
para o diretório do sistema e recarrega as units quando encontra uma mudança.

O repositório inteiro é a unidade de sincronização. Isso torna o modelo fácil
de entender, mas não oferece lifecycle independente para cada serviço nem um
modelo de componentes comparável ao de plataformas Kubernetes.

## Quando usar

orches faz sentido quando um único host é suficiente, o estado desejado cabe em
Quadlets e a simplicidade é mais importante que templating, multi-tenancy ou
rollback por componente. Em ambientes que precisam dessas propriedades, uma
ferramenta mais estruturada ou Kubernetes pode ser mais adequada.

## Relações

- [materia](materia.md) usa um modelo de componentes mais rico.
- [GitOps](gitops.md) explica a prática geral.
- [Podman Quadlets](../podman-quadlets.md) explica o formato de entrada.
