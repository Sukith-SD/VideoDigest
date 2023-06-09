from pymongo import MongoClient

client= MongoClient("mongodb://localhost:27017/") # connect to the database

def initialize_db():
    client["videodigest"]
    if "users" not in client["videodigest"].list_collection_names():
        client["videodigest"]["users"].insert_one({"name": "admin", "password": "admin","data":{"projects":[]}})
    client.close()
    return

def validate_user(username, password):
    users = client["videodigest"]["users"]
    existing_user = users.find_one({"name": username})
    if existing_user is None:
        return False
    if existing_user["password"] == password:
        return True
    return False

def register_user(username,password):
    users = client["videodigest"]["users"]
    if users.find_one({"name": username}) is None:
        users.insert_one({"name": username, "password": password,"data":{"projects":[]}})
        return True 
    return False

def get_data(user):
    users = client["videodigest"]["users"]
    data=users.find_one({"name": user})["data"]
    return data

def add_project(user,project):
    users = client["videodigest"]["users"]
    users.update_one({"name":user},{"$push":{"data.projects":project}})
    return