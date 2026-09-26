# Comparativo de arquiteturas de aplicações

Monólito, microsserviços e microfrontend não são escolhas mutuamente exclusivas. Frontend e backend são camadas de responsabilidade; monólito e microsserviços são formas de dividir processos e deploy; microfrontend é uma forma de dividir a interface.

## Comparação

| Dimensão | Monólito modular | Microsserviços | Microfrontend |
| --- | --- | --- | --- |
| Unidade principal | Aplicação ou módulo | Serviço por capacidade | Parte de interface |
| Comunicação | Chamadas locais | Rede ou mensagens | Composição HTML, módulos ou eventos |
| Dados | Pode compartilhar banco | Ownership por serviço | Não define persistência |
| Deploy | Geralmente conjunto | Independente por serviço | Independente por parte |
| Falhas | Mais locais ao processo | Parciais e distribuídas | Falha por região ou remote |
| Operação | Mais simples | Mais complexa | Complexa no runtime do cliente |
| Escala | Aplicação inteira ou módulos internos | Por serviço | Bundle, remote ou rota |

## Critérios

Considere primeiro o domínio e a equipe. Se os limites ainda mudam, mantenha módulos no mesmo processo para permitir refatoração barata. Se uma capacidade precisa escalar, publicar ou isolar falhas de maneira diferente, extraia um serviço com contrato próprio.

Considere microfrontend somente quando a independência de equipes na interface for um problema real. Se a dor é bundle grande, use code splitting. Se a dor é código desorganizado, use módulos e boundaries. Se a dor é deploy lento, investigue o pipeline antes de adicionar composição remota.

## Matriz de decisão

| Situação | Direção provável |
| --- | --- |
| Produto pequeno e domínio incerto | Monólito modular |
| Uma equipe full stack | Monólito modular ou frontend e backend bem separados |
| Capacidades com escalas muito diferentes | Serviço separado após medir necessidade |
| Equipes independentes por domínio | Microsserviços ou módulos com ownership claro |
| Interface com equipes e releases independentes | Microfrontend, se contratos forem sustentáveis |
| Apenas bundle inicial grande | Code splitting e carregamento sob demanda |
| Necessidade de alta consistência entre operações | Manter a transação no mesmo módulo |
| Integrações demoradas ou reprocessáveis | Jobs e mensagens, em monólito ou serviços |

## Caminhos de evolução

Uma evolução comum é começar com um monólito modular, separar frontend e backend por contrato, extrair jobs assíncronos, publicar APIs estáveis e somente depois extrair uma capacidade que tenha motivo concreto. A direção inversa também é válida: vários serviços podem ser reunidos quando a distribuição deixou de trazer benefício.

O critério é o custo total. Conte build, deploy, infraestrutura, observabilidade, suporte, incidentes, tempo de mudança, consistência, segurança e capacidade de contratação. Independência de deploy é valiosa, mas não compensa automaticamente uma rede de dependências frágeis.

## Erros comuns

- chamar qualquer API de microsserviço;
- dividir por camada técnica em vez de capacidade;
- compartilhar banco e declarar autonomia;
- criar microfrontends para resolver problemas de organização interna;
- permitir chamadas remotas pequenas e encadeadas;
- esconder autorização apenas na interface;
- assumir que um container por processo reduz complexidade;
- ignorar rollback e compatibilidade entre versões.

## Fontes

- [Martin Fowler, Microservices](https://martinfowler.com/articles/microservices.html)
- [Martin Fowler, microservice trade-offs](https://martinfowler.com/articles/microservice-trade-offs.html)
- [micro-frontends.org](https://micro-frontends.org/)
- [webpack, Module Federation](https://webpack.js.org/concepts/module-federation/)
