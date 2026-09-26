# Mandatory Access Control

Mandatory Access Control, MAC, aplica uma política central que controla o fluxo entre sujeitos e objetos. O usuário ou proprietário do objeto não pode simplesmente relaxar a regra. O sistema usa atributos, rótulos, níveis de segurança ou políticas administradas por uma autoridade central.

## Modelo de rótulos

Um sistema MAC pode associar ao sujeito uma autorização e ao objeto uma classificação. Uma decisão pode exigir que o nível do sujeito domine o nível do objeto, além de verificar categorias ou compartimentos. Outros sistemas usam labels mais gerais e regras de fluxo, sem reduzir tudo a uma hierarquia numérica.

Bell-LaPadula é uma família voltada à confidencialidade. Biba é uma família voltada à integridade. SELinux fornece um mecanismo de política mandatory no Linux, mas sua linguagem e seus tipos não são simplesmente uma implementação de Bell-LaPadula.

## SELinux e LSM

No Linux, SELinux usa o framework Linux Security Modules para aplicar decisões além das permissões discricionárias tradicionais. Contextos, tipos, domínios e regras determinam quais operações são permitidas. O processo pode ser dono de um arquivo e ainda assim ser negado pela política SELinux.

MAC não substitui DAC. As camadas podem ser avaliadas em conjunto, e uma operação precisa passar por todas as restrições relevantes. Um troubleshooting correto identifica qual camada negou, em vez de desligar o mecanismo inteiro.

## Vantagens

MAC é útil quando uma política de contenção precisa prevalecer sobre a decisão do proprietário. Ele reduz o impacto de um processo comprometido, limita fluxos entre domínios e ajuda a separar informações por classificação ou finalidade.

## Custos e limites

A política é mais difícil de entender e operar que uma ACL simples. Aplicações novas podem falhar por acessos que não foram declarados. Uma política permissiva demais elimina a proteção; uma política opaca leva administradores a colocar o sistema em modo permissivo.

Use logs de negação, testes de política e implantação gradual. Não trate o modo permissivo como solução permanente. Documente quais objetos, processos, sockets, mounts e dispositivos fazem parte do domínio protegido.

## Fluxo de avaliação

Uma operação pode ser permitida por DAC e negada por MAC. O kernel ou o enforcement point consulta o contexto do sujeito, o contexto do objeto e a regra da política. Em SELinux, uma negação precisa ser analisada junto com o tipo de processo, o tipo do recurso e a classe da operação.

Não copie uma regra de allow apenas porque ela remove um log. Primeiro confirme se o fluxo é legítimo, limite a regra ao domínio e recurso necessários e teste operações que continuam proibidas.

## MAC, MLS e compartimentos

Mandatory policies podem usar níveis hierárquicos, categorias, tipos, domínios ou uma combinação. MLS normalmente trabalha com níveis de classificação e compartimentos. Type enforcement trabalha com tipos e transições. São mecanismos relacionados, mas não equivalentes.

## Operação

Políticas MAC devem ser versionadas, testadas em ambiente representativo e atualizadas junto com a aplicação. Auditoria precisa distinguir negação esperada, tentativa de abuso e regressão de configuração. Uma mudança no domínio do processo pode ser tão relevante quanto uma mudança de código.

## Relação com ABAC

MAC pode ser expresso usando atributos e regras. ABAC é uma forma mais geral de avaliar atributos de sujeito, objeto, ação e ambiente; MAC descreve a autoridade e a possibilidade de alteração da política. Portanto, ABAC pode implementar políticas que tenham comportamento mandatório, mas os termos não são intercambiáveis.

## Fontes

- [NIST, access control methodologies](https://csrc.nist.gov/CSRC/media/Publications/white-paper/2010/12/01/economic-analysis-of-rbac-final-report/final/documents/20101219_RBAC2_Final_Report.pdf)
- [SELinux Project](https://selinuxproject.org/page/Main_Page)
- [Red Hat, SELinux user and administrator guide](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/using_selinux/index)
