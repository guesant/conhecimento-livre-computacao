# Comparação entre hash e criptografia

Hash, criptografia simétrica e criptografia assimétrica são mecanismos
diferentes. A escolha depende da propriedade que o sistema precisa obter, não
de qual nome parece mais seguro.

| Mecanismo | Chave usada | Recupera a entrada | Propriedade principal | Exemplo de uso |
| --- | --- | --- | --- | --- |
| Hash | nenhuma chave, em geral | não | digest e detecção de alteração | integridade, identificador de conteúdo |
| Hash de senha | salt e parâmetros, com segredo opcional | não | verificação lenta de uma senha | login |
| Cifra simétrica | segredo compartilhado | sim, com a chave | confidencialidade eficiente | dados em repouso, sessão |
| Cifra assimétrica | chave pública e privada | conforme o esquema | distribuição, assinatura e autenticação | PKI, SSH, FIDO2 |
| MAC | segredo compartilhado | não | integridade e autenticidade entre partes que compartilham chave | mensagens internas |
| Assinatura | chave privada para assinar | não | autenticidade verificável por chave pública | release, certificado, documento |

## Perguntas de decisão

Se o sistema precisa verificar se um conteúdo mudou, comece por um hash ou
MAC, dependendo de quem precisa confiar no valor publicado. Se precisa
esconder dados, use uma cifra autenticada. Se precisa distribuir a capacidade
de verificar uma assinatura ou autenticar uma chave sem compartilhar o mesmo
segredo, use criptografia assimétrica.

Senhas são um caso especial. O banco não deve possuir uma chave que decifre
senhas. Ele deve armazenar um verificador derivado com uma função adaptativa,
como Argon2id. Se a aplicação precisa recuperar dados cifrados, isso é outro
problema e exige uma chave de recuperação com ciclo de vida próprio.

## Erros comuns

Calcular SHA-256 de uma senha e chamá-lo de armazenamento seguro ignora custo
adaptativo, salt e defesa contra hardware especializado. Cifrar uma senha no
banco com uma chave global cria um alvo único que permite recuperar todas as
senhas quando a chave vaza. Usar uma chave pública para assinar ou uma chave
privada para distribuir dados também mistura operações diferentes.

Uma composição comum é hash para identificar ou resumir, assinatura para
provar origem e cifra simétrica para proteger o conteúdo. A cifra assimétrica
entra para proteger chaves, autenticar participantes ou estabelecer uma sessão.

## Relações

- [Hash](hash.md)
- [Criptografia simétrica](criptografia-simetrica.md)
- [Criptografia assimétrica](criptografia-assimetrica.md)
- [Hashing de senhas](index.md)
