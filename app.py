from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api()
db = SQLAlchemy()         
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)

#engine = db.create_engine('sqlite:///project.db')
#connection = engine.connect()
#metadata = db.MetaData()

#data = {1: {"name": "house1", "problems": "some_problem1"},
#        2: {"name": "house2", "videos": "some_problem2"}}

class test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    adress = db.Column(db.String, nullable = False)
    state = db.Column(db.String, nullable = False)
    admin = db.Column(db.String, nullable = False)

with app.app_context():
   db.create_all()

#metadata.create_all(engine)
object = {1:{"adress": "golubinskaya", "state": "good", "admin":"gilishnik"},
          2:{"adress": "golubinskaya22", "state": "good222", "admin":"gilishnik321312"},
          3:{"adress": "golubinskaya33", "state": "good31231", "admin":"gilishnik33333"}}

class App(Resource):
    def get(self, id):
        if id == 0:
            return object
        else:
            return object[id]

    def delete(self, id):
        del object[id]
        return object

    def post(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("adress", type=str)
        parser.add_argument("state", type=str)
        parser.add_argument("admin", type=str)
        params = parser.parse_args()
        object[id] = params
        test.adress = params["adress"]
        test.state = params["state"]
        test.admin = params["admin"]
        db.session.commit()
        return object




api.add_resource(App, "/obj/<int:id>")
api.init_app(app)

#@app.route("/")
#def hello():
#    return "Hello, World!"


    
if __name__ == "__main__":
    app.run(debug=True, port=3000, host='127.0.0.1')







