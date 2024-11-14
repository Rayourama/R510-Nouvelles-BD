import redis
import json

server = redis.Redis(host='localhost', decode_responses=True, port="6379")

#Traitement du fichier Pilotes.txt
piloteFile = open("PILOTES.txt", 'r', encoding='utf-8')
pilotes = {}

for line in piloteFile:
    line = line.split('\t')
    pilotes[line[0]] = {"nom": line[1], "naissance": line[2], "ville": line[3].rstrip()}

#Traitement du fichier Clients.txt
clientFile = open("CLIENTS.txt", 'r', encoding='utf-8')
clients = {}

for line in clientFile:
    line = line.split('\t')
    clients[line[0]] = {"nom": line[1], "numeroRue": line[2], "nomRue": line[3], "codePostal": line[4], "ville": line[5].rstrip()}

#Traitement du fichier DefClasses.txt
classesFile = open('DEFCLASSES.txt', 'r', encoding="utf-8")
classes = {}

for line in classesFile:
    line = line.split('\t')
    if line[0] not in classes:
        classes[line[0]] = {line[1]: int(line[2].rstrip())}
    else:
        classes[line[0]][line[1]] = int(line[2].rstrip())

#Traitement du fichier Avions.txt
avionsFile = open("AVIONS.txt", 'r', encoding='utf-8')
avions = {}

for line in avionsFile:
    line = line.rstrip().split("\t")
    avions[line[0]] = {"nom": line[1], "capacite": line[2], "ville": line[3]}

#Traitement du fichier Vols.txt
volsFile = open('VOLS.txt', 'r', encoding="utf-8")
vols = {}

for line in volsFile:
    line = line.split("\t")
    vols[line[0]] = {"villeDepart": line[1], "villeArrivee": line[2], "dateDepart": line[3], "heureDepart": line[4], "dateArrivee": line[5], 
                     "heureArrivee": line[6], "pilote": pilotes[line[7]], "avion": avions[line[8].rstrip()]}

#Traitement du fichier Reservations.txt
reservationFile = open("RESERVATIONS.txt", 'r', encoding='utf-8')
reservations = []

for line in reservationFile:
    line = line.split('\t')
    reservations.append({"client": clients[line[0]], "vol": vols[line[1]], "classe": {"nom": line[2], "coeffPrix": classes[line[1]][line[2]]}, 
                         "places": int(line[3].rstrip())})

#Ajout des données dans la base
for i in range(len(reservations)):
    server.set(f"reservations:{i+1}", json.dumps({"reservations": reservations[i]}))
