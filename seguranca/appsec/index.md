# Segurança de aplicações

Segurança de aplicações reúne técnicas que observam partes diferentes do software. A classificação é útil porque "scanner de segurança" sozinho não diz o que foi examinado nem quais classes de falha permanecem invisíveis.

| Abordagem | Objeto principal | Precisa executar a aplicação? | Exemplo de pergunta |
| --- | --- | --- | --- |
| [SAST](sast/index.md) | código próprio | não | dados não confiáveis alcançam uma operação perigosa? |
| [SCA](sca/index.md) | componentes de terceiros | não | uma versão presente possui vulnerabilidade conhecida? |
| [DAST](dast.md) | aplicação em execução | sim | o comportamento exposto permite uma exploração? |
| [RASP](rasp.md) | processo da aplicação em execução | sim | o comportamento ativo deve ser observado ou bloqueado? |
| [Fuzzing](fuzzing/index.md) | entradas e estados alcançados pelo programa | sim | uma entrada incomum quebra um parser ou uma invariante? |
| [Secret scanning](secret-scanning/index.md) | arquivos e histórico | não | uma credencial foi persistida no repositório? |

## Caso de uso: pipeline em camadas

Um projeto web pode executar secret scanning antes do merge, SAST sobre o código alterado, SCA sobre lockfiles e artefatos, fuzzing em parsers e DAST contra um ambiente implantado. RASP, AV e EDR entram em runtime, com outra responsabilidade e outro modelo de operação.

Uma prática ruim é transformar a existência de qualquer scanner em evidência genérica de "segurança". O relatório só demonstra algo sobre o objeto, regras, versão da ferramenta e momento efetivamente analisados.

## Boas práticas

Defina primeiro a superfície que precisa de cobertura e só depois escolha a ferramenta. Registre o motivo de cada gate, preserve resultados relevantes, trate suppressions como decisões revisáveis e diferencie descoberta de vulnerabilidade de decisão de risco.

## Más práticas

Evite contar quantidade de scanners como métrica de maturidade, executar ferramentas sobre entradas incompletas, ignorar todos os findings por excesso de ruído ou bloquear toda mudança sem distinguir severidade e explorabilidade.

## Continue por aqui

Comece por [segurança no ciclo de vida](seguranca-no-ciclo-de-vida.md) para escolher a camada. Depois aprofunde [SAST](sast/index.md), [SCA](sca/index.md), [DAST](dast.md), [RASP](rasp.md), [fuzzing](fuzzing/index.md) ou [secret scanning](secret-scanning/index.md).
