# Armazenamento de dados

Armazenamento é a camada que preserva bytes, objetos ou cópias derivadas além do processo que os produziu. Ela inclui armazenamento de objetos, caches e políticas de expiração, mas não deve ser confundida com o modelo de consulta de um banco ou com uma fila de trabalho.

## Páginas

- [Silo](../armazenamento-objetos/silo.md) apresenta um storage compatível com a API de objetos do S3.
- [Cache](../cache.md) trata cópias derivadas, invalidação e stale data.
- [TTL e expiração](../ttl.md) trata validade temporal em caches, mensagens, DNS e sessões.

Armazenamento de objetos é apropriado para arquivos e artefatos endereçados por chave. Cache reduz latência e carga, mas pode desaparecer ou ficar obsoleto. Um TTL define uma política de validade, não uma garantia de que um dado será removido exatamente no instante do vencimento.

## Decisão

Avalie durabilidade, consistência, versionamento, lifecycle, custo de leitura e escrita, egress, criptografia, retenção e restauração. Para dados críticos, defina como a cópia será validada e recuperada. Para dados derivados, defina como serão reconstruídos quando o cache ou o objeto temporário for perdido.
