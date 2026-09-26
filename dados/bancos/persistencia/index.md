# Persistência

Persistência trata como o estado sobrevive ao processo, ao host e a uma
interrupção. O modelo precisa considerar durabilidade, ordenação, concorrência,
recuperação, retenção e o custo de consulta.

[Bancos](../index.md) organizam modelos de dados e consultas. Storage de objetos,
cache e arquivos atendem necessidades diferentes de persistência e devem ser
comparados pelo contrato de durabilidade, não apenas pelo espaço disponível.
