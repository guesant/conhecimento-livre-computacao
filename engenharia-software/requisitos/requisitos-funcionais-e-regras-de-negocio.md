# Requisitos funcionais e regras de negócio

Requisito funcional descreve um comportamento, uma capacidade ou um resultado que o sistema
deve fornecer. Em português, algumas equipes usam RF para requisito funcional e RN para
requisito de negócio ou requisito funcional. Como as siglas variam, o documento deve definir
seu vocabulário. Nesta documentação, RN pode significar requisito funcional quando o contexto
deixar isso explícito, mas regra de negócio permanece uma categoria separada.

## Requisito funcional

Um requisito funcional deve deixar claro quem inicia a operação, sobre qual recurso, sob quais
condições, com quais entradas, regras, saídas e erros. Ele pode descrever uma ação de usuário,
uma integração, um processamento assíncrono, uma política de autorização ou uma reação a um
evento externo.

| Elemento | Pergunta |
| --- | --- |
| Ator ou sistema | Quem solicita ou dispara o comportamento? |
| Pré-condição | O que precisa ser verdadeiro antes da operação? |
| Entrada | Quais dados, comandos ou eventos são aceitos? |
| Regra | Qual transformação, decisão ou validação ocorre? |
| Saída | O que o usuário ou sistema externo observa? |
| Erro | Como são comunicados ausência, conflito, rejeição e indisponibilidade? |
| Pós-condição | O que passa a ser verdadeiro quando a operação termina? |
| Efeitos laterais | Que auditoria, evento, notificação ou alteração é produzida? |

## Regra de negócio

Regra de negócio é uma política, cálculo, restrição ou decisão do domínio. Ela pode ser
aplicada por uma tela, uma API, um job ou uma operação manual, portanto não deve ficar presa
à interface que primeiro a revelou. Exemplos são limite de crédito, elegibilidade, retenção,
ordenação, transição de estado e necessidade de aprovação.

Uma regra pode alimentar vários requisitos funcionais. Se a regra muda, todos os fluxos que a
usam precisam ser identificados. Quando a política precisa de uma exceção, registre a condição
explicitamente em vez de espalhar um `if` diferente em cada consumidor.

## Acceptance criteria

Critérios de aceite são condições observáveis usadas para decidir se o requisito foi atendido.
Eles não precisam repetir o requisito inteiro. Devem esclarecer exemplos importantes, fronteiras,
erros e estados que a descrição curta deixou abertos.

Um bom critério evita implementação específica. "Ao confirmar um pagamento válido, o cliente
recebe a confirmação e o pedido fica disponível para acompanhamento" descreve resultado. "O
controller chama a classe X" descreve implementação e deve ficar em uma especificação técnica,
caso seja necessário.

## Exemplo

Requisito:

> Um usuário autenticado pode solicitar a exportação dos próprios dados. A aplicação deve
> aceitar uma solicitação por vez, informar que o processamento é assíncrono e disponibilizar
> um resultado somente ao próprio usuário.

Critérios de aceite:

- uma solicitação válida retorna confirmação de recebimento;
- uma segunda solicitação enquanto a primeira está em processamento recebe uma resposta de
  conflito ou é consolidada conforme a regra definida;
- o arquivo concluído não pode ser acessado por outro usuário;
- falhas são registradas sem expor dados pessoais na mensagem ao usuário;
- o resultado tem expiração e a política de retenção está definida.

## Anti-patterns

Evite transformar cada campo de uma tela em um requisito isolado sem explicar o objetivo.
Evite escrever apenas o caminho feliz. Evite esconder regra de autorização em critérios visuais.
Evite usar "e assim por diante" para omitir estados que alteram risco ou custo. Evite chamar
qualquer item de backlog de requisito sem indicar se ele é necessidade, solução, tarefa ou
hipótese.

## Relações

- [Engenharia de requisitos](engenharia-de-requisitos.md) trata elicitação, validação e mudança.
- [Requisitos não funcionais](requisitos-nao-funcionais.md) trata propriedades do sistema.
- [Use Cases](use-cases.md) detalha fluxos e extensões.
- [BDD e Gherkin](bdd-e-gherkin.md) transforma exemplos de comportamento em especificações.
