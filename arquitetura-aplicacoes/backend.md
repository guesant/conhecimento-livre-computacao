# Backend

Backend é a parte da aplicação que recebe solicitações confiáveis o suficiente para serem processadas, aplica regras de negócio, acessa dados e integra sistemas externos. Ele pode ser um servidor web, uma API, um worker, um job assíncrono ou uma combinação deles.

## Responsabilidades

Um backend normalmente executa:

- autenticação e resolução de identidade;
- autorização no ponto que protege o recurso;
- validação de entrada e normalização;
- regras de domínio e invariantes;
- transações e persistência;
- integração com serviços externos;
- filas, jobs e tarefas demoradas;
- serialização de respostas e erros;
- observabilidade, auditoria e limites.

Um controller ou handler HTTP deve traduzir a entrada para um caso de uso e devolver uma resposta. Não é saudável concentrar query, decisão de negócio, renderização e integração externa no mesmo método.

## API e apresentação

A API é um contrato de interação, não necessariamente a implementação inteira do backend. REST, GraphQL, gRPC e mensagens possuem semânticas diferentes para recursos, erros, streaming, versionamento e descoberta.

DTOs separam o formato externo do modelo de persistência. Isso evita expor colunas internas, permite validar campos e reduz o acoplamento entre banco e consumidores. Uma resposta pública deve selecionar os campos necessários e aplicar paginação, limites e autorização na própria consulta.

## Domínio e dados

Uma aplicação pode ter uma camada de domínio explícita, uma arquitetura por casos de uso ou módulos coesos dentro de um framework. O nome da pasta importa menos que as fronteiras: regra de negócio não deve depender diretamente de detalhes de HTTP ou de um widget da interface.

No backend monolítico, módulos podem compartilhar o mesmo processo e banco, mas devem possuir contratos internos, donos de tabelas e regras de dependência. Em microsserviços, a fronteira deve incluir o dado: compartilhar diretamente a mesma tabela entre serviços cria acoplamento e dificulta evolução independente.

## Síncrono e assíncrono

O caminho síncrono deve ser curto e previsível. Trabalho pesado, retry prolongado, consulta a muitos registros, geração de arquivo e integração lenta devem ir para filas ou jobs quando o usuário não precisa do resultado imediatamente.

Jobs precisam de idempotência, timeout, retry limitado, backoff, dead letter ou mecanismo de investigação. Uma fila não elimina a necessidade de consistência; apenas muda quando e onde a operação é concluída.

## Escala e confiabilidade

Escalar horizontalmente exige que sessões, arquivos temporários, locks e caches tenham uma estratégia compatível com várias instâncias. Banco, filas e serviços externos continuam sendo limites de capacidade.

Timeouts devem existir em chamadas de rede. Retries precisam respeitar idempotência e evitar tempestade. Circuit breakers, bulkheads e rate limits protegem o backend, mas não compensam uma interface mal definida.

## Segurança

Valide toda entrada no servidor, use parâmetros em queries, limite paginação, trate concorrência e aplique autorização antes de retornar dados. Diferencie `404`, `401`, `403`, validação e indisponibilidade sem vazar existência de recursos protegidos além do necessário.

Segredos devem vir da infraestrutura de runtime, não do frontend nem do repositório. Logs não devem conter tokens, senhas ou payloads sensíveis por padrão.

## Fontes

- [OWASP, Application Security Verification Standard](https://owasp.org/www-project-application-security-verification-standard/)
- [Microsoft, Backend for Frontend](https://learn.microsoft.com/en-us/azure/architecture/patterns/backends-for-frontends)
- [Martin Fowler, Microservices](https://martinfowler.com/articles/microservices.html)
