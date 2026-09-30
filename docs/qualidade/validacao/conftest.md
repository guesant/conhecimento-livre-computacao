# Conftest

Conftest avalia documentos estruturados com políticas Rego. Ele separa a
validação estrutural do documento da decisão organizacional sobre o que pode
ser aplicado.

## O que ele resolve

O fluxo recebe YAML, JSON, HCL ou outro formato suportado, converte o conteúdo
para a representação esperada pela política e executa regras OPA. A saída
indica violações, mensagens e o código de retorno do processo. Isso permite
avaliar manifests renderizados, valores de Helm, configuração de OpenTofu e
artefatos de pipeline antes de enviá-los ao ambiente.

Conftest não é um admission controller e não substitui a validação de schema.
Um documento pode obedecer ao schema e ainda violar uma regra de segurança ou
de governança.

## Modelo de política

As políticas são organizadas por pacote Rego. Uma regra deve expressar uma
decisão observável, produzir uma mensagem útil e receber somente os dados de
que precisa. Políticas pequenas facilitam testes unitários e reduzem o risco
de uma mudança de estrutura quebrar regras não relacionadas.

Uma política pode verificar, por exemplo, que uma imagem usa digest, que um
Deployment possui limites de recursos ou que um recurso não pode publicar uma
porta específica. A regra deve deixar claro se uma ausência é erro, aviso ou
caso permitido.

## Uso em pipeline

O pipeline normalmente renderiza o artefato primeiro, executa schema
validation e então chama Conftest com o diretório de políticas. A ordem evita
que uma política precise interpretar estruturas inválidas. O mesmo conjunto
de políticas deve ser executado localmente e na CI, com versões fixadas e
entrada reproduzível.

Não transforme toda preferência de estilo em uma política bloqueante. Regras
que não protegem uma propriedade operacional, de segurança ou de conformidade
criam atrito e incentivam o bypass.

## Failure modes e diagnóstico

Falhas podem vir de uma política não carregada, de um caminho de entrada
incorreto, de uma mudança no schema do documento ou de uma regra que assume
campos opcionais como obrigatórios. Para diagnosticar, confirme o formato da
entrada, liste as políticas carregadas, execute uma política isoladamente e
compare o documento renderizado com a versão usada no pipeline.

Evite ignorar a política inteira para um caso excepcional. Quando a exceção é
real, modele-a explicitamente na política e teste tanto o caminho permitido
quanto o bloqueado.

## Relações

- [Schema validation](schema-validation.md) verifica a forma do documento.
- [Policy as code](policy-as-code.md) explica o modelo mais amplo de políticas.
- [kubeconform](kubeconform.md) é uma ferramenta especializada em schemas de
  recursos Kubernetes.

## Fontes primárias

- [Conftest](https://www.conftest.dev/)
- [Open Policy Agent](https://www.openpolicyagent.org/docs/latest/)
