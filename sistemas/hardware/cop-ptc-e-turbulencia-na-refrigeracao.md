# COP, PTC e turbulência na refrigeração

Em sistemas de refrigeração, a expressão "coeficiente positivo" pode apontar
para assuntos diferentes. O primeiro é o coeficiente de performance, ou COP,
uma métrica termodinâmica. O segundo é o PTC, sigla de *Positive Temperature
Coefficient*, um componente cuja resistência elétrica aumenta com a temperatura
em determinada faixa de operação.

Turbulência é um terceiro assunto relacionado. Ela pode melhorar a transferência
de calor em evaporadores, condensadores e trocadores, mas também aumenta a perda
de carga. O projeto não deve tentar maximizar a turbulência isoladamente. Deve
buscar o melhor resultado para capacidade de refrigeração, consumo total,
pressão, ruído, confiabilidade e manutenção.

## Coeficiente de performance

Para um refrigerador ou ar-condicionado, o COP é a razão entre o calor removido
do ambiente frio e a energia fornecida ao sistema:

```text
COP_cooling = Q_L / W_in
```

`Q_L` é a taxa de calor retirada do lado frio e `W_in` é o trabalho ou a
potência de entrada, com unidades compatíveis. A definição pode incluir
compressor, ventiladores, bombas, controles e outros consumos, dependendo da
fronteira do sistema e da condição de ensaio.

O COP de refrigeração é positivo quando o equipamento está removendo calor do
ambiente de interesse e consumindo energia para realizar esse processo. Isso
não significa que ele seja sempre maior que um. Também não significa que COP
seja uma porcentagem: é uma razão adimensional. Um COP de 3 representa três
unidades de calor removidas para cada unidade de energia de entrada na fronteira
adotada.

Um COP acima de 1 não viola a conservação de energia. O compressor não está
criando calor removido. Ele está transferindo energia térmica de uma região fria
para uma região mais quente, usando trabalho externo. O condensador rejeita o
calor removido mais o trabalho fornecido:

```text
Q_H = Q_L + W_in
```

Em uma bomba de calor, a métrica pode ser calculada no modo de aquecimento:

```text
COP_heating = Q_H / W_in
```

Por isso, o mesmo equipamento pode ter COP de refrigeração e COP de aquecimento
diferentes. A comparação só é válida quando as condições de temperatura,
carga, fronteira de medição e acessórios são equivalentes.

### COP ideal e COP real

Para um ciclo reversível ideal, o COP de refrigeração de Carnot é:

```text
COP_Carnot = T_cold / (T_hot - T_cold)
```

As temperaturas são absolutas, em kelvin. A fórmula mostra por que reduzir a
diferença entre a temperatura de evaporação e a temperatura de condensação
tende a melhorar o desempenho ideal. Um sistema real fica abaixo desse limite
por causa de compressão não ideal, quedas de pressão, trocas térmicas finitas,
perdas elétricas, vazamentos, controle, formação de gelo e consumo de
ventiladores e bombas.

O COP também varia com a carga e com o ponto de operação. Comparar dois
aparelhos somente pelo COP nominal pode esconder diferença de temperatura
externa, condição de ensaio, carga parcial, degelo, consumo em espera e escopo
dos auxiliares.

## PTC e coeficiente de temperatura positivo

Um termistor PTC possui um coeficiente de temperatura positivo: sua resistência
aumenta quando sua temperatura sobe, especialmente na região característica do
componente. Essa propriedade pode ser usada para medir temperatura, limitar
corrente, controlar aquecimento, proteger motores ou formar um circuito de
partida.

O comportamento não deve ser confundido com a afirmação de que qualquer
resistência elétrica aumenta linearmente com a temperatura. Um PTC tem uma
curva própria, limites de corrente, dissipação, tempo de resposta e faixa de
operação. O projeto deve usar a curva e os dados do fabricante.

### PTC na partida do compressor

Em pequenos compressores herméticos, um PTC pode ser usado no circuito de
partida do motor. Durante a partida, a corrente aquece o componente. Conforme a
resistência aumenta, a corrente do enrolamento auxiliar diminui, retirando-o da
condição de partida e deixando o motor em regime.

Esse funcionamento cria uma dependência térmica. Se a alimentação for
interrompida e restabelecida antes de o PTC esfriar, ou se a pressão do sistema
não estiver equalizada, o compressor pode não conseguir partir. O protetor do
motor pode abrir o circuito e exigir um período de espera antes de permitir
nova tentativa.

Um PTC de partida não é automaticamente equivalente a um protetor térmico.
Um protetor térmico pode usar bimetal, sensor, eletrônica ou outra solução para
interromper o motor sob sobretemperatura ou sobrecorrente. No compressor, o PTC,
o protetor, o capacitor, a pressão e a lógica de controle podem formar um
sistema conjunto, mas cada componente tem uma responsabilidade diferente.

### PTC como sensor e proteção

Em uma aplicação de sensor, o controlador mede ou interpreta a resistência do
PTC para estimar temperatura. Em uma aplicação de proteção, o aumento de
resistência pode limitar corrente ou alterar o estado de um circuito. A
proteção só é válida se o circuito considerar curto, circuito aberto,
dissipação, tolerância, envelhecimento e falhas do próprio sensor.

Não se deve substituir um PTC por um resistor de valor parecido sem conferir a
curva, a potência, o tempo de resposta e o modo de falha. Também não se deve
testar um circuito de compressor diretamente na rede sem o esquema correto e
sem as precauções do fabricante.

## Turbulência a favor da refrigeração

Em um escoamento laminar, camadas próximas à parede podem trocar calor com
limitação causada pela camada-limite térmica. A turbulência mistura regiões do
fluido, transporta energia entre o núcleo e a parede e pode reduzir a espessura
efetiva dessa camada. O coeficiente convectivo de transferência de calor pode
aumentar.

Esse efeito pode ajudar em:

- evaporadores, ao melhorar a troca entre o refrigerante e a parede do tubo;
- condensadores, ao retirar calor do refrigerante ou do gás para o ambiente;
- serpentinas de ar, ao melhorar a mistura e o contato com aletas;
- trocadores compactos, ao aumentar a troca em uma área menor;
- escoamentos bifásicos, quando a distribuição das fases permanece controlada.

O ganho não vem de "agitar" o fluido de forma gratuita. Para produzir mais
turbulência, o sistema pode precisar de maior velocidade, superfícies rugosas,
aletas, defletores, curvas ou misturadores. Essas soluções aumentam a queda de
pressão e podem exigir mais potência de compressor, ventilador ou bomba.

## O compromisso entre troca de calor e perda de carga

Uma forma simplificada de representar a troca de calor é:

```text
Q = U A DeltaT_lm F
```

`U` representa o coeficiente global, `A` a área de troca, `DeltaT_lm` a
diferença média logarítmica de temperatura e `F` um fator de correção da
configuração. A turbulência pode aumentar uma parcela de `U`, mas não garante
que `Q` ou o COP do equipamento também aumentarão na mesma proporção.

O escoamento também produz uma queda de pressão. Em uma instalação com
ventilador ou bomba, essa queda se transforma em potência adicional. Em um
circuito de refrigerante, uma queda excessiva pode reduzir a pressão de
evaporação, aumentar a razão de compressão, alterar o superaquecimento ou
sub-resfriamento e reduzir o COP. No lado do ar, um ventilador mais potente
pode consumir o ganho obtido na serpentina.

O objetivo de projeto é otimizar uma função de custo que inclua pelo menos:

| Métrica | O que observar |
| --- | --- |
| Capacidade térmica | calor transferido na condição de projeto e em carga parcial |
| COP do sistema | compressor, ventiladores, bombas, controles e degelo quando aplicável |
| Queda de pressão | lado do refrigerante, ar, água ou outro fluido |
| Distribuição | regiões sem fluxo, bypass, recirculação e maldistribuição entre circuitos |
| Confiabilidade | vibração, erosão, ruído, fadiga, congelamento e sujeira |
| Manutenção | acesso, limpeza, risco de entupimento e sensibilidade a incrustação |

## Reynolds, Nusselt e projeto

O número de Reynolds ajuda a comparar a influência relativa de inércia e
viscosidade no escoamento. O regime não depende apenas de uma etiqueta fixa:
geometria, rugosidade, entrada, curvatura, temperatura e propriedades do
fluido também importam.

O número de Nusselt relaciona transferência convectiva com condução através de
uma camada de referência. Correlações de Nusselt normalmente usam Reynolds,
Prandtl, geometria e condições de contorno. Em escoamentos turbulentos, a
correlação precisa corresponder ao tubo, à superfície, ao fluido, ao regime e ao
intervalo de operação reais.

Algumas estratégias para aumentar a troca de calor sem simplesmente elevar a
velocidade são:

- aletas e superfícies expandidas, principalmente no lado do ar;
- microcanais e passagens compactas, quando a fabricação e a manutenção forem adequadas;
- defletores e geometrias que gerem vórtices controlados;
- circuitos paralelos bem distribuídos, evitando que um único canal concentre a vazão;
- superfícies texturizadas ou onduladas, com validação da perda de carga;
- controle de ventiladores e bombas conforme a carga, evitando potência constante desnecessária.

Uma solução pode aumentar o coeficiente local e ainda piorar o resultado
global. A validação deve medir capacidade, temperaturas, pressões, vazão,
potência elétrica e estabilidade, em vez de observar apenas a temperatura de
um ponto.

## Turbulência em escoamento bifásico

Evaporadores e condensadores frequentemente trabalham com líquido e vapor ao
mesmo tempo. Nesse caso, a turbulência não é apenas uma propriedade de um
fluido homogêneo. Padrões como fluxo estratificado, anular, em bolhas ou em
slug alteram a área molhada, o coeficiente de troca, a queda de pressão e a
distribuição do refrigerante.

Uma geometria que melhora a mistura em um trecho pode aumentar o arraste de
líquido, criar instabilidade, favorecer retorno de óleo ou prejudicar o
distribuidor. O projeto deve avaliar o circuito completo, incluindo entrada,
saída, retorno de óleo, controle de expansão e proteção do compressor.

## Como pensar sobre as três ideias juntas

COP, PTC e turbulência atuam em camadas diferentes:

| Conceito | Camada | Pergunta |
| --- | --- | --- |
| COP | desempenho termodinâmico | quanto efeito útil de refrigeração o sistema entrega por energia de entrada? |
| PTC | componente elétrico e controle | como a resistência varia com temperatura e como isso altera partida, medição ou proteção? |
| Turbulência | transporte de calor e quantidade de movimento | como melhorar a troca sem pagar mais potência e perda de carga do que o ganho vale? |

Melhorar o fluxo pode aumentar a capacidade, mas o compressor pode consumir
mais. Um PTC pode proteger ou controlar a partida, mas pode impedir uma nova
partida enquanto ainda estiver quente. Um COP alto pode ocorrer em uma condição
nominal restrita e não representar o consumo anual. Cada decisão precisa ser
avaliada dentro da fronteira e do regime de operação corretos.

## Fontes

- [ASHRAE Handbook, ciclos de termodinâmica e refrigeração](https://handbook.ashrae.org/Handbooks/F17/IP/f17_ch02/f17_ch02_ip.aspx)
- [ASHRAE Terminology, coefficient of performance](https://terminology.ashrae.org/?term=coefficient%20of%20performance)
- [TDK Electronics, termistores PTC](https://www.tdk-electronics.tdk.com/en/180382/tech-library/publications/protection-devices/ptc-thermistors/173670)
- [Danfoss, compressores e dispositivos de partida PTC](https://assets.danfoss.com/documents/latest/27738/AN000086421812en-000101.pdf)
- [NIST, transferência de calor em escoamento turbulento de CO2](https://www.nist.gov/publications/heat-transfer-turbulent-supercritical-carbon-dioxide-flowing-heated-horizontal-tube)
- [Department of Energy, troca de calor e perda de pressão](https://arpa-e-foa.energy.gov/FileContent.aspx?FileID=ae70544d-9498-4574-a894-e5087b43e90f)
