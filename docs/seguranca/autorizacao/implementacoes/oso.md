# Oso

Oso é um framework de autorização embutida na aplicação. Ele oferece uma
linguagem de políticas, Polar, e bibliotecas para integrar decisões ao código
da aplicação.

## Modelo

Oso combina regras declarativas com fatos da aplicação. A decisão costuma
ocorrer no mesmo processo do serviço, o que reduz latência, mas aproxima a
política do ciclo de deploy da aplicação.

## Limites

Uma biblioteca local não resolve automaticamente consistência entre serviços.
Quando várias aplicações compartilham autorização por objeto, um modelo
central de relações ou um PDP compartilhado pode ser mais adequado.

## Fonte

- [Documentação do Oso](https://www.osohq.com/docs)
