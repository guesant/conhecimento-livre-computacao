# Governança

A Internet não é administrada por uma única organização. Seus recursos, padrões, serviços de interconexão e obrigações legais pertencem a camadas diferentes. Confundir essas camadas produz diagnósticos errados, como esperar que um registro de domínios resolva um problema de roteamento ou que uma autoridade de proteção de dados opere servidores DNS.

Esta área separa as principais organizações brasileiras e latino-americanas por responsabilidade:

| Camada | Organização ou serviço | Responsabilidade principal |
| --- | --- | --- |
| Governança nacional | [CGI.br](cgi-br.md) | Diretrizes estratégicas e coordenação multissetorial da Internet no Brasil |
| Execução técnica nacional | [NIC.br](nic-br.md) | Implementação de iniciativas do CGI.br e operação de centros e serviços |
| Nomes de domínio | [Registro.br](registro-br.md) | Registro e manutenção de domínios sob `.br` |
| Interconexão | [IX.br](ix-br.md) | Infraestrutura para troca direta de tráfego entre sistemas autônomos |
| Recursos de numeração regionais | [LACNIC](lacnic.md) | Endereços IPv4, IPv6, ASNs e resolução reversa na América Latina e no Caribe |
| Telecomunicações no Brasil | [Anatel](anatel.md) | Regulação, outorga, fiscalização, qualidade, espectro e homologação de produtos |
| Proteção de dados | [ANPD](anpd.md) | Orientação, regulamentação, fiscalização e sanções no escopo da LGPD |

## Como as responsabilidades se relacionam

Uma organização pode usar um domínio `.br` administrado pelo Registro.br, anunciar um prefixo IP obtido por meio de seu relacionamento com o LACNIC, fazer peering em um ponto do IX.br e ainda precisar cumprir normas da ANPD ao tratar dados pessoais. Esses fatos não transformam as organizações em uma única cadeia administrativa. Cada uma atua sobre um objeto diferente.

O CGI.br define diretrizes e coordena iniciativas de interesse nacional. O NIC.br executa projetos e mantém serviços associados a essa governança. Registro.br e IX.br são serviços técnicos operados dentro desse ecossistema, mas resolvem problemas diferentes: um trata da unicidade e delegação de nomes; o outro, da interconexão de redes.

O LACNIC pertence à camada regional de registros de Internet. Ele administra recursos de numeração e políticas para a América Latina e o Caribe, enquanto o Registro.br administra o espaço de nomes `.br`. A ANPD está em outra dimensão: é uma autoridade administrativa para proteção de dados pessoais, não um registro de recursos de Internet nem uma operadora de infraestrutura.

## O que não deve ser confundido

### Registro, registrador e provedor DNS

Um registry mantém a base de um espaço de nomes. Um registrar ou provedor de serviços intermedeia operações para titulares. Um provedor DNS hospeda zonas autoritativas. O Registro.br é o registry do `.br`, mas registrar um domínio não obriga o titular a usar a hospedagem DNS ou de aplicação do mesmo fornecedor.

### IX e provedor de trânsito

Um Internet Exchange Point fornece uma infraestrutura de interconexão para participantes trocarem tráfego diretamente. Ele não substitui a contratação de trânsito IP, não é um provedor de acesso e não garante que todos os destinos da Internet serão alcançados por peering local.

### LACNIC e Registro.br

O LACNIC trabalha com recursos de numeração, como endereços IP e ASNs. O Registro.br trabalha com nomes sob `.br`. Um domínio pode apontar para endereços administrados por uma organização diferente daquela que administra o domínio.

### Anatel e governança da Internet

A [Anatel](anatel.md) regula os serviços de telecomunicações, a utilização do espectro, a outorga de serviços, a fiscalização de prestadoras e a homologação de produtos sujeitos aos requisitos técnicos. Ela não registra domínios, não atribui ASN, não opera o IX.br e não é uma autoridade geral sobre o conteúdo das aplicações. Uma mesma rede pode estar sujeita à Anatel pela prestação do serviço, ao CGI.br e ao NIC.br por recursos e iniciativas da Internet e à ANPD pelo tratamento de dados pessoais.

### ANPD e governança técnica

A ANPD trata da proteção de dados pessoais e da aplicação da LGPD. Ela pode publicar regras e fiscalizar tratamentos de dados, mas não atribui ASN, não registra domínios, não coordena o IX.br e não substitui órgãos responsáveis por telecomunicações ou pela operação de redes.

## Relação com a governança global

Essas organizações se conectam a uma estrutura global que inclui a IANA, a ICANN, os registros regionais de Internet e organizações de padrões como a IETF. A IANA mantém registros globais de identificadores e delega blocos de endereços aos RIRs. O LACNIC é o RIR da América Latina e do Caribe. Essa camada global não elimina a autonomia operacional e regulatória das organizações nacionais.

## Fontes primárias

- [CGI.br](https://cgi.br/sobre/)
- [NIC.br](https://www.nic.br/sobre/)
- [Registro.br](https://registro.br/)
- [IX.br](https://www.ix.br/sobre)
- [LACNIC](https://www.lacnic.net/pt/web/lacnic/acerca-lacnic)
- [ANPD, competências](https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/competencias)
- [IANA](https://www.iana.org/)
- [ICANN](https://www.icann.org/)
