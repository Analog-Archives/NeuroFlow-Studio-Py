from tinydb import TinyDB, Query


db = TinyDB('data_layer.json')
data = db.all()[0]['data'] 
print(data)