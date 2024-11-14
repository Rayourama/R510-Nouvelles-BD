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

# Récupérer tous les documents
documents = collection.find()

for doc in documents:
    print(doc)
