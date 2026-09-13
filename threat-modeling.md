# Threat modeling

Modelagem de ameaças é o exercício de nomear, de forma sistemática, o que se está protegendo, quem poderia querer atacar, por onde, e o que já mitiga cada caminho, em vez de confiar na intuição de quem desenhou o sistema para lembrar de tudo. O valor não está em produzir um documento, está no processo de sistematizar a pergunta "o que pode dar errado aqui, e propositalmente, não por acidente", que é fácil de pular quando o foco natural de quem constrói um sistema está em fazê-lo funcionar, não em fazê-lo resistir a alguém tentando quebrá-lo de propósito.

## STRIDE

STRIDE é um dos frameworks mais usados para estruturar esse exercício, e funciona como uma lista de checagem de categorias de ameaça, cada letra representando uma categoria: **Spoofing**, se fazer passar por outra identidade; **Tampering**, alterar dado ou código sem autorização; **Repudiation**, negar ter feito uma ação, na ausência de prova em contrário; **Information disclosure**, expor informação para quem não deveria ter acesso; **Denial of service**, impedir o uso legítimo do sistema; e **Elevation of privilege**, obter mais permissão do que deveria ser possível. Passar cada componente de um sistema por essas seis lentes ajuda a não esquecer uma categoria inteira de risco só porque ela não é a mais óbvia para aquele componente específico.

## PASTA

PASTA (Process for Attack Simulation and Threat Analysis) é um framework mais elaborado, orientado a risco de negócio em vez de só a categoria técnica de ameaça: ele começa definindo objetivos de negócio e o que teria impacto real se comprometido, decompõe a aplicação tecnicamente, analisa ameaças e vulnerabilidades conhecidas, e simula ataques concretos, terminando numa análise de risco que conecta a ameaça técnica ao seu custo real. É um processo mais pesado que STRIDE, mais adequado a sistemas grandes com múltiplos times e stakeholders de negócio envolvidos na priorização.

A escolha entre os dois (ou entre esses e outros frameworks) depende da escala do problema: STRIDE é rápido de aplicar a um componente ou sistema específico; PASTA se justifica quando a modelagem de ameaças precisa competir por prioridade com outras iniciativas de negócio e precisa de uma linguagem de risco que faça sentido fora do time técnico.

## Continue por aqui

[Modelo de ameaças](../arquitetura/modelo-de-ameacas.md), na arquitetura, é a aplicação concreta desse exercício a este cluster específico: os ativos protegidos, as fronteiras de confiança cruzadas, e o que mitiga cada travessia, na ordem inspirada por STRIDE ainda que sem nomear cada categoria explicitamente.
