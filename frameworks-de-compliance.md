# Frameworks de compliance

[OWASP](owasp.md), [MITRE ATT&CK](mitre-attack.md) e o NIST (já citado em [Padrões e governança da internet](padroes-e-governanca-da-internet.md)) publicam conhecimento técnico de segurança de forma aberta e gratuita: uma lista de vulnerabilidades comuns, uma base de comportamento de atacante, um framework de referência. Frameworks de compliance resolvem um problema adjacente, mas diferente: como uma organização prova, para um auditor externo ou para um cliente que exige essa prova, que segue um conjunto de controles de segurança e de processo, não apenas que conhece as boas práticas, mas que as aplica de forma verificável e auditável ao longo do tempo.

## SOC 2: controle interno, auditado por terceiro

SOC 2 (System and Organization Controls 2) é um relatório de auditoria, não uma certificação binária de aprovado ou reprovado: uma empresa de auditoria independente avalia os controles internos de uma organização contra um conjunto de critérios (segurança, disponibilidade, integridade de processamento, confidencialidade, privacidade, chamados de "trust service criteria"), e emite um relatório documentando o que encontrou. Um relatório Tipo 1 avalia se os controles estão desenhados adequadamente num momento específico no tempo; um relatório Tipo 2, mais exigente e mais valorizado por quem o exige de um fornecedor, avalia se esses controles de fato operaram de forma eficaz ao longo de um período (tipicamente vários meses), não apenas se existiam no papel. SOC 2 é particularmente comum como exigência entre empresas de tecnologia B2B: uma empresa que vende software para outras empresas frequentemente precisa apresentar um relatório SOC 2 Tipo 2 antes de um cliente corporativo maior aceitar usar seu produto, uma exigência que se tornou, na prática, um padrão de mercado nesse segmento específico, mais do que uma exigência legal formal.

## ISO 27001: um sistema de gestão de segurança da informação

ISO 27001 é uma norma internacional que certifica não um produto específico, mas um sistema de gestão de segurança da informação (SGSI) inteiro: o conjunto de políticas, processos e controles que uma organização mantém para gerenciar risco de segurança de forma contínua e sistemática, não apenas controles técnicos isolados. Diferente do SOC 2, que é um relatório de auditoria, ISO 27001 é uma certificação de fato, obtida através de um processo de auditoria por um organismo certificador credenciado, com validade por um período determinado e sujeita a auditorias de manutenção periódicas para continuar válida. A diferença central de enfoque frente ao SOC 2 é que a ISO 27001 avalia primariamente o processo de gestão de risco em si (a organização identifica riscos, decide como tratá-los, revisa essa decisão periodicamente), enquanto o SOC 2 avalia a eficácia de controles específicos já implementados; uma organização pode, e frequentemente busca, as duas certificações em paralelo, porque atendem a audiências e a exigências de mercado diferentes, uma mais comum fora dos Estados Unidos e outra mais comum dentro dele, embora essa distinção geográfica venha diminuindo com o tempo.

## Padrões setoriais

[PCI DSS](seguranca/compliance/pci-dss.md) trata dados de pagamento e o ambiente que pode afetá-los. [HIPAA](seguranca/compliance/hipaa.md) trata obrigações de privacidade e segurança relacionadas a informações de saúde protegidas nos Estados Unidos. Eles possuem escopo e autoridade diferentes de SOC 2 e ISO 27001, portanto não devem ser resumidos como mais duas certificações genéricas.

## O padrão comum: controle mais evidência mais auditoria

Esses modelos, apesar de diferenças reais de escopo e de rigor, compartilham uma estrutura lógica que vale generalizar: declarar um controle esperado, manter evidência de que esse controle de fato opera e submeter essa evidência a uma avaliação compatível com o regime aplicável. Essa estrutura explica por que o trabalho real de buscar conformidade não é implementar controles técnicos novos do zero, mas instrumentar e documentar evidência contínua de que eles operam como deveriam.

## Continue por aqui

[OWASP](owasp.md) e [MITRE ATT&CK](mitre-attack.md) cobrem o conhecimento técnico de vulnerabilidade e comportamento de ataque que informa boa parte dos controles técnicos que esses frameworks exigem provar. [Zero trust](zero-trust.md) cobre um princípio arquitetural que, quando aplicado, tende a facilitar a conformidade com controles de segmentação e controle de acesso exigidos por frameworks como o PCI-DSS.
