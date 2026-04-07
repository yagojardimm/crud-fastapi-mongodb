import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27018")
client = MongoClient(MONGO_URL)
db = client["gerenciador_tarefas"]
tasks_collection = db["tasks"]