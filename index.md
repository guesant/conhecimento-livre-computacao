# Tutorial

O tutorial ensina os conceitos deste repositório na ordem em que eles aparecem de verdade: primeiro o bootstrap único via Ansible, depois o estado contínuo via GitOps. Ele é uma sequência guiada, do início ao fim, para quem nunca operou este repositório chegar a um cluster funcionando e entender, ao longo do caminho, por que cada etapa existe. Se você já conhece o repositório e só precisa de um passo específico, vá direto ao [operacional](../operacional/index.md); se você quer entender uma peça em profundidade sem repetir o bootstrap inteiro, veja a [arquitetura](../arquitetura/index.md).

- [Primeiro bootstrap](primeiro-bootstrap.md): provisiona um Raspberry Pi do zero até um cluster k3s funcionando, com Cilium, cert-manager, CloudNativePG, ArgoCD, Sealed Secrets e o Argo CD Image Updater instalados.
