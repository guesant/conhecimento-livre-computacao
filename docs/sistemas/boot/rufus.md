# Rufus

Rufus é uma ferramenta Windows para formatar unidades removíveis e criar mídias inicializáveis a partir de ISOs e outros formatos. É útil para instalar Windows ou Linux, inicializar utilitários e gravar firmware que exige DOS.

## Quando escolher

Use Rufus quando a unidade deve conter uma mídia inicializável única e você precisa escolher detalhes como esquema de partição, destino de firmware e modo de imagem. Para carregar muitas imagens no mesmo dispositivo, Ventoy ou YUMI costumam ser mais adequados.

O processo é destrutivo para o dispositivo selecionado. Confirme capacidade, modelo e letra da unidade antes de iniciar.

## Fluxo

1. Baixe a ISO da fonte oficial.
2. Verifique checksum quando o projeto oferecer.
3. Abra Rufus no Windows.
4. Selecione a unidade correta.
5. Selecione a imagem.
6. Escolha GPT e UEFI, ou MBR e BIOS, conforme o destino.
7. Escolha o modo ISO ou DD quando a imagem oferecer mais de uma alternativa.
8. Revise qualquer opção de personalização.
9. Grave e valide o resultado.

A escolha entre GPT e MBR não é estética. Ela precisa combinar com o modo de firmware, a tabela de partições e a forma como o instalador foi construído.

## Windows

Rufus pode aplicar opções específicas ao criar uma mídia Windows, conforme a versão da ferramenta e da ISO. Essas opções podem alterar requisitos de hardware, conta local, coleta ou instalação. Use-as somente quando houver uma decisão explícita e documentada.

A mídia criada instala Windows; ela não equivale automaticamente a Windows To Go. Um sistema portátil tem requisitos, desempenho, licenciamento e riscos próprios.

## Segurança e diagnóstico

Baixe Rufus do site oficial ou do repositório oficial. Desconfie de versões modificadas, aplicativos móveis que reutilizam o nome e executáveis distribuídos por sites de download genéricos.

Se a unidade não inicia, teste outra porta e confirme modo UEFI, Secure Boot, sistema de arquivos, imagem e checksum. Se o instalador inicia mas falha depois, investigue a ISO e o hardware separadamente.

## Comparação

| Ferramenta | Melhor caso |
| --- | --- |
| Rufus | Uma mídia dirigida, especialmente Windows |
| Ventoy | Várias imagens copiadas como arquivos |
| balenaEtcher | Gravação simples de imagem em USB ou SD |
| dd | Cópia bruta reproduzível em shell |
| YUMI | Kit multiboot com menu e recursos próprios |
| Media Creation Tool | Mídia oficial de instalação do Windows |

## Fontes primárias

- [Rufus](https://rufus.ie/)
- [Rufus usage notes](https://github.com/pbatard/rufus/wiki/Usage-Notes)
- [Rufus FAQ](https://github.com/pbatard/rufus/wiki/FAQ)
