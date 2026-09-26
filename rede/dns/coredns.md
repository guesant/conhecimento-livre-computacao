# CoreDNS

CoreDNS é um servidor DNS extensível escrito em Go e organizado como uma
cadeia de plugins. Um `Corefile` define server blocks, zonas e diretivas. A
ordem efetiva dos plugins é determinada pela compilação do CoreDNS, enquanto
o arquivo de configuração decide quais plugins participam de cada cadeia.

## Plugins e comportamento

Plugins podem responder, transformar, encaminhar, observar ou apenas alterar o
comportamento do servidor. Alguns exemplos são:

| Plugin | Função |
| --- | --- |
| `kubernetes` | descoberta de Services e outras informações do cluster |
| `forward` | encaminhamento para resolvers upstream |
| `cache` | cache de respostas e controle de TTL |
| `file` | autoridade a partir de arquivos de zona |
| `hosts` | nomes locais derivados de um arquivo de hosts |
| `rewrite` | reescrita de nomes, tipos ou respostas conforme política |
| `health` e `ready` | endpoints de saúde e prontidão |
| `prometheus` | métricas do servidor e dos plugins |

O binário oficial inclui plugins padrão, mas plugins externos podem exigir
recompilação. Isso torna CoreDNS pequeno e adaptável, mas a configuração e a
imagem usada precisam ser versionadas para que uma atualização não altere a
cadeia de resolução sem revisão.

## Kubernetes

CoreDNS é usado como serviço de descoberta de DNS em Kubernetes e K3s. O
plugin `kubernetes` consulta o estado do cluster para responder por zonas como
`cluster.local`. O plugin `forward` envia consultas fora das zonas do cluster
para resolvers upstream, enquanto `cache`, `errors`, `health`, `ready` e
`prometheus` cobrem operação.

CoreDNS não substitui o API server, o CNI ou o Service. Ele publica uma visão
DNS dos objetos que o plugin conhece. Problemas de endpoints, Services,
permissões da ServiceAccount, Corefile ou upstream devem ser distinguidos.

## Outros usos

CoreDNS pode servir zonas por arquivo, encaminhar domínios internos,
implementar DNS local em edge e oferecer uma cadeia pequena para ambientes
embarcados ou de laboratório. Ele é mais adequado quando a configuração pode
ser tratada como código e a equipe aceita trabalhar com plugins e Corefile.

Para administrar muitas zonas com workflows de provisionamento e backend
relacional, PowerDNS Authoritative ou BIND podem oferecer abstrações mais
apropriadas.

## Segurança e operação

Não exponha recursão ou métricas sem ACLs. Restrinja a ServiceAccount do
plugin Kubernetes, monte o Corefile como configuração versionada, proteja
endpoints de saúde e acompanhe erros de plugin, latência, cache, SERVFAIL e
falhas de acesso ao API server. Em Kubernetes, trate a disponibilidade do DNS
como dependência do cluster e distribua réplicas conforme o domínio de falha.

## Fontes primárias

- [CoreDNS](https://coredns.io/)
- [Corefile configuration](https://coredns.io/manual/configuration/)
- [Kubernetes plugin](https://coredns.io/plugins/kubernetes/)
