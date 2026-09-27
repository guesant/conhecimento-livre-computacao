# Custódia de chaves fora do host

Uma chave privada usada pelo operador não precisa viver como um arquivo no
sistema operacional. Mantê-la fora do filesystem reduz o impacto de ataques
de supply chain, extensões maliciosas, dependências comprometidas, scripts de
bootstrap e ferramentas que procuram arquivos em `~/.ssh`, variáveis de
ambiente ou diretórios de configuração.

Essa medida não transforma o endpoint em confiável. Ela muda o que um invasor
precisa obter. Em vez de copiar um arquivo e usá-lo depois, o invasor precisa
pedir uma operação ao cofre, ao agente ou ao hardware, durante uma sessão que
pode exigir autorização do usuário.

## Três propriedades diferentes

Não exportabilidade, armazenamento cifrado e autenticação interativa não são a
mesma propriedade.

Uma chave em um cofre cifrado pode estar protegida em repouso, mas ser
descriptografada na memória quando o cofre é desbloqueado. Um agente pode
evitar que cada processo leia o arquivo, mas qualquer processo autorizado ao
socket pode tentar pedir uma assinatura. Um TPM ou autenticador externo pode
impedir a exportação da chave, mas o sistema operacional ainda pode solicitar
uma assinatura enquanto a política permitir.

A escolha deve começar pelo ataque que se quer impedir:

| Mecanismo | Protege principalmente | Limite principal |
| --- | --- | --- |
| Cofre cifrado | Cópia do arquivo em repouso | A chave pode aparecer na memória após desbloqueio |
| SSH agent | Distribuição do arquivo entre processos | O socket pode virar uma interface de assinatura |
| YubiKey | Exportação da chave e cópia por supply chain | Um processo pode tentar usar a chave quando autorizado |
| TPM | Chave vinculada ao dispositivo | Não é portátil e o sistema local continua solicitando operações |
| Secure Enclave | Chave vinculada ao dispositivo Apple | Depende das APIs e não substitui uma política de autorização |

## YubiKey para SSH

Há dois modelos comuns.

No primeiro, o OpenSSH usa uma credencial FIDO2 criada no autenticador. Os
tipos `ecdsa-sk` e `ed25519-sk` fazem com que o material privado permaneça no
autenticador. O arquivo criado no host contém a referência necessária para
localizar a credencial, não uma cópia equivalente da chave privada. O uso pode
exigir PIN, toque ou ambos.

No segundo, uma chave PIV ou OpenPGP residente na YubiKey é acessada por uma
integração compatível, como PKCS#11 ou o agente correspondente. A chave
privada continua no dispositivo e o cliente solicita uma operação de
assinatura.

O primeiro modelo normalmente oferece uma integração FIDO mais direta com
OpenSSH. O segundo pode ser útil quando a mesma chave precisa participar de
smart card, assinatura ou outros fluxos já existentes. A escolha depende dos
servidores, da distribuição, da política de PIN e da necessidade de usar a
mesma credencial fora de SSH.

A [documentação da Yubico sobre PIV](https://docs.yubico.com/software/yubikey/tools/pivtool/webdocs.pdf)
descreve o uso de chaves armazenadas na YubiKey para login SSH. O manual do
[OpenSSH `ssh-keygen`](https://man.openbsd.org/ssh-keygen) documenta os tipos
de chave `ecdsa-sk` e `ed25519-sk`.

## Bitwarden SSH Agent

O Bitwarden Desktop pode expor um socket local de SSH Agent. A chave privada
fica armazenada como item do cofre e o cliente SSH pede listagem ou assinatura
ao agente. O Bitwarden pode exigir que o usuário desbloqueie o cofre ou
autorize a operação.

Isso é melhor que espalhar chaves PEM em cada repositório, backup e máquina,
mas não equivale a uma chave não exportável de hardware. Quando o cofre está
desbloqueado e a solicitação é autorizada, o agente pode assinar em nome do
cliente. A política deve usar autorização por operação ou por curto período,
quando disponível, e manter o socket acessível somente à sessão esperada.

O Bitwarden documenta limitações como ausência de gerenciamento equivalente a
`ssh-add` e seleção por solicitação. Por isso, o inventário deve manter uma
chave por finalidade, com `IdentityFile` e regras de host claras, sem depender
de uma grande coleção de chaves carregadas ao mesmo tempo.

Fontes: [Bitwarden SSH Agent](https://bitwarden.com/help/ssh-agent/) e
[Bitwarden sobre SSH](https://bitwarden.com/help/about-ssh/).

## KeePassXC SSH Agent

O KeePassXC pode guardar a chave dentro do banco KeePassXC e adicioná-la a um
agente SSH compatível quando o banco é desbloqueado. Também pode guardar
somente o segredo necessário para desbloquear um arquivo de chave armazenado
em outro local.

Esse arranjo protege o arquivo em repouso e centraliza o desbloqueio, mas a
chave importada para o agente pode existir na memória do agente. O KeePassXC é
um cliente de uma implementação de SSH Agent, não um agente universalmente
isolado. O ciclo de vida da chave, a confirmação da operação e a remoção no
bloqueio precisam ser verificados na combinação de KeePassXC, agente e sistema
operacional.

Consulte a [documentação do KeePassXC sobre SSH Agent](https://keepassxc.org/docs/KeePassXC_UserGuide#_ssh_agent_integration)
antes de assumir que uma opção de confirmação ou timeout existe no agente
escolhido.

## TPM

Um TPM pode criar ou proteger uma chave não migrável ligada ao dispositivo.
Integrações PKCS#11, bibliotecas do sistema e aplicações específicas podem
usar o TPM como provedor de operações. O arquivo no host pode conter um
identificador ou um objeto selado, mas não precisa conter a chave privada em
formato exportável.

O TPM é adequado para uma estação administradora dedicada, para identidade do
host, para assinatura vinculada ao boot ou para uma chave cuja portabilidade
não seja necessária. Ele é menos adequado como único fator de recuperação do
operador, pois a troca de placa, limpeza do TPM, reinstalação e perda da
máquina podem destruir a disponibilidade da credencial.

Selar uma operação aos PCRs acrescenta uma condição sobre o estado de boot,
mas atualizações legítimas também alteram medições. Antes de selar uma chave,
defina a política de transição, a recuperação e a forma de re-enrolamento.

O [TPM](../hardware/tpm.md) descreve confiança, medição e os limites de
enforcement. A especificação do [Trusted Computing Group](https://trustedcomputinggroup.org/resource/tpm-library-specification/)
define a interface do componente, não a política operacional da organização.

## Secure Enclave

Em plataformas Apple, APIs do Keychain e do Secure Enclave podem criar chaves
que permanecem protegidas pelo hardware e só são usadas quando as condições
de acesso são atendidas. O aplicativo recebe o resultado da operação, não a
chave privada exportada.

Isso é útil para uma chave vinculada a um Mac ou outro dispositivo Apple, mas
não deve ser confundido com um cofre portátil. A chave normalmente não pode
ser transferida para outro computador, e a integração direta com OpenSSH
depende do provedor ou aplicativo utilizado. Um arquivo tradicional em
`~/.ssh` não se torna Secure Enclave-backed apenas porque o computador possui
Secure Enclave.

A política do Keychain pode exigir código do dispositivo, biometria ou
presença. A [documentação de segurança da Apple](https://support.apple.com/en-ca/guide/security/sec59b0b31ff/web)
explica o isolamento do Secure Enclave, e a documentação de
[Keychain](https://support.apple.com/en-au/guide/security/secb0694df1a/web)
explica que as ACLs podem impor condições de autenticação avaliadas pelo
Secure Enclave.

## Supply chain do operador

O controle é mais eficaz quando a chave nunca aparece no ambiente de execução
de ferramentas não confiáveis. Mesmo assim, um processo malicioso pode tentar
ler `SSH_AUTH_SOCK`, observar argumentos, modificar o comando antes da
assinatura ou usar a sessão já autorizada. A defesa precisa combinar custódia
com isolamento e autorização.

Uma estação de administração deve, no mínimo:

- usar uma chave por finalidade e por domínio de confiança;
- evitar chaves privadas em repositórios, imagens, dotfiles e backups comuns;
- exigir toque, PIN, biometria ou confirmação para operações sensíveis;
- manter `ForwardAgent` desabilitado por padrão;
- usar certificados SSH de curta duração quando houver uma CA operacional;
- restringir hosts, usuários, comandos e origem de cada credencial;
- registrar fingerprints e rotação, com revogação testada;
- manter uma segunda credencial de recuperação sob custódia separada;
- separar a máquina de desenvolvimento da estação de administração quando o
  risco justificar;
- tratar extensões, scripts de shell, plugins e dependências como código que
  pode solicitar uma operação ao agente.

Agent forwarding merece atenção especial. Ele não envia a chave privada ao
servidor remoto, mas disponibiliza uma capacidade de solicitar assinaturas a
partir da sessão remota. Um servidor comprometido pode tentar abusar dessa
capacidade enquanto a conexão estiver aberta. Prefira certificados de curta
duração, bastions controlados ou chaves com restrições de destino quando o
fluxo exigir salto entre hosts.

## O que não deve ser prometido

Guardar a chave fora do filesystem não impede um atacante que controla o
endpoint de:

- executar comandos com a autorização já concedida;
- pedir assinaturas repetidas enquanto o agente estiver desbloqueado;
- alterar o destino, o comando ou o conteúdo que o operador está prestes a
  autorizar;
- roubar tokens de sessão já existentes;
- apagar ou modificar `authorized_keys`, certificados e políticas no servidor;
- explorar a recuperação de conta ou a autoridade que emite certificados.

A proteção reduz a extração silenciosa e prolonga a oportunidade de detectar
um uso indevido. Ela não substitui menor privilégio, revisão de comandos,
isolamento da estação e revogação rápida.

## Estratégia recomendada

Para uma chave de administração portátil, prefira YubiKey com FIDO2 ou PIV e
mantenha uma segunda chave de recuperação. Para chaves que precisam acompanhar
uma estação Apple ou Linux específica, avalie Secure Enclave ou TPM com
política de recuperação explícita. Para reduzir a presença de arquivos
privados em várias máquinas, Bitwarden SSH Agent ou KeePassXC podem centralizar
o armazenamento, desde que o risco de um agente desbloqueado seja aceito.

Em todos os casos, publique somente a chave pública no serviço, confirme
fingerprints por um canal independente e teste revogação e substituição antes
de depender da chave para a única entrada administrativa.
