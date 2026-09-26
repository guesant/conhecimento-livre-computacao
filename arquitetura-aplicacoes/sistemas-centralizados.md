# Sistemas centralizados

Um sistema centralizado concentra processamento, estado ou decisão em um ambiente de controle principal. O termo não exige que exista uma única máquina. Um cluster operado como uma unidade, com um banco central e uma aplicação principal, pode ser centralizado do ponto de vista de governança e dados.

## Formas de centralização

### Processo único

Uma aplicação executa em um processo ou em poucas réplicas coordenadas. Chamadas internas são locais e transações podem atravessar módulos com menos custo.

### Serviço central

Clientes diferentes dependem de uma API ou plataforma comum. A centralização facilita políticas, auditoria e consistência, mas transforma esse serviço em uma dependência compartilhada.

### Dados centralizados

Vários componentes usam uma fonte de dados comum. Isso simplifica joins e transações, mas cria acoplamento de schema, carga concentrada e um domínio de falha compartilhado.

### Controle centralizado

Uma autoridade administra identidade, configuração, políticas ou entrega. O sistema pode ter vários workers e réplicas, mas a decisão ou o controle da mudança passa por um ponto comum.

## Vantagens

Centralização reduz complexidade de coordenação. Um único modelo de dados pode usar transações locais, uma política pode ser auditada em um lugar e uma equipe pode corrigir o sistema sem negociar contratos distribuídos entre muitos owners.

Ela também ajuda no início de um produto, quando os limites de domínio ainda são incertos. Refatorar módulos dentro do mesmo processo costuma ser mais barato que refatorar APIs remotas.

## Limitações

Um componente central pode virar gargalo de capacidade ou disponibilidade. Uma falha, uma migração ruim ou uma alteração incompatível pode afetar muitos consumidores. A centralização também pode limitar autonomia de equipes e impor um ritmo de release comum.

Não confunda centralização com ausência de escala. Uma aplicação central pode ter réplicas, cache, filas e alta disponibilidade. O que permanece central é a responsabilidade ou a fonte de verdade.

## Alta disponibilidade

Eliminar um ponto único de falha exige replicação, eleição, quorum, backup, recuperação e testes. Réplicas não resolvem automaticamente escrita concorrente, split brain ou corrupção de dados.

Um banco central com múltiplas réplicas ainda precisa de estratégia para failover, consistência, migração e capacidade. Um serviço central com várias instâncias precisa de sessão, cache, locks e filas compatíveis com a execução horizontal.

## Quando escolher

Centralização é apropriada quando consistência forte, simplicidade, equipe pequena, transações cruzadas e domínio ainda em evolução pesam mais que autonomia de deploy. Um monólito modular com backend e dados bem governados pode ser uma arquitetura centralizada saudável.

## Como evitar degradação

- divida o código em módulos com ownership;
- limite dependências internas e ciclos;
- aplique paginação e limites em APIs centrais;
- separe workloads lentos em workers;
- monitore saturação, filas e latência;
- mantenha backups e restauração testados;
- estabeleça contratos, mesmo quando a chamada é local.

## Relação com microsserviços

Microsserviços reduzem parte da centralização ao distribuir capacidades, dados e deploy. Isso não significa que o sistema deixe de ter componentes centrais. DNS, identidade, observabilidade, registry, gateway e plataforma podem continuar sendo dependências comuns.

## Fontes

- [Martin Fowler, Microservices](https://martinfowler.com/articles/microservices.html)
- [NIST, contingency planning guide](https://csrc.nist.gov/pubs/sp/800/34/rev-1/final)
