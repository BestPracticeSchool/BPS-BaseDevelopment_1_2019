from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT , jwt_required
from security import authenticate, identity

app = Flask(__name__)
app.secret_key = "evgen"
api = Api(app)

jwt = JWT(app, authenticate, identity) #/auth

items = [
    {
        "name":"FirstItem",
        "price": 15.99
    }
]


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
            type=float,
            required=True,
            help="This field cannot be left blank!"
    )



    def get(self, name):
        item = next(filter(lambda x : x['name'] == name, items), None)
        if item:
            return item , 200
        return {"message" : "Item not found"}, 404 


    @jwt_required()
    def post(self, name):
        data = Item.parser.parse_args()
        item = {"name" : name, "price" : data['price']}
        items.append(item)
        return item, 201
    
    def put(self, name):
        data = Item.parser.parse_args()
        item = next(filter(lambda x : x['name'] == name, items), None)
        if item:
            item['price'] = data['price']
        else:
            item = {"name": name, "price":data['price']}
            items.append(item)
        return item , 201

    def delete(self, name):
        global items 
        items = list(filter(lambda x: x['name'] != name, items), None)
        if items:
            return {"message" : "Item deleted"} , 200
        else:
            return {"message" : "Item not found"}, 404

class ItemList(Resource):
    def get(self):
        return {"items" : items}, 200


api.add_resource(ItemList, "/items")
api.add_resource(Item, "/item/<string:name>")
app.run(port = 8080, debug = True)