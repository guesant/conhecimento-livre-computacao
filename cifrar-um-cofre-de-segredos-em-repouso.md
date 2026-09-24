# Cifrar um cofre de segredos em repouso

Além do par SOPS mais age e do Ansible Vault, já cobertos em [Criptografia de segredos no Git](criptografia-de-segredos-no-git.md), existe um espaço mais amplo de ferramentas para manter um material crítico (uma chave privada, um pequeno conjunto de segredos de bootstrap) cifrado em repouso fora de qualquer repositório versionado, cada uma resolvendo o problema com um modelo diferente.

Nenhuma dessas ferramentas depende de reimplementar criptografia própria; todas se apoiam em primitivas criptográficas já maduras e auditadas, a diferença está em como cada uma organiza e expõe essa cifragem para o uso do dia a dia.

## Sistema de arquivos cifrado por arquivo: `gocryptfs`

`gocryptfs` cifra um diretório inteiro arquivo por arquivo, incluindo o nome de cada arquivo, montando a versão decifrada sob demanda através de FUSE (o mecanismo que permite implementar um sistema de arquivos inteiro em espaço de usuário, sem exigir um módulo de kernel dedicado, já mencionado em [rsync e sshfs](rsync-e-sshfs.md)).

O ganho central sobre cifrar um contêiner monolítico inteiro é que cada arquivo dentro do diretório cifrado corresponde a um arquivo cifrado individual no armazenamento subjacente, o que permite sincronizar ou versionar mudanças incrementais; o custo é que cifrar também o nome do arquivo (não só o conteúdo) elimina qualquer possibilidade de diff legível numa ferramenta de controle de versão, porque o nome muda de forma imprevisível junto com qualquer mudança de conteúdo.

Para quem usa macOS, `gocryptfs` depende de uma implementação de FUSE para esse sistema (macFUSE, ou a alternativa mais recente FUSE-T), e compatibilidade entre versões específicas de cada uma dessas implementações e do próprio macOS é um ponto que vale confirmar antes de depender dessa combinação para um material crítico, já que problemas de compatibilidade entre FUSE e uma versão específica de sistema operacional têm histórico de aparecerem sem aviso após uma atualização.

## Contêiner cifrado com interface própria: Cryptomator

Cryptomator cifra um conjunto de arquivos dentro de um "cofre" (vault) próprio, com uma interface dedicada para abrir e fechar esse cofre, pensado originalmente para proteger arquivos sincronizados através de um serviço de nuvem não confiável.

Sua própria documentação oficial recomenda não depender dele como uma solução de backup por si só, e cofres sincronizados através de uma ferramenta de sincronização de arquivos que aplica apenas parte de uma mudança (uma sincronização interrompida no meio, por exemplo) têm histórico documentado de corrupção do cofre inteiro, não apenas do arquivo afetado.

Isso é relevante especificamente para quem pensaria em usar essa ferramenta como parte de uma estratégia de sincronizar um material crítico entre mais de uma máquina através de um serviço de nuvem comum.

## Imagem de disco cifrada nativa do sistema operacional

Sistemas operacionais atuais oferecem, nativamente, um mecanismo de imagem de disco cifrada sem instalar nada adicional: no macOS, uma sparsebundle cifrada criada pelo próprio utilitário de disco do sistema; em outros sistemas, um mecanismo equivalente próprio.

A vantagem é não depender de nenhuma ferramenta de terceiro, apoiando-se inteiramente em algo que o próprio sistema operacional já mantém e atualiza; a limitação óbvia é o acoplamento ao sistema operacional específico que criou essa imagem, o que se torna relevante quando o material precisa ser acessado, ou recuperado, a partir de uma máquina rodando um sistema operacional diferente do que criou a imagem originalmente.

## Cifrar cada arquivo individualmente com uma ferramenta de proposição única

Uma alternativa mais simples que qualquer sistema de arquivos ou contêiner dedicado é cifrar cada arquivo sensível individualmente com uma ferramenta de cifragem assimétrica de proposição única, como o próprio `age` (já coberto em profundidade em [Criptografia de segredos no Git](criptografia-de-segredos-no-git.md)) usado diretamente sobre um arquivo solto, sem um sistema de arquivos ou contêiner por cima.

Isso evita toda a complexidade adicional de montar e desmontar um volume, ao custo de gerenciar a organização dos arquivos cifrados manualmente, sem a conveniência de navegar uma estrutura de diretórios já decifrada enquanto o cofre está "aberto".

Um gerenciador de senha de linha de comando como o `pass` organiza esse mesmo princípio (um valor por arquivo, cifrado individualmente) de forma um pouco mais estruturada: cada segredo vira um arquivo cifrado com GPG dentro de uma árvore de diretórios que funciona como categorização, e o histórico de mudanças em si pode ser versionado com git, já que o conteúdo de cada arquivo continua sendo apenas texto cifrado.

`passage` é a variante que troca GPG por `age` como mecanismo de cifragem, a mesma vantagem de simplicidade de chave já discutida na comparação entre os dois em [Criptografia de segredos no Git](criptografia-de-segredos-no-git.md#age-contra-pgp-por-que-a-distribuicao-de-chave-publica-muda-tudo), aplicada aqui a um gerenciador de senha de linha de comando em vez de a segredos de um cluster Kubernetes.

## Compartilhamento de segredo: dividir para que ninguém sozinho reconstrua

O esquema de compartilhamento de segredo de Shamir divide um segredo em várias partes (shares), de forma que um número mínimo delas, menor que o total, seja suficiente para reconstruir o segredo original, mas qualquer quantidade menor que esse mínimo não revele nada sobre ele. Isso resolve um problema diferente de cifrar um arquivo: em vez de uma chave única que decifra tudo, o segredo em si fica dividido entre múltiplos guardiões, nenhum dos quais consegue reconstruí-lo sozinho.

Uma limitação real de implementações mais simples desse esquema (algumas ferramentas de linha de comando amplamente disponíveis, por exemplo) é a ausência de verificação de integridade nas partes: um share corrompido ou incorreto pode reconstruir silenciosamente um segredo errado, sem nenhum aviso de que algo deu errado no processo, uma implementação mais cuidadosa do esquema deveria incluir verificação que detecte essa condição antes de aceitar o resultado como válido.

## Chave protegida por hardware

Um token de hardware dedicado (o mesmo tipo de dispositivo já descrito em [SSH](ssh.md#chaves-em-hardware-yubikey-e-login-assimetrico) para autenticação SSH) pode, em princípio, também proteger uma chave de decifragem de um cofre de segredos, com a mesma vantagem estrutural, a chave nunca existe fora do chip.

Na prática, a viabilidade dessa combinação depende do suporte específico da ferramenta de sistema operacional usada para gerar a chave, e do suporte da própria ferramenta de cifragem ao tipo de chave resultante.

Nem toda combinação de sistema operacional, protocolo de chave de hardware e ferramenta de cifragem já suporta essa integração de ponta a ponta, então vale confirmar contra a versão específica de cada peça envolvida antes de assumir que a combinação funciona, em vez de assumir que qualquer chave de hardware é intercambiável com qualquer ferramenta.

## Gerenciador de senha comercial com CLI

Um gerenciador de senha comercial com suporte a linha de comando e integração com automação (a maioria dos grandes fornecedores oferece isso hoje) resolve o problema de guardar um material crítico com uma interface unificada, sincronização entre dispositivos já resolvida pelo fornecedor, e frequentemente um recurso de compartilhamento controlado entre múltiplas pessoas.

O custo é confiar a cifragem e a disponibilidade desse material a um fornecedor terceiro, uma dependência de disponibilidade e de confiança que uma solução inteiramente local não tem; se esse custo compensa a conveniência depende de quanto a organização já confia naquele fornecedor para outros materiais sensíveis, e de quantas pessoas realmente precisam de acesso compartilhado e controlado ao mesmo material.

## Módulo de segurança de hardware (TPM)

Um módulo de plataforma confiável (TPM), presente em boa parte do hardware moderno, pode selar uma chave de forma que ela só seja liberada quando o estado do hardware e do processo de inicialização corresponder exatamente ao esperado, uma proteção contra extrair a chave de um disco copiado para outra máquina.

A limitação prática é a disponibilidade desse hardware especificamente na máquina em questão, incluindo máquinas virtuais, que nem sempre expõem um TPM para o sistema convidado, e a portabilidade: uma chave selada a um TPM específico não migra facilmente para outro hardware, o que é uma proteção deliberada contra um cenário de ataque, mas também uma limitação real quando o objetivo inclui poder recuperar o material a partir de qualquer máquina disponível, não só da original.

## Continue por aqui

[Criptografia de segredos no Git](criptografia-de-segredos-no-git.md) cobre SOPS, age e Ansible Vault em profundidade, as opções mais diretamente integradas a um fluxo de repositório versionado. [SSH](ssh.md) cobre o mecanismo de chave protegida por hardware com mais detalhe, no contexto de autenticação em vez de cifragem de cofre.
