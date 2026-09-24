# GitLab Runner com Docker executor

O Docker executor usa uma imagem de job e cria containers isolados para o job e
para seus services. O runner precisa alcançar uma Docker Engine, diretamente
no host ou por uma configuração equivalente, e o executor define imagens,
volumes, políticas de pull, limites e concorrência.

O cache local costuma viver em volumes Docker ou em um diretório configurado
no host. Isso é rápido, mas fica preso ao runner que executou o job. Quando
mais de um runner precisa compartilhar cache, o backend deve ser distribuído,
como S3, Silo ou outro serviço compatível.

## Segurança

Montar `/var/run/docker.sock` dá ao job controle efetivo sobre a Docker Engine
do host. Use isso apenas quando o runner e os projetos tiverem o mesmo domínio
de confiança. Docker-in-Docker isola melhor o daemon, mas acrescenta custo,
armazenamento e uma superfície operacional própria. Imagens e services devem
ter allowlists e políticas de pull coerentes com a supply chain.

## Cache

O cache de dependências deve ser identificado por chaves que incluam sistema,
arquitetura, versão do compilador e lockfile. Um cache incorreto é pior que um
cache miss porque pode produzir builds não reprodutíveis. O cache distribuído
deve continuar sendo uma otimização, nunca a única fonte de um artefato
necessário para recuperação.

## Relações

- [Kubernetes executor](kubernetes-executor.md) cria um Pod por job.
- [Cache de GitLab Runner](cache.md) trata backend S3, Silo e limpeza.
- [Squid](../../rede/proxy/squid.md) trata cache de downloads externos.

## Fonte primária

- [GitLab Runner Docker executor](https://docs.gitlab.com/runner/executors/docker/)
