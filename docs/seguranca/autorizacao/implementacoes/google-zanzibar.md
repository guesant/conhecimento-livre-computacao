# Google Zanzibar

Google Zanzibar é o sistema distribuído de autorização por relações descrito
em uma publicação do Google. O modelo usa relações entre sujeitos e recursos,
consultas de permissão e garantias de consistência adequadas a uma grande
organização.

## Ideias centrais

O sistema trata autorização como um serviço global, separa o armazenamento de
relações do enforcement e usa revisões para relacionar decisões a um estado
observado. A consistência escolhida influencia segurança, latência e
disponibilidade.

## Relações

OpenFGA, SpiceDB, Auth0 FGA e Ory Keto são implementações ou serviços que usam
ideias da família Zanzibar. Nenhum deles deve ser assumido como uma cópia
intercambiável do sistema original.

## Fonte

- [Zanzibar, Google Research](https://research.google/pubs/zanzibar-googles-consistent-global-authorization-system/)
