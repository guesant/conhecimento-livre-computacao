# HCL

HashiCorp Configuration Language, HCL, é uma linguagem declarativa usada para
descrever configuração e infraestrutura. Ela combina blocos nomeados,
atributos, expressões e tipos estruturados.

## Modelo

Blocos agrupam uma unidade semântica, como resource ou provider. Atributos
recebem expressões, que podem referenciar variáveis, locals, resources e data
sources. O grafo de referências permite planejar dependências sem transformar
a configuração em uma sequência imperativa.

HCL não é uma linguagem exclusiva de Terraform ou OpenTofu. As ferramentas
definem o schema dos blocos e o significado das expressões que aceitam.

## Relações

- [OpenTofu](opentofu.md) usa HCL para infraestrutura.
- [Resource](resource.md) e [Data source](data-source.md) são blocos distintos.
- [State](state.md) registra resultado conhecido fora do arquivo HCL.

## Fonte primária

- [HCL syntax](https://github.com/hashicorp/hcl/blob/main/hclsyntax/spec.md)
