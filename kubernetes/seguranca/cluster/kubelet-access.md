# Acesso seguro ao Kubelet

O Kubelet é o agente que executa Pods no nó, conversa com o container runtime,
monta volumes e reporta estado ao API server. Além da reconciliação local, ele
expõe endpoints HTTPS de operação e diagnóstico. Esses endpoints podem
permitir ações muito mais fortes que uma simples consulta de status, por isso
o Kubelet deve ser tratado como uma superfície administrativa do nó.

## Por que o endpoint é sensível

Uma identidade com acesso amplo ao Kubelet pode obter informações de Pods,
consultar métricas e, dependendo da configuração e do endpoint, executar
operações no contexto do runtime. O risco não é reduzido por o Kubelet estar
em uma rede interna. Um Pod comprometido, uma máquina da rede de gestão ou um
proxy mal configurado pode alcançar a porta.

A porta somente leitura legada não fornece uma fronteira de autenticação
adequada. Ela deve permanecer desabilitada. O endpoint seguro deve ser o único
caminho de gestão e deve aceitar apenas identidades e redes necessárias.

## Autenticação

O Kubelet pode autenticar clientes por certificado de cliente e por webhook de
autenticação que consulta o API server. O mecanismo escolhido precisa ser
compatível com a forma como operadores, métricas e ferramentas de diagnóstico
acessam o nó. Habilitar o webhook sem garantir conectividade ao API server pode
transformar uma mudança de segurança em uma indisponibilidade operacional.

Uma configuração baseada em bearer token deve validar issuer, audience,
expiração e origem. Tokens compartilhados entre vários componentes tornam a
revogação e a atribuição de responsabilidade difíceis. Certificados precisam
ter finalidade, autoridade e período de validade definidos, além de um
procedimento de rotação.

## Autorização

Autenticar um cliente não significa permitir todos os endpoints. O modo de
autorização do Kubelet deve aplicar decisões baseadas na identidade e na ação
solicitada. Em produção, a autorização por webhook é a opção que integra o
Kubelet ao modelo de autorização do cluster e evita confiar apenas em um
modo anônimo ou permissivo.

Um exemplo conceitual de configuração do Kubelet é:

```yaml
authentication:
  anonymous:
    enabled: false
  webhook:
    enabled: true
authorization:
  mode: Webhook
readOnlyPort: 0
```

Os campos devem ser aplicados na forma suportada pela versão e pela
distribuição. Não copie esse trecho para substituir a configuração gerada por
K3s, kubeadm ou outro distribuidor sem conferir o arquivo de configuração e o
processo de inicialização utilizado pelo ambiente.

## Rede e firewall

O acesso ao Kubelet deve ser permitido somente a API servers e ferramentas
explicitamente necessárias. NetworkPolicy pode proteger tráfego de Pods, mas
não substitui firewall do nó e pode não cobrir interfaces de host, Pods com
`hostNetwork` ou caminhos controlados diretamente pelo CNI. A proteção deve
ser aplicada no firewall do sistema, nas regras do cloud e no desenho das
sub-redes.

Não publique a porta do Kubelet por um LoadBalancer, Ingress, Gateway ou
proxy reverso. Um proxy que encaminha a porta sem preservar autenticação,
validação de certificado e origem pode criar uma nova superfície equivalente
à porta original.

## Diagnóstico sem relaxar a segurança

Quando um componente não consegue consultar o Kubelet, confirme o endereço e
a porta, a rota, o firewall, a autoridade do certificado, o token ou
certificado do cliente e a decisão de autorização. Verifique também se o
cliente está tentando usar o endpoint de leitura desabilitado.

Não habilite acesso anônimo como diagnóstico temporário em produção. Colete
logs do Kubelet, eventos do Node e os logs do API server, teste uma identidade
específica e reverta a alteração imediatamente se uma exceção controlada for
inevitável.

## Relações

- [Kubelet](../../control-plane/kubelet.md) explica a reconciliação local.
- [Acesso ao API server](api-access.md) explica a identidade do componente.
- [RBAC](../../access/rbac.md) trata a autorização do API server.
- [Node authorizer](https://kubernetes.io/docs/reference/access-authn-authz/node/)
  descreve a identidade de nó.
- [NetworkPolicy](../../networking/network-policy.md) limita tráfego de Pods,
  mas não substitui o firewall do host.

## Fonte primária

- [Kubelet authentication and authorization](https://kubernetes.io/docs/reference/access-authn-authz/kubelet-authn-authz/)
