# Warehouse

Warehouse é o recurso do Kargo que observa fontes de artefatos e gera Freight
elegível para promoção. Ele funciona como uma fronteira de descoberta: conhece
onde procurar, como interpretar versões e quais combinações podem formar um
candidato, mas não representa sozinho a aplicação já implantada.

## Fontes e subscriptions

Um Warehouse pode observar imagens de container, repositórios Git e outros
recursos suportados pela versão do Kargo. A configuração informa repositório,
credencial, filtros, política de seleção e intervalo de observação. O recurso
precisa ter acesso somente de leitura quando a fonte não exige escrita.

A subscription não deve ser confundida com uma promoção. Ela define como uma
fonte participa da descoberta; o Stage decide como o Freight será transformado
no ambiente. Misturar esses papéis torna difícil descobrir se uma falha ocorreu
na busca, na seleção ou na aplicação.

## Seleção de versões

O Warehouse pode observar a versão mais recente, combinar versões de várias
imagens ou exigir que um commit Git acompanhe o artefato. A política precisa
ser determinística. Se a ordem dos componentes não for definida, duas
execuções podem criar Freight diferente a partir das mesmas fontes.

Tags móveis devem ser tratadas com cautela. Para delivery auditável, registre
digests e commits. A fonte pode publicar a imagem e atualizar o Git em momentos
diferentes; a estratégia deve esperar consistência, rejeitar combinações
incompletas ou declarar explicitamente que a versão parcial é aceitável.

## Reconciliação

O controller observa o Warehouse, consulta as fontes e atualiza o status. Uma
falha transitória de registry, credencial ou rede não deve produzir um Freight
falso. O status precisa diferenciar erro de autenticação, ausência de versão,
filtro sem resultado e falha de criação do candidato.

Ao alterar a configuração, considere o histórico de Freight já criado. Remover
um filtro não deve apagar cegamente candidatos que ainda sustentam rollback.
Retenção e garbage collection precisam preservar as versões necessárias ao
rollback e à auditoria.

## Relações

- [Freight](freight.md) é o candidato criado pelo Warehouse.
- [Kargo](index.md) apresenta a reconciliação e a promoção.
- [Supply chain](../../seguranca/supply-chain/index.md) trata provenance, digest e assinatura.

## Fontes primárias

- [Kargo Warehouse](https://docs.kargo.io/concepts/warehouses/)
- [Kargo image subscriptions](https://docs.kargo.io/concepts/warehouses/#subscriptions)
