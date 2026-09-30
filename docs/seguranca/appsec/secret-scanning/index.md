# Secret scanning

Secret scanning procura material que se parece com credenciais: tokens, chaves, senhas, certificados privados e outros valores cuja exposição pode conceder acesso.

A propriedade mais importante desse problema é histórica. Remover uma credencial do arquivo atual não a remove automaticamente dos commits anteriores, caches, artefatos, forks ou clones que já a receberam.

## Casos de uso

Secret scanning pode atuar antes do commit, no pull request, sobre o histórico completo e continuamente sobre repositórios já existentes. Cada momento reduz um risco diferente: prevenção local diminui a chance de publicação; CI impede novas exposições de avançarem; varredura histórica encontra dívida antiga.

## Exemplo

Se um token válido foi commitado e depois removido em outro commit, a correção primária é revogar ou rotacionar o token. Reescrever o histórico pode reduzir persistência e redistribuição, mas não recupera a confidencialidade de um valor que terceiros já podem ter copiado.

## Boas práticas

Combine padrões específicos de provedores com heurísticas quando apropriado. Escaneie histórico quando o objetivo é descobrir exposições antigas. Trate findings válidos como incidentes de credencial, não como simples defeitos de lint. Prefira credenciais curtas, escopos mínimos e mecanismos que facilitem rotação.

## Más práticas

Apagar a linha e manter a mesma credencial ativa é a má prática clássica. Também é perigoso colocar valores reais numa allowlist apenas para silenciar a ferramenta, registrar secrets nos próprios logs do scanner ou supor que alta entropia identifica todo tipo de segredo.

## Ferramentas

Gitleaks é uma implementação popular dessa categoria. Outros provedores oferecem secret scanning integrado ao serviço de hospedagem ou a plataformas de segurança. Ferramentas diferem em regras, capacidade de analisar histórico, validação de credenciais e integração com prevenção de commit.

## Fontes

- Gitleaks: <https://gitleaks.io/>
- GitHub, About secret scanning: <https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning>

## Continue por aqui

[Criptografia de segredos no Git](../../../criptografia-de-segredos-no-git.md) trata do caso deliberado em que material cifrado precisa permanecer versionado. Secret scanning trata da exposição acidental do segredo em claro.
