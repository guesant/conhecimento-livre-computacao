# Manutenção preventiva

Manutenção preventiva é a execução planejada de atividades em intervalos de tempo, volume, versão ou uso para reduzir a probabilidade de falha. Ela ocorre mesmo quando o componente ainda parece saudável. O intervalo deve considerar risco, desgaste, custo de indisponibilidade, janela operacional, dependências e evidência histórica.

## Exemplos em software

Em software, a manutenção preventiva pode incluir atualização de dependências, aplicação de patches, renovação de certificados, rotação de credenciais, limpeza de dados temporários, compactação, revisão de índices, teste de restauração, validação de backups, atualização de imagens, revisão de permissões e remoção de versões sem suporte.

Também inclui revisar alertas, validar runbooks, testar failover, verificar jobs recorrentes, conferir espaço para WAL, revisar filas e repetir exercícios de rollback. Um sistema pode continuar funcionando enquanto acumula risco operacional. A ausência de falha hoje não prova que a manutenção pode ser adiada indefinidamente.

## Agendamento

Cada tarefa precisa de owner, frequência, duração estimada, pré-condições, evidência esperada e plano de interrupção. Tarefas que exigem mudança devem ter janela, comunicação e rollback. Tarefas que podem ser automatizadas devem ser idempotentes e registrar o resultado.

O calendário deve evitar concentrar riscos. Atualizar todas as dependências, migrar banco, trocar certificado e reiniciar componentes na mesma janela dificulta atribuir causa quando algo falha. Mudanças devem ser agrupadas por dependência técnica, mas separadas quando a combinação aumenta o domínio de falha.

## Vantagens e limites

Manutenção preventiva reduz exposição a vulnerabilidades conhecidas, evita acumulação de lixo, conserva capacidade e mantém o sistema em uma faixa suportada. Ela é especialmente útil quando falhas têm consequências graves ou quando a correção emergencial é difícil.

Seu limite é executar trabalho sem necessidade imediata. Reinícios frequentes podem introduzir indisponibilidade. Atualizações por calendário podem não acompanhar o estado real. Limpezas agressivas podem apagar dados ainda úteis. A manutenção deve ser guiada por risco e métricas, não por uma regra cega de periodicidade.

## Verificação

Uma atividade preventiva só deve ser considerada concluída quando o efeito foi verificado. Depois de renovar um certificado, teste a cadeia e os consumidores. Depois de executar uma limpeza, confirme retenção e espaço recuperado. Depois de atualizar uma dependência, execute testes, verifique o artefato e observe métricas. Depois de alterar um backup, faça uma restauração.

Quando a condição do componente é mensurável, a manutenção preventiva pode ser complementada ou substituída por [manutenção preditiva](manutencao-preditiva.md). Quando uma falha já ocorreu, o trabalho passa a ser [manutenção corretiva](manutencao-corretiva.md).
