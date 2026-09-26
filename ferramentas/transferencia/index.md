# Transferência

Esta área separa os problemas de transferência de dados dos modos de acesso a
arquivos remotos. O protocolo escolhido depende do fluxo, do modelo de
confiança e de a operação ser uma cópia pontual, uma sincronização ou uma
montagem contínua.

## Categorias

- [Transferência de arquivos](transferencia/index.md) reúne protocolos e
  ferramentas que copiam ou sincronizam dados.
- [Acesso a arquivos remotos](acesso/index.md) reúne montagens e operações que
  fazem um filesystem remoto parecer acessível localmente.

A escolha deve começar pelo comportamento desejado, não pelo protocolo
disponível.
