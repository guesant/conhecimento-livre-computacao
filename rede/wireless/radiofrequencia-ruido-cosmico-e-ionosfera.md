# Radiofrequência, ruído cósmico e ionosfera

Uma antena nunca recebe apenas o sinal desejado. Ela capta radiação natural do
céu, emissões solares, ruído térmico do próprio sistema, interferência de
outros transmissores e sinais refletidos ou espalhados pelo ambiente. O
receptor transforma parte dessa energia em um nível de ruído, e o que importa
para a comunicação é a relação entre sinal e ruído dentro da largura de banda
utilizada.

O termo "ruído de fundo do universo" reúne fenômenos diferentes. O fundo
cósmico de micro-ondas é uma radiação remanescente do universo primordial,
enquanto a emissão difusa da Via Láctea, fontes extragalácticas, o Sol e a
atmosfera contribuem de maneira diferente conforme a frequência e a direção da
antena. Em telecomunicações, também é necessário separar o ruído natural da
interferência produzida por pessoas e equipamentos.

## Ruído natural do céu

O fundo cósmico de micro-ondas, ou CMB, tem um espectro aproximadamente de
corpo negro com temperatura de 2,725 K. Seu máximo de potência por frequência
ocorre na região de micro-ondas, perto de 160 GHz, mas a radiação pode ser
medida em uma faixa mais ampla. Ele não é, por si só, a fonte dominante em
qualquer antena terrestre: em frequências mais baixas, a emissão síncrotron da
Galáxia e outras fontes do céu podem ser muito mais intensas.

Em radioastronomia, a direção para a qual a antena aponta importa. O plano da
Via Láctea costuma apresentar mais emissão difusa que regiões afastadas do
plano galáctico. Fontes compactas, como pulsares, quasares e remanescentes de
supernovas, podem aparecer sobre esse fundo. Uma medição de céu também inclui
lobos laterais da antena, perdas do cabo e o próprio ruído do amplificador.

O Sol acrescenta emissão variável. Além do brilho térmico, explosões solares
podem produzir rajadas de rádio em várias faixas. Uma rajada não é o mesmo que
o fundo cósmico: ela é uma fonte transitória que pode elevar o ruído recebido,
saturar um receptor ou degradar a relação sinal-ruído de um enlace.

Na engenharia de rádio, costuma-se representar a contribuição combinada por
uma temperatura de ruído. Essa temperatura não significa que todo o ruído seja
um corpo físico nessa temperatura. É uma forma de expressar a potência de
ruído equivalente na entrada do receptor. A potência térmica aproximada em uma
largura de banda `B` é dada por `kTB`, em que `k` é a constante de Boltzmann e
`T` reúne as contribuições do céu, da antena, do cabo e do receptor.

## Faixas de radiofrequência

A nomenclatura de frequência usada em telecomunicações divide o espectro em
faixas de uma década. A tabela abaixo segue a classificação tradicional da
UIT-R. A alocação de serviços, a potência permitida e o uso efetivo dependem
do país, da região e do plano nacional de frequências.

| Sigla | Nome em inglês | Faixa aproximada | Características comuns |
| --- | --- | --- | --- |
| ELF | Extremely Low Frequency | 3 a 30 Hz | estudos geofísicos, sinais de navegação e fenômenos de grande escala |
| SLF | Super Low Frequency | 30 a 300 Hz | aplicações muito específicas e pesquisa |
| ULF | Ultra Low Frequency | 300 Hz a 3 kHz | geofísica, comunicação especial e ruído de rede |
| VLF | Very Low Frequency | 3 a 30 kHz | navegação, sinais de tempo e comunicação com submarinos |
| LF | Low Frequency | 30 a 300 kHz | navegação, radiodifusão de ondas longas e balizas |
| MF | Medium Frequency | 300 kHz a 3 MHz | radiodifusão em ondas médias, navegação e serviços marítimos |
| HF | High Frequency | 3 a 30 MHz | ondas curtas, radioamadorismo, aviação, marítimo e comunicações de longa distância |
| VHF | Very High Frequency | 30 a 300 MHz | FM, aviação, rádio móvel, televisão e serviços marítimos |
| UHF | Ultra High Frequency | 300 MHz a 3 GHz | televisão, redes móveis, GNSS, Wi-Fi em 2,4 GHz e enlaces diversos |
| SHF | Super High Frequency | 3 a 30 GHz | radar, enlaces, Wi-Fi em 5 GHz, satélite e backhaul |
| EHF | Extremely High Frequency | 30 a 300 GHz | radar avançado, pesquisa, enlaces de alta capacidade e radioastronomia |

Algumas fontes também apresentam THF para frequências acima de 300 GHz. Os
limites nominais e os nomes de algumas faixas podem aparecer com pequenas
variações em documentos históricos, mas a recomendação da UIT é a referência
para a nomenclatura internacional.

## AM, FM, SW, HF e as siglas parecidas

AM e FM não são faixas de frequência. São formas de modulação:

- em AM, a amplitude da portadora varia de acordo com a informação;
- em FM, a frequência instantânea da portadora varia de acordo com a informação.

Uma transmissão AM pode existir em MF, HF ou outras faixas. FM é muito comum
na radiodifusão em VHF, mas também pode ser usada em sistemas móveis, enlaces
e telemetria em outras frequências. A escolha da modulação afeta largura de
banda, resistência a ruído, eficiência de potência e complexidade do receptor.

SW significa shortwave, ou ondas curtas. No uso de radiodifusão e de
radioamadorismo, o termo costuma apontar para a região de HF, de 3 a 30 MHz,
na qual a ionosfera pode permitir enlaces além do horizonte. SW não descreve
uma modulação específica: uma transmissão de ondas curtas pode usar AM, SSB,
CW, digital ou outra técnica.

HF é a sigla correta para High Frequency. `HW` não é a sigla padronizada para
essa faixa. `UF` também não substitui `UHF`: Ultra High Frequency é escrito
UHF. A diferença não é apenas ortográfica, porque as siglas fazem parte de
planos de frequência, normas de equipamentos e procedimentos de operação.

## Uso terrestre

Em terra, frequência, largura de canal, potência, antena e propagação precisam
ser analisadas juntas. Alguns exemplos de associação são:

| Faixa ou região | Usos frequentes | Observação de propagação |
| --- | --- | --- |
| LF e MF | balizas, navegação e radiodifusão em ondas longas ou médias | pode haver onda de superfície e, em determinadas condições, reflexão ionosférica |
| HF | ondas curtas, radioamadorismo, comunicações aeronáuticas e marítimas | pode usar reflexão ou refração na ionosfera para alcançar longas distâncias |
| VHF | radiodifusão FM, aviação, serviços móveis e marítimos | normalmente depende de linha de visada, mas relevo e condições atmosféricas alteram o alcance |
| UHF | televisão, redes móveis, segurança pública, GNSS e Wi-Fi em 2,4 GHz | antenas menores e maior capacidade, com mais sensibilidade a obstáculos conforme a frequência sobe |
| SHF | Wi-Fi em 5 GHz, enlaces ponto a ponto, radar e satélite | grande largura de banda, mas maior atenuação por obstáculos, oxigênio, chuva e cabos |

As faixas de radiodifusão são exemplos, não uma autorização de transmissão.
No Brasil, a Anatel define atribuição e condições de uso do espectro, e o
equipamento ou serviço pode exigir homologação, licença ou coordenação. Um
receptor pode ouvir uma frequência sem que o usuário tenha autorização para
transmitir nela.

## Frequências de satélite

Satélites usam bandas que atravessam a atmosfera e a ionosfera em direções de
subida e descida. A nomenclatura por letra, como L, S, C, X, Ku e Ka, é útil
para descrever famílias de aplicações, mas não substitui a frequência exata,
o plano de canal, a polarização ou a autorização do sistema.

| Banda | Faixa aproximada | Aplicações recorrentes |
| --- | --- | --- |
| VHF e UHF | dezenas de MHz a poucos GHz | telemetria, rastreio e comando de satélites pequenos, radioamadorismo e alguns serviços de observação |
| L | 1 a 2 GHz | GNSS, telefonia e dados móveis por satélite, navegação e serviços de baixa atenuação por chuva |
| S | 2 a 4 GHz | telemetria, rastreio e comando, meteorologia e comunicação móvel |
| C | 4 a 8 GHz | comunicação fixa por satélite e enlaces com boa resistência relativa à chuva |
| X | 8 a 12 GHz | observação da Terra, radar, pesquisa e missões governamentais ou científicas |
| Ku | 12 a 18 GHz | televisão, VSAT, conectividade e distribuição de conteúdo |
| Ka | 27 a 40 GHz | banda larga de alta capacidade, gateways e satélites de alto throughput |

As faixas de satélite variam conforme o regulamento, a região e a missão. Um
enlace costuma ter frequências diferentes para uplink e downlink, e pode usar
polarizações distintas para reaproveitar o espectro. Frequências maiores
permitem antenas menores e mais largura de banda, mas aumentam os desafios de
atenuação atmosférica, chuva, apontamento e estabilidade de osciladores.

VHF, UHF e L podem sofrer atrasos, rotação de polarização e cintilação
ionosférica. Em Ku e Ka, a chuva e a absorção troposférica frequentemente
dominam a margem do enlace, embora a ionosfera ainda possa importar em
determinados modos, latitudes e eventos solares.

## A ionosfera como meio de propagação

A ionosfera é uma região parcialmente ionizada da atmosfera superior. Sua
densidade de elétrons muda com a hora local, a estação, a atividade solar, a
latitude, o campo magnético e a ocorrência de tempestades geomagnéticas. Ela
não é uma parede uniforme que reflete todas as ondas.

As regiões D, E e F são uma forma útil de descrever camadas com comportamentos
distintos. A região D, mais baixa, pode absorver HF durante o dia. As regiões E
e F podem refratar ou refletir determinadas ondas, dependendo da frequência,
do ângulo de incidência e da densidade eletrônica. À noite, a recombinação
reduz algumas camadas e muda as condições do enlace.

Em HF, a onda pode retornar à superfície depois de interagir com a ionosfera,
criando comunicação além do horizonte. A frequência máxima utilizável, o
ângulo de incidência e o estado ionosférico determinam se um salto será
possível. Um enlace de ondas curtas pode desaparecer, mudar de intensidade ou
chegar por múltiplos caminhos, produzindo desvanecimento e distorção.

VLF e LF podem se propagar por um guia formado aproximadamente pela superfície
da Terra e pela ionosfera. VHF e frequências superiores normalmente atravessam
a ionosfera ou dependem de linha de visada, mas ainda podem sofrer eventos
como espalhamento, refração anômala e sporadic E. Em sinais de satélite, a
ionosfera pode introduzir atraso dependente da frequência, rotação de
polarização e cintilação de amplitude e fase.

GNSS é um exemplo prático. O receptor usa sinais em bandas L, e a densidade de
elétrons no caminho altera o tempo de propagação. Modelos, receptores de dupla
frequência e correções diferenciais ajudam a reduzir o erro. Durante atividade
solar intensa, cintilação e gradientes ionosféricos podem prejudicar aquisição,
rastreamento e precisão, sobretudo em regiões equatoriais e polares.

## Ruído, interferência e relação sinal-ruído

Ruído é uma contribuição indesejada que pode ser natural ou interna ao
receptor. Interferência é uma emissão de outro sistema que ocupa ou invade a
faixa utilizada. A distinção nem sempre é feita de modo estrito em uma
medição, mas ela muda a mitigação.

| Origem | Exemplo | Mitigação típica |
| --- | --- | --- |
| Cósmica | CMB, emissão galáctica e fontes extragalácticas | escolher frequência e largura de banda, orientar a antena e aumentar ganho útil |
| Solar | rajada de rádio durante evento solar | monitorar clima espacial, aumentar margem e usar diversidade ou outra faixa |
| Atmosférica | descargas elétricas e absorção por gases ou chuva | filtragem, diversidade, potência e planejamento de enlace |
| Terrestre natural | ruído térmico, fontes, motores e descargas próximas | aterramento, blindagem, filtros e separação física |
| Intencional ou acidental | outra estação, emissor defeituoso ou vazamento de oscilador | coordenação, análise de espectro, filtros, antena direcional e fiscalização |

Um filtro estreito pode melhorar a relação sinal-ruído ao excluir energia fora
do canal, mas não recupera informação já perdida dentro dele. Aumentar a
potência do transmissor também não resolve um receptor saturado ou um problema
de interferência muito próximo. Antena, polarização, diversidade espacial,
codificação, interleaving, modulação adaptativa e correção de erros fazem parte
da mesma decisão de enlace.

## Radioastronomia e silêncio de rádio

Observatórios precisam medir sinais extremamente fracos. Um transmissor local
pode ser muito mais intenso no receptor do observatório que uma fonte
astronômica distante, mesmo quando sua potência total parece pequena. Por isso
existem faixas protegidas, coordenação de frequência, zonas de silêncio, filtros
e políticas para evitar emissões próximas.

Satélites, radares, redes móveis, enlaces e constelações podem beneficiar a
conectividade, mas também aumentam o ambiente de interferência de
radioastronomia. A proteção exige observar potência irradiada, largura de
banda, emissões fora de faixa, lóbulos laterais, visibilidade do satélite e
tempo de exposição do instrumento.

## Como analisar um problema de rádio

Quando um enlace sofre quedas, não atribua automaticamente o problema à
ionosfera ou ao ruído cósmico. Meça o fenômeno e compare o horário e o local:

1. registre frequência central, largura de canal, modulação, polarização e
   potência recebida;
2. observe espectro, piso de ruído, saturação e relação sinal-ruído;
3. compare antena, cabo, conectores, alimentação e aterramento;
4. verifique chuva, relevo, obstruções, horário local e geometria do enlace;
5. consulte atividade solar, índice geomagnético e condições ionosféricas;
6. compare com outra frequência, outra polarização, outra antena ou outro
   caminho;
7. confira se a emissão está autorizada e se o equipamento é homologado.

Uma alteração simultânea em vários enlaces de HF pode indicar ionosfera ou
interferência ampla. Uma falha apenas em um cabo, conector ou rádio aponta para
um problema local. A evidência deve separar propagação, hardware, configuração
e ocupação do espectro.

## Relação com clima espacial

Rajadas solares, ejeções de massa coronal e tempestades geomagnéticas podem
alterar a ionosfera, induzir correntes em condutores longos e elevar a taxa de
falhas em alguns sistemas. Esses efeitos são relacionados, mas não idênticos.
Uma página específica sobre [clima espacial, indução e eletrônica](../../sistemas/hardware/clima-espacial-e-eletronica.md)
trata de correntes geomagneticamente induzidas, surtos conduzidos e erros de
bits em semicondutores.

## Fontes primárias

- [UIT-R V.431, nomenclatura das bandas de frequência](https://www.itu.int/rec/R-REC-V.431/en)
- [NASA LAMBDA, espectro do fundo cósmico de micro-ondas](https://lambda.gsfc.nasa.gov/education/lambda_graphics/cmb_monopole.html)
- [NOAA Space Weather Prediction Center, ionosfera](https://www.swpc.noaa.gov/phenomena/ionosphere)
- [NOAA, efeitos da ionosfera sobre sinais de rádio](https://www.swpc.noaa.gov/phenomena/ionospheric-scintillation)
- [Anatel, atribuição e destinação de radiofrequências](https://www.gov.br/anatel/pt-br/regulado/radiofrequencia/atribuicao-destinacao-e-distribuicao-de-radiofrequencias)
