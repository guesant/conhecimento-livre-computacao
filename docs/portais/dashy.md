# Dashy

Dashy é um portal de serviços auto-hospedado para organizar links e informações de aplicações em uma página inicial. A configuração pode ser mantida como arquivo, o que facilita revisão, backup e promoção junto do restante da infraestrutura.

## Modelo

O portal é organizado em seções e itens. Um item pode apontar para uma aplicação, carregar um ícone e, quando configurado, exibir um widget ou indicador associado ao serviço. O valor do Dashy está na composição do acesso, não em substituir a aplicação referenciada.

## Operação

Mantenha a configuração fora da imagem e monte-a por um mecanismo versionado ou por um volume com backup. Separe links públicos de links administrativos e coloque o portal atrás do mesmo modelo de autenticação aplicado às demais interfaces internas. Widgets devem ter timeouts, limites de frequência e permissões mínimas.

## Limitações

Quanto mais widgets forem habilitados, maior será o número de chamadas, a dependência de APIs externas e a superfície de credenciais. Um erro de um serviço não deve impedir o carregamento do restante do portal. Evite transformar o Dashy em uma página que executa consultas caras em todas as visitas.

## Relações

- [Portais e dashboards](index.md) compara a responsabilidade da categoria.
- [Homarr](homarr.md) é uma alternativa com maior ênfase em widgets e administração pela interface.
- [Homepage](homepage.md) é uma alternativa declarativa voltada a integrações configuradas em arquivos.

## Fonte primária

- [Documentação do Dashy](https://dashy.to/docs/)
