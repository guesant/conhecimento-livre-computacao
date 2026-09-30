# Field-Level Authorization

Field-Level Authorization decide quais campos de um recurso um subject pode
ler ou alterar. Ela é necessária quando dois usuários podem acessar o mesmo
objeto, mas não os mesmos atributos.

## Implementação

O filtro pode ocorrer na API, serializer, query ou banco. Não dependa somente
de remover o campo na interface, pois exportações e endpoints alternativos
podem expô-lo.

## Custo

Granularidade por campo aumenta complexidade de schema e testes. Use-a para
dados realmente sensíveis, não para substituir um modelo de domínio confuso.
