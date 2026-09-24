# Proteção de endpoints Linux

Endpoint protection em Linux combina agente, telemetria, prevenção, detecção e resposta para hosts e, em alguns produtos, workloads e containers. O agente não substitui hardening, patching, controle de identidade, isolamento de rede ou observabilidade do serviço.

## AV e EDR

Antivírus tradicional procura malware usando assinaturas, heurísticas e sinais comportamentais sobre arquivos e processos. EDR amplia o foco: coleta telemetria, correlaciona eventos, permite investigação e pode executar ações de resposta. Os nomes comerciais variam e alguns produtos combinam as duas categorias, mas a comparação deve considerar a capacidade efetivamente disponível para Linux.

| Categoria | O que faz | Tipo de análise | Quando é usado | Alvo principal |
| --- | --- | --- | --- | --- |
| AV | Identifica e bloqueia malware conhecido ou suspeito | Assinatura, heurística e comportamento | Continuamente no endpoint e em arquivos recebidos | Sistema operacional e filesystem |
| EDR | Registra atividade, detecta padrões e apoia contenção e investigação | Telemetria e análise comportamental | Continuamente em hosts e workloads suportados | Processos, arquivos, rede e identidade do endpoint |

ClamAV é uma alternativa aberta para antivírus em cenários compatíveis. Wazuh pode fornecer HIDS, coleta e resposta self-hosted, mas não deve ser tratado automaticamente como equivalente a um EDR comercial com agente de prevenção. Sophos Intercept X for Server, SentinelOne Singularity Endpoint e Symantec Endpoint Security são alternativas comerciais; a oferta, o agente e a cobertura de kernel precisam ser confirmados para a distribuição escolhida.

Preço não define cobertura. Verifique prevenção, detecção, resposta remota, retenção, atualização do agente, impacto de CPU e memória, suporte ao kernel, funcionamento sem conexão com a console e procedimento de recuperação após um bloqueio incorreto.

## Critérios de seleção

Compare suporte real à distribuição e ao kernel, modelo de privilégio, impacto de CPU e memória, cobertura de workloads e containers, detecção em runtime, EDR, resposta remota, retenção de eventos, integração com SIEM, gestão central e requisitos de licença. “Suporta Linux” pode significar apenas uma modalidade de proteção, não paridade de recursos com Windows.

[Sophos Intercept X for Server](sophos.md), [SentinelOne Singularity Endpoint](sentinelone.md) e [Symantec Endpoint Security](symantec.md) são produtos de categorias próximas. A [comparação de endpoint Linux](../../comparacoes/seguranca/linux-endpoint.md) resume as diferenças sem transformar declarações de fornecedor em garantia independente.

## Operação

Instale o agente somente depois de medir o custo sobre o workload e definir exclusões estreitas. Valide atualização, conectividade com a console, comportamento em kernel novo, recuperação após reinício e remoção segura. Em servidores críticos, teste a política em modo de observação antes de habilitar bloqueios amplos.

## Relações

- [Observabilidade](../../observabilidade/index.md) trata sinais de saúde e desempenho, não prevenção de malware.
- [SAST](../appsec/sast/index.md), [SCA](../appsec/sca/index.md) e [fuzzing](../appsec/fuzzing/index.md) examinam superfícies diferentes.
- [PCI DSS](../compliance/pci-dss.md) e [HIPAA](../compliance/hipaa.md) podem exigir evidências de controles, mas não prescrevem uma marca específica de endpoint protection.
