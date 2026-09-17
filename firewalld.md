# firewalld

firewalld é um serviço de gestão de firewall para Linux que, por baixo, configura as mesmas tabelas de filtragem de pacote do kernel (nftables nas distribuições atuais, iptables nas mais antigas), mas expõe um modelo mais alto nível baseado em zonas, em vez de exigir que cada regra seja escrita diretamente na sintaxe de baixo nível dessas tabelas. Isso facilita raciocinar sobre a política de firewall como um todo, ao custo de uma camada de abstração a mais entre a regra declarada e o pacote de rede real.

## Zonas

Uma zona agrupa um nível de confiança e um conjunto de regras associado: a zona `public`, por exemplo, normalmente aceita bem menos tráfego de entrada do que uma zona `trusted`. Uma interface de rede, ou uma origem específica (um endereço ou uma faixa de CIDR), é atribuída a uma zona, e a partir daí segue as regras dessa zona. Isso permite, por exemplo, que uma interface exposta à internet fique numa zona restritiva enquanto uma interface só de rede interna fica numa zona mais permissiva, sem precisar duplicar regra por regra para cada interface.

## Regra permanente versus regra de runtime

Toda mudança em firewalld pode ser aplicada de duas formas: só na configuração em memória, que vale até o próximo reinício do serviço (runtime), ou também gravada em disco, que sobrevive a um reinício (`--permanent`). Uma regra aplicada só em runtime e nunca tornada permanente desaparece silenciosamente na próxima reinicialização da máquina, o que é uma causa comum e discreta de "a regra que eu apliquei sumiu".

## O recarregamento atômico

Aplicar uma regra permanente não muda o comportamento em runtime imediatamente; é preciso um `reload` para que a configuração permanente seja recarregada e passe a valer. O ponto crítico é que esse `reload` em firewalld é atômico: ele não derruba as conexões existentes nem deixa a máquina momentaneamente sem nenhuma regra ativa enquanto recarrega, ao contrário de uma estratégia ingênua de "apagar tudo e reaplicar", que abriria uma janela real, ainda que curta, em que o firewall não está protegendo nada. Essa garantia é o que torna seguro alterar a regra de firewall de uma máquina remota pela própria conexão que aquela regra protege, sem correr o risco de se trancar para fora no meio do processo.

## Como um bloqueador de intrusão se encaixa no firewall

Uma ferramenta como o fail2ban não filtra pacote nenhum por conta própria: ela só lê uma fonte de eventos, geralmente um arquivo de log de autenticação ou, num sistema baseado em systemd, o próprio journal, decide que uma origem deve ser banida depois de tentativas repetidas, e delega o bloqueio de verdade a um backend. Numa máquina onde o firewalld já administra as regras, o backend mais coerente é um ipset que o próprio firewalld gerencia, em vez de uma regra escrita direto na tabela do kernel por fora dele: assim as duas ferramentas nunca competem pela mesma configuração, e o firewalld continua sendo a única fonte da verdade sobre o que está bloqueado na máquina.

## Continue por aqui

[Modelo de ameaças](../arquitetura/modelo-de-ameacas.md) explica por que uma zona de firewall só filtra a chain `INPUT`, e por que isso não protege uma porta exposta por uma `Service` do Kubernetes do tipo `LoadBalancer` ou `NodePort`, cujo tráfego passa pela chain `FORWARD` depois de um DNAT. A role real de firewall do hl-infrastructure está documentada em [Ansible: as roles do bootstrap](../arquitetura/ansible.md).
