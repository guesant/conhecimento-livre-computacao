# Tailscale

Tailscale é uma rede overlay baseada em WireGuard que conecta dispositivos por identidade, sem exigir que cada participante tenha um endereço público ou que a rede local exponha portas de entrada. O cliente cria uma interface virtual, autentica o dispositivo num plano de controle e tenta estabelecer caminhos diretos entre os participantes.

## Plano de controle e plano de dados

O plano de controle distribui identidade, chaves públicas, endereços da rede overlay, políticas de acesso e informações necessárias para a descoberta dos participantes. Ele coordena a rede, mas não precisa transportar todo o tráfego de dados.

O plano de dados usa WireGuard entre os dispositivos. Quando NAT ou firewalls impedem um caminho direto, a rede pode recorrer a mecanismos de relay, como servidores DERP. O relay facilita a conectividade, mas pode aumentar latência e custo de transferência; por isso, vale observar quando os caminhos são diretos e quando dependem de relay.

## Identidade e políticas

O acesso não deve ser modelado apenas como pertencimento à rede. As políticas ACL e as regras de postura definem quais identidades podem iniciar conexões para quais dispositivos, portas e grupos. A autenticação do dispositivo e a autorização do fluxo são decisões diferentes: um dispositivo pode estar autenticado sem receber acesso amplo.

Use grupos para expressar funções, tags para representar dispositivos administrados por automação e regras específicas para serviços sensíveis. O princípio de menor privilégio continua valendo dentro da rede overlay. Logs de conexão e mudanças de política devem fazer parte da investigação de incidentes.

## Subnet routers e exit nodes

Um dispositivo pode anunciar uma rede privada como subnet router. Isso permite alcançar hosts que não executam o cliente, mas amplia o domínio de confiança para todos os destinos anunciados. As rotas devem ser específicas, autorizadas e monitoradas.

Um exit node encaminha o tráfego geral de um cliente por outro dispositivo. Ele pode ser útil em redes não confiáveis ou quando um endereço de saída específico é necessário, mas concentra visibilidade, disponibilidade e risco de abuso. Não use um exit node como substituto automático para segmentação ou autorização na aplicação.

## DNS e descoberta

MagicDNS associa nomes aos dispositivos da rede overlay e reduz a necessidade de manter endereços manualmente. Isso simplifica a descoberta, mas torna o serviço de nomes parte da superfície de disponibilidade e privacidade. Separe nomes usados para administração de nomes publicados para aplicações e não trate resolução de nome como prova de autorização.

## Limites e alternativas

Tailscale não elimina a necessidade de firewall, TLS, autorização de aplicação, atualização dos clientes, backup ou observabilidade. Também não é equivalente a uma VPN site-to-site tradicional em todos os cenários: uma VPN pode conectar redes inteiras sob uma política de roteamento central, enquanto uma rede overlay orientada a identidade costuma oferecer controle mais granular entre dispositivos.

Compare Tailscale com WireGuard configurado diretamente, Headscale, NetBird, ZeroTier, VPNs baseadas em IPsec e serviços de acesso privado. Considere quem controla o plano de controle, onde ficam os metadados, como ocorre a recuperação de identidade, se há dependência de relay e como as políticas são auditadas.

## Fontes primárias

- [Tailscale documentation](https://tailscale.com/kb/)
- [ACLs and grants](https://tailscale.com/kb/1018/acls/)
- [Subnet routers](https://tailscale.com/kb/1019/subnets/)
- [Exit nodes](https://tailscale.com/kb/1103/exit-nodes/)
- [DERP relay servers](https://tailscale.com/kb/1232/derp-servers/)
