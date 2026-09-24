# Firewall do host e portas publicadas

UFW (Uncomplicated Firewall) é uma interface de linha de comando sobre o mesmo netfilter que [firewalld](firewalld.md) configura, pensada para um firewall de host único com sintaxe curta, sem exigir conhecimento direto de nftables. O modelo é uma lista simples de regras, avaliada na ordem em que aparecem, mais uma política padrão por direção (`incoming`, `outgoing`, `routed`) aplicada quando nenhuma regra corresponde; a convenção recomendada é `deny incoming`/`allow outgoing`, bloquear tudo por padrão e liberar explicitamente o necessário. Uma regra pode ser restrita por porta, protocolo, interface de entrada e origem; regras adicionadas com o UFW já ativo têm efeito imediato, mas mudar a política padrão exige `ufw reload` para valer nas conexões novas. Por baixo, o UFW gera regras iptables/nftables como qualquer outra ferramenta de alto nível.

Nenhuma das duas ferramentas, UFW ou firewalld, é estritamente superior; ambas configuram o mesmo netfilter com modelos de organização diferentes. UFW usa uma lista linear que vale para o host inteiro, com curva de aprendizado baixa para casos simples; firewalld associa cada interface a uma zona nomeada, com curva de aprendizado maior mas modelo nativo para múltiplas interfaces com nível de confiança distinto (uma pública, uma de gerenciamento privada). UFW tende a ser a escolha mais simples para um host com uma única interface relevante e uma política de confiança única, o caso comum de um nó K3s single-node; firewalld tende a ser mais adequado quando existem várias interfaces exigindo tratamento diferente, ou quando regras combinando múltiplas condições (rich rules) aparecem com frequência. Rodar as duas no mesmo host cria uma segunda fonte de verdade, já que as duas manipulam as mesmas regras nftables por baixo e podem se sobrescrever sem aviso.

## O que nenhum firewall de host protege sozinho

Uma porta publicada pelo Docker pode não ser filtrada da forma que UFW ou firewalld sugerem. Com UFW, o Docker pode encaminhar o tráfego publicado antes que ele passe pelas chains normalmente geridas pelo UFW; com firewalld, o Docker cria sua própria zona, cujo target padrão é `ACCEPT`. Uma porta publicada não deve ser considerada protegida só porque o firewall do host tem política padrão de bloqueio, porque o Docker está inserindo regras próprias nas mesmas chains do netfilter, e a ordem de avaliação, não a política do firewall de alto nível, decide o que acontece primeiro. Para um serviço que só deve ser acessado pelo próprio host, o bind correto é no loopback:

```yaml
ports:
  - "127.0.0.1:5432:5432"
```

Para um serviço que deve ser acessado só por uma rede específica, o bind é no endereço da interface correspondente:

```yaml
ports:
  - "192.168.1.10:5432:5432"
```

Publicar como `5432:5432`, sem endereço, normalmente faz bind em todas as interfaces disponíveis, incluindo qualquer uma exposta publicamente, mesmo que o operador só pretendesse alcançabilidade local ou interna.

## Continue por aqui

[Netfilter, nftables e diagnóstico de rede](netfilter-nftables-e-diagnostico.md) cobre o mecanismo comum de chains e prioridade por trás desse conflito entre Docker e o firewall de host; [firewalld](firewalld.md) documenta como este cluster realmente configura o firewall do node, incluindo o `--permanent` e o recarregamento atômico que o UFW resolve de forma mais simples, mas menos expressiva.
