# Spring Security Authorization

Spring Security Authorization fornece filtros, authorities, method security e
policies para proteger aplicações Spring. A decisão pode ocorrer no request,
em métodos ou em expressões de segurança.

## Modelo

Autenticação estabelece o principal; autorização decide a ação permitida. A
configuração deve definir o comportamento para endpoints não mapeados e usar
negação por padrão.

## Limites

Annotations e expressions não substituem um modelo de domínio coerente. A
aplicação ainda precisa controlar ownership, tenant e filtragem de consultas.

## Fonte

- [Spring Security Authorization](https://docs.spring.io/spring-security/reference/servlet/authorization/index.html)
