# Engenharia de software

Engenharia de software trata decisões de desenho, evolução, teste e operação do código.
Princípios não são checklists que garantem qualidade sozinhos. Eles ajudam a formular
perguntas sobre responsabilidade, dependência, coesão, mudança e custo de manutenção.

## Escopo

Uma decisão de design deve considerar domínio, linguagem, tamanho do sistema, equipe,
ciclo de mudança, desempenho e requisitos de operação. Um princípio útil em um framework
orientado a objetos pode precisar de outra forma em um programa funcional, uma aplicação
de dados ou um script operacional.

## Conteúdo

- [Ciclo de vida de aplicações](ciclo-de-vida-de-aplicacoes.md) organiza planejamento,
  requisitos, arquitetura, implementação, entrega, operação, manutenção, métricas e
  aposentadoria.
- [Engenharia de requisitos](requisitos/index.md) reúne elicitação, especificação,
  requisitos funcionais e não funcionais, Use Cases, BDD, backlog e priorização.
- [Clean Code](clean-code.md) discute legibilidade, coesão, tratamento de erros, testes e
  refatoração sem transformar heurísticas em regras universais.
- [Arquitetura Limpa](arquitetura-limpa.md) organiza dependências para proteger políticas
  centrais de detalhes externos.
- [Complexidade ciclomática](complexidade-ciclomatica.md) mede caminhos de controle e
  apoia testes e priorização de revisão.
- [Complexidade cognitiva](complexidade-cognitiva.md) estima a dificuldade de compreender
  o fluxo e o contexto de uma função.
- [SOLID](solid.md) apresenta cinco princípios para avaliar desenho orientado a objetos.
- [Concorrência e sincronização](concorrencia/index.md) organiza condições de corrida,
  mutexes, semáforos, deadlocks, leases e protocolos de progresso.
- [Edsger W. Dijkstra](dijkstra.md) apresenta as contribuições de Dijkstra para algoritmos,
  programação estruturada, verificação formal, concorrência e sistemas distribuídos.

SOLID se relaciona a coesão e acoplamento, mas não substitui modularidade, testes,
observabilidade, modelagem de domínio, segurança ou simplicidade. Aplicar abstrações
antes de existir uma variação real pode produzir mais código e esconder o fluxo.
