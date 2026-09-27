# Shamir Secret Sharing

Shamir Secret Sharing é um esquema de compartilhamento de segredo baseado em
polinômios. Um segredo é dividido em partes de modo que qualquer conjunto de
`k` partes, em um total de `n`, consiga reconstruí-lo, enquanto menos de `k`
partes não deve revelar informação suficiente sobre o segredo.

## Modelo matemático

O esquema escolhe um polinômio de grau `k - 1` sobre um campo finito. O segredo
é o termo independente. Cada participante recebe um ponto diferente do
polinômio. A reconstrução usa interpolação de Lagrange e recupera o termo
independente quando o limiar é atingido.

O limiar não é criptografia de armazenamento por si só. Ele distribui a
capacidade de reconstruir uma chave, mas cada parte precisa de autenticação,
confidencialidade e integridade. Uma parte adulterada pode impedir a
reconstrução ou produzir um valor incorreto se não houver verificação adicional.

## Escolha do limiar

`3-of-5`, por exemplo, tolera a perda de duas partes e não permite que dois
participantes reconstruam sozinhos. O valor deve refletir disponibilidade,
independência organizacional e risco de conluio. Colocar todas as partes no
mesmo servidor, no mesmo cofre ou com a mesma pessoa não cria independência
real, mesmo que o número matemático esteja correto.

## Uso para recuperação

O esquema é adequado para uma chave mestra de recuperação, uma chave de
desbloqueio ou uma credencial que só deve ser usada em uma cerimônia. Não é
normalmente adequado para cada requisição de uma aplicação: reconstruir o
segredo em um processo cria uma concentração temporária de confiança.

Uma cerimônia precisa definir identidade dos participantes, registro de partes,
verificação de integridade, ambiente limpo, auditoria, rotação e destruição de
material temporário. A política também deve dizer como recuperar quando uma
parte é perdida e como revogar uma parte suspeita.

## Confusões comuns

O esquema não é um backup cifrado completo, não substitui um KMS e não prova a
identidade de quem apresenta uma parte. Também não protege contra um participante
que possui o limiar e decide revelar o segredo. Para dividir uma chave já usada
por outro sistema, preserve seu formato, sua entropia e o procedimento de
reconstrução antes de apagar a cópia original.

## Relações

- [age](age.md) trata criptografia de arquivos e chaves de recuperação.
- [Custódia de chaves fora do host](custodia-de-chaves-fora-do-host.md) trata separação operacional.
- [Criptografia simétrica](../criptografia/criptografia-simetrica.md) explica a chave que pode ser compartilhada.

## Fontes primárias

- [How to share a secret, Adi Shamir](https://web.mit.edu/6.857/OldStuff/Fall03/ref/Shamir-HowToShareASecret.pdf)
- [Handbook of Applied Cryptography, secret sharing](http://cacr.uwaterloo.ca/hac/about/chap12.pdf)
