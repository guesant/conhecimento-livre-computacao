# TLS automático

TLS é o protocolo que cifra uma conexão e prova a identidade de um servidor por meio de um certificado, emitido por uma autoridade certificadora em quem o navegador (ou outro cliente) já confia de antemão. Antes de existir uma forma automatizada de obter esse certificado, o processo era manual: gerar uma solicitação de certificado, enviar para uma autoridade certificadora, pagar, provar posse do domínio de alguma forma específica daquela autoridade, e repetir tudo isso periodicamente antes de cada expiração. Isso tornava TLS uma fricção real, e por muito tempo foi comum sites inteiros rodarem sem cifragem só para evitar esse processo.

## ACME e a Let's Encrypt

O protocolo ACME (Automatic Certificate Management Environment) padronizou esse processo: um cliente ACME prova a posse de um domínio de forma automatizada (respondendo a um desafio HTTP num caminho específico daquele domínio, ou publicando um registro DNS específico) e recebe, também de forma automatizada, um certificado válido, tipicamente por 90 dias. A Let's Encrypt é a autoridade certificadora sem fins lucrativos que popularizou esse fluxo, emitindo certificados gratuitos e validados só por esse processo automatizado, sem intervenção humana em nenhum dos dois lados. A validade curta de 90 dias não é uma limitação, é uma escolha deliberada: como a renovação é automática, um certificado de vida curta reduz o estrago de uma chave privada comprometida sem impor nenhum custo operacional a mais em troca.

## O padrão de operator aplicado à emissão de certificado

Dentro de um cluster Kubernetes, esse fluxo inteiro (solicitar, provar posse, renovar antes de expirar, distribuir o certificado renovado para quem precisa dele) pode ser automatizado por um operator dedicado a isso; cert-manager é a implementação mais usada desse padrão. Ele observa objetos declarando "este domínio precisa de um certificado válido, emitido por esta autoridade" e mantém isso verdade continuamente, renovando antes da expiração sem intervenção manual, incluindo casos em que a validade é de só alguns dias. O conceito geral de operator, que sustenta isso, está detalhado em [Operators do Kubernetes](kubernetes-operators.md).

## Continue por aqui

O cert-manager é instalado neste cluster pela role documentada em [Ansible: as roles do bootstrap](../arquitetura/ansible.md).
