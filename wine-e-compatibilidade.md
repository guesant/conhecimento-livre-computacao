# Wine e compatibilidade

As páginas anteriores desta seção tratam de isolamento e virtualização: uma VM roda um sistema operacional convidado completo sobre hardware emulado ou virtualizado, e as tecnologias intermediárias entre container e VM ainda dependem de algum grau desse isolamento. Wine resolve um problema vizinho, mas fundamentalmente diferente: rodar um binário Windows em Linux sem emular hardware nenhum e sem que exista, em nenhum momento, um kernel Windows em execução. Entender essa diferença é o que permite decidir corretamente entre Wine, ou o gerenciador Bottles construído sobre ele, e uma VM completa via QEMU e KVM para um caso de uso real.

## Tradução de API, não emulação de hardware

Um binário Windows compilado para a arquitetura x86_64 contém instruções de máquina nativas dessa arquitetura, as mesmas instruções que um processador Intel ou AMD executa diretamente, independentemente de o sistema operacional por baixo ser Windows ou Linux. O que torna um binário Windows incompatível com Linux não é a arquitetura de CPU, mas a interface: ele espera chamar a API Win32, com milhares de funções do ecossistema Windows, e receber de volta um comportamento específico dessa API, que o kernel Linux não implementa.

Wine intercepta essas chamadas e as traduz para equivalentes do POSIX e do Linux: uma chamada Win32 de abertura de arquivo é convertida na chamada de sistema Linux equivalente, uma chamada de registro do Windows é atendida por uma estrutura de dados própria do Wine que simula esse registro, e assim por diante para milhares de funções da API. O binário Windows continua sendo executado diretamente pelo processador do host, sem tradução de instrução por instrução; só as chamadas à API do sistema operacional passam pela camada de tradução do Wine. É por isso que, em CPUs da mesma arquitetura, o overhead de rodar uma aplicação sob Wine é tipicamente pequeno comparado ao de emulação completa, próximo do desempenho nativo para a maior parte das aplicações.

Essa mesma característica é também o limite do modelo: como não há tradução de instrução, um binário Windows compilado para ARM não roda sob Wine em um host x86, nem o inverso. É exatamente o oposto do modo de emulação por tradução dinâmica que um emulador completo como o QEMU pode usar, que traduz instrução por instrução e por isso funciona entre arquiteturas diferentes, ao custo de ser muito mais lento.

## Prefix: um ambiente isolado por aplicação

Wine organiza o ambiente de cada instalação em um prefix, um diretório que contém uma estrutura de arquivos e um registro simulados, equivalentes ao que uma instalação Windows real teria em seu disco principal, incluindo as pastas de programas, o equivalente simulado das bibliotecas de sistema e as chaves de registro que a aplicação espera encontrar. Cada prefix é isolado dos demais: uma aplicação instalada em um prefix não enxerga o que está instalado em outro, o que permite manter versões diferentes de bibliotecas Windows, configurações de registro conflitantes, ou até versões diferentes do próprio Wine, uma por aplicação, sem que uma interfira na outra. Esse isolamento por prefix é o que possibilita, por exemplo, rodar duas aplicações que exigem versões incompatíveis da mesma dependência lado a lado no mesmo host.

Jogos e aplicações gráficas Windows tipicamente usam Direct3D, a API gráfica proprietária da Microsoft, que não existe nativamente em Linux. DXVK traduz chamadas Direct3D 9, 10 e 11 para Vulkan, a API gráfica multiplataforma de baixo nível, e VKD3D faz o equivalente para Direct3D 12. Essas duas camadas são o que permite que jogos Windows atinjam desempenho gráfico competitivo sob Wine, traduzindo a API gráfica da mesma forma que o Wine traduz o restante da API Win32, em vez de reimplementar Direct3D do zero ou depender de um driver gráfico proprietário da Microsoft que não existe para Linux.

## Bottles: gerência de prefixes, runners e dependências

Usar Wine diretamente exige gerenciar manualmente prefixes, escolher qual versão do Wine, chamada de runner, usar para cada aplicação, e instalar dependências comuns, como bibliotecas de runtime do Visual C++, do .NET, ou fontes, que muitas aplicações Windows esperam encontrar já presentes. Bottles é uma interface gráfica que empacota essa gerência: cada bottle corresponde a um prefix isolado, com um runner específico associado e um conjunto de dependências instaláveis por modelo pronto, sem exigir que o usuário edite variáveis de ambiente ou rode comandos de configuração manualmente para cada uma. Bottles não substitui o Wine, é construído sobre ele: toda a tradução de API descrita acima continua sendo feita pelo Wine, e Bottles só organiza e simplifica o que, de outra forma, seria gerenciado por linha de comando.

## Wine e Bottles vs. VM completa

Wine e Bottles de um lado, e uma VM completa via QEMU e KVM do outro, resolvem o mesmo problema de alto nível, rodar software Windows em um host Linux, mas com trade-offs opostos, e a escolha certa depende do caso específico.

| Critério | Wine ou Bottles | VM completa |
| --- | --- | --- |
| Desempenho | Próximo do nativo, sem overhead de virtualização de hardware | Overhead de virtualização, geralmente pequeno com KVM, mas presente |
| Compatibilidade de driver | Limitada ao que Wine, DXVK e VKD3D traduzem; drivers Windows nativos não rodam | Total, drivers Windows reais rodam dentro do convidado |
| Anti-cheat de jogos | Muitos sistemas anti-cheat de kernel detectam ou recusam rodar sob Wine deliberadamente | Depende de detecção de virtualização pelo anti-cheat, variável por jogo |
| Isolamento do sistema convidado | Nenhum; a aplicação roda sob o mesmo kernel Linux do host, sem um Windows completo por trás | Total, um kernel Windows completo isolado pelo hipervisor |
| Backup e portabilidade do ambiente | Um prefix é uma pasta, copiável e versionável facilmente | Uma imagem de disco completa, maior, mas também um artefato único |
| Compatibilidade de aplicação | Alta para a maioria das aplicações comuns e muitos jogos, mas não garantida | Praticamente garantida, é um Windows real |

Na prática, Wine e Bottles se justificam quando a aplicação é compatível, algo verificável previamente em bases de compatibilidade da comunidade, quando desempenho importa mais do que compatibilidade total, e quando não há dependência de um driver ou anti-cheat que exija um Windows real. Uma VM completa se justifica quando a aplicação usa recursos de sistema que o Wine não traduz corretamente, quando há dependência de um driver de hardware específico do Windows, ou quando o jogo ou aplicação ativamente detecta e recusa rodar sob camadas de compatibilidade.

CrossOver, da CodeWeavers, é um produto comercial baseado no mesmo motor Wine, com suporte pago e integração adicional; não é uma tecnologia diferente, é uma distribuição comercial do mesmo projeto. Proton, a camada de compatibilidade da Valve para jogos no Steam Play, usa exatamente os mesmos mecanismos descritos acima, Wine para tradução de API e DXVK ou VKD3D para gráficos, mas empacotados e mantidos pela Valve especificamente para o catálogo da Steam.

## Continue por aqui

[VMs e hipervisores](vms-e-hipervisores.md) cobre a alternativa de isolamento total que Wine e Bottles deliberadamente não tentam replicar. [Zones e jails](sistemas/virtualizacao/zones-jails.md) e [microVMs e sandboxes](sistemas/virtualizacao/microvms-e-sandboxes.md) cobrem o espectro de tecnologias entre um container comum e uma VM completa, nenhuma delas voltada à compatibilidade de aplicação que esta página trata. Para o índice geral desta seção, veja [aprender](index.md).
