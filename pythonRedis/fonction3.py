import json
import redis
from fonction1 import villes_arrivee_reservations

# Connexion au serveur Redis
server = redis.Redis(host='localhost', decode_responses=True, port=6379)

def get_villeDepart_from_villeArrivee():
    arrival_cities = villes_arrivee_reservations()  # Appel de la fonction importée
    depart_from_arrivee = {}  # Dictionnaire pour stocker les villes de départ pour chaque ville d'arrivée

    # Parcourir chaque ville d'arrivée
    for i in arrival_cities:
        departure_cities = set()  # Utiliser un set pour éviter les doublons
        reservation_keys = server.keys("reservations:*")  # Obtenir toutes les réservations

        # Parcourir chaque réservation pour vérifier les villes de départ associées
        for key in reservation_keys:
            reservation_data = json.loads(server.get(key))  # Charger les données JSON de la réservation
            ville_arrivee = reservation_data["reservations"]["vol"]["villeArrivee"]
            ville_depart = reservation_data["reservations"]["vol"]["villeDepart"]

            # Si la ville d'arrivée correspond, ajouter la ville de départ au set
            if ville_arrivee == i:
                departure_cities.add(ville_depart)

        # Ajouter la liste de villes de départ dans le dictionnaire pour cette ville d'arrivée
        depart_from_arrivee[i] = list(departure_cities)

    return depart_from_arrivee

# Exemple d'utilisation
if __name__ == "__main__":
    depart_from_arrivee = get_villeDepart_from_villeArrivee()
    print(depart_from_arrivee)