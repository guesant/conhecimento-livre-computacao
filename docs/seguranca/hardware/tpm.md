# TPM

Trusted Platform Module, ou TPM, é um componente definido pelo Trusted
Computing Group para fornecer funções de confiança ligadas à plataforma. Ele
pode gerar ou proteger chaves, manter valores de autorização, registrar
medições e participar de atestação. A especificação TPM 2.0 define uma
interface de comandos, não uma política completa de segurança para cada
sistema.

## Chaves e armazenamento selado

Uma chave pode ser criada de forma que a operação ocorra dentro do TPM ou que
seu uso dependa de uma hierarquia e de uma autorização. Dados podem ser selados
a valores de Platform Configuration Registers, os PCRs. Na abertura, o TPM só
libera o uso quando as condições medidas correspondem à política.

Selar dados ao boot pode impedir que um segredo seja liberado para um sistema
que iniciou com firmware, bootloader ou configuração diferente. Isso precisa
ser projetado junto com atualizações: uma mudança legítima de boot pode alterar
PCRs e bloquear a recuperação se não houver uma política de transição.

## Medição e attestation

O TPM pode receber medições de componentes durante o boot. Atestação permite
que um verificador avalie uma afirmação assinada sobre o estado observado.
Medição não é o mesmo que enforcement: o TPM registra ou assina evidência,
mas o sistema operacional e a política precisam decidir o que fazer com ela.

## O que o TPM não resolve

TPM não substitui controle de acesso, atualização, anti-malware, isolamento de
processos ou backup. Um processo autorizado pode pedir ao TPM a operação que
sua política permite. Se o endpoint estiver comprometido enquanto a chave está
sendo usada, o TPM não desfaz a ação legítima.

TPM físico, firmware TPM e vTPM possuem domínios de falha e garantias
diferentes. O desenho precisa considerar disponibilidade, migração de VM,
reset, troca de placa, clear do TPM e recuperação de credenciais.

## Relações

- [Secure Enclave](secure-enclave.md) usa outro modelo de processador isolado.
- [Secure Boot](../../sistemas/boot/secure-boot.md) trata a cadeia de inicialização.
- [Autenticação sem senha](../identidade/autenticacao-sem-senha.md) usa
  credenciais de chave pública.

## Fontes primárias

- [Trusted Computing Group, TPM 2.0 Library](https://trustedcomputinggroup.org/resource/tpm-library-specification/)
- [Trusted Computing Group, TPM](https://trustedcomputinggroup.org/work-groups/trusted-platform-module/)
