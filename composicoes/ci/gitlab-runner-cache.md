# Composição de cache para GitLab Runner

Um ambiente de runners pode usar dois caches em camadas, desde que cada um
tenha uma responsabilidade clara. Squid reduz downloads externos repetidos; Silo
fornece o armazenamento S3 compartilhado que o GitLab Runner usa para cache de
job. Eles não são substitutos nem devem apontar para o mesmo diretório físico.

## Fluxo

1. O runner inicia o job no Docker executor ou em um Pod do Kubernetes.
2. O cliente consulta o cache distribuído do GitLab Runner no Silo.
3. Dependências que ainda precisam sair para a Internet passam pelo Squid.
4. O job produz um `cache.zip`, que o Runner envia para o Silo.
5. O lifecycle do Silo expira objetos antigos fora do caminho crítico.

O cache distribuído deve ficar em uma rede privada e usar credenciais próprias.
O proxy deve ser explícito e limitado aos runners. SSL bump somente entra quando
há uma necessidade real de cachear conteúdo HTTPS e os clientes confiam na CA
administrada; caso contrário, use túnel TLS normal e aceite que o payload não
será cacheado pelo Squid.

## Garbage collection

O Silo deve receber regras de lifecycle por prefixo, com expiração do objeto
atual e das versões não correntes. O bucket deve usar limites de capacidade,
monitoramento e folga operacional. O GitLab pode limpar caches manualmente ou
por mudança de chave, mas essa ação não substitui lifecycle no backend.

O job não pode depender de um objeto específico existir. Quando a limpeza
remover um cache, o comportamento esperado é um download completo e a geração
de um novo cache. Se o storage ficar indisponível, o pipeline deve registrar o
miss ou erro conforme a política de confiabilidade, sem transformar um arquivo
descartável em banco de dados operacional.

## Limites recomendados

- separar buckets ou prefixos por grupo de confiança;
- limitar `concurrent` e o tamanho máximo do objeto no Runner;
- limitar `cache_dir`, PVC e `cache_mem` conforme a capacidade real;
- rejeitar imagens e objetos acima do limite previsto;
- usar TTL curto para caches de branches e maior para lockfiles estáveis;
- alertar antes de atingir o limite de storage;
- testar a recuperação após limpeza completa.

## Relações

- [Cache de GitLab Runner](../../ci/gitlab-runner/cache.md) detalha a
  configuração do backend.
- [Squid](../../rede/proxy/squid.md) detalha o proxy e a CA.
- [Silo](../../dados/armazenamento-objetos/silo.md) detalha lifecycle e limites.
