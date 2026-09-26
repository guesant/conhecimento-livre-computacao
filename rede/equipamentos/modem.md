# Modem

Modem é o equipamento que modula e demodula sinais para transportar dados por um meio de acesso. O termo vem de modulador e demodulador. A função está entre o dispositivo do assinante e a rede de acesso do provedor.

## Onde ele aparece

Há modems para diferentes meios, incluindo linhas telefônicas, cabo coaxial, rádio e outros sistemas de acesso. Em redes de fibra, é comum utilizar uma ONT ou ONU, que realiza a terminação óptica e apresenta uma interface para a rede interna. Produtos comerciais podem chamar o equipamento de modem mesmo quando a tecnologia não usa modulação no sentido tradicional de um modem telefônico.

Em uma arquitetura HFC, por exemplo, o cable modem conversa com um CMTS na rede do provedor. O modem do assinante não é o backbone, o roteador de borda ou o servidor de aplicação. Ele termina uma tecnologia de acesso e entrega conectividade ao próximo equipamento.

## Modem em bridge e modo roteado

No modo bridge, o modem passa a conexão para um roteador separado. O roteador recebe o endereço ou a sessão do provedor e concentra NAT, firewall, DHCP e Wi-Fi, se essas funções estiverem nele.

No modo roteado, o próprio equipamento executa funções de camada 3 e pode criar uma rede privada para os dispositivos locais. Se um segundo roteador também fizer NAT, surge uma configuração de NAT duplo, que pode afetar encaminhamento de portas, VPNs, jogos e descoberta de serviços.

## Diagnóstico

Sincronização, potência, erros do enlace e estado de autenticação pertencem ao caminho entre o modem e o provedor. Endereço IP local, rota padrão, DNS e regras de firewall pertencem a camadas posteriores. Separar esses sinais evita alterar o Wi-Fi para resolver uma falha de sinal no meio de acesso.

## Fontes primárias

- [ITU-T E.681, arquitetura de acesso baseada em cabo modem](https://www.itu.int/rec/T-REC-E.681)
- [ITU-T G.9711, acesso de banda larga em pares metálicos e coaxiais](https://www.itu.int/epublications/publication/itu-t-g-9711-2021-cor-1-2022-12)
