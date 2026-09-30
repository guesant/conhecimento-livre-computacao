# Balana

Balana é uma implementação de XACML para avaliação de políticas de autorização.
Ela fornece um PDP que interpreta políticas e requisições segundo o modelo
XACML.

## Modelo

A decisão é derivada de atributos, regras e algoritmos de combinação. O sistema
precisa receber uma requisição completa e confiável; não deve aceitar atributos
de autorização diretamente de um cliente não confiável.

## Relações

Balana é uma implementação de engine XACML. A linguagem e o modelo XACML são
mais amplos que uma biblioteca de RBAC local e exigem uma governança própria de
políticas.

## Fonte

- [Projeto Balana](https://github.com/wso2/balana)
