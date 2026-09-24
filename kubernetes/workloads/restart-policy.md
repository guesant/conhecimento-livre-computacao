# Restart policy

restartPolicy define como containers de um Pod são reiniciados após término, dentro da semântica suportada pelo workload.

Jobs normalmente usam Never ou OnFailure. A política não substitui limites de tentativas do controller.

Veja [Job](job.md) e [backoff limit](backoff-limit.md).
