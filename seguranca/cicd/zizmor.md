# zizmor

zizmor é uma ferramenta de análise estática para CI/CD. Seu alvo não é o código da aplicação, mas definições como workflows e actions do GitHub Actions, além de outras configurações suportadas.

Isso importa porque CI é uma superfície privilegiada: workflows podem possuir tokens, publicar artefatos, assinar releases e executar código proveniente de contribuições externas.

## Casos de uso

zizmor pode auditar workflows durante pull requests, revisar repositórios existentes, produzir SARIF para code scanning e detectar classes de problema específicas de CI, como permissões excessivas, referências mutáveis, triggers perigosos e usos inseguros de recursos do GitHub Actions.

Um uso local básico é:

```bash
zizmor .
```

A ferramenta também pode analisar apenas workflows ou consultar repositórios remotos quando recebe as credenciais necessárias.

## Exemplo de risco: referência mutável

Uma Action referenciada apenas por uma tag pode apontar para conteúdo diferente no futuro sem que o workflow mude. O audit `unpinned-uses` identifica referências que não oferecem a imutabilidade de um SHA de commit.

A boa prática, quando a política exige imutabilidade, é fixar a Action pelo SHA e manter uma anotação legível da versão humana. A atualização pode então ser automatizada por uma ferramenta de dependências.

## Exemplo de risco: permissões

Conceder `contents: write`, `packages: write` ou `id-token: write` globalmente quando apenas um job precisa desse poder amplia o impacto de um comprometimento.

A documentação do zizmor recomenda declarar permissões de forma mínima e próxima do ponto de uso. Um padrão restritivo começa com:

```yaml
permissions: {}
```

e concede ao job apenas o necessário.

## Boas práticas

Rode zizmor sobre mudanças de workflow antes do merge. Use permissões mínimas. Prefira referências imutáveis para dependências externas. Avalie findings no contexto do trigger e da origem das entradas. Use SARIF quando fizer sentido preservar e acompanhar findings.

## Más práticas

É inadequado executar um workflow privilegiado sobre código controlado por um fork sem compreender o modelo de confiança do trigger. Também é má prática liberar permissões amplas para "resolver" erros de autorização ou silenciar audits sem entender o caminho de exploração.

zizmor continua sendo análise estática: comportamento dependente exclusivamente de runtime pode escapar do modelo. Ele reduz classes conhecidas de risco, não prova segurança completa da pipeline.

## Alternativas e complementos

Linters de YAML e validação de schema verificam estrutura, não necessariamente segurança. Policy engines podem impor regras organizacionais. CodeQL analisa código de aplicação e bibliotecas, portanto não deve ser tratado como substituto direto de uma ferramenta especializada na configuração do CI.

## Fontes

- Documentação do zizmor: <https://docs.zizmor.sh/>
- Audit rules: <https://docs.zizmor.sh/audits/>
- Integração com GitHub Actions: <https://docs.zizmor.sh/integrations/>

## Continue por aqui

[SAST](../appsec/sast/index.md) explica a família de análise estática aplicada ao código. [Pinagem por digest e hash](../../pinagem-por-digest-e-hash.md) aprofunda o problema geral de referências mutáveis.
