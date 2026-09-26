# Topologias de rede

Topologia descreve como os nós e enlaces de uma rede se relacionam. Há uma
topologia física, que trata de cabos, rádios, portas e disposição dos
equipamentos, e uma topologia lógica, que trata de como os dados percorrem os
domínios de enlace e as redes roteadas. As duas podem ser diferentes.

Uma sala pode ter vários cabos ligados a um switch central, formando uma
estrela física, enquanto VLANs, roteamento e overlays criam várias topologias
lógicas sobre o mesmo equipamento. Da mesma forma, uma rede mesh sem fio pode
usar uma infraestrutura cabeada em estrela para alcançar o gateway.

## Topologias físicas e lógicas

| Topologia | Organização | Vantagens | Limitações e falhas |
| --- | --- | --- | --- |
| Ponto a ponto | um enlace liga dois nós | simples, previsível e fácil de diagnosticar | não escala para muitos participantes |
| Estrela | todos os nós ligam a um ponto central | expansão e isolamento de portas simples | o ponto central é um domínio de falha |
| Barramento | vários nós compartilham o mesmo meio | pouco cabeamento em redes antigas | colisões, alcance e falha do meio afetam vários nós |
| Anel | cada nó liga ao próximo, fechando um circuito | caminho previsível e possibilidade de redundância | falha ou erro de configuração pode interromper o anel |
| Árvore | estrelas hierárquicas ligadas por níveis | organização e agregação | falhas ou saturação no nível superior afetam ramos |
| Malha | nós possuem vários caminhos entre si | redundância e caminhos alternativos | custo, complexidade e necessidade de evitar loops |
| Híbrida | combina duas ou mais formas | adapta-se ao cenário real | exige documentação das fronteiras e dos domínios de falha |

## Estrela

É a topologia dominante em redes Ethernet modernas. Hosts ligam a switches de
acesso, switches de acesso ligam a distribuição e a distribuição liga ao
núcleo ou ao roteador. A hierarquia pode formar uma árvore ou uma estrela de
estrelas.

A falha de um cabo geralmente afeta um host, mas a falha do switch central
afeta todos os equipamentos que dependem dele. Redundância pode ser obtida
com dois switches, links agregados, fontes independentes e caminhos de
roteamento, mas só existe de fato se o desenho evitar um domínio único de
falha.

## Barramento e anel

Barramentos foram comuns em Ethernet coaxial e em outros meios compartilhados.
Hoje aparecem mais como herança, redes industriais específicas ou modelos
conceituais. Um único meio compartilhado torna o diagnóstico e a expansão
mais difíceis.

No anel, o tráfego pode seguir um sentido ou usar mecanismos de proteção para
isolar um enlace quebrado. Anéis são usados em algumas redes metropolitanas,
industriais e de transporte, mas não devem ser tratados como uma simples
ligação circular de switches sem controle de loops e convergência.

## Árvore e spine-leaf

Árvore organiza acesso, distribuição e núcleo. Ela é simples de explicar, mas
pode concentrar tráfego em uplinks e equipamentos intermediários. Em um
data center, a topologia spine-leaf cria vários caminhos entre leafs e spines,
com cada leaf ligado a todos os spines aplicáveis. Ela se aproxima de uma
malha parcial e é analisada com ECMP, capacidade, latência e domínio de falha.

## Malha e ponto-multiponto

Uma malha pode ser completa, quando todos os nós têm enlaces entre si, ou
parcial, quando apenas alguns caminhos alternativos existem. Redes mesh sem
fio podem usar múltiplos saltos de rádio; redes roteadas podem criar uma malha
de túneis; redes de provedores podem usar rádios ponto-multiponto.

Mais caminhos não significam automaticamente mais disponibilidade. É preciso
definir descoberta, seleção de caminho, prevenção de loops, convergência,
capacidade compartilhada, autenticação e comportamento quando um nó está
isolado. Em rádio, cada salto pode consumir airtime e reduzir a capacidade
disponível aos clientes.

## Topologia lógica

VLANs dividem domínios de broadcast sobre switches físicos. Roteamento de
camada 3 cria domínios separados e controla a passagem entre eles. VPNs e
overlays podem formar uma rede lógica sobre uma infraestrutura que possui
outra disposição física. Em Kubernetes, CNI, Service, Gateway e mesh também
criam caminhos lógicos que não correspondem a uma porta física individual.

## Critérios de escolha

Escolha a topologia a partir de capacidade, distância, disponibilidade,
manutenção, custo, crescimento, segurança, domínio de falha e habilidade da
equipe. Documente os caminhos primários e alternativos, os pontos de
agregação, as dependências de energia e os equipamentos que precisam ser
recuperados primeiro.

Uma topologia resiliente não é apenas aquela que possui cabos duplicados. Ela
precisa de protocolos de convergência, configuração testada, monitoramento,
peças ou substitutos disponíveis e um procedimento de recuperação que a equipe
consiga executar sob pressão.

## Relações

- [Redes mesh](../wireless/mesh.md) trata a malha sem fio com mais detalhe.
- [VLAN](../fundamentos/vlan.md) trata segmentação lógica no enlace.
- [Roteamento](../roteamento/index.md) trata caminhos entre redes.
- [Categorias de cabos](../cabeamento/categorias-de-cabos.md) trata o meio
  físico cabeado.

## Fontes primárias

- [IEEE 802.1 Working Group](https://www.ieee802.org/1/)
- [IEEE 802.3 Ethernet Working Group](https://ieee802.org/3/)
- [IEEE 802.11 Working Group](https://www.ieee802.org/11/)
