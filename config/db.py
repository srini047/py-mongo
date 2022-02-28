import os
# from decouple import config
from pymongo import MongoClient

DB_URL = os.getenv("DB_URL")

client = MongoClient(DB_URL)
db = client['db']
