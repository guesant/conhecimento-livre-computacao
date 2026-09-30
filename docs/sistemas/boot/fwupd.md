# fwupd

fwupd é um serviço e conjunto de ferramentas para consultar, distribuir e aplicar atualizações de firmware em sistemas Linux. Ele fornece uma interface comum para dispositivos suportados e pode obter metadados e pacotes do Linux Vendor Firmware Service, LVFS, quando o fabricante publica o firmware nesse serviço.

fwupd não torna qualquer firmware atualizável. O dispositivo, o firmware, o fabricante e a plataforma precisam oferecer um método compatível, como cápsulas UEFI, atualização de dispositivo USB ou um protocolo específico do hardware.

## Componentes

O daemon `fwupd` executa as operações privilegiadas. `fwupdmgr` é a ferramenta de linha de comando usada pelo administrador para consultar dispositivos, atualizar metadados, listar versões e iniciar atualizações. Ambientes gráficos podem chamar o mesmo serviço por D-Bus.

O LVFS distribui metadados e firmware publicados pelos fabricantes. A confiança depende das assinaturas, da cadeia de distribuição e da validação feita pelo dispositivo. A existência de uma atualização no LVFS não significa que ela seja aplicável a todo modelo parecido.

## Fluxo de uso

Uma sequência de diagnóstico comum é:

```bash
fwupdmgr get-devices
fwupdmgr refresh
fwupdmgr get-updates
fwupdmgr update
fwupdmgr get-history
```

`get-devices` identifica o hardware e suas capacidades. `refresh` atualiza os metadados disponíveis. `get-updates` mostra candidatos e `update` aplica as atualizações aprovadas. `get-history` ajuda a verificar o resultado e a investigar falhas.

As versões atuais podem oferecer comandos adicionais para avaliar a postura de segurança. Consulte a ajuda instalada e a documentação da distribuição, porque nomes e comportamentos podem mudar entre versões.

## Cápsulas UEFI e dbx

Uma atualização de firmware pode ser entregue como cápsula UEFI, que o sistema operacional grava para ser processada pelo firmware no próximo boot. O fluxo exige suporte do equipamento e pode reiniciar a máquina várias vezes. Não interrompa energia durante a aplicação.

fwupd também pode distribuir atualizações da lista dbx quando o equipamento e a distribuição suportam esse fluxo. Uma atualização de dbx melhora a proteção contra carregadores revogados, mas deve ser avaliada junto com a cadeia de boot instalada e com as mídias de recuperação disponíveis.

## Segurança operacional

Antes de atualizar firmware, confirme o modelo exato, a fonte do pacote, o nível de bateria ou a alimentação estável, a existência de backup e a disponibilidade de recuperação local ou remota. Em servidores, confirme também como o BMC, a console serial e o boot alternativo serão acessados se o sistema não voltar.

Não use firmware de outro modelo apenas porque o conector ou o nome comercial parece igual. Firmware pode alterar tabelas de hardware, políticas de boot e compatibilidade de dispositivos. A atualização deve ser registrada com versão anterior, versão nova, data e resultado.

## Diagnóstico

Quando um dispositivo não aparece, verifique se o kernel o identifica, se o plugin correspondente está instalado, se o fabricante oferece o modelo no LVFS e se o firmware permite a operação. Mensagens do daemon e do journal ajudam a distinguir ausência de suporte, falha de assinatura, dispositivo ocupado e erro durante a instalação.

Em uma falha pós-atualização, preserve os logs antes de repetir a operação. Tentar várias atualizações sem registrar o estado pode apagar evidências e dificultar o contato com o fabricante.

## Fontes primárias

- [fwupd](https://fwupd.org/)
- [Documentação do fwupd](https://fwupd.github.io/libfwupdplugin/)
- [Linux Vendor Firmware Service](https://fwupd.org/lvfs/docs)
- [Repositório upstream do fwupd](https://github.com/fwupd/fwupd)
