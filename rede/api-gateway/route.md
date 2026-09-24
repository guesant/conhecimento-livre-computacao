# API gateway route

Uma route define como uma requisição corresponde a um service. Ela pode usar
host, path, método, headers, SNI ou combinações desses atributos.

## Ordem e especificidade

Rotas sobrepostas precisam de uma regra clara de precedência. Um path genérico
que aparece antes de uma exceção pode capturar tráfego que deveria alcançar
outro backend. Teste rotas negativas, métodos não permitidos e trailing slash.

A route não deveria conter credenciais ou lógica de negócio. Ela seleciona
caminho e aplica políticas declaradas pelos plugins ou pelo service.

## Relações

- [Service](service.md) recebe o tráfego selecionado.
- [Plugin](plugin.md) aplica política.
- [Consumer](consumer.md) identifica uma entidade cliente.

## Fonte primária

- [Kong routes](https://docs.konghq.com/gateway/latest/entities/route/)
