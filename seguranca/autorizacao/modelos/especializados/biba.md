# Biba

Biba é um modelo formal orientado à integridade. Ele limita como dados de menor integridade podem influenciar sujeitos ou objetos de maior integridade.

## Regras clássicas

As regras tradicionais são descritas como:

- **no read down**, um sujeito não deve ler dados de integridade inferior quando isso permitir contaminação;
- **no write up**, um sujeito não deve escrever em um objeto de integridade superior.

As formulações e variantes podem mudar conforme o sistema. O ponto central é impedir que dados ou sujeitos menos confiáveis contaminem estados que exigem maior integridade.

## Uso

Biba é útil como modelo mental para separar dados confiáveis de dados não confiáveis, proteger configurações e limitar fluxos em sistemas críticos. Ele não trata confidencialidade. Um sistema pode precisar de Biba e Bell-LaPadula ao mesmo tempo, com políticas diferentes para integridade e sigilo.

## Relação com MAC

Biba pode ser implementado como uma política obrigatória baseada em níveis. O proprietário do objeto não deve conseguir relaxar a restrição de integridade apenas alterando uma ACL.

## Limitações

Integridade não é apenas um nível estático. Assinaturas, proveniência, validação, transações, revisão e controles de alteração também importam. Um rótulo de integridade errado não torna o dado confiável.

## Fontes

- [NIST, access control methodologies](https://csrc.nist.gov/CSRC/media/Publications/white-paper/2010/12/01/economic-analysis-of-rbac-final-report/final/documents/20101219_RBAC2_Final_Report.pdf)
- [NIST, meta model for access control](https://csrc.nist.gov/pubs/conference/2008/06/11/a-meta-model-for-access-control/final)
