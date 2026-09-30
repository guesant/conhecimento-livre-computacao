# Usage Control

Usage Control, UCON, amplia a autorização para considerar o uso contínuo de um recurso. Em vez de decidir apenas no instante de abertura, o sistema pode reavaliar atributos, impor obrigações e verificar condições durante a execução.

## Componentes

Uma decisão UCON pode envolver:

- **authorization**, se o sujeito possui o direito inicial;
- **obligation**, uma ação que deve ser executada antes, durante ou depois do uso;
- **condition**, um requisito ambiental que não é necessariamente uma propriedade do sujeito ou recurso;
- **continuity**, a possibilidade de reavaliar enquanto o uso continua;
- **attribute mutability**, atributos que podem mudar durante a sessão.

Um exemplo é permitir que uma sessão leia dados enquanto a licença está válida, exigir registro de auditoria durante o uso e interromper o acesso quando a conta for suspensa.

## Diferença para autorização pontual

Em um modelo pontual, a aplicação decide quando abre o recurso e tende a confiar nessa decisão até o fim da operação. UCON pergunta se a autorização continua válida, se as obrigações foram cumpridas e se as condições permanecem satisfeitas.

Isso é relevante para streaming, licenças, processamento longo, acesso a dados sensíveis e operações que atravessam fronteiras administrativas.

## Obrigações

Uma obrigação pode exigir registrar um uso, aplicar marca d'água, atualizar consumo, notificar um responsável ou apagar uma cópia ao final da sessão. A autorização só deve prosseguir quando a obrigação puder ser cumprida ou quando a política declarar uma compensação segura.

Condições são fatos externos, como rede aprovada, licença válida ou estado do dispositivo. A obrigação é uma ação que o sistema deve executar. Confundir os dois leva a políticas que concedem acesso sem garantir o efeito operacional esperado.

## Custos

Reavaliar continuamente pode ser caro e difícil de sincronizar. A interrupção precisa ser segura, o componente que mantém o uso deve ser observável e o sistema precisa definir o que acontece quando o PDP ou a fonte de atributos não responde.

Não transforme todo request HTTP em uma sessão UCON sem necessidade. Para operações curtas, um check com revogação e expiração bem definidos costuma ser mais simples.

## Relação com tokens

Um token com expiração representa somente uma janela temporal. Ele não garante que obrigações foram cumpridas nem que a conta continua autorizada. Introspection, leases, heartbeats e canais de revogação podem aproximar um sistema de UCON, mas introduzem tráfego e estado.

## Falha durante o uso

Defina se a sessão termina imediatamente, entra em modo somente leitura, aguarda recuperação ou conclui apenas uma operação já iniciada. A escolha depende do risco. Um download de dados sensíveis pode precisar ser interrompido; uma transação já confirmada pode exigir compensação em vez de rollback impossível.

## Casos adequados

Considere UCON para licenciamento, consumo de conteúdo, uso de dados regulados, jobs longos e delegações que podem ser revogadas durante a execução. Defina métricas para tempo até revogação, sessões ativas, falhas de reavaliação e ações compensatórias.

## Fontes

- [NIST, access control models and policies](https://csrc.nist.gov/pubs/sp/800/192/final)
- [NIST, meta model for access control](https://csrc.nist.gov/pubs/conference/2008/06/11/a-meta-model-for-access-control/final)
