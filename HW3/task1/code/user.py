import sqlite3
from flask_restful import Resource, reqparse


class User(object):
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password


    @classmethod
    def find_by_username(cls, username):
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()

        query_select = "SELECT * FROM users WHERE username=?"
        cur.execute(query_select, (username,))

        row = cur.fetchone() # None

        if row:
            user = cls(*row)   
        else:
            user = None 
        conn.close()

        return user 

    @classmethod
    def find_by_id(cls, _id):
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()

        query_select = "SELECT * FROM users WHERE id=?"
        cur.execute(query_select, (_id,))

        row = cur.fetchone() # None

        if row:
            user = cls(*row)   
        else:
            user = None 
        conn.close()

        return user 

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )

    def find_by_username(cls, username):
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()

        query_select = "SELECT * FROM users WHERE username=?"
        cur.execute(query_select, (username,))

        row = cur.fetchone() # None

        if row:
            user = User(*row)   
        else:
            user = None 
        conn.close()

        return user 

    def post(self):
        data = UserRegister.parser.parse_args() # {"username": "evgen", "password" : "asdqwe"}
        if self.find_by_username(data['username']) is None:
            conn = sqlite3.connect('data.db')
            cur = conn.cursor()

            query_insert = "INSERT INTO users VALUES(NULL, ?, ?)"
            cur.execute(query_insert, (data['username'], data['password']))

            conn.commit()
            conn.close()

            return {"message" : "User created!"}, 201
        return {"message": "User already exists!"}, 401

