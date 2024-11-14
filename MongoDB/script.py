from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
from os import getenv
import json

load_dotenv()
uri = 'mongodb+srv://ryan:GDDnICV36OXxvLO6@cluster0.t1fzs.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'

# Créez un nouveau client et connectez-vous au serveur
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["MongoPython"]  # Remplacez par le nom de votre base de données

# Création des collections
pilotes_collection = db["pilotes"]
clients_collection = db["clients"]
classes_collection = db["classes"]
avions_collection = db["avions"]
vols_collection = db["vols"]
reservations_collection = db["reservations"]

# Traitement du fichier Pilotes.txt
with open("PILOTES.txt", 'r', encoding='utf-8') as piloteFile:
    for line in piloteFile:
        line = line.split('\t')
        pilote_data = {"id": line[0], "nom": line[1], "naissance": line[2], "ville": line[3].rstrip()}
        pilotes_collection.insert_one(pilote_data)

# Traitement du fichier Clients.txt
with open("CLIENTS.txt", 'r', encoding='utf-8') as clientFile:
    for line in clientFile:
        line = line.split('\t')
        client_data = {
            "id": line[0],
            "nom": line[1],
            "numeroRue": line[2],
            "nomRue": line[3],
            "codePostal": line[4],
            "ville": line[5].rstrip()
        }
        clients_collection.insert_one(client_data)

# Traitement du fichier DefClasses.txt
with open('DEFCLASSES.txt', 'r', encoding="utf-8") as classesFile:
    for line in classesFile:
        line = line.split('\t')
        class_data = {"id": line[0], "nom": line[1], "coeffPrix": int(line[2].rstrip())}
        classes_collection.insert_one(class_data)

# Traitement du fichier Avions.txt
with open("AVIONS.txt", 'r', encoding='utf-8') as avionsFile:
    for line in avionsFile:
        line = line.rstrip().split("\t")
        avion_data = {"id": line[0], "nom": line[1], "capacite": line[2], "ville": line[3]}
        avions_collection.insert_one(avion_data)

# Traitement du fichier Vols.txt
with open('VOLS.txt', 'r', encoding="utf-8") as volsFile:
    for line in volsFile:
        line = line.split("\t")
        vol_data = {
            "id": line[0],
            "villeDepart": line[1],
            "villeArrivee": line[2],
            "dateDepart": line[3],
            "heureDepart": line[4],
            "dateArrivee": line[5],
            "heureArrivee": line[6],
            "pilote": line[7].rstrip(),
            "avion": line[8].rstrip()
        }
        vols_collection.insert_one(vol_data)

# Traitement du fichier Reservations.txt
with open("RESERVATIONS.txt", 'r', encoding='utf-8') as reservationFile:
    for line in reservationFile:
        line = line.split('\t')
        reservation_data = {
            "client": line[0],
            "vol": line[1],
            "classe": {"nom": line[2]},  # Vous devrez probablement récupérer le coeffPrix des classes ici
            "places": int(line[3].rstrip())
        }
        reservations_collection.insert_one(reservation_data)

print("Données insérées dans MongoDB avec succès.")