# just: executor de tarefas

Um projeto acumula, com o tempo, uma lista de comandos que quem trabalha nele precisa lembrar: como rodar os testes, como formatar o código, como aplicar as migrações. Guardar isso só num README funciona até o README ficar desatualizado ou até alguém digitar o comando errado por memória; `just` resolve isso lendo um `justfile` na raiz do projeto e expondo cada bloco nomeado ali como um comando de primeira classe (`just <nome>`), descobrível de uma vez com `just --list`, em vez de espalhado em prosa. A comparação inevitável é com o `Makefile` do Make, que já cumpre um papel parecido há décadas, mas carrega duas armadilhas sintáticas conhecidas, indentação obrigatória por tab (um espaço no lugar errado quebra a receita de um jeito difícil de enxergar no editor) e a necessidade de declarar manualmente `.PHONY` para toda receita que não produz um arquivo de saída, sem o que o Make pode decidir, silenciosamente, que a receita já está satisfeita e pular a execução. `just` existe especificamente para reter o valor do padrão (comandos nomeados, documentados, com dependência entre si) sem herdar esse histórico de erro sintático.

Um `justfile` declara receitas e, quando necessário, dependência entre elas:

```just
default:
    @just --list

build:
    npm run build

test: build
    npm test
```

A receita chamada `default`, sem argumento, é a que roda quando alguém invoca `just` sem especificar nome nenhum, um bom lugar para listar as receitas disponíveis em vez de rodar algo por acidente. `test: build` declara que `test` depende de `build`: rodar `just test` executa `build` primeiro automaticamente, sem que quem chama precise lembrar da ordem correta.

O limite claro de `just` é o que ele deliberadamente não tenta ser: um executor de comandos locais ao host onde é invocado, sem inventário de máquinas remotas, sem transporte SSH embutido, e sem o conceito de convergir um sistema para um estado declarado se ele já não estiver lá, o papel que cabe a uma ferramenta de gestão de configuração como o [Ansible](ansible.md). Um `justfile` que chama `ansible-playbook` dentro de uma receita não é incomum, e não é uma contradição: `just` continua sendo a camada de conveniência e documentação de comandos, o Ansible continua sendo quem de fato aplica um estado a uma máquina remota.

## Continue por aqui

[Ansible](ansible.md) cobre a ferramenta que resolve o problema que `just` deliberadamente não resolve, convergência de estado numa máquina remota. [Shells e scripts](shells-e-scripts.md) cobre as armadilhas de portabilidade que um script chamado a partir de uma receita `just` ainda precisa respeitar.
