# Manutenção preditiva

Manutenção preditiva usa a condição observada do sistema para decidir quando intervir. Em vez de reiniciar ou substituir um componente apenas porque passou determinado tempo, a equipe acompanha sinais de degradação e age quando a probabilidade de falha ou o custo de esperar ultrapassa um limite.

Em software, a condição pode ser representada por erro, latência, fila, uso de disco, idade de certificado, crescimento de banco, taxa de retries, saturação de conexões, consumo de memória, pausas do garbage collector, falhas de backup ou divergência de réplicas. Em hardware, podem entrar temperatura, desgaste, SMART, vibração e energia. A ideia é a mesma: usar observação para escolher o momento da intervenção.

## Da medição à decisão

A manutenção preditiva precisa de sinal confiável, linha de base, regra de decisão e ação executável. A linha de base descreve o comportamento normal por horário, carga, versão e ambiente. A regra pode ser um limiar, uma tendência, um intervalo de confiança ou um modelo de anomalia.

Uma regra útil também considera lead time. Se uma tendência indica que o volume de disco atingirá o limite em três dias, há tempo para expandir o volume ou revisar retenção. Se indica falha em dez minutos, pode ser necessário reduzir tráfego, drenar o workload ou restaurar uma réplica. A previsão só é operacionalmente útil quando a ação cabe na janela disponível.

## Exemplos

Um banco pode ser analisado pelo crescimento de WAL, bloat, locks, latência e espaço. Um cluster pode ser analisado por pressão de memória, evictions, falha de probes e saturação de nós. Uma aplicação pode ser analisada por p95, p99, taxa de erro, retries, filas e reinícios. Um certificado pode ser renovado quando a validade restante atingir um limite, e não apenas em uma data fixa.

A intervenção pode ser automática ou exigir aprovação. Expansão de um volume e remoção de cache temporário podem ser automatizadas com limites. Migração de dados, redução de retenção e alteração de capacidade podem exigir revisão humana. A política deve declarar quando a automação para e qual evidência libera a mudança.

## Riscos

A manutenção preditiva falha quando os sinais são incompletos, quando há mudanças de instrumentação ou quando a equipe confunde correlação com causa. Um alerta baseado em limiar fixo pode ignorar sazonalidade. Um modelo pode aprender um comportamento já degradado como se fosse normal. Um falso positivo pode causar uma intervenção perigosa.

Toda regra deve ter observabilidade do próprio detector. Registre quantas previsões foram feitas, quantas ações ocorreram, quantas eram necessárias e quantas falhas escaparam. Recalibre após deploys, migrations, mudanças de tráfego e mudanças de hardware.

Manutenção preditiva complementa a [manutenção preventiva](manutencao-preventiva.md) e reduz intervenções desnecessárias. Ela não substitui [manutenção corretiva](manutencao-corretiva.md), que é necessária quando uma falha já afetou o sistema.
