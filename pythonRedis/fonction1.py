import redis
import json

server = redis.Redis(host='localhost', decode_responses=True, port="6379")

def villes_arrivee_reservations():
    # Récupérer toutes les clés des réservations
    keys = server.keys('reservations:*')
    
    villes_arrivee = set()  # Utilisation d'un set pour éviter les doublons
    
    # Parcourir chaque réservation pour extraire la ville d'arrivée
    for i in keys:
        # Récupérer les données de la réservation (au format JSON)
        data = json.loads(server.get(i))
        
        # Extraire la ville d'arrivée du vol associé à la réservation
        ville_arrivee = data['reservations']['vol']['villeArrivee']
        
        # Ajouter la ville d'arrivée au set
        villes_arrivee.add(ville_arrivee)
    
    # Retourner la liste des villes d'arrivée
    return list(villes_arrivee)

villes_arrivee = villes_arrivee_reservations()
server.set('villes_arrivee', json.dumps(villes_arrivee))

print(villes_arrivee)