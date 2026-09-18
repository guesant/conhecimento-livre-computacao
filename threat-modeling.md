# Threat modeling

Modelagem de ameaças é o exercício de nomear, de forma sistemática, o que se está protegendo, quem poderia querer atacar, por onde, e o que já mitiga cada caminho, em vez de confiar na intuição de quem desenhou o sistema para lembrar de tudo. O valor não está em produzir um documento, está no processo de sistematizar a pergunta "o que pode dar errado aqui, de propósito e não por acidente". Essa pergunta é fácil de pular, porque o foco natural de quem constrói um sistema está em fazê-lo funcionar, e não em fazê-lo resistir a alguém tentando quebrá-lo. Feito cedo, o exercício ainda é barato: mover uma fronteira de confiança no desenho custa uma conversa, enquanto movê-la num sistema já em produção custa uma migração.

## STRIDE

STRIDE é um dos frameworks mais usados para estruturar esse exercício, e funciona como uma lista de checagem de categorias de ameaça, uma categoria por letra da sigla. **Spoofing** é se fazer passar por outra identidade; **Tampering**, alterar dado ou código sem autorização; **Repudiation**, negar ter feito uma ação, na ausência de prova em contrário. **Information disclosure** é expor informação para quem não deveria ter acesso; **Denial of service**, impedir o uso legítimo do sistema; e **Elevation of privilege**, obter mais permissão do que deveria ser possível. Passar cada componente de um sistema por essas lentes ajuda a não esquecer uma categoria inteira de risco só porque ela não é a mais óbvia para aquele componente específico.

## PASTA

PASTA (Process for Attack Simulation and Threat Analysis) é um framework mais elaborado, orientado a risco de negócio em vez de só a categoria técnica de ameaça. Ele começa definindo objetivos de negócio e o que teria impacto real se comprometido, decompõe a aplicação tecnicamente, analisa ameaças e vulnerabilidades conhecidas, e simula ataques concretos. O fim do processo é uma análise de risco que conecta a ameaça técnica ao seu custo real, em linguagem que sobrevive fora do time de engenharia. É um processo mais pesado que STRIDE, mais adequado a sistemas grandes com múltiplos times e stakeholders de negócio envolvidos na priorização.

A escolha entre esses frameworks depende da escala do problema. STRIDE é rápido de aplicar a um componente ou sistema específico, e o custo de rodá-lo é uma sessão de discussão com quem conhece o desenho. PASTA se justifica quando a modelagem de ameaças precisa competir por prioridade com outras iniciativas de negócio, e portanto precisa de uma linguagem de risco que faça sentido fora do time técnico. Num sistema operado por uma pessoa só, o peso de PASTA raramente se paga, e o resultado útil vem de passar cada fronteira de confiança pelas lentes de STRIDE e registrar o que mitiga cada travessia.

## Continue por aqui

[Modelo de ameaças](../arquitetura/modelo-de-ameacas.md), na arquitetura, é a aplicação concreta desse exercício a este cluster específico: os ativos protegidos, as fronteiras de confiança cruzadas, e o que mitiga cada travessia, na ordem inspirada por STRIDE ainda que sem nomear cada categoria explicitamente. [MITRE ATT&CK](mitre-attack.md) faz o percurso inverso, partindo do comportamento do atacante em vez dos ativos, e é o complemento natural deste exercício.
