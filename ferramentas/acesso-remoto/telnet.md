# Telnet

Telnet é um protocolo de terminal remoto definido originalmente para operar
uma sessão interativa sobre TCP. O servidor tradicional escuta na porta TCP
23. O protocolo transporta caracteres e comandos de terminal, mas não oferece
criptografia nem autenticação moderna por si só.

## Uso histórico e atual

Telnet foi usado para terminais remotos, testes de serviços e administração de
equipamentos. Hoje SSH é a escolha para administração porque protege o canal,
valida a identidade do host e oferece autenticação e encaminhamento mais
adequados.

O comando `telnet` também aparece em procedimentos antigos para testar se uma
porta TCP aceita conexão. Esse uso não transforma a sessão em uma conexão
segura e pode ser substituído por `nc`, `curl`, `openssl s_client` ou uma
ferramenta específica que valide o protocolo esperado.

## Riscos

Uma sessão Telnet pode expor credenciais, comandos, respostas e dados a quem
consegue observar o caminho. Não publique Telnet na Internet. Em redes legadas,
restrinja a origem por ACL ou firewall, isole a rede de administração, registre
o acesso e estabeleça um plano de migração para SSH ou para o protocolo seguro
do equipamento.

Não confunda Telnet com o terminal local, com SSH ou com um simples teste de
porta. Um teste TCP pode confirmar apenas que um socket aceitou a conexão; ele
não confirma autenticação, capacidade do serviço ou segurança do protocolo.

## Relações

- [SSH](../../ssh.md) é a alternativa usual para terminal remoto seguro.
- [Ferramentas de acesso remoto](index.md) compara clientes e transportes.
- [Diagnóstico de rede](../../diagnostico/rede.md) organiza testes de conexão.

## Fonte primária

- [RFC 854, Telnet Protocol Specification](https://www.rfc-editor.org/rfc/rfc854)
