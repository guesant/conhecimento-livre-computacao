# Checkov

Checkov é uma ferramenta de análise estática para infraestrutura como código. Ela possui checks para múltiplos frameworks, incluindo Terraform/OpenTofu, Kubernetes e outros formatos.

## Casos de uso

É útil em repositórios heterogêneos que desejam uma camada comum de checks sobre várias linguagens de infraestrutura.

## Boa prática

Escolha checks relevantes ao contexto, fixe versão da ferramenta na CI e documente suppressions com justificativa. Analise código renderizado quando transformações fazem parte da entrega.

## Má prática

Habilitar toda regra disponível e depois ignorar centenas de findings cria fadiga. Também é inadequado tratar compliance de ferramenta como prova de segurança da infraestrutura em runtime.

## Fontes

- Checkov: https://www.checkov.io/

## Continue por aqui

[KubeLinter](kubelinter.md) é mais estreito e especializado em Kubernetes.