# Supply chain e SBOM

A cadeia de suprimentos de software (supply chain) é a soma de tudo que entra na composição final de um sistema sem ter sido escrito por quem o publica: bibliotecas de terceiros, suas próprias dependências transitivas, a imagem base de um container, as ferramentas usadas para compilar e empacotar. Um ataque de supply chain compromete um desses elos, em vez de atacar o software final diretamente, porque um único elo comprometido se propaga automaticamente para todo projeto que depende dele, muitas vezes sem que ninguém perceba a origem real do problema.

O caso mais citado dessa categoria é o Log4Shell, uma vulnerabilidade crítica descoberta em 2021 numa biblioteca de log (Log4j) extremamente popular no ecossistema Java. A gravidade não estava só na vulnerabilidade em si, estava em quantos sistemas diferentes, de organizações completamente sem relação entre si, dependiam dessa mesma biblioteca sem sequer saber que a usavam diretamente, muitas vezes por causa de uma dependência transitiva de outra dependência. Esse incidente tornou concreto um risco que antes era mais teórico: não basta confiar no próprio código, é preciso ter visibilidade sobre tudo que ele arrasta consigo.

## SBOM

Um SBOM (Software Bill of Materials, ou lista de materiais de software) é justamente essa visibilidade tornada explícita: um documento estruturado listando cada componente que compõe um software, com sua versão exata. A analogia com uma lista de ingredientes de um produto alimentício é direta: sem ela, não há como saber se um ingrediente específico, mais tarde descoberto como problemático, está presente ou não, sem reabrir a receita inteira. Com um SBOM em mãos, quando uma vulnerabilidade nova é descoberta numa biblioteca específica, basta consultar quais sistemas listam essa biblioteca no seu SBOM para saber quem está exposto, em vez de reexaminar cada sistema do zero.

Os dois formatos mais usados para representar um SBOM são o SPDX, originado na comunidade de licenciamento de software livre e depois adotado também para esse uso, e o CycloneDX, criado especificamente com foco em segurança de supply chain. Um formato relacionado, o VEX (Vulnerability Exploitability eXchange), complementa o SBOM respondendo a uma pergunta que ele sozinho não responde: dado que o componente X está presente, e uma vulnerabilidade foi anunciada nele, ela é de fato explorável neste uso específico, ou o código vulnerável nem chega a ser executado no caminho real da aplicação?

## Continue por aqui

[Scanning de vulnerabilidade](vulnerability-scanning.md) detalha a categoria de scanner (SCA) que examina justamente essas dependências de terceiros. [A pipeline de CI](../arquitetura/ci.md), na arquitetura, mostra o OSV-Scanner rodando sobre este repositório, consultando exatamente esse tipo de base de vulnerabilidade conhecida, e o Trivy gerando um SBOM real em formato CycloneDX para cada imagem que o cluster roda, publicado como artefato de cada execução.
