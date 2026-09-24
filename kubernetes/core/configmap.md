# ConfigMap

ConfigMap armazena configuração não sensível para consumo por Pods. Ele pode
ser exposto como variáveis de ambiente, argumentos ou arquivos montados em um
volume. O objeto separa configuração do manifesto da imagem, mas não cria um
sistema de configuração dinâmica por conta própria.

## Atualização

Uma alteração em ConfigMap pode refletir em volumes montados depois de um
intervalo, mas variáveis de ambiente e argumentos são definidos quando o
container é criado. Aplicações que precisam reagir à mudança devem observar
arquivos, reiniciar Pods por mecanismo explícito ou usar uma camada de
configuração apropriada.

O comportamento de rollout deve ser definido pelo consumidor. Um Deployment
que não muda seu Pod template não cria uma revisão só porque um ConfigMap
mudou. Checksums no template ou um reloader podem conectar os dois lifecycles,
mas essa conexão é uma convenção adicional.

## Limites

ConfigMap não é lugar para senhas, chaves privadas ou tokens. Base64 em um
Secret também não é criptografia, mas Secret comunica uma intenção de
tratamento diferente e integra mecanismos de proteção do cluster.

## Relações

- [Secret](secret.md) trata dados sensíveis.
- [Pod](pod.md) consome o conteúdo.
- [Immutable ConfigMap](https://kubernetes.io/docs/concepts/configuration/configmap/)
  pode impedir alterações acidentais.

## Fonte primária

- [ConfigMaps](https://kubernetes.io/docs/concepts/configuration/configmap/)
