# OpenSSF Scorecard

OpenSSF Scorecard avalia sinais públicos de segurança e manutenção de um projeto open source. Ele observa práticas como proteção de branch, revisão, testes de CI, pinagem de dependências, artefatos binários, SBOM, vulnerabilidades conhecidas, releases assinados e uso de SAST. O resultado é uma evidência automatizada sobre práticas observáveis, não uma certificação de que o código está seguro.

## O que ele mede

Cada check tenta responder uma pergunta específica. Por exemplo, o check de SAST procura evidências de uma ferramenta reconhecida, o check de SBOM procura um inventário publicado e o check de dependências procura vulnerabilidades conhecidas. Um score baixo pode significar ausência real de controle ou simplesmente que o mecanismo não reconheceu uma implementação equivalente.

O projeto deve ler o detalhe e a remediação de cada check. Melhorar o score sem corrigir o risco, como criar um artefato nominal que ninguém atualiza, produz conformidade aparente e não segurança.

## Formas de uso

O Scorecard pode rodar como GitHub Action em um repositório próprio ou como CLI contra um repositório que se deseja avaliar. A Action fornece feedback contínuo; a CLI é útil para auditoria e comparação. Permissões, token, retenção de resultados e publicação do relatório precisam seguir a política do pipeline.

## Boas práticas para repositórios

Proteja branches e exija checks antes do merge. Fixe Actions e imagens por digest ou SHA quando o risco justificar. Não versione binários gerados. Publique SBOM com releases, assine artefatos, mantenha uma política de segurança e corrija dependências vulneráveis. Execute testes e scanners em toda mudança relevante.

Scorecard não substitui SAST, SCA, SBOM, Gitleaks, Trivy ou revisão humana. Ele verifica sinais de que práticas existem e ajuda a priorizar lacunas da cadeia de desenvolvimento.

## Relações

- [Software supply chain](index.md) organiza SBOM, proveniência, atestação e assinatura.
- [SAST](../appsec/sast/index.md) analisa o código.
- [SBOM](sbom.md) descreve componentes do artefato.
- [Pinagem por digest e hash](../../pinagem-por-digest-e-hash.md) trata referências imutáveis.
- [OSS-Fuzz](../appsec/fuzzing/oss-fuzz.md) cobre fuzzing contínuo em projetos open source.

## Fontes primárias

- [OpenSSF Scorecard, checks](https://github.com/ossf/scorecard/blob/main/docs/checks.md)
- [OpenSSF Scorecard, beginner checks](https://github.com/ossf/scorecard/blob/main/docs/beginner-checks.md)
