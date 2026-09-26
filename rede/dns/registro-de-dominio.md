# Registro de domínio

Registrar um domínio cria uma relação administrativa com um registrador e permite controlar a delegação daquele nome na hierarquia DNS. Registrador, registry e provedor DNS são papéis diferentes, embora um mesmo fornecedor possa oferecer mais de um.

## Caso de uso

Uma organização pode registrar o domínio em um fornecedor e hospedar a zona autoritativa em outro. A delegação no parent aponta para nameservers autoritativos; registros dentro da zona são administrados no provedor DNS.

## Como registrar um domínio

"Comprar um domínio" normalmente significa registrar o direito de uso de um
nome por um período renovável. O titular não compra a hierarquia DNS nem o
endereço IP. Ele mantém uma inscrição no registry, por meio de um registrar ou
do próprio serviço de registro quando esse modelo estiver disponível.

O fluxo geral é:

1. escolher o nome e o TLD, como `.br`, `.com` ou outro sufixo compatível com o
   público e as regras do registry;
2. consultar a disponibilidade no serviço oficial ou em um registrar;
3. criar uma conta protegida por MFA e informar corretamente o titular;
4. pagar o período de registro e configurar a renovação automática;
5. informar nameservers autoritativos ou usar o DNS oferecido pelo registrar;
6. criar registros A, AAAA, CNAME, MX, TXT e outros conforme os serviços;
7. habilitar DNSSEC quando o provedor e o TLD suportarem a cadeia de confiança;
8. guardar credenciais, códigos de transferência e contatos de recuperação.

Para `.br`, o caminho é o [Registro.br](https://registro.br/). Em outros TLDs,
o registry define as regras e registrars credenciados intermediam o registro.
O fornecedor que vende o domínio não precisa ser o mesmo que hospeda DNS, site,
e-mail, CDN ou API.

## Transferência e expiração

Antes de trocar de registrar, verifique bloqueio de transferência, código EPP
ou AuthInfo, prazo restante, contatos e a possibilidade de renovar durante o
processo. Mantenha alertas para expiração e confirme que a forma de pagamento
não depende de uma única pessoa. Perder um domínio pode interromper DNS, e-mail,
login, certificados, webhooks e integrações de terceiros.

## Boa prática

Proteja a conta do registrador com autenticação forte, mantenha contatos e renovação sob controle e trate alterações de nameserver e DS como mudanças sensíveis.

## Má prática

Confundir "comprar domínio" com "hospedar DNS" dificulta migrações e troubleshooting. Outra má prática é depender de renovação manual sem alertas para um domínio usado por serviços críticos.

## Continue por aqui

[DNSSEC](dnssec.md) adiciona cadeia de confiança à delegação. A página de resolução, zonas e registros explica o conteúdo da zona.
