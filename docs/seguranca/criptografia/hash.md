# Hash

Hash é uma função que transforma uma entrada de tamanho arbitrário em uma
saída de tamanho definido, chamada digest. Uma função de hash criptográfica
deve tornar impraticável encontrar uma entrada que produza um digest escolhido,
encontrar duas entradas com o mesmo digest e reconstruir a entrada original a
partir da saída.

Hash não é criptografia reversível. Não existe uma chave que permita
decifrar um digest e recuperar a entrada. A propriedade útil depende do
algoritmo, do tamanho da saída, do contexto e da ausência de ataques conhecidos.

## Usos diferentes

Hash rápido pode verificar integridade de arquivos, identificar conteúdo,
construir estruturas de dados e participar de protocolos. Hash de senha precisa
ser deliberadamente lento, adaptativo e resistente a paralelismo massivo. Por
isso, SHA-256 e SHA-3 não devem substituir Argon2id ou bcrypt para armazenar
senhas.

Um hash sozinho não prova quem produziu o conteúdo. Um atacante pode alterar o
arquivo e recalcular o hash publicado no mesmo canal. Para autenticar origem,
combine a mensagem com um segredo em um MAC ou use uma assinatura digital com
chave privada.

## Salt, nonce e contexto

Salt separa instâncias de um mesmo problema, como senhas iguais em registros
distintos. Nonce identifica uma operação em esquemas que exigem unicidade,
como cifras autenticadas. Eles não têm a mesma função e não devem ser
intercambiados por conveniência.

Os parâmetros e o contexto precisam ser codificados sem ambiguidade. Concatenar
campos sem delimitação pode fazer entradas diferentes produzirem a mesma
representação antes mesmo do hash. Use formatos definidos pela biblioteca ou
pelo protocolo.

## Integridade não é confidencialidade

Um digest público permite detectar alteração somente quando o digest esperado
veio de uma fonte confiável. Ele não esconde o conteúdo. Para confidencialidade
use criptografia; para autenticidade use MAC ou assinatura; para senha use uma
função de derivação adaptativa.

## Relações

- [Hashing de senhas](index.md) trata armazenamento e verificação de senhas.
- [Criptografia simétrica](criptografia-simetrica.md) usa uma chave compartilhada.
- [Criptografia assimétrica](criptografia-assimetrica.md) usa um par de chaves.
- [Comparativo entre hash e criptografia](comparativo-hash-cifras.md) separa os objetivos.

## Fontes

- [NIST, Secure Hash Standard, FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final)
- [NIST, SHA-3 Standard, FIPS 202](https://csrc.nist.gov/pubs/fips/202/final)
- [RFC 9106, Argon2](https://www.rfc-editor.org/rfc/rfc9106)
