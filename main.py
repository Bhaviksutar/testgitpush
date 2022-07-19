import pymongo
import dns

client = pymongo.MongoClient("mongodb+srv://ineuron:bhavik3501@bhavik.uoqsm.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)
d = {
    "name": "bhavik",
    "email":"bhaviksutar352@gmail.com",
    "surname":"sutar"

}
db1 = client['mongotest']
coll= db1['test']
coll.insert_one(d)