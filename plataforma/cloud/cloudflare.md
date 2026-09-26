# Cloudflare

Cloudflare opera uma rede de edge para DNS, CDN, proxy reverso, segurança de aplicações, mitigação de DDoS, conectividade privada e execução distribuída. A plataforma também inclui Workers, armazenamento, bancos orientados à edge e recursos de desenvolvimento. Seu centro de gravidade é colocar funções de rede e aplicação próximas do usuário, não oferecer uma VM tradicional para qualquer workload.

## Modelo de plataforma

DNS direciona o nome. O proxy pode terminar TLS, aplicar cache, WAF e políticas. A CDN serve conteúdo a partir da borda. Workers executam JavaScript, TypeScript ou outros runtimes compatíveis com o modelo de execução da plataforma. Produtos como R2 e Durable Objects tratam classes específicas de armazenamento e coordenação, mas não devem ser presumidos como um banco relacional genérico.

## Quando faz sentido

Cloudflare é uma camada forte para proteger e acelerar aplicações, publicar sites, controlar DNS, conectar redes privadas, executar lógica próxima dos usuários e reduzir a exposição direta da origem. Também pode ser usada como parte de uma arquitetura em que compute e banco continuam em outro provedor.

## Limitações

Cache, consistência, autenticação, invalidação e observabilidade precisam ser desenhados com cuidado. Código na borda possui limites de runtime, APIs e persistência diferentes de um processo em VM. Um proxy também pode mascarar falhas da origem e dificultar diagnóstico se os logs não forem correlacionados.

Cloudflare não substitui automaticamente cluster, fila, worker, banco relacional ou armazenamento de backup. Avalie egress, lock-in, exportação de dados, regiões efetivas e o comportamento durante indisponibilidade da origem.

## Fontes primárias

- [Cloudflare developer documentation](https://developers.cloudflare.com/)
- [Cloudflare Workers](https://developers.cloudflare.com/workers/)
- [Cloudflare developer platform](https://www.cloudflare.com/developer-platform/products/)
