# Hiren's BootCD PE

Hiren's BootCD PE é um ambiente Windows PE x64 inicializável com ferramentas gratuitas para diagnóstico e recuperação. Ele é uma continuação comunitária do uso conhecido do Hiren's BootCD para emergências, mas não deve ser confundido com o Hiren's BootCD original, cuja última versão oficial foi publicada em 2012.

## Para que serve

O ambiente é útil quando o Windows instalado não inicia ou quando é necessário operar o disco sem carregar o sistema principal. Os usos incluem copiar dados antes de reinstalar, investigar armazenamento, executar ferramentas de diagnóstico, verificar conectividade e reparar alguns componentes do boot.

A seleção de ferramentas muda com a versão. Consulte a página oficial e o changelog antes de depender de um utilitário específico.

## Boot e requisitos

A edição PE é voltada a máquinas x64 modernas e suporta boot UEFI. A página do projeto informa requisito de pelo menos 4 GB de RAM para a edição atual, mas o consumo real depende dos drivers e programas carregados.

Grave a ISO em USB por uma ferramenta confiável, escolha o dispositivo no boot menu e confirme que Secure Boot e o modo de firmware são compatíveis. Em um servidor remoto, uma ISO pode ser anexada por mídia virtual do BMC, embora a transferência seja mais lenta.

## Procedimento de recuperação

1. Inicialize o PE sem montar automaticamente volumes sensíveis para escrita, quando essa opção existir.
2. Identifique disco, volumes, usuários e sistema de arquivos.
3. Faça uma cópia dos dados importantes para outro dispositivo.
4. Colete logs e informações antes de reparar.
5. Execute uma ferramenta por vez e preserve o resultado.
6. Reinicie somente depois de desmontar a mídia e revisar alterações.
7. Valide boot, integridade dos dados e drivers no sistema normal.

Não use uma ferramenta de limpeza, senha ou partição sem confirmar o alvo. Um ambiente live tem acesso amplo aos discos.

## Confiança e legalidade

Baixe a imagem de uma fonte oficial ou de um espelho cuja integridade possa ser verificada. Não substitua arquivos da imagem por versões modificadas sem entender a origem e o risco.

O projeto atual declara que inclui ferramentas gratuitas e legais. Isso não significa que toda ferramenta tenha a mesma licença ou que um executável externo seja seguro por definição. Mantenha inventário, verifique hashes e prefira ferramentas com origem conhecida.

## Limitações

Hiren's BootCD PE não é um sistema de backup completo, não garante compatibilidade com todo hardware e não substitui ferramentas específicas do fabricante. Não é a primeira escolha para testar RAM profundamente, recuperar uma partição criptografada sem a chave ou diagnosticar um BMC remoto.

Quando a máquina não inicia por falha física, use diagnóstico especializado. Quando o armazenamento está instável, priorize imagem ou cópia de recuperação antes de reparos in-place.

## Relações

- [GParted Live](gparted-live.md) é uma alternativa Linux focada em particionamento.
- [MemTest86 e Memtest86+](memtest.md) são mais adequados para testes de memória.
- [iDRAC](../hardware/idrac.md) pode anexar a ISO por mídia virtual.
- [Instalação pela rede](network-install.md) reduz a dependência de USB.

## Fontes primárias

- [Hiren's BootCD PE](https://www.hirensbootcd.org/)
- [About Hiren's BootCD PE](https://www.hirensbootcd.org/about/)
- [Hiren's BootCD PE how-to guides](https://www.hirensbootcd.org/howtos/)
