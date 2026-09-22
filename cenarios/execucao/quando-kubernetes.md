# Quando Kubernetes faz sentido

Kubernetes é uma plataforma de reconciliação e orquestração, não uma condição para executar containers. A pergunta útil é quais problemas adicionais sua API e seu ecossistema resolvem no cenário em questão.

## O que Kubernetes compra

Controllers reconciliam estado desejado; scheduler escolhe placement; Services abstraem endpoints; namespaces e RBAC criam fronteiras administrativas; CNI e NetworkPolicy estruturam rede; CSI abstrai storage; CRDs/operators estendem a API; admission/policy permitem governança; ecossistemas de GitOps e observabilidade assumem essas primitives.

Se várias dessas propriedades são necessárias, operar a plataforma pode ser mais barato que reconstruí-las separadamente.

## O que Kubernetes não compra sozinho

Não cria alta disponibilidade quando todos os nós compartilham o mesmo failure domain. Não torna automaticamente uma aplicação stateless. Não resolve backup, disaster recovery, segurança de aplicação ou observabilidade apenas porque existem objetos Kubernetes para integrá-los.

## Cenário favorável

Múltiplos serviços, deploy frequente, necessidade de reconciliação, equipes compartilhando infraestrutura, políticas uniformes, operators, integração com ecossistema cloud-native ou múltiplos clusters tornam a plataforma progressivamente mais justificável.

## Cenário desfavorável

Um host com poucos serviços estáveis e uma equipe pequena pode obter quase todo o valor necessário com systemd e containers. Nesse caso, Kubernetes adiciona control plane, rede de cluster, certificados e abstrações de storage sem necessariamente remover outra complexidade.

## Kubernetes como contrato de portabilidade

Usar a API Kubernetes em ambientes pequenos pode ser deliberado quando ela é o contrato comum entre edge, laboratório e produção. O benefício é padronização operacional, não eficiência absoluta de cada host.

Esse argumento só vale quando a organização realmente reutiliza manifests, charts, operators, policies, automação ou conhecimento. Instalar Kubernetes em todo lugar sem reutilização apenas replica custo.

## Modos de uso

Kubernetes gerenciado transfere parte da operação do control plane ao provedor. Distribuições leves como K3s reduzem footprint e empacotamento. Clusters self-managed completos dão mais controle e também mais responsabilidades.

A escolha da modalidade deve ser separada da escolha da API Kubernetes.

## Anti-patterns

"Kubernetes porque pode crescer" sem horizonte ou requisito concreto é speculative complexity. "Nunca Kubernetes em single-node" também é uma regra ruim: operators, API comum, GitOps ou laboratório fiel podem justificar o custo.

## Continue por aqui

[Single-node](single-node.md) compara padrões concretos. [Distribuições Kubernetes](../../distribuicoes-kubernetes.md) trata formas de empacotar a plataforma.
