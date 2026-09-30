# Baseline de análise estática

Um baseline registra findings já conhecidos para permitir que uma política trate novas violações de forma diferente da dívida existente.

## Caso de uso

Em código legado com muitos findings, exigir zero violações imediatamente pode impedir adoção do scanner. Um baseline permite bloquear regressões enquanto a dívida anterior é tratada separadamente.

## Boa prática

Torne a dívida visível, revise o baseline e remova entradas quando o problema desaparecer.

## Má prática

Usar baseline como lista permanente de exceções sem owner ou revisão apenas congela vulnerabilidades e reduz confiança no gate.

## Continue por aqui

[SAST](index.md) explica como baseline participa de uma estratégia de adoção.
