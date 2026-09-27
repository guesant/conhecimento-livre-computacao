# Supabase RLS

Supabase RLS usa Row-Level Security do PostgreSQL para filtrar linhas conforme
o usuário e o contexto da sessão. Policies ficam no banco e são aplicadas às
consultas compatíveis.

## Modelo

Uma policy define quando uma linha pode ser selecionada, inserida, atualizada
ou removida. O contexto precisa ser derivado de claims e funções confiáveis,
não de parâmetros que o cliente possa forjar.

## Limites

RLS não corrige automaticamente funções privilegiadas, views inseguras ou
conexões administrativas. Teste cada operação e verifique o comportamento do
owner e de roles com bypass.

## Fonte

- [Supabase Row-Level Security](https://supabase.com/docs/guides/database/postgres/row-level-security)
