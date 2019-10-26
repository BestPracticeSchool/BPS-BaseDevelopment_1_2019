from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = []

class Item(Resource):
    def get(self, name):
        for item in items:
            if item["name"] == name:
                return item, 200
        return {"Item": None}, 404


    def post(self, name):
        item = {"name" : name, "price": 12.00}
        items.append(item)
        return item , 201
    

class ItemList(Resource):
    def get(self):
        return {"items" : items}, 200

api.add_resource(Item, '/item/<string:name>') #...../student/Alex
api.add_resource(ItemList, '/items')
app.run(port = 8080, debug = True)