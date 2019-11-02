from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identity

app = Flask(__name__)
app.secret_key = "evgen"
api = Api(app)

jwt = JWT(app, authenticate, identity)

items = [
    {
        "name":"MyItem",
        "price":150.99
    }
]

class Items(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
            type=float,
            required=True,
            help="This field cannot be left blank!"
        )


    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x : x['name'] == name, items), None)
        if item:
            return item, 200 
        return {"message":"Item not found"}, 404

    def post(self, name):
        if next(filter(lambda x : x['name'] == name, items), None):
            return {"message" : "This item is already  here"}, 400
        data = Item.parser.parse_args()
        item = {"name":data['name'], "price":data['price']}
        items.append(item)
        return item, 201

    def delete(self, name):
        global items 
        items = list(filter(lambda x: x['name'] != name, items), None)
        return {"message":"Item deleted"}, 200

    def put(self, name):
        data = Item.parser.parse_args()
        #data = request.get_json()
        item = next(filter(lambda x : x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price' :data['price']}
            items.append(item)
            return item, 201
        else:
            item.update(data)
        return item

    
class ItemList(Resource):
    @jwt_required()
    def get(self):
        return {"items" : items} , 200
        
api.add_resource(Items, '/item/<string:name>')
api.add_resource(ItemList, '/items')
app.run(port = 8080, debug = True)