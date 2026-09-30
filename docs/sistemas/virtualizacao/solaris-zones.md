# Solaris Zones

Solaris Zones é um mecanismo de virtualização de sistema operacional que separa ambientes de execução sobre um mesmo kernel Solaris. A zona global administra o host, enquanto zonas não globais recebem escopos próprios de processos, filesystem, rede, identidade e recursos. O modelo oferece uma fronteira mais integrada que a composição manual de primitivas isoladas.

## Zona global e zonas não globais

A zona global é a instância com autoridade sobre o sistema e sobre o ciclo de vida das demais zonas. Uma zona não global executa serviços dentro de um ambiente limitado, com recursos e datasets definidos pelo administrador. O processo de instalação, configuração, boot e shutdown da zona pertence ao host, mesmo quando a zona oferece uma experiência de sistema relativamente completa ao seu administrador.

O isolamento não transforma automaticamente todos os recursos em objetos independentes. A zona continua dependendo do kernel, do storage, da rede, dos dispositivos autorizados e das políticas do host. Alterar uma propriedade global pode afetar várias zonas, por isso a administração deve separar responsabilidades e registrar o ownership de cada recurso.

## Tipos de zona

Solaris possui zonas não globais tradicionais para compartilhar o kernel e, conforme a versão e a plataforma, kernel zones para executar um kernel próprio dentro de uma fronteira de virtualização. A kernel zone aproxima o modelo de uma máquina virtual, enquanto a zona tradicional possui custo menor e integra melhor os recursos do sistema hospedeiro. O nome da tecnologia não basta para inferir o nível de isolamento, pois o tipo de zona muda a garantia.

Zonas também podem usar recursos de rede e armazenamento com diferentes graus de compartilhamento. A configuração precisa declarar interfaces, endereços, datasets, delegações, limites e serviços permitidos. Uma zona com acesso administrativo excessivo ou dispositivos desnecessários pode ampliar sua capacidade de afetar o host.

## Ciclo de vida

O administrador cria uma configuração, instala o ambiente, verifica dependências e inicia a zona. Durante a operação, comandos do host permitem observar estado, processos, recursos e eventos, enquanto a zona administra os serviços que lhe foram delegados. Atualizações devem ser testadas em uma zona separada ou em um ambiente de boot apropriado quando a plataforma oferecer esse recurso.

O rollback depende do que foi alterado. Um snapshot de filesystem pode recuperar dados, mas não substitui a validação da configuração, da rede, dos serviços e do boot. Para workloads críticos, o procedimento deve incluir backup externo, teste de restauração e um caminho para operar sem a zona original.

## Relação com containers e VMs

Zones compartilha o kernel nas zonas tradicionais e por isso não oferece a mesma fronteira de uma VM completa. Containers de sistema Linux seguem uma ideia parecida, mas usam namespaces, cgroups e políticas do kernel Linux. Uma microVM ou uma VM tradicional fornece um kernel convidado próprio, com mais custo e uma separação diferente de dispositivos, boot e observabilidade.

O mecanismo é apropriado quando a equipe opera Solaris, precisa consolidar ambientes com baixo overhead e aceita o domínio de falha do kernel compartilhado. Não é uma razão para escolher Solaris quando as aplicações exigem drivers, runtimes ou ferramentas que só existem no ecossistema Linux. Compare compatibilidade, suporte, ciclo de atualização, equipe e fronteira de segurança antes de escolher.

## Relações

- [BSD Jail](bsd-jail.md) apresenta o mecanismo de isolamento do FreeBSD.
- [Comparação entre Solaris Zones e BSD Jails](zones-jails.md) compara as duas tecnologias.
- [Containers de sistema](system-containers.md) explica o modelo equivalente no Linux.
- [MicroVM](microvm.md) mostra uma fronteira que inclui kernel convidado próprio.

## Fontes primárias

- [Oracle Solaris Zones documentation](https://docs.oracle.com/en/operating-systems/solaris/oracle-solaris/11.4/administration/)
- [Oracle Solaris Zones overview](https://docs.oracle.com/cd/E53394_01/html/E54766/zones.intro-1.html)
- [Oracle Solaris Kernel Zones](https://docs.oracle.com/en/operating-systems/solaris/oracle-solaris/11.4/administration/)
