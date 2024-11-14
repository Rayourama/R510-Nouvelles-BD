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
collection = db["reservations"]  # Remplacez par le nom de votre collection
vols_collection = db["vols"]

def compter_pilotes_dans_reservations():
    pilotes_uniques = set()
    
    # Récupérer toutes les réservations
    reservations = collection.find()
    
    # Parcourir chaque réservation
    for reservation in reservations:
        # Vérifiez que reservation est un dictionnaire
        if isinstance(reservation, dict) and 'vol' in reservation:
            vol_id = reservation['vol']  # ID du vol
            vol_data = vols_collection.find_one({"id": vol_id})  # Récupérer les détails du vol
            
            if vol_data and 'pilote' in vol_data:  # Vérifiez que vol_data est valide
                pilote_id = vol_data['pilote']
                pilotes_uniques.add(pilote_id)  # Ajouter l'ID du pilote au set
        else:
            print(f"Format inattendu pour la réservation : {reservation}")
    
    # Retourner le nombre de pilotes uniques
    return len(pilotes_uniques)

# Appel de la fonction pour compter les pilotes
nombre_de_pilotes = compter_pilotes_dans_reservations()

# Affichage du nombre de pilotes
print("Nombre de pilotes dans la base :", nombre_de_pilotes)