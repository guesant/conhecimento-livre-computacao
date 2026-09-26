# TLS automático

TLS é o protocolo que cifra uma conexão e prova a identidade de um servidor por meio de um certificado, emitido por uma autoridade certificadora em quem o navegador (ou outro cliente) já confia de antemão. Antes de existir uma forma automatizada de obter esse certificado, o processo era manual: gerar uma solicitação de certificado, enviar para uma autoridade certificadora, pagar, provar posse do domínio de alguma forma específica daquela autoridade, e repetir tudo isso periodicamente antes de cada expiração.

Isso tornava TLS uma fricção real, e por muito tempo foi comum sites inteiros rodarem sem cifragem só para evitar esse processo.

## ACME e a Let's Encrypt

O protocolo ACME (Automatic Certificate Management Environment) padronizou esse processo: um cliente ACME prova a posse de um domínio de forma automatizada e recebe, também de forma automatizada, um certificado com validade curta. A Let's Encrypt é a autoridade certificadora sem fins lucrativos que popularizou esse fluxo, emitindo certificados gratuitos e validados só por esse processo automatizado, sem intervenção humana de nenhum lado.

Essa validade curta não é uma limitação, é uma escolha deliberada: como a renovação é automática, um certificado de vida curta reduz o estrago de uma chave privada comprometida sem impor nenhum custo operacional a mais em troca.

O desafio HTTP-01 prova a posse respondendo numa rota específica do próprio domínio, servida no caminho que a autoridade certificadora consulta durante a validação; o desafio DNS-01 prova a mesma posse publicando um registro TXT temporário na zona DNS do domínio. Só o DNS-01 valida um certificado wildcard, que cobre todos os subdomínios de um domínio com um único certificado, porque a prova recai sobre a zona inteira, não sobre uma rota HTTP de um subdomínio específico.

No cert-manager, o emissor que usa DNS-01 declara o provedor de DNS dentro do campo `solvers`, apontando para o segredo que guarda o token de API do provedor pelo campo `apiTokenSecretRef`. Esse token nunca precisa de mais permissão do que editar registros DNS da zona em questão, porque é só isso que o desafio exige.

## O padrão de operator aplicado à emissão de certificado

Dentro de um cluster Kubernetes, esse fluxo inteiro (solicitar, provar posse, renovar antes de expirar, distribuir o certificado renovado para quem precisa dele) pode ser automatizado por um operator dedicado a isso; cert-manager é a implementação mais usada desse padrão. Ele observa objetos declarando "este domínio precisa de um certificado válido, emitido por esta autoridade" e mantém isso verdade continuamente, renovando antes da expiração sem intervenção manual, incluindo casos em que a validade é de só alguns dias.

O conceito geral de operator, que sustenta isso, está detalhado em [Operators do Kubernetes](kubernetes-operators.md).

## Quando o domínio não existe na Internet

ACME e a Let's Encrypt resolvem o caso de um domínio público, que qualquer cliente da Internet precisa validar. Um cluster também pode ter nomes internos, que só fazem sentido dentro da própria rede e nunca são resolvíveis por fora, e para esses nomes a Let's Encrypt simplesmente não emite certificado, porque não tem como provar posse de um domínio que não existe publicamente.

A saída, nesse caso, é o próprio cert-manager emitir a partir de uma autoridade certificadora interna que ele mesmo cria: um `ClusterIssuer` autoassinado gera um certificado de CA, e um segundo emissor, apontando para essa CA, emite os certificados de uso final.

Nenhum cliente fora da rede confia nessa CA por padrão, então ela precisa ser instalada manualmente nos dispositivos que vão confiar nesses nomes internos, ao contrário de uma CA pública como a Let's Encrypt, que todo navegador já traz embutida.

## `cmctl`: diagnosticar sem esperar o próximo ciclo de reconciliação

O cert-manager expõe seu estado através dos próprios recursos que gerencia, a cadeia `Certificate`, `CertificateRequest` e os recursos de desafio ACME descrita em [Diagnóstico de Pod, nó, certificado e Argo CD](../operacional/diagnostico-de-pod-no-cluster-e-do-argocd.md), mas inspecionar essa cadeia manualmente a cada vez é mais lento do que precisa ser.

`cmctl` é o cliente de linha de comando complementar ao próprio cert-manager, com atalhos específicos para isso: `cmctl status certificate` resume o estado de um certificado sem montar manualmente a consulta à cadeia inteira de recursos, e `cmctl renew` força uma tentativa de renovação imediata. Esse segundo comando serve para confirmar que a causa de uma falha já foi corrigida, sem esperar pelo próximo ciclo automático de renovação.

Um detalhe que vale reter para não errar a instalação: o `cmctl` versiona de forma independente do próprio cert-manager, então pareá-los pelo mesmo número de versão é um erro de suposição, não uma regra real do projeto. A versão certa de cada um vem da respectiva página de releases, não de assumir que os dois avançam juntos.

## Continue por aqui

O cert-manager entra neste cluster como `Application` de plataforma do Argo CD, sincronizada pelo root, e não por uma role própria do Ansible; veja [GitOps: root e satélites](../arquitetura/gitops-root-e-satelites.md). O uso real dele aqui é justamente o caso de domínio interno descrito acima, para os nomes sob `guesant.internal` alcançáveis só pela tailnet: a cadeia de `ClusterIssuer` autoassinados e o certificado curinga que ela emite estão detalhados em [Ingress: os nomes internos pela tailnet](../arquitetura/ingress.md).
