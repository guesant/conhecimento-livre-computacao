# rclone

rclone copia e sincroniza dados entre muitos backends, incluindo object storage e serviços cloud.

É apropriado quando o destino não é simplesmente outro filesystem acessível por SSH.

O comando sync é destrutivo no destino quando necessário para espelhar origem; valide direção. bisync resolve um problema diferente, com estado e conflitos de sincronização bidirecional.