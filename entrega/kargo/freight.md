# Freight

Freight é a unidade de promoção do Kargo. Ela representa uma versão candidata
de um conjunto de artefatos, normalmente imagens de container e metadados
associados, que pode atravessar uma sequência de stages. O Freight não é apenas
uma tag: ele registra uma seleção concreta de artefatos e serve como objeto
observável para promoção, verificação e rollback.

## Relação com Warehouse e Stage

Um Warehouse observa repositórios ou registries e cria Freight quando encontra
uma combinação que satisfaz seus critérios. Um Stage define como esse Freight
será transformado e aplicado em um ambiente. A promoção liga o Freight a um
Stage, enquanto as imagens continuam armazenadas no registry.

```mermaid
flowchart LR
    registry[Registry ou Git]
    warehouse[Warehouse]
    freight[Freight candidato]
    stage[Stage]
    delivery[Manifestos do ambiente]
    registry --> warehouse
    warehouse --> freight
    freight --> stage
    stage --> delivery
```

## Imutabilidade e identidade

Uma tag pode ser movida ou sobrescrita. Um digest identifica o conteúdo do
artefato e deve ser usado quando a promoção precisa ser reproduzível. O Freight
precisa permitir responder qual imagem, qual digest, qual commit e quais
transformações chegaram ao ambiente. Reutilizar uma tag sem atualizar a
identidade observada pode fazer a promoção parecer concluída enquanto o
workload executa conteúdo diferente.

## Seleção e promoção

O Warehouse pode combinar artefatos, exigir ordem, aplicar filtros e incluir
metadados. A estratégia deve evitar que uma imagem incompatível com o schema ou
com o ambiente seja elegível apenas porque possui a tag esperada. Stage pode
executar verificações, gerar valores, aplicar manifests e exigir aprovação
manual ou promoção automática.

Promoção não é o mesmo que build. O build produz um artefato; o Freight
identifica uma versão candidata; o Stage define a transformação e o destino.
Separar essas responsabilidades facilita reprocessar uma entrega sem compilar
novamente o mesmo conteúdo.

## Diagnóstico e rollback

Investigue a cadeia por nome do Freight, digest, Stage, health checks e revisão
do recurso de destino. Um rollback seguro seleciona um Freight anterior que
continua disponível e compatível com o schema do ambiente. Apagar artefatos ou
reutilizar tags durante uma promoção quebra a capacidade de reconstruir o
histórico.

## Relações

- [Warehouse](warehouse.md) define como candidatos são descobertos.
- [Kargo](index.md) explica projetos, stages e promoção.
- [Digest de imagem](../../containers/digest.md) define a identidade do artefato.

## Fontes primárias

- [Kargo Freight](https://docs.kargo.io/concepts/freight/)
- [Kargo promotion](https://docs.kargo.io/concepts/promotion/)
