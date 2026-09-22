# Lychee

Lychee verifica links em arquivos e documentação, detectando destinos quebrados ou inacessíveis conforme sua configuração.

## Casos de uso

É útil em documentação versionada, READMEs e sites estáticos com muitas referências externas e internas.

## Boa prática

Diferencie falha permanente de indisponibilidade transitória, configure exclusões estreitas e preserve contexto do link que falhou.

## Má prática

Ignorar domínios inteiros para fazer o gate passar pode esconder regressões reais.