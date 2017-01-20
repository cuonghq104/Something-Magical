#mongodb://<dbuser>:<dbpassword>@ds027425.mlab.com:27425/techfood
import mongoengine
import json

#mongodb://<dbuser>:<dbpassword>@ds161048.mlab.com:61048/kingcua

#mongodb://<dbuser>:<dbpassword>@ds117869.mlab.com:17869/somethingmagical

host = "ds117869.mlab.com"
port = 17869
db_name = "somethingmagical"
user_name = "linchong"
password = "linchong"

def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
   return [json.loads(item.to_json()) for item in l]

def item2json(item):
   return json.loads(item.to_json())