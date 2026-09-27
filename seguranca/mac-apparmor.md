# AppArmor

AppArmor é um mecanismo de Mandatory Access Control, MAC, para Linux. Ele
associa perfis a programas e limita caminhos, capacidades, operações de rede e
outros recursos. A política é centrada na identidade do executável e costuma
ser ajustada de forma incremental.

## Modelo

Um perfil descreve o que um processo pode ler, escrever, executar, abrir ou
acessar. A política pode usar herança, transições e regras para abstrair um
conjunto de caminhos. O processo continua sujeito às permissões DAC, capabilities,
namespaces, seccomp e às regras do serviço que está chamando.

O modo enforcing bloqueia operações não permitidas. O modo complain registra
violações sem bloquear e é útil para gerar uma hipótese inicial, mas não deve
ser confundido com proteção ativa. A política gerada precisa ser revisada para
não transformar todo acesso observado em permissão permanente.

## Operação

Comece identificando o perfil efetivo e os eventos de negação. Relacione o
processo, o caminho, a operação, o namespace e o serviço que iniciou a ação.
Teste tanto o caminho permitido quanto operações que devem continuar proibidas.
Empacote e versiona os perfis junto com o serviço, evitando alterações manuais
que desaparecem na próxima atualização.

Ubuntu carrega AppArmor por padrão em instalações e imagens comuns, mas a
presença de um pacote não prova que o perfil esteja carregado ou em enforcing.
Debian, openSUSE e outras distribuições podem oferecer suporte com defaults
diferentes. Verifique o host real com as ferramentas da distribuição.

## Relações

- [Mandatory Access Control](autorizacao/modelos/mac.md) explica o modelo geral.
- [SELinux](mac-selinux.md) usa outra representação de política e outro fluxo
  operacional para aplicar MAC.
- [Capabilities](../sistemas/linux/capabilities.md) e [seccomp](../sistemas/linux/seccomp.md)
  são controles complementares, não substitutos.

## Fonte primária

- [AppArmor documentation](https://apparmor.net/)
