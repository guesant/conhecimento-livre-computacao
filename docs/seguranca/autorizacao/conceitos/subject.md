# Subject

Subject é a identidade em nome da qual uma operação é solicitada. Pode ser um
usuário, serviço, grupo, role, workload ou identidade delegada.

## Identidade

O identificador usado na autorização deve ser estável e vir de uma fonte
confiável. Email, nome exibido ou claims não validadas não devem ser usados
como identidade primária.

## Relações

O subject é diferente da sessão e do token. A sessão autentica o chamador; o
subject representa a entidade que receberá a decisão.
