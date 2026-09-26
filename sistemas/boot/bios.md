# BIOS

BIOS, Basic Input/Output System, é o modelo tradicional de firmware usado para inicializar computadores antes da adoção generalizada de UEFI. O firmware executa verificações iniciais, inicializa dispositivos básicos e transfere o controle para o código de boot encontrado no dispositivo escolhido.

O nome BIOS também é usado de forma genérica para o menu de configuração da placa-mãe, inclusive quando a implementação real é UEFI. Para diagnosticar boot, é mais preciso perguntar qual modo está ativo, legado ou UEFI, do que confiar no nome exibido pelo fabricante.

## Fluxo legado

No fluxo tradicional, o firmware escolhe um dispositivo e lê o setor inicial esperado. Em discos particionados com MBR, o primeiro setor contém a tabela de partições e um pequeno trecho de código de boot. Esse código precisa carregar um estágio posterior, que encontra o bootloader e o sistema operacional.

O espaço disponível no setor inicial é pequeno. Por isso, o bootloader legado normalmente é dividido em estágios e depende de convenções específicas do firmware. O processo não oferece a mesma abstração de filesystem e o mesmo modelo de entradas persistentes de UEFI.

BIOS legado não significa necessariamente boot somente pelo disco interno. Discos USB, CDs e outros dispositivos podem conter setores de boot compatíveis, desde que o firmware consiga enumerá-los e a ordem de boot os selecione. O meio físico e o modo de boot são dimensões diferentes.

## Limitações

O modelo legado possui limitações históricas de endereçamento, espaço de código, inicialização de dispositivos e organização do carregador. Algumas limitações foram contornadas por extensões de firmware e bootloaders, mas o resultado varia entre fabricantes.

Também não existe no BIOS tradicional um equivalente padronizado ao Secure Boot do UEFI. Um sistema legado pode validar componentes em camadas posteriores, mas a decisão de executar o primeiro código de boot não segue as variáveis autenticadas e as bases de assinatura do modelo UEFI.

## Compatibilidade

CSM permite que alguns firmwares UEFI ofereçam um fluxo compatível com BIOS. Isso pode ser útil para sistemas antigos, mas mistura expectativas diferentes. Um sistema instalado em modo legado pode não iniciar quando CSM é desativado, e um sistema instalado em UEFI pode não ser encontrado quando o firmware é forçado para o modo legado.

Ao migrar uma instalação, não altere o modo de boot como primeira tentativa de correção. Registre o particionamento, faça backup da ESP ou do setor de boot, confirme o carregador e só então escolha uma estratégia de conversão.

## Fontes primárias

- [UEFI Forum, visão geral da especificação](https://uefi.org/specs/UEFI/2.11/02_Overview.html)
- [GNU GRUB, manual de instalação](https://www.gnu.org/software/grub/manual/grub/html_node/Installing-GRUB-natively.html)
