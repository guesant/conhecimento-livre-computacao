# Análises de incidentes

Esta seção transforma incidentes públicos em estudos de caso técnicos. O objetivo
não é apenas registrar a causa imediata, mas reconstruir a cadeia de decisões,
dependências, sinais, controles de recuperação e condições que permitiram a
falha.

Os relatos oficiais são a fonte primária dos fatos. Vídeos, palestras e análises
externas ajudam a visualizar a sequência, mas não substituem o post-mortem da
organização envolvida. A análise separa fatos documentados de interpretações e
de recomendações que podem ser aplicadas a outros ambientes.

## Como ler os estudos

Cada caso é dividido em contexto, sequência temporal, mecanismo técnico,
decisões durante a resposta, aspectos positivos, falhas de processo e controles
que poderiam ter interrompido a cadeia. Essa separação é importante porque um
incidente raramente resulta de uma única ação. Em geral, uma mudança normal,
uma suposição válida apenas em condições ideais, uma automação sem contexto e
uma recuperação não exercitada se reforçam até produzir um resultado grave.

O fato de uma ação ter contribuído para o incidente não significa que a pessoa
que a executou seja a causa completa. A análise deve perguntar por que o sistema
permitia aquela ação, por que os sinais não interromperam o procedimento e por
que a recuperação não era mais rápida ou segura.

## Casos

- [Incidente do GitHub em 2018](github-2018.md) descreve uma partição de rede
  que provocou uma promoção automática de primários entre regiões, divergência
  de dados e uma recuperação de mais de um dia.
- [Incidente do GitLab em 2017](gitlab-2017.md) descreve a perda do diretório
  do banco primário, a falha silenciosa de backups e uma recuperação baseada em
  snapshot com perda de dados.
- [Lições comuns](licoes.md) compara os mecanismos e transforma os casos em
  controles verificáveis para arquitetura, operação, backup e resposta.
- [Inventário de casos de engenharia](inventario-de-casos.md) reúne migrações,
  incidentes de rede, falhas de plano de controle e reconstruções de plataforma.

## Casos de roteamento

- [Cloudflare 1.1.1.1 em 2024](cloudflare-2024.md) trata RPKI, hijack e route
  leak.
- [Vazamento da Verizon em 2019](verizon-2019.md) trata BGP optimizer, filtros
  e propagação indevida.
- [Telegram na Índia em 2026](telegram-2026.md) trata bloqueio nacional,
  escopo BGP e propagação internacional.
- [Meta em 2021](meta-2021.md) trata backbone, BGP, DNS e recuperação fora do
  plano de controle.
- [Bloqueios silenciosos](bloqueios-silenciosos.md) trata filtragem regional,
  IPs compartilhados e dependências em Vercel, GitHub Pages e CDNs.

## Relações com o restante da documentação

Os casos devem ser lidos junto com o [runbook de resposta a incidente](../../../operacional/resposta-a-incidente.md),
com os fundamentos de [backup](../backup/backup.md), [RPO](../backup/rpo.md)
e [RTO](../backup/rto.md), e com os procedimentos de [teste de restauração](../backup/teste-de-restauracao.md).
Os experimentos controlados descritos em [chaos engineering](../testes/chaos-engineering.md)
ajudam a verificar se os controles realmente funcionam antes de uma falha real.

## Como distinguir fato, observação e recomendação

Um estudo de incidente precisa deixar claro que tipo de afirmação está sendo
feita. O post-mortem da organização envolvida é a fonte principal para causa,
horário e impacto interno. Coletores de rota, medições de usuários e relatórios
de terceiros são evidência independente do comportamento observado na rede. Uma
recomendação é uma conclusão nossa, não um fato sobre o evento.

| Tipo de afirmação | Exemplo | Como escrever |
| --- | --- | --- |
| Fato documentado | A organização informou que uma mudança retirou rotas | Atribuir à fonte primária |
| Observação externa | Coletores viram um origin ASN diferente | Informar a fonte e o ponto de observação |
| Inferência | O mecanismo é compatível com um route leak | Usar linguagem probabilística e explicar a base |
| Recomendação | Um filtro de exportação reduziria o blast radius | Separar do relato do incidente |

Essa separação evita transformar uma medição parcial em atribuição de intenção.
Também impede que uma prática recomendada seja apresentada como se tivesse sido
implementada pela empresa estudada. Quando as fontes discordarem, a divergência
deve permanecer visível e a conclusão deve ser limitada ao que ambas sustentam.

## Perguntas comuns a todos os casos

Além da causa imediata, cada estudo deve responder a perguntas que permitem
comparar plataformas diferentes:

1. Qual propriedade estava sendo protegida: disponibilidade, consistência,
   durabilidade, confidencialidade, integridade ou recuperabilidade?
2. Qual estado era a autoridade e como o sistema impedia duas autoridades
   concorrentes?
3. Qual dependência compartilhada ampliou o impacto?
4. Qual sinal apareceu antes da indisponibilidade e qual sinal ficou invisível?
5. O plano de recuperação dependia do componente que havia falhado?
6. Que parte do produto voltou primeiro e que efeitos derivados ainda estavam
   atrasados?
7. Qual teste reproduziria a falha sem repetir o dano em produção?

Um caso só é transferível quando a resposta descreve a propriedade e o mecanismo,
e não apenas o nome da tecnologia usada pela empresa.
