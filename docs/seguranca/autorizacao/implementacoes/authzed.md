# Authzed

Authzed é a organização e a plataforma associada ao ecossistema SpiceDB. Seu
produto gerenciado oferece autorização baseada em relações sem exigir que cada
aplicação opere diretamente o banco e os componentes de distribuição.

## Responsabilidade

A plataforma hospeda o PDP e o armazenamento de relações. A aplicação continua
responsável por autenticar sujeitos, escolher identificadores estáveis,
escrever relações corretas e tratar indisponibilidade do serviço.

## Modelo operacional

O schema define relações e permissões. O consumidor consulta uma decisão para
um sujeito, uma ação e um recurso. O contrato deve definir se uma falha no PDP
nega a operação, usa cache limitado ou interrompe o fluxo.

## Relações

Authzed e SpiceDB compartilham o modelo de autorização, mas uma instalação
autogerenciada e um serviço gerenciado possuem responsabilidades operacionais
diferentes.

## Fontes

- [Authzed](https://authzed.com/)
- [Documentação do SpiceDB](https://authzed.com/docs/spicedb/overview)
