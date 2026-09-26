# Categorias de cabos de rede

Categoria é uma classificação de desempenho elétrico do sistema de
cabeamento balanceado. Ela não é o mesmo que velocidade Ethernet. A velocidade
depende também do transceptor, comprimento, instalação, conectores, ruído,
temperatura, diafonia e do padrão IEEE usado.

## Categorias comuns

| Categoria | Frequência de referência | Uso comum | Observações |
| --- | --- | --- | --- |
| Cat 3 | até 16 MHz | telefonia e instalações antigas | não é escolha para uma LAN moderna |
| Cat 5 | até 100 MHz | legado | foi substituída na prática por Cat 5e |
| Cat 5e | até 100 MHz | 1000BASE-T, PoE e acesso comum | também pode atender 2,5GBASE-T e alguns cenários 5GBASE-T |
| Cat 6 | até 250 MHz | acesso de maior margem e 1 Gb/s | 10GBASE-T pode ser limitado pelo comprimento e pela instalação |
| Cat 6A | até 500 MHz | 10GBASE-T em até 100 m de canal compatível | reduz risco de diafonia alienígena em instalações adequadas |
| Cat 7 | até 600 MHz | cabeamento blindado de maior desempenho | classificação principalmente ISO/IEC, não deve ser confundida com uma porta Ethernet |
| Cat 7A | até 1000 MHz | instalações ISO/IEC de frequência mais alta | custo e conectividade precisam ser justificados |
| Cat 8 | até 2000 MHz | 25GBASE-T e 40GBASE-T em distâncias curtas | voltada principalmente a data centers e canais de até 30 m |

Os limites de frequência não garantem a mesma taxa em qualquer distância. A
instalação deve ser especificada como canal, enlace permanente, cabo, patch
cord e conectores compatíveis. Misturar componentes de classes diferentes pode
reduzir o desempenho para o menor componente ou invalidar a certificação.

## Condutor e blindagem

Cabo sólido é usado em enlaces permanentes; cabo flexível trançado é comum em
patch cords. CCA, uma mistura com alumínio revestido de cobre, não equivale ao
cobre sólido exigido por instalações de cabeamento estruturado e pode causar
perdas, aquecimento e problemas de PoE.

UTP não possui blindagem individual ou geral. F/UTP, U/FTP, F/FTP e S/FTP
possuem combinações diferentes de blindagem. A blindagem só ajuda quando
conectores, patch panels, racks e aterramento formam um sistema coerente.

## Ethernet e PoE

Cat 5e ou superior costuma atender Ethernet de 1 Gb/s e alimentação PoE em
instalações compatíveis. Para 10 Gb/s, Cat 6A oferece uma margem mais clara
para 100 m. PoE aquece feixes de cabos, e o projeto precisa considerar
categoria, agrupamento, temperatura, corrente e classe da fonte. A tabela de
um switch não substitui a verificação do canal inteiro.

## Boas práticas

- separar energia e dados conforme a norma aplicável;
- respeitar raio de curvatura e força de tração;
- não exceder o comprimento máximo do canal;
- identificar as duas pontas e documentar o patch panel;
- certificar o enlace com equipamento apropriado;
- não comprar Cat 8 para uma rede que não possui portas ou distância que usem
  esse recurso;
- especificar a norma de cabeamento, a categoria e o tipo de blindagem no
  projeto, em vez de confiar apenas no nome comercial do cabo.

## Fontes primárias

- [IEEE 802.3 Ethernet Working Group](https://ieee802.org/3/)
- [ISO/IEC JTC 1/SC 25](https://www.iso.org/committee/45342.html)
- [TIA standards](https://www.tiaonline.org/standards/)
