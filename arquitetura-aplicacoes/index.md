# Arquitetura de aplicações

Uma aplicação pode ser descrita por várias dimensões ao mesmo tempo. Frontend e backend dizem respeito a responsabilidades e ao lado da interação em que elas acontecem. Monólito e microsserviços dizem respeito à forma como a aplicação é dividida em unidades de execução e deploy. Microfrontend descreve uma estratégia para dividir a camada de interface.

Esses termos não são alternativas na mesma dimensão. Uma aplicação pode ter um frontend React, um backend Laravel monolítico e um banco PostgreSQL. Também pode ter um frontend composto por microfrontends e um backend composto por serviços. O erro comum é tratar "frontend", "backend" e "microsserviço" como classificações concorrentes.

## Dimensões

| Dimensão | Pergunta | Exemplos |
| --- | --- | --- |
| Interface | Onde a interação com o usuário acontece? | Server-rendered, SPA, mobile, CLI |
| Backend | Onde vivem regras, dados e integrações? | API, aplicação web, workers |
| Unidade de execução | O que sobe e escala junto? | Monólito, serviço, função |
| Unidade de deploy | O que é publicado independentemente? | Aplicação, serviço, microfrontend |
| Fronteira de dados | Quem é dono do estado? | Banco compartilhado, banco por serviço |
| Fronteira de equipe | Quem constrói e opera a capacidade? | Equipe por camada ou por domínio |

## Composição típica

O navegador ou outro cliente envia uma requisição para um frontend ou diretamente para uma API. O frontend pode renderizar HTML, executar JavaScript e chamar o backend. O backend autentica, autoriza, valida a entrada, executa regras de negócio, lê ou grava dados e integra sistemas externos.

Essa divisão não exige processos separados. Em um monólito web, frontend, controllers, domínio, jobs e acesso ao banco podem estar no mesmo executável. A separação é lógica, mesmo quando o deploy é único.

Em uma arquitetura distribuída, a chamada entre módulos pode virar HTTP, gRPC ou mensagem. Essa mudança introduz rede, timeout, retry, autenticação entre serviços, observabilidade, consistência eventual e falhas parciais. Distribuir um módulo não é somente mover arquivos para outro repositório.

## Fronteiras importantes

Uma boa fronteira deve reduzir mudanças acopladas, ter contratos claros, possuir dados que possam ser governados e ser operável por uma equipe. Fronteiras artificiais criam chamadas chatty, duplicação de modelos e dependências cíclicas.

A capacidade de fazer deploy independente só existe quando o componente realmente pode ser testado, publicado, observado e revertido sem exigir que todos os consumidores mudem ao mesmo tempo. Um processo separado sem autonomia de dados e release pode ser apenas um monólito distribuído.

## Escolha inicial

Para uma equipe pequena ou um produto ainda incerto, um monólito modular costuma reduzir custo e preservar a possibilidade de refatorar. Microsserviços fazem sentido quando existem limites de domínio compreendidos, necessidades de escala ou disponibilidade diferentes, equipes autônomas e maturidade operacional para operar uma rede de serviços.

Microfrontend faz sentido quando a organização precisa de autonomia de equipes na interface e aceita o custo de contratos de navegação, design system, runtime, observabilidade e performance. Não é uma técnica obrigatória para dividir um frontend grande.

## Conteúdo desta seção

- [Frontend](frontend.md) explica interface, renderização, estado e comunicação com o backend.
- [Backend](backend.md) explica APIs, domínio, persistência, jobs e integração.
- [Monólito](monolito.md) explica execução e deploy como uma unidade, incluindo o monólito modular.
- [Monólito modular](monolito-modular.md) explica fronteiras internas, contratos de módulos e evolução de uma aplicação única.
- [Barramento interno](bus-interno.md) explica comandos, consultas e eventos dentro do mesmo processo, com exemplos para Java.
- [Erlang/OTP](erlang-otp.md) explica processos leves, `gen_server` e árvores de supervisão.
- [Microsserviços](microsservicos.md) explica fronteiras distribuídas, dados, contratos e operação.
- [Microfrontend](microfrontend.md) explica composição de interfaces independentes.
- [Comparativo](comparativo.md) organiza os trade-offs sem transformar uma opção em regra universal.
- [Sistemas centralizados](sistemas-centralizados.md) explica concentração de
  processamento, dados, controle e suas formas de escala.
- [Sistemas distribuídos](sistemas-distribuidos.md) explica falhas parciais,
  coordenação, consistência e operação por rede.
- [Self-stabilization e autoestabilização](self-stabilization.md) explica convergência
  para estados legítimos depois de corrupção transitória ou início arbitrário.
- [Centralizado, distribuído e microsserviços](centralizado-distribuido-microservicos.md)
  compara as dimensões e os critérios de escolha.

## Fontes

- [Martin Fowler, Microservices](https://martinfowler.com/articles/microservices.html)
- [Martin Fowler, Micro Frontends](https://martinfowler.com/articles/micro-frontends.html)
- [micro-frontends.org](https://micro-frontends.org/)
- [Microsoft, Backend for Frontend](https://learn.microsoft.com/en-us/azure/architecture/patterns/backends-for-frontends)
