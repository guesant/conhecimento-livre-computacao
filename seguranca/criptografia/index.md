# Hashing de senhas

Senha não deve ser armazenada em texto claro nem protegida por uma cifra reversível. A
aplicação deve armazenar somente o material necessário para verificar uma tentativa futura,
usando uma função de derivação lenta, adaptativa e com salt único por registro.

Esta categoria trata funções de hashing de senhas. Ela não trata hashing rápido para
integridade de arquivos, assinatura digital, cifra de dados ou derivação de uma chave de
backup. São problemas diferentes e possuem requisitos diferentes.

## O que precisa ser armazenado

Um registro de senha normalmente precisa carregar:

- identificador do algoritmo;
- versão do algoritmo, quando aplicável;
- parâmetros de custo;
- salt aleatório e único;
- resultado derivado;
- eventualmente um identificador de pepper mantido fora do banco.

O formato codificado deve permitir que a aplicação escolha o verificador correto e saiba se
o custo precisa ser atualizado. Não é necessário esconder o algoritmo ou o salt. O segredo
é a senha e, se usado, o pepper.

## Comparação inicial

| Algoritmo | Propriedade principal | Limitação importante | Uso recomendado |
| --- | --- | --- | --- |
| Argon2id | Memória e CPU configuráveis, com proteção equilibrada | Exige tuning de memória sob concorrência | Nova aplicação quando disponível |
| Argon2i | Acesso à memória independente da senha | Mais custo para resistir a trade-offs | Casos específicos de side-channel |
| Argon2d | Acesso dependente da senha, forte contra alguns ataques especializados | Possível exposição a side-channel | Não usar para senha como escolha geral |
| bcrypt | Custo adaptativo e ampla compatibilidade | Limite de entrada de 72 bytes e pouca memória | Sistemas legados ou quando Argon2 não está disponível |
| PBKDF2 | Baseada em HMAC e disponível em ambientes FIPS | Não é memory-hard | Requisito de compatibilidade ou compliance |

Para novas aplicações, Argon2id costuma ser o primeiro candidato. OWASP recomenda bcrypt
principalmente para sistemas legados quando Argon2 e scrypt não estão disponíveis. A escolha
final depende da biblioteca, do ambiente, do requisito de compliance e do benchmark de
verificação sob a concorrência real.

## Fluxo de cadastro e login

No cadastro ou na troca de senha:

1. receba a senha por um canal protegido;
2. aplique as regras de comprimento e política sem truncar silenciosamente;
3. gere um salt com um CSPRNG ou deixe a biblioteca gerar;
4. derive o hash com parâmetros medidos;
5. armazene a string codificada e os parâmetros;
6. nunca registre a senha, o hash intermediário ou o pepper.

No login:

1. carregue o registro pelo identificador da conta;
2. passe a senha recebida à função de verificação da biblioteca;
3. compare por meio da API da biblioteca, sem comparar strings manualmente;
4. retorne uma resposta que não revele se o usuário existe;
5. se o custo armazenado estiver antigo, rederive o hash após autenticação bem-sucedida;
6. invalide sessões ou tokens conforme a política de troca e comprometimento.

Não faça `hash(senha)` em cada login e compare strings simples. Esse padrão pode usar salt
incorreto, perder os parâmetros ou introduzir diferenças de tempo. Use `verify` e
`needsRehash` da biblioteca escolhida.

## Parâmetros e capacidade

O custo deve tornar uma tentativa legítima suficientemente rápida para o usuário e cada
tentativa de ataque suficientemente cara. Meça criação e verificação sob concorrência,
com CPU e memória semelhantes às da produção.

Memória configurada por hash se multiplica pelo número de logins concorrentes. Um parâmetro
adequado para uma requisição isolada pode provocar OOM quando um atacante abre muitas sessões.
Rate limiting, proteção de endpoint, filas e limites de worker complementam o password hash.

Faça benchmark quando trocar hardware, runtime, biblioteca ou número de réplicas. O objetivo
não é escolher o maior número possível, mas manter um custo que a infraestrutura consiga
absorver sem sacrificar disponibilidade.

## Migração

Algoritmos modernos não conseguem transformar um hash antigo em um hash novo sem a senha.
Uma migração gradual funciona assim:

1. aceite temporariamente o formato antigo somente no verificador isolado;
2. após uma verificação bem-sucedida, gere o novo Argon2id ou bcrypt com os parâmetros atuais;
3. substitua o valor no mesmo fluxo protegido;
4. marque contas que não retornam para exigir reset depois de uma janela definida;
5. remova o verificador antigo quando a política permitir.

Não faça downgrade para facilitar compatibilidade com um hash legado. Não transforme um hash
antigo em texto, nem armazene a senha temporariamente para uma migração em lote.

## Relação com autenticação

Hash de senha protege uma credencial armazenada. Ele não fornece MFA, sessão, recuperação,
rate limiting, detecção de abuso, autorização ou proteção contra phishing. A aplicação ainda
precisa de política para tentativas falhas, recuperação de conta, credenciais comprometidas,
logs e cookies.

Veja [Argon2](argon2.md), [bcrypt](bcrypt.md), [gerenciamento de segredos](../secrets/index.md)
e [autenticação e autorização](../identidade/fundamentos/index.md).

## Fontes primárias

- [OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
- [RFC 9106, Argon2](https://www.rfc-editor.org/rfc/rfc9106)
- [libsodium password hashing](https://doc.libsodium.org/password_hashing)
- [OpenBSD crypt manual](https://man.openbsd.org/crypt.3)
