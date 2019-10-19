from flask import Flask, jsonify, request 

app = Flask(__name__)

stores = [
    {
        'name':'EvgenStore',
        'items':[
            {
                'item':'ItemOne',
                'price':15.50
            }
        ]
    }
]

@app.route("/")
def homepage():
    return "<h1>This is myy homepage!</h1>"

@app.route('/store', methods = ['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store), 200

@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store), 200
    return jsonify({"ERROR":"STORE NOT FOUND"})


@app.route('/stores', methods = ['GET'])
def get_stores():
    return jsonify({'stores' : stores}), 200

@app.route('/store/<string:name>/item', methods = ['POST'])
def create_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            request_data = request.get_json()
            new_item = {
                'name':request_data['name'],
                'price':request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item), 200
    return {'message':'store not found'}

@app.route('/store/<string:name>/item', methods = ['GET'])
def get_item_from_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items':store['items']}), 200
    return jsonify({'message':'Items not found'})



app.run(port = 8080, debug = True)