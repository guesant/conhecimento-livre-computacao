# Auto-unseal e KMS

Auto-unseal substitui a apresentação manual das chaves de unseal por uma
operação automática contra um serviço de gerenciamento de chaves externo.
Durante a inicialização, o secret store autentica, solicita a descriptografia
da chave mestra cifrada e conclui o destravamento.

## O que muda

O mecanismo reduz o trabalho operacional após crashes, atualizações e
failovers. Em uma topologia com várias réplicas, ele evita exigir que alguém
destrave cada instância antes de ela participar da eleição.

Ele não elimina a proteção do material criptográfico. A confiança passa a
estar na identidade que o secret store usa para chamar o KMS e na política que
limita essa identidade à chave e às operações necessárias. Comprometer essa
identidade pode produzir um efeito equivalente à exposição das chaves de
unseal.

## Domínio de falha

O KMS deve estar fora do domínio de falha que o secret store protege. Guardar
a única chave de auto-unseal dentro do mesmo cluster cria dependência circular:
o cluster precisa do secret store para recuperar a credencial, e o secret
store precisa do cluster para recuperar a chave.

## Quando usar

Auto-unseal faz sentido em produção, quando a recuperação não pode esperar um
operador humano. Em ambientes de desenvolvimento, o unseal manual pode ser
mais simples e reduzir componentes externos.

## Relações

[Vault](vault.md) e [OpenBao](openbao.md) usam esse modelo. [Backup da chave
age](age-key-backup.md) trata outro modelo de recuperação, baseado em material
cifrado fora do cluster.
