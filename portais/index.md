# Portais e dashboards de serviços

Portais de serviços e dashboards de homelab reúnem links, estado operacional e atalhos para aplicações internas. Eles resolvem um problema de navegação e descoberta, não substituem observabilidade, autenticação, inventário ou um catálogo de serviços bem definido.

## Responsabilidades

Um portal pode organizar aplicações por grupo, expor bookmarks, consultar APIs de serviços e mostrar indicadores simples. A fonte do link, o mecanismo de descoberta e o estado exibido precisam ser separados: uma página inicial não deve se tornar a autoridade dos dados operacionais que apenas referencia.

## Escolha

[Dashy](dashy.md) é uma opção centrada em configuração declarativa e seções de links. [Homarr](homarr.md) oferece uma experiência de painel mais integrada, com widgets e edição pela interface. [Homepage](homepage.md), do projeto gethomepage, privilegia configuração declarativa e integração com serviços por arquivos.

Escolha considerando o modo de administração, a necessidade de widgets, o custo de renderização, o modelo de autenticação, a persistência da configuração e a facilidade de revisar mudanças no Git. Em um cluster pequeno, limites de CPU e memória e a simplicidade do backup importam tanto quanto a aparência.

## Segurança

O portal deve ficar atrás de autenticação e autorização apropriadas. Widgets que consultam APIs não devem receber tokens administrativos no navegador sem uma necessidade explícita. Trate URLs, nomes de serviços e metadados exibidos como dados potencialmente sensíveis, porque eles podem revelar topologia, versões ou endpoints internos.

## Relações

- [Observabilidade](../observabilidade/index.md) trata coleta, armazenamento e análise de sinais.
- [Ingress](../kubernetes/networking/ingress.md) e [Gateway API](../gateway-api.md) tratam publicação de serviços.
- [Dashboards de observabilidade](../observabilidade/grafana.md) respondem perguntas sobre sinais, enquanto um portal organiza o acesso às aplicações.

## Fontes primárias

- [Dashy](https://dashy.to/)
- [Homarr](https://homarr.dev/)
- [Homepage](https://gethomepage.dev/)
