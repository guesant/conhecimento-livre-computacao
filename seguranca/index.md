# Segurança

Segurança não é uma ferramenta nem um gate isolado. É a redução sistemática de risco em superfícies diferentes: código próprio, dependências, credenciais, infraestrutura, identidade, cadeia de suprimentos e sistema em execução. Uma técnica que cobre uma dessas superfícies não implica cobertura das demais.

Esta seção funciona como mapa. As páginas abaixo aprofundam cada abordagem e, quando uma ferramenta possui comportamento, limitações e alternativas próprias, ela recebe uma página separada.

## Segurança de aplicações

[Segurança de aplicações](appsec/index.md) organiza as técnicas pelo objeto que observam.

- [SAST](appsec/sast/index.md) analisa código sem executá-lo.
- [SCA](appsec/sca/index.md) identifica componentes de terceiros e vulnerabilidades conhecidas.
- [DAST](appsec/dast.md) testa a aplicação em execução pela interface exposta.
- [Secret scanning](appsec/secret-scanning/index.md) procura credenciais que entraram em arquivos ou histórico.

Essas técnicas são complementares. Um SAST não substitui SCA porque não responde quais CVEs existem nas dependências; SCA não substitui DAST porque não observa o comportamento da aplicação implantada; secret scanning não demonstra que uma aplicação é segura, apenas reduz uma classe específica de exposição.

## Segurança de CI/CD

Pipelines também executam código, recebem entradas, consomem dependências e frequentemente possuem credenciais privilegiadas. [zizmor](cicd/zizmor.md) é uma ferramenta especializada em análise estática de configurações de CI/CD, especialmente GitHub Actions.

## Identidade e diretórios

[Identidade e diretórios](identidade/index.md) separa diretório LDAP, autenticação Kerberos, PKI, DNS, sincronização de tempo e integração de clientes. [FreeIPA](identidade/freeipa.md) documenta uma composição integrada; [SSSD](identidade/sssd.md) documenta o componente que opera nos hosts Linux.

## Continue por aqui

[Threat modeling](../threat-modeling.md) ajuda a decidir quais superfícies e ameaças merecem prioridade antes de escolher controles. [Supply chain](supply-chain/index.md) e [SBOM](supply-chain/sbom.md) aprofundam composição, proveniência e artefatos.
