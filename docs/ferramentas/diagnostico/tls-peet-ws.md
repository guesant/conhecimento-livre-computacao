# tls.peet.ws

[tls.peet.ws](https://tls.peet.ws/) é um serviço público de diagnóstico que exibe propriedades observáveis da requisição HTTP e da negociação TLS. Ele é útil para uma inspeção pontual de um cliente, de um proxy ou de uma cadeia de rede, desde que o usuário compreenda que os dados serão enviados a um serviço externo.

## Endpoints

- A página principal apresenta uma visualização humana dos sinais observados.
- [`/api/all`](https://tls.peet.ws/api/all) retorna a coleta completa em JSON.
- [`/api/tls`](https://tls.peet.ws/api/tls) concentra os dados relacionados ao TLS.
- [`/api/clean`](https://tls.peet.ws/api/clean) fornece uma versão reduzida da resposta.

A resposta completa pode incluir endereço de origem, User-Agent, versão HTTP, cifras, extensões, versões TLS, grupos, algoritmos de assinatura, JA3, JA4, sinais de HTTP/2 e PeetPrint. O conteúdo é dinâmico e representa a requisição que acabou de ser recebida, portanto não deve ser copiado como fixture estática.

## Uso em diagnóstico

Para consultar o JSON sem a interface gráfica, use:

```bash
curl -sS https://tls.peet.ws/api/all | jq
```

Compare duas execuções somente depois de controlar o navegador, a versão, o proxy, o destino e o caminho de rede. Uma diferença pode estar no cliente ou em um intermediário que termina TLS e cria uma nova conexão.

## Segurança e limites

Não envie tokens, cookies, payloads privados ou cabeçalhos sensíveis para um serviço público. A consulta deve ser usada para diagnóstico, não como dependência de produção, health check ou mecanismo de autorização. Disponibilidade, limites de uso e formato de resposta podem mudar.

Quando a evidência precisar permanecer dentro do ambiente controlado, prefira uma instância própria de [TrackMe](trackme.md) ou outro coletor operado pela equipe. Mesmo em uma instância própria, aplique retenção mínima, controle de acesso e remoção de identificadores que não sejam necessários.

## Relações

- [Fingerprinting de TLS e HTTP](../../seguranca/tls/fingerprinting.md) explica o significado e as limitações dos sinais.
- [Diagnóstico técnico](../../diagnostico/index.md) ajuda a escolher a ferramenta de acordo com a hipótese.

## Fonte

- [tls.peet.ws](https://tls.peet.ws/)
- [tls.peet.ws/api/all](https://tls.peet.ws/api/all)
