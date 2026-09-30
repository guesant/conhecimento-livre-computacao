# Confluence

Confluence é um workspace de conhecimento e colaboração da Atlassian. Seu
modelo principal é formado por páginas organizadas em espaços e árvores de
páginas. Ele atende documentação técnica, decisões, planos, atas, políticas,
runbooks e bases de conhecimento que precisam ser editadas e descobertas por
mais de uma pessoa.

## Modelo de conteúdo

Uma página tem histórico de versões, comentários, permissões e links. Um espaço
agrupa conteúdo de uma equipe, produto, projeto ou domínio. A árvore de páginas
organiza a navegação, mas não deve substituir uma taxonomia editorial pensada:
uma árvore profunda demais esconde informação, enquanto um espaço sem donos vira
um depósito de documentos difíceis de revisar.

Defina proprietário, público, ciclo de revisão e destino de cada classe de
conteúdo. Uma decisão arquitetural, uma instrução operacional e uma referência
consultável podem viver em espaços relacionados, mas não deveriam compartilhar
o mesmo template sem necessidade.

## Colaboração

Edição simultânea, comentários, menções, notificações, templates e recursos
visuais ajudam equipes a construir conhecimento. A integração com Jira pode
ligar uma página a um projeto ou item de trabalho; a integração com Bitbucket
pode relacionar documentação e mudanças de código. Esses links são contexto,
não substitutos de uma política de backup e exportação.

## Cloud e Data Center

Confluence Cloud delega infraestrutura e upgrades à Atlassian. Confluence Data
Center é autogerenciado e exige planejamento de nós, storage, banco, busca,
backup, atualizações, identidade e recuperação. Em ambos os casos, permissões
de espaço e página devem ser revisadas, principalmente quando conteúdo pode ser
compartilhado externamente.

## Segurança e retenção

Documentação frequentemente contém segredos acidentais, dados pessoais,
diagramas de rede e decisões sensíveis. Use classificação, restrições de
espaço, revisão de convidados, retenção e auditoria. Não trate um espaço como
cofre de secrets. Conteúdo apagado, anexos e versões antigas precisam entrar no
modelo de retenção e no plano de exportação.

## Quando usar

Confluence é adequado quando a organização precisa de páginas colaborativas,
hierarquia, histórico, busca e integração com trabalho de produto. Para
documentação versionada junto do código, Markdown no Git pode ser mais
reprodutível. Para uma base pequena e pública, um site estático pode reduzir
permissões e custo operacional.

## Relações

- [Atlassian](atlassian.md) explica a relação com Jira e Bitbucket.
- [Bitbucket](../forjas/bitbucket.md) hospeda código e revisão.
- [Ferramentas de colaboração](../index.md) separa forge de conhecimento.

## Fontes

- [Confluence, guia introdutório](https://www.atlassian.com/software/confluence/resources/guides/get-started/overview)
- [Confluence features](https://www.atlassian.com/software/confluence/features)
- [Set up Confluence spaces](https://www.atlassian.com/software/confluence/resources/guides/get-started/set-up)
