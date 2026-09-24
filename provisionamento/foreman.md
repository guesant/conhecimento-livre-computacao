# Foreman

Foreman é uma plataforma de ciclo de vida e provisionamento de hosts. Ele pode coordenar DHCP, DNS, TFTP, PXE, boot UEFI HTTP, templates de instalação, descoberta de hardware, grupos de hosts e integração com recursos de computação.

Foreman não é apenas um servidor TFTP e não é apenas um inventário. Ele combina serviços de descoberta, decisão de perfil, instalação e registro do host.

## Componentes

Uma instalação típica pode envolver:

| Componente | Responsabilidade |
| --- | --- |
| Foreman Server | API, interface, inventário, templates e política |
| Smart Proxy | Executa serviços próximos à rede, como DHCP, DNS e TFTP |
| Discovery image | Inicializa uma máquina desconhecida e envia fatos |
| Provisioning template | Gera respostas para Kickstart, Preseed, AutoYaST ou Agama |
| Host group | Define valores e associações reutilizáveis |
| Compute resource | Cria ou controla VMs quando integrado a uma plataforma |

A separação por Smart Proxy permite colocar serviços de provisionamento perto das redes sem expor todos os sistemas diretamente ao servidor central.

## Modos de provisionamento

Foreman pode provisionar por:

- PXE ou UEFI HTTP em hosts compatíveis;
- PXE Discovery, que registra hardware antes de escolher o perfil;
- boot disk para redes que não permitem configurar DHCP;
- PXE-less Discovery com kexec, quando a versão e o suporte permitirem;
- recursos de computação integrados, quando a plataforma oferece API.

A escolha é uma decisão de rede e ciclo de vida. Boot de rede é eficiente em frota, mas depende de DHCP, TFTP ou HTTP e do firmware. Boot disk reduz a dependência de DHCP, mas exige distribuir uma mídia ou imagem.

## Fluxo de descoberta

Um host desconhecido inicia a imagem de discovery, coleta hardware e aparece como host descoberto. Uma regra pode associar o host a um host group e disparar provisionamento automático. No modo manual, o operador revisa os dados, escolhe o perfil e inicia a instalação.

Uma descoberta automática precisa de critérios fortes. MAC address, serial, arquitetura e rede podem ser usados juntos para evitar instalar o sistema errado em um host apenas porque ele apareceu no segmento.

## Templates

Templates transformam parâmetros do host em configuração de instalação. O template deve ser versionado, testado e compatível com a distribuição. Kickstart, Preseed, AutoYaST e Agama não são linguagens intercambiáveis; cada instalador possui perguntas, módulos e limitações próprios.

Separe template, snippet e dados de host. Não escreva credenciais fixas em templates. Use mecanismos de segredo com escopo e tempo de vida adequados.

## Segurança

Foreman administra o caminho que instala sistemas. Proteja a interface, a API, Smart Proxies e os serviços DHCP, DNS e TFTP. Restrinja quem pode editar templates, host groups e regras de discovery.

Um template comprometido pode criar uma máquina com acesso administrativo ou inserir um agente persistente em toda a frota. Faça revisão de mudanças, valide imagens e mantenha auditoria de quem iniciou provisionamento.

## Diagnóstico

Separe a cadeia por etapas:

1. O host recebeu DHCP?
2. O firmware baixou o primeiro payload?
3. O menu ou a imagem de discovery iniciou?
4. O host apareceu no Foreman?
5. A regra escolheu o host group correto?
6. O instalador recebeu o template?
7. O sistema instalado iniciou e foi registrado?

Verifique eventos do Foreman, logs do Smart Proxy, arquivos TFTP, requisições HTTP, template renderizado e logs do instalador. Um problema de discovery não deve ser diagnosticado como falha do sistema operacional instalado.

## Foreman, cloud-init e Ansible

Foreman decide e coordena o provisionamento do host. cloud-init personaliza uma cloud image ou instância no primeiro boot. Ansible pode aplicar configuração contínua depois que existe SSH e identidade.

Usar os três pode ser coerente, desde que cada um tenha uma fronteira. Foreman não deve competir com Ansible por cada arquivo do sistema, e cloud-init não deve conter a configuração inteira da frota.

## Relações

- [Instalação pela rede](../sistemas/boot/network-install.md) explica PXE, iPXE e UEFI HTTP.
- [Cloud image](cloud-image.md) explica imagens pré-instaladas.
- [cloud-init](cloud-init.md) explica a configuração de primeira inicialização.
- [Ansible](../ansible.md) trata gestão de configuração posterior.

## Fontes primárias

- [Foreman documentation](https://docs.theforeman.org/)
- [Foreman provisioning hosts](https://docs.theforeman.org/5.0/Provisioning_Hosts/index-katello.html)
- [Foreman Discovery plugin](https://theforeman.org/plugins/foreman_discovery/18.0/index.html)
- [Foreman GitHub organization](https://github.com/theforeman)
