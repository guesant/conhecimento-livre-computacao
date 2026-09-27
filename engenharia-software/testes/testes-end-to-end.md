# Testes end-to-end

Teste end-to-end, ou E2E, verifica uma jornada através de várias partes do
sistema, usando uma perspectiva próxima à de um usuário ou consumidor real.
Em uma aplicação web, isso pode incluir browser, frontend, backend,
autenticação, banco de dados e integrações selecionadas.

O objetivo é confirmar que as fronteiras funcionam em conjunto. Um teste E2E
pode detectar problemas que nenhum teste unitário encontra, como rota
incorreta, cookie incompatível, contrato quebrado, migração ausente,
permissão mal configurada ou falha de hidratação.

## O que entra no fluxo

O ambiente deve ser definido pelo risco. Nem todo E2E precisa usar serviços de
terceiros ou produção. Um ambiente efêmero e controlado costuma produzir
feedback melhor. As dependências externas podem ser simuladas quando o
objetivo é o fluxo da aplicação, desde que haja testes separados para o
contrato da integração real.

Os dados precisam ser determinísticos. Crie entidades identificáveis, isole
tenants, limpe o estado ou use um banco descartável e evite depender de dados
que outra execução pode alterar. Autenticação, emails, filas e uploads
precisam de estratégias próprias para o ambiente de teste.

## Custo e flakiness

E2E é mais lento e possui mais pontos de falha que um teste unitário. Browser,
rede, servidor, banco, relógio, animações e recursos compartilhados podem
interferir. A resposta não é aumentar timeouts indiscriminadamente. Registre
artefatos, espere por condições observáveis, controle os recursos e investigue
a origem da instabilidade.

Use E2E para fluxos de alto valor, como login, autorização, publicação,
checkout, recuperação ou uma jornada que atravessa contratos importantes.
Não transforme cada combinação de dados em uma jornada completa quando uma
camada mais baixa oferece feedback suficiente.

## Seletores e asserções

Prefira seletores baseados em função ou contrato, como role, label, test id
estável ou URL pública. Classes de layout, posições e detalhes gerados pelo
CSS são frágeis. Asserções devem verificar o resultado que o usuário percebe,
não apenas que um clique foi executado.

Um fluxo E2E precisa validar estados de sucesso e falha. Quando a aplicação
usa carregamento assíncrono, espere dados, transições ou navegação por uma
condição verificável. Não use sleeps fixos para compensar uma sincronização
incerta.

## Execução em CI

A pipeline deve publicar logs, screenshots, vídeo ou trace quando houver uma
falha. Separe falha de produto, falha de ambiente e teste instável. Repetir
automaticamente um teste pode ajudar a coletar evidência, mas não deve
transformar flakiness em aprovação silenciosa.

Combine E2E com testes unitários, de integração, de contrato, acessibilidade e
segurança. O E2E demonstra uma jornada, não a correção de toda a lógica
interna.

## Ferramentas

[Cypress](cypress.md) e [Playwright](playwright.md) são ferramentas comuns
para automatizar browsers. A escolha deve considerar browsers necessários,
isolamento, execução paralela, depuração, suporte a múltiplos contextos,
integrações e experiência da equipe.
