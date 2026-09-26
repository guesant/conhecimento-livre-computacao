# Chocolatey

Chocolatey é um gerenciador de pacotes para Windows baseado em pacotes NuGet e scripts PowerShell. O pacote `.nupkg` contém metadados e código de instalação, e pode baixar o instalador do fornecedor durante a instalação ou carregar o binário conforme a estratégia adotada pelo mantenedor.

## Feeds e pacotes

O Chocolatey pode consumir o repositório comunitário público, feeds privados e repositórios internos. Um pacote de qualidade deve declarar versão, checksum, licença, origem, dependências, install script, uninstall script e comportamento de upgrade.

O repositório comunitário usa moderação para avaliar pacotes submetidos. Isso reduz riscos, mas não substitui a revisão da organização. Um feed interno pode impor allowlist, aprovação, retenção, proxy de artefatos e política de rollback.

## Segurança

Scripts Chocolatey podem executar com privilégios administrativos e modificar arquivos, serviços, registro e PATH. O `.nupkg` e o instalador baixado são partes diferentes da cadeia de confiança. Revise o script, fixe URLs e checksums, valide assinatura do instalador e não habilite feeds arbitrários em máquinas de produção.

Chocolatey não é um sandbox. A segurança vem da origem controlada, da revisão do pacote, das permissões do processo, do isolamento da máquina e do controle de mudanças.

## Build e atualização

O mantenedor cria o pacote, testa o script e publica no feed. Em muitos pacotes o binário é baixado durante a instalação, portanto o processo de build do software e o processo de empacotamento Chocolatey são separados. A atualização compara metadados do feed e executa novamente a lógica de instalação ou upgrade.

Para uma frota, prefira pacotes internos revisados, cache de instaladores, logs centralizados, pinagem de versão e testes de uninstall e upgrade. O pacote precisa ser idempotente para não deixar estados diferentes entre máquinas.

## Fontes primárias

- [Chocolatey documentation](https://docs.chocolatey.org/en-us/)
- [Create Chocolatey packages](https://docs.chocolatey.org/en-us/create/create-packages/)
- [Community repository moderation](https://docs.chocolatey.org/en-us/community-repository/moderation/)
- [Chocolatey package repository](https://community.chocolatey.org/)
