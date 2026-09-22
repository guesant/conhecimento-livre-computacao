# Registro de domínio

Registrar um domínio cria uma relação administrativa com um registrador e permite controlar a delegação daquele nome na hierarquia DNS. Registrador, registry e provedor DNS são papéis diferentes, embora um mesmo fornecedor possa oferecer mais de um.

## Caso de uso

Uma organização pode registrar o domínio em um fornecedor e hospedar a zona autoritativa em outro. A delegação no parent aponta para nameservers autoritativos; registros dentro da zona são administrados no provedor DNS.

## Boa prática

Proteja a conta do registrador com autenticação forte, mantenha contatos e renovação sob controle e trate alterações de nameserver e DS como mudanças sensíveis.

## Má prática

Confundir "comprar domínio" com "hospedar DNS" dificulta migrações e troubleshooting. Outra má prática é depender de renovação manual sem alertas para um domínio usado por serviços críticos.

## Continue por aqui

[DNSSEC](dnssec.md) adiciona cadeia de confiança à delegação. A página de resolução, zonas e registros explica o conteúdo da zona.