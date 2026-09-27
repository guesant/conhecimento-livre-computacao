# No-IP

No-IP é um provedor de serviços que inclui DNS dinâmico. Seu uso mais comum é
associar um hostname a um endereço IP residencial ou de laboratório que muda
ao longo do tempo. O nome permanece estável para quem precisa alcançar o
serviço, enquanto um cliente de atualização informa ao provedor o endereço
atual.

## Componentes do uso

Uma composição típica possui:

- uma conta e um hostname administrados no serviço;
- um agente Dynamic Update Client, o DUC, em um host ou roteador;
- uma conexão de saída para o serviço de atualização;
- um registro DNS que aponta para o endereço público atual;
- um serviço local configurado para responder ao hostname.

O agente pode consultar o endereço observado na Internet ou receber essa
informação do equipamento de borda. Quando identifica uma alteração, envia
uma atualização autenticada. A frequência, o método de autenticação e as
opções disponíveis dependem do cliente e do plano utilizado.

## O que validar no desenho

Antes de escolher No-IP, confirme:

1. se o provedor de Internet entrega um endereço alcançável ou usa CGNAT;
2. se o roteador suporta o método de atualização necessário;
3. se IPv4, IPv6 ou ambos precisam ser publicados;
4. qual TTL é aceitável para a mudança de endereço;
5. se o hostname será usado somente para VPN, para um proxy ou para um
   serviço diretamente exposto;
6. como o certificado TLS será emitido e renovado;
7. como a credencial de atualização será armazenada e rotacionada.

No-IP só atualiza o nome. Port forwarding, firewall, autenticação, autorização
e hardening continuam sendo responsabilidades do ambiente publicado. Um
hostname atualizado não transforma um serviço interno em um serviço seguro.

## DUC, roteador ou agente próprio

Executar o cliente no roteador reduz dependências no host que publica a
aplicação. Executá-lo em um servidor pode ser necessário quando o roteador não
tem suporte adequado ou quando o endereço observado precisa ser interpretado
por uma lógica específica.

O agente deve ser executado com a menor permissão possível e deve falhar de
forma observável. Uma atualização repetida a cada intervalo fixo sem comparar o
valor anterior pode criar tráfego e ruído desnecessários. Falhas de DNS,
expiração de credencial, alteração da interface WAN e indisponibilidade
temporária do provedor precisam aparecer em logs e alertas.

## Limitações e alternativas

Se o requisito é acesso administrativo privado, uma VPN ou um túnel de saída
pode ser mais adequado do que publicar portas com DDNS. Se o requisito é
balanceamento ou failover, use um serviço de DNS e uma arquitetura que
suportem health checks e retirada de endpoints. Se o requisito é somente
descoberta interna, split-horizon DNS pode evitar que o tráfego atravesse a
Internet.

No-IP é uma implementação de serviço DDNS. A decisão deve começar pelo modelo
de conectividade, não pelo nome do provedor.

## Fontes

- [No-IP, Dynamic DNS](https://www.noip.com/support/knowledgebase/what-is-dynamic-dns)
- [No-IP, configuração de DDNS no roteador](https://www.noip.com/support/knowledgebase/how-to-configure-ddns-in-router/)
- [DNS dinâmico](ddns.md)
- [Split-horizon DNS](split-horizon.md)
