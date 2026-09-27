# Open Policy Containers

Open Policy Containers, OPCR, é uma proposta para empacotar e distribuir
políticas como artefatos compatíveis com registries de container. A política
passa a ter digest, metadados e um fluxo de promoção semelhante ao de outros
artefatos de supply chain.

## Benefícios

O empacotamento facilita versionamento, assinatura, replicação e promoção entre
ambientes. O consumidor ainda precisa validar o tipo de política, a linguagem,
as dependências e a compatibilidade do runtime.

## Segurança

Trate o artefato de política como código executável do ponto de vista da
decisão. Use digest, assinatura, provenance e revisão antes de carregá-lo em
um PDP ou admission controller.

## Fonte

- [Open Policy Containers](https://openpolicycontainers.com/)
