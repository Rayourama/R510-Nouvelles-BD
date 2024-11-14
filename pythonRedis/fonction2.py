import redis
import json

server = redis.Redis(host='localhost', decode_responses=True, port="6379")

def compter_pilotes():
    # Récupérer toutes les clés des réservations
    keys = server.keys('reservations:*')
    
    # Créer un set pour stocker les pilotes uniques
    pilotes = set()
    
    # Parcourir chaque réservation
    for i in keys:
        # Récupérer les données de la réservation (au format JSON)
        reservation_data = json.loads(server.get(i))
        
        # Extraire le pilote de la réservation
        pilote = reservation_data['reservations']['vol']['pilote']
        
        # Ajouter le pilote au set (les doublons seront ignorés automatiquement)
        pilotes.add(pilote['nom'])
    
    # Retourner le nombre de pilotes uniques
    return len(pilotes)

nombre_pilotes = compter_pilotes()
print(nombre_pilotes)

server.set("NB_Pilotes",nombre_pilotes)