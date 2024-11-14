from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
from os import getenv
import json
from fonction1 import villes_arrivee_reservations

load_dotenv()
uri = 'mongodb+srv://ryan:GDDnICV36OXxvLO6@cluster0.t1fzs.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'

client = MongoClient(uri,server_api=ServerApi('1'))
db = client["MongoPython"]

def get_villeDepart_from_villeArrivee():
    
    # Appel de la fonction pour obtenir la liste des villes d'arrivée
    arrival_cities = villes_arrivee_reservations()
    
    # Dictionnaire pour stocker les villes de départ par ville d'arrivée
    depart_from_arrivee = {}
    
    # Parcourir chaque ville d'arrivée
    for i in arrival_cities:
        # Trouver tous les vols qui arrivent à cette ville
        vols = db["vols"].find({"villeArrivee": i})
        
        # Ensemble pour stocker les villes de départ uniques
        departure_cities = set()
        
        # Parcourir les vols et extraire les villes de départ
        for vol in vols:
            if "villeDepart" in vol:  # Vérifier que la ville de départ existe
                departure_cities.add(vol["villeDepart"])
        
        # Ajouter la liste des villes de départ à la clé correspondant à la ville d'arrivée
        depart_from_arrivee[i] = list(departure_cities)
    
    return depart_from_arrivee

if __name__ == "__main__":
    result = get_villeDepart_from_villeArrivee()
    for arrival, departures in result.items():
        print("Villes de départ pour la ville d'arrivée ", arrival, " : ", departures)