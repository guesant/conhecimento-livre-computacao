# Argon2

Argon2 é uma função de hashing de senhas e derivação de chaves criada para tornar ataques
de tentativa mais caros em CPU e memória. Ela foi a vencedora da Password Hashing
Competition e foi especificada para uso interoperável no [RFC 9106](https://www.rfc-editor.org/rfc/rfc9106).

Argon2 não cifra a senha e não permite recuperar o texto original. Para verificar uma
senha, a aplicação executa a mesma função com a senha candidata, o salt e os parâmetros
armazenados, e compara o resultado por meio da API da biblioteca.

## Variantes

### Argon2d

Argon2d usa acessos à memória dependentes dos dados derivados da senha. Essa propriedade
pode dificultar alguns ataques paralelos especializados, mas o padrão de acesso pode vazar
informação por canais laterais de tempo ou cache.

Por isso, Argon2d não deve ser a escolha geral para armazenamento de senhas quando um
atacante pode observar o ambiente de execução. Ele pode fazer sentido em cenários de
proof-of-work ou quando o modelo de ameaça exclui side-channels, mas isso precisa ser uma
decisão explícita.

### Argon2i

Argon2i usa acesso à memória independente do conteúdo da senha. Isso oferece uma propriedade
mais favorável contra determinados side-channels, mas exige mais passes ou parâmetros
adequados para resistir a time-memory trade-offs.

Argon2i pode ser usado para derivação de chave ou em uma biblioteca que o exige por motivos
específicos, mas não é normalmente a primeira escolha para armazenar senhas novas.

### Argon2id

Argon2id combina os modelos: no início do primeiro passe usa o comportamento independente
de dados de Argon2i e depois usa o comportamento dependente de dados de Argon2d conforme a
especificação. A intenção é equilibrar proteção contra side-channel e custo de ataques
paralelos.

O RFC 9106 exige suporte a Argon2id, enquanto Argon2d e Argon2i são variantes opcionais.
Para senha de usuário, Argon2id é a escolha geral recomendada quando a implementação está
disponível.

## Parâmetros

Uma configuração de Argon2 normalmente inclui:

| Parâmetro | Significado | Efeito de aumentar |
| --- | --- | --- |
| `m` | memória usada, normalmente em KiB na API | aumenta pressão de memória e custo do atacante |
| `t` | número de passes ou iterações | aumenta trabalho de CPU e memória |
| `p` | grau de paralelismo ou lanes | usa mais paralelismo até o limite da máquina |
| `T` | tamanho do resultado | altera a saída, não substitui o custo principal |
| `S` | salt aleatório | separa hashes iguais e impede pré-computação reutilizável |
| `K` | segredo opcional ou pepper da API | adiciona segredo fora do banco, quando usado corretamente |
| `X` | associated data opcional | vincula o resultado a um contexto adicional |

Nem toda biblioteca expõe todos os parâmetros com os mesmos nomes ou unidades. Use a API
da implementação e armazene a string codificada produzida por ela.

### Tuning

O custo deve ser ajustado com benchmark de login, cadastro e reset de senha. Teste também
uma rajada de tentativas concorrentes, porque o atacante controla a quantidade de pedidos
ao endpoint.

Como referência, OWASP publica uma configuração mínima atual para Argon2id de 19 MiB de
memória, duas iterações e paralelismo 1. O RFC 9106 também apresenta configurações
recomendadas mais pesadas para ambientes com mais recursos. Esses números não substituem
medição do ambiente e não devem ser copiados para um dispositivo com limites muito menores
sem avaliar disponibilidade.

Memória e concorrência precisam ser planejadas juntas. Se um worker puder verificar 100
senhas ao mesmo tempo, uma configuração de 64 MiB pode demandar vários gigabytes durante
um ataque. Rate limiting, proteção contra credential stuffing e limites de workers são parte
do desenho.

## Salt, pepper e formato

O salt deve ser aleatório, único por senha e armazenado junto ao hash. Ele não precisa ser
secreto. A string codificada costuma carregar variante, versão, parâmetros, salt e resultado,
em um formato semelhante a:

```text
$argon2id$v=19$m=...,t=...,p=...$salt$hash
```

O formato exato pertence à biblioteca. Não monte ou faça parse manualmente se a biblioteca
possui funções para isso.

Pepper é um segredo adicional mantido fora do banco, normalmente em secret manager ou HSM.
Ele pode aumentar a proteção contra um dump isolado do banco, mas cria dependência de
recuperação, rotação e disponibilidade. Se o pepper for perdido, a verificação pode deixar
de funcionar; se for exposto junto com o banco, sua proteção adicional desaparece.

## Verificação e rehash

Use a função de verificação da biblioteca, que lê os parâmetros codificados e compara de
forma apropriada. Depois de uma autenticação bem-sucedida, verifique se o hash está abaixo
do custo atual. Se estiver, rederive com Argon2id novo e substitua o valor sem pedir a senha
em texto novamente.

Não rehash uma senha usando o hash antigo como se fosse a senha. Isso cria uma credencial
alternativa e pode manter um segredo fraco como entrada permanente.

## Derivação de chave não é armazenamento de senha

Argon2 pode derivar uma chave para criptografar dados, mas os objetivos são diferentes.
Para uma chave de arquivo, a aplicação precisa definir tamanho da chave, salt, nonce, cifra,
associated data e mecanismo de autenticação. Para uma senha de login, precisa armazenar um
verificador e usar parâmetros adaptativos.

Não reutilize o mesmo formato ou contexto sem domain separation. A biblioteca pode oferecer
APIs diferentes para hashing de senha e derivação de chave por esse motivo.

## Relações

[Hashing de senhas](index.md) cobre o fluxo geral. [bcrypt](bcrypt.md) é uma alternativa
mais antiga e amplamente compatível. [libsodium](https://doc.libsodium.org/password_hashing)
usa Argon2id na API de alto nível atual, mas a aplicação ainda deve tratar parâmetros,
limites e migração de acordo com a versão e o ambiente.

## Fontes primárias

- [RFC 9106](https://www.rfc-editor.org/rfc/rfc9106)
- [OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
- [libsodium password hashing](https://doc.libsodium.org/password_hashing)
- [Argon2 reference implementation](https://github.com/P-H-C/phc-winner-argon2)
