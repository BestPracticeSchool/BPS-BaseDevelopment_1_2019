from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required, current_identity
import create_tables
from security import authenticate, identity
from items import Item, ItemList
from user import UserRegister

app = Flask(__name__)

app.secret_key = 'evgen'
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

app.run(debug=True, port=8080) 
