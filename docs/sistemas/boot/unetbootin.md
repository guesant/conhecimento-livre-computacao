# UNetbootin

UNetbootin, Universal Netboot Installer, cria live USBs ou instala algumas distribuições Linux e BSD a partir de uma imagem baixada ou fornecida pelo operador. O projeto também documenta um modo de instalação em disco rígido.

## Modos de uso

A ferramenta pode:

- selecionar uma distribuição de uma lista integrada;
- baixar uma imagem quando o catálogo suportar a versão;
- usar uma ISO local;
- criar uma unidade live;
- executar um fluxo de instalação em disco conforme a plataforma.

O catálogo integrado e os mecanismos de boot não são uma garantia de compatibilidade com imagens modernas. Prefira obter a imagem da distribuição e verificar seus requisitos de UEFI, Secure Boot e persistência.

## Quando usar

UNetbootin pode ser útil em máquinas antigas ou em um fluxo simples de live USB. Para imagens Windows, imagens raw de appliances, múltiplas ISOs ou instalações modernas que esperam uma gravação específica, use Ventoy, Rufus, Etcher, dd ou a ferramenta recomendada pelo projeto da imagem.

## Riscos do modo de disco

O modo de instalação em disco altera o armazenamento e o bootloader do sistema. Não use esse modo como atalho para evitar backup ou entender particionamento. Confirme se o resultado é reversível e se o bootloader usado é compatível com o firmware.

## Diagnóstico

Se a unidade não inicia, valide:

- checksum e origem da ISO;
- esquema de partição;
- modo UEFI ou Legacy;
- Secure Boot;
- suporte da distribuição ao método;
- porta e firmware do computador.

Se a imagem funciona quando gravada por outra ferramenta, isso não prova que UNetbootin corrompeu os dados. O método de boot pode ser diferente do método esperado pela distribuição.

## Relações

- [Rufus](rufus.md) é uma alternativa Windows com controle detalhado.
- [balenaEtcher](balena-etcher.md) é uma alternativa simples para imagens.
- [Ventoy](ventoy.md) evita regravar a unidade a cada ISO.

## Fontes primárias

- [UNetbootin wiki](https://github.com/unetbootin/unetbootin/wiki)
- [UNetbootin repository](https://github.com/unetbootin/unetbootin)
