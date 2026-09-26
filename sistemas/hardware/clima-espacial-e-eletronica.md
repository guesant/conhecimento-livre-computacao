# Clima espacial, indução e erros em eletrônica

Atividade solar pode afetar sistemas tecnológicos por mecanismos diferentes. A expressão "onda solar" é imprecisa: o Sol emite radiação eletromagnética, vento solar e partículas energéticas; ejeções de massa coronal podem alterar a magnetosfera terrestre e produzir tempestades geomagnéticas. Cada fenômeno interage com a infraestrutura de uma forma diferente.

É importante separar duas situações que às vezes são tratadas como se fossem a mesma coisa:

- uma variação do campo magnético terrestre pode induzir tensão e corrente em condutores extensos;
- uma partícula energética pode depositar carga dentro de um semicondutor e alterar o estado de uma célula de memória ou de um flip-flop.

Uma gaiola condutora não é uma proteção universal contra atividade solar. Ela pode atenuar campos elétricos e sinais eletromagnéticos em determinadas faixas de frequência, mas não bloqueia automaticamente campos magnéticos quase estáticos, correntes que entram por cabos ou partículas ionizantes de alta energia.

## Indução em fios e cabos

Pela lei de Faraday, uma variação do fluxo magnético produz um campo elétrico induzido. Em uma forma simplificada, a tensão ao longo de um caminho condutor depende da integral do campo elétrico nesse caminho. Quanto maior o comprimento efetivo do condutor e quanto mais rápida ou intensa for a variação geomagnética, maior pode ser a diferença de potencial acumulada entre seus extremos.

Durante uma tempestade geomagnética, correntes na ionosfera e na magnetosfera modificam o campo magnético observado na superfície. O campo geoeletromagnético resultante pode criar correntes geomagneticamente induzidas, conhecidas como GICs. Elas tendem a ter comportamento quase contínuo em relação à frequência normal da rede elétrica, embora a perturbação possa variar em escalas de segundos a minutos.

O efeito é mais relevante em caminhos longos e aterrados, como linhas de transmissão, cabos de comunicação, oleodutos e gasodutos. Um fio curto dentro de um computador não costuma formar uma antena ou um caminho suficientemente longo para reproduzir o cenário de uma linha de transmissão. O risco não é determinado apenas pelo material do fio, mas pelo comprimento, pela orientação, pela topologia de aterramento, pela resistividade do solo e pela rede à qual ele está conectado.

Em transformadores, uma corrente contínua ou quase contínua sobreposta à corrente alternada pode deslocar o ponto de operação do núcleo magnético. A saturação aumenta correntes e consumo de reativo, produz aquecimento, distorção e esforços sobre equipamentos. Esse é um problema de rede elétrica e de infraestrutura, não simplesmente um pulso que "entra no computador e troca bits".

A NOAA documenta GICs em redes elétricas e tubulações, e descreve como a saturação de transformadores pode provocar instabilidade, desligamentos e danos. O material técnico do serviço meteorológico espacial também registra que diferenças de potencial podem se acumular ao longo de linhas e cabos muito extensos.

## O que uma gaiola de Faraday faz

Uma gaiola de Faraday é um recinto ou invólucro condutor no qual cargas livres se redistribuem para reduzir o campo elétrico no interior. Na prática, sua eficiência depende da frequência, da continuidade elétrica das superfícies, do tamanho das aberturas, das emendas, da qualidade do contato e da forma como cabos entram e saem.

Uma blindagem costuma funcionar melhor quando é acompanhada de:

- portas e emendas com contato condutor contínuo;
- aberturas pequenas em relação ao comprimento de onda relevante;
- filtros nos pontos de entrada de energia e sinal;
- aterramento e equipotencialização projetados para o sistema;
- isolamento galvânico ou fibra óptica quando o condutor metálico não for necessário;
- proteção contra surtos e transientes nas interfaces.

Uma caixa metálica com uma fonte, um cabo de rede e um cabo de alimentação passando por aberturas sem filtragem não é uma gaiola ideal. Esses cabos podem conduzir energia e ruído para dentro do recinto, além de criar caminhos de corrente entre terras diferentes.

Também há uma limitação de frequência. Uma blindagem pode atenuar muito bem radiofrequência e campos elétricos variáveis, mas campos magnéticos de frequência muito baixa exigem materiais, geometria, distância e técnicas específicas. Uma tempestade geomagnética produz variações lentas em comparação com sinais de rádio. Por isso, fechar um computador em uma caixa metálica não elimina o risco de uma corrente induzida na rede de alimentação.

## Como partículas solares podem modificar bits

Partículas energéticas podem atravessar regiões sensíveis de um circuito integrado. Ao passar por uma junção do semicondutor, uma partícula ionizante produz pares de carga. Se a carga coletada ultrapassar a carga crítica de uma célula, latch ou flip-flop, o estado lógico pode mudar.

Esse fenômeno é chamado de single-event upset, ou SEU. Em memória, ele aparece como a alteração de um bit de zero para um ou de um para zero. O componente pode continuar funcionando depois do evento, por isso o erro é chamado de soft error quando uma reescrita, correção ou reinicialização restaura a operação. Outros efeitos de evento único são mais graves:

- single-event transient, um pulso que pode ser capturado por uma lógica vizinha;
- single-event latch-up, uma condução parasita que pode exigir desligamento e, em alguns casos, danificar o componente;
- single-event burnout, falha destrutiva em dispositivos de potência;
- multiple-bit upset, quando uma única trajetória afeta várias células.

Esse mecanismo não depende de uma onda eletromagnética atravessar a memória como se fosse um comando. Ele depende de uma partícula suficientemente energética interagir fisicamente com o silício. A NASA descreve SEUs como mudanças reversíveis no estado de circuitos bistáveis e registra que, em memória, eles se manifestam como bit flips. Eventos de partículas solares aumentam a taxa de falhas em componentes sensíveis, especialmente fora da proteção atmosférica e magnetosférica da Terra.

No solo, a atmosfera e a magnetosfera reduzem muito a exposição em comparação com satélites, aeronaves e missões espaciais. Isso não torna a taxa zero: partículas cósmicas e secundárias podem produzir erros raros em sistemas terrestres. Em ambientes de alta altitude, em voos, em data centers com grande quantidade de memória e durante eventos solares intensos, a probabilidade acumulada merece tratamento explícito.

Uma gaiola de Faraday comum não bloqueia partículas de alta energia da mesma maneira que bloqueia campos elétricos. Blindagem radiológica depende de material, espessura, energia e geometria, e pode gerar partículas secundárias. Em sistemas espaciais, a mitigação envolve seleção de componentes, testes de radiação, arquitetura tolerante a falhas e cálculo de taxa de upset, não apenas um invólucro metálico.

## Indução elétrica e SEU não são o mesmo problema

Os dois mecanismos podem ocorrer no mesmo evento solar, mas exigem controles diferentes.

| Mecanismo | Caminho principal | Sintoma típico | Proteção dominante |
| --- | --- | --- | --- |
| GIC | campo geomagnético variável, solo e condutores extensos | corrente anormal, saturação, aquecimento e desligamento | monitoramento de rede, operação elétrica, proteção de transformadores e controle de aterramento |
| Surto conduzido | rede elétrica, cabos e interfaces | reset, fonte fora da especificação, transiente ou dano | DPS, filtros, isolamento, aterramento e proteção de interface |
| SEU | partícula energética dentro do semicondutor | bit flip ou estado lógico incorreto | ECC, EDAC, scrubbing, redundância e componentes tolerantes à radiação |
| SEL ou burnout | partícula e estrutura parasita de potência | sobrecorrente ou dano permanente | limite de corrente, desligamento, projeto e qualificação do componente |

Por isso, dizer que um sistema está "sem gaiola" não é uma descrição suficiente da causa. Um sistema pode estar em uma caixa metálica e ainda receber um surto pelo cabo de energia. Também pode estar dentro de uma caixa e sofrer um SEU causado por uma partícula que a blindagem não reteve. Inversamente, uma falha durante uma tempestade solar pode ser causada por uma interrupção de energia, por erro de GPS ou por uma GIC na rede, sem que nenhum bit tenha sido alterado diretamente por radiação.

## Proteções de hardware e software

Para memória e lógica digital, ECC ou EDAC detecta e, dentro dos limites do código, corrige erros. Memory scrubbing lê e regrava periodicamente as posições para reduzir o acúmulo de erros corrigíveis. Paridade, CRC e hashes detectam corrupção em mensagens e arquivos, mas não reparam o dado por si só. Para reparar, é necessário manter uma cópia confiável, uma réplica ou um mecanismo de reconstrução.

Em sistemas críticos, use uma combinação de detecção, correção e recuperação:

- watchdogs e reinicialização segura;
- validação de invariantes e estados impossíveis;
- reexecução idempotente de operações;
- cópias com checksums e backups testados;
- replicação com domínios de falha distintos;
- logs de auditoria para distinguir corrupção de falha de transporte;
- modos fail-safe quando a integridade não puder ser garantida.

Replicar o mesmo sistema no mesmo gabinete não elimina um evento comum. Para melhorar a independência, separe fontes, caminhos de energia, domínios físicos e, quando necessário, implementações. A redundância só ajuda se o sistema conseguir detectar a divergência e escolher ou reconstruir um estado válido.

Para infraestrutura elétrica e cabos externos, as medidas são diferentes: monitoramento de clima espacial, coordenação operacional, proteção de transformadores, limitação de caminhos de corrente, aterramento bem projetado e proteção contra surtos. Em um servidor, o objetivo prático costuma ser reduzir o impacto de falhas de energia e de dados, não tentar transformar o rack em um abrigo contra qualquer partícula solar.

## Diagnóstico

Quando uma falha coincide com atividade solar, não conclua imediatamente que houve bit flip. Correlacione:

1. alertas de clima espacial e índices geomagnéticos;
2. eventos de energia, UPS, PDU, nobreak e transformadores;
3. logs de ECC, MCE, WHEA, EDAC e correções de memória;
4. resets, watchdogs, kernel panics e erros de armazenamento;
5. erros de rede, GPS, relógio e sincronização;
6. escopo temporal e geográfico do incidente.

Um erro isolado em memória pode ser um SEU, mas também pode ser defeito do módulo, temperatura, tensão, firmware ou erro de sinal. A evidência deve vir da telemetria do hardware e da repetição do padrão, não apenas da coincidência temporal com uma notícia sobre uma erupção solar.

## Fontes primárias

- [NOAA sobre correntes geomagneticamente induzidas em redes elétricas](https://swpc-drupal.woc.noaa.gov/impacts/electric-power-transmission)
- [NOAA sobre efeitos do clima espacial na Terra](https://www.nesdis.noaa.gov/our-environment/space-weather/the-effects-of-space-weather-earth)
- [NOAA sobre tempestades geomagnéticas](https://swpc-drupal.woc.noaa.gov/phenomena/geomagnetic-storms)
- [NASA sobre efeitos de radiação em microcircuitos](https://ntrs.nasa.gov/citations/19890014178)
- [NASA JPL sobre single-event upset](https://parts.jpl.nasa.gov/asic/Sect.3.4.html)
- [NASA sobre efeitos de eventos únicos em eletrônica](https://ntrs.nasa.gov/api/citations/20200008611/downloads/20200008611.pdf)
