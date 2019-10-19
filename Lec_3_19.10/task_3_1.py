from flask import Flask, jsonify , request
#JSON === JavaScriptObjectNotation 
stores = [
    {
        'name':'EvgenStore',
        'items':[
            {
                'name':'Book',
                'price': 15.99
            }
        ]
    }
]

app = Flask(__name__)
# RES 1 /
# GET / --homepage of stores marketplace
@app.route('/', methods = ['GET'])
def homepage():
    return "<h1> Welcome to our MARKETPLACE!!!</h1>"
# RES 2 /store
# POST /store data:{name:}
@app.route('/store', methods = ['POST'])
def create_store():
    request_data = request.get_json() # {'name':'Store name'}
    new_store = {
        'name': request_data['name'],
        'items':[]
    }
    stores.append(new_store)
    return jsonify(new_store), 200


# GET /store/<string:name>
@app.route('/store/<string:name>', methods = ['GET'])
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store), 200
    return jsonify({'message':'store not found'})


# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods = ['POST'])
def create_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            request_data = request.get_json() # {'name': 'MyItem', 'price':15.92}
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(store), 200
    return jsonify({'message' : 'store not found'})

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item', methods = ['GET'])
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items':store['items']}), 200
    return jsonify({'message':'store not found'})
# RES 3 /stores
# GET /stores
@app.route('/stores', methods = ['GET'])
def get_stores():
    return jsonify({'stores':stores}), 200

app.run(port = 8080, debug = True)