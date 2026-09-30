# Use Cases

Use Case descreve como um ator alcança um objetivo observável usando um sistema. O foco é a
interação e o resultado, não a tela ou a classe que implementa o comportamento. Um caso de uso
pode representar uma pessoa, outro sistema, um dispositivo ou um evento temporal como ator.

## UML e a abordagem de Alistair Cockburn

Um diagrama UML de casos de uso mostra atores, objetivos e relações entre casos. Ele é útil
para delimitar o sistema e conversar sobre escopo, mas não substitui a descrição dos fluxos.

Alistair Cockburn popularizou uma forma narrativa de escrever casos de uso, com níveis de
objetivo, atores, pré-condições, garantias, fluxo principal, extensões, variações e condições
de sucesso. A versão detalhada, frequentemente chamada de fully dressed, é apropriada quando
há risco, integração, regras e exceções suficientes para justificar o custo de especificação.

## Estrutura recomendada

| Campo | Conteúdo |
| --- | --- |
| Nome e objetivo | Resultado que o ator quer alcançar |
| Escopo | Sistema, serviço ou domínio descrito |
| Nível | Resumo, objetivo do usuário, subfunção ou detalhe interno |
| Atores | Quem inicia, participa ou recebe o resultado |
| Pré-condições | O que deve ser verdadeiro antes do início |
| Garantia mínima | O que continua verdadeiro mesmo quando o objetivo falha |
| Garantia de sucesso | Estado obtido no final bem-sucedido |
| Fluxo principal | Caminho normal, escrito em termos de intenção |
| Extensões | Exceções, alternativas, validações e recuperações |
| Regras relacionadas | Políticas do domínio aplicadas ao fluxo |
| Requisitos especiais | RNFs relevantes, como segurança ou tempo |

## Exemplo resumido

**Objetivo:** publicar uma versão aprovada.

**Atores:** mantenedor e pipeline de entrega.

**Pré-condições:** a alteração foi revisada e os testes obrigatórios passaram.

**Fluxo principal:**

1. o mantenedor solicita a publicação;
2. o sistema confirma a versão e os artefatos;
3. o pipeline promove a versão para o ambiente escolhido;
4. o sistema registra a evidência e informa o resultado.

**Extensões:**

- se o artefato não tiver assinatura válida, a publicação é recusada;
- se o ambiente estiver indisponível, a solicitação fica pendente ou falha conforme a política;
- se a verificação pós-publicação falhar, o sistema inicia rollback ou interrompe a promoção.

O exemplo não exige que a equipe escolha GitOps, uma ferramenta de CI ou uma implementação
específica. Essas são decisões posteriores, guiadas por requisitos e restrições.

## Níveis de objetivo

Um caso de uso pode ser muito amplo, como "operar uma plataforma", ou muito baixo, como
"validar um campo". Cockburn diferencia níveis para evitar misturar objetivo de negócio,
objetivo de usuário e subfunção. O nível de resumo ajuda a mapear o domínio; o nível de objetivo
do usuário costuma ser a unidade mais útil para conversar sobre valor e aceite.

Não transforme cada clique em um caso de uso. Uma sequência inteira pode representar um único
objetivo. Também não esconda regras importantes em um fluxo que só descreve a tela. O caso de
uso deve permanecer válido se a interface mudar para API, automação ou operação assistida.

## Use Case e User Story

Uma user story é uma forma curta de expressar uma necessidade, normalmente com usuário,
capacidade e valor. Um Use Case descreve contexto, fluxo e extensões com mais detalhes. Eles
podem coexistir:

- a story mantém o item pequeno e discutível no backlog;
- o Use Case organiza os fluxos e regras que atravessam várias stories;
- os critérios de aceite e os exemplos demonstram o comportamento;
- a documentação técnica registra contratos e decisões de implementação.

Não há uma conversão mecânica em que toda story vira um Use Case completo. Use o nível de detalhe
necessário para risco, complexidade, quantidade de atores e necessidade de comunicação.

## Use Case e BDD

O fluxo principal e as extensões de um Use Case podem fornecer exemplos para BDD. O BDD deve
selecionar comportamentos observáveis e não copiar todo o texto do caso de uso para um arquivo
de teste. Uma extensão importante pode virar um cenário; uma regra interna sem resultado
observável pode continuar na especificação técnica.

## Erros comuns

- escrever o caso de uso como uma sequência de cliques;
- confundir ator com cargo ou tela;
- omitir pré-condições e garantias;
- colocar toda exceção em um parágrafo sem identificar seu resultado;
- fazer o fluxo depender de nomes de classes, endpoints ou tabelas;
- criar casos de uso para cada detalhe técnico sem um objetivo de ator;
- tratar o diagrama UML como documentação suficiente.

## Fontes primárias e referências

- [OMG, UML](https://www.omg.org/spec/UML/)
- [Alistair Cockburn, Writing Effective Use Cases](https://alistair.cockburn.us/writing-effective-use-cases/)
- [ISO/IEC/IEEE 29148](https://www.iso.org/obp/ui?_escaped_fragment_=iso%3Astd%3Aiso-iec-ieee%3A29148%3Aed-2%3Av1%3Aen)
