# Dogtag Certificate System

Dogtag é uma infraestrutura de autoridade certificadora de código aberto para emissão e gerenciamento de certificados. O sistema cobre partes do ciclo de vida de uma PKI, incluindo emissão, revogação, publicação de CRL, OCSP, perfis de certificado, SCEP e funções de registro.

## Responsabilidades

Uma instalação Dogtag pode operar CA, subsistemas de registro e políticas de emissão. Perfis determinam quais solicitações são aceitas e como certificados são formados. Revogação e publicação de status permitem que consumidores descubram que uma credencial não deve mais ser aceita.

A CA não é apenas um endpoint que assina CSR. Ela precisa proteger a chave da autoridade, controlar quem pode aprovar solicitações, manter auditoria e definir recuperação. Comprometer a CA amplia o impacto para todos os certificados emitidos por sua hierarquia.

## Relação com FreeIPA

FreeIPA pode integrar Dogtag como sua CA para certificados de usuários, hosts e serviços. O diretório guarda dados da solução, Kerberos fornece autenticação e Dogtag fornece a autoridade criptográfica. Essa composição permite tratar identidade de usuário e identidade de máquina dentro de políticas relacionadas, mas não elimina a necessidade de escolher perfis, validade, revogação e distribuição de confiança.

## Quando usar

Dogtag é apropriado quando a organização precisa de uma CA completa com ciclo de vida, perfis e integração com identidade corporativa ou FreeIPA. Uma CA menor como step-ca pode ser mais simples quando o problema é emitir certificados automatizados para poucos protocolos e não exige os mesmos subsistemas.

Cert-manager pode automatizar consumidores Kubernetes, mas não substitui automaticamente a autoridade e os fluxos administrativos do Dogtag. Eles podem participar da mesma composição em papéis diferentes.

## Failure modes

- Chave da CA indisponível ou perdida impede emissão e pode impedir recuperação da hierarquia.
- Perfil permissivo pode emitir identidades além do necessário.
- CRL ou OCSP inacessíveis alteram a capacidade de consumidores verificarem revogação.
- CA e registro fora de sincronia podem criar solicitações pendentes ou inconsistentes.
- Confiança não distribuída faz certificados válidos parecerem inválidos nos clientes.

## Relações

- [CA](ca.md) explica a autoridade certificadora como conceito.
- [CSR](csr.md) explica a solicitação de assinatura.
- [Revogação](revocation.md) e [OCSP](ocsp.md) explicam o status posterior à emissão.
- [FreeIPA](../identidade/freeipa.md) documenta a composição integrada.

## Fonte primária

- [Dogtag Certificate System](https://www.dogtagpki.org/)
