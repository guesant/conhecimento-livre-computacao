# bubblewrap

bubblewrap é uma ferramenta de sandbox para Linux que cria um processo com namespaces, mounts, limitações de acesso e outras primitivas do kernel. Ele não é um daemon de containers, não define uma imagem OCI e não tenta administrar um sistema convidado completo. A aplicação ou o launcher fornece a política de isolamento e o conjunto de arquivos que o processo poderá enxergar.

## Modelo de sandbox

O processo é iniciado dentro de uma nova configuração de namespaces e de filesystem montado conforme os argumentos fornecidos. A aplicação pode receber um root filesystem somente leitura, diretórios específicos compartilhados, um namespace de rede isolado ou a rede do host, conforme a política. O resultado é uma fronteira pequena e composável, mas também uma configuração que pode ser difícil de revisar se for construída sem uma convenção clara.

O sandbox não cria segurança por apenas ser chamado. Bind mounts, capabilities, sockets, acesso a dispositivos, ambiente, arquivos graváveis e integração com D-Bus podem reabrir caminhos para o host. O operador deve tratar cada recurso concedido como parte da política de confiança e limitar o conjunto ao que a aplicação realmente precisa.

## Relação com containers

Um container de aplicação normalmente parte de uma imagem, possui um runtime com lifecycle próprio e pode ser administrado por Docker, Podman ou Kubernetes. bubblewrap oferece apenas a construção de uma sandbox de processo e deixa o lifecycle, a distribuição, a atualização e a observabilidade para o chamador. Ele é mais próximo de uma biblioteca de composição de isolamento do que de uma plataforma de containers.

Essa diferença torna bubblewrap útil para aplicações desktop, ferramentas de build, visualizadores de documentos e processos que precisam reduzir acesso ao sistema. Também torna inadequado tratá-lo como substituto automático de uma política completa de imagens, supply chain, rede e workloads. Para um serviço de produção, a escolha deve considerar quem cria a sandbox e como sua configuração será testada e atualizada.

## Segurança e limites

O kernel continua sendo a autoridade da sandbox, e vulnerabilidades ou configurações privilegiadas podem comprometer a fronteira. Um processo com acesso a um socket administrativo pode controlar um serviço fora do sandbox mesmo que o filesystem esteja isolado. A análise deve incluir mounts, namespaces, seccomp quando usado, capabilities, LSM, ambiente e IPC.

Uma política reproduzível deve estar versionada, ser testada com casos de acesso permitido e negado e emitir evidência suficiente para diagnóstico. Não use diretórios temporários ou caminhos graváveis por usuários não confiáveis como parte de uma decisão de segurança sem controlar ownership e permissões. A sandbox reduz superfície, mas não substitui atualização, autenticação, autorização e validação da origem do software.

## Relações

- [Containers de sistema](system-containers.md) descreve um ambiente de sistema sobre namespaces.
- [gVisor](gvisor.md) media chamadas de sistema com um componente adicional.
- [MicroVM](microvm.md) fornece um kernel convidado próprio.
- [Mapa de MicroVMs e sandboxes](microvms-e-sandboxes.md) posiciona as alternativas.

## Fontes primárias

- [bubblewrap repository](https://github.com/containers/bubblewrap)
- [bubblewrap manual](https://github.com/containers/bubblewrap/blob/main/docs/bwrap.xml)
- [Linux namespaces](https://man7.org/linux/man-pages/man7/namespaces.7.html)
