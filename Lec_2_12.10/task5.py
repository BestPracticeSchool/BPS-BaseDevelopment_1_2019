from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    return """
        <h1>Hello WEB!</h1>
        <p> This is my first web site!</p>
        <p> It's only get request!</p>
        """

app.run(port = 8080, debug = True)