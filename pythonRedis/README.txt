/*******************************************************************************
* Redis pour Python                                                            *
*                                                                              *
* Bienvenue dans la méthode pour rejouer l'expérience proposée.                *
* Date:    2024-11-14                                                          *
* Auteur:  Ryan RAMASSAMY                                                      *
*******************************************************************************/

Ce document permet de rejouer l'ensemble de l'expérience effectué avec Redis afin de manipuler au mieux les données.

Rendez-vous à cette adresse pour l'installation et la configuration de Redis sur votre machine Linux.
https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/install-redis-from-source/

Effectuer cette série de commande : 
- wget https://download.redis.io/redis-stable.tar.gz
- tar -xzvf redis-stable.tar.gz

/*********************************
*(Ces commandes sont facultatives)*
*- cd redis-stable                *
*- make                           *
*- make BUILD_TLS=yes             *
*- sudo make install              *
**********************************/

Après avoir décompresser l'archive, vous obtenez alors un dossier redis-stable. Déplacez-vous dans ce dossier.
- cd redis-stable

Et lancez la commande suivante afin de lancer votre server Redis.
- src/redis-server
Vous obtiendrez alors un aperçu ainsi qu'une réponse vous montrant que votre serveur est bien lancé.

Une fois ceci fait, ouvrez un nouveau terminal et lancez la commande suivante pour lancer la base de données.
- src/redis-cli
Vous verrez alors que la base se lance en local. Vous pouvez tapez "PING" afin de vérifier que la base répond correctement.
Elle devrait vous répondre "PONG"

Afin d'utiliser python, commencez par ouvrir un nouveau terminal et installez la bibliothèque suivante.
- pip install redis

Une fois ceci fait, il ne vous reste plus qu'à exécuter l'ensemble des scripts python qui se trouve dans l'archive en respectant cette syntaxe.
- python3 script.py