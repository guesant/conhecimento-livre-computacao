# Semicondutores

Semicondutores são materiais e dispositivos cuja condutividade elétrica pode ser controlada. Em sistemas digitais, eles formam transistores, memórias, sensores, circuitos de potência, processadores e aceleradores. A indústria não é uma única fábrica: ela é uma cadeia distribuída entre design, software de projeto, materiais, equipamentos, fabricação, encapsulamento, teste e integração em produtos.

Esta categoria separa a explicação física da litografia das organizações que fabricam equipamentos ou chips e dos riscos que afetam a cadeia. A separação é importante porque uma empresa pode ser líder em uma etapa sem controlar as demais. A ASML fabrica sistemas de litografia. A TSMC opera como foundry de lógica para projetos de clientes. Micron, Samsung e SK hynix têm forte presença em memória, mas também atuam em outras etapas e produtos.

## Como navegar

- [Litografia EUV](litografia-euv.md) explica como a luz de 13,5 nm é produzida, refletida e usada para transferir padrões para wafers.
- [ASML](asml.md) explica a posição da empresa na cadeia de equipamentos de litografia.
- [TSMC](tsmc.md) explica o modelo de foundry e a fabricação de lógica avançada.
- [Samsung Semiconductor](samsung-semiconductor.md) explica a combinação de foundry, lógica, memória e encapsulamento.
- [Micron](micron.md) explica a cadeia de memória e armazenamento da empresa norte-americana.
- [SK hynix](sk-hynix.md) explica sua especialização em DRAM, NAND e HBM.
- [Geopolítica dos semicondutores](geopolitica.md) trata da concentração de capacidades e das dependências entre países.
- [Regulação dos semicondutores](regulacao.md) trata de exportações, subsídios, investimento, segurança e meio ambiente.
- [Impacto ambiental dos semicondutores](impacto-ambiental.md) trata de água, energia, gases, químicos e clima.
- [Crises de chips](crises-de-chips.md) explica por que uma perturbação localizada pode interromper produtos em muitos países.

## O mapa da cadeia

Uma representação útil é:

1. pesquisa de materiais, dispositivos e processos;
2. arquitetura, propriedade intelectual e design do circuito;
3. ferramentas de EDA para transformar o design em máscaras e regras de fabricação;
4. wafers, gases, fotoresistentes, químicos, metais e outros materiais;
5. equipamentos de deposição, gravação, limpeza, medição, inspeção e litografia;
6. fabricação front-end, em que camadas são construídas sobre o wafer;
7. corte, encapsulamento, interconexão e teste;
8. montagem em placas, servidores, veículos, equipamentos industriais e dispositivos de consumo.

Essa cadeia contém segmentos com economias, prazos e gargalos diferentes. Um chip pode ter projeto disponível, mas não ter capacidade de wafer. Pode haver wafer suficiente, mas faltar substrato, equipamento de teste ou capacidade de encapsulamento. Também pode haver memória disponível, mas faltar um controlador, um componente de energia ou um circuito analógico necessário para o produto final.

## O que o termo "nó" não significa

Nomes como 7 nm, 5 nm, 3 nm ou 2 nm identificam gerações de processo e não devem ser lidos como uma medida única e direta de todos os componentes físicos do transistor. Cada fabricante combina densidade, biblioteca de células, regras de design, desempenho, consumo, custo, rendimento e tipos de transistor de maneira própria.

EUV é uma tecnologia de exposição usada em algumas camadas. Ela não é sinônimo de um nó, de um transistor ou de um chip completo. Processos avançados continuam usando DUV, deposição, gravação, metrologia, inspeção, encapsulamento e muitas outras tecnologias em conjunto.

## Relação com sistemas

O resultado da cadeia aparece diretamente nas áreas de [CPU](../../cpu/cpu.md), [GPU](../../cpu/gpu.md), [RAM](../../cpu/ram.md) e [System on a Chip](../../cpu/soc.md). O desempenho de um sistema não depende somente da litografia. Arquitetura, memória, interconexão, software, refrigeração, energia, embalagem e disponibilidade também podem ser determinantes.

## Fontes primárias

- [ASML, EUV lithography](https://www.asml.com/en/products/euv-lithography-systems)
- [TSMC, tecnologia de 3 nm](https://www.tsmc.com/english/dedicatedFoundry/technology/logic/l_3nm)
- [Samsung Foundry](https://semiconductor.samsung.com/about-us/business-area/foundry/)
- [Micron, perfil corporativo](https://www.micron.com/about/company/corporate-profile)
- [SK hynix, perfil corporativo](https://www.skhynix.com/company/UI-FR-CP02/)
- [European Chips Act](https://digital-strategy.ec.europa.eu/en/policies/european-chips-act)
- [CHIPS for America](https://www.nist.gov/chips)
