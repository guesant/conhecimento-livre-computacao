# CI/CD

CI/CD é geralmente pronunciado como um termo só, mas na verdade descreve três práticas distintas, com fronteiras claras entre elas, e a confusão entre a segunda e a terceira é comum mesmo entre quem trabalha com isso todo dia.

**Integração contínua** (Continuous Integration) é a prática de integrar mudanças de código num branch compartilhado com frequência, e verificar automaticamente, a cada integração, que nada quebrou: rodar testes, checar formatação, compilar. O nome vem do problema original que resolve, que é a dor de integrar mudanças grandes e divergentes depois de muito tempo trabalhando isoladamente; integrar com frequência, em pedaços pequenos, torna cada integração barata de verificar e barata de corrigir se algo quebrar.

**Entrega contínua** (Continuous Delivery) estende isso um passo adiante: toda mudança que passa pela integração contínua fica automaticamente pronta para ser colocada em produção, empacotada e validada, mas a decisão final de efetivamente colocá-la em produção continua sendo manual. O ganho aqui é reduzir a fricção e o risco de cada deploy, tornando-o um evento rotineiro e de baixo risco, mesmo que ainda exija uma decisão humana de apertar o botão.

**Implantação contínua** (Continuous Deployment) remove esse botão: toda mudança que passa pelas verificações automatizadas vai para produção sem intervenção humana nenhuma. A diferença entre entrega e implantação contínua não é técnica, é de decisão organizacional: as duas exigem a mesma maturidade de automação e teste, mas só uma delas remove a aprovação humana do caminho crítico.

## Continue por aqui

[A pipeline de CI](../arquitetura/ci.md), na arquitetura, descreve os jobs paralelos que compõem a integração contínua deste repositório, listados em [ci.yml](https://github.com/guesant/hl-infrastructure/blob/main/.github/workflows/ci.yml), e por que ele para exatamente nesse ponto, sem implantação automática de si mesmo (o que muda automaticamente, via [ArgoCD](argocd.md), é o estado do cluster a partir do git, não o próprio processo de CI). ["GitOps: root e satélites"](../arquitetura/gitops-root-e-satelites.md) explica como a convergência contínua do cluster se relaciona, e se diferencia, desses três conceitos.
