# Startup probe

Startup probe protege aplicações cuja inicialização pode demorar. Enquanto ela ainda não teve sucesso, liveness e readiness não assumem seu comportamento normal.

Ela permite tolerância ampla durante startup sem tornar a liveness excessivamente permissiva depois que a aplicação já iniciou.

Veja [liveness](liveness-probe.md) e [readiness](readiness-probe.md).