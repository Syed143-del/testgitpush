import pymongo

client = pymongo.MongoClient("mongodb+srv://Syed:Goodboy143@cluster0.ogg7usb.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d={
    "name" : "sdhanshu",
    "email" : "sudhanshu@ineuron.ai",
    "surname" : "kumar"
}

db1=client["mongotest"]
coll=db1['test']
coll.insert_one(d)