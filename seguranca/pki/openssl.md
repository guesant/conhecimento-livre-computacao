# OpenSSL para PKI

OpenSSL é uma biblioteca e um conjunto de comandos para criptografia, TLS e
operações com X.509. Ele pode gerar chaves, criar solicitações de assinatura,
assinar certificados, inspecionar extensões, montar uma cadeia e verificar
assinaturas. Ele não é, por si só, uma autoridade certificadora operacional completa:
proteção de chave, aprovação, publicação, revogação, auditoria e rotação continuam
sendo responsabilidades do desenho de PKI.

## Separação de papéis

Uma chave privada gera ou assina, mas nunca precisa ser enviada na CSR. A CSR contém
a chave pública, a identidade solicitada, extensões que a CA pode avaliar e uma
assinatura feita com a chave privada correspondente. A CA decide o que realmente
entra no certificado e assina essa decisão com sua própria chave privada.

O exemplo abaixo usa uma CA raiz local e uma identidade de servidor. Em produção,
mantenha a raiz offline, use uma CA intermediária para emitir folhas e proteja as
chaves com armazenamento adequado. Os comandos são didáticos e não devem reutilizar
arquivos ou senhas de teste em um ambiente real.

## Escolha do algoritmo

RSA continua sendo uma opção interoperável, mas exige tamanhos maiores e operações
mais pesadas. ECDSA oferece chaves menores e bom desempenho, desde que clientes,
proxies e bibliotecas suportem a curva escolhida. Ed25519 é excelente para muitos
usos de assinatura, mas a compatibilidade com certificados X.509 e produtos TLS
específicos precisa ser verificada antes de adotá-lo como padrão de uma PKI.

| Uso | Exemplo didático | Decisão que precisa ser verificada |
| --- | --- | --- |
| CA raiz | RSA 3072 ou maior | Compatibilidade, custódia e validade longa. |
| CA intermediária | RSA 3072 ou ECDSA P-256 | Suporte dos emissores e do trust store. |
| Servidor ou cliente | RSA 2048, RSA 3072 ou ECDSA P-256 | Bibliotecas dos consumidores e política de rotação. |

O algoritmo da chave e o algoritmo de assinatura do certificado são decisões
relacionadas, mas não idênticas. Um certificado pode conter uma chave ECDSA e ser
assinado por uma CA RSA, por exemplo. A política deve proibir combinações fracas,
algoritmos obsoletos e tamanhos incompatíveis com o período durante o qual a
identidade será aceita.

## Inventário do material

Um fluxo de emissão deve produzir e registrar o propósito de cada arquivo:

| Arquivo | Conteúdo | Pode ser público? |
| --- | --- | --- |
| `*.key.pem` | Chave privada | Não. Proteja e audite o acesso. |
| `*.csr.pem` | Pedido assinado com chave pública | Em geral, sim, se a identidade não for sensível. |
| `*.cert.pem` | Certificado assinado | Sim, normalmente. |
| `fullchain.pem` | Folha seguida das intermediárias | Sim, para apresentação TLS. |
| `*.srl` | Serial local de emissão pontual | Não publique sem necessidade. |
| `*.crl.pem` | Lista assinada de revogação | Pode ser publicada conforme a política. |

O nome do arquivo não é uma proteção. Um certificado público pode revelar nomes
internos, e uma chave privada pode acabar exposta por permissões do diretório, backup,
histórico do shell ou artefato de CI. A classificação precisa acompanhar o arquivo
desde a geração até o descarte.

## Gerar a chave da CA

Crie um diretório com permissões restritas antes de gerar material privado:

```bash
umask 077
mkdir -p pki-demo
cd pki-demo

openssl genpkey \
  -algorithm RSA \
  -aes-256-cbc \
  -pkeyopt rsa_keygen_bits:3072 \
  -out root-ca.key.pem
```

O parâmetro de cifragem faz o OpenSSL solicitar uma senha para proteger a chave em
repouso. Isso não resolve sozinho o problema de custódia: a senha precisa ser
entregue por um canal protegido e a chave não deve ficar em um repositório ou em um
workload comum.

## Criar o certificado raiz

Uma raiz é um certificado autoassinado. O campo `basicConstraints` declara que ela
pode atuar como CA, `keyUsage` limita o uso de assinatura de certificados e CRLs e
`pathlen` restringe a quantidade de CAs subordinadas permitidas abaixo dela.

```bash
openssl req \
  -x509 \
  -new \
  -sha256 \
  -days 3650 \
  -key root-ca.key.pem \
  -out root-ca.cert.pem \
  -subj "/C=BR/O=Example/CN=Example Root CA" \
  -addext "basicConstraints=critical,CA:TRUE,pathlen:1" \
  -addext "keyUsage=critical,keyCertSign,cRLSign" \
  -addext "subjectKeyIdentifier=hash"
```

Uma raiz autoassinada não é confiável só por ter uma assinatura válida. Ela se torna
âncora quando é instalada deliberadamente no trust store de um sistema, runtime,
proxy ou cliente. Distribuir a raiz é uma decisão de confiança, não uma consequência
automática da emissão.

## Criar uma CA intermediária

Uma CA intermediária limita a exposição da raiz. Gere sua chave e CSR com a raiz
fora do host de emissão, transfira apenas o pedido aprovado para o ambiente que pode
assinar e proteja a chave da intermediária com uma custódia separada.

```bash
openssl genpkey \
  -algorithm RSA \
  -pkeyopt rsa_keygen_bits:3072 \
  -out issuing-ca.key.pem

openssl req \
  -new \
  -sha256 \
  -key issuing-ca.key.pem \
  -out issuing-ca.csr.pem \
  -subj "/C=BR/O=Example/CN=Example Issuing CA"
```

As extensões da intermediária são diferentes das extensões de uma folha:

```ini
basicConstraints = critical, CA:TRUE, pathlen:0
keyUsage = critical, keyCertSign, cRLSign
subjectKeyIdentifier = hash
authorityKeyIdentifier = keyid, issuer
```

Assine o pedido com a raiz e confira a cadeia antes de instalar a intermediária no
emissor:

```bash
openssl x509 \
  -req \
  -sha256 \
  -days 1825 \
  -in issuing-ca.csr.pem \
  -CA root-ca.cert.pem \
  -CAkey root-ca.key.pem \
  -CAcreateserial \
  -out issuing-ca.cert.pem \
  -extfile issuing-ca.ext

openssl verify -CAfile root-ca.cert.pem issuing-ca.cert.pem
```

`pathlen:0` permite que a intermediária assine folhas, mas não outra CA abaixo dela.
Esse limite impede que um emissor operacional crie uma hierarquia inesperada. A
política pode preferir uma intermediária por ambiente, função ou domínio para tornar
revogação, auditoria e atribuição mais precisas.

## Gerar chave e CSR do servidor

```bash
openssl genpkey \
  -algorithm RSA \
  -pkeyopt rsa_keygen_bits:2048 \
  -out server.key.pem

openssl req \
  -new \
  -sha256 \
  -key server.key.pem \
  -out server.csr.pem \
  -subj "/C=BR/O=Example/CN=api.example.test" \
  -addext "subjectAltName=DNS:api.example.test,DNS:api.internal.example"
```

O Common Name não substitui o SAN para validação de hostname. Uma CA ou processo de
aprovação deve verificar se os nomes solicitados pertencem ao requerente e se o uso
da identidade corresponde ao ambiente. Para um certificado de cliente, a extensão
`extendedKeyUsage` deve indicar `clientAuth`; para um servidor, `serverAuth`.

## Assinar a folha

Coloque as extensões aprovadas num arquivo de configuração da emissão:

```ini
basicConstraints = critical, CA:FALSE
keyUsage = critical, digitalSignature, keyEncipherment
extendedKeyUsage = serverAuth
subjectAltName = DNS:api.example.test, DNS:api.internal.example
subjectKeyIdentifier = hash
authorityKeyIdentifier = keyid, issuer
```

Salve o conteúdo como `server.ext` e assine com a CA:

```bash
openssl x509 \
  -req \
  -sha256 \
  -days 825 \
  -in server.csr.pem \
  -CA root-ca.cert.pem \
  -CAkey root-ca.key.pem \
  -CAcreateserial \
  -out server.cert.pem \
  -extfile server.ext
```

Assinar a folha diretamente com a raiz encurta o laboratório, mas aumenta o impacto
de qualquer operação que precise usar a chave raiz. Em uma PKI operacional, prefira
assinar a folha com `issuing-ca.key.pem` e forneça `issuing-ca.cert.pem` em
`-CA`; a raiz fica restrita à criação ou substituição da intermediária.

O resultado é uma folha assinada, não uma cadeia completa. Se houver uma CA
intermediária, o servidor normalmente apresenta a folha seguida das intermediárias,
na ordem que permite ao cliente alcançar a raiz confiável. A raiz geralmente não
precisa ser enviada, pois já deve estar no trust store.

## Configuração mínima de uma CA emissora

Quando o laboratório precisa demonstrar o ciclo completo de emissão, o estado do
emissor deve ser criado explicitamente. Uma estrutura mínima pode ser:

```text
issuing-ca/
  certs/
  crl/
  newcerts/
  private/
  index.txt
  serial
  crlnumber
  cert.pem
  private/key.pem
```

Os arquivos `index.txt`, `serial` e `crlnumber` não são decoração. O índice registra
o estado de cada certificado, o serial evita reutilização de identificadores e o
contador de CRL permite distinguir uma lista nova de uma lista antiga. Proteja o
diretório inteiro e não permita que duas instâncias modifiquem esses arquivos sem
coordenação.

Uma configuração reduzida para uma CA intermediária de servidor pode ser:

```ini
[ ca ]
default_ca = issuing_ca

[ issuing_ca ]
dir = ./issuing-ca
database = $dir/index.txt
new_certs_dir = $dir/newcerts
certificate = $dir/cert.pem
private_key = $dir/private/key.pem
serial = $dir/serial
crlnumber = $dir/crlnumber
default_md = sha256
default_days = 825
default_crl_days = 7
policy = policy_server
copy_extensions = none

[ policy_server ]
countryName = supplied
organizationName = supplied
commonName = supplied

[ server_extensions ]
basicConstraints = critical, CA:FALSE
keyUsage = critical, digitalSignature, keyEncipherment
extendedKeyUsage = serverAuth
subjectKeyIdentifier = hash
authorityKeyIdentifier = keyid, issuer
```

O valor `copy_extensions = none` evita que o solicitante injete automaticamente
extensões da CSR no certificado final. O emissor precisa escolher explicitamente o
SAN e o uso permitido. Se a organização decidir copiar extensões, isso deve ser
acompanhado por validação dos campos da CSR e por uma policy que impeça a emissão de
CA, `serverAuth` ou `clientAuth` fora do contexto aprovado.

Inicialize o estado antes de emitir:

```bash
install -d -m 0700 \
  issuing-ca/certs \
  issuing-ca/crl \
  issuing-ca/newcerts \
  issuing-ca/private

touch issuing-ca/index.txt
printf '1000\n' > issuing-ca/serial
printf '1000\n' > issuing-ca/crlnumber

cp issuing-ca.cert.pem issuing-ca/cert.pem
cp issuing-ca.key.pem issuing-ca/private/key.pem
chmod 0600 issuing-ca/private/key.pem
```

Em seguida, emita uma folha a partir de uma CSR já aprovada:

```bash
openssl ca \
  -config ca.cnf \
  -extensions server_extensions \
  -in server.csr.pem \
  -out server.cert.pem
```

O comando pode pedir confirmação e registrar a emissão no índice. Em uma operação
real, a aprovação deve acontecer fora do comando e deixar uma evidência vinculada ao
serial. Não automatize a aprovação apenas porque a CSR tem um nome que parece
conhecido.

## Emitir identidade de cliente

Uma identidade de cliente usa a mesma sequência de chave, CSR e assinatura, mas a
política de extensões muda. O objetivo não é validar um hostname de servidor, e sim
declarar que a chave pode autenticar um cliente naquele sistema.

```ini
basicConstraints = critical, CA:FALSE
keyUsage = critical, digitalSignature
extendedKeyUsage = clientAuth
subjectAltName = URI:spiffe://example.test/workload/api
subjectKeyIdentifier = hash
authorityKeyIdentifier = keyid, issuer
```

O SAN pode ser DNS, URI, email ou outro tipo aceito pela política. O valor deve ser
um identificador que o sistema consiga associar a um registro de workload, não uma
string livre escolhida pelo cliente. Se a mesma CA emitir certificados de servidor e
cliente, `extendedKeyUsage` e a política de autorização precisam impedir que uma
identidade de um papel seja reutilizada no outro.

Para mTLS com uma CA intermediária, o servidor apresenta a folha e a intermediária,
enquanto o cliente confia na raiz. O servidor confia na raiz ou na intermediária de
clientes e valida a cadeia do cliente. O bundle de apresentação e o bundle de
validação são artefatos diferentes e não devem ser trocados por conveniência.

## Inspecionar e verificar

```bash
openssl x509 -in server.cert.pem -noout -text
openssl req -in server.csr.pem -noout -text
openssl verify -CAfile root-ca.cert.pem server.cert.pem
openssl s_client -connect api.example.test:443 -servername api.example.test -showcerts
```

Verificar a assinatura da CA não basta. O cliente também precisa conferir período de
validade, SAN, `keyUsage`, `extendedKeyUsage`, restrições de CA e, quando aplicável,
estado de revogação. `openssl verify` recebe opções adicionais para cadeia,
propósito e CRL; o conjunto exato deve refletir o uso real, não apenas a existência
de uma assinatura.

Quando a intermediária é usada, separe a âncora do emissor:

```bash
openssl verify \
  -CAfile root-ca.cert.pem \
  -untrusted issuing-ca.cert.pem \
  -purpose sslserver \
  server.cert.pem

openssl verify \
  -CAfile root-ca.cert.pem \
  -untrusted issuing-ca.cert.pem \
  -purpose sslclient \
  client.cert.pem
```

Esse teste verifica o caminho, mas ainda precisa ser complementado pelo hostname real,
pelo trust store do produto e por uma conexão TLS. `openssl s_client` ajuda a
observar o que o servidor apresenta, enquanto `curl` exercita a validação feita por
uma biblioteca HTTP. Os dois comandos podem produzir resultados diferentes quando
carregam CAs ou políticas distintas.

## Diferencie laboratório de emissão operacional

`openssl req` cria uma CSR, e `openssl x509 -req` pode assinar uma CSR em um fluxo
pequeno. Esses comandos não formam sozinhos uma CA operacional. Eles não aprovam a
identidade, não mantêm um inventário completo, não implementam uma fila de pedidos,
não publicam automaticamente o certificado e não coordenam revogação entre
consumidores.

O comando `openssl ca` adiciona um banco de estado baseado em arquivos. Ainda assim,
ele continua exigindo que o operador proteja o diretório, faça backup consistente,
evite duas emissões concorrentes e publique os artefatos com controle de acesso. A
diferença entre um laboratório e uma autoridade real não é somente trocar o comando:
é a existência de governança, aprovação, custódia, auditoria e recuperação.

## Verificações antes de instalar uma chave

Antes de distribuir uma chave privada, confirme que ela corresponde à folha e que a
folha corresponde à CSR aprovada. Comparar a chave pública evita instalar uma chave
que não pode completar `CertificateVerify` ou um certificado que foi emitido para
outro pedido.

```bash
openssl pkey \
  -in server.key.pem \
  -pubout \
  -outform DER | openssl dgst -sha256

openssl x509 \
  -in server.cert.pem \
  -pubkey \
  -noout | openssl pkey \
  -pubin \
  -outform DER | openssl dgst -sha256

openssl x509 \
  -in server.cert.pem \
  -noout \
  -checkend 2592000
```

Os dois primeiros hashes devem ser iguais. `-checkend` permite falhar quando a
validade termina dentro de uma janela definida, o que é útil em uma verificação de
pipeline ou de health check. A validação ainda precisa conferir SAN, finalidade,
emissor, cadeia e revogação.

Não coloque a senha da chave na linha de comando: ela pode aparecer em histórico,
process list ou logs de CI. Prefira um prompt interativo, um agente de secrets ou uma
integração de custódia que entregue o material somente ao processo autorizado. Se uma
chave precisa ser usada por um serviço sem interação, a proteção da chave em repouso
deve ser combinada com permissões, isolamento e rotação, não substituída por uma
senha embutida no script.

## Estado de uma CA baseada em arquivos

Uma configuração de `openssl ca` normalmente aponta para diretórios e arquivos que
representam estados diferentes:

| Estado | Função | Risco operacional |
| --- | --- | --- |
| Banco de índice | Registra certificados emitidos, válidos e revogados | Corrupção ou edição manual quebra o inventário |
| Arquivo de serial | Escolhe o serial da próxima emissão | Concorrência pode repetir ou perder números |
| Arquivo de CRL number | Versiona a CRL publicada | Publicação sem sincronização confunde consumidores |
| Diretório de certificados | Guarda folhas emitidas | Permissões e backup expõem identidades |
| Diretório de chaves | Guarda chaves da CA | Comprometimento altera toda a confiança abaixo |

O diretório precisa de controle de concorrência. Dois processos assinando ao mesmo
tempo podem ler o mesmo serial, modificar o índice de forma incompatível ou publicar
uma CRL que não corresponde ao conjunto de certificados emitidos. Bloqueio de arquivo,
fila de emissão ou uma ferramenta de CA com armazenamento transacional são opções
mais seguras que disparar comandos paralelos de shell.

Faça backup dos arquivos de estado juntos. Restaurar apenas a chave e esquecer o
índice pode impedir a revogação de uma folha já emitida; restaurar apenas o índice e
perder a chave pode preservar o inventário, mas tornar impossível assinar a próxima
CRL. O backup também precisa ser testado em uma cópia isolada para comprovar que a CA
consegue emitir, revogar e gerar a CRL depois da recuperação.

## PEM, DER e PKCS#12

PEM é uma representação textual base64 com marcadores, adequada para configuração,
mas não é sinônimo de conteúdo público nem de segurança. DER é a codificação binária
do objeto ASN.1. A extensão do arquivo não é suficiente para saber qual formato o
programa exige.

PKCS#12, normalmente com extensão `.p12` ou `.pfx`, pode agrupar chave privada,
certificado e cadeia em um contêiner protegido por senha. Ele é útil para importar
uma identidade em alguns sistemas operacionais, mas aumenta o impacto de uma senha
compartilhada e não deve ser enviado para um serviço que espera apenas a folha PEM.

Ao converter um contêiner, confirme se a cadeia está na ordem correta e se a chave
privada é exportável. O procedimento de importação precisa deixar claro qual
componente retém a chave, qual CA entra no trust store e quais cópias temporárias
serão destruídas.

## Validade, rotação e reload

A validade do certificado deve ser menor que a capacidade de detectar e responder a
um comprometimento, mas não tão curta que a renovação dependa de uma operação manual
frágil. O emissor precisa renovar antes de `notAfter`, distribuir folha e
intermediárias, confirmar permissões da chave e recarregar o consumidor.

Uma rotação sem interrupção normalmente segue esta ordem:

1. gerar uma chave nova em local protegido;
2. criar e aprovar a CSR;
3. emitir a nova folha com os mesmos usos necessários;
4. distribuir chave, folha e intermediárias com permissões corretas;
5. executar o teste de configuração do consumidor;
6. fazer reload e confirmar o certificado apresentado;
7. observar handshakes e retirar a folha antiga quando não houver dependências.

Se a chave antiga foi comprometida, essa ordem pode precisar ser invertida: a
revogação e o bloqueio de sessões se tornam prioritários. A decisão deve estar
associada ao motivo da rotação e não ser escondida num script que trata todos os
casos como renovação normal.

## Revogar com banco de CA

O comando `openssl x509` é útil para exemplos pontuais, mas não mantém sozinho o
inventário necessário para revogação. Uma CA que usa `openssl ca` mantém arquivos de
estado, como índice de certificados, número serial e número da próxima CRL. Depois
de configurar uma autoridade com esse estado, o fluxo conceitual é:

```bash
openssl ca -config ca.cnf -revoke server.cert.pem
openssl ca -config ca.cnf -gencrl -out root-ca.crl.pem
openssl verify \
  -CAfile root-ca.cert.pem \
  -CRLfile root-ca.crl.pem \
  -crl_check \
  server.cert.pem
```

Publicar a CRL, incluir sua URL em `cRLDistributionPoints`, distribuir a nova versão
e garantir que os verificadores realmente façam a consulta são etapas separadas.
Uma CA online também pode oferecer OCSP. Em ambientes maiores, uma ferramenta de
PKI como step-ca, Dogtag ou um serviço gerenciado costuma ser preferível a manter
manualmente o estado e a política em arquivos locais.

## Proteção da chave

A chave da CA é mais sensível que uma chave de servidor. Use uma raiz offline, uma CA
intermediária com validade e permissões menores, backups cifrados, quorum para
operações críticas e auditoria. Para chaves de serviço, planeje rotação, reload sem
interrupção e sobreposição entre certificado antigo e novo.

## Limites do estado local

O fluxo `openssl ca` é útil para entender o modelo de uma CA, mas os arquivos de
índice e serial precisam de exclusão mútua, backup consistente e proteção contra
edições concorrentes. Duas emissões simultâneas sobre o mesmo estado podem
produzir números repetidos, entradas inconsistentes ou uma CRL que não representa
todos os certificados emitidos.

Antes de usar uma CA baseada em arquivos, defina quem pode emitir, onde fica o
estado, como o estado é restaurado e como as operações são auditadas. O backup da
chave sem o índice produz uma identidade que não pode ser revogada corretamente;
o backup do índice sem a chave permite auditar o histórico, mas não operar a CA.
Esses artefatos possuem requisitos de proteção e recuperação diferentes.

## Perfil, extensão e finalidade

Não reutilize um único arquivo de extensão para raiz, intermediária, servidor e
cliente. A raiz normalmente não deve ser apresentada em cada conexão; a
intermediária emissora precisa restringir `basicConstraints` e `pathLen`; a folha
de servidor precisa de SAN DNS ou IP e `serverAuth`; a folha de cliente precisa
de uma identidade e `clientAuth`.

Uma emissão pode ser criptograficamente válida e ainda violar o contrato do
serviço se o uso, o nome ou a política de confiança estiverem errados. O pipeline
deve inspecionar o certificado emitido, verificar a cadeia e testar a finalidade
antes de copiar a chave para o consumidor.

## Relações

- [Certificado X.509](certificate.md) explica identidade, extensões e lifecycle.
- [CSR](csr.md) detalha a solicitação de assinatura.
- [Cadeia de certificados](certificate-chain.md) explica a validação do caminho.
- [Revogação](revocation.md) compara CRL, OCSP e rotação.
- [mTLS no Nginx](../tls/nginx-mtls.md) aplica certificados em um terminador TLS.

## Fontes primárias

- [OpenSSL documentation](https://docs.openssl.org/)
- [OpenSSL x509](https://docs.openssl.org/master/man7/x509/)
- [OpenSSL req](https://docs.openssl.org/master/man1/openssl-req/)
- [RFC 5280](https://www.rfc-editor.org/rfc/rfc5280)
