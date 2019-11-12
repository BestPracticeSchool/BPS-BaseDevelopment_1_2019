import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import  jwt_required

items = []


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )

    def find_by_name(self, name):
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()

        query_select = "SELECT * FROM items WHERE name=?"
        cur.execute(query_select, (name,))

        row = cur.fetchone() # None

        if row:
            item = Item(*row)   
        else:
            item = None 
        conn.close()

        return item 


    @jwt_required()
    def get(self, name):
        return {'item': next(filter(lambda x: x['name'] == name, items), None)}

    def post(self, name):
        if self.find_by_name(name):
            return {'message': "An item with name '{}' already exists.".format(name)}, 401

        data = Item.parser.parse_args()

        conn = sqlite3.connect('data.db')
        cur = conn.cursor()

        query_insert = "INSERT INTO items VALUES( ?, ?)"
        cur.execute(query_insert, (name, data['price']))

        conn.commit()
        conn.close()
        item = {'name': name, 'price': data['price']}
        return item, 201

        
        

    @jwt_required()
    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item deleted'}

    @jwt_required()
    def put(self, name):
        data = Item.parser.parse_args()
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item

class ItemList(Resource):
    def get(self):
        return {'items': items}