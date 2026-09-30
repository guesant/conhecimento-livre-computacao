# QuickJS

QuickJS é uma engine JavaScript pequena e embutível, desenvolvida por Fabrice
Bellard. Ela é adequada para ferramentas, automação e aplicações que precisam
incorporar uma linguagem de script sem carregar um runtime de servidor inteiro.

## Embedding

A aplicação hospedeira cria um runtime e contextos, carrega código, registra
funções nativas e controla o acesso a recursos. Filesystem, rede, relógio,
processos e módulos não são concedidos pela linguagem sozinha. O embedder deve
definir uma API mínima e validar argumentos.

Isso permite usar QuickJS como uma camada de extensão, mas também cria uma
fronteira de segurança que o projeto precisa construir. Limitar tempo de CPU,
memória, profundidade de chamadas e acesso a objetos nativos é responsabilidade
do hospedeiro. Avaliar código não confiável exige sandbox real; uma engine
embutida isolada apenas por convenção não é sandbox suficiente.

## Memória e ciclo de vida

QuickJS usa contagem de referências e coleta de ciclos. O embedder ainda
precisa destruir runtimes, contextos e valores na ordem correta e tratar
exceções retornadas pela API C. Um script pode manter objetos vivos por meio de
closures e referências globais.

## Escolha

QuickJS é interessante quando tamanho, inicialização e controle do host são
mais importantes que o ecossistema de APIs de Node. Node, Bun e engines de
navegador são alternativas melhores quando a aplicação precisa de grande
compatibilidade com pacotes e APIs web.

## Fonte primária

- [QuickJS JavaScript Engine](https://bellard.org/quickjs/)
- [QuickJS source code](https://github.com/bellard/quickjs)
