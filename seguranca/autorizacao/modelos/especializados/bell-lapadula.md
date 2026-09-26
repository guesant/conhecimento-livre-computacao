# Bell-LaPadula

Bell-LaPadula é um modelo formal orientado à confidencialidade e ao fluxo de informação. Ele trabalha com níveis de classificação e autorizações que limitam como sujeitos leem e escrevem objetos.

## Regras clássicas

As regras mais conhecidas são:

- **no read up**, um sujeito não deve ler um objeto em nível superior ao seu clearance;
- **no write down**, um sujeito não deve escrever informação classificada em um nível inferior.

Essas regras reduzem o fluxo de informação de níveis altos para níveis baixos. O modelo pode incluir categorias ou compartimentos para separar domínios de interesse.

## O que ele resolve

Bell-LaPadula ajuda a formalizar confidencialidade em ambientes de múltiplos níveis, especialmente quando a preocupação é evitar que dados secretos sejam lidos por sujeitos sem clearance ou vazem para níveis inferiores.

Ele não garante integridade, disponibilidade, autenticidade ou correção da classificação. Um sujeito autorizado pode ainda escrever dados incorretos em seu próprio nível.

## Relação com MAC e ABAC

O modelo é normalmente implementado como uma política obrigatória, em que o proprietário não pode relaxar o fluxo. ABAC pode representar níveis, categorias e contexto, mas a semântica de dominação e fluxo precisa ser preservada explicitamente.

## Limitações

Classificações erradas, canais laterais, cópias fora do mecanismo e administradores privilegiados podem comprometer o objetivo. O modelo também pode dificultar colaboração e reclassificação, que exigem procedimentos e auditoria.

## Fontes

- [NIST, access control methodologies](https://csrc.nist.gov/CSRC/media/Publications/white-paper/2010/12/01/economic-analysis-of-rbac-final-report/final/documents/20101219_RBAC2_Final_Report.pdf)
- [NIST, meta model for access control](https://csrc.nist.gov/pubs/conference/2008/06/11/a-meta-model-for-access-control/final)
