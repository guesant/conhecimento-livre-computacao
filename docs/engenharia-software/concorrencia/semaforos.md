# Semáforos

Semáforo é um contador de sincronização. Uma operação de espera reduz o contador quando
há capacidade; uma operação de sinalização aumenta o contador e pode acordar um
participante. Um semáforo binário pode representar uma permissão, mas não é idêntico a um
mutex porque normalmente não possui o mesmo conceito de ownership.

Dijkstra descreveu as operações P e V como primitivas para bloquear e acordar processos.
Um semáforo iniciado com um permite uma entrada por vez. Um semáforo iniciado com N
representa N unidades de capacidade, como conexões, slots de worker ou buffers.

## Mutex, semáforo e evento

Um mutex protege ownership exclusivo. Um semáforo contador protege capacidade. Um evento
ou latch sinaliza que uma condição ocorreu. Escolher um semáforo para representar tudo
isso pode esconder o protocolo e facilitar liberações indevidas.

Um semáforo não transporta automaticamente o dado que motivou o sinal. Se uma thread
sinaliza antes de publicar o estado, a thread acordada pode observar uma versão incompleta.
Use as garantias de memória da API ou combine o sinal com uma estrutura protegida.

## Produtor e consumidor

Um buffer limitado pode usar dois contadores: itens disponíveis e posições livres. O
mutex protege a estrutura do buffer; os semáforos coordenam quando produtor e consumidor
podem avançar. Isso separa exclusão mútua de capacidade.

Em uma fila distribuída, prefira a semântica do próprio broker ou banco. Um semáforo em
memória de um pod não limita os consumidores de outros pods e não sobrevive ao restart.

## Riscos

- esquecer um `post` pode bloquear participantes indefinidamente;
- liberar duas vezes cria capacidade fictícia;
- usar contador sem limite permite acumular trabalho até esgotar memória;
- não definir fairness pode causar starvation;
- manter o semáforo durante I/O amplia a seção crítica;
- perder o processo dono pode deixar a capacidade presa.

Quando o processo pode morrer, use lease com expiração ou um mecanismo que detecte o
proprietário. TTL e heartbeat ajudam a detectar abandono, mas não corrigem uma operação
que continua executando depois da expiração.

## Relações

- [Mutex](mutex.md) trata exclusão mútua e ownership.
- [Condição de corrida](race-condition.md) trata interleavings incorretas.
- [Deadlock](deadlock.md) trata espera circular.
- [Edsger W. Dijkstra](../dijkstra.md) explica as contribuições de Dijkstra para
  semáforos, concorrência e raciocínio formal.

## Fontes

- [EWD 209, uma abordagem construtiva para correção de programas](https://www.cs.utexas.edu/~EWD/transcriptions/EWD02xx/EWD209.html)
- [EWD 123, processos sequenciais cooperantes](https://www.cs.utexas.edu/~EWD/transcriptions/EWD01xx/EWD123-2.html)
