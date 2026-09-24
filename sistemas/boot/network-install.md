# Instalação pela rede

Instalação pela rede inicializa uma máquina usando uma interface de rede e busca o instalador ou o ambiente de boot em um servidor. O objetivo não é necessariamente instalar sem mídia física, mas separar o boot do armazenamento local e centralizar imagens, versões e configuração.

## Cadeia de boot

Uma cadeia comum contém:

1. firmware Legacy BIOS ou UEFI;
2. DHCP ou proxyDHCP para indicar a inicialização;
3. um transporte inicial, tradicionalmente TFTP;
4. um bootloader como PXELINUX, iPXE ou GRUB;
5. kernel e initrd, ou um segundo estágio;
6. instalador, ambiente live ou ferramenta de diagnóstico;
7. fonte de pacotes e configuração automatizada.

O DHCP descobre a rede e pode indicar um arquivo de boot. O TFTP é simples para o primeiro payload, mas lento para arquivos grandes. HTTP costuma ser melhor para kernel, initrd, imagens e pacotes depois que o bootloader possui rede suficiente.

## PXE e iPXE

PXE é uma família de mecanismos de boot de rede integrada a muitos firmwares. iPXE é um bootloader com suporte a protocolos e scripts mais amplos. Um fluxo pode usar PXE apenas para entregar o iPXE e deixar o iPXE buscar o restante por HTTP.

Essa separação reduz a quantidade de lógica no firmware e permite menus, variáveis e scripts mais ricos. Ela também adiciona uma dependência: um firmware que não consegue iniciar o primeiro estágio não alcança o iPXE.

## BIOS e UEFI

Legacy BIOS e UEFI usam payloads diferentes. Uma configuração deve declarar quais arquiteturas e modos suporta e testar ambos quando o parque for heterogêneo.

Secure Boot altera a cadeia de confiança. Um binário não assinado pode exigir desativação temporária, uma chave própria ou um shim assinado. Desativar Secure Boot é uma decisão de segurança, não uma etapa neutra de troubleshooting.

## Instalador, live e provisionamento

Um instalador de rede entrega o suficiente para particionar o disco, configurar rede e baixar pacotes. Uma imagem live entrega um ambiente completo temporário e costuma consumir mais memória e banda. Um sistema de provisionamento acrescenta respostas automatizadas, seleção de perfil, configuração de identidade e registro do host.

Não confunda o menu de boot com o processo de provisionamento. netboot.xyz pode disponibilizar instaladores e utilitários, mas cada sistema operacional ainda define sua própria instalação, armazenamento e automação.

## Arquitetura mínima

Uma rede de laboratório pode ter DHCP ou proxyDHCP controlado, TFTP para o primeiro arquivo, HTTP para payloads maiores, armazenamento versionado, logs, validação de checksum e uma alternativa de boot local.

O servidor de boot deve estar disponível antes do host que será instalado. Em uma rede com múltiplos DHCP, evite introduzir opções PXE globalmente sem entender quais máquinas serão afetadas.

## Operação segura

Fixe versões de instaladores e não substitua uma imagem em uso sem manter a anterior. Use nomes imutáveis ou diretórios versionados para que um reboot durante manutenção não baixe metade de uma nova imagem.

Proteja scripts de boot contra alteração não autorizada. Um script iPXE pode direcionar a máquina para um kernel ou instalador controlado por terceiros, portanto o repositório de boot é parte da cadeia de confiança.

## Diagnóstico

| Sintoma | Camada provável |
| --- | --- |
| Não recebe endereço | VLAN, DHCP ou firmware |
| Recebe endereço mas não baixa arquivo | opção de boot, TFTP ou firewall |
| Baixa iPXE e para ao buscar kernel | URL, HTTP, TLS ou arquitetura |
| Inicia instalador mas não acha pacotes | DNS, rota, mirror ou proxy |
| Instala mas não inicia depois | particionamento, bootloader ou Secure Boot |

Use captura de tráfego somente com autorização e cuidado com dados de rede. Compare o payload entregue ao modo de firmware e à arquitetura do host.

## Fontes primárias

- [netboot.xyz introduction](https://netboot.xyz/docs/)
- [iPXE documentation](https://ipxe.org/docs)
- [UEFI specifications](https://uefi.org/specifications)
- [PXE support reference](https://www.intel.com/content/www/us/en/support/articles/000017572/server-products.html)
