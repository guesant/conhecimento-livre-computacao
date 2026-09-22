# ACME

Automatic Certificate Management Environment, ACME, é um protocolo para automatizar emissão e renovação de certificados.

O cliente demonstra controle ou autorização sobre uma identidade conforme um challenge suportado e solicita à CA a emissão do certificado.

## Público e privado

Let's Encrypt popularizou ACME para certificados públicos. CAs privadas como step-ca também podem expor ACME para reutilizar clientes e automações existentes.

## O que ACME não resolve

ACME automatiza o protocolo de emissão. Ele não distribui automaticamente a CA privada aos trust stores dos consumidores e não define autorização de aplicação.

## Fonte

- RFC 8555: <https://www.rfc-editor.org/rfc/rfc8555>

## Continue por aqui

[step-ca](step-ca.md) implementa um servidor ACME possível. [Trust store](trust-store.md) cobre o outro lado da confiança.
