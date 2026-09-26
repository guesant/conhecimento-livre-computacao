# Heroku

Heroku é uma plataforma como serviço para construir, publicar e operar aplicações sem administrar diretamente servidores. O modelo tradicional usa buildpacks para transformar o código em um slug e dynos para executar processos. Add-ons e serviços externos complementam banco, cache, filas, observabilidade e outros recursos.

## Modelo de execução

O deploy produz uma versão imutável do aplicativo, e os dynos executam processos definidos pela aplicação. Web dynos atendem requisições; worker dynos processam tarefas assíncronas; processos agendados podem ser adicionados por serviços da plataforma ou por componentes externos. O filesystem local não deve ser tratado como armazenamento durável.

## Quando faz sentido

Heroku é forte quando a prioridade é experiência de desenvolvimento, convenção de deploy, ambientes simples, revisão rápida e baixo trabalho de operação de host. É uma opção didática e produtiva para APIs e aplicações web que se encaixam no modelo de processos da plataforma.

## Limitações

O cliente tem menos controle sobre sistema operacional, rede e topologia do que numa IaaS. Custos de dynos, add-ons, transferência e serviços externos precisam ser acompanhados. Aplicações com requisitos específicos de kernel, rede privada, jobs longos ou armazenamento local podem precisar de outro modelo.

Use variáveis de ambiente para configuração, trate releases como artefatos reproduzíveis, mantenha migrações reversíveis e defina como exportar banco, logs e arquivos antes de depender de add-ons.

## Fontes primárias

- [Heroku platform](https://www.heroku.com/platform/)
- [Heroku build process](https://www.heroku.com/dynos/build/)
- [Buildpacks](https://devcenter.heroku.com/articles/buildpacks)
