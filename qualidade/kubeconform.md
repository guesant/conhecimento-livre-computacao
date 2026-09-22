# kubeconform

kubeconform valida manifests Kubernetes contra schemas, incluindo suporte a fontes adicionais para CRDs.

## Casos de uso

É adequado como gate rápido para detectar campos inválidos, tipos incorretos e incompatibilidades de schema antes do deployment.

## Boa prática

Valide manifests renderizados e mantenha a fonte de schemas alinhada às versões usadas.

## Má prática

Usar kubeconform como scanner de segurança mistura validade estrutural com postura de segurança.

## Fontes

- kubeconform: <https://github.com/yannh/kubeconform>
