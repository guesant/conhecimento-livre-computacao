# Auditoria do Kubernetes

Auditoria registra eventos relacionados às requisições da API. Ela responde
quem fez uma requisição, em qual momento, a partir de onde, contra qual
recurso e qual foi o resultado. É diferente de um log de aplicação, de um
evento de Pod e de uma métrica: cada fonte explica uma parte da operação.

## O que deve ser observado

Uma política de auditoria define quais eventos são registrados e em qual
nível. A requisição pode ser observada antes ou depois da leitura do objeto,
mas registrar o conteúdo completo de todos os objetos aumenta custo e risco.
Secrets, tokens, ConfigMaps com dados sensíveis e corpos grandes exigem
tratamento especial. A política deve preservar evidência suficiente para
investigar a ação sem transformar o log em uma cópia desnecessária de
credenciais.

Os eventos importantes incluem alterações de RBAC, ServiceAccounts, Secrets,
Pods privilegiados, admission configurations, acesso a subrecursos de
execução e operações em namespaces de infraestrutura. Operações de leitura
também podem ser relevantes quando um componente acessa todos os Secrets ou
lista recursos em todo o cluster.

## Backends e retenção

O API server pode enviar eventos para arquivo local ou para um backend externo,
conforme a configuração da versão e da distribuição. Um arquivo de auditoria
precisa de rotação, permissões, espaço reservado e envio para armazenamento
protegido. Se o nó for comprometido, o arquivo local pode ser alterado ou
apagado, portanto logs centralizados e imutáveis são preferíveis para
investigação.

Defina retenção de acordo com risco, obrigação regulatória e capacidade de
consulta. Retenção infinita não é sinônimo de segurança: amplia exposição,
custo e dificuldade de separar um evento importante do ruído. Archive em um
destino com controle de acesso, integridade verificável e relógio sincronizado.

## Disponibilidade e failure mode

Auditoria acontece no caminho de uma requisição e pode consumir CPU, disco,
rede e storage. O backend não deve bloquear o API server indefinidamente por
uma falha de armazenamento, mas perder eventos de uma operação crítica também
pode ser inaceitável. A política de retenção e o comportamento quando o
backend fica indisponível precisam ser decididos conscientemente.

Monitore volume de eventos, latência de gravação, filas, drops, uso de disco e
falhas de envio. Um disco cheio em um control plane pode causar uma falha de
disponibilidade, enquanto uma configuração que descarta tudo pode manter a
disponibilidade sem fornecer evidência.

## Consultas e correlação

Correlacione `auditID` com logs do API server, eventos de admission, logs de
controllers e identidade do workload. O registro de auditoria mostra a
requisição recebida, não necessariamente o efeito final depois de vários
controllers reconciliarem o objeto.

Em um incidente, preserve o arquivo original e calcule hash antes de fazer
normalização ou ingestão. Registre fuso, sincronização de relógio e origem do
arquivo. Não altere o evento para encaixá-lo na narrativa do incidente.

## Exemplo de política mínima

O conteúdo exato depende da versão e dos requisitos do cluster, mas uma
política deve explicitar recursos, grupos, namespaces, usuários e níveis de
log. Um exemplo conceitual é:

```yaml
apiVersion: audit.k8s.io/v1
kind: Policy
rules:
  - level: Metadata
    resources:
      - group: rbac.authorization.k8s.io
        resources:
          - roles
          - rolebindings
          - clusterroles
          - clusterrolebindings
  - level: RequestResponse
    resources:
      - group: ""
        resources:
          - pods/exec
          - pods/attach
          - pods/portforward
  - level: Metadata
    omitStages:
      - RequestReceived
```

O exemplo não é uma política pronta para produção. A regra de `RequestResponse`
para subrecursos pode conter dados sensíveis e deve ser limitada por risco. A
política final precisa declarar as exceções de Secrets, configurar retenção e
ser testada com consultas reais.

## Fontes primárias

- [Auditing](https://kubernetes.io/docs/tasks/debug/debug-cluster/audit/)
- [Auditing reference](https://kubernetes.io/docs/reference/config-api/apiserver-audit.v1/)
- [Security checklist](https://kubernetes.io/docs/concepts/security/security-checklist/)
