from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api()
db = SQLAlchemy()         
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)

class test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    adress = db.Column(db.String, nullable = False)
    state = db.Column(db.String, nullable = False)
    admin = db.Column(db.String, nullable = False)

with app.app_context():
   db.create_all()


class App(Resource):
    def get(self, id):
        #take_obj = db.session.get(id)
        take_obj = db.session.get(test, id)
        print(take_obj.adress, take_obj.state, take_obj.admin)
        print(type(take_obj.adress))
        return {"adress": take_obj.adress, "state": take_obj.state, "admin": take_obj.admin}

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
        new_test = test(adress = params["adress"],
                        state = params["state"],
                        admin = params["admin"])
        db.session.add(new_test)
        db.session.commit()
        return object


api.add_resource(App, "/obj/<int:id>")
api.init_app(app)

    
if __name__ == "__main__":
    app.run(debug=True, port=3000, host='127.0.0.1')







