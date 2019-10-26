from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = [
    {
        "name":"FirstItem",
        "price": 15.99
    }
]


class Item(Resource):
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item , 200
        return {"message" : "Item not found"}, 404

    def post(self, name):
        item = {"name" : name, "price" : 14.55}
        items.append(item)
        return item, 201
    
    def put(self, name):
        for item in items:
            if item['name'] == name:
                item['price'] *= 10
                return item, 200
        return {"message" : "Item not found"}, 404

    def delete(self, name):
        for item in items:
            if item['name'] == name:
                pass 



class ItemList(Resource):
    def get(self):
        return {"items" : items}, 200


api.add_resource(ItemList, "/items")
api.add_resource(Item, "/item/<string:name>")
app.run(port = 8080, debug = True)
