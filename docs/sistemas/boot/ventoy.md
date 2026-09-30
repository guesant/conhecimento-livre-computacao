# Ventoy

Ventoy instala um bootloader em uma unidade e deixa a partição principal disponível como armazenamento comum. Depois da instalação inicial, imagens ISO, WIM, IMG, VHD, VHDX e EFI podem ser copiadas como arquivos. No boot, Ventoy encontra as imagens e apresenta um menu.

## Modelo de uso

Ventoy é diferente de um gravador que destrói e reescreve a unidade para cada ISO:

| Abordagem | Resultado |
| --- | --- |
| Gravador tradicional | Uma imagem ocupa o dispositivo e normalmente substitui o conteúdo anterior |
| Ventoy | Uma instalação cria o ambiente de boot e vários arquivos de imagem convivem em uma partição |
| Multiboot gerenciado | Um menu e scripts específicos integram imagens e opções de persistência |

A praticidade de copiar arquivos não significa que toda imagem terá o mesmo comportamento. Algumas distribuições exigem plugin, modo de boot específico ou uma imagem compatível com o método adotado.

## Instalação e atualização

A instalação do Ventoy recria a estrutura do dispositivo. Confirme o disco inteiro, não uma partição, e faça backup do que ainda estiver nele. Uma atualização posterior deve usar o modo de update para preservar a partição de dados quando a versão suportar essa operação.

No Linux, confirme o alvo antes de executar o instalador:

```bash
lsblk
sudo sh Ventoy2Disk.sh -i /dev/sdX
```

O exemplo é deliberadamente genérico. Nunca substitua `/dev/sdX` sem verificar o modelo e a capacidade do dispositivo.

## Secure Boot e persistência

Ventoy oferece um fluxo para Secure Boot que depende da versão e da plataforma. Teste a mídia em cada classe de firmware antes de depender dela em uma emergência.

Persistência e plugins podem guardar alterações fora da ISO. Isso é útil para uma distribuição live, mas transforma o dispositivo em um ambiente com estado. Documente o arquivo de persistência, proteja dados sensíveis e não confunda um live persistente com uma instalação de produção.

## Organização

Organize as imagens por finalidade e inclua versão e arquitetura no nome. Um conjunto de recuperação pode conter:

- instaladores de sistemas;
- GParted Live;
- Hiren's BootCD PE;
- MemTest86 ou Memtest86+;
- ferramentas de firmware;
- imagens de diagnóstico.

Valide checksums e mantenha uma cópia offline. O menu deve continuar funcional mesmo quando a rede não existir.

## Diagnóstico

Se a imagem não aparece, confirme extensão, partição de dados, caminho e filtros do Ventoy. Se aparece mas não inicia, confirme modo UEFI ou Legacy, Secure Boot, arquitetura e compatibilidade específica da imagem.

Teste um Linux live e um instalador Windows antes de levar o dispositivo para uma recuperação. Um dispositivo multiboot sem teste é apenas uma coleção de arquivos.

## Segurança

O dispositivo pode executar kernels, initrds e ambientes com acesso total aos discos. Proteja-o contra alteração e trate-o como uma credencial operacional. Não mantenha chaves privadas ou senhas no mesmo dispositivo usado por várias pessoas.

## Relações

- [Rufus](rufus.md) grava uma imagem ou cria uma mídia Windows em um fluxo mais dirigido.
- [YUMI](yumi.md) oferece um multiboot com frontend e integração própria.
- [dd](dd.md) faz cópia bruta e não oferece a camada de seleção do Ventoy.
- [Instalação pela rede](network-install.md) elimina a dependência de USB em uma frota.

## Fontes primárias

- [Ventoy](https://www.ventoy.net/)
- [Ventoy documentation](https://www.ventoy.net/en/doc_start.html)
- [Ventoy image file support](https://www.ventoy.net/en/doc_vlnk.html)
