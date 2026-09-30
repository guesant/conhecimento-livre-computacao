# DNS resolver

Um resolver recebe uma consulta de um cliente e obtém uma resposta por cache ou
consultando outros servidores. Um stub resolver do sistema geralmente
encaminha a pergunta; o resolvedor recursivo executa a busca necessária.

## Recursão e cache

Sem uma resposta válida no cache, o resolver recursivo segue delegações desde
a raiz, TLD e servidor autoritativo. TTL define por quanto tempo a resposta
pode ser reutilizada. Cache reduz latência e carga, mas mantém respostas
antigas até a expiração.

`dig @<servidor> nome tipo` isola o resolver consultado.
`dig +trace nome` mostra a cadeia de delegação sem usar uma recursão
intermediária da mesma forma.

## Segurança

Um resolver precisa controlar quem pode fazer consultas recursivas e validar
DNSSEC quando essa responsabilidade estiver habilitada. Expor recursão para a
internet facilita abuso e amplificação. DNSSEC autentica dados, mas não
criptografa a consulta.

## Failure modes

Diferencie NXDOMAIN, resposta vazia, timeout, SERVFAIL e resposta antiga no
cache. Compare o stub, o resolver local e o autoritativo antes de alterar o
registro. Uma mudança correta pode continuar invisível até o TTL expirar.

## Relações

- [Servidor autoritativo](authoritative.md) mantém dados de uma zona.
- [Zona DNS](zone.md) define a fronteira administrativa.
- [DNSSEC](dnssec.md) valida autenticidade de respostas.

## Fontes primárias

- [RFC 1034](https://www.rfc-editor.org/rfc/rfc1034)
- [RFC 1035](https://www.rfc-editor.org/rfc/rfc1035)
