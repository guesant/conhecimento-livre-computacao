# Path-based routing

Path-based routing seleciona backend pelo caminho da requisição HTTP.

É útil para agrupar serviços sob um mesmo host, mas aplicações precisam compreender prefixos, geração de URLs e eventual reescrita de path.

Usá-lo com software que assume execução na raiz pode causar redirects e assets quebrados.