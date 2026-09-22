# Cenários e padrões de solução

Páginas de conceito respondem "o que é?". Páginas de ferramenta respondem "como esta implementação funciona?". Esta área responde uma terceira pergunta: "dadas estas restrições, que desenho faz sentido e como as peças se combinam?".

Um cenário não escolhe uma tecnologia universalmente melhor. Ele torna explícitas as forças que mudam a decisão: quantidade de hosts, disponibilidade necessária, número de serviços e operadores, recursos de hardware, estado persistente, isolamento entre equipes, conectividade, compliance, automação, experiência operacional e expectativa de crescimento.

## Execução de aplicações

[Serviços em um único host](execucao/single-node.md) compara processo nativo, containers gerenciados por systemd/Quadlet, Compose e Kubernetes single-node. [Pequeno cluster](execucao/pequeno-cluster.md) trata o ponto em que múltiplos hosts, scheduling e tolerância a falhas mudam o problema.

## Plataforma

[Quando Kubernetes faz sentido](execucao/quando-kubernetes.md) separa "consigo executar em Kubernetes" de "ganho algo suficiente para pagar o custo da plataforma".

## Como usar estes guias

Comece pelo cenário, identifique as premissas que coincidem com o ambiente e siga os links para conceitos e implementações. Se uma premissa mudar, reavalie a decisão; não transforme uma escolha contextual em padrão universal.
