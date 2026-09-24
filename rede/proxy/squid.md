# Squid

Squid é um forward proxy HTTP que pode reutilizar respostas de rede para
reduzir latência, tráfego externo e carga nos repositórios consultados. Ele
também pode operar como túnel para conexões HTTPS, mas um túnel `CONNECT`
normal não permite inspecionar nem reutilizar o conteúdo cifrado.

## Cache e limites

O cache precisa ser dimensionado como recurso descartável. `cache_dir` define o
armazenamento em disco, `cache_mem` controla objetos mantidos em memória e
`maximum_object_size` evita que uma resposta grande ocupe o cache destinado a
arquivos menores. `refresh_pattern` define como respostas sem uma política
explícita de cache podem ser consideradas frescas, mas não deve ser usado para
ignorar indiscriminadamente `Cache-Control`, autenticação ou instruções de
privacidade.

O tamanho, a idade e a taxa de acerto devem ser observados. Cache cheio deve
remover objetos antigos e não bloquear jobs. Downloads reprodutíveis por
digest, pacotes públicos e camadas de imagem são candidatos melhores do que
respostas personalizadas ou dados autenticados.

## Squid CA e SSL bump

O SSL bump faz o Squid terminar a conexão TLS do cliente, abrir outra conexão
com o servidor e apresentar ao cliente um certificado gerado para o hostname.
Esse certificado é assinado por uma CA que o cliente precisa confiar. Na
prática, a CA do Squid cria uma autoridade intermediária para o proxy agir como
um intermediário autorizado no tráfego selecionado.

Isso é uma inspeção de segurança e não apenas uma otimização de cache. A CA
privada permite ler e alterar tráfego de qualquer cliente que confie nela, por
isso deve ser limitada a máquinas e domínios sob controle administrativo. Não
instale essa CA em dispositivos pessoais ou em workloads que não pertencem ao
domínio de confiança. Certificados pinados, mTLS e alguns registries podem
deixar de funcionar ou exigir uma exceção `splice`, que mantém o túnel sem
descriptografar.

Uma política segura começa com `peek` e `splice` para excluir destinos
incompatíveis, e só usa `bump` para uma allowlist explícita. A chave da CA deve
ser protegida como uma chave de assinatura, com rotação e auditoria.

## Relações

- [Forward proxy](forward-proxy.md) explica a posição do Squid na rede.
- [TLS termination](../../seguranca/tls/termination.md) explica a fronteira de
  confiança criada pela terminação TLS.
- [Cache de GitLab Runner](../../ci/gitlab-runner/cache.md) aplica o proxy ao
  tráfego de jobs e separa isso do cache distribuído em objeto.

## Fontes primárias

- [Squid configuration reference](https://www.squid-cache.org/Doc/config/)
- [ssl_bump](https://www.squid-cache.org/Doc/config/ssl_bump/)
- [Dynamic SSL Certificate Generation](https://wiki.squid-cache.org/Features/DynamicSslCert)
