# Fine-Grained Authorization

Fine-grained authorization, FGA, é autorização em um nível menor que uma rota
ou um papel global. A decisão pode depender do objeto, da relação, da linha,
do campo, do tenant ou do contexto da operação.

## Trade-off

Mais granularidade melhora precisão, mas aumenta custo de modelagem, consulta,
cache, auditoria e migração. O nível escolhido deve acompanhar o risco e a
necessidade real do domínio.

## Relações

FGA inclui autorização por objeto e por relação, mas não exige uma tecnologia
específica. OpenFGA e SpiceDB são implementações da família Zanzibar.
