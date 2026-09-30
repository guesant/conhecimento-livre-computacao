# Cloud image

Cloud image é uma imagem de disco pré-instalada e preparada para ser clonada ou importada por uma plataforma de nuvem, virtualização ou laboratório. Diferente de uma ISO de instalação, ela normalmente contém um sistema de arquivos pronto para iniciar e um agente ou datasource capaz de receber identidade e configuração.

## Formatos

A imagem pode ser publicada em formatos como raw, QCOW2, VMDK ou VHD, de acordo com o consumidor. O formato não define sozinho o suporte a cloud-init; a imagem precisa conter o agente, um kernel adequado e a configuração da distribuição.

Uma imagem pode ser:

- genérica, voltada a mais de uma plataforma;
- otimizada para uma nuvem;
- mínima, com menos pacotes e menor superfície;
- especializada, com drivers ou agentes de uma plataforma.

## Ciclo de vida

1. Escolha a distribuição, arquitetura e versão.
2. Baixe a imagem de fonte oficial.
3. Valide checksum, assinatura e manifesto.
4. Importe para a plataforma.
5. Injete metadata e user-data.
6. Inicie uma instância descartável.
7. Valide rede, disco, console, SSH e cloud-init.
8. Promova somente a versão testada.
9. Retire imagens antigas conforme a política de retenção.

Não altere uma única imagem compartilhada em produção. Trate imagens como artefatos versionados e gere uma nova revisão para cada mudança de base.

## Identidade e limpeza

Uma imagem clonável não deve carregar hostname, chaves de host, tokens, usuários pessoais ou estado de uma instância anterior. A distribuição e o cloud-init oferecem mecanismos para limpar estado, mas a estratégia precisa ser testada para a plataforma usada.

O disco de origem pode conter logs, caches e dados sensíveis. Verifique o conteúdo antes de publicar e limite quem pode ler o artefato.

## Cloud image e ISO

| Característica | Cloud image | ISO |
| --- | --- | --- |
| Estado inicial | Disco pré-instalado | Instalador ou ambiente live |
| Tempo de boot | Geralmente menor | Depende da instalação |
| Personalização | Metadata e cloud-init | Perguntas ou resposta automatizada |
| Uso típico | VMs e nuvens | Instalação presencial ou PXE |
| Reprodutibilidade | Artefato versionado | Reinstalação a cada host |

## Diagnóstico

Se a imagem não inicia, confirme formato, arquitetura, firmware, controlador de disco e console. Se inicia mas não recebe configuração, investigue datasource, metadata, user-data, rede e estado persistente do cloud-init.

Uma imagem de outra nuvem pode depender de drivers, datasource ou serviços que não existem na sua plataforma. Use a imagem genérica documentada quando precisar de portabilidade.

## Fontes primárias

- [Ubuntu public images](https://ubuntu.com/docs/public-images/)
- [Ubuntu cloud image artifacts](https://ubuntu.com/docs/public-images/public-images-reference/artifacts/)
- [OpenStack image guide](https://docs.openstack.org/image-guide/introduction.html)
