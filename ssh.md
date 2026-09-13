# SSH

SSH (Secure Shell) é o protocolo que permite abrir uma sessão de terminal remota, ou copiar arquivos, ou encapsular outras conexões, de forma cifrada, sobre uma rede que pode não ser confiável. A forma mais comum de autenticação não é senha, é um par de chaves: uma chave privada, que fica só na máquina de quem conecta e nunca é enviada pela rede, e uma chave pública, que é copiada para a máquina de destino e autoriza quem possui a chave privada correspondente. A segurança do esquema depende inteiramente da chave privada continuar privada; copiá-la para outra máquina, ou deixá-la sem senha própria (passphrase) num disco que pode ser roubado, anula boa parte da proteção.

## Chave pessoal versus deploy key

Uma chave pessoal identifica uma pessoa e normalmente autoriza acesso a várias máquinas e serviços diferentes; se ela vazar, o raio de dano é tudo que aquela pessoa podia acessar. Uma **deploy key** é uma chave gerada especificamente para uma automação ou uma máquina, autorizada só para um destino específico (por exemplo, só para clonar um repositório git, ou só para acessar um servidor específico); se ela vazar, o raio de dano fica contido àquele destino único. Separar chaves por finalidade, em vez de reusar a mesma chave pessoal em toda automação, é o que torna um vazamento administrável em vez de catastrófico.

## `~/.ssh/config` e `known_hosts`

O arquivo `~/.ssh/config` permite declarar, por hospedeiro, qual chave usar, qual usuário, qual porta, e outras opções, sem precisar repetir tudo isso na linha de comando toda vez. O arquivo `~/.ssh/known_hosts` guarda a chave pública de cada servidor ao qual já se conectou; na primeira conexão, o cliente pergunta se aquela chave (a "impressão digital" do servidor) deve ser aceita, e da próxima vez em diante ele compara silenciosamente. Se a chave do servidor mudar sem explicação (reinstalação legítima à parte), o cliente recusa a conexão por padrão, porque isso é exatamente o sinal que um ataque de interceptação (man-in-the-middle) produziria.

A opção `IdentitiesOnly=yes` força o cliente a oferecer só a chave configurada explicitamente para aquele hospedeiro, em vez de tentar todas as chaves carregadas no agente SSH em sequência; isso evita que um servidor de destino descubra, pela ordem de tentativas, quais outras chaves (e portanto quais outros destinos) o cliente possui.

## Tunelamento

Além de abrir uma sessão de terminal, uma conexão SSH pode encapsular outro tráfego de rede: um túnel local expõe uma porta remota como se fosse local, um túnel remoto faz o inverso, e um túnel dinâmico funciona como um proxy SOCKS genérico. Isso é útil para alcançar um serviço que só escuta numa rede interna (por exemplo, um banco de dados que não deveria estar exposto na internet) a partir de fora, usando o próprio servidor SSH como ponte, sem abrir uma porta adicional exposta.

## Continue por aqui

O modelo de ameaças deste repositório, em [Modelo de ameaças](../arquitetura/modelo-de-ameacas.md), detalha a fronteira real entre a máquina do operador e o node via SSH, incluindo o que fica fora desse controle. A role real que aplica hardening de SSH no node está documentada em [Ansible: as roles do bootstrap](../arquitetura/ansible.md).
