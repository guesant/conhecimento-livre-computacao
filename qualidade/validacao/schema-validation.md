# Schema validation

Schema validation verifica se um documento corresponde a uma estrutura
formal. O schema descreve campos, tipos, obrigatoriedade, valores permitidos e
às vezes relações entre campos. O resultado é uma decisão sobre a validade
estrutural da entrada, não sobre sua segurança ou adequação operacional.

## Modelo de entrada e saída

O validador recebe um documento e um schema compatível com seu formato e
versão. Ele retorna sucesso ou violações localizadas, como campo desconhecido,
tipo incorreto, propriedade ausente ou valor fora do conjunto permitido. Um
pipeline deve preservar o código de saída e o contexto do documento para que
uma falha seja diagnosticável.

No Kubernetes, o schema OpenAPI do recurso descreve a estrutura conhecida pelo
servidor. CRDs podem fornecer schemas próprios. Validar o manifesto
renderizado é importante, porque valores de Helm, patches e templates podem
alterar a estrutura que será aplicada.

## Limites

Um documento estruturalmente válido ainda pode executar como root, expor uma
porta indevida, solicitar recursos incompatíveis com o cluster ou violar uma
política da organização. Essas propriedades pertencem a policy as code,
análise de segurança e revisão operacional.

O schema também pode não representar toda a semântica do controlador. Campos
aceitos pelo servidor podem ter efeitos diferentes conforme o controlador,
versão ou combinação de recursos. A validação deve acompanhar a versão real
do ambiente.

## Posição no pipeline

Uma sequência útil é renderizar o artefato, validar o schema, executar políticas
organizacionais e só então publicar ou aplicar. O schema deve falhar cedo,
antes que uma política produza uma mensagem confusa para uma entrada que já é
inválida.

## Relações

- [kubeconform](kubeconform.md) automatiza validação de manifests Kubernetes.
- [Conftest](conftest.md) verifica políticas sobre documentos estruturados.
- [Policy as code](policy-as-code.md) trata regras que não cabem no schema.

## Fontes primárias

- [Kubernetes API concepts](https://kubernetes.io/docs/reference/using-api/api-concepts/)
- [Custom resources](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/)
- [JSON Schema](https://json-schema.org/specification)
