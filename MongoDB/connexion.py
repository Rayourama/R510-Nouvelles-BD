from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
from os import getenv
import json

load_dotenv()
#Veillez à changer cette variable
uri = 'mongodb+srv://ryan:GDDnICV36OXxvLO6@cluster0.t1fzs.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'

# Créez un nouveau client et connectez-vous au serveur
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["MongoPython"]  # Remplacez par le nom de votre base de données

# Envoyez un ping pour confirmer une connexion réussie
try:
    db.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)