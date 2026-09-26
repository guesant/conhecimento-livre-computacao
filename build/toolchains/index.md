# Toolchains

Uma toolchain é o conjunto de compiladores, linkers, SDKs, bibliotecas, headers, runtimes e utilitários necessários para produzir ou analisar software de uma plataforma. Ela define o ambiente técnico usado pelo sistema de build, mas não é o próprio grafo de build.

## Componentes documentados

- [LLVM](../llvm.md) fornece infraestrutura de compiladores e ferramentas de análise.
- [Hermit](../hermit.md) ajuda a fornecer ferramentas herméticas e previsíveis ao projeto.
- [Nix](../nix.md) modela pacotes e ambientes de forma declarativa.
- [pkgx](../pkgx.md) facilita a obtenção de ferramentas por versões e referências portáveis.

Uma toolchain pode ser nativa, cross-compiled, hospedada em um container ou montada por um gerenciador declarativo. Fixar versões reduz drift entre máquina local, CI e ambiente de release, mas aumenta a responsabilidade de atualizar imagens, caches, certificados e dependências de segurança.

## O que não pertence a esta categoria

CMake, Meson, Make e Ninja são sistemas de build ou seus executores. Nx, Turborepo e moon coordenam tarefas entre projetos de um monorepo. Eles podem consumir uma toolchain, mas resolverem problemas diferentes. Manter essas categorias separadas torna mais claro se uma falha vem do compilador, do grafo de build ou do coordenador de tarefas.

## Critérios

Escolha uma toolchain considerando alvo, ABI, suporte da linguagem, depuração, licenciamento, origem dos binários, reprodutibilidade, patches aplicados e ciclo de atualização. O mesmo nome de compilador pode representar versões e configurações diferentes em distribuições, imagens de container e ambientes de CI.
