# Qualidade preditiva

Qualidade preditiva usa sinais históricos e atuais para estimar que uma degradação ou falha pode ocorrer no futuro. Ela não espera que o erro seja explícito. Procura mudanças em tendências, correlações e condições precursoras para permitir uma ação antes que o impacto alcance o usuário.

O termo não exige aprendizado de máquina. Um alerta de espaço em disco baseado em crescimento observado, uma projeção de saturação de conexões e uma regra que detecta aumento de p99 são formas preditivas. Modelos estatísticos e algoritmos de machine learning podem ajudar quando há volume e qualidade de dados, mas não transformam uma previsão em certeza.

## Sinais preditivos

Os melhores sinais são anteriores ao sintoma final. Exemplos incluem crescimento de WAL, aumento de tempo de fila, redução de cache hit, tendência de consumo de disco, elevação de retries, esgotamento de pool de conexões, crescimento de objetos em storage, falhas de renovação e aumento de cardinalidade.

Um sinal precisa de contexto. A mesma CPU alta pode ser capacidade normal durante um batch ou indício de saturação para uma API interativa. O modelo deve considerar horário, carga, versão, região, sazonalidade e relação com outros sinais. Métricas isoladas tendem a gerar falsos positivos.

## Pipeline de previsão

Uma implementação madura separa coleta, qualidade do dado, cálculo, decisão e ação. Primeiro, os dados são coletados com timestamp, unidade, origem e versão. Depois são tratados valores ausentes, mudanças de cardinalidade, reinícios, outliers e alterações de instrumentação. O cálculo pode usar limiar, média móvel, regressão, sazonalidade, anomalia ou modelo supervisionado.

O resultado precisa ser traduzido em ação operacional. Uma previsão de disco cheio pode abrir uma tarefa de expansão, aumentar retenção, remover dados temporários ou reduzir geração. Uma previsão de expiração pode iniciar rotação controlada. Uma previsão de saturação pode antecipar scaling, reduzir concorrência ou bloquear uma promoção.

## Precisão e custo

Previsões erradas têm custo. Falso positivo consome tempo e pode causar mudanças desnecessárias. Falso negativo oferece confiança indevida e deixa a falha avançar. Por isso, a qualidade preditiva deve acompanhar precisão, recall, lead time, custo por alerta e resultado da ação tomada.

O horizonte também importa. Uma previsão com cinco minutos de antecedência pode ser útil para reduzir tráfego, mas insuficiente para comprar capacidade ou executar uma migração. O alerta deve indicar a janela estimada, a incerteza, a evidência e o prazo recomendado para agir.

## Limitações

Mudanças de arquitetura, releases, migrations e mudanças de tráfego podem invalidar dados históricos. Um modelo treinado em comportamento normal pode considerar uma nova operação legítima como anomalia. Todo detector precisa de revisão após grandes mudanças e de um caminho para silenciar ou recalibrar a previsão.

Qualidade preditiva não substitui observabilidade básica nem resposta. Sem métricas confiáveis, não há previsão confiável. Sem runbook e owner, a previsão apenas antecipa uma falha sem produzir benefício. O resultado deve entrar no ciclo de prevenção, manutenção e resposta reativa.
