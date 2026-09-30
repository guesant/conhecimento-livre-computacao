# step-ca

step-ca é uma autoridade certificadora privada operável pela própria organização. Ela emite certificados X.509 e SSH e oferece provisioners que definem como identidades podem solicitar certificados, incluindo suporte a ACME.

## O problema que resolve

Uma organização frequentemente precisa de certificados para nomes, dispositivos ou workloads internos que não devem depender de uma CA pública. Operar uma CA privada fornece controle sobre identidade, validade, política e ciclo de vida.

O preço é assumir responsabilidades que uma CA pública normalmente absorve: proteção de chaves, disponibilidade do serviço de emissão, distribuição de confiança, rotação e resposta a comprometimento.

## Root e intermediárias

Uma raiz é a âncora de confiança. Mantê-la offline e usar uma intermediária online reduz a exposição da chave cuja substituição exige redistribuir confiança.

Isso não é ritual obrigatório para qualquer laboratório. Em ambientes descartáveis, uma topologia mais simples pode ser aceitável. Quanto maior o impacto de comprometer a CA, mais valiosa fica a separação.

## Provisioners

Provisioners determinam como clientes autenticam pedidos. ACME é útil quando clientes já implementam esse protocolo. Outros provisioners podem atender identidades e fluxos diferentes.

A escolha do provisioner é parte do modelo de identidade: automatizar emissão sem controlar quem pode pedir qual identidade cria uma CA conveniente e insegura.

## Certificados curtos

Validades menores reduzem a janela de uso de uma credencial comprometida e tornam automação de renovação obrigatória. Isso troca dependência de revocation por dependência maior da disponibilidade do processo de renovação.

O desenho precisa monitorar expiração e falha de renovação. "Automático" sem observabilidade apenas muda o modo de falha.

## Caso de uso: TLS interno

Um serviço interno recebe certificado assinado pela CA privada. Clientes precisam receber o root/intermediate apropriado em seu trust store. [trust-manager](trust-manager.md) pode automatizar parte dessa distribuição em Kubernetes.

## Caso de uso: ACME interno

Clientes compatíveis com ACME solicitam e renovam certificados sem integrar uma API proprietária da CA. O ganho é reutilizar um protocolo padronizado.

## Segurança das chaves

A chave privada da raiz deve ter proteção proporcional ao impacto. Intermediárias online continuam sensíveis e merecem backup seguro, controle de acesso e plano de rotação.

HSM ou KMS podem reduzir exposição de material de chave em cenários que justificam custo e dependência adicionais.

## Boas práticas

Separe emissão de distribuição de confiança; use identidades e provisioners estreitos; prefira validade curta quando renovação é confiável; teste rotação antes de precisar dela; mantenha backup e procedimento de recuperação; monitore expiração.

## Más práticas

Distribuir a chave privada da CA aos workloads. Usar uma única credencial de provisionamento irrestrita para todos os clientes. Criar uma PKI privada sem mecanismo de distribuir a CA. Manter certificados longos porque renovação não foi automatizada.

## Alternativas

Vault PKI, OpenBao PKI e CAs gerenciadas por provedores podem ocupar a responsabilidade de emissão. A escolha envolve operação própria, integração, políticas, custo e onde as chaves devem viver.

## Fontes

- step-ca: <https://smallstep.com/docs/step-ca/>
- ACME provisioner: <https://smallstep.com/docs/step-ca/provisioners/#acme>
- RFC 8555, ACME: <https://www.rfc-editor.org/rfc/rfc8555>

## Continue por aqui

[PKI](index.md) situa a ferramenta. [trust-manager](trust-manager.md) resolve distribuição de confiança. [Emissão e distribuição de confiança](../../composicoes/seguranca/pki.md) explica a composição completa.
