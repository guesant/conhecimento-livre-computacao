# PowerDNS Authoritative Server

PowerDNS Authoritative Server é um nameserver que responde pelas zonas que
administra. Ele não deve ser tratado como um resolver recursivo genérico para
clientes. Seu modelo de dados usa backends, que podem ser arquivos de zona,
bancos relacionais, armazenamento próprio, APIs ou outras integrações
suportadas pela versão instalada.

## Modelo operacional

O servidor recebe uma consulta, identifica a zona autoritativa e lê o registro
no backend configurado. A separação entre serviço DNS e armazenamento facilita
automação, delegação e operação multi-tenant, mas transforma o banco ou a API
em uma dependência de consistência e disponibilidade. O caminho de consulta
deve ser medido separadamente do caminho administrativo que altera zonas.

Backends relacionais como PostgreSQL podem ser úteis quando equipes ou
aplicações precisam administrar muitas zonas por meio de dados estruturados.
Isso não significa que o DNS deva consultar tabelas arbitrárias a cada
requisição. O backend, cache e índices precisam ser dimensionados para o
padrão de consultas real.

## Recursos e aplicações

- autoridade para domínios públicos ou internos;
- zonas primárias e secundárias, com AXFR e IXFR conforme a configuração;
- DNSSEC e gerenciamento de material criptográfico;
- atualizações dinâmicas ou publicação por API, com autenticação adequada;
- integração com bancos relacionais e sistemas de provisionamento;
- operação atrás de dnsdist para balanceamento, filtragem e proteção de
  abuso.

É uma boa escolha quando o catálogo de zonas precisa ser automatizado,
consultado por ferramentas ou integrado a uma base de dados. Para um único
roteador doméstico, a complexidade de um backend e de uma API pode ser
desnecessária.

## Segurança

Desabilite recursão no serviço autoritativo, limite transferências de zona a
secundários conhecidos, proteja TSIG e restrinja a API de gerenciamento à rede
administrativa. A API embutida pode expor estatísticas, configurações, zonas e
material sensível; não a publique sem autenticação e controle de origem.

Separe o processo autoritativo do recursor quando os clientes, políticas e
níveis de confiança forem diferentes. Use dnsdist ou filtragem externa quando
o serviço precisar de rate limiting, defesa contra abuso ou distribuição
entre instâncias.

## Diagnóstico

Verifique o backend, a zona, o serial, a delegação, o estado DNSSEC, a
autorização de transferência e a resposta do autoritativo diretamente. Compare
`dig @servidor nome tipo +norecurse` com a resposta de um resolver recursivo.
Um erro no banco ou na API de provisionamento pode impedir uma alteração sem
que o processo DNS esteja indisponível para as zonas já carregadas.

## Relações

- [PowerDNS Recursor](powerdns-recursor.md) trata resolução recursiva e cache.
- [Servidor DNS autoritativo](authoritative.md) explica o papel independente
  da implementação.
- [dnsdist](https://www.dnsdist.org/) pode distribuir e filtrar consultas.
- [DNSSEC](dnssec.md) explica autenticação de dados DNS.

## Fontes primárias

- [PowerDNS Authoritative Server documentation](https://docs.powerdns.com/authoritative/)
- [PowerDNS Authoritative API](https://doc.powerdns.com/authoritative/http-api/)
- [PowerDNS project](https://www.powerdns.com/)
