# Cache

Cache é uma cópia derivada mantida para reduzir latência, custo ou carga sobre a fonte
de verdade. O cache pode conter uma resposta HTTP, um objeto serializado, uma consulta,
um fragmento de página ou um resultado de computação.

O cache não deve ser tratado como a autoridade editorial ou transacional sem uma decisão
explícita. Ele pode estar vazio, expirado, inconsistente ou indisponível. A aplicação
precisa saber como consultar a origem, quando aceitar dados stale e como invalidar uma
entrada.

## Cache key e valor

A chave precisa incluir tudo que altera o resultado: recurso, parâmetros relevantes,
locale, identidade de cache, versão do schema e, quando necessário, tenant ou permissões.
Uma chave incompleta pode devolver dados de outro idioma, usuário ou autorização.

O valor deve possuir um formato versionado. Alterar a estrutura sem alterar a chave pode
fazer uma versão nova tentar desserializar um valor antigo. TTL, versão ou namespace de
cache permitem descartar dados incompatíveis.

## Cache-aside

No padrão cache-aside, a aplicação consulta o cache primeiro. Em um miss, consulta a
origem, retorna o resultado e grava a cópia. O caminho de escrita atualiza a origem e
remove ou versiona a entrada correspondente.

É um padrão simples e explícito, mas possui uma janela entre a escrita e a invalidação.
Se duas requisições observarem um miss ao mesmo tempo, ambas podem consultar a origem.
Um lock curto, coalescing de promise ou mecanismo de single flight pode reduzir stampede,
sem transformar o lock em requisito para o caminho inteiro.

## Outros padrões

No read-through, o componente de cache consulta a origem no miss. No write-through, uma
escrita passa pelo cache e pela origem antes de confirmar. No write-behind, o cache
confirma antes de persistir na origem, o que reduz latência, mas aumenta risco de perda e
complexidade de recuperação.

Use write-behind somente quando a aplicação puder tolerar atraso, reordenação e perda
temporária. Para dados editoriais ou transacionais, a fonte de verdade normalmente deve
ser confirmada antes de o cache ser atualizado.

## TTL e invalidação

TTL limita a idade máxima, mas não garante que o dado ficará disponível até o fim do
período. Invalidação por evento remove ou versiona a chave imediatamente depois de uma
alteração confirmada.

Versionar a chave permite publicar uma nova geração sem apagar a anterior imediatamente.
Um processo pode servir a geração anterior durante a preparação e trocar a referência
quando a nova estiver pronta. A limpeza de gerações antigas deve ter limite de memória e
retenção.

## Stale-while-revalidate

Stale-while-revalidate serve uma entrada vencida dentro de uma janela aceitável e agenda
uma atualização em background. Isso reduz latência percebida e evita que a indisponibilidade
temporária da origem transforme toda leitura em erro.

O sistema precisa distinguir três estados: fresco, stale aceitável e ausente. Se não há
valor stale, o caminho pode consultar a origem ou retornar loading, fallback ou erro
conforme a criticidade. Não transforme um cache miss em falha obrigatória quando a origem
continua disponível.

## Stampede, avalanche e penetração

Cache stampede ocorre quando muitas requisições renovam a mesma chave simultaneamente.
Single flight, jitter no TTL, prewarming e stale-while-revalidate reduzem o pico.

Cache avalanche ocorre quando muitas chaves expiram juntas ou uma camada inteira é perdida.
TTL com variação, limitação da origem e aquecimento progressivo ajudam a reduzir o impacto.

Cache penetration ocorre quando consultas repetidas por dados inexistentes sempre chegam à
origem. Negative caching com TTL curto pode ajudar, desde que a criação de um recurso não
fique invisível além da janela aceitável.

## Consistência e segurança

Uma leitura de cache pode ficar atrás da origem. O contrato deve dizer se aceita stale,
se exige read-after-write ou se deve consultar a autoridade depois de uma alteração.
Separar chaves por tenant, usuário, locale e política de acesso é obrigatório quando o
valor não é público.

Não armazene tokens, credenciais ou dados pessoais sem avaliar criptografia, acesso,
retenção e limpeza. Cache em memória de processo não é compartilhado entre réplicas e
desaparece no restart. Cache distribuído adiciona rede, autenticação, capacidade e outro
failure domain.

## Observabilidade

Monitore hit rate, miss rate, latência, tamanho, evictions, idade, stale responses,
erros de serialização e chamadas à origem. Hit rate alto não prova correção: uma chave
errada pode produzir muitos hits do valor errado.

Métricas agregadas devem evitar chaves individuais como labels. Use logs e traces para
investigar uma entrada específica e inclua a versão, namespace e motivo do miss.

## Cache e CDN

Uma CDN é uma camada de cache distribuída na borda da rede. O [CDN](../rede/cdn.md)
explica headers HTTP, origem, purge, assets versionados e limites para conteúdo privado.
Cache de aplicação e CDN podem coexistir, mas possuem chaves, TTLs e autoridade
independentes.

## Relações

- [CDN](../rede/cdn.md) distribui cache HTTP próximo do consumidor.
- [Replicação](replicacao.md) mantém cópias do estado primário.
- [Transações e ACID](transacoes-acid.md) define o limite de confirmação da fonte de verdade.
- [Resiliência](../confiabilidade/resiliencia.md) trata fallback e indisponibilidade da origem.
- [Stale-while-revalidate](https://datatracker.ietf.org/doc/html/rfc5861) formaliza uma diretiva HTTP relacionada.

## Fonte primária

- [RFC 9111, HTTP caching](https://www.rfc-editor.org/rfc/rfc9111.html)
- [RFC 5861, stale controls](https://www.rfc-editor.org/rfc/rfc5861.html)
