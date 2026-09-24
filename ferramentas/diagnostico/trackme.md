# TrackMe

[TrackMe](https://github.com/pagpeter/TrackMe) é uma aplicação em Go para fingerprinting passivo de requisições. O projeto expõe servidores HTTP de baixo nível para observar TLS, HTTP/1.1, HTTP/2, cabeçalhos, ordem de campos e frames, sendo adequado para laboratório e investigação de comportamento de clientes.

## O que o projeto oferece

O projeto disponibiliza endpoints para consultar a observação completa, os dados TLS, uma resposta reduzida, contagem de requisições e busca por alguns fingerprints. A resposta pode incluir JA3, JA4, fingerprint de HTTP/2, PeetPrint e informações da requisição.

O uso de um servidor de baixo nível é importante para o objetivo do projeto: um framework web comum pode normalizar ou esconder parte dos dados antes que a aplicação consiga observá-los. Isso torna o TrackMe útil para comparar clientes em uma rede controlada e para estudar o efeito de proxies e versões de bibliotecas.

## Execução e operação

O repositório apresenta execução por Docker e por Go. Em ambos os casos, trate o ambiente como uma ferramenta de diagnóstico, forneça certificados adequados para os testes TLS e restrinja a exposição de rede. Uma instância pública pode coletar endereços IP, User-Agent, cabeçalhos e outras informações de conexão.

Antes de habilitar persistência ou endpoints de busca, defina retenção, autenticação, autorização e proteção contra abuso. Não confunda um ambiente de laboratório com um serviço pronto para receber tráfego de usuários sem endurecimento adicional.

## Interpretação

As impressões retornadas pelo TrackMe são sinais de implementação e de caminho de rede. Elas não identificam de forma confiável uma pessoa, um dispositivo ou uma organização. Navegadores podem mudar a ordem dos campos, proxies podem terminar TLS e clientes diferentes podem produzir sinais semelhantes.

Use o projeto para testar uma hipótese delimitada, documentando cliente, versão, configuração, ponto de coleta e caminho de rede. Compare as respostas sem guardar metadados que não sejam necessários para a investigação.

## Relações

- [Fingerprinting de TLS e HTTP](../../seguranca/tls/fingerprinting.md) explica o modelo e as limitações da técnica.
- [tls.peet.ws](tls-peet-ws.md) oferece uma alternativa hospedada para inspeções pontuais.

## Fonte

- [TrackMe no GitHub](https://github.com/pagpeter/TrackMe)
