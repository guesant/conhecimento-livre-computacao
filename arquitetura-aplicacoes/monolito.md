# Monólito

Um monólito é uma aplicação publicada como uma unidade de execução ou deploy. Isso não significa que todo o código esteja sem módulos. Um monólito modular pode ter fronteiras internas fortes, contratos entre domínios e equipes responsáveis por partes diferentes, enquanto continua compartilhando o processo e, às vezes, o banco.

## Tipos de monólito

### Monólito tradicional

Interface, controllers, regras, acesso a dados e jobs podem viver no mesmo projeto e ser publicados juntos. A simplicidade operacional é uma vantagem, mas a separação interna pode se degradar com o tempo.

### Monólito modular

Módulos são organizados por capacidade ou contexto de negócio. Cada módulo define entradas, saídas e dependências permitidas. O código pode compartilhar runtime, mas não deve acessar internals de outro módulo sem uma interface deliberada.

### Monólito distribuído

Partes que deveriam ser uma unidade são espalhadas por processos que dependem uns dos outros para cada operação. Ele possui custo de rede e de operação sem obter autonomia real de deploy ou dados. É um risco comum ao extrair serviços por camadas técnicas em vez de capacidades de negócio.

## Vantagens

Um monólito reduz chamadas de rede internas, facilita transações locais, simplifica debug e exige menos componentes de infraestrutura. Uma alteração coordenada pode ser testada e publicada como um único artefato. Para uma equipe pequena, isso libera tempo para produto e qualidade.

Ele também pode escalar horizontalmente. Várias instâncias do mesmo aplicativo atrás de um balanceador não deixam de ser um monólito; escala de execução e decomposição em serviços são decisões diferentes.

## Limitações

Quando o código cresce sem modularidade, mudanças tornam-se acopladas, o build fica lento, uma falha pode afetar toda a aplicação e cada parte precisa escalar junto. Um banco compartilhado pode dificultar evolução e criar dependência entre módulos.

Esses problemas não são consequência inevitável do monólito. Eles indicam ausência de fronteiras, testes insuficientes ou ciclo de vida inadequado.

## Como manter um monólito saudável

- organize por domínio ou capacidade, não apenas por tipo técnico;
- proíba dependências entre internals de módulos;
- mantenha DTOs e contratos internos explícitos;
- atribua ownership por módulo;
- meça build, deploy, latência e tamanho das mudanças;
- use testes de arquitetura para impedir ciclos;
- mantenha migrações e transações coerentes;
- extraia apenas quando houver uma razão operacional concreta.

## Quando extrair

Extração pode ser justificada por escala muito diferente, isolamento de falha, requisito de disponibilidade, autonomia de equipe, ciclo de release ou fronteira de segurança. Comece por uma capacidade relativamente independente, defina seu contrato e extraia dados junto com o comportamento quando isso for necessário.

Não extraia uma tabela ou uma camada inteira apenas para produzir um serviço. A nova unidade deve ter responsabilidade clara e uma maneira de operar, observar, testar e reverter mudanças.

## Fontes

- [Martin Fowler, Microservices](https://martinfowler.com/articles/microservices.html)
- [Martin Fowler, monolith first](https://martinfowler.com/bliki/MonolithFirst.html)
- [Martin Fowler, modularity](https://martinfowler.com/articles/monolith-first.html)
