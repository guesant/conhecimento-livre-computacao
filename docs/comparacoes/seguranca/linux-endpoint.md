# Proteção de endpoint Linux

Sophos, SentinelOne e Symantec atendem uma responsabilidade semelhante, mas a escolha não deve ser feita por uma coluna de marketing. A cobertura efetiva depende da distribuição, do kernel, do tipo de workload, da licença e do modo de administração.

| Provedor | Solução | Ponto forte a investigar | Cuidado na comparação |
| --- | --- | --- | --- |
| Sophos | Intercept X for Server | Console centralizada, proteção comportamental e detecções de runtime para modalidades Linux suportadas | Recursos avançados podem depender de Intercept X Advanced for Server, XDR ou programa de acesso; confirme a matriz Linux |
| SentinelOne | Singularity Endpoint | EDR com prevenção, telemetria e resposta centralizadas, apresentado pelo fornecedor como orientado por IA e comportamento | Confirme paridade de prevenção e resposta no kernel e na distribuição Linux escolhidos |
| Symantec, Broadcom | Symantec Endpoint Security | Integração enterprise, políticas e controles de prevenção voltados a ambientes corporativos | Edições, agentes e recursos de exploração de memória podem variar por sistema operacional e contrato |

## Dimensões técnicas

Compare primeiro a instalação e o suporte ao kernel. Em seguida, meça consumo de CPU, memória, I/O e latência no workload real. Depois valide o que acontece quando o agente perde conectividade, como políticas são atualizadas, quais eventos chegam à console, como ocorre isolamento ou remediação e como o agente é removido durante uma recuperação.

Para requisitos de conformidade, a ferramenta deve ser ligada a evidências concretas, como políticas vigentes, logs de alteração, cobertura dos hosts, testes de resposta e retenção. Nenhum dos três produtos, isoladamente, demonstra conformidade com [PCI DSS](../../seguranca/compliance/pci-dss.md) ou [HIPAA](../../seguranca/compliance/hipaa.md).

## Páginas individuais

- [Sophos Intercept X for Server](../../seguranca/endpoint/sophos.md)
- [SentinelOne Singularity Endpoint](../../seguranca/endpoint/sentinelone.md)
- [Symantec Endpoint Security](../../seguranca/endpoint/symantec.md)
