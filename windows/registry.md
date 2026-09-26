# Registro do Windows

O Registro é uma base hierárquica usada pelo Windows e por aplicações para armazenar configuração, associações, políticas e estado. Ele é exposto por hives, chaves, subchaves e valores. `regedit` é uma interface gráfica para inspeção e edição; não é um mecanismo de backup, auditoria ou validação por si só.

## Hives e escopos

Entre os hives conhecidos estão `HKEY_LOCAL_MACHINE`, para configuração da máquina, `HKEY_CURRENT_USER`, para o usuário atual, `HKEY_USERS`, para perfis carregados, e `HKEY_CLASSES_ROOT`, uma visão combinada de associações de classes. O mesmo nome pode existir em escopos diferentes, e a aplicação pode preferir política de máquina ou de usuário.

## Segurança e operação

Chaves possuem ACLs e podem ser alteradas por processos com privilégios. Um valor incorreto pode impedir login, quebrar serviços, alterar políticas de segurança ou causar comportamento difícil de diagnosticar. Antes de editar, exporte a chave relevante, documente a mudança, teste o rollback e prefira Group Policy, MDM ou a configuração suportada pela aplicação quando existir.

Não use scripts encontrados na internet que importam grandes arquivos `.reg` sem revisar todas as chaves e valores. O Registro não é um depósito para qualquer configuração: arquivos de configuração, políticas declarativas e mecanismos de gerenciamento geralmente são mais auditáveis.

## Ferramentas

`regedit` inspeciona e edita. `reg.exe` permite operações de linha de comando. PowerShell oferece APIs e cmdlets para automação, mas uma automação precisa tratar tipos, permissões, caminhos 32-bit e 64-bit e o hive correto.

## Fonte primária

- [Windows Registry for developers](https://learn.microsoft.com/en-us/windows/win32/sysinfo/registry)
- [Registry functions](https://learn.microsoft.com/en-us/windows/win32/sysinfo/registry-functions)
