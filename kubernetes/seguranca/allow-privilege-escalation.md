# allowPrivilegeEscalation

allowPrivilegeEscalation controla se um processo pode obter mais privilégios que seu processo pai em condições suportadas pelo runtime/kernel.

Defini-lo como false é uma defesa importante, mas não substitui redução de capabilities e outras políticas de isolamento.