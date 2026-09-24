# Secret

Secret é um objeto Kubernetes destinado a transportar dados sensíveis para
Pods e outros consumidores. Ele pode ser usado como variável de ambiente,
arquivo montado ou referência de configuração. O tipo do objeto comunica
intenção, mas criar um Secret não garante que seu conteúdo esteja cifrado em
todo caminho ou invisível para todo administrador do cluster.

## Proteção

O valor serializado em YAML normalmente aparece em base64, que é uma codificação
e não uma proteção criptográfica. Segurança depende de TLS para a API, controle
de acesso, encryption at rest do datastore, restrições de logs, política de
backup e cuidado com ambientes onde o Secret é montado.

RBAC deve limitar leitura e escrita. Um Pod que pode ler um Secret por meio de
ServiceAccount pode expor o valor por logs, debug ou endpoint. A menor
permissão possível continua sendo necessária mesmo quando o datastore está
cifrado.

## Lifecycle

A rotação precisa considerar como o consumidor recebe a nova versão. Variáveis
de ambiente exigem recriação do Pod. Um arquivo montado pode atualizar depois
de um intervalo, mas a aplicação precisa observar e recarregar o conteúdo com
segurança. Apagar um Secret também pode quebrar Pods, jobs e controllers que
dependem dele.

## Relações

- [ServiceAccount](serviceaccount.md) fornece identidade ao Pod.
- [SOPS](../../secret-store-externo.md) trata armazenamento seguro
  antes da aplicação ao cluster.
- [Bootstrap e rotação](../../bootstrap-e-rotacao-de-segredos.md) relaciona
  distribuição e lifecycle.

## Fonte primária

- [Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)
