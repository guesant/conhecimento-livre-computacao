# Registro.br

O Registro.br é o serviço responsável pelo registro e pela manutenção de nomes de domínio sob o `.br`. Ele funciona como registry nacional do espaço de nomes brasileiro, mantendo a base de titulares, domínios e delegações conforme as regras aplicáveis.

## O que um registro de domínio resolve

O registro cria uma relação administrativa para que um nome, como `exemplo.com.br`, seja único dentro da hierarquia `.br`. Depois do registro, o titular pode informar servidores DNS autoritativos e controlar os registros da zona por meio desses servidores.

Registrar o domínio não hospeda automaticamente o site, a API, o e-mail ou o banco de dados. Esses serviços podem estar em provedores diferentes. O papel do Registro.br é manter a delegação e a administração do nome, não executar a aplicação apontada pelo nome.

## Registry, registrar e DNS

O Registro.br é o registry. Provedores de serviços homologados podem intermediar operações de registro e manutenção. Um provedor de hospedagem pode oferecer DNS, aplicações e e-mail, mas não se torna automaticamente o registry do `.br`.

O fluxo de resolução envolve camadas diferentes:

1. o Registro.br mantém a delegação do domínio no `.br`;
2. a delegação aponta para nameservers autoritativos;
3. os nameservers respondem pelos registros da zona;
4. o cliente resolve o nome por meio de um resolver recursivo.

## Segurança e operação

Alterar nameservers, registros DS de DNSSEC ou contatos administrativos pode redirecionar serviços inteiros. A conta do titular deve usar autenticação forte, contatos atualizados, controle de renovação e revisão independente para mudanças sensíveis.

Um domínio expirado pode deixar de ser publicado. Um domínio registrado, mas com nameservers incorretos, pode existir administrativamente e ainda assim não resolver. Esses são problemas diferentes e exigem diagnósticos diferentes.

## Relação com outras organizações

O Registro.br pertence ao ecossistema operacional do NIC.br e segue diretrizes relacionadas ao CGI.br. Ele não atribui IPv4, IPv6 ou ASN, responsabilidade que pertence ao registro regional correspondente, como o LACNIC para a América Latina e o Caribe.

## Fontes primárias

- [Registro.br](https://registro.br/)
- [Registro de novos domínios](https://registro.br/ajuda/registro-de-novos-dominios/)
- [Estatísticas de domínios `.br`](https://registro.br/dominio/estatisticas/)
- [DNSSEC no Registro.br](https://registro.br/ajuda/dnssec/)
