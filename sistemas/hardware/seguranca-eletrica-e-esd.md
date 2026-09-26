# Segurança elétrica, proteção e ESD

Segurança elétrica não é uma única barreira. Uma instalação precisa reduzir a
probabilidade de contato perigoso, limitar a energia disponível, interromper
falhas, conduzir correntes de defeito por um caminho controlado e proteger as
pessoas quando ainda existir risco residual. EPI é apenas uma camada desse
conjunto.

Também é importante separar a rede elétrica da eletrônica de baixa energia.
Um disjuntor, um DR e um DPS têm funções diferentes. Uma pulseira antiestática,
uma luva isolante e um aterramento de proteção também não são substitutos uns
dos outros.

Esta página é material educacional. Instalação, diagnóstico ou alteração de
rede elétrica deve seguir o projeto, as normas aplicáveis e a atuação de
profissional habilitado ou autorizado. Não use a documentação para trabalhar
em circuito energizado ou improvisar uma proteção.

## Os riscos não são iguais

| Risco | O que acontece | Proteção principal |
| --- | --- | --- |
| Sobrecarga | a corrente supera a capacidade do condutor por tempo suficiente | fusível ou disjuntor de sobrecorrente |
| Curto-circuito | uma impedância muito baixa produz corrente elevada | disjuntor, fusível, coordenação e condutor adequado |
| Falha para terra | uma parte energizada entra em contato com carcaça, estrutura ou terra | PE, equipotencialização, DR e desligamento automático |
| Corrente de fuga | corrente não intencional atravessa isolamento, filtros ou capacitâncias | inspeção, isolamento, DR e manutenção |
| Surto | sobretensão transitória por raio, manobra ou acoplamento | DPS, coordenação e aterramento |
| Arco elétrico | corrente atravessa um meio ionizado, com calor, luz e pressão | distância, barreira, proteção contra arco e desenergização |
| Contato direto | pessoa toca uma parte normalmente energizada | isolamento, invólucro, barreira e procedimento |
| Contato indireto | pessoa toca uma carcaça energizada por uma falha | condutor de proteção, equipotencialização e DR |
| ESD | descarga eletrostática rápida entre corpos com potenciais diferentes | controle de carga, aterramento ESD e embalagem adequada |

Uma única ocorrência pode envolver mais de um risco. Um DPS pode conduzir um
surto e falhar, uma fonte pode desenvolver fuga para a carcaça, e uma conexão
de proteção ruim pode fazer a carcaça permanecer em uma tensão perigosa.

## Disjuntor e fusível

Disjuntores e fusíveis protegem principalmente condutores e equipamentos
contra sobrecorrente. Eles interrompem o circuito quando a corrente e o tempo
atingem uma condição prevista para o dispositivo. Não são detectores gerais de
contato humano.

Um disjuntor termomagnético combina dois comportamentos. O elemento térmico
responde a sobrecargas persistentes, enquanto o elemento magnético atua muito
mais rapidamente em correntes elevadas de curto-circuito. A curva de disparo,
a corrente nominal, a capacidade de interrupção, o número de polos e a
coordenação com os dispositivos a montante e a jusante precisam corresponder
ao projeto.

Outros dispositivos de sobrecorrente incluem:

- fusíveis, que usam um elemento que se funde e normalmente precisam ser
  substituídos;
- disjuntores miniatura, ou MCB, usados em circuitos finais de menor potência;
- disjuntores de caixa moldada, ou MCCB, usados em correntes e capacidades de
  interrupção maiores;
- disjuntores abertos, ou ACB, aplicados em quadros e entradas de maior porte;
- disjuntores de proteção de motor, dimensionados para sobrecarga e curto em
  circuitos de motores;
- disjuntores eletrônicos, que medem corrente e aplicam curvas configuráveis;
- dispositivos combinados com proteção diferencial, que somam funções e não
  devem ser confundidos com um disjuntor termomagnético simples.

O valor nominal do disjuntor não deve ser aumentado para impedir disparos sem
verificar a seção do condutor, a capacidade térmica, a corrente de curto, a
temperatura, o método de instalação e o equipamento alimentado. Um dispositivo
maior pode deixar o cabo sem proteção.

## DR, RCD, GFCI e proteção diferencial

O DR, chamado de dispositivo diferencial residual, compara a corrente que sai
pelos condutores ativos com a corrente que retorna. Se uma parte da corrente
escapa por terra, por uma carcaça, por uma tubulação ou por uma pessoa, surge um
desequilíbrio. O dispositivo pode então abrir o circuito com uma sensibilidade e
um tempo definidos.

Em outros países aparecem os nomes RCD, RCCB e GFCI. O princípio geral é
parecido, mas as normas, sensibilidades, testes e combinações de funções podem
ser diferentes. Um RCCB ou IDR pode proteger contra corrente diferencial sem
oferecer proteção de sobrecorrente. Um RCBO ou DDR pode combinar diferencial e
sobrecorrente no mesmo equipamento.

Há tipos de DR adequados a formas diferentes de corrente residual. A
classificação exata depende da norma e do fabricante, mas é comum encontrar:

| Tipo | Uso conceitual |
| --- | --- |
| AC | correntes residuais alternadas senoidais |
| A | correntes alternadas e componentes pulsantes de corrente contínua |
| F | cargas monofásicas com eletrônica e frequências residuais específicas |
| B | correntes alternadas, pulsantes e contínuas suaves, comuns em certas cargas com conversores |
| Seletivo ou temporizado | coordenação com outros diferenciais a jusante |
| Tipo portátil | proteção diferencial integrada a plugue, extensão ou tomada |

O DR não torna o contato com a rede seguro. Ele reduz o tempo de exposição em
certos defeitos, mas pode não atuar em todos os caminhos de corrente. Se uma
pessoa tocar simultaneamente dois condutores ativos, a corrente pode sair por
um condutor e retornar por outro sem produzir o desequilíbrio que o DR mede.
Também há limites de tempo, sensibilidade, instalação e funcionamento do
próprio dispositivo.

O botão de teste simula uma condição de desequilíbrio e precisa ser usado
conforme o manual e a rotina de manutenção. Um DR que não desarma no teste não
deve ser tratado como proteção disponível.

## DPS e surtos

O DPS, ou dispositivo de proteção contra surtos, limita sobretensões transitórias
desviando ou absorvendo parte da energia para um caminho projetado. Ele é
associado a condutores ativos, neutro, PE e ao sistema de equipotencialização
conforme o esquema da instalação. Um DPS não estabiliza continuamente uma rede
fora da tensão nominal e não substitui o disjuntor, o fusível ou o DR.

Em termos de instalação, é comum separar funções por posição:

- proteção de entrada, próxima da origem da instalação e capaz de lidar com
  energia elevada;
- proteção de distribuição, coordenada com a proteção de entrada;
- proteção próxima do equipamento, com menor distância elétrica e menor nível
  residual admissível.

Em diferentes normas aparecem classes, tipos ou categorias com critérios
próprios. A coordenação depende de tensão, corrente de descarga, nível de
proteção, modo de falha, distância, ligação ao PE e do DPS instalado a montante.
Um módulo com varistor, TVS ou centelhador é um componente ou subconjunto, não
uma garantia de que o quadro inteiro está protegido.

O comprimento dos condutores importa. Um caminho longo entre o DPS e o
equipamento pode manter uma tensão residual relevante durante um pulso rápido.
Surtos também podem entrar por cabos de rede, coaxiais, telefonia, antenas,
USB, serial e outras interfaces. Proteger apenas a entrada de energia não
elimina todos os caminhos.

## Aterramento, PE e equipotencialização

O aterramento de proteção cria uma referência e um caminho de baixa impedância
para correntes de defeito, mas não é simplesmente fincar uma haste e conectar
qualquer fio nela. O projeto precisa considerar o esquema de aterramento,
condutores de proteção, equipotencialização, impedância, corrente de falha,
proteção contra surtos, interferência e diferenças de potencial entre partes do
sistema.

O condutor de proteção, ou PE, liga partes metálicas expostas ao sistema de
proteção. A equipotencialização reduz a diferença de tensão entre estruturas
que uma pessoa poderia tocar ao mesmo tempo. Neutro e PE têm funções diferentes
e não devem ser unidos em pontos arbitrários.

Uma carcaça com tensão em relação ao piso pode indicar PE interrompido,
inversão, isolamento degradado, filtro EMI, fonte defeituosa, tensão induzida ou
outro problema. A causa não deve ser adivinhada pelo valor visto em um
multímetro de alta impedância.

## EPI e EPC

EPI é o equipamento de proteção individual usado por uma pessoa. EPC é a
proteção coletiva que reduz o risco para várias pessoas ou impede o acesso ao
perigo. A preferência é eliminar ou controlar o risco na fonte, desenergizar,
isolar e bloquear antes de depender do EPI.

Exemplos de EPI relacionados a riscos elétricos incluem:

- luvas isolantes compatíveis com a classe de tensão e em condição adequada;
- mangas isolantes quando o risco exigir proteção dos braços;
- capacete com características elétricas e proteção contra impacto;
- protetor facial e vestimenta com proteção contra efeitos térmicos de arco,
  quando a análise de risco indicar;
- óculos de segurança, proteção auditiva e calçado adequado ao risco;
- vestimentas, ferramentas e acessórios compatíveis com o ambiente e a tarefa.

Exemplos de EPC e controles de engenharia incluem:

- invólucros, barreiras, tampas e anteparos;
- isolamento, segregação e distância de aproximação;
- aterramento temporário e equipotencialização quando previstos no procedimento;
- sinalização, bloqueio, etiquetagem e controle de acesso;
- detector de tensão adequado e instrumento de medição apropriado;
- tapetes, plataformas e mantas isolantes quando especificados;
- proteção contra arco, telas, enclausuramento e comando remoto.

Uma luva de uso geral não é automaticamente uma luva isolante. Um calçado
isolante não autoriza contato com uma parte energizada. EPI precisa ter
especificação, inspeção, armazenamento, ensaio e substituição compatíveis com o
risco. No Brasil, a NR-6 trata do EPI e do Certificado de Aprovação; a NR-10
trata das condições de segurança em instalações e serviços com eletricidade.

## O "choque" e a corrente de fuga

O corpo sente corrente, não uma etiqueta de tensão. A intensidade percebida e o
risco dependem da tensão aplicada, do caminho pelo corpo, do tempo, da
frequência, da umidade da pele, da área de contato, do ambiente e das condições
do coração e dos músculos. Um formigamento é um sinal de que corrente pode
estar atravessando o corpo e não deve ser normalizado.

Uma fonte chaveada pode ter capacitores de filtro entre os condutores ativos e
o chassi. Em equipamento com dois pinos ou com PE ausente, o chassi pode ficar
flutuando em uma tensão alternada medida com instrumento de alta impedância. Ao
tocar na carcaça, uma pequena corrente pode passar pelo corpo para uma
referência de terra. Esse fenômeno pode explicar parte da sensação de
formigamento, mas não permite concluir que o equipamento está seguro. Fuga
excessiva, isolamento quebrado ou PE interrompido podem produzir sintomas
parecidos com uma capacitância normal do filtro.

Em caso de choque, formigamento, faísca, cheiro de aquecimento ou disjuntor e
DR desarmando repetidamente:

1. interrompa o uso sem tocar novamente na parte suspeita;
2. desenergize por um meio seguro e conhecido, quando isso puder ser feito sem
   expor outra pessoa ao risco;
3. retire o equipamento de serviço e identifique-o;
4. não remova o pino de terra, não aumente o disjuntor e não faça uma ponte no
   DR;
5. encaminhe a instalação e o equipamento para avaliação qualificada;
6. depois de um choque relevante, procure atendimento de emergência conforme a
   gravidade e os protocolos locais, mesmo que a marca externa pareça pequena.

Um DR que desarma pode estar revelando um problema real. Reenergizar várias
vezes até o dispositivo "parar de cair" remove justamente a proteção que está
sinalizando a falha.

## Eletricidade estática e ESD

Eletricidade estática é carga elétrica acumulada em um corpo ou superfície. Ela
pode surgir por atrito, separação de materiais, contato, indução e movimento de
pessoas ou embalagens. Uma pessoa pode acumular uma tensão suficiente para
produzir uma faísca perceptível ao tocar uma maçaneta, mas a energia total pode
ser pequena em comparação com a rede elétrica.

ESD, ou descarga eletrostática, é perigosa para eletrônica mesmo quando a
pessoa não sente nada. Uma descarga curta pode perfurar uma porta de entrada,
alterar um óxido, degradar um componente ou gerar um defeito latente que só
aparece depois. O fato de não haver faísca visível não prova que não houve ESD.

Uma bancada de controle ESD pode usar:

- pulseira dissipativa ligada a um ponto de referência apropriado;
- tapete dissipativo e calçado compatível;
- superfície e ferramentas próprias para ESD;
- embalagens antiestáticas para transporte e armazenamento;
- controle de materiais isolantes, umidade e fluxo de pessoas;
- ionizador quando a carga não puder ser controlada apenas por aterramento;
- proteção de entrada com TVS, resistores, filtros e estruturas de clamp no
  projeto eletrônico.

Pulseira ESD não é EPI para trabalho em rede elétrica. Ela deve ser usada em
uma bancada desenergizada, com o sistema de aterramento da estação projetado e
verificado. Conectar uma pessoa a um ponto de terra desconhecido enquanto ela
trabalha perto de tensão perigosa pode criar um caminho adicional para a
corrente.

## Diferença entre proteção elétrica e proteção ESD

| Proteção | Objetivo | Não substitui |
| --- | --- | --- |
| Disjuntor ou fusível | interromper sobrecorrente | DR, DPS ou isolamento |
| DR | detectar desequilíbrio de corrente para terra | disjuntor, DPS ou contato seguro |
| DPS | limitar sobretensão transitória | disjuntor, DR ou aterramento projetado |
| PE e equipotencialização | controlar diferença de potencial e caminho de defeito | isolamento, proteção diferencial ou EPI |
| EPI | reduzir exposição da pessoa ao risco residual | desenergização e proteção de engenharia |
| Pulseira e tapete ESD | controlar carga em bancada eletrônica | proteção contra rede elétrica |
| UPS e filtro de linha | continuidade, filtragem e proteção conforme o modelo | DPS coordenado, DR e instalação segura |
| Transformador isolador | separar galvanicamente um circuito em aplicações específicas | proteção contra tocar simultaneamente os dois lados |

UPS, estabilizador e filtro de linha são nomes comerciais com capacidades muito
variáveis. Verifique se existe DPS real, qual é o modo de falha, se há proteção
contra sobrecorrente, qual a energia suportada e se o equipamento tem
aterramento funcional. Um equipamento ligado a uma tomada sem PE não ganha um
aterramento verdadeiro apenas por ter um botão ou uma luz indicadora.

## Inspeção e manutenção

Uma instalação segura precisa de documentação, identificação dos circuitos,
dispositivos dimensionados, inspeções e testes. A manutenção deve considerar
aperto, aquecimento, oxidação, isolamento, continuidade do PE, operação do DR,
estado do DPS, coordenação das proteções, alterações de carga e sinais de
arco.

Não faça medição de resistência ou continuidade em circuito energizado com um
instrumento que não foi projetado para isso. Não use um multímetro comum como
detector universal de ausência de tensão. A categoria de medição, os cabos, as
pontas, o procedimento e a competência de quem mede fazem parte da segurança.

O diagnóstico deve começar pela desenergização e pelo controle da energia
perigosa. A ausência de tensão precisa ser verificada com método apropriado,
incluindo a comprovação do instrumento antes e depois da medição quando o
procedimento exigir. Fontes alternativas, UPS, capacitores, geradores,
fotovoltaica e retorno por outros circuitos precisam ser considerados.

## Fontes e normas

- [NR-10, segurança em instalações e serviços em eletricidade](https://www.gov.br/trabalho-e-emprego/pt-br/acesso-a-informacao/participacao-social/conselhos-e-orgaos-colegiados/comissao-tripartite-paritaria-permanente/normas-regulamentadoras/normas-regulamentadoras-vigentes/norma-regulamentadora-no-10-nr-10)
- [NR-6, equipamentos de proteção individual](https://www.gov.br/trabalho-e-emprego/pt-br/assuntos/inspecao/seguranca-e-saude-no-trabalho/normas-regulamentadoras-nrs/nr-06-atualizada-2022.pdf)
- [OSHA, ground-fault circuit interrupters](https://www.osha.gov/etools/construction/electrical-incidents/ground-fault-circuit-interrupters)
- [OSHA, proteção por aterramento](https://www.osha.gov/etools/electric-power/hazardous-energy-control/grounding-employee-protection)
- [EOS/ESD Association, fundamentos de ESD](https://www.esda.org/esd-overview/esd-fundamentals/part-1-an-introduction-to-esd/)
- [EOS/ESD Association, princípios de controle de ESD](https://www.esda.org/esd-overview/esd-fundamentals/part-2-principles-of-esd-control/)
