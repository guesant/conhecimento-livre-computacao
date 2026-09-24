# Media Creation Tool

Media Creation Tool é o utilitário oficial da Microsoft para criar mídia de instalação do Windows. Ele baixa os componentes necessários e pode preparar uma unidade USB ou gerar uma imagem ISO conforme a edição e a versão oferecidas pela Microsoft.

## Quando usar

Use a ferramenta quando a prioridade for obter uma mídia de instalação diretamente do fluxo oficial da Microsoft, com seleção guiada de idioma, edição e arquitetura.

Ela é diferente de Rufus:

| Ferramenta | Responsabilidade principal |
| --- | --- |
| Media Creation Tool | Obter e preparar mídia oficial do Windows |
| Rufus | Gravar uma ISO e escolher parâmetros detalhados da unidade |
| Ventoy | Inicializar várias imagens mantidas como arquivos |
| Foreman | Provisionar uma frota por rede e templates |

## Fluxo seguro

1. Baixe o executável da página oficial da Microsoft.
2. Confirme a edição, idioma e arquitetura.
3. Faça backup do USB escolhido.
4. Selecione a opção para criar mídia.
5. Aguarde download e gravação.
6. Ejete a unidade corretamente.
7. Teste o boot antes de instalar.

A ferramenta não substitui licença, ativação, backup ou validação de compatibilidade do computador. A mídia criada pode instalar uma versão diferente daquela que você imaginava se a página ou o canal tiver mudado.

## ISO e USB

Uma ISO é útil para arquivo, máquina virtual, gravação posterior e reprodutibilidade. Um USB preparado é útil para iniciar imediatamente um computador. Se você precisa aplicar opções especiais de partição, contornar incompatibilidades documentadas ou combinar a imagem com uma configuração de boot diferente, gere ou obtenha a ISO e use uma ferramenta adequada.

## Diagnóstico

Se o download falhar, verifique conectividade, espaço em disco e data do sistema. Se o USB não inicia, confirme firmware UEFI, Secure Boot, arquitetura, ordem de boot e integridade da unidade.

Não repita uma instalação em um computador sem confirmar os volumes e os dados que serão substituídos.

## Fonte primária

- [Microsoft: create installation media for Windows](https://support.microsoft.com/en-US/Windows/Deployment/Install-Upgrade/create-installation-media-for-windows)
