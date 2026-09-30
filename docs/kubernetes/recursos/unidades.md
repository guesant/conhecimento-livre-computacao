# Unidades de recursos no Kubernetes

Kubernetes representa recursos com o tipo `resource.Quantity`. A mesma
gramática é usada em requests, limits, capacidade de nós e vários recursos
gerenciados por controllers. A unidade não é uma porcentagem do nó: ela
expressa uma quantidade que o scheduler e o runtime interpretam segundo o
recurso declarado.

Esta página trata principalmente de CPU e memória. A mesma representação é
usada para armazenamento efêmero e páginas enormes, enquanto GPUs e outros
recursos estendidos normalmente são contagens inteiras sem uma unidade física
definida pelo Kubernetes.

## CPU

CPU é medida em unidades de processador. `1` representa uma unidade de CPU,
`0.5` representa meia unidade e `500m` representa 500 millicpu, também
equivalentes a meia unidade.

| Valor | Interpretação |
| --- | --- |
| `1` | uma unidade de CPU |
| `0.5` | meia unidade de CPU |
| `500m` | 500 millicpu, ou meia unidade |
| `1000m` | uma unidade de CPU |
| `2500m` | duas unidades e meia de CPU |

O sufixo `m` significa milésimo neste recurso. `500m` não significa 500 MB e
`1m` de CPU não é um core pequeno. É uma fração de tempo de processador que o
kernel pode contabilizar e limitar. A menor precisão documentada para CPU é
um millicpu.

Uma unidade de CPU não é uma promessa universal de um core físico. Em um nó
bare metal, a capacidade depende dos processadores lógicos apresentados pelo
Linux. Em um nó virtualizado, depende dos vCPUs que o hypervisor apresenta.
`requests.cpu` participa do scheduling e `limits.cpu` define um teto de
execução, normalmente aplicado por cgroups.

## Memória

Memória é medida em bytes. Pode ser escrita sem sufixo, com sufixo decimal SI
ou com sufixo binário IEC:

| Forma | Multiplicador |
| --- | ---: |
| `1` | 1 byte |
| `1k` | 1.000 bytes |
| `1M` | 1.000.000 bytes |
| `1G` | 1.000.000.000 bytes |
| `1T` | 1.000.000.000.000 bytes |
| `1P` | 1.000.000.000.000.000 bytes |
| `1E` | 1.000.000.000.000.000.000 bytes |
| `1Ki` | 1.024 bytes |
| `1Mi` | 1.024² bytes |
| `1Gi` | 1.024³ bytes |
| `1Ti` | 1.024⁴ bytes |
| `1Pi` | 1.024⁵ bytes |
| `1Ei` | 1.024⁶ bytes |

Assim, `1G` e `1Gi` não são o mesmo tamanho. A diferença cresce em valores
maiores. Use `Mi` e `Gi` quando a intenção for trabalhar com múltiplos binários
de 1.024, que é a convenção mais comum para memória de containers.

O sufixo `m` também faz parte da gramática geral de quantidades, mas em
memória significa um milésimo de byte. `400m` representa 0,4 byte e quase
certamente é um erro de configuração. Não confunda `400m` com `400Mi`.

## Expoentes e precisão

A gramática também aceita expoentes decimais com `e` ou `E`, por exemplo
`129e6`, que representa 129.000.000 unidades do recurso. Expoentes tornam
manifests menos legíveis e podem ser confundidos com sufixos, portanto prefira
`129M` ou `129Mi` quando essa forma expressar claramente a intenção.

O parser de quantities trata maiúsculas, minúsculas e o `i` como parte da
unidade. `M`, `m`, `Mi` e `mi` não devem ser tratados como variações visuais do
mesmo valor. A API pode normalizar a representação ao devolver o objeto, então
o texto enviado não deve ser usado como fonte de identidade.

## Exemplo de workload

```yaml
resources:
  requests:
    cpu: "250m"
    memory: "256Mi"
    ephemeral-storage: "1Gi"
  limits:
    cpu: "1"
    memory: "1Gi"
    ephemeral-storage: "2Gi"
```

Esse container participa do scheduling com 250 millicpu e 256 MiB. Pode usar
até uma unidade de CPU e 1 GiB de memória, observadas as políticas do nó e do
runtime. O limite de CPU tende a produzir throttling quando excedido. O limite
de memória pode provocar pressão de memória e encerramento por OOM quando o
processo não consegue permanecer dentro do cgroup.

Colocar as quantities entre aspas evita que o YAML transforme a entrada em um
tipo numérico antes de a API receber a string da quantidade. Também torna
visível que `250m`, `256Mi` e `1Gi` são valores com semântica própria, não
inteiros comuns.

## Recursos que usam a mesma ideia

`ephemeral-storage` usa quantidades de bytes e pode ser usado em requests e
limits. O espaço contabilizado inclui o que o kubelet acompanha para o
container, como camada gravável e logs, conforme a configuração e o runtime do
nó.

`hugepages-2Mi` e `hugepages-1Gi` são exemplos de recursos de páginas enormes.
O nome do recurso contém o tamanho da página e a quantidade declarada é a
quantidade de bytes reservada nesse tipo de página. O workload precisa pedir
uma página suportada pelo nó; não basta trocar o sufixo do manifesto.

GPUs e recursos estendidos possuem nomes definidos pelo device plugin ou pelo
cluster, como `nvidia.com/gpu`. Em geral são declarados como contagens inteiras
e não admitem fracionamento como `500m`.

## Requests, limits e capacidade

Uma quantity só ganha significado operacional quando associada a um recurso e
um campo. `500m` em `requests.cpu` influencia a decisão do scheduler; o mesmo
valor em `limits.cpu` é um teto. `512Mi` em `requests.memory` participa do
encaixe do Pod; em `limits.memory` restringe a memória do cgroup.

O scheduler compara requests com a capacidade alocável do nó, não com a
quantidade de memória atualmente livre no instante da decisão. O kubelet e o
runtime aplicam limits, enquanto o kernel pode usar page cache e outras
estruturas que fazem o consumo observado não coincidir exatamente com a soma
dos valores do processo.

Não existe uma unidade de porcentagem para dizer "20% do nó". Calcule a
quantidade adequada para o workload e deixe o scheduler comparar essa demanda
com cada nó. Se a intenção for uma parcela relativa, ela precisa ser expressa
por requests, limits, quotas ou políticas de prioridade.

## Erros comuns

- escrever `400m` quando a intenção era `400Mi`;
- trocar `G` por `Gi` sem perceber que o multiplicador mudou;
- tratar `1000m` como um core físico dedicado;
- pedir uma fração de GPU, que normalmente é um recurso inteiro;
- usar um limite de memória como se fosse uma reserva de memória;
- somar vCPUs virtuais sem considerar a sobrealocação do hypervisor;
- usar valores sem aspas e depender da conversão do parser YAML;
- usar `ephemeral-storage` como substituto de um volume persistente.

## Relações

- [CPU no Kubernetes](cpu.md) explica scheduling, throttling e CPU Manager.
- [Requests](requests.md) detalha a demanda usada pelo scheduler.
- [Limits](limits.md) detalha os tetos aplicados aos containers.
- [QoS de Pods](qos.md) explica como requests e limits formam classes de QoS.
- [CPU virtual no Proxmox](../../sistemas/virtualizacao/proxmox-cpu.md) explica a camada de virtualização anterior ao nó.

## Fontes primárias

- [Kubernetes, resource units](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#resource-units-in-kubernetes)
- [Kubernetes API, resource.Quantity](https://kubernetes.io/docs/reference/kubernetes-api/common-definitions/quantity/)
- [Kubernetes, manage compute resources](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/)
- [Kubernetes, local ephemeral storage](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#local-ephemeral-storage)
- [Kubernetes, huge pages](https://kubernetes.io/docs/tasks/manage-hugepages/scheduling-hugepages/)
