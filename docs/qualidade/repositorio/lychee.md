# Lychee

Lychee verifica links em arquivos e documentação. Ele pode encontrar destinos
HTTP inacessíveis, referências locais quebradas e âncoras ausentes, conforme os
formatos e opções usados na execução.

## Classes de link

Links locais devem ser verificados com o sistema de arquivos e com o parser da
documentação. Links externos podem falhar por indisponibilidade transitória,
rate limit, autenticação ou bloqueio de automação. Misturar as duas classes em
um único diagnóstico dificulta saber se houve regressão real.

O gate deve tratar links internos quebrados como erro determinístico. Para
fontes externas, configure timeout, tentativas e exclusões estreitas. Uma
exclusão deve explicar o comportamento do destino, não apenas esconder a
falha de uma execução.

## Execução no repositório

Execute Lychee sobre as extensões documentais que o projeto versiona e
preserve a lista de caminhos gerados ou temporários fora da análise. Depois de
mover uma página, valide links relativos e âncoras antes de atualizar a
navegação. Uma página removida pode continuar acessível por compatibilidade,
mas não deve deixar referências quebradas.

## Failure modes

Um falso positivo pode resultar de redirecionamento, certificado, resposta
intermitente ou URL que exige autenticação. Reproduza o destino fora do
agregador, diferencie erro permanente de erro de rede e só então ajuste a
configuração. Ignorar um domínio inteiro esconde regressões reais.

## Relações

- [Manutenção de repositório](index.md) posiciona a verificação de links no
  ciclo de manutenção.
- [Diátaxis](../../diataxis.md) ajuda a separar links de tutorial, explicação,
  referência e operação.

## Fonte primária

- [Lychee](https://lychee.cli.rs/)
