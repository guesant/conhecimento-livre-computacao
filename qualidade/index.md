# Qualidade de software

Qualidade de software é a capacidade de entregar comportamento correto, seguro, operável e sustentável ao longo do tempo. Ela não é uma propriedade que aparece apenas quando uma suíte de testes passa. Resulta da combinação entre requisitos verificáveis, desenho, implementação, validação, observabilidade, manutenção e resposta a falhas.

## Estratégias

- [Qualidade proativa](proativa.md) trata riscos antes que uma falha alcance usuários.
- [Qualidade preventiva](preventiva.md) cria barreiras para modos de falha já conhecidos.
- [Qualidade preditiva](preditiva.md) usa sinais para antecipar degradação ou falha.
- [Qualidade reativa](reativa.md) detecta, contém, corrige e transforma incidentes em aprendizado.
- [Smoke tests de áreas protegidas](smoke-tests-de-areas-protegidas.md) verificam rapidamente interfaces autenticadas e operações críticas.

Essas estratégias se complementam. A qualidade proativa organiza a análise antes da construção. A prevenção transforma riscos conhecidos em controles. A predição procura sinais anteriores ao impacto. A reação reduz dano quando o comportamento real diverge do esperado. Nenhuma delas elimina a necessidade das outras.

## Evidência

Uma afirmação de qualidade precisa de uma evidência adequada à pergunta. Teste unitário demonstra uma regra isolada. Teste de integração demonstra uma fronteira. Smoke test demonstra que uma área essencial monta e responde. Métrica demonstra tendência. Alertas demonstram que uma condição pode ser percebida. Postmortem demonstra aprendizado sobre uma falha ocorrida.

Não use cobertura de linhas como substituto para cobertura de risco. Um sistema pode executar quase todo o código e ainda não testar autorização, migração, concorrência, expiração, recuperação ou comportamento sob indisponibilidade.

## Operação

Qualidade precisa sobreviver ao deploy. Releases graduais, rollback, feature flags, backups verificáveis, limites de capacidade, observabilidade, runbooks e manutenção organizada conectam engenharia de software à operação. A documentação deve registrar não apenas como implementar uma mudança, mas como saber que ela continua correta depois de publicada.

## Relações

- [Testes de software](../engenharia-software/testes/index.md) organiza camadas e perguntas de teste.
- [Observabilidade](../observabilidade/index.md) explica sinais usados para detectar e investigar comportamento.
- [Confiabilidade](../confiabilidade/resiliencia/index.md) trata degradação, recuperação e continuidade.
- [Checklist operacional](../../operacional/checklist.md) reúne critérios transversais de aceitação, segurança, performance e manutenção.
