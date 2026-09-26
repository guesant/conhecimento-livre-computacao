# Normas e frameworks de boas práticas

Normas, frameworks, métodos e práticas de engenharia resolvem problemas diferentes. Uma norma define requisitos ou uma forma reconhecida de organizar um sistema de gestão. Um framework oferece uma estrutura para avaliar risco, controle ou capacidade. Um método orienta o trabalho cotidiano de uma equipe. Uma lei ou obrigação contratual define o que é exigido por uma autoridade ou por um cliente. Confundir essas categorias produz auditorias baseadas em nomes e processos que parecem conformes, mas não reduzem o risco real.

Uma boa implementação começa pelo resultado desejado. A equipe precisa saber qual produto entrega, quais riscos administra, quais propriedades o sistema deve preservar, como uma mudança chega à produção, como um incidente é tratado e quais evidências demonstram que o processo funcionou. A norma ou o framework entra depois para dar vocabulário, critérios e rastreabilidade.

## Como usar uma referência sem transformá-la em checklist vazio

Antes de adotar uma norma, registre o escopo. O escopo pode ser uma organização, um produto, um serviço, um sistema de informação, uma equipe ou uma parte da cadeia de fornecimento. Depois separe requisito, controle, procedimento, evidência, responsável, frequência, exceção e risco aceito.

Uma evidência útil demonstra que algo aconteceu e permite verificar quando, por quem, sobre qual objeto e com qual resultado. Um documento de política prova intenção; um log, um registro de mudança, uma revisão, um teste ou uma medição prova execução. Nenhum deles é suficiente isoladamente quando o controle precisa operar continuamente.

Também é importante distinguir conformidade de eficácia. Uma equipe pode possuir uma política de backup e ainda não conseguir restaurar os dados. Pode executar uma revisão de código e ainda deixar uma vulnerabilidade crítica passar. Pode ter um procedimento de incidentes e não conseguir localizar o responsável durante uma indisponibilidade. A avaliação precisa verificar o desenho do controle e seu funcionamento.

## Mapa por finalidade

| Finalidade | Pergunta principal | Referências úteis |
| --- | --- | --- |
| Desenvolvimento | Como construir e manter software com qualidade e segurança? | ISO/IEC/IEEE 12207, NIST SSDF, OWASP SAMM, OWASP ASVS |
| Implantação | Como entregar mudanças de forma repetível, observável e reversível? | DORA, SLSA, GitOps, ITIL 4, ISO/IEC 20000-1 |
| Resposta a incidente | Como detectar, conter, recuperar e aprender com um incidente? | NIST SP 800-61 Rev. 3, ISO/IEC 27035, SRE, ITIL 4 |
| Suporte ao usuário | Como receber, classificar, resolver e comunicar solicitações? | ISO/IEC 20000-1, ITIL 4, SLAs, catálogo de serviços |
| Desenvolvimento ágil | Como organizar descoberta, priorização, feedback e entrega incremental? | Manifesto Ágil, Scrum Guide, Kanban, XP |
| Requisitos não funcionais | Quais propriedades mensuráveis o sistema precisa preservar? | ISO/IEC 25010, SRE, SLOs, contratos de serviço |
| Auditoria | Como avaliar controles e evidências com independência e rastreabilidade? | ISO 19011, ISO/IEC 27001, NIST SP 800-53A, SOC 2 |
| Governança e risco | Como decidir, priorizar, responsabilizar e revisar riscos? | ISO 31000, ISO/IEC 38500, NIST CSF 2.0, COBIT |
| Continuidade | Como manter ou recuperar serviços após falhas severas? | ISO 22301, RPO, RTO, planos de continuidade e recuperação |

Essa tabela é um mapa. Cada referência possui escopo próprio e não deve ser tratada como equivalente às demais.

## Desenvolvimento de software

### ISO/IEC/IEEE 12207 e ciclo de vida

[ISO/IEC/IEEE 12207](https://www.iso.org/standard/63712.html) organiza processos do ciclo de vida de software, incluindo aquisição, desenvolvimento, operação, manutenção e descarte. Ela não determina uma arquitetura de aplicação nem impõe Scrum, Kanban ou uma linguagem. Seu valor está em fornecer uma forma comum de discutir responsabilidades e atividades ao longo do ciclo de vida.

Uma equipe pode usar 12207 para verificar se trata, de maneira explícita, requisitos, arquitetura, implementação, verificação, validação, configuração, operação, manutenção e retirada de um sistema. A aplicação precisa ser proporcional ao contexto. Copiar todos os processos de uma organização regulada para um pequeno serviço pode criar burocracia sem reduzir risco.

### NIST SSDF

O [NIST Secure Software Development Framework](https://csrc.nist.gov/pubs/sp/800/218/final) acrescenta práticas de segurança ao ciclo de desenvolvimento. Ele organiza recomendações para preparar a organização, proteger o software e o ambiente de desenvolvimento, produzir software bem protegido e responder a vulnerabilidades.

O SSDF é um vocabulário de práticas, não um processo de desenvolvimento completo. Ele pode ser associado a Scrum, Kanban, modelo tradicional, desenvolvimento interno ou aquisição de software. Entre as evidências comuns estão inventário de componentes, revisão de código, análise de dependências, testes de segurança, proteção do pipeline, proveniência do artefato, triagem de vulnerabilidades e correções com causa raiz.

### OWASP SAMM e ASVS

[OWASP SAMM](https://owaspsamm.org/) é um modelo de maturidade para organizar e medir práticas de segurança de software. Ele ajuda a identificar uma capacidade atual, escolher uma evolução possível e acompanhar melhoria. Não deve ser usado para declarar que uma aplicação é segura apenas porque uma pontuação subiu.

O [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) é uma referência de requisitos de verificação de segurança para aplicações. Ele é mais concreto que um modelo de maturidade e pode alimentar requisitos, threat modeling, revisão, testes e critérios de aceite. O nível escolhido precisa refletir o risco e os ativos protegidos.

Essas referências complementam as páginas de [segurança no ciclo de vida](seguranca/appsec/seguranca-no-ciclo-de-vida.md), [SAST](seguranca/appsec/sast/index.md), [DAST](seguranca/appsec/dast.md), [fuzzing](seguranca/appsec/fuzzing/index.md) e [supply chain](seguranca/supply-chain/index.md).

### ISO 9001 e qualidade organizacional

[ISO 9001](https://www.iso.org/standard/62085.html) define requisitos para um sistema de gestão da qualidade. Ela trata contexto, liderança, planejamento, suporte, operação, avaliação de desempenho e melhoria. Não é uma norma de teste de software nem garante que cada produto terá boa qualidade técnica.

Em software, o sistema de gestão pode abranger controle de requisitos, revisão de mudanças, competência, tratamento de não conformidades, medição de processo e melhoria contínua. A equipe deve evitar criar documentos que existem somente para a auditoria. O controle precisa ajudar a produzir o resultado que a organização declara buscar.

## Implantação, entrega e mudança

Uma implantação confiável transforma uma mudança em um artefato identificável, valida esse artefato, publica-o por um caminho reproduzível, observa seu comportamento e preserva uma forma de recuperação. O processo deve separar construção, promoção e ativação quando isso reduzir risco.

### DORA e desempenho de entrega

As métricas [DORA](https://dora.dev/guides/dora-metrics/) observam o desempenho do sistema de entrega por meio de frequência de deploy, tempo de mudança, taxa de falha de mudança e tempo de recuperação. Elas são indicadores de fluxo e estabilidade, não metas para pressionar equipes a publicar sem qualidade.

Métricas de entrega devem ser interpretadas junto com incidentes, defeitos, segurança, satisfação de usuário e custo operacional. Aumentar frequência de deploy enquanto aumenta rollback e indisponibilidade não é melhoria. A medição deve comparar períodos e contextos equivalentes, sem usar ranking entre equipes com produtos e riscos diferentes.

### ITIL 4 e gestão de mudanças

[ITIL](https://www.peoplecert.org/ways-to-get-certified/itil) é uma biblioteca de práticas de gestão de serviços. Seus conceitos de incidente, requisição, problema, mudança, nível de serviço, conhecimento e melhoria contínua são úteis para conectar desenvolvimento, operação e suporte. ITIL não exige um comitê lento para cada deploy; a prática deve distinguir mudanças de baixo risco, mudanças normais e mudanças emergenciais.

Uma mudança deve ter motivo, escopo, risco, responsável, janela quando necessária, plano de validação e plano de recuperação. A aprovação deve ser proporcional ao risco. Um processo que aprova tudo superficialmente é pior que um processo que automatiza mudanças repetíveis e concentra revisão humana nas exceções.

### GitOps e supply chain

GitOps, [SLSA](seguranca/supply-chain/slsa.md), [SBOM](seguranca/supply-chain/sbom.md), [proveniência](seguranca/supply-chain/provenance.md), [atestação](seguranca/supply-chain/attestation.md) e [assinatura de artefatos](seguranca/supply-chain/artifact-signing.md) tratam partes diferentes da cadeia.

- GitOps declara e reconcilia o estado desejado de entrega.
- SLSA organiza níveis e práticas para aumentar a confiança na origem e no processo de construção.
- SBOM descreve componentes presentes no artefato.
- Proveniência registra como, com quais fontes e em qual ambiente o artefato foi produzido.
- Atestação associa uma afirmação verificável a um artefato.
- Assinatura permite verificar integridade e origem conforme uma política de confiança.

Nenhum desses mecanismos prova sozinho que o software é seguro ou adequado ao negócio. A confiança depende também de revisão de código, testes, controle de acesso, atualização de dependências, observabilidade e resposta a vulnerabilidades.

## Resposta a incidentes

Um incidente é um evento que exige coordenação porque afeta ou pode afetar confidencialidade, integridade, disponibilidade, segurança, privacidade ou obrigações contratuais. Um alerta é um sinal; um incidente é uma condição que precisa de decisão e resposta. A severidade deve refletir impacto, urgência, extensão, incerteza e necessidade de coordenação.

O [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) integra resposta a incidentes ao gerenciamento de risco do [CSF 2.0](https://www.nist.gov/cyberframework). A resposta não começa somente depois da detecção: preparação, governança, melhoria e recuperação também fazem parte da capacidade de resposta.

Um processo operacional maduro costuma conter:

1. preparação de pessoas, acessos, ferramentas, contatos, backups, runbooks e exercícios;
2. detecção e análise, com confirmação, escopo, impacto, linha do tempo e classificação;
3. contenção proporcional, preservando evidências e evitando ampliar o dano;
4. erradicação da causa, rotação de credenciais e correção de exposição;
5. recuperação gradual, com validação de integridade e observação reforçada;
6. comunicação com usuários, clientes, autoridades e fornecedores quando aplicável;
7. revisão sem culpa, com ações corretivas atribuídas, prazo e verificação de eficácia.

O post-mortem deve explicar o sistema e as condições que permitiram o evento, não procurar um culpado conveniente. A ausência de culpa não elimina responsabilidade: ações devem ter donos, prazos e critérios verificáveis. A página [resposta a incidente](../operacional/resposta-a-incidente.md) descreve o procedimento deste ambiente.

## Suporte ao usuário e gestão de serviços

Suporte é uma capacidade de serviço, não apenas uma caixa de entrada. O usuário precisa saber como pedir ajuda, o que fornecer, quando receberá uma atualização, como uma urgência é avaliada e qual será o caminho de escalonamento.

O [ISO/IEC 20000-1](https://www.iso.org/standard/70636.html) define requisitos para um sistema de gestão de serviços. Ele conecta planejamento, desenho, transição, entrega, relacionamento, resolução, controle e melhoria dos serviços. ITIL fornece práticas e linguagem operacional, enquanto a norma define requisitos que podem ser auditados quando a organização busca conformidade.

Um fluxo de suporte deve distinguir pelo menos:

- incidente, quando algo não funciona como esperado;
- requisição, quando o usuário pede um acesso, informação ou serviço previsto;
- problema, quando a organização investiga causas de incidentes recorrentes;
- mudança, quando altera um serviço, configuração ou infraestrutura;
- feedback, quando uma necessidade ou fricção ainda não constitui falha.

Boas práticas incluem registrar impacto e urgência separadamente, pedir apenas dados necessários, proteger informações pessoais, confirmar reprodução, manter o usuário informado, registrar a solução em uma base de conhecimento e verificar se o encerramento realmente resolveu o problema. Métricas de suporte devem incluir tempo de primeira resposta, tempo de resolução, reincidência, reabertura, satisfação e cumprimento de objetivos de serviço, sem incentivar respostas rápidas que não resolvem a demanda.

## Desenvolvimento ágil

O [Manifesto para Desenvolvimento Ágil de Software](https://agilemanifesto.org/) valoriza colaboração, software funcionando, interação com o cliente e resposta a mudanças, sem dizer que planejamento, documentação, contratos ou ferramentas não têm valor. A interpretação correta é de prioridade, não de descarte.

O [Scrum Guide](https://scrumguides.org/scrum-guide.html) define um framework com responsabilidades, eventos e artefatos. Scrum pode ajudar quando existe um produto, um backlog priorizado, um time com capacidade de entregar incrementos e um ciclo de inspeção e adaptação. Ele não corrige automaticamente dependências externas, falta de decisão, arquitetura inviável ou ausência de usuários.

Kanban enfatiza fluxo, visualização do trabalho, limites de trabalho em andamento e melhoria evolutiva. Extreme Programming enfatiza práticas técnicas como desenvolvimento orientado a testes, integração contínua, design simples e programação em par. Scrum, Kanban e XP podem ser combinados, desde que a equipe preserve a coerência do sistema de trabalho e não crie cerimônias sem propósito.

Uma prática ágil saudável conecta descoberta, definição de pronto, implementação, revisão, teste, segurança, implantação e aprendizado. Se a equipe entrega histórias rapidamente, mas acumula defeitos, incidentes e trabalho operacional não planejado, a velocidade aparente está escondendo falta de capacidade.

## Requisitos não funcionais

Requisitos não funcionais descrevem propriedades, restrições e qualidades do sistema. O termo não significa que sejam secundários. Disponibilidade, segurança, latência, recuperação e privacidade podem ser mais determinantes que uma funcionalidade visível.

[ISO/IEC 25010](https://www.iso.org/standard/35733.html) fornece um modelo de qualidade para sistemas e software. A edição e o escopo do modelo devem ser conferidos na fonte ISO antes de uma contratação ou auditoria, pois versões diferentes podem organizar as características de forma distinta.

Na prática, um requisito não funcional precisa ser mensurável e associado a um contexto:

| Qualidade | Formulação verificável |
| --- | --- |
| Disponibilidade | O serviço mantém uma meta de disponibilidade mensal, excluindo apenas janelas explicitamente definidas. |
| Desempenho | Uma proporção definida de requisições termina abaixo de uma latência em uma carga especificada. |
| Capacidade | O sistema suporta uma quantidade de usuários, eventos, dados ou requisições sem violar os objetivos acordados. |
| Recuperabilidade | Após uma falha definida, o serviço retorna em um tempo e com uma perda máxima de dados definidos. |
| Segurança | Ações, identidades, dados e componentes obedecem controles verificáveis e têm evidência de revisão. |
| Manutenibilidade | Uma mudança pode ser testada, implantada, observada e revertida com esforço e risco aceitáveis. |
| Compatibilidade | O sistema interopera com versões, protocolos, navegadores ou serviços explicitamente suportados. |
| Acessibilidade | A interface atende critérios definidos para navegação, percepção, operação e compreensão. |
| Observabilidade | Falhas relevantes podem ser detectadas, diferenciadas e investigadas com sinais e contexto suficientes. |
| Operabilidade | Uma equipe autorizada consegue operar, atualizar, diagnosticar e recuperar o serviço por procedimentos conhecidos. |

SLOs, SLIs, testes de carga, threat modeling, testes de restauração e critérios de aceite transformam adjetivos em decisões verificáveis. "Rápido", "seguro" e "escalável" não são requisitos completos até que o contexto, a medida e o limite estejam definidos.

## Auditoria e evidências

[ISO 19011](https://www.iso.org/standard/70017.html) orienta auditorias de sistemas de gestão. Uma auditoria deve ter objetivo, escopo, critérios, método, competência, independência proporcional e tratamento das evidências. Auditoria não é repetir o checklist do sistema nem procurar qualquer divergência sem relação com o critério.

O [NIST SP 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) organiza controles de segurança e privacidade. O [NIST SP 800-53A](https://csrc.nist.gov/pubs/sp/800/53/a/r5/final) trata da avaliação desses controles. A diferença é importante: um catálogo diz o que deve ser controlado; um método de avaliação orienta como examinar desenho, implementação e operação.

[SOC 2](frameworks-de-compliance.md), [ISO 27001](frameworks-de-compliance.md), [PCI DSS](seguranca/compliance/pci-dss.md) e [HIPAA](seguranca/compliance/hipaa.md) possuem escopos, autoridades e evidências diferentes. Não se deve dizer que uma certificação ou relatório torna todos os produtos e processos seguros. O resultado depende do escopo auditado, do período, das exceções e da operação real dos controles.

Uma matriz de controle útil contém:

| Campo | Finalidade |
| --- | --- |
| Objetivo | Explica o risco ou resultado que o controle trata. |
| Requisito | Diz o que deve ser preservado ou feito. |
| Controle | Descreve o mecanismo preventivo ou detectivo. |
| Procedimento | Explica como a equipe executa o controle. |
| Evidência | Mostra que o controle operou em um período e escopo definidos. |
| Responsável | Identifica quem executa e quem acompanha. |
| Frequência | Define quando o controle deve ocorrer. |
| Exceção | Registra desvio, validade, justificativa e aprovação. |
| Resultado | Registra findings, ações corretivas e verificação posterior. |

## Governança, risco e compliance

O [NIST Cybersecurity Framework 2.0](https://www.nist.gov/cyberframework) organiza resultados de cibersegurança em Govern, Identify, Protect, Detect, Respond e Recover. Ele ajuda a conversar sobre risco e prioridade, mas não é uma lista universal de controles. As referências informativas permitem relacioná-lo a controles e normas mais específicos.

[ISO 31000](https://www.iso.org/standard/65694.html) trata princípios e diretrizes para gestão de riscos. Risco deve ser formulado como relação entre evento, causa, consequência, probabilidade, incerteza e tratamento. Um inventário de riscos que apenas lista ameaças sem dono, decisão e data de revisão não é gestão de risco.

[ISO/IEC 38500](https://www.iso.org/standard/81684.html) trata governança de tecnologia da informação. Governança define direção, avalia opções e monitora resultados; gestão planeja e executa. A distinção evita que o mesmo grupo defina uma política, opere o controle e declare sozinho que o resultado foi adequado.

[COBIT](https://www.isaca.org/resources/cobit) oferece um modelo de governança e gestão de informação e tecnologia, com objetivos, componentes e critérios de desempenho. Ele é mais amplo que uma norma técnica de segurança e pode ser usado para alinhar tecnologia, risco, controles e objetivos organizacionais.

### Privacidade, continuidade e setores regulados

Privacidade exige mais que criptografia. É necessário definir finalidade, minimização, retenção, acesso, direitos, compartilhamento, incidentes e descarte. O [NIST Privacy Framework](https://www.nist.gov/privacy-framework) ajuda a estruturar risco de privacidade; requisitos legais, contratuais e setoriais continuam prevalecendo.

[ISO 22301](https://www.iso.org/standard/75106.html) trata sistemas de gestão de continuidade de negócios. A continuidade relaciona serviços críticos, dependências, impacto, estratégia, capacidade de recuperação, comunicação e exercícios. Backup é apenas uma parte da recuperação.

Os tópicos de [PCI DSS](seguranca/compliance/pci-dss.md), [HIPAA](seguranca/compliance/hipaa.md), [SOC 2 e ISO 27001](frameworks-de-compliance.md), [backup](confiabilidade/backup/backup.md) e [teste de restauração](confiabilidade/backup/teste-de-restauracao.md) devem ser consultados conforme o dado, o setor e o escopo real do sistema.

## Como combinar as referências

Uma composição razoável para uma equipe de software pode ser:

1. usar ISO/IEC/IEEE 12207 para mapear o ciclo de vida;
2. usar ISO/IEC 25010 para transformar qualidade em requisitos não funcionais;
3. usar NIST SSDF e OWASP SAMM para práticas de segurança do desenvolvimento;
4. usar DORA e SRE para medir entrega, confiabilidade e recuperação;
5. usar ITIL ou ISO/IEC 20000-1 para organizar serviços, suporte, incidentes e mudanças;
6. usar NIST CSF, ISO 27001, CIS Controls ou COBIT conforme o objetivo de risco e governança;
7. usar ISO 19011, NIST SP 800-53A ou o critério contratual para avaliar evidências;
8. usar PCI DSS, HIPAA, legislação de privacidade ou outros requisitos setoriais quando o escopo exigir.

Essa composição não é um pacote obrigatório. A seleção deve considerar o tamanho da organização, o tipo de dado, o impacto do serviço, o contrato, a jurisdição, o custo de evidência e a capacidade de manter os controles. Adotar cinco frameworks sem dono e sem medição costuma produzir mais documentação, não mais segurança ou qualidade.

## Relações com este repositório

- [Auditoria e abordagens de auditoria](auditoria-e-abordagens.md) explica sistemas, papéis, evidências, técnicas e estratégias de auditoria.
- [Engenharia de software](engenharia-software/index.md) trata princípios e desenho de código.
- [Qualidade e validação](qualidade/validacao/index.md) trata schemas, políticas e validação declarativa.
- [Manutenção de repositório](qualidade/repositorio/index.md) trata qualidade do material versionado.
- [Entrega e GitOps](entrega/index.md) trata reconciliação, rollout e promoção.
- [Segurança no ciclo de vida](seguranca/appsec/seguranca-no-ciclo-de-vida.md) trata análise de segurança por etapa.
- [Resiliência](confiabilidade/resiliencia.md) trata timeout, retry, fallback, circuit breaker e limites.
- [Resposta a incidente](../operacional/resposta-a-incidente.md) descreve a resposta operacional deste ambiente.
- [Frameworks de compliance](frameworks-de-compliance.md) compara SOC 2, ISO 27001 e controles setoriais.

## Fontes primárias e referências

- [Manifesto para Desenvolvimento Ágil de Software](https://agilemanifesto.org/)
- [Scrum Guide](https://scrumguides.org/scrum-guide.html)
- [DORA metrics](https://dora.dev/guides/dora-metrics/)
- [NIST Cybersecurity Framework 2.0](https://www.nist.gov/cyberframework)
- [NIST SP 800-61 Rev. 3, incident response](https://csrc.nist.gov/pubs/sp/800/61/r3/final)
- [NIST SP 800-218, SSDF](https://csrc.nist.gov/pubs/sp/800/218/final)
- [NIST SP 800-53, security and privacy controls](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)
- [NIST SP 800-53A, assessment procedures](https://csrc.nist.gov/pubs/sp/800/53/a/r5/final)
- [CIS Critical Security Controls](https://www.cisecurity.org/controls)
- [OWASP SAMM](https://owaspsamm.org/)
- [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/)
- [ISO standards catalogue](https://www.iso.org/standards.html)
