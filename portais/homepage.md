# Homepage

Homepage, do projeto gethomepage, é um dashboard auto-hospedado orientado a configuração declarativa. Ele reúne links, grupos, serviços e widgets por meio de arquivos que podem ser versionados e revisados junto da infraestrutura.

## Modelo declarativo

A composição do painel fica separada em arquivos de configuração, serviços, bookmarks e widgets. Essa separação permite revisar o que é navegação, o que é consulta de estado e o que é segredo. O container deve receber apenas os arquivos necessários e a persistência deve ser respaldada por backup.

## Integrações

Widgets consultam APIs de serviços e exibem informações como estado, uso ou contagem. Cada integração deve usar credenciais próprias, com o menor escopo possível, e ter limites de timeout e frequência. A falha de uma integração deve afetar seu widget, não ocultar os links básicos do painel.

## Quando usar

Homepage é uma boa escolha quando a configuração declarativa, a revisão no Git e a reprodução em outro host são mais importantes do que uma edição visual completa. O custo é exigir mais conhecimento de YAML e um ciclo explícito para validar e promover alterações.

## Relações

- [Portais e dashboards](index.md) explica o espaço de decisão.
- [Dashy](dashy.md) oferece uma alternativa centrada em seções e links.
- [Homarr](homarr.md) oferece uma alternativa com administração mais interativa.

## Fonte primária

- [Documentação do Homepage](https://gethomepage.dev/)
