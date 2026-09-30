# k3s

Kubernetes é o sistema que orquestra containers: recebe uma descrição do que deve estar rodando (quais aplicações, quantas réplicas, que recursos cada uma pode consumir) e mantém esse estado, reiniciando o que falha e distribuindo carga entre as máquinas disponíveis. Um cluster completo é composto por vários componentes que normalmente rodam separados, entre eles o servidor de API, o `etcd` que guarda o estado, o escalonador e o controller manager. Essa separação faz sentido operacional quando o cluster tem muitas máquinas, porque cada peça pode ser escalada, atualizada e observada por conta própria. Num cluster pequeno ela vira uma quantidade de peças móveis desproporcional ao problema, com custo de memória e de atenção que ninguém recupera em benefício nenhum.

k3s é uma distribuição de Kubernetes, mantida pela Rancher/SUSE, feita para reduzir exatamente esse custo operacional sem abandonar a API do Kubernetes: tudo que sabe falar com um cluster Kubernetes comum (`kubectl`, [Helm](containers/packaging/helm.md), um manifesto YAML padrão) fala com um cluster k3s sem adaptação. A diferença está em como ele é empacotado e executado, não no que ele expõe para quem usa. Uma consequência prática dessa compatibilidade é que a versão do k3s continua sendo uma versão do Kubernetes, embora inclua um sufixo que identifica a revisão do empacotamento. Quem precisa saber se um recurso da API existe num cluster olha para a versão correspondente e consulta a documentação do Kubernetes, sem precisar de uma tabela de tradução.

## Binário único

Em vez de vários processos e serviços separados, k3s empacota os componentes essenciais de um cluster Kubernetes num único binário Go, com dependências trocadas por alternativas mais leves, como SQLite num cluster de nó único. Isso reduz o consumo de memória e o número de processos a monitorar, tornando viável rodar Kubernetes em hardware modesto. O mesmo binário ainda traz um cliente embutido, invocado como `k3s kubectl`, sem depender de um `kubectl` separado no node. A contrapartida do empacotamento único é que atualizar qualquer componente significa trocar o binário inteiro e reiniciar o serviço, em vez de atualizar uma peça de cada vez.

## kubeconfig

O `kubeconfig` é o arquivo que o `kubectl` (e qualquer outra ferramenta que fale com a API do Kubernetes) usa para saber a qual cluster se conectar, com qual credencial e, quando há mais de um cluster configurado, qual contexto usar por padrão. Ele contém o endereço do servidor de API, o certificado da autoridade certificadora do cluster (para validar que está falando com o servidor certo) e a credencial de quem está conectando. Perder esse arquivo não significa perder o cluster, mas significa perder o acesso administrativo a ele até gerar ou recuperar um novo.

## Compatibilidade de versão entre kubectl e o API server

O projeto Kubernetes declara um limite explícito de quanto um `kubectl` pode divergir da versão do API server com que ele fala, normalmente até uma versão minor de distância em qualquer direção. Fora dessa janela, o cliente monta uma requisição num formato que o servidor já não entende mais, ou deixa de enviar um campo que o servidor passou a exigir, e o erro só aparece na hora de aplicar um manifesto, não na conexão em si. Isso importa em qualquer lugar que baixe um `kubectl` separado da versão do próprio cluster, como uma imagem de ferramentas de CI, porque essas versões podem divergir silenciosamente com o tempo se nada as mantiver alinhadas.

## Continue por aqui

O [Ansible](ansible.md) pode instalar e configurar esta distribuição, enquanto uma pipeline de CI pode verificar a compatibilidade entre a versão do `kubectl` usada pelas ferramentas e a versão do k3s.
