# k3s

Kubernetes é o sistema que orquestra containers: recebe uma descrição do que deve estar rodando (quais aplicações, quantas réplicas, que recursos cada uma pode consumir) e mantém esse estado, reiniciando o que falha e distribuindo carga entre as máquinas disponíveis. Um cluster Kubernetes completo é composto por vários componentes que normalmente rodam separados (o servidor de API, o `etcd` que guarda o estado, o escalonador, o controller manager, e mais), o que faz sentido operacional quando o cluster tem dezenas ou centenas de máquinas, mas é uma quantidade de peças móveis desproporcional para um cluster pequeno.

k3s é uma distribuição de Kubernetes, mantida pela Rancher/SUSE, feita para reduzir exatamente esse custo operacional sem abandonar a API do Kubernetes: tudo que sabe falar com um cluster Kubernetes comum (`kubectl`, Helm, um manifesto YAML padrão) fala com um cluster k3s sem adaptação. A diferença está em como ele é empacotado e executado, não no que ele expõe para quem usa.

## Binário único

Em vez de vários processos e serviços separados, k3s empacota os componentes essenciais de um cluster Kubernetes num único binário Go, com dependências trocadas por alternativas mais leves (por exemplo, `etcd` pode ser substituído por SQLite num cluster de nó único, já que não há necessidade de um banco distribuído quando só existe uma máquina). Isso reduz drasticamente o consumo de memória e o número de processos a monitorar, tornando viável rodar um cluster Kubernetes de verdade num hardware modesto, como um Raspberry Pi, onde um Kubernetes completo simplesmente não caberia com folga.

## kubeconfig

O `kubeconfig` é o arquivo que o `kubectl` (e qualquer outra ferramenta que fale com a API do Kubernetes) usa para saber a qual cluster se conectar, com qual credencial e, quando há mais de um cluster configurado, qual contexto usar por padrão. Ele contém o endereço do servidor de API, o certificado da autoridade certificadora do cluster (para validar que está falando com o servidor certo) e a credencial de quem está conectando. Perder esse arquivo não significa perder o cluster, mas significa perder o acesso administrativo a ele até gerar ou recuperar um novo.

## Continue por aqui

O [primeiro bootstrap](../operacional/primeiro-bootstrap.md) mostra o comando que recupera o `kubeconfig` gerado por este repositório. [Ansible: as roles do bootstrap](../arquitetura/ansible.md) documenta como a role `k3s` instala e configura esta distribuição especificamente para este cluster.
