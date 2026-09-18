# Fundações do software livre e aberto

Um projeto de código aberto sem estrutura jurídica nenhuma por trás enfrenta problemas que a licença sozinha não resolve: quem é dono legal do código quando não existe uma empresa formal, quem pode receber doações em nome do projeto, quem tem legitimidade para processar alguém que viola a licença. Um conjunto de fundações existe especificamente para preencher essa lacuna, cada uma com um modelo ligeiramente diferente de como se relaciona com os projetos que abriga.

## OSI: quem decide o que conta como "código aberto"

A Open Source Initiative (OSI) mantém a Open Source Definition, um conjunto de critérios que uma licença precisa satisfazer para ser chamada legitimamente de "código aberto" (permitir redistribuição livre, exigir disponibilização do código-fonte, permitir modificação e trabalho derivado, entre outros critérios), e opera um processo de revisão que aprova formalmente licenças específicas contra esses critérios. Isso resolve um problema real de ambiguidade: sem uma definição com processo de aprovação por trás, qualquer produto poderia se autodenominar "open source" sem satisfazer nenhum critério real, um problema conhecido como "open-washing". Uma licença aprovada pela OSI (MIT, Apache 2.0, GPL, BSD, entre dezenas de outras) carrega a garantia de que passou por esse escrutínio; uma licença "open source" que a OSI nunca aprovou merece leitura cuidadosa antes de confiar no rótulo.

## Apache Software Foundation: governança de projeto, não só código

A Apache Software Foundation (ASF) não é dona de um único produto, é uma guarda-chuva legal e de governança para dezenas de projetos independentes (o servidor HTTP Apache é só o mais antigo e o que dá nome à fundação), cada um seguindo o mesmo modelo de tomada de decisão baseado em consenso de committers, sem uma empresa única controlando a direção do projeto. Esse modelo resolve um problema de risco de continuidade: um projeto cuja governança depende inteiramente de uma pessoa ou empresa específica corre risco real de abandono se essa pessoa ou empresa perder interesse; um projeto sob a governança formal da ASF tem um processo de sucessão de liderança já estabelecido, independente de qualquer indivíduo específico continuar envolvido.

## Software Freedom Conservancy: um lar fiscal e jurídico para quem não quer fundar uma fundação

A Software Freedom Conservancy oferece um serviço mais específico: fiscal sponsorship, permitindo que um projeto de código aberto receba doações, assine contratos e tenha presença legal sem precisar constituir sua própria entidade jurídica separada, um processo caro e burocrático para um projeto pequeno mantido por poucas pessoas. A Conservancy também historicamente se envolveu em ações de enforcement de licença copyleft, processando ou negociando com empresas que distribuíam software sob GPL sem cumprir a obrigação de disponibilizar o código-fonte correspondente, um trabalho que a maioria dos mantenedores individuais de projeto não teria recurso jurídico nem tempo para conduzir sozinho.

## Creative Commons: licenciamento fora do software

Creative Commons resolve um problema adjacente, mas fora do escopo de licença de software: como licenciar conteúdo (texto, imagem, música, dados) de forma aberta, com um conjunto de licenças modulares que permitem ao autor escolher exigências específicas, exigir atribuição, proibir uso comercial, exigir que derivados sejam compartilhados sob a mesma licença, ou qualquer combinação dessas condições. A confusão mais comum é tratar uma licença Creative Commons como se fosse uma licença de software: as duas famílias resolvem categorias de obra diferentes, e aplicar uma licença de software a um texto ou a uma imagem, ou vice-versa, produz ambiguidade jurídica sobre o que exatamente está sendo permitido.

## Internet Archive: preservação como missão declarada

O Internet Archive é uma biblioteca digital sem fins lucrativos cuja missão declarada é "acesso universal a todo conhecimento", mantendo o Wayback Machine (um arquivo histórico de versões passadas de páginas web, útil quando uma fonte citada num documento técnico muda de conteúdo ou deixa de existir) além de acervos de livros, software antigo e mídia. Sua relevância para qualquer documentação técnica que cita fontes externas é direta: uma referência a uma página específica pode ser verificada contra uma versão arquivada dela num momento passado, uma forma de mitigar o problema de um link que, com o tempo, aponta para um conteúdo diferente do que existia quando foi citado originalmente.

## Continue por aqui

[Unix: famílias e padrões](unix-familias-e-padroes.md) cobre a diferença entre uma licença permissiva (BSD) e uma copyleft (GPL), a distinção jurídica de fundo que a OSI formaliza através de um processo de aprovação. [Padrões e governança da internet](padroes-e-governanca-da-internet.md) cobre as organizações equivalentes no lado de padrão técnico de protocolo, em vez de licenciamento de código.
