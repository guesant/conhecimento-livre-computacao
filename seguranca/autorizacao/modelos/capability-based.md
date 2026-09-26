# Capability-Based Access Control

Capability-Based Access Control usa um artefato que combina referência a um recurso e autoridade para executar determinadas operações. Quem possui uma capability pode apresentá-la ao sistema, sujeito às regras de validade e de delegação.

## Capability e identidade

Uma capability não é apenas um identificador público. Ela deve ser difícil de forjar ou deve ser um handle que o sistema não permite fabricar arbitrariamente. O artefato pode carregar direitos, apontar para uma entrada protegida ou representar um objeto em uma arquitetura de capabilities.

Isso muda a pergunta de "qual permissão este usuário possui?" para "como este processo obteve esta autoridade e quais direitos ela contém?" A capability pode ser delegada sem que o receptor tenha acesso a todas as permissões do emissor.

## Formas comuns

Tokens de acesso com escopo, signed URLs e handles de recursos têm características de capability, embora não sejam necessariamente capabilities puras. Uma URL assinada para baixar um objeto concede uma operação limitada por tempo, recurso e método. Um token bearer é mais fraco quando pode ser copiado e usado por qualquer pessoa que o obtenha.

Modelos de capability em sistemas operacionais podem usar referências não forjáveis dentro do kernel. Aplicações web normalmente usam tokens assinados, identificadores opacos ou delegação controlada, com riscos adicionais de vazamento, replay e revogação.

## Direitos e delegação

Uma capability deve conter ou referenciar um conjunto mínimo de direitos. Delegar significa criar uma capability derivada com direitos iguais ou menores, nunca elevar autoridade. A derivação deve preservar escopo, tenant, recurso, operação e expiração.

Em uma arquitetura de objeto, o receptor que possui a referência consegue invocar somente as operações expostas por ela. Em uma API, a mesma ideia exige que o servidor valide a capability em cada operação e não aceite um ID de recurso separado que amplie o alcance do token.

## Vantagens

Capabilities tornam a delegação explícita, podem reduzir consultas a listas de permissões e permitem autoridade limitada por recurso, operação e expiração. Elas combinam bem com links temporários, workers e serviços que precisam acessar somente um objeto específico.

## Revogação e vazamento

O principal custo é revogar uma capability já emitida. O sistema pode usar TTL curto, denylist, versão do recurso, estado online ou um serviço intermediário. Se o token for bearer, quem o copia recebe a mesma autoridade até sua expiração ou revogação.

Não coloque dados sensíveis desnecessários no artefato. Valide audiência, issuer, assinatura, expiração, método, recurso, tenant e nonce quando replay for uma ameaça. Uma capability para leitura não deve ser aceita em uma operação de escrita.

## Bearer e proof of possession

Uma capability bearer pode ser usada por qualquer pessoa que a possua. Tokens vinculados a uma chave ou a uma sessão reduzem replay, mas exigem que o cliente prove posse em cada uso. URL assinada precisa limitar método, caminho, query relevante, tamanho e duração, além de não aparecer em logs ou referers.

## Comparação

RBAC concede direitos indiretamente por papéis. ReBAC deriva direitos de relações. Capability-based access control entrega a autoridade como um artefato ou referência. Um sistema pode combinar os modelos: RBAC decide quem pode emitir uma capability e a capability limita o worker ao recurso necessário.

## Casos adequados

Use esta abordagem para uploads e downloads temporários, delegação entre serviços, tarefas assíncronas de escopo reduzido e sistemas que conseguem proteger handles. Evite usar um token bearer de longa duração como substituto genérico de autorização por recurso.

## Fontes

- [NIST, access control models](https://csrc.nist.gov/pubs/sp/800/192/final)
- [OAuth 2.0 bearer token usage](https://www.rfc-editor.org/rfc/rfc6750)
- [Capability Myths Demolished, Mark S. Miller](https://srl.cs.jhu.edu/pubs/SRL2003-02.pdf)
