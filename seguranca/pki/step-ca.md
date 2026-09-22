# step-ca

step-ca é uma autoridade certificadora privada operável pela própria organização. Ela suporta emissão X.509 e SSH e pode expor ACME, permitindo integrar clientes que já conhecem esse protocolo.

## Casos de uso

É útil para identidades internas, nomes que uma CA pública não deve ou não pode emitir e ambientes que precisam controlar política e ciclo de vida da própria CA.

## Boa prática

Proteja chaves de CA de acordo com seu impacto, separe raiz e intermediárias quando o modelo justificar, automatize certificados de curta duração e teste renovação e revogação.

## Má prática

Manter a chave raiz online apenas por conveniência aumenta desnecessariamente o impacto de comprometimento. Outra má prática é introduzir uma CA privada sem planejar como os consumidores receberão e atualizarão o trust bundle.

## Fontes

- Smallstep step-ca: https://smallstep.com/docs/step-ca/

## Continue por aqui

[trust-manager](trust-manager.md) resolve distribuição de confiança, não emissão.