# Kong Gateway

Kong Gateway é um API gateway que combina roteamento, autenticação, plugins,
rate limiting, transformação e observabilidade. Ele implementa o conceito de
gateway, mas não substitui o domínio da aplicação nem define sozinho o contrato
de cada serviço.

## Catálogo com banco

No modo tradicional, o Kong guarda serviços, rotas, consumers e configuração de
plugins em um banco relacional. No Kong atual, PostgreSQL é a opção principal;
versões anteriores também suportavam Cassandra. O banco introduz uma dependência
operacional, credenciais e um estado compartilhado que precisa ser protegido
durante migrações ou múltiplas instalações.

O decK sincroniza um arquivo declarativo com o catálogo por meio da API
administrativa. Ele calcula a diferença entre estado desejado e estado real e
permite revisar a mudança antes de aplicá-la, sem editar o banco diretamente.

## Modo sem banco

No modo DB-less, o gateway carrega o catálogo de um arquivo declarativo YAML ou
de uma configuração enviada ao endpoint apropriado. Leituras continuam
disponíveis, mas escritas incrementais pela API administrativa não são a fonte
de verdade. Uma alteração substitui o documento completo e exige recarga.

Esse modo remove o banco externo, mas não elimina o estado: ele passa a viver no
arquivo e no processo de publicação. Plugins que precisam persistir estado entre
requisições podem não oferecer o mesmo comportamento. A compatibilidade deve ser
verificada para cada versão e plugin usado.

## Kong Ingress Controller

No Kubernetes, o Kong Ingress Controller traduz recursos como Ingress ou CRDs do
Kong em configuração do gateway. O catálogo passa a ser representado por
objetos do cluster e pode seguir o fluxo GitOps dos demais manifests. O preço é
acoplar as rotas ao modelo de objetos e ao ciclo de reconciliação do Kubernetes.

## Modo híbrido

O modo híbrido separa control plane e data plane. O control plane mantém o
catálogo e a coordenação; os data planes recebem a configuração e processam o
tráfego sem precisar de um banco local. Isso permite distribuir o processamento
e isolar a superfície administrativa, mas adiciona canais de sincronização,
certificados e estados intermediários para operar.

## Konnect

Konnect é o control plane gerenciado do ecossistema Kong. O operador mantém um
ou mais data planes e entrega a gestão do catálogo a um serviço externo. Isso
reduz infraestrutura própria, mas cria dependência de conectividade, política de
dados e licenciamento. O fato de o tráfego continuar passando pelo data plane
local não elimina a importância de proteger o canal de gestão.

## Quando escolher

DB-less faz sentido quando configuração declarativa imutável e ausência de banco
são prioridades. O modo com banco é mais adequado quando mudanças incrementais,
plugins e gestão centralizada são necessários. O modo híbrido ajuda quando a
escala ou a separação entre gestão e tráfego justifica a complexidade. Em um
ambiente pequeno, o gateway deve ser comparado ao custo de um reverse proxy com
políticas menores.

## Relações

- [API gateway](index.md) define a categoria e a fronteira com reverse proxy.
- [Service](service.md), [Route](route.md), [Plugin](plugin.md) e
  [Consumer](consumer.md) descrevem as principais abstrações do catálogo.
- [Gateway API](../../gateway-api.md) apresenta o padrão Kubernetes que pode
  ser usado pelo controlador.
- [Rate limiting](../rate-limiting/index.md) descreve políticas de consumo.

## Fontes primárias

- [Kong Gateway concepts](https://docs.konghq.com/gateway/latest/)
- [decK](https://docs.konghq.com/deck/latest/)
- [Kong DB-less mode](https://docs.konghq.com/gateway/latest/production/deployment-topologies/db-less-and-declarative-config/)
- [Kong Ingress Controller](https://docs.konghq.com/kubernetes-ingress-controller/latest/)
