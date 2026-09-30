# Autorização

Autorização decide se uma identidade pode realizar uma ação sobre um recurso em determinado contexto. A decisão pode considerar sujeito, ação, recurso, ambiente, horário, rede, risco e estado da sessão.

RBAC associa permissões a papéis. ABAC avalia atributos. ReBAC usa relações entre entidades. ACLs ligam permissões diretamente a objetos. O modelo escolhido deve ser explícito, auditável e aplicado no servidor, mesmo quando a interface já esconde ações indisponíveis.

Autenticação não concede acesso automaticamente. Um token válido pode identificar o usuário sem permitir a operação solicitada. A aplicação deve validar audiência, escopo, tenant, recurso e política antes de executar uma mudança.

## Falhas comuns

Confundir identidade com permissão, confiar em campos enviados pelo cliente, usar apenas controles de interface e não invalidar privilégios após mudança de papel são falhas recorrentes. Testes devem cobrir tanto acesso permitido quanto negação por cada fronteira relevante.
