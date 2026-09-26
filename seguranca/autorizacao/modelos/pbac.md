# Policy-Based Access Control

Policy-Based Access Control, PBAC, usa políticas declarativas para decidir quais ações são permitidas ou negadas. A política pode combinar identidade, papéis, atributos, relações, estado e contexto. PBAC descreve a forma de administrar e avaliar regras, não uma única estrutura de dados.

## Estrutura

Uma arquitetura PBAC separa normalmente:

- PEP, que aplica a decisão;
- PDP, que avalia a política;
- PIP, que fornece atributos e relações;
- PAP, que cria e publica políticas;
- policy store, que mantém versões e metadados.

Essa separação torna a política revisável sem alterar o código da aplicação, mas aumenta a necessidade de governança. Uma alteração de política pode mudar o comportamento de vários serviços ao mesmo tempo.

## Efeitos e precedência

Uma linguagem PBAC precisa definir default deny, allow explícito, deny explícito, prioridade e combinação de resultados. Sem uma precedência determinística, duas políticas podem produzir decisões diferentes dependendo da ordem de carregamento.

O sistema também deve definir o que acontece com erro de avaliação, atributo ausente, PDP indisponível e versão incompatível do schema. Em operações sensíveis, falhas devem negar ou interromper a operação, nunca transformar erro em permissão.

## Ciclo de uma política

Uma policy nasce como requisito de negócio, é escrita em uma linguagem ou estrutura, validada, testada, aprovada e publicada. Em produção, o PDP carrega uma versão identificável e retorna a decisão junto com metadados suficientes para auditoria. Uma alteração deve poder ser comparada com a versão anterior e revertida.

Separar policy do código não significa separar policy do controle de mudanças. Mudanças de autorização precisam de revisão, testes de regressão, responsável e janela de publicação. O PAP não deve ser um painel sem trilha de auditoria.

## Policy decision e filtragem

Um check de autorização responde se uma operação pontual pode ocorrer. Uma lista autorizada exige uma consulta de objetos ou uma tradução da policy para o banco. Não é seguro buscar todos os registros e esconder os não autorizados depois.

Se a engine não puder produzir filtros corretos, o serviço deve limitar a consulta, usar uma projeção de segurança ou escolher um modelo que suporte a operação. Decisões individuais para milhares de linhas criam latência, inconsistência e pressão sobre o PDP.

## Política local e política remota

Um engine local reduz latência e continua funcionando sem rede, mas distribui modelos e políticas dentro de cada processo. Um PDP remoto centraliza publicação e observabilidade, mas exige autenticação entre serviços, timeout, fallback e capacidade.

Uma estratégia híbrida pode carregar uma versão assinada localmente e consultar uma fonte central apenas durante atualização. Nesse caso, defina a idade máxima da policy e como uma revogação urgente invalida cópias.

## Relação com outros modelos

PBAC pode expressar RBAC usando condições sobre papéis, ABAC usando atributos e ReBAC usando relações. Cedar é uma linguagem PBAC com `permit`, `forbid`, entidades e schema. Casbin usa um modelo configurável, um matcher e políticas. Oso e Open Policy Agent são outras famílias de engines de políticas, com linguagens e escopos diferentes.

PBAC não implica que políticas devam ser remotas. Um engine pode ser embutido no processo, e as políticas podem ser empacotadas com a aplicação ou carregadas de um repositório versionado.

## Operação

Versione policies e schemas. Valide sintaxe, referências, testes positivos e negativos, isolamento entre tenants e ausência de permissões excessivas antes da publicação. Registre a versão da política que produziu a decisão.

Não permita que cada serviço invente nomes para as mesmas ações. Um vocabulário comum para `read`, `write`, `publish`, `approve` e `administer` reduz incompatibilidades, mas cada ação ainda precisa ser ligada ao recurso correto.

## Quando usar

PBAC vale a pena quando várias aplicações precisam compartilhar políticas, quando mudanças de autorização precisam passar por revisão independente ou quando regras condicionais são grandes demais para ficarem espalhadas em código procedural.

Para uma aplicação pequena, um serviço de políticas pode ser complexidade desnecessária. Um serviço de domínio com checks explícitos pode ser mais fácil de verificar.

## Anti-patterns

Evite policies que reproduzem toda a lógica de negócio, regras com nomes de rota instáveis, permissões genéricas como `admin`, atributos sem dono e exceções que só existem em produção. Também evite permitir que o cliente envie a policy, o tenant ou o principal efetivo da requisição.

## Fontes

- [NIST, verification and test methods for access control policies](https://csrc.nist.gov/pubs/sp/800/192/final)
- [Cedar, authorization](https://docs.cedarpolicy.com/auth/authorization.html)
- [Apache Casbin, model syntax](https://casbin.apache.org/docs/syntax-for-models/)
