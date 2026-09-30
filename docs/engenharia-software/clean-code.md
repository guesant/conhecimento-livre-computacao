# Clean Code

Clean Code é uma família de práticas para tornar o código compreensível, modificável e verificável. O termo ficou associado ao livro de Robert C. Martin, mas as ideias não formam uma especificação formal nem uma lista universal de regras. Um código é "limpo" em relação ao domínio, à equipe, à linguagem, ao ciclo de mudança e ao nível de risco que precisa suportar.

O objetivo não é fazer todos os arquivos parecerem iguais. É reduzir o esforço necessário para entender uma intenção, localizar uma mudança, testar um comportamento e identificar uma falha. Uma regra que reduz linhas, mas esconde a responsabilidade ou aumenta acoplamento, não melhorou o código.

## Nomes e intenção

Nomes devem revelar responsabilidade, unidade, estado ou contrato. Uma função chamada `calculateTotal` ainda pode ser ambígua se não disser moeda, arredondamento, impostos ou critério de inclusão. Um nome bom reduz a necessidade de comentários que apenas traduzem sintaxe.

Evite nomes genéricos, abreviações sem contexto, booleanos ambíguos e reutilização de uma mesma variável para conceitos diferentes. O nome deve acompanhar a linguagem do domínio e mudar quando o significado mudar. Renomear é uma refatoração legítima quando reduz custo futuro.

## Funções e módulos

Uma função deve ter uma responsabilidade coerente, poucas razões para mudar e um nível de abstração relativamente uniforme. "Pequena" não significa necessariamente quatro linhas. Uma função de parsing, validação, persistência e emissão de evento pode estar errada mesmo depois de ser dividida artificialmente em wrappers com os mesmos acoplamentos.

Separe cálculo puro de efeitos colaterais quando isso tornar o comportamento testável. Faça dependências importantes aparecerem no contrato. Evite booleanos que mudam muitos modos ocultos, condicionais profundas e callbacks com regras de negócio espalhadas pelo JSX ou por handlers de infraestrutura.

## Comentários e estrutura

Comentários devem explicar uma decisão, uma restrição externa, um workaround ou um invariante que não seja inferível do código. Comentários que repetem "incrementa contador" envelhecem quando a implementação muda. Se uma explicação pode ser expressa por nome, função, tipo ou estrutura melhor, prefira a estrutura.

Formatação consistente reduz ruído, mas não substitui desenho. Um arquivo bem formatado pode ter responsabilidade demais; um arquivo com várias classes pode ter baixa coesão mesmo que o linter não reclame. Linters devem apoiar revisão, não decidir sozinhos se o domínio foi bem modelado.

## Tratamento de erros

Código limpo distingue ausência esperada, entrada inválida, falha transitória, falha de autorização, conflito e erro inesperado. Não capture uma exceção para continuar com dados incompletos sem declarar a consequência. Não retorne valores fabricados para esconder corrupção quando o consumidor precisa saber que a operação falhou.

Mensagens de erro para usuários devem ser seguras e úteis; logs para operadores precisam de contexto, causa e correlation ID sem expor segredos. O tratamento deve respeitar o contrato da camada: uma infraestrutura pode traduzir uma exceção de banco; um controller não deveria decidir uma regra de negócio apenas porque capturou qualquer erro.

## Testes e refatoração

Testes devem tornar o comportamento esperado observável. Testes de unidade ajudam a isolar regras puras; testes de integração validam contratos, banco, filas e fronteiras; testes de sistema verificam fluxos reais. Um teste que replica detalhes privados impede refatorações sem proteger o comportamento que importa.

Refatore em passos pequenos, com feedback rápido e um objetivo estrutural claro. Elimine duplicação quando as partes realmente compartilham uma razão para mudar. Abstrair duas linhas parecidas pode criar uma dependência pior que a repetição. A melhoria deve ser avaliada por coesão, acoplamento, testabilidade, legibilidade e custo de mudança, não apenas por uma métrica.

## O que Clean Code não é

Clean Code não é uma obrigação de decompor todo método em funções minúsculas, não é ausência de comentários, não é aplicar SOLID sem contexto e não é uma arquitetura específica. Também não é uma justificativa para alterar um contrato público sem migração, para esconder complexidade de domínio em classes genéricas ou para transformar cada repetição acidental em framework interno.

Uma abstração é boa quando torna uma decisão explícita e reduz mudanças acopladas. Uma abstração é ruim quando exige conhecer camadas indiretas, cria parâmetros de configuração sem significado ou torna o fluxo principal mais difícil de seguir. O código deve ser avaliado por quem precisa mantê-lo.

## Relações

- [Arquitetura Limpa](arquitetura-limpa.md) trata fronteiras e direção de dependências em uma escala maior.
- [Complexidade ciclomática](complexidade-ciclomatica.md) conta caminhos de decisão para apoiar testes e revisão.
- [Complexidade cognitiva](complexidade-cognitiva.md) estima o esforço mental necessário para entender o fluxo.
- [SOLID](solid.md) apresenta princípios de desenho orientado a objetos.
- [Análise de complexidade](analise-de-complexidade.md) trata custo assintótico de algoritmos, não legibilidade do código.

## Fontes

- [Clean Code, Robert C. Martin, catálogo Pearson](https://www.pearson.com/en-us/subject-catalog/p/clean-code-a-handbook-of-agile-software-craftsmanship/P200000009486)
- [Clean Code, material de amostra da Pearson](https://ptgmedia.pearsoncmg.com/images/9780132928472/samplepages/0132928477.pdf)
- [The Programmer's Oath, Robert C. Martin](https://blog.cleancoder.com/uncle-bob/2015/11/18/TheProgrammersOath.html)
