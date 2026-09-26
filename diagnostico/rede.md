# Diagnóstico de rede

Um problema de rede real raramente aponta de cara para qual peça falhou; o
sintoma costuma ser uma frase vaga, como uma conexão que cai ou um serviço
inacessível. A ordem certa de investigação começa pelas verificações mais
baratas e locais, que descartam uma classe inteira de causas de uma vez, e só
avança para ferramentas mais caras quando as anteriores não explicam o
sintoma.

A primeira pergunta nunca deveria ser se o destino está acessível, e sim se a
peça mais próxima existe e está no estado esperado. Confirmar que a interface
está `UP`, com `LOWER_UP` e o endereço correto atribuído, tratado em
[interfaces, rotas e camada 2 no Linux](../interfaces-rotas-e-l2-no-linux.md),
elimina de uma vez toda a classe de problemas de camada física.

Antes de pensar em rede externa, vale confirmar que existe um processo
escutando na porta e na interface esperadas. `ss -tlnp` lista sockets TCP em
escuta com o processo dono.

Um serviço escutando em `127.0.0.1:8080` nunca responde a uma conexão vinda de
outra máquina, mesmo com interface, rota e firewall corretos, porque o
processo simplesmente não aceita conexões chegando por uma interface
diferente de loopback. Esse sintoma se parece com firewall bloqueando, mas a
causa está inteiramente do lado da aplicação.

Com interface e serviço confirmados, `ping` testa a hipótese mais simples de
conectividade, primeiro para o próprio host, depois para o gateway padrão,
depois para o destino final. Cada etapa isola um segmento diferente do
caminho: falhar em alcançar o gateway aponta para um problema local, enquanto
alcançar o gateway mas não o destino aponta para algo além do host.

A ausência de resposta não é prova definitiva, porque o ICMP pode estar
bloqueado por um firewall intermediário mesmo com o serviço real acessível por
outro protocolo.

Quando `ping` falha para o destino final mas funciona para o gateway, o próximo
passo é descobrir em qual salto o caminho quebra. O `traceroute` mostra uma
passagem única pela rota.

O `mtr` combina as duas ideias, ping e traceroute, atualizando estatísticas de
perda e latência por salto continuamente, mais útil para distinguir uma falha
total de um salto apenas instável. Um salto marcado como `*` não prova rota
quebrada por si só, porque roteadores intermediários costumam limitar
deliberadamente esse tipo de tráfego.

Quando a resposta é que a rede alcança o destino, mas o comportamento
observado não é o esperado, a única forma de confirmar o que está de fato
acontecendo é capturar o tráfego real com o `tcpdump`. É deliberadamente a
última ferramenta deste fluxo, porque interpretar uma captura de pacotes sem
antes eliminar interface, serviço, rota e alcançabilidade básica é gastar
esforço analisando dados que uma verificação mais barata já teria explicado.

O `tc` não diagnostica conectividade: governa como o kernel enfileira,
prioriza, limita ou descarta pacotes numa interface, através de disciplinas de
fila, classes hierárquicas e filtros que decidem em qual classe cada pacote
entra. Um sintoma que passa por todas as etapas anteriores sem explicação,
sobretudo lento mas não totalmente fora do ar, pode ter origem numa política
de `tc` aplicada deliberadamente, como limitação de banda, em vez de uma
falha real.

## Continue por aqui

[Netfilter e nftables](../netfilter-nftables-e-diagnostico.md) explica o
firewall do kernel. O [cookbook de comandos de rede e DNS](../../referencia/comandos-de-rede-e-dns.md)
reúne a sintaxe rápida de `ping`, `ss` e `mtr`.
