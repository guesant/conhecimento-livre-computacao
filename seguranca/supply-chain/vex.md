# VEX

Vulnerability Exploitability eXchange, VEX, declara se uma vulnerabilidade
conhecida afeta ou não um produto específico. Ele adiciona contexto à
identificação de componentes feita por um SBOM ou scanner.

## Estados

Um fornecedor pode declarar que a vulnerabilidade não afeta o produto, que é
afetada, que a correção está disponível ou que a investigação ainda está em
andamento. A afirmação deve incluir produto, versão, vulnerabilidade e
justificativa suficiente para auditoria.

VEX não apaga a vulnerabilidade do componente. Ele documenta a análise de
impacto e evita que uma correspondência automática seja tratada como incidente
sem contexto.

## Relações

- [SBOM](sbom.md) lista componentes.
- [OSV-Scanner](../appsec/sca/osv-scanner.md) encontra correspondências.
- [CycloneDX](cyclonedx.md) e [SPDX](spdx.md) transportam metadados.

## Fonte primária

- [CISA VEX](https://www.cisa.gov/resources-tools/resources/vulnerability-exploitability-exchange-vex)
