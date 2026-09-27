# Criptografia simétrica

Criptografia simétrica usa a mesma chave secreta, ou chaves derivadas de um
segredo comum, para cifrar e decifrar dados. Ela é eficiente para grandes
volumes e aparece no armazenamento, em túneis, em sessões TLS e em protocolos
de aplicação.

O problema central é distribuir a chave. Todos que precisam decifrar também
podem, em princípio, produzir ou modificar dados. O sistema precisa proteger
essa chave, definir seus destinatários e impedir que uma cópia continue válida
depois de uma revogação.

## Cifras autenticadas

Uma cifra autenticada, como AES-GCM ou ChaCha20-Poly1305, oferece
confidencialidade e integridade autenticada. Além do texto cifrado, a operação
produz uma tag que falha quando o ciphertext, o nonce ou os dados associados
foram alterados.

Nonce não é senha nem chave. Em modos que exigem unicidade, reutilizar o mesmo
nonce com a mesma chave pode revelar relações entre mensagens ou comprometer a
segurança. O formato deve armazenar ou transportar o nonce e a tag de forma
inequívoca.

Dados associados podem autenticar contexto que não precisa ser cifrado, como
um identificador de versão, tenant ou tipo de registro. O consumidor precisa
fornecer exatamente o mesmo contexto durante a decifragem.

## Chave e derivação

Uma senha humana tem pouca entropia para ser usada diretamente como chave.
Derive a chave com uma KDF adequada, como Argon2id, scrypt ou PBKDF2 conforme
o requisito. A derivação deve usar salt, parâmetros e um contexto separados
de outros usos da mesma senha.

Quando uma chave aleatória é protegida por uma chave pública, o protocolo usa
normalmente um esquema híbrido: a cifra simétrica protege o conteúdo e a
criptografia assimétrica protege a chave de sessão. Isso combina desempenho
com distribuição controlada.

## Modos inadequados

ECB revela padrões e não deve ser usado para cifrar dados estruturados. CBC
sem autenticação permite alterações ou ataques de padding quando o protocolo
não trata esses problemas. Construir uma cifra própria, reutilizar nonce ou
comparar tags de forma inadequada pode anular um algoritmo robusto.

Prefira bibliotecas de alto nível que ofereçam uma construção autenticada
completa. Não escolha algoritmo somente pelo nome: versão da biblioteca,
geração de aleatoriedade, armazenamento da chave, rotação e recuperação fazem
parte da segurança.

## Relações

- [Hash](hash.md) produz digests, não texto decifrável.
- [Criptografia assimétrica](criptografia-assimetrica.md) ajuda a distribuir
  chaves sem compartilhar previamente o mesmo segredo.
- [age](../secrets/age.md) usa um formato de criptografia de arquivos.

## Fontes

- [NIST, Recommendation for Block Cipher Modes, SP 800-38D](https://csrc.nist.gov/pubs/sp/800/38/d/final)
- [RFC 8439, ChaCha20 and Poly1305](https://www.rfc-editor.org/rfc/rfc8439)
- [OWASP, Cryptographic Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html)
