# Manutenção de repositório

Esta categoria trata mecanismos que preservam a qualidade do repositório ao
longo do tempo. Ela separa o contrato do histórico, a integridade dos links e
outras verificações que não pertencem à validação do artefato de produção.

## Fronteiras

Ferramentas de manutenção verificam o material versionado e o fluxo de
colaboração. Elas não substituem testes da aplicação, schema validation,
policy as code ou scanners de segurança. Um link válido, por exemplo, não
prova que o código para o qual ele aponta é seguro.

## Navegação

- [commitlint](commitlint.md) verifica o contrato das mensagens de commit.
- [Lychee](lychee.md) verifica links locais e externos.
- [jscpd](jscpd.md) procura duplicação lexical e clones próximos.

## Relações

- [Validação declarativa](../validacao/index.md) trata a validade estrutural e
  as políticas dos artefatos.
- [Diátaxis](../../diataxis.md) ajuda a classificar documentação sem misturar
  procedimento, explicação e referência.
