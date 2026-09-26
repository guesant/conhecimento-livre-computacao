# Comparativo de soluções de autorização

Casbin, Casdoor, Cedar, CASL e OpenFGA aparecem frequentemente na mesma pesquisa porque todos podem participar de uma arquitetura de controle de acesso. Eles não são substitutos diretos. A primeira decisão é identificar se o problema é autenticar pessoas, avaliar políticas locais, compartilhar regras entre camadas ou consultar relações persistentes.

## Posição de cada solução

| Solução | Categoria | Modelo principal | Execução | Identidade própria |
| --- | --- | --- | --- | --- |
| Casbin | Biblioteca | RBAC, ABAC, ACL, ReBAC modelado | Embutida | Não |
| Casdoor | Plataforma IAM e SSO | Usuários, organizações, papéis e permissões | Serviço | Sim |
| Cedar | Linguagem e engine | Policy, RBAC e ABAC | Embutida ou serviço que a hospede | Não |
| CASL | Biblioteca JS/TS | Abilities, condições e campos | Embutida | Não |
| OpenFGA | Serviço de autorização | ReBAC com modelos e tuplas | Serviço | Não |

## Como escolher

Escolha Casbin quando a aplicação precisa de uma biblioteca de enforcement com um modelo configurável e a equipe aceita manter storage, sincronização e administração por conta própria. Ele é uma boa opção para uma API que já tem usuários e papéis e precisa de decisão local.

Escolha Casdoor quando o problema inclui login, SSO, federação, organizações, administração de usuários e emissão de tokens. Ele pode participar da autorização, mas a aplicação deve continuar protegendo recursos e tenants com suas próprias regras.

Escolha Cedar quando políticas declarativas, schema, validação e separação entre regra e código são prioridades. Ele é adequado para um PDP embutido ou para uma plataforma que hospede políticas Cedar.

Escolha CASL quando o centro da necessidade é representar abilities no backend e no frontend JavaScript ou TypeScript. Ele é particularmente útil para adaptar a interface e para compartilhar uma linguagem de capabilities entre camadas, sem pretender ser um IdP ou um serviço central de relações.

Escolha OpenFGA quando a pergunta dominante é relacional: quem pode acessar este documento por ser membro desta organização, colaborador deste projeto ou herdeiro desta pasta? Ele vale o custo de um serviço adicional quando o grafo é grande ou compartilhado por vários serviços.

## Combinações possíveis

Uma composição comum é Casdoor como IdP, uma API como PEP e OpenFGA como PDP de relações. A API valida o token emitido pelo IdP, traduz o subject para o identificador interno e consulta OpenFGA antes da operação.

Outra composição é um IdP existente, Casbin no backend e CASL no frontend. O backend mantém a decisão autoritativa; CASL recebe uma projeção segura para esconder ações e melhorar a experiência.

Cedar pode ocupar o lugar do motor local em uma API que precisa de políticas auditáveis. Casbin pode continuar sendo usado em outro serviço com um modelo diferente, mas duplicar a mesma regra em linguagens e engines exige testes de equivalência.

## Dimensões que não podem ser ignoradas

### Latência

Bibliotecas locais eliminam uma chamada de rede, mas podem depender de dados que a aplicação ainda precisa buscar. Serviços como OpenFGA centralizam decisões, mas exigem conexão, timeout e observabilidade. O cache pode reduzir custo e atrasar revogação.

### Consistência

Alteração de uma policy local, publicação de um modelo Cedar e escrita de uma tupla OpenFGA têm mecanismos diferentes de propagação. Uma operação financeira ou administrativa não deve usar o mesmo nível de consistência de uma página de navegação.

### Filtragem de dados

Autorizar uma linha não é o mesmo que construir uma lista autorizada. Se a aplicação precisa filtrar milhares de recursos, deve avaliar suporte a consultas, `ListObjects`, tradução para banco ou uma projeção própria. Um loop de checks por item pode virar o gargalo e ainda produzir resultados incompletos sob concorrência.

### Administração

Casbin, Cedar e CASL não fornecem necessariamente um painel para usuários e papéis. OpenFGA administra modelos e tuplas, mas não autentica pessoas. Casdoor cobre administração de identidade, mas adicioná-lo apenas para resolver um `can edit` simples cria uma dependência desnecessária.

### Auditoria

Registre a decisão, o principal normalizado, a ação, o recurso, a versão do modelo e um correlation ID, respeitando minimização de dados. Não registre tokens ou atributos sensíveis sem necessidade. Uma auditoria útil precisa permitir reconstruir por que uma decisão foi tomada, não apenas mostrar que uma rota foi chamada.

## Erros de arquitetura

Não trate grupo do OIDC como autorização completa sem definir escopo e revogação. Não proteja apenas o botão no frontend. Não permita que um cliente escolha livremente o `tenant` enviado à API. Não misture identidade, política e dados de recurso em um único token sem limites de tamanho e ciclo de vida.

Também não escolha OpenFGA, Cedar ou Casbin apenas por popularidade. O modelo de negócio deve vir primeiro. Uma regra de propriedade local pode ser mais segura e simples em uma query de domínio; uma rede de compartilhamento entre organizações pode justificar um grafo dedicado.

## Fontes

- [Apache Casbin](https://casbin.apache.org/docs/overview/)
- [Casdoor](https://casdoor.ai/docs/overview/)
- [Cedar Policy Language](https://docs.cedarpolicy.com/)
- [CASL](https://casl.js.org/)
- [OpenFGA](https://openfga.dev/docs)
