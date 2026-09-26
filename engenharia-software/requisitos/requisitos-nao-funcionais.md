# Requisitos não funcionais

Requisitos não funcionais, RNF, descrevem propriedades, restrições e condições de operação do
sistema. Eles não são menos importantes por não representarem uma ação visível. Disponibilidade,
latência, segurança, acessibilidade, custo e recuperação podem determinar se uma funcionalidade
é realmente utilizável.

## RNF não significa requisito vago

"A aplicação deve ser segura" é uma intenção. Um requisito verificável identifica escopo,
ameaça, medida, contexto e tolerância. Por exemplo, uma classe de leitura pode exigir p95 abaixo
de um limite sob uma carga definida, e um processo de recuperação pode exigir RPO e RTO
específicos.

| Dimensão | Formulação que precisa ser decidida |
| --- | --- |
| Desempenho | Qual operação, carga, percentil, ambiente e janela de medição? |
| Disponibilidade | Qual serviço, período, dependência e comportamento durante degradação? |
| Capacidade | Quantos usuários, eventos, bytes, conexões e crescimento? |
| Escalabilidade | O que cresce verticalmente, horizontalmente, por partição ou por fila? |
| Resiliência | Como o sistema reage a timeout, erro, atraso, duplicidade e indisponibilidade? |
| Segurança | Quais ameaças, identidades, controles, evidências e limites? |
| Privacidade | Quais dados são coletados, usados, compartilhados, retidos e apagados? |
| Recuperação | Qual perda de dados e tempo de restauração são aceitáveis? |
| Operabilidade | Como detectar, diagnosticar, alterar, reverter e auditar? |
| Manutenibilidade | Como atualizar dependências, esquema, contratos e componentes? |
| Compatibilidade | Quais clientes, versões, protocolos e formatos coexistem? |
| Acessibilidade | Quais pessoas, tecnologias assistivas e critérios devem ser atendidos? |
| Localização | Quais idiomas, formatos, moedas, fusos e regras regionais? |
| Custo | Qual orçamento de computação, armazenamento, rede, licença e suporte? |

## ISO/IEC 25010 e outras referências

A ISO/IEC 25010 oferece um modelo de qualidade de produto que ajuda a nomear atributos e
subatributos. Ela não escolhe os números da aplicação. A equipe ainda precisa transformar o
atributo em uma medida adequada ao contexto.

FURPS+ organiza funcionalidade, usabilidade, confiabilidade, desempenho, suporte e restrições.
O NFR Framework trata requisitos de qualidade como objetivos que podem entrar em conflito e
ser refinados em decisões técnicas. Quality Attribute Scenarios tornam o requisito concreto
com estímulo, ambiente, resposta e medida.

ATAM é uma abordagem de avaliação de arquitetura baseada em atributos de qualidade, cenários,
riscos e trade-offs. Ele é mais adequado quando decisões arquiteturais importantes precisam
ser avaliadas com diferentes stakeholders, e não como checklist automático para qualquer projeto.

## Quality Attribute Scenario

Um cenário de atributo de qualidade pode ser descrito com seis partes:

1. fonte do estímulo;
2. estímulo;
3. ambiente;
4. artefato afetado;
5. resposta esperada;
6. medida de resposta.

Exemplo: durante uma falha do provedor de pagamentos, em produção, uma requisição de cobrança
deve retornar uma resposta de indisponibilidade em até dois segundos, sem duplicar a cobrança,
registrando o evento e permitindo nova tentativa segura. Esse cenário conecta resiliência,
timeout, idempotência, observabilidade e experiência do usuário.

## Conflitos e trade-offs

RNFs competem. Criptografia pode aumentar custo de CPU. Retenção longa melhora auditoria, mas
aumenta custo e risco de privacidade. Consistência forte pode aumentar latência. Alta
disponibilidade pode exigir replicação e operação mais complexas.

Não resolva o conflito apagando um dos requisitos. Registre a prioridade, o contexto, a métrica,
o risco residual e o responsável pela aceitação. Um SLO, um orçamento de erro, um limite de
custo ou uma política de retenção pode tornar a decisão operável.

## Verificação e operação

RNFs precisam aparecer no desenho, nos testes, nos dashboards e nos runbooks. Um limite de p95
sem medição em produção não é um controle. Uma política de backup sem teste de restauração não
prova recuperação. Uma exigência de segurança sem identidade, logs e evidência não permite
auditoria.

Defina também o comportamento quando o limite for ultrapassado. A resposta pode ser bloquear
uma mudança, reduzir carga, ativar degradação, escalar recursos, abrir incidente ou aceitar
temporariamente o risco com prazo de revisão.

## Fontes primárias

- [ISO/IEC 25010](https://www.iso.org/standard/78176.html)
- [ISO/IEC/IEEE 29148](https://www.iso.org/obp/ui?_escaped_fragment_=iso%3Astd%3Aiso-iec-ieee%3A29148%3Aed-2%3Av1%3Aen)
- [SEI, Attribute-Driven Design e avaliação de arquitetura](https://www.sei.cmu.edu/our-work/architecture-analysis-and-design/)
