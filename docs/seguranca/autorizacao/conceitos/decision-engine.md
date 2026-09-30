# Decision Engine

Decision engine é o componente que interpreta um modelo e calcula uma decisão
de autorização. PDP é o papel arquitetural; decision engine descreve o motor
que executa a avaliação.

## Propriedades

Uma decisão segura deve ser determinística para a mesma entrada e versão de
policy. O engine deve limitar tempo de avaliação, recursão, consultas externas
e tamanho da entrada.
