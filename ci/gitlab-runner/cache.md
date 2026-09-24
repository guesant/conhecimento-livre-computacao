# Cache de GitLab Runner

O cache do GitLab CI/CD é uma otimização para dependências e resultados
reutilizáveis entre jobs. O job deve continuar correto depois de um cache miss.
O Runner pode guardar o cache localmente ou enviá-lo para um backend
distribuído compatível com S3, como Silo.

## Backend S3 compatível

O runner usa um bucket, um prefixo e credenciais próprias. `Shared = true`
permite que runners compartilhem as mesmas chaves de cache; o prefixo deve
separar ambientes e projetos quando a confiança não for comum. As credenciais
devem limitar acesso ao bucket e não podem ser expostas em logs de job.

No Kubernetes, o Helm chart do GitLab Runner recebe a configuração TOML e uma
Secret com as credenciais. No Docker executor, a mesma configuração fica no
`config.toml` do runner.

## Squid para downloads

Squid pode reduzir downloads repetidos de registries e repositórios acessíveis
por HTTP. HTTPS comum é um túnel e não permite reutilizar seu payload; para
inspecionar e cachear esse tráfego seria necessário SSL bump com uma CA
administrada nos runners. A CA deve ser instalada somente nos jobs e hosts sob
controle, e destinos com mTLS, certificate pinning ou dados privados devem ser
excluídos por `splice` ou por política de domínio.

O Squid e o Silo resolvem problemas diferentes: o primeiro cacheia tráfego de
saída; o segundo armazena os arquivos de cache que o GitLab Runner envia e
baixa explicitamente.

## Limites e garbage collection

Defina TTL por prefixo, limite de tamanho de objeto e limite de concorrência de
uploads. Configure lifecycle no Silo para expirar caches atuais e versões
antigas. Se versionamento estiver habilitado, expirar apenas a versão atual
não basta, porque versões não correntes continuam ocupando espaço.

Monitore bytes usados, objetos por prefixo, idade do objeto mais antigo,
acertos, misses, latência e erros de lifecycle. Faça a limpeza fora do caminho
do job e aceite que a primeira execução após a limpeza será mais lenta.

Um desenho inicial seguro é manter caches de dependências por lockfile, usar
TTL de dias ou semanas conforme a frequência de atualização, limitar o tamanho
máximo e reservar folga de storage. Artefatos de release e dados de auditoria
não devem compartilhar esse bucket descartável.

## Relações

- [Docker executor](docker-executor.md) explica cache local e isolamento Docker.
- [Kubernetes executor](kubernetes-executor.md) explica `/cache`, PVC e Pods.
- [Silo](../../dados/armazenamento-objetos/silo.md) explica o backend de objeto
  e as regras de lifecycle.
- [Squid](../../rede/proxy/squid.md) explica o proxy e a CA de SSL bump.

## Fontes primárias

- [Caching in GitLab CI/CD](https://docs.gitlab.com/ci/caching/)
- [GitLab Runner distributed cache](https://docs.gitlab.com/runner/configuration/speed_up_job_execution/)
- [GitLab Runner cache configuration](https://docs.gitlab.com/runner/configuration/advanced-configuration/)
