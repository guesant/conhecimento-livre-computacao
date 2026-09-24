# Resolução, zonas e registros DNS

Uma consulta simples como `dig grafana.internal` devolve uma resposta em milissegundos. Isso esconde uma cadeia de decisões: quem respondeu, se a resposta veio de cache, e quantos servidores foram consultados pelo caminho. Um resolver busca a resposta em nome de um cliente, consultando vários outros servidores se precisar.

Um nameserver autoritativo, por outro lado, guarda a informação de uma zona específica e a entrega diretamente, sem consultar mais ninguém. Um mesmo servidor pode acumular os dois papéis, o caso comum em homelab, mas conceitualmente são funções distintas. Resolver decide para onde perguntar; autoritativo decide qual é a resposta certa para aquela zona.

Numa consulta recursiva completa, o resolvedor consulta primeiro um servidor raiz. Esse servidor não sabe o endereço final, mas sabe quais servidores respondem pela TLD pedida. Ele então consulta a TLD, que por sua vez não sabe o endereço final, mas sabe quais servidores são autoritativos para a zona.

Só o último salto, o servidor autoritativo da zona, tem a resposta de fato. Cada seta de quem responde por é uma delegação: um servidor pai não guarda os registros da zona filha, apenas aponta para quem guarda. O mecanismo exato, com o registro `NS` e o glue record, é o assunto da próxima seção.

Esse caminho completo só acontece quando nenhum servidor intermediário já tem a resposta em cache. Cada registro DNS carrega um TTL (Time To Live, em segundos), o tempo que qualquer resolvedor pode reutilizar essa resposta sem consultar a autoridade de novo. Um TTL de 86400 segundos, ou 24 horas, significa que o resolvedor recursivo responde da própria memória até esse prazo expirar. Só a primeira consulta a um nome percorre a cadeia inteira até a autoridade; as seguintes vêm do cache, o que as torna mais rápidas.

TTLs baixos, de segundos a poucos minutos, fazem sentido para registros que mudam com frequência, como um endpoint atrás de um balanceador com failover ativo. TTLs altos, de horas a dias, reduzem carga na infraestrutura de resolução para registros estáveis, ao custo de propagação mais lenta quando o registro muda. Baixar o TTL antes de uma migração planejada, e restaurá-lo depois, reduz a janela em que clientes ainda respondem com o endereço antigo.

Uma confusão comum ao diagnosticar DNS é tratar "o DNS não funciona" como um problema único. Na prática existem pelo menos duas camadas de resolvedor entre um cliente e a internet. O stub resolver é a peça mais simples da cadeia, o resolvedor do próprio sistema operacional: não faz recursão nenhuma, apenas encaminha toda consulta para o resolvedor configurado.

Em sistemas Linux tradicionais essa configuração vive em `/etc/resolv.conf`. Em distribuições que usam systemd-resolved, esse arquivo costuma ser um link simbólico gerenciado automaticamente. A configuração real por interface, nesse caso, é consultada com `resolvectl status`, não editando o arquivo diretamente, porque uma edição manual tende a ser sobrescrita na próxima atualização de estado.

O resolvedor recursivo é a peça que efetivamente resolve o nome do zero, ou responde a partir do próprio cache se já tiver a resposta. Pode ser um serviço público, o resolvedor do provedor de internet, ou um resolvedor rodando na própria rede local, como o CoreDNS de um cluster K3s. É o caso de [split-horizon DNS](rede/dns/split-horizon.md), em que o resolvedor interno responde de forma diferente do público para o mesmo nome.

Diagnosticar para qual resolvedor a consulta está indo, antes de assumir que a autoridade da zona está com problema, é o primeiro passo prático de qualquer investigação. `dig @<IP>` força a consulta contra um resolvedor específico, isolando se o problema está no resolvedor configurado ou mais adiante na cadeia. Já `dig +trace` reconstrói o caminho real desde os servidores raiz, seguindo a cadeia de delegação manualmente, útil para tornar visível o que o cache normalmente esconde.

## Zonas, delegação e tipos de registro

Uma zona é a porção do espaço de nomes DNS pela qual um conjunto específico de servidores é autoritativo. `example.com` é uma zona, e `sub.example.com`, se for delegada separadamente, é outra zona distinta, mesmo fazendo parte do mesmo domínio visualmente. Essa distinção importa porque autoridade é definida por zona, não por domínio: um servidor pode ser autoritativo para uma zona sem saber nada sobre uma subzona delegada a outro conjunto de servidores.

Toda zona começa com um registro `SOA` (Start of Authority), que não aponta para um endereço, mas descreve a própria zona. Ele guarda qual servidor é a fonte primária dos dados, um contato do responsável, e um número de série incrementado a cada mudança. Também carrega temporizadores que controlam replicação e expiração entre um primário e seus secundários.

Delegar uma zona significa apontar, a partir da zona pai, para os servidores responsáveis pela zona filha, através de um ou mais registros `NS` (Name Server). Quando o servidor raiz delega a TLD .com para seus próprios servidores, o que existe de fato é um conjunto desses registros na zona raiz. Cada um aponta para o nome de um servidor de TLD, sem guardar nenhum dado da zona filha.

Isso esconde um problema sutil quando o próprio servidor de nomes de uma zona tem um nome dentro dela, como um servidor chamado `ns1.example.com` respondendo pela zona `example.com`. Para delegar a esse servidor, o resolvedor precisaria primeiro descobrir seu endereço IP. Isso normalmente exigiria consultar a própria zona ainda inalcançada, um ciclo de referência circular que o glue record resolve, descrito a seguir.

Um glue record é um registro `A` ou `AAAA` do próprio servidor de nomes, publicado diretamente na zona pai junto com o registro de delegação. Ele é entregue na mesma resposta, para que o resolvedor nunca precise fechar o ciclo descrito acima. Glue records só são necessários quando o nome do servidor está dentro, ou abaixo, da própria zona que ele serve.

Um servidor de nomes com nome fora dessa zona não precisa de glue, porque seu endereço já é resolvível normalmente, sem depender da zona delegada. O registro `DS`, publicado da mesma forma ao lado do registro NS na zona pai, estende esse mesmo mecanismo de delegação. Ele forma uma cadeia de assinaturas verificável, o assunto de [DNSSEC, mDNS e registro de domínio](dnssec-mdns-e-registro-de-dominio.md).

Os tipos de registro em uso real neste contexto:

| Registro | Descrição |
| --- | --- |
| `A`/`AAAA` | Apontam um nome para um endereço IPv4 ou IPv6. |
| `CNAME` | É um alias que não pode coexistir com outros registros no mesmo nome, o motivo pelo qual o apex de um domínio raramente usa esse tipo. |
| `TXT` | Guarda texto arbitrário, usado por SPF, DKIM e pelo desafio DNS-01 do ACME que uma ferramenta de emissão de certificado usa para provar controle de um domínio. |
| `MX` | Aponta o servidor de e-mail responsável pelo domínio, com prioridade. |
| `SRV` | Descreve serviço, protocolo, prioridade, peso, porta e alvo no formato `_serviço._protocolo.nome`. |
| `CAA` | Restringe quais autoridades certificadoras podem emitir certificado para o nome. |

O registro `CAA` (RFC 8659) é o único desta lista pensado puramente como controle de segurança, não como dado de roteamento. Ele não muda para onde o tráfego vai, apenas quem tem permissão de emitir certificado para o nome. Um domínio sem nenhum registro `CAA` permite qualquer autoridade certificadora pública.

Publicar um registro restringindo a emissão a uma CA específica reduz a superfície de um certificado fraudulento emitido por engano ou comprometimento em outra CA. A instalação de uma ferramenta de emissão automatizada de certificado não configura `CAA` por si só. É uma camada adicional e opcional que o operador da zona decide publicar.

O `PTR` faz o caminho oposto dos demais tipos, resolvendo um endereço IP de volta para um nome. Isso acontece através de uma zona reversa especial, `in-addr.arpa` para IPv4 e `ip6.arpa` para IPv6, cujo espaço de nomes é construído a partir do próprio endereço, com os octetos invertidos. Configurar esse registro corretamente depende de quem controla a zona reversa, tipicamente o provedor de hospedagem ou o registro regional responsável pelo bloco de IP, não o dono do domínio direto.

Na prática ele importa por dois motivos concretos. Servidores de e-mail costumam rejeitar ou penalizar conexões de um IP sem esse registro configurado. Ferramentas de log também o usam para resolver o endereço de origem de uma conexão de volta a um nome legível.

## Continue por aqui

[DNSSEC, mDNS e registro de domínio](dnssec-mdns-e-registro-de-dominio.md) cobre como um resolvedor confirma que uma resposta não foi forjada, o caso em que não existe servidor DNS nenhum, e a diferença entre resolução e dados de registro; [servidores DNS e conectividade WAN](servidores-dns-e-conectividade-wan.md) cobre os softwares que implementam cada papel e a decisão de rede que antecede qualquer consulta DNS.
