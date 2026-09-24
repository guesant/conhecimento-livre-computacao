# Homarr

Homarr é um dashboard auto-hospedado para reunir aplicações, atalhos, widgets e informações operacionais em uma interface única. Ele é adequado quando a equipe prefere configurar parte do painel visualmente e precisa de integrações prontas para serviços comuns.

## Modelo

O painel organiza componentes em uma área visual com links e widgets. A configuração e os dados persistentes precisam de uma estratégia explícita de volume, backup e controle de acesso. A interface de administração reduz a barreira inicial, mas pode afastar alterações da revisão no Git se não houver um processo de exportação ou registro.

## Quando usar

Homarr faz sentido quando a prioridade é uma experiência interativa, com widgets e edição acessível a usuários que não querem manter toda a composição em YAML. Em ambientes regulados ou fortemente orientados a GitOps, avalie se o estado editado na interface pode ser reproduzido de forma determinística.

## Segurança e recursos

Integrações devem usar tokens específicos, com escopo mínimo e armazenamento protegido. Defina requests e limits, controle a frequência de consultas e evite widgets que exponham informações de administração ou segredos no lado do cliente. O dashboard deve degradar por widget, sem tornar uma API indisponível um erro global.

## Relações

- [Portais e dashboards](index.md) define limites e critérios da categoria.
- [Dashy](dashy.md) privilegia uma configuração mais simples e declarativa.
- [Homepage](homepage.md) privilegia integração configurada em arquivos e revisão no Git.

## Fonte primária

- [Documentação do Homarr](https://homarr.dev/docs/)
