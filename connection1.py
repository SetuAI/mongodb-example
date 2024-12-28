import pymongo
from pymongo import MongoClient
import os
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())


password = os.getenv("mongodb_pwd")

# connection string with password using f string


connection_String = f'mongodb+srv://chirantandatascience:{password}@cluster0.ilnkn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'

client = MongoClient(connection_String)

