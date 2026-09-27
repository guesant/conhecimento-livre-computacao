# Resource

Resource é o objeto protegido por uma decisão. Pode ser uma rota, documento,
arquivo, linha, campo, bucket, namespace ou recurso de infraestrutura.

## Identificação

O identificador deve ser canônico, não ambíguo e vinculado ao tenant correto.
Uma policy que recebe apenas um nome curto pode autorizar o recurso errado.

## Escopo

O resource pode possuir relações com outros recursos. Em ReBAC, essas relações
permitem derivar acesso sem copiar permissões para todas as instâncias.
