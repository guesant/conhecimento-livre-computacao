# SOPS keyservice

O keyservice do SOPS separa a operação de chaves do processo que edita ou decifra o arquivo. O cliente SOPS pode usar o serviço local padrão ou encaminhar operações para um processo acessível por TCP ou socket Unix. Isso permite concentrar uma chave, um prompt de aprovação ou uma integração com um dispositivo protegido em outro contexto de execução.

## Modelo

O arquivo continua cifrado com a estrutura e os metadados do SOPS. O keyservice recebe operações necessárias para proteger ou recuperar a chave de dados, mas não transforma o arquivo cifrado em um secret store nem elimina a necessidade de proteger o processo cliente.

O serviço pode ser iniciado com `sops keyservice`. A opção de rede pode ser `tcp` ou `unix`, e o endereço deve ser explícito. O cliente seleciona serviços adicionais pela opção `--keyservice` ou pela variável `SOPS_KEYSERVICE`, usando o formato de URI suportado pela versão instalada.

## Socket Unix

Um socket Unix limita o transporte à máquina ou a um namespace que tenha acesso ao caminho. O diretório e o socket devem ter proprietário e permissões restritos. Evite colocá-lo em um diretório temporário compartilhado ou montá-lo em containers que não precisam realizar operações de chave.

Um socket não autentica automaticamente todos os consumidores. A permissão de abertura do arquivo, o isolamento do processo, o prompt do serviço e a política do sistema operacional formam o controle real. Um processo com acesso ao socket pode solicitar operações autorizadas pelo serviço.

## Serviço TCP

TCP permite separar cliente e serviço entre máquinas, mas aumenta o domínio de exposição. O endpoint não deve ser publicado sem autenticação e proteção de transporte apropriadas. Firewall, rede privada e prompt interativo não substituem autenticação criptográfica quando o serviço atravessa uma fronteira de confiança.

## Quando usar

Use um keyservice quando a chave privada ou a operação de KMS deve permanecer em um agente dedicado, quando a aprovação precisa ser centralizada ou quando o processo que executa o deploy não deve possuir diretamente o material de chave. Para um fluxo simples em uma única máquina, o serviço local padrão costuma ter menos componentes e menos pontos de falha.

O keyservice é diferente de `SSH_AUTH_SOCK`: o socket SSH encaminha pedidos de assinatura para autenticação SSH, enquanto o keyservice do SOPS atende operações de chaves usadas na criptografia dos arquivos SOPS. Ambos exigem controle de acesso ao socket.

## Failure modes

- O socket não existe, foi removido ou não está acessível ao usuário do processo.
- O serviço está vivo, mas a política ou o backend de chave rejeita a operação.
- O cliente usa uma URI incompatível com a versão do SOPS instalada.
- Um socket ou endpoint compartilhado permite que outro processo peça operações de chave.
- O serviço fica disponível, mas a chave externa, KMS ou dispositivo protegido não está disponível.

## Relações

- [SOPS e age](sops-age.md) explica o modelo de cifragem e destinatários.
- [Bootstrap](bootstrap.md) trata a primeira credencial necessária para decifrar.
- [SSH](../../ssh.md) cobre o mecanismo semelhante usado pelo agente SSH, inclusive o socket e o encaminhamento.

## Fontes primárias

- [Documentação do SOPS](https://getsops.io/docs/)
- [Opções de keyservice do SOPS](https://github.com/getsops/sops/blob/main/cmd/sops/main.go)
