# Ubiquiti

Ubiquiti mantém linhas diferentes para redes integradas, segurança física e provedores. UniFi concentra gateways, switches, Wi-Fi, câmeras, controle de acesso e integrações com uma experiência de gerenciamento unificada. UISP atende principalmente provedores wireless e redes de acesso, com rádios e equipamentos gerenciados para operações distribuídas. Os dois ecossistemas não devem ser tratados como um único produto.

## Hardware e famílias

| Família | Hardware e função | Ambiente típico |
| --- | --- | --- |
| UniFi Cloud Gateways | Gateways com roteamento, firewall, VPN, segmentação e console de gerenciamento | residência avançada, SMB, escritórios e múltiplos sites |
| UniFi Switching | Switches de acesso, agregação, PoE e uplinks de maior velocidade | LAN, câmeras, VoIP e Wi-Fi |
| UniFi WiFi | Pontos de acesso para uso interno e externo, com gerenciamento centralizado | residência, escritório, hotel, educação e varejo |
| UniFi Protect | Câmeras, gravadores e software de segurança física | videomonitoramento local |
| UniFi Access | Leitores, controladores e dispositivos de porta | controle de acesso físico |
| UISP wireless | Rádio, CPE e enlaces airMAX, airFiber ou famílias relacionadas | WISP e enlaces de longa distância |
| UISP routing e switching | Roteadores e switches para provedores e sites distribuídos | transporte e acesso de ISP |
| EdgeMAX | Linha de roteamento e switching historicamente associada a EdgeRouter e EdgeSwitch | instalações existentes e migrações avaliadas individualmente |

A disponibilidade de produtos e a direção de cada linha mudam. Para uma implantação nova, confirme se o modelo pertence ao ecossistema UniFi, UISP ou a uma linha legada, qual controlador é necessário e qual é a política de firmware e suporte.

## Aplicações

UniFi é usado para gateway, NAT, firewall, VPN, VLAN, Wi-Fi, switches PoE, câmeras, controle de acesso e operação multi-site. A gestão pode usar console local, hospedagem própria, opções de nuvem e integrações, conforme o produto. UISP é voltado a inventário, provisionamento e monitoramento de redes de provedores, incluindo rádios, CPEs, roteadores e switches.

O painel integrado é uma vantagem de operação, mas também cria dependência do modelo de gerenciamento escolhido. Valide o que funciona sem Internet, o que exige console, quais dados ficam na nuvem, como os backups são exportados e como uma configuração pode ser recuperada sem o controlador original.

## Casos de uso

- residência ou homelab com gateway, switches e Wi-Fi integrados;
- pequena empresa com vários sites e operação simplificada;
- hotel, varejo, educação e hospitalidade com SSIDs, VLANs, portal e PoE;
- videomonitoramento local integrado à rede;
- controle de acesso físico associado ao mesmo ambiente operacional;
- WISP com rádios, CPEs e enlaces ponto a ponto ou ponto-multiponto;
- organizações que preferem uma experiência integrada a administrar muitos produtos por CLI independente.

Para ambientes que exigem roteamento dinâmico muito profundo, automação aberta, suporte formal de operadora ou interoperabilidade detalhada com equipamentos de muitos fabricantes, compare Ubiquiti com MikroTik, Cisco, plataformas Linux e appliances dedicados. A simplicidade do ecossistema não elimina a necessidade de avaliar limites de escala, logs e recuperação.

## Suporte e segurança

Ubiquiti fornece documentação, central de ajuda, atualizações, comunidade e suporte conforme o produto e o canal. A organização deve definir quem administra as contas, onde ficam as credenciais, como o acesso remoto é protegido e como a configuração é recuperada quando uma console falha.

Separe redes de administração, usuários, câmeras e IoT. Use MFA na conta de gerenciamento, limite administradores, aplique firmware suportado, restrinja acesso remoto, preserve backups e acompanhe avisos de segurança. Em WISP, trate rádios, CPEs e interfaces de gestão como uma superfície exposta e aplique filtragem no enlace e no equipamento de borda.

## Fontes primárias

- [Ubiquiti](https://www.ui.com/)
- [UniFi support](https://help.ui.com/)
- [UISP](https://isp.ui.com/)
- [Ubiquiti store](https://store.ui.com/)
