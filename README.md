Mongo db connection steps : 

create a new mongo db account 
create a free cluster

create user

password : upSW3wqwWmJVyT4O
cluster link :https://cloud.mongodb.com/v2/676a637d3ecfaa69716b5faf#/clusters

run this on cmd : >python -m pip install "pymongo[srv]"==3.12

when connecting with mongo db compass
make sure to use 

mongodb+srv://chirantandatascience:<db_password>@cluster0.ilnkn.mongodb.net/

and replace db_password with the password you created in the mongo db account

###################################################
connection code : 

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://chirantandatascience:<db_password>@cluster0.ilnkn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# ###########Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# #########Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

#################################################################################
srv link : mongodb+srv://chirantandatascience:<db_password>@cluster0.ilnkn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
##################################################################################

Copy the connection string, then open MongoDB Compass

mongodb+srv://chirantandatascience:<db_password>@cluster0.ilnkn.mongodb.net/






