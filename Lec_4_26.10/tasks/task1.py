from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

#'/student/<name>' ->>>> Hello <name>!
class Student(Resource):
    def get(self, name):
        message = "Hello %s!"%name 
        return {"message" : message}, 200

class Students(Resource):
    def get(self):
        return "0...."

api.add_resource(Student, "/student/<string:name>")
api.add_resource(Students, "/students")
app.run(port = 8080, debug = True)
