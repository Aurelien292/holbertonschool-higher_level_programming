![alt text](HTTPS.jpeg)


# Guide sur HTTP, HTTPS et Méthodes HTTP
## Introduction
Ce projet explore les concepts clés du protocole HTTP et de sa version sécurisée, HTTPS. Il couvre les différences fondamentales entre HTTP et HTTPS, en mettant l'accent sur les aspects de sécurité, ainsi que sur la structure des requêtes et des réponses HTTP. Vous y trouverez également un aperçu des méthodes HTTP courantes (GET, POST, PUT, DELETE) et des codes de statut associés . L'objectif de ce projet est de fournir une meilleure compréhension de la communication client-serveur via HTTP/HTTPS, et de démontrer comment interagir efficacement avec ces protocoles dans le développement d'applications web.

## Différenciation HTTP et HTTPS:

__HTTP :__ (HyperText Transfer Protocol) : C’est un protocole de communication utilisé pour échanger des informations sur le web. Cependant, HTTP n'est pas sécurisé, ce qui signifie que les données envoyées entre le navigateur et le serveur peuvent être interceptées et lues par des personnes malveillantes.

__HTTPS :__ (HyperText Transfer Protocol Secure) : C'est la version sécurisée de HTTP. HTTPS ajoute un niveau de sécurité en chiffrant les données avec un certificat SSL/TLS. Cela permet de protéger les informations échangées, en assurant leur confidentialité et leur intégrité. HTTPS est particulièrement important pour les sites qui traitent des données sensibles, comme les informations bancaires ou les mots de passe.

## Comprendre la structure HTTP:

Visitez un simple site web, faites un clic droit et choisissez « inspecter » ou « Élément d'inspection ». Naviguez jusqu'à l'onglet « Réseau ». Cela montre toutes les demandes de réseau faites par la page.
Rechargez la page et observez la première demande. Cliquez dessus. Explorer la section « En-tête » pour comprendre la structure des demandes et des réponses HTTP. Vous verrez des méthodes, des chemins, des codes d'état, des en-têtes, et plus encore.

### Exemple et explication : 

#### Dans cet exemple, un navigateur a effectué une requête GET vers https://intranet.hbtn.io/projects/2123

__Type de demande sur la page :__ GET est la méthode HTTP utilisée pour demander une ressource à un serveur

__État 200 :__ Cela signifie que la requête a été réussie.

__Version HTTP/2 :__ Cela indique que le serveur a répondu en utilisant HTTP/2, une version améliorée du protocole HTTP. HTTP/2 améliore la vitesse de transfert en permettant des connexions multiplexées (envoie plusieurs requêtes en même temps)

__Transfert 17,01 Ko (taille 118,72 Ko) :__ Cela indique la quantité de données qui ont été transférées
