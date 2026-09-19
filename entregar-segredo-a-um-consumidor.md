# Entregar segredo a um consumidor

Um segredo gerado num lugar (um banco de dados que cria a própria credencial de acesso, uma autoridade que emite um token) frequentemente precisa chegar a um consumidor que vive em outro domínio de confiança: outro cluster, outro namespace administrado por outra equipe, outro ambiente de rede inteiro.

O problema de entrega é distinto do problema de gerar o segredo e do problema de mantê-lo cifrado em repouso; cada abordagem abaixo resolve especificamente essa travessia de fronteira, com um modelo de confiança e um custo operacional próprios. Nenhuma é superior às demais em todo contexto: a escolha depende de quantos backends diferentes precisam ser suportados, de que fronteira de rede o consumidor consegue efetivamente atravessar, e de quanto peso operacional adicional o ambiente tolera.

## Um segredo aplicado manualmente

A forma mais simples de entrega é a mais direta: alguém copia o valor e o aplica manualmente no destino, seja como um `Secret` do Kubernetes, seja como uma variável de ambiente.

Isso funciona sem nenhuma ferramenta adicional, mas tem um custo que só aparece depois: nada em nenhum repositório versionado registra que aquele segredo precisa existir ali, então recuperar o ambiente de um estado limpo depende inteiramente de um runbook e de alguém lembrar (ou documentar) de onde o valor original veio. Quanto mais segredos aplicados dessa forma um ambiente acumula, mais frágil fica a capacidade de reconstruí-lo de forma confiável.

## Operator dedicado a um backend específico

Um operator escrito para falar com um backend específico de gerenciamento de segredos (o Infisical Kubernetes Operator, por exemplo) observa um recurso customizado declarando qual segredo buscar, autentica contra a API daquele backend, e materializa o valor como um `Secret` nativo do Kubernetes.

Isso funciona bem quando o consumidor e o backend estão no mesmo domínio de rede, mas gera um problema estrutural específico quando o próprio backend só é alcançável através de uma camada de rede que depende do cluster já estar funcional para existir (um proxy de borda, um túnel).

Buscar o segredo de bootstrap que permitiria a própria camada de rede subir, atravessando essa mesma camada de rede para alcançar o backend, é uma circularidade real, não um detalhe de implementação a contornar com mais uma tentativa.

Esse tipo de dependência circular tende a aparecer especificamente quando um mecanismo pensado originalmente para segredo de aplicação (rodando depois que a plataforma já está de pé) é reaproveitado para segredo de plataforma (necessário durante o próprio processo de subir a plataforma).

## External Secrets Operator: um padrão comum entre vários backends

Diferente de um operator dedicado a um único backend, o External Secrets Operator (ESO), já coberto em [Secret store externo](secret-store-externo.md), sincroniza valores de múltiplos backends diferentes (Vault, OpenBao, AWS Secrets Manager, e também plataformas como o Infisical, quando um provider compatível existe) através da mesma API declarativa comum.

Isso reduz o acoplamento a um backend específico, permitindo trocar de fornecedor sem reescrever os manifestos consumidores, mas não elimina por si só o problema de circularidade descrito acima: se o backend só é alcançável através da mesma camada de rede que depende do segredo para subir, o ESO herda exatamente a mesma limitação estrutural que um operator dedicado teria, só trocando qual operator específico enfrenta o problema.

## Sealed Secrets: cifrar contra a chave pública do próprio cluster de destino

Sealed Secrets resolve um problema ligeiramente diferente, como versionar um segredo cifrado em Git de forma segura para um cluster específico, não como atravessar uma fronteira de rede entre ambientes diferentes em tempo de execução.

Um controller dedicado, rodando dentro do cluster de destino, gera um par de chaves e expõe só a pública; quem cifra usa essa chave pública para produzir um `SealedSecret`, e só aquele controller específico, com a chave privada que nunca sai do cluster, consegue reverter a operação.

Isso amarra o segredo cifrado a um controller e a um cluster específicos: um `SealedSecret` gerado para um ambiente não abre em outro, e recuperar a capacidade de decifrar depois de reconstruir o cluster do zero depende de ter preservado o par de chaves do controller antes da perda, não apenas o repositório com os `SealedSecret`s cifrados.

## Secrets Store CSI Driver: montar sem materializar um Secret nativo

O Secrets Store CSI Driver segue um caminho estruturalmente diferente dos anteriores: em vez de materializar um `Secret` do Kubernetes a partir de um backend externo, ele monta o valor diretamente como um volume dentro do Pod, sem nunca criar um objeto `Secret` correspondente na API do cluster.

Isso reduz a superfície de exposição do valor. Um `Secret` do Kubernetes, mesmo cifrado em repouso no etcd, ainda é um objeto de API que qualquer identidade com a permissão certa pode ler.

Um valor que nunca vira `Secret` não tem essa superfície de leitura via API. Isso tem um custo: exigir que a aplicação consumidora leia o valor de um arquivo montado em vez de uma variável de ambiente ou de uma referência a `Secret`, uma mudança que pode exigir ajuste na própria aplicação, dependendo de como ela já espera receber configuração sensível.

A disponibilidade de um provider compatível com o backend de segredos específico do ambiente é o fator prático que decide se essa opção está de fato no radar.

## Servidor de segredo dedicado

Um servidor de segredo dedicado, como Vault ou OpenBao (já cobertos em [Secret store externo](secret-store-externo.md)), centraliza o gerenciamento de segredos como um serviço próprio, com controle de acesso granular e trilha de auditoria, tipicamente consumido através de um dos mecanismos já descritos acima (um operator dedicado, o ESO).

Adicionar essa peça a um ambiente que já usa outra plataforma de gerenciamento de segredos levanta uma pergunta de sobreposição direta: se o objetivo é resolver a entrega entre domínios, a pergunta relevante é se esse servidor substitui a plataforma já em uso ou se passa a coexistir como mais uma peça de infraestrutura a operar, cada resposta com um custo de manutenção diferente.

## Identidade de workload em vez de segredo estático

SPIFFE (Secure Production Identity Framework for Everyone) e sua implementação de referência, SPIRE, propõem uma resposta estruturalmente diferente de todas as anteriores.

Em vez de distribuir um segredo estático (uma senha, um token de longa duração) que precisa ser gerado, cifrado, transportado e eventualmente rotacionado, cada workload recebe uma identidade criptográfica própria, verificável, emitida automaticamente com base em atributos que o próprio ambiente de execução já atesta (em qual nó roda, sob qual conta de serviço, qual imagem executa), sem que nenhum segredo de longa duração precise existir em lugar nenhum para provar essa identidade.

Isso elimina uma classe inteira de problema de entrega e rotação de segredo, porque não há mais segredo estático para entregar; o custo é a maturidade e a complexidade de operar essa infraestrutura de identidade, que soma um componente novo e um modelo mental novo para qualquer ambiente que ainda não tenha esse tipo de exigência, e que só se paga quando o número de workloads e a necessidade real de identidade verificável entre eles justificam esse investimento.

## Continue por aqui

[Secret store externo](secret-store-externo.md) cobre o ESO, o par OpenBao/Vault e o mecanismo de auto-unseal em profundidade. [Criptografia de segredos no Git](criptografia-de-segredos-no-git.md) cobre a outra família de solução, cifrar o valor antes de versioná-lo, que resolve um problema relacionado mas distinto deste, onde o segredo mora e como chega até quem o versiona, não como atravessa uma fronteira de rede em tempo de execução.
