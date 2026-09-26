# ngrok

ngrok é uma plataforma de ingress e tunelamento que cria endpoints públicos para serviços alcançáveis a partir de uma máquina local ou de uma rede privada. Um agente, SDK ou conector inicia uma conexão de saída com a infraestrutura do ngrok; as requisições recebidas no endpoint são encaminhadas ao serviço configurado. Isso permite testar webhooks, compartilhar uma aplicação local, demonstrar uma interface ou investigar uma integração sem publicar diretamente o endereço da rede doméstica.

## Modelo de uso

O agente deve ser executado próximo do serviço, com uma configuração que identifique o protocolo, a porta e as políticas do endpoint. Para HTTP e HTTPS, o serviço pode receber um hostname público e metadados encaminhados pelo proxy. Outros protocolos, como TCP, dependem do tipo de endpoint, do plano e da configuração escolhida.

O túnel resolve conectividade, não a lógica da aplicação. A aplicação ainda precisa autenticar usuários, autorizar ações, validar payloads, proteger contra replay e registrar o correlation ID. Um endpoint temporário continua sendo um endpoint público e deve ser considerado hostil desde o primeiro request.

## Casos adequados

ngrok é particularmente útil para receber callbacks de provedores que exigem uma URL pública, testar OAuth localmente, inspecionar uma integração com pagamentos ou mensageria, compartilhar uma revisão com alguém e reproduzir problemas que só acontecem quando a aplicação está atrás de uma rede externa.

Ele também pode apoiar desenvolvimento remoto, mas não deve ser confundido com uma rede privada entre usuários ou com alta disponibilidade de produção. Para publicar um serviço por longos períodos, avalie domínio estável, controle de acesso, logs, limites de tráfego, custo, redundância e o impacto de depender de um intermediário externo.

## Segurança

Nunca exponha uma porta apenas porque o processo está escutando localmente. Restrinja o endpoint ao serviço necessário, use autenticação ou políticas de acesso, remova o túnel quando o teste terminar e não encaminhe painéis administrativos, bancos ou interfaces de gerenciamento sem uma camada adicional de identidade.

Tokens e credenciais do agente devem ser armazenados fora do repositório e injetados com o menor privilégio possível. Os logs de inspeção podem conter dados sensíveis, tokens, cookies e payloads pessoais; retenção e acesso precisam ser tratados como parte da superfície de segurança.

## Diagnóstico

Quando um webhook não chega, separe as camadas: o provedor resolveu o hostname, o endpoint do ngrok aceitou a conexão, a política permitiu a requisição, o agente manteve o túnel, a máquina alcançou a porta local e a aplicação respondeu corretamente. Essa decomposição evita atribuir ao túnel um erro causado por firewall local, rota, TLS de origem ou código da aplicação.

## Relação com outras opções

ngrok se relaciona a Cloudflare Tunnel, Tailscale Funnel, VPNs e reverse proxies. A diferença mais relevante é o objetivo operacional. ngrok costuma ser escolhido pela rapidez de criar um endpoint para desenvolvimento e integração. Cloudflare Tunnel pode se integrar a DNS, Access e redes privadas. Uma VPN cria conectividade entre redes ou identidades, mas não necessariamente oferece um endpoint público pronto para webhook.

## Fontes primárias

- [Documentação do ngrok](https://ngrok.com/docs/start)
- [Endpoints e agentes](https://ngrok.com/docs/using-ngrok/)
- [Políticas de tráfego](https://ngrok.com/docs/traffic-policy/)
- [Segurança do ngrok](https://ngrok.com/docs/guides/security/)
