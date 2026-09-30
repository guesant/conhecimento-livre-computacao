# Firestore Security Rules

Firestore Security Rules controlam leitura e escrita de documentos e
subcoleções no Firestore. A decisão pode usar request.auth, dados existentes e
o conteúdo que será gravado.

## Cuidados

O desenho precisa acompanhar a forma das queries. Uma query que não consegue
provar a condição da policy deve falhar, e uma regra baseada apenas na UI não
protege o documento.

## Relações

Firestore Rules são autorização de dados, não RBAC genérico. Para relações
complexas, modele claims, documentos de membership ou um serviço de FGA.

## Fonte

- [Cloud Firestore Security Rules](https://firebase.google.com/docs/firestore/security/get-started)
