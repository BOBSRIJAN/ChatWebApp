from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("MONGOdb")
print(f"API Key: {api_key}")

mongo_client = MongoClient(api_key)
db = mongo_client['massage12']
massage = db['msg']
active_users = db['active_users']
