# PCI DSS

PCI DSS, Payment Card Industry Data Security Standard, é um padrão de requisitos técnicos e operacionais para entidades que armazenam, processam ou transmitem dados de titulares de cartão, além de entidades que podem afetar a segurança do ambiente de dados de cartão.

## Escopo

O ponto mais importante é delimitar o Cardholder Data Environment, CDE, e os sistemas conectados ou capazes de impactá-lo. Segmentação pode reduzir escopo quando for efetiva e demonstrável, mas declarar uma rede como separada não prova que ela está isolada. Fluxos, identidades, integrações, armazenamento, logs e fornecedores precisam ser analisados.

## Controles

O padrão combina requisitos sobre configuração segura, proteção de dados, controle de acesso, monitoramento, testes, gestão de vulnerabilidades e políticas. A versão aplicável, o método de validação e a evidência exigida dependem do papel da entidade, do volume e do tipo de transação e da orientação do PCI Security Standards Council ou do assessor responsável.

Criptografia, firewall, EDR, scanner e testes de penetração são controles possíveis dentro de uma estratégia, não sinônimos de conformidade. O controle precisa estar implementado no escopo correto, ser operado continuamente e produzir evidência suficiente para a avaliação.

## Relação com a arquitetura

Um ambiente pequeno pode reduzir exposição ao não armazenar dados de cartão e delegar pagamento a um provedor. Essa decisão altera o escopo, mas não elimina a necessidade de avaliar integrações, credenciais, redirecionamentos, logs e sistemas que possam afetar o fluxo de pagamento.

## Limitações

PCI DSS não é uma certificação universal de segurança do produto, não substitui threat modeling e não transforma um relatório de auditoria em garantia de ausência de incidentes. Requisitos mudam, documentos de validação possuem versões próprias e a interpretação formal deve ser feita com a documentação vigente e o assessor aplicável.

## Fonte primária

- [PCI Data Security Standard](https://www.pcisecuritystandards.org/standards/pci-dss/)
- [PCI SSC document library](https://www.pcisecuritystandards.org/document_library/)
