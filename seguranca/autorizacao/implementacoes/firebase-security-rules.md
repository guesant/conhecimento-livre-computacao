# Firebase Security Rules

Firebase Security Rules são políticas declarativas para controlar acesso a
serviços Firebase. Elas avaliam identidade, caminho, dados existentes e dados
propostos antes de permitir uma operação.

## Modelo

Rules precisam restringir leitura e escrita por recurso, usuário, tenant e
estado do documento. A validação deve considerar consultas, subcoleções e
operações em lote.

## Limites

Rules não são filtros mágicos para qualquer consulta e não protegem código
backend que usa credenciais administrativas. Teste a matriz de acesso com o
emulator e trate o backend como outra fronteira.

## Fonte

- [Firebase Security Rules](https://firebase.google.com/docs/rules)
