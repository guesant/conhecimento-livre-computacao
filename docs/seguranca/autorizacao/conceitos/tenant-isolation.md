# Tenant isolation

Tenant isolation impede que dados, operações e recursos de uma organização
sejam acessados por outra. É uma propriedade do desenho completo, não apenas
um campo tenant_id.

## Camadas

O isolamento pode usar banco separado, schema, RLS, filtros de consulta,
policies, namespaces, chaves de criptografia e limites de recursos. Quanto mais
crítico o dado, menos a aplicação deve depender de uma única camada.

## Teste

Teste acesso cruzado com IDs válidos de outro tenant, jobs, exportações,
cache, arquivos e endpoints administrativos.
