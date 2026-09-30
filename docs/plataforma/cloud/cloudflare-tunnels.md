# Cloudflare Tunnel

Cloudflare Tunnel publica uma origem privada por meio de uma conexão iniciada pelo conector `cloudflared`. Em vez de abrir uma porta de entrada no roteador e encaminhar tráfego diretamente para o serviço, o conector estabelece uma conexão de saída até a rede da Cloudflare. As requisições recebidas pelo hostname são então encaminhadas para os serviços definidos na configuração do túnel.

Esse modelo é útil quando o serviço está atrás de NAT, firewall ou uma rede sem endereço público. Também pode reduzir a superfície de exposição de um laboratório, publicar uma aplicação temporariamente para testes e conectar aplicações privadas a uma política de acesso baseada em identidade.

## Componentes

Um túnel possui uma identidade e uma configuração de ingress que associa hostnames e caminhos a serviços internos. O `cloudflared` executa próximo da origem e precisa alcançar o destino local, como HTTP, HTTPS ou outro protocolo suportado pela configuração. A camada Cloudflare recebe a conexão pública e coordena o encaminhamento, enquanto o serviço original continua dentro da rede privada.

Tunnel e Access são conceitos relacionados, mas não equivalentes. Tunnel fornece conectividade. Access pode exigir identidade, política, grupo, postura do dispositivo ou service token antes de encaminhar o tráfego. Um túnel sem uma política de autenticação adequada não transforma uma aplicação administrativa em aplicação pública segura.

## Alta disponibilidade

Um único conector cria um ponto de falha. Para uma origem importante, execute conectores redundantes, distribua-os conforme os failure domains disponíveis e valide o comportamento durante a perda de um processo, de um nó e da conexão externa. A redundância do túnel não corrige uma origem que possui uma única réplica ou um banco indisponível.

O processo do conector deve ser tratado como infraestrutura: imagem e versão devem ser fixadas, credenciais devem ficar em um secret manager, logs devem ser coletados e atualizações devem ser testadas. Evite colocar tokens de túnel em repositórios, imagens públicas, scripts de inicialização ou logs.

## Casos apropriados

Tunnel funciona bem para publicar um serviço interno com DNS controlado, conectar um cluster ou laboratório sem abrir portas de entrada, proteger um painel com Access, testar webhooks e disponibilizar uma aplicação de desenvolvimento sem alterar o firewall residencial.

Para tráfego de produção sensível a latência, protocolos especiais ou requisitos de residência, verifique o caminho completo, os limites de conexão, a observabilidade e o contrato do serviço. Um proxy de terceiros adiciona uma dependência operacional e pode alterar a forma como origem, cliente e certificados são observados.

## Cuidados de segurança

A regra de ingress deve ser específica. Não encaminhe uma rede inteira quando apenas um serviço precisa ser publicado. Restrinja o serviço de destino, valide o host recebido, use autenticação na aplicação e aplique rate limiting quando o endpoint for público. Para SSH, bancos e interfaces administrativas, prefira acesso autenticado e políticas de identidade em vez de publicar uma porta genérica.

O túnel também não substitui segmentação de rede, NetworkPolicy, TLS entre serviços ou backup. Se o `cloudflared` for comprometido, o impacto depende dos destinos que sua identidade consegue alcançar; por isso, a conta de execução e a rede do conector devem ter o menor privilégio possível.

## Relação com outras opções

Cloudflare Tunnel se aproxima de ngrok, Tailscale Funnel, VPNs e reverse proxies, mas o modelo de identidade, a distribuição do conector e a forma de administrar DNS e políticas variam. A escolha depende de quem controla a borda, se o objetivo é publicação temporária ou permanente, e se a rede privada precisa ser alcançada por usuários autenticados ou por outras redes.

## Fontes primárias

- [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)
- [Visão geral dos conectores](https://developers.cloudflare.com/cloudflare-one/networks/connectors/)
- [Cloudflare Access](https://developers.cloudflare.com/cloudflare-one/applications/)
- [Configuração de ingress](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/local-management/ingress/)
