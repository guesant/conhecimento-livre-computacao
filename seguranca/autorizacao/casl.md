# CASL

CASL é uma biblioteca isomórfica de autorização para JavaScript e TypeScript. Ela representa as capacidades de um usuário por meio de uma `Ability`, com operações como `can` e `cannot`, condições sobre recursos e, quando necessário, restrição a campos específicos.

O objetivo de CASL é permitir que uma aplicação expresse e consulte abilities no backend e no frontend. Ele é útil para adaptar a interface ao que o usuário pode fazer, mas a decisão de segurança precisa ser aplicada novamente no servidor.

## Modelo de ability

Uma ability descreve ações, subjects e condições. Um exemplo conceitual seria permitir que uma pessoa leia artigos publicados e edite apenas os artigos cujo `authorId` coincide com seu identificador.

```ts
can("read", "Article", { published: true });
can("update", "Article", { authorId: user.id });
cannot("delete", "Article");
```

A definição exata depende do builder e da versão do pacote. O ponto importante é que a regra precisa usar um tipo de subject estável e dados que o backend também valide. Um nome de subject inferido de maneira diferente entre frontend e backend pode causar divergência.

## Condições e campos

Condições permitem expressar filtros por atributos. Restrições de campo permitem dizer que uma ação pode atingir alguns campos, mas não outros. Isso pode ser útil para telas administrativas, mas não deve ser confundido com filtragem segura de payload. O backend deve aplicar um DTO permitido, validar campos e rejeitar alterações que a ability não autoriza.

Em listagens, integrações como `accessibleBy` podem traduzir regras para consultas de banco quando o adapter oferece esse suporte. A tradução deve ser testada: uma ability usada somente no navegador não protege a consulta, e uma regra que não pode ser convertida para o banco pode exigir pós-filtragem ou um modelo diferente.

## Frontend e backend

No frontend, CASL pode esconder ações, desabilitar controles e explicar por que uma operação não está disponível. Isso reduz chamadas rejeitadas e melhora a experiência. O frontend não é uma fronteira de confiança. Um usuário pode alterar JavaScript, chamar a API diretamente ou fabricar um payload.

No backend, CASL pode ser usado como biblioteca de decisão, principalmente em APIs Node.js e serviços TypeScript. Mesmo assim, a aplicação precisa validar o token OIDC ou a sessão, carregar o recurso atual e executar a ability com dados confiáveis.

Não serialize uma ability arbitrária enviada pelo cliente. O conjunto de regras deve vir de uma fonte autenticada ou ser criado pelo servidor a partir de papéis e atributos confiáveis.

## Compartilhamento de regras

Uma vantagem de CASL é compartilhar conceitos entre camadas do ecossistema JavaScript. Isso não significa que o mesmo objeto deva ser copiado sem adaptação. O backend pode conhecer regras de persistência, tenant e estado que não existem na tela; o frontend pode trabalhar com uma representação parcial para apresentação.

Se a autorização atravessa várias linguagens e serviços, uma biblioteca local pode gerar cópias divergentes. Nesse cenário, uma linguagem ou serviço central, como Cedar ou OpenFGA, pode fornecer um contrato comum, enquanto CASL fica responsável pela projeção adequada à interface.

## Persistência e revogação

CASL não é um servidor de políticas nem um banco de identidade. A aplicação decide onde papéis, relações e atributos vivem. Se as regras mudam em produção, é necessário invalidar abilities já criadas, atualizar sessões ou garantir que a decisão seja construída a cada operação sensível.

Cache de ability pode ser útil para uma tela, mas não deve sobreviver à revogação além do limite aceito. Uma mudança de papel precisa alcançar operações de escrita, não apenas remover botões da interface.

## Casos adequados

CASL é adequado para:

- frontend React, Vue ou outro cliente JavaScript;
- backend Node.js e TypeScript;
- regras de UI que dependem de ação, subject e condições;
- aplicações pequenas e médias onde o modelo cabe em uma biblioteca;
- compartilhar uma representação de capabilities entre servidor e cliente.

Ele é menos adequado como única solução quando há muitos serviços não JavaScript, relações profundas, necessidade de auditoria centralizada ou consultas autorizadas em grande escala.

## Relação com as outras soluções

CASL não autentica, não é IdP e não é um substituto do Casdoor. Ele se aproxima de Casbin por ser uma biblioteca local, mas tem foco forte no ecossistema JavaScript e na representação de abilities. Cedar separa a linguagem de policy da aplicação. OpenFGA mantém relações persistentes e responde consultas de autorização baseadas em tuplas.

## Fontes

- [CASL](https://casl.js.org/)
- [CASL, repository](https://github.com/stalniy/casl)
- [CASL, guide](https://casl.js.org/v6/en/guide/intro)
- [CASL, Prisma integration](https://casl.js.org/v6/en/cookbook/advanced/authorize-with-prisma)
