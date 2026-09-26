# AppImage

AppImage é um formato de distribuição de aplicações Linux em que o usuário recebe um arquivo executável que contém a aplicação e parte das bibliotecas necessárias. O runtime monta ou acessa o conteúdo da imagem e inicia o programa sem exigir uma instalação tradicional no gerenciador de pacotes.

## Empacotamento

O build normalmente começa em um `AppDir`, que contém o executável, bibliotecas, recursos, metadados AppStream e o arquivo `.desktop`. Ferramentas como `linuxdeploy`, `appimage-builder`, `appimagetool` e serviços como Open Build Service podem produzir a imagem. O upstream pode compilar do código ou converter um pacote existente, mas a responsabilidade pela compatibilidade continua sendo de quem publica o AppImage.

## Segurança

AppImage não fornece sandbox obrigatório. O processo executa com as permissões do usuário e pode acessar os mesmos recursos que outro binário local, limitado pelas permissões normais e por políticas externas como SELinux, AppArmor ou sandbox adicional. A extensão `.AppImage` não prova autenticidade.

Distribuidores devem publicar checksums, assinatura digital, origem do build e política de atualização. O formato suporta mecanismos opcionais de atualização, mas não existe uma loja ou canal central obrigatório para todos os AppImages.

## Atualização e integração

O arquivo pode ser substituído por uma nova versão, mantido em um diretório de aplicações ou integrado ao menu por ferramentas como `appimaged`. A atualização pode ser feita pelo projeto, por um mecanismo embutido ou manualmente. Isso é diferente de um pacote APT que participa do estado de dependências da distribuição.

## Quando usar

AppImage é útil para testar uma versão independente da distribuição, entregar uma ferramenta a usuários sem alterar o sistema ou transportar uma aplicação em um único arquivo. Ele é menos conveniente quando são necessários patches da distribuição, atualizações centralizadas, integração profunda com serviços do sistema ou confinamento obrigatório.

## Fontes primárias

- [AppImage](https://appimage.org/)
- [AppImage packaging guide](https://docs.appimage.org/packaging-guide/index.html)
- [AppImage updates](https://docs.appimage.org/packaging-guide/optional/updates.html)
