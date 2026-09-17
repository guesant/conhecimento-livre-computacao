# OWASP

OWASP (Open Worldwide Application Security Project, antes Open Web Application Security Project) é uma fundação sem fins lucrativos dedicada a melhorar a segurança de software, mantida por contribuição voluntária de uma comunidade global, sem vínculo com nenhum fornecedor específico de ferramenta de segurança. É comum a sigla ser usada como sinônimo de um único documento, o Top 10, mas a fundação mantém muitos projetos e capítulos locais em cidades ao redor do mundo, cobrindo desde ferramentas de teste até guias de desenvolvimento seguro e material educacional.

## O Top 10

O OWASP Top 10 é uma lista, revisada periodicamente, das categorias de vulnerabilidade mais críticas e mais comuns encontradas em aplicações web, baseada em dados agregados de organizações e ferramentas de segurança que contribuem com suas próprias descobertas. Categorias como injeção (SQL, comando, e outras), quebra de controle de acesso, e configuração de segurança incorreta aparecem recorrentemente entre as revisões, o que sinaliza que são problemas estruturais recorrentes na forma como software é construído, não modismos passageiros. O Top 10 não é uma checklist de teste exaustiva, é uma priorização de onde o esforço de segurança costuma valer mais a pena primeiro, dado o histórico observado.

## Além do Top 10

Entre os outros projetos mantidos pela fundação, alguns aparecem com frequência fora do contexto puramente web: o ASVS (Application Security Verification Standard), um padrão detalhado de requisitos de segurança organizados por nível de rigor, usado como referência para auditoria e certificação; e o Dependency-Check, uma ferramenta de SCA (análise de composição de software, detalhada em [Scanning de vulnerabilidade](vulnerability-scanning.md)) mantida sob o guarda-chuva do projeto.

## Continue por aqui

[MITRE ATT&CK](mitre-attack.md) olha o mesmo problema pelo lado do atacante, catalogando o que ele faz depois de explorar uma vulnerabilidade destas. [Threat modeling](threat-modeling.md) e [scanning de vulnerabilidade](vulnerability-scanning.md) cobrem, de forma mais sistemática e mais automatizável respectivamente, boa parte do mesmo espaço de problema que o Top 10 lista informalmente. [Mapa de controles](../arquitetura/mapa-de-controles.md), na arquitetura, mostra qual gate concreto deste repositório cobre qual categoria de risco.
