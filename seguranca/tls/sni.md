# Server Name Indication

Server Name Indication, SNI, permite que o cliente informe o nome do servidor desejado durante a negociação TLS.

Isso permite hospedar múltiplos nomes no mesmo endpoint e selecionar configuração/certificado apropriado.

SNI pode ser usado por proxies para decidir encaminhamento mesmo em desenhos de [TLS passthrough](passthrough.md).