import pymongo
from pymongo import MongoClient
from Listfile import CommonList

# from s1 import Ui_Form

# if __name__ == "__main__":
# try:
#     def addItem():
#         print("Welcome to pymongo")
#         client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
#         print("Connection Successful")
#         db = client['new']
#         collections = db['newDb']
#
#         for item in CommonList.reqData:
#             print(item)
#             for it in item:
#                 collections.insert_one({'name': item["name"], 'code': item["code"]})
#
#
#     addItem()
#
# except Exception as e:
#     print("Error: database service are down")
#


try:
    def addItem():
        print("Welcome to pymongo")
        client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
        print("Connection Successful")
        db = client['pymongoDatabase']
        collections = db['pymongoNew']

        for item in CommonList.reqData:
            print(item)
            for it in item:
                collections.insert_one({'name': item["name"], 'code': item["code"]})


    addItem()
except:
    print("Error: database service are down")

# collections.insert_one({'name': self.name.text(), 'code': self.passcode.text()})

# dictionary = {'name': 'ankita', 'age': '21', 'company': 'cars24'}
# collections.insert_one(dictionary)
# for item in CommonList.reqData:
#     print(item)
#     for it in item:
#         collections.insert_one({'name': self.name.text(), 'code': self.passcode.text()})

# insertThese = [
#     {'name': item["self.name.text()"]}, {'code': item["self.passcode.text()"]}]

# collections.insert_one({'name': self.name.text(), 'code': self.passcode.text()})
