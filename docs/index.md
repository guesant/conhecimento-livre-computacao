# Conhecimento livre de computação

Esta é uma base aberta e livre de conhecimento. Seu objetivo é reunir, organizar e tornar consultável o máximo possível de conhecimento útil sobre Ciência da Computação, incluindo conceitos, abordagens, ferramentas, materiais e referências. O acervo reúne tutoriais, ensinamentos conceituais, guias práticos, cheatsheets para consulta rápida e fontes para estudo e aprofundamento, sem depender de uma implementação específica.

A base não é uma trilha fechada nem a documentação de um produto. Ela pode ser usada para aprender, pesquisar, comparar alternativas, implementar soluções e revisar conceitos. A organização segue uma árvore de conhecimento: primeiro domínio e categoria, depois conceito ou abordagem e, por fim, implementações concretas.

A regra central é profundidade estreita. Uma página pode ser longa, mas deve aprofundar uma unidade de conhecimento. O formato depende do objetivo: tutoriais conduzem uma aprendizagem, guias orientam uma tarefa, cheatsheets condensam comandos e relações para consulta, e referências registram fatos, interfaces e fontes primárias. Quando ferramentas ou abordagens diferentes pertencem à mesma categoria, a categoria recebe uma página-mapa e cada assunto independente recebe endereço próprio.

## Uma árvore estreita e profunda

A navegação começa por cinco macroáreas e aprofunda o assunto progressivamente. Cada nível possui no máximo cinco itens navegáveis, sem contar a página de visão geral do próprio nível. A regra reduz escolhas simultâneas sem limitar a profundidade da coleção.

### Fundamentos

[Fundamentos](educacao-pesquisa/index.md) reúne formação, estudo, padrões, governança e critérios de comparação. É a entrada para conceitos que orientam a leitura dos demais domínios.

### Sistemas

[Sistemas](sistemas/index.md) cobre hardware, sistemas operacionais, Unix, containers, virtualização, Kubernetes, nuvem, hospedagem e computação de borda. Uma implementação concreta aparece depois do conceito que ela realiza.

### Software

[Software](engenharia-software/index.md) reúne desenvolvimento, arquitetura, linguagens, web, build, artefatos, automação, infraestrutura como código, entrega e qualidade. [Engenharia de software](engenharia-software/index.md) é uma das entradas conceituais desse domínio.

### Dados e comunicação

[Dados](dados/index.md) organiza SQL, bancos, consistência, armazenamento, colaboração e mensageria. [Redes](rede/index.md) conduz pelos fundamentos de comunicação, DNS, conectividade, tráfego e serviços de rede.

### Segurança e confiabilidade

[Segurança](seguranca/index.md), [observabilidade](observabilidade/index.md), [confiabilidade](confiabilidade/resiliencia/index.md), backup e diagnóstico formam a área de proteção, operação e recuperação.

## Tipos de material

Quando um assunto possui materiais diferentes, eles são separados em cinco formatos: conceitos, tutoriais, guias, referências e cheatsheets. Um conceito explica o modelo mental; um tutorial conduz uma aprendizagem; um guia orienta uma tarefa; uma referência registra fatos e interfaces; um cheatsheet serve para consulta rápida.

Uma ferramenta não é uma categoria de primeiro nível. Keycloak aparece dentro de identidade, Tailscale dentro de conectividade privada, Cloudflare dentro de DNS ou borda e Raspberry Pi dentro de computadores de placa única. Comparações, composições, cenários e diagnósticos ficam junto do assunto que explicam.

## Como ler uma página

Páginas profundas procuram responder, quando aplicável: o que é; o que não é; como funciona; quando usar; quando não usar; exemplos; boas práticas; más práticas; falhas comuns; trade-offs; implicações de segurança e operação; alternativas; aplicações reais e fontes primárias.

Exemplos demonstram mecanismos e ajudam a relacionar a teoria com a prática. Procedimentos operacionais e decisões de arquitetura devem ser definidos pela documentação de cada ambiente que aplicar esses conhecimentos.

## Continue por aqui

Se o objetivo é compreender a infraestrutura de baixo para cima, uma ordem útil é Sistemas e Linux -> Virtualização e containers -> Redes -> Kubernetes -> Automação/IaC -> Entrega/GitOps -> Segurança -> Observabilidade -> Backup.

Essa ordem é uma trilha, não uma dependência rígida. As páginas-mapa de cada domínio permitem entrar diretamente no assunto necessário sem ler a documentação inteira em sequência.
