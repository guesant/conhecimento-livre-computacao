# Aserto

Aserto é uma plataforma de autorização que oferece políticas, dados de
identidade e decisões de acesso para aplicações. Seu foco é centralizar
autorização fina sem obrigar cada produto a duplicar regras.

## Arquitetura

O sistema pode usar um PDP remoto ou um componente próximo da aplicação. A
política precisa receber um subject, um resource, uma action e contexto
confiável. O resultado deve ser auditável e associado à versão da política.

## Critérios

Aserto é interessante quando a organização precisa de governança central,
integração com diretórios e decisões por objeto. Verifique dependência de
serviço externo, disponibilidade durante falhas e portabilidade das políticas.

## Fonte

- [Documentação do Aserto](https://docs.aserto.com/)
