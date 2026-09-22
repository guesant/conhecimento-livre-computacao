# Bancos chave-valor

Um banco key-value organiza dados principalmente como associação entre uma chave e um valor. O modelo favorece acesso direto quando a aplicação conhece a chave.

## Casos de uso

Cache, sessão, coordenação e estados simples com lookup por identificador são usos comuns, dependendo das garantias oferecidas pela implementação.

## Boa prática

Modele chaves, TTL, consistência e persistência de acordo com o papel real do dado. Diferencie cache descartável de estado que precisa sobreviver a falhas.

## Má prática

Usar um key-value store como banco primário apenas porque operações simples são rápidas pode transferir complexidade de consulta e integridade para a aplicação.

## Continue por aqui

[Document databases](documentos.md) oferecem um modelo de consulta diferente para dados estruturados.