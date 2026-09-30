# netboot.xyz

netboot.xyz é um menu de boot baseado em iPXE que reúne instaladores de sistemas operacionais, distribuições live, hypervisors e utilitários. Ele permite usar um dispositivo ou um endpoint de rede para chegar a vários ambientes, em vez de manter uma mídia física separada para cada imagem.

## O que ele faz

O projeto entrega uma interface de seleção e os payloads necessários para iniciar opções compatíveis. O menu inclui instalações Linux pela rede, distribuições live, utilitários de disco e recuperação, ferramentas de segurança e forense, hypervisors e armazenamento, além de alguns fluxos Windows baseados em WIM.

Ele não é um substituto universal do instalador de cada sistema e não garante que o sistema escolhido terá drivers, resposta automatizada ou suporte ao hardware específico.

## Modos de uso

| Modo | Descrição | Uso adequado |
| --- | --- | --- |
| USB | Grava um bootloader netboot.xyz em um dispositivo | Laboratório e recuperação presencial |
| PXE ou TFTP | A rede entrega o primeiro estágio | Parque controlado e servidores sem mídia |
| Self-hosted | Hospeda menus e recursos sob seu controle | Ambientes sem dependência externa |
| Container | Executa o serviço em container | Laboratórios e redes com compose |
| Ansible | Automatiza a publicação da configuração | Frotas com gestão de configuração |
| Endpoint remoto | Anexa o menu por BMC ou console virtual | Servidor sem sistema inicializável |

Use o modo mais simples que atende ao risco. Um USB é excelente para uma emergência isolada; self-hosting é melhor quando a rede não pode depender de um serviço externo.

## Arquitetura

Em PXE, DHCP ou proxyDHCP encaminha o host para um primeiro payload. TFTP ou outro mecanismo fornece o bootloader. O iPXE então busca menus e recursos adicionais, normalmente por HTTP.

A documentação do projeto cobre boot por USB, TFTP, self-hosting e diagnóstico. O suporte inclui arquiteturas x86 de 32 e 64 bits e arm64, além de modos Legacy e UEFI. A opção exibida depende da arquitetura e do modo em que o menu foi iniciado.

## Fluxo operacional

1. Confirme arquitetura, modo UEFI ou Legacy e política de Secure Boot.
2. Escolha USB, PXE ou uma instância self-hosted.
3. Inicie o menu netboot.xyz.
4. Escolha instalador, live system ou utilitário.
5. Valide origem, versão e checksum quando disponível.
6. Execute o procedimento específico da ferramenta.
7. Remova ou desabilite o boot de rede quando a instalação terminar.

Em uma rede de produção, mantenha uma versão conhecida do menu e das imagens. Não dependa de uma alteração remota de catálogo durante uma recuperação sem acesso alternativo.

## Self-hosting

Self-hosting reduz dependência de endpoints públicos e permite controlar cache, logs, versões e disponibilidade. Ele não elimina a necessidade de atualizar os menus ou validar as fontes upstream.

Uma implantação self-hosted precisa definir onde DHCP, TFTP e HTTP rodam, como recursos são baixados e atualizados, como arquivos são verificados, quais hosts podem fazer boot, como o serviço é recuperado e qual alternativa existe fora da rede principal.

## Segurança

Um menu de boot controla qual kernel, initrd ou instalador será executado. Restrinja a rede de boot, proteja os arquivos e mantenha versões imutáveis para auditoria. Não coloque credenciais em scripts iPXE.

Se a rede de boot puder servir uma imagem diferente para um servidor administrativo, ela se torna uma superfície de comprometimento equivalente ao repositório de software. Use checksums, assinaturas quando oferecidas e revisão dos scripts.

## Diagnóstico

O diagnóstico deve identificar se o host recebeu DHCP, se o arquivo inicial foi localizado, se o iPXE conseguiu rede, se o menu foi carregado, se o payload existe e se o kernel iniciou.

Verifique arquitetura e modo de firmware antes de trocar servidores ou reescrever imagens. Um payload BIOS não é automaticamente adequado para UEFI.

## Relações

- [Instalação pela rede](network-install.md) explica PXE, iPXE, DHCP, TFTP e HTTP.
- [GParted Live](gparted-live.md) é um utilitário que pode ser iniciado pela rede.
- [MemTest86 e Memtest86+](memtest.md) podem ser executados por PXE.

## Fontes primárias

- [netboot.xyz documentation](https://netboot.xyz/docs/)
- [Quick start](https://netboot.xyz/docs/quick-start/)
- [Booting methods](https://netboot.xyz/docs/booting-methods/)
- [Self-hosting](https://netboot.xyz/docs/self-hosting/)
