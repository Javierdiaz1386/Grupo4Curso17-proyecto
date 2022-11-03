import pymongo
import certifi


ca = certifi.where()
client = pymongo.MongoClient(
    "mongodb+srv://teamJavi:MisionTIC_2022@registraduriac17g4.5e5fdau.mongodb.net/"
    "registraduria_db?retryWrites=true&w=majority",
    tlsCAFile=ca
)

db = client.test
print(db)

data_base = client['registraduria_db']
print(data_base.list_collection_names())

collection = data_base.get_collection('candidato')
print(collection.find())
