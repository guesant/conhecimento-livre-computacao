# Linux capabilities em containers

Linux capabilities dividem partes do privilégio tradicional de root em unidades menores.

Em containers, remover capabilities desnecessárias reduz a superfície disponível após comprometimento. Uma política comum começa removendo todas e adicionando apenas as exigidas.

Capabilities são mecanismo do Linux, não invenção do Kubernetes; SecurityContext apenas expõe configuração relacionada.