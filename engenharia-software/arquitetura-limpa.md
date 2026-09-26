# Arquitetura Limpa

Arquitetura Limpa é uma abordagem para organizar uma aplicação de modo que regras centrais de negócio não dependam de detalhes externos como framework, banco, transporte, interface ou mecanismo de entrega. A proposta é proteger decisões de alto valor contra mudanças em detalhes que evoluem mais rapidamente.

O nome é associado ao livro de Robert C. Martin, mas o princípio central é anterior e se relaciona a ideias como separação de responsabilidades, inversão de dependências, Ports and Adapters e Onion Architecture. O diagrama de círculos não deve ser tratado como uma estrutura de diretórios obrigatória.

## Regra de dependência

A regra de dependência diz que dependências de código devem apontar para dentro, em direção às políticas e regras mais estáveis. Entidades não dependem de controllers. Casos de uso não dependem de um ORM específico. Adaptadores traduzem entre o contrato interno e detalhes externos.

Essa regra é sobre dependência de código e de conhecimento, não apenas sobre o sentido visual das setas. Se uma interface de repositório vive no núcleo e sua implementação usa PostgreSQL vive na borda, o núcleo declara o que precisa e a infraestrutura implementa o contrato. Um framework que exige herança dentro das entidades pode inverter essa relação mesmo quando os diretórios parecem corretos.

## Camadas conceituais

Entidades representam regras e invariantes do domínio que não dependem de uma aplicação específica. Casos de uso coordenam uma ação do sistema, traduzem entrada em operações de negócio e definem o resultado que o consumidor precisa.

Interface adapters convertem HTTP, CLI, eventos, DTOs, modelos de persistência e respostas externas para os formatos que os casos de uso entendem. Frameworks e drivers ficam na borda: banco, web framework, filas, cache, filesystem, SDKs e detalhes de deploy.

Uma aplicação pode nomear essas camadas como domain, application, adapters e infrastructure, ou usar outra convenção. O nome não garante a arquitetura. O teste é verificar se uma regra central consegue ser testada e evoluída sem inicializar o framework, fazer uma requisição ou conhecer a estrutura do banco.

## Fluxo de uma operação

Em uma leitura HTTP, o controller recebe e valida a forma da entrada, cria um DTO ou Query e chama um caso de uso. O caso de uso coordena portas como um reader ou repositório. A implementação concreta consulta o banco. O resultado retorna por uma estrutura de aplicação e o presenter ou controller o transforma em resposta HTTP.

Em uma escrita, o controller não deve concentrar regra de negócio. Ele traduz a entrada, o handler aplica invariantes e a infraestrutura persiste ou publica eventos. A transação, o retry, a idempotência e os efeitos assíncronos precisam ser definidos explicitamente, porque uma separação de diretórios não resolve consistência por si só.

## Inversão de dependência

Inversão de dependência não significa usar um container de injeção em toda parte. Significa que a política define uma abstração estável e detalhes dependem dela. A composição concreta ocorre em um ponto conhecido, como bootstrap, container de dependências ou módulo de infraestrutura.

Interfaces demais podem piorar o desenho. Crie uma porta quando existe uma fronteira real, uma variação, um efeito externo ou uma necessidade de teste que justifique o contrato. Uma interface que apenas repete cada método de uma classe concreta pode aumentar indirection sem proteger uma decisão relevante.

## Vantagens e custos

A abordagem ajuda a testar domínio e aplicação, trocar adaptadores, separar contrato público de modelo de persistência e controlar acoplamento ao framework. Também torna mais explícitos ownership, transações, mapeamentos e fronteiras.

O custo está em mapeamentos, DTOs, interfaces, composição e disciplina de dependências. Para um CRUD pequeno e estável, a arquitetura pode adicionar camadas sem reduzir risco. Para um sistema com várias entradas, regras importantes, integrações e ciclo de vida longo, essa separação pode reduzir mudanças acopladas.

Não confunda Arquitetura Limpa com microsserviços. Ela pode ser usada em um monólito modular, em uma aplicação server-rendered ou em um serviço distribuído. Extrair processos antes de entender as fronteiras apenas transforma dependências de código em dependências de rede.

## Como avaliar uma aplicação

Pergunte onde vivem as regras, quem pode alterá-las, quais módulos conhecem o banco, se o controller possui lógica de negócio, se o domínio importa o framework e se um teste de caso de uso precisa de rede. Examine também o caminho de erro, a transação, o timeout, a autorização e a observabilidade.

Uma arquitetura limpa não elimina dependências, ela as torna visíveis e direcionadas. O resultado esperado é que mudanças em detalhes externos tenham um raio de impacto previsível. Se os adaptadores apenas repassam chamadas, os DTOs duplicam todos os modelos sem proteger contratos e o núcleo conhece toda a infraestrutura, a separação pode ser nominal em vez de efetiva.

## Relações

- [Clean Code](clean-code.md) trata qualidade local, nomes, funções, testes e refatoração.
- [Backend](../arquitetura-aplicacoes/backend.md) descreve responsabilidades de APIs, domínio, persistência e jobs.
- [Monólito modular](../arquitetura-aplicacoes/monolito-modular.md) aplica fronteiras internas sem exigir deploy separado.
- [Barramento interno](../arquitetura-aplicacoes/bus-interno.md) apresenta command bus, query bus e event bus em uma aplicação modular.
- [Complexidade cognitiva](complexidade-cognitiva.md) ajuda a avaliar o custo mental do código dentro das camadas.

## Fontes

- [Clean Architecture, Robert C. Martin, Pearson](https://www.pearson.com/en-us/subject-catalog/p/clean-architec-ture-a-craftsmans-guide-to-software-structure-and-design/P200000009528/9780134494166)
- [Ports and Adapters, Alistair Cockburn](https://alistair.cockburn.us/hexagonal-architecture/)
- [Martin Fowler, Presentation Domain Data Layering](https://martinfowler.com/bliki/PresentationDomainDataLayering.html)
