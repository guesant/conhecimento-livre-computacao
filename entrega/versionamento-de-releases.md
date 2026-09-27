# Mapa de versionamento de releases e identificadores

Uma versão publicada precisa responder duas perguntas diferentes. A primeira é qual contrato ou conjunto de funcionalidades a release oferece. A segunda é qual artefato exato foi produzido e executado. SemVer, CalVer e numeração sequencial tentam comunicar a primeira pergunta. Um hash Git responde principalmente à segunda.

Confundir essas funções causa problemas práticos. Um hash não informa se uma API mudou de modo incompatível. Uma versão semântica não prova qual conteúdo de um artefato foi publicado. Uma data ajuda a ordenar releases, mas não garante compatibilidade. Um número sequencial pode identificar uma build sem carregar qualquer significado sobre a API.

## Versionamento semântico

SemVer usa três componentes: `MAJOR.MINOR.PATCH`. A especificação pressupõe uma API pública que possa ser analisada.

- `MAJOR` indica mudança incompatível com a API anterior;
- `MINOR` indica funcionalidade nova compatível;
- `PATCH` indica correção compatível;
- pré-releases, como `2.0.0-rc.1`, ficam abaixo da versão final;
- build metadata, como `1.4.2+linux.amd64`, acrescenta informação sem determinar precedência.

O benefício é transformar o número em uma promessa de compatibilidade. Essa promessa só funciona se o projeto definir a API, considerar comportamento observável e aplicar a regra de forma consistente. Uma alteração pode ser tecnicamente compatível para uma biblioteca e incompatível para uma aplicação que dependia de um detalhe antes não documentado.

SemVer funciona bem para bibliotecas, APIs, CLIs e componentes que mantêm contratos consumidos por terceiros. Ele funciona pior quando o produto entrega continuamente, não possui API estável ou quando toda release precisa ser consumida como um snapshot independente. A especificação também exige que o conteúdo de uma versão publicada não seja alterado; uma correção deve receber outra versão.

## Versionamento por calendário

CalVer incorpora a data da release ao identificador. Formatos comuns incluem ano e mês, ano e semana ou ano, mês e sequência do release, mas o projeto precisa documentar seu formato. Um exemplo como `2026.09` comunica quando a versão foi publicada, não que mudanças entre `2026.08` e `2026.09` são compatíveis.

Esse esquema é útil para distribuições, imagens, ferramentas e serviços em que atualidade ou ciclo de manutenção importam mais que uma promessa universal de compatibilidade. Ele também torna evidente a idade de uma release e combina bem com cadências regulares.

CalVer não deve ser interpretado como ordenação de compatibilidade. Uma release de manutenção pode quebrar comportamento mesmo que o mês tenha avançado pouco. Se consumidores precisam de uma promessa explícita, o projeto pode documentar compatibilidade separadamente, usar canais estáveis e preview, ou combinar uma política de compatibilidade com a data.

## Numeração sequencial

O esquema sequencial atribui um contador crescente às releases ou builds: `1042`, `1043`, `1044`. O número pode representar uma versão de produto, uma execução de CI, uma revisão de pacote ou simplesmente a ordem de publicação.

Sua vantagem é a simplicidade. O identificador é fácil de ordenar e pode ser aceito por sistemas que não entendem SemVer. Sua desvantagem é não carregar semântica. `1044` não informa se houve correção, recurso novo ou quebra de contrato. A equipe precisa consultar changelog, metadados da build, contrato da API ou uma referência Git.

O contador também exige definir o escopo. Um contador por pipeline pode repetir entre branches, projetos ou ambientes. Um contador global pode ser difícil de coordenar. Se a propriedade relevante for unicidade, use um identificador de build com origem e contexto, por exemplo `api-1044` ou `2026.09.26-1044`, sem fingir que isso comunica compatibilidade.

## Hash Git

Git identifica objetos por um hash do conteúdo e dos metadados do objeto. Um commit inclui a árvore do snapshot, o commit pai, identidade, data e mensagem. Por isso, alterar qualquer um desses elementos produz outro identificador. O hash é excelente para rastreabilidade e reprodução: uma imagem, um binário ou uma implantação pode apontar para o commit que a produziu.

O hash não é uma versão de produto. Ele não tem ordem de compatibilidade, não indica a intenção da mudança e não é uma mensagem de release. Um hash curto só pode ser usado enquanto for inequívoco dentro do repositório; o hash completo é mais adequado para manifestos, auditoria e referências automatizadas.

O hash também não é uma assinatura. Ele identifica o conteúdo, mas não prova quem autorizou ou produziu o commit. Para autenticidade, combine commit ou tag com assinatura, controle de origem, proveniência e atestação. Git historicamente usa SHA-1 em muitos repositórios, embora também suporte repositórios com SHA-256; o formato efetivo deve ser tratado como propriedade do repositório, não presumido por uma integração.

## Como combinar os esquemas

Os esquemas podem cumprir funções complementares. Uma release pode ter a versão `3.2.1`, um número interno de build `1044` e o commit `a1b2c3d...`. O primeiro comunica o contrato; o segundo ajuda a localizar a execução no CI; o terceiro identifica a origem exata do código.

Uma imagem de container pode usar uma tag legível, como `3.2.1`, junto de um digest imutável. Um manifesto de deploy pode registrar a tag para leitura humana e resolver o digest para impedir que uma tag reapontada altere o conteúdo. A mesma ideia vale para charts, binários e artefatos publicados com checksum.

## Comparação

| Esquema | Comunica | Ordena | Indica compatibilidade | Identifica conteúdo exato |
| --- | --- | --- | --- | --- |
| SemVer | tipo de mudança de API | Sim | Sim, se a política for seguida | Não |
| CalVer | data ou cadência | Sim, se o formato for definido | Não por si só | Não |
| Sequencial | ordem ou número interno | Sim dentro do mesmo escopo | Não | Não |
| Hash Git | objeto ou commit exato | Não como versão de produto | Não | Sim, para o objeto identificado |

## Seleção prática

Use SemVer quando consumidores precisam decidir se uma atualização é compatível. Use CalVer quando a idade, a cadência e a janela de manutenção são mais importantes que a semântica da API. Use numeração sequencial para builds e releases internas, desde que o escopo esteja definido. Use hash Git para rastreabilidade, reprodução e ligação entre fonte e artefato.

Não use nenhum desses números como substituto de changelog, contrato, testes de compatibilidade, SBOM ou proveniência. Versionar é comunicar uma identidade; garantir o conteúdo e a segurança da release exige metadados e verificações adicionais.

## Fontes primárias

- [Semantic Versioning 2.0.0](https://semver.org/lang/pt-BR/spec/v2.0.0.html)
- [CalVer](https://calver.org/)
- [Git objects](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects)
- [Git revision selection](https://git-scm.com/book/en/v2/Git-Tools-Revision-Selection)
