from flask import Flask

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

@app.run("/")
def homepage():
    return "<h1>This is myy homepage!</h1>"

@app.route('/store', methods = ['POST'])
def create_store():
    pass

@app.route('/store/<string:name>')
def get_store(name):
    pass 

@app.route('/stores', methods = ['GET'])
def get_stores():
    pass 

@app.route('/store/<string:name>/item', methods = ['POST'])
def create_item_in_store(name):
    pass 

@app.route('/store/<string:name>/item', methods = ['GET'])
def get_item_from_store(name):
    pass



app.run(port = 8080, debug = True)