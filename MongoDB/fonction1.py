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
collection = db["reservations"]
vols_collection = db["vols"]

def villes_arrivee_reservations():
    # Récupérer toutes les réservations
    reservations = collection.find()
    
    villes_arrivee = set()  # Utilisation d'un set pour éviter les doublons
    
    # Parcourir chaque réservation pour extraire la ville d'arrivée
    for reservation in reservations:
        vol_id = reservation['vol']  # Obtenez l'ID du vol
        vol_data = vols_collection.find_one({"id": vol_id})  # Récupérer les détails du vol
        
        if vol_data and 'villeArrivee' in vol_data:  # Vérifiez que vol_data est valide
            ville_arrivee = vol_data['villeArrivee']
            villes_arrivee.add(ville_arrivee)  # Ajouter la ville d'arrivée au set
    
    # Retourner la liste des villes d'arrivée
    return list(villes_arrivee)

# Appel de la fonction pour obtenir les villes d'arrivée
villes_arrivee = villes_arrivee_reservations()

# Affichage des villes d'arrivée
print("Villes d'arrivée :", villes_arrivee)


