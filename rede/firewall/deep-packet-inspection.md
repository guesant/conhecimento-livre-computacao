# Deep Packet Inspection

Deep Packet Inspection, ou DPI, é uma técnica de análise de tráfego que examina
mais do que os campos necessários para encaminhar um pacote. O mecanismo pode
combinar cabeçalhos, estado da conexão, metadados, padrões de protocolo e, quando
possui acesso ao conteúdo, dados da camada de aplicação para classificar ou aplicar
uma política.

DPI não é sinônimo de firewall. Um firewall pode filtrar somente endereços, portas e
estado. Um IDS pode inspecionar tráfego e apenas alertar. Um proxy pode terminar a
conexão e compreender HTTP. DPI descreve principalmente a profundidade e o método de
análise, não uma posição específica nem uma decisão obrigatória.

## O que pode ser observado

Um analisador pode combinar dimensões diferentes:

| Dimensão | Exemplos | Limitação |
| --- | --- | --- |
| Cabeçalho | IP, porta, protocolo, tamanho e direção | Não identifica necessariamente a aplicação |
| Estado | Handshake, sequência e relação entre fluxos | Exige memória e expiração correta |
| Protocolo | DNS, HTTP, TLS, QUIC e outros formatos | Precisa acompanhar versões e extensões |
| Conteúdo | URI, método, payload ou comando | Depende de texto claro ou terminação controlada |
| Comportamento | Frequência, volume, duração e padrão de pacotes | Pode gerar inferências e falsos positivos |
| Identidade | Usuário, dispositivo, workload ou certificado | Depende de associação confiável |

A inspeção pode procurar não conformidade de protocolo, malware, indicadores de
intrusão, exfiltração, abuso, uso de aplicação ou critérios administrativos. Também
pode classificar fluxos para qualidade de serviço, medição e planejamento.

## Onde a inspeção acontece

Em modo passivo, um TAP, espelhamento de porta ou sensor recebe uma cópia do tráfego.
Esse arranjo reduz o risco de interromper o encaminhamento, mas não consegue bloquear
diretamente sem um componente adicional.

Em modo inline, o dispositivo fica no caminho do tráfego e pode permitir, atrasar,
rejeitar, redirecionar ou encerrar a conexão. A posição inline torna a política
efetiva, mas adiciona latência, um domínio de falha e a necessidade de definir o que
acontece quando o inspetor está indisponível.

Um proxy de aplicação trabalha em uma camada ainda diferente. Ele termina uma sessão,
interpreta o protocolo e inicia outra sessão. Isso permite política rica para HTTP,
SMTP ou outros protocolos, mas modifica a topologia de confiança e exige tratar
certificados, autenticação, streaming e compatibilidade.

## Criptografia e limites

TLS, IPsec, QUIC e outros mecanismos reduzem o conteúdo disponível para um observador
intermediário. Mesmo quando o payload está protegido, endereço, tamanho, tempo,
direção, frequência, handshake e outros metadados ainda podem permitir análise de
tráfego.

Para ler conteúdo TLS, um equipamento precisa estar em uma das pontas ou atuar como
terminador autorizado, normalmente com uma autoridade certificadora confiada pelos
clientes. Isso transforma a inspeção em uma decisão de segurança e privacidade, não
apenas em uma configuração de rede. A chave privada, a cadeia de confiança, o
armazenamento de evidências e a exclusão de dados sensíveis precisam ser governados.

Não se deve concluir que criptografia tornou o tráfego invisível, nem que DPI sempre
consegue ler a aplicação. A disponibilidade de conteúdo depende do protocolo, do
local da inspeção, da configuração e das chaves. O [RFC 8404](https://www.rfc-editor.org/rfc/rfc8404.html)
descreve como a criptografia pervasiva altera operações de rede, inclusive inspeção,
otimização e diagnóstico.

## Usos legítimos e riscos

DPI pode fazer parte de IDS, IPS, prevenção de malware, filtragem de conteúdo,
controle de egress, classificação de aplicações, QoS, diagnóstico e detecção de
anomalias. Em uma rede corporativa, o uso precisa ter finalidade, escopo, retenção,
acesso e base legal adequados.

Os riscos incluem vigilância indevida, coleta excessiva, exposição de credenciais,
quebra de confidencialidade, bloqueio de tráfego legítimo, incompatibilidade com
protocolos novos e degradação de desempenho. Inspecionar payload não é automaticamente
mais seguro: uma regra incorreta pode impedir recuperação, atualização ou comunicação
de emergência.

## Operação e engenharia

Uma implantação responsável define antes:

- quais fluxos serão observados e por quê;
- se o sensor será passivo ou inline;
- quais protocolos e versões serão suportados;
- limites de CPU, memória, conexões e throughput;
- comportamento fail-open ou fail-closed;
- como os eventos serão correlacionados sem registrar segredos;
- como regras serão testadas, versionadas e revertidas;
- quais dados terão retenção e quem poderá acessá-los.

Monitore perda de pacotes, fila de inspeção, latência, conexões descartadas, falhas
de decodificação, atualização de assinaturas e divergência entre tráfego permitido e
tráfego efetivamente entregue. Separe falha do inspetor de bloqueio intencional. Um
alerta que apenas informa que houve bloqueio não explica se a política funcionou ou se
o próprio mecanismo está degradado.

## Relações

- [Tipos de firewall](index.md) organiza filtros stateless, stateful, WAF, IDS e IPS.
- [Netfilter](netfilter.md) explica o caminho
  de filtragem no Linux.
- [TLS](../../seguranca/tls/index.md) explica a proteção criptográfica que
  limita inspeção intermediária.
- [Censura de rede](../censura/index.md) mostra como técnicas de classificação e
  filtragem podem ser usadas em escala estatal.

## Fontes

- [RFC 8404, Effects of Pervasive Encryption on Operators](https://www.rfc-editor.org/rfc/rfc8404.html)
- [RFC 9065, Transport Header Confidentiality](https://www.rfc-editor.org/rfc/rfc9065.html)
- [RFC 9505, Survey of Worldwide Censorship Techniques](https://www.rfc-editor.org/rfc/rfc9505.html)
