# bcrypt

bcrypt é uma função de hashing de senhas baseada no Blowfish e no esquema de expansão de
chave EksBlowfish. Ela foi desenhada para ser adaptativa: o custo de derivação aumenta por
um fator configurável, permitindo elevar o esforço quando o hardware fica mais rápido.

bcrypt continua amplamente disponível em linguagens, frameworks e formatos legados. Para
aplicações novas, Argon2id costuma ser preferível quando a biblioteca e os requisitos do
ambiente permitem, porque oferece custo de memória configurável além do custo de CPU.

## Formato

Um hash bcrypt costuma ter um formato semelhante a:

```text
$2b$12$..............................
```

O prefixo identifica uma variante, o campo numérico é o work factor e o restante codifica
salt e resultado no formato específico do bcrypt. Não divida ou gere esse valor manualmente;
use a biblioteca que implementa `hash`, `verify` e, quando disponível, `needsRehash`.

### Variantes

Implementações podem encontrar prefixos como `$2a$`, `$2b$` e `$2y$`. Eles refletem
compatibilidade e histórico de implementações, inclusive correções de interpretação de
bytes. A aplicação deve seguir a biblioteca e o formato que ela suporta; não altere o
prefixo apenas como texto.

## Work factor

O custo de bcrypt é expresso como um logaritmo. Aumentar o fator em um passo dobra
aproximadamente o trabalho de expansão de chave. O custo deve ser o maior que a infraestrutura
suporta para o login normal, reset e criação de conta, mantendo proteção contra rajadas.

OWASP recomenda work factor 10 ou maior como mínimo para sistemas que precisam permanecer
em bcrypt, mas o valor adequado deve ser medido no hardware e na biblioteca utilizados.
Um fator muito baixo facilita tentativas offline; um fator excessivo pode derrubar a
disponibilidade durante uma tentativa distribuída de login.

## Limite de 72 bytes

O bcrypt tradicional limita a entrada a 72 bytes, não necessariamente 72 caracteres.
UTF-8, acentos e emojis podem ocupar vários bytes. Algumas bibliotecas truncam, rejeitam ou
tratam entradas longas de forma diferente.

Essa limitação precisa ser conhecida no contrato da aplicação. Não trunque silenciosamente
uma senha longa, porque dois textos diferentes podem produzir a mesma entrada efetiva.
Prefira uma biblioteca que documente o comportamento e valide o limite em bytes.

### Pre-hashing

Aplicar SHA-256 ou outra função rápida antes de bcrypt pode parecer uma forma de superar o
limite, mas cria riscos de interoperabilidade, bytes nulos, truncamento e password shucking.
Não introduza `bcrypt(hash(senha))` sem uma construção documentada, encoding inequívoco,
domain separation e plano de migração. Para novos sistemas, escolher Argon2id evita essa
limitação de forma mais direta.

## Salt e verificação

Cada senha precisa de salt distinto. A biblioteca deve gerar o salt e codificá-lo no
resultado. O salt pode ser armazenado no banco; ele impede que senhas iguais produzam o
mesmo valor e reduz o benefício de tabelas pré-computadas.

No login, use o verificador da biblioteca contra a string completa. Não recompute usando
um salt fixo, não compare hashes com `==` fora da API e não revele se a conta existe.

## Migração de bcrypt para Argon2id

Uma migração segura é gradual:

1. mantenha o verificador bcrypt apenas durante a janela de migração;
2. quando o login for validado, derive Argon2id com o custo atual;
3. substitua o hash bcrypt pelo novo formato no mesmo fluxo protegido;
4. mantenha métricas de contas restantes e de falhas;
5. encerre o suporte ao formato antigo depois do prazo de reset definido.

Se uma conta não retorna para autenticar, não há como obter a senha original a partir do
bcrypt. O caminho é resetar a credencial ou exigir recuperação, nunca tentar converter o
hash antigo em outro hash.

## bcrypt não é bcrypt_pbkdf

`bcrypt` para armazenamento de senha e `bcrypt_pbkdf` para derivação de chave são APIs e
objetivos diferentes. O segundo produz bytes de chave a partir de senha, salt, rounds e
tamanho solicitado; ele não deve ser tratado automaticamente como o formato de login do
primeiro.

Confundir os dois pode gerar um sistema que não tem verificação compatível, usa parâmetros
inadequados ou armazena um segredo derivado sem o formato necessário para migração.

## Comparação com Argon2id

| Dimensão | bcrypt | Argon2id |
| --- | --- | --- |
| Compatibilidade | Muito ampla em stacks antigas | Depende de biblioteca atualizada |
| Custo de CPU | Configurável por work factor | Configurável por iterações |
| Custo de memória | Não é o foco principal | Configurável e memory-hard |
| Limite conhecido | 72 bytes em implementações tradicionais | Depende da API e do limite da aplicação |
| Novos sistemas | Opção de compatibilidade | Opção preferencial quando disponível |
| Migração | Fácil de verificar durante transição | Deve armazenar formato e parâmetros codificados |

## Fontes primárias

- [OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
- [OpenBSD crypt manual](https://man.openbsd.org/crypt.3)
- [bcrypt paper, OpenBSD](https://www.openbsd.org/papers/bcrypt-paper.pdf)
- [Openwall bcrypt implementation](https://www.openwall.com/crypt/)
- [OpenBSD bcrypt_pbkdf](https://man.openbsd.org/bcrypt_pbkdf.3)
