# Cypress

Cypress é uma ferramenta de testes para aplicações web com suporte a testes
end-to-end e de componentes. Os testes são escritos em JavaScript ou
TypeScript e podem executar ações no browser, fazer asserções sobre a
interface e controlar partes da comunicação da aplicação.

## Modelo de execução

O Cypress trabalha próximo da aplicação que está sendo testada e oferece uma
fila de comandos, espera automática em várias operações, snapshots e
ferramentas de depuração. Esse modelo torna a execução interativa e ajuda a
entender o estado da página em cada passo.

A espera automática não corrige uma sincronização mal definida. O teste ainda
deve esperar uma condição observável, usar seletores estáveis e evitar sleeps
fixos. Timeouts maiores podem apenas esconder uma aplicação lenta ou um teste
que não encontrou o elemento correto.

## E2E e componentes

No modo E2E, o Cypress abre a aplicação e percorre uma jornada. No modo de
componentes, ele monta uma unidade visual com seu ambiente de teste. O segundo
modo dá feedback mais rápido para estados de UI, enquanto o primeiro valida
rotas, integração e comportamento atravessado.

Intercepte chamadas de rede somente quando isso for compatível com a hipótese.
Um teste que simula todo o backend não prova que o frontend está integrado ao
contrato real. Mantenha testes de contrato e alguns fluxos com serviços reais
no ambiente controlado.

## Pontos fortes e limites

Cypress oferece uma experiência de desenvolvimento integrada, boa inspeção do
estado do teste e APIs voltadas a quem trabalha com aplicações web. A escolha
pode ser menos adequada quando o projeto precisa controlar muitos contextos de
browser independentes, testar múltiplos engines com a mesma suíte ou modelar
cenários de automação fora do navegador.

O isolamento, o reset de dados, a autenticação e o controle de rede precisam
ser desenhados pelo projeto. A ferramenta não elimina flakiness causada por
estado compartilhado, animação, dependência externa ou ambiente instável.

## CI

Execute a suíte em ambiente reproduzível, guarde screenshots, vídeos e logs
quando houver falha e não use retry como substituto de diagnóstico. Divida
testes críticos e extensos quando o tempo total impedir feedback frequente.

## Fontes

- [Introdução ao Cypress](https://docs.cypress.io/app/core-concepts/introduction-to-cypress)
- [Documentação do Cypress](https://docs.cypress.io/)
- [Testes end-to-end](testes-end-to-end.md)
