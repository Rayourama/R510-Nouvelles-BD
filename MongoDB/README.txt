/*******************************************************************************
* Utilisation de MongoDB à l'aide de Python                                    *
*                                                                              *
* Bienvenue dans la méthode pour rejouer l'expérience proposée.                *
* Date:    2024-11-14                                                          *
* Auteur:  Ryan RAMASSAMY                                                      *
*******************************************************************************/

Ce document permet de rejouer l'ensemble de l'expérience effectué avec MongoDB afin de déployer 
un environnement fonctionnel.
Afin d'intéragir avec notre serveur MongoDB à l'aide de Python, nous utiliserons le cloud.

#1# Pour commencer, rendez-vous sur MongoDB Atlas, créer vous un compte et connectez-vous.

#2# Vous devez ensuite vous créer une organisation. => Cliquez sur l'icone de votre profil en haut 
à droite de la page ensuite selectionnez la rubrique "Organisations". Cliquez ensuite sur 
"Créer une nouvelle organisation", donnez un nom à votre organisation

#3# Une fois créé, cliquez sur "Nouveau projet". Donnez un nom à voter projet et si vous le souhaitez 
ajoutez des tags. Vous aurez alors la possibilité de créer un cluster, cliquez sur "créer" et 
choisissez le niveau gratuit.

#4# Il vous est alors demandé de créer un utilisateur pour accéder au cluster 
que vous venez de créer. Cliquez sur "Créer utilisateur"(Veillez à bien copier le mot de passe!). Cliquez ensuite sur 
"Choisir une méthode de connexion" puis sur "Drivers" ou "Conducteurs"

#5# Installez les deux bibliothèques suivantes : pip install "pymongo[srv]" python-dotenv (Vous aurez ensuite besoin de python3!)

#6# Récupérez le code situer dans "connexion.py" et veillez à changer la variable "uri" et à la remplacer par le lien fournit.
(Il devrait ressembler à quelque chose comme ça : 
mongodb+srv://<username>:<db_password>@cluster0.108gp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0)
Votre nom d'utilisateur apparaîtra dans le lien. Si le mot de passe ne figure pas déjà dans le lien, alors collez-le à la place de
"<db_password>"

#7# Vous pouvez maintenant exécuter votre script votre à l'aide de la commande suivante : python3 votre_script.py
Vous obtiendrez alors une réponse vous notifiant que la connexion à MongoDB est un succès.

****************************************************************************
*En cas de problèmes, le lien suivant vous mène directement au tutoriel :  * 
* https://github.com/sessaadouni/Tuto_Mongo_Atlas/blob/master/tuto.md      *
****************************************************************************

Maintenant vous pouvez exécutez l'ensemble des scripts python disponible dans ce dossier. 
Voici dans quel ordre les exécuter (pour suivre la logique du rapport) : 

1) script.py
2) get.py
3) fonction1.py
4) fonction2.py
5) fonction3.py
6) time.py

ATTENTION! Chacun de ces scripts contient à nouveau un uri de connexion, veillez à changez le lien actuel par le votre.