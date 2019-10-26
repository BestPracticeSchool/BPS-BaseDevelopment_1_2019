from flask import Flask 

app = Flask(__name__)

@app.route('/')
def homepage():
    return "<h1>kEKlOL</h1>"

app.run(port = 8080, debug = True)