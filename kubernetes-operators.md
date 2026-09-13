# Operators do Kubernetes

O Kubernetes nativamente sabe gerenciar coisas relativamente simples de descrever de forma genérica: "mantenha N réplicas de um container rodando", "exponha este grupo de pods sob este nome". Mas muito software tem uma lógica operacional específica, que não cabe nesse modelo genérico: um banco de dados Postgres, por exemplo, precisa de um processo particular para promover uma réplica a primária durante uma falha, para fazer backup de forma consistente, para aplicar uma atualização de versão sem perda de dados. O padrão de operator existe para ensinar essa lógica específica ao Kubernetes, em vez de exigir que uma pessoa a execute manualmente toda vez que for necessária.

## CRD e controller

Um operator é composto por duas partes. Uma **CRD** (Custom Resource Definition) ensina ao Kubernetes um tipo de objeto novo, que não existe nativamente; depois de registrada, um objeto desse tipo pode ser criado, editado e consultado como qualquer objeto nativo do Kubernetes (`kubectl get`, `kubectl apply`, e assim por diante). Um **controller** é o processo que observa objetos desse tipo novo e age para que a realidade corresponda ao que eles declaram. Juntos, CRD e controller estendem o Kubernetes com um tipo de recurso e a lógica que sabe operá-lo, sem precisar modificar o Kubernetes em si.

## O loop de reconciliação

O mecanismo interno que faz um controller funcionar é o loop de reconciliação: continuamente, ele observa o estado desejado (o que o objeto customizado declara) e o estado real (o que existe de fato), e calcula a diferença entre os dois; se há diferença, ele age para reduzi-la, e repete o processo. Esse loop não para depois de aplicar uma mudança uma vez; ele continua rodando indefinidamente, então uma mudança externa que desvie o estado real do desejado (um pod apagado manualmente, por exemplo) é detectada e corrigida na próxima iteração do loop, sem que ninguém precise notar o desvio e corrigi-lo manualmente. É o mesmo princípio de convergência contínua que sustenta o GitOps, descrito em [ArgoCD e GitOps](argocd.md), só que aplicado a um recurso específico dentro do cluster em vez de ao cluster inteiro.

## Continue por aqui

O hl-infrastructure usa esse padrão em várias camadas: CloudNativePG opera bancos Postgres (veja o exemplo real em [Adicionar um satélite novo](../operacional/adicionar-um-satelite.md)), cert-manager opera certificados (veja [TLS automático](tls-automatico.md)), e o próprio Sealed Secrets e o Argo CD Image Updater seguem essa mesma estrutura de CRD mais controller, documentados em [Ansible: as roles do bootstrap](../arquitetura/ansible.md).
