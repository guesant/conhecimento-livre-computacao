# Can I Use

[Can I Use](https://caniuse.com/) apresenta tabelas de compatibilidade para recursos da plataforma web. O serviço organiza o suporte por navegador e versão, diferencia suporte completo, parcial, ausente e desconhecido e permite consultar recursos específicos.

## Quando consultar

Consulte o Can I Use quando a escolha de uma API, propriedade CSS, formato ou recurso de plataforma depender dos navegadores atendidos pela aplicação. A tabela é especialmente útil para identificar o menor navegador suportado, decidir se uma alternativa é necessária e localizar mudanças de suporte entre versões.

O resultado precisa ser interpretado junto com a política de suporte do produto. Uma porcentagem global de uso não decide sozinha se um recurso pode ser adotado, porque um único navegador corporativo ou uma versão embarcada pode ser obrigatório no cenário.

## Como interpretar os dados

Observe a versão do navegador, o estado do suporte e as notas associadas ao recurso. Suporte parcial pode depender de uma opção de configuração, de uma parte da especificação ou de uma limitação que afeta exatamente o uso planejado. Recursos marcados como desconhecidos exigem teste ou consulta adicional.

O Can I Use é uma fonte de compatibilidade, não uma especificação. Use a [MDN Web Docs](mdn.md) para entender o comportamento da API e consulte a documentação normativa ou do navegador quando uma diferença de implementação tiver impacto de segurança ou de correção.

## Limites

Os dados podem mudar conforme novas versões são publicadas e não substituem um teste automatizado ou manual. A aplicação deve declarar seus navegadores alvo, testar os caminhos críticos e tratar degradação progressiva quando a capacidade não estiver disponível.

## Relações

- Use [MDN Web Docs](mdn.md) para o contrato técnico do recurso.
- Use [TLS e fingerprinting](../seguranca/tls/fingerprinting.md) para investigar diferenças observadas na conexão HTTP ou TLS.

## Fonte

- [Can I Use](https://caniuse.com/)
