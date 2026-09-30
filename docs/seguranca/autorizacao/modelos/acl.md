# Access Control List

Uma Access Control List, ACL, associa um objeto a entradas que informam quais sujeitos ou grupos podem executar determinadas ações. A entrada costuma conter um identificador, direitos como leitura ou escrita e, em alguns sistemas, um efeito de permitir ou negar.

## Modelo

O objeto é o centro da decisão. Uma lista conceitual pode ser:

```text
document:42
  user:alice: read, write
  group:reviewers: read
  user:bob: deny
```

O resultado depende da ordem ou da combinação das entradas. Sistemas diferentes usam deny explícito, primeira correspondência, última correspondência ou combinação de permissões. Essa semântica precisa ser conhecida antes de migrar ACLs.

ACL não é o mesmo que DAC, embora muitas ACLs sejam mecanismos de um sistema discricionário. A ACL descreve onde a permissão está registrada; DAC descreve quem pode alterar ou delegar essa permissão.

## Vantagens

ACL é fácil de entender quando há poucos sujeitos por objeto e quando a pergunta principal é "quem acessa este recurso?". Ela acompanha naturalmente arquivos, buckets, documentos e objetos de armazenamento. Também torna possível revisar uma permissão específica sem reconstruir toda a matriz de usuários e recursos.

## Limitações

Uma ACL por objeto pode gerar muitas entradas, duplicação e operações caras para listar tudo o que um usuário pode acessar. Remover um usuário exige procurar em muitas listas. Alterar o nome ou a identidade do sujeito pode exigir migração de referências.

ACLs também costumam representar mal hierarquia e contexto. Se cada combinação de grupo, tenant, ação e condição vira uma entrada, o conjunto perde legibilidade e pode conter conflitos.

## Herança e precedência

Diretórios, buckets e documentos podem herdar ACLs de um pai. A aplicação precisa definir se uma entrada filha substitui, restringe ou apenas complementa a entrada herdada. Uma regra `deny` também precisa ter escopo claro: negar em um nível deve bloquear todos os descendentes ou somente o objeto atual?

Não use a ordem de linhas como precedência acidental. Armazene o efeito e a prioridade explicitamente ou valide que as entradas são mutuamente consistentes.

## Revogação e migração

Revogar um usuário em ACLs distribuídas exige localizar entradas diretas, grupos, links assinados, caches e cópias. Use identificadores imutáveis em vez de nomes exibidos. Ao migrar dados, preserve o efeito original e teste objetos sem ACL, objetos com herança e objetos com conflito.

## Operação segura

Defina uma regra determinística para conflito entre allow e deny. Valide se o sujeito pertence ao tenant do objeto antes de avaliar a ACL. Evite aceitar identificadores fornecidos diretamente pelo cliente sem resolver a identidade no servidor.

Para listagens, não busque todas as linhas e filtre no frontend. A consulta deve aplicar a ACL no banco ou usar um índice autorizado. Para grandes grafos de compartilhamento, considere ReBAC e um serviço como OpenFGA.

## Quando usar

ACL é uma escolha razoável para compartilhamento direto de arquivos, permissões de objetos em storage e sistemas em que o conjunto de sujeitos por recurso é pequeno. Em aplicações com papéis estáveis, RBAC costuma reduzir a repetição. Em aplicações com regras condicionais, ABAC ou PBAC pode ser mais expressivo.

## Fontes

- [NIST, discretionary access control](https://csrc.nist.gov/glossary/term/discretionary_access_control)
- [NIST, access control models](https://csrc.nist.gov/pubs/sp/800/192/final)
