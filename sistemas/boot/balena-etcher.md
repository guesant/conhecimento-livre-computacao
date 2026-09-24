# balenaEtcher

balenaEtcher grava imagens de sistema em cartões SD e unidades USB. O fluxo principal escolhe uma imagem, escolhe um destino e inicia a gravação, com validação posterior quando habilitada.

## Modelo de uso

Etcher trata a entrada como uma imagem a ser gravada em bloco. Ele é apropriado para:

- imagens de Raspberry Pi;
- sistemas live;
- imagens raw de appliance;
- recuperação de dispositivos;
- imagens comprimidas suportadas pela versão.

Ele não é um gerenciador multiboot. Depois da gravação, o conteúdo da unidade segue o layout da imagem e não uma partição de dados criada para armazenar várias ISOs.

## Fluxo seguro

1. Baixe a imagem do projeto que a publica.
2. Confirme checksum ou assinatura.
3. Abra Etcher e selecione a imagem.
4. Confira o destino por modelo e capacidade.
5. Inicie a gravação.
6. Aguarde a validação.
7. Ejete a unidade antes de removê-la.

A seleção do destino merece a mesma atenção que um comando dd. Uma imagem gravada no disco errado pode destruir o sistema operacional ou dados de recuperação.

## Vantagens e limites

Etcher reduz erros comuns de seleção e torna a gravação acessível para quem não precisa controlar cada parâmetro de bloco. Ele suporta Windows, macOS e Linux em arquiteturas documentadas pelo projeto.

A abstração também esconde detalhes. Quando for necessário escolher GPT, MBR, ISO mode, DD mode ou opções específicas do instalador Windows, Rufus ou uma ferramenta do próprio sistema pode ser melhor.

## Diagnóstico

Se a validação falhar, descarte a unidade como suspeita até testar leitura completa e outra mídia. Verifique a imagem original, espaço disponível, permissões, conexão USB e alimentação do dispositivo.

Se a unidade grava mas não inicia, confirme se a imagem suporta o firmware e a arquitetura. Etcher não transforma uma imagem não inicializável em uma imagem inicializável.

## Segurança

Use versões do projeto oficial e valide a imagem antes da gravação. Não deixe uma unidade de recuperação conectada a um computador de produção depois do boot se ela não for necessária.

## Relações

- [dd](dd.md) executa a cópia bruta diretamente no shell.
- [Rufus](rufus.md) oferece mais opções para mídias Windows e firmware.
- [Ventoy](ventoy.md) mantém várias imagens em um mesmo dispositivo.

## Fontes primárias

- [Etcher documentation](https://etcher-docs.balena.io/)
- [Etcher manual testing](https://etcher-docs.balena.io/MANUAL-TESTING/)
