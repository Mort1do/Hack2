from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy
from Users import users
from WorkGroups import work_groups
from WorkProcess import workprocess
from Objects import objects

app = Flask(__name__)
api = Api()
db = SQLAlchemy()         
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///buildings.db"
db.init_app(app)

#class test(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    adress = db.Column(db.String, nullable = False)
#    state = db.Column(db.String, nullable = False)
#    admin = db.Column(db.String, nullable = False)

with app.app_context():
   db.create_all()


class App(Resource):
    def get(self, id):
        user = users()
        take_obj = db.session.get(user, id)
        print(take_obj.login, take_obj.password)
        print(type(take_obj.adress))
        return {"login": take_obj.login, "password": take_obj.password}

    def delete(self, id):
        del object[id]
        return object

    #def post(self, id):
    #    parser = reqparse.RequestParser()
    #    parser.add_argument("adress", type=str)
    #    parser.add_argument("state", type=str)
    #    parser.add_argument("admin", type=str)
    #    params = parser.parse_args()
    #    new_test = test(adress = params["adress"],
    #                    state = params["state"],
    #                    admin = params["admin"])
    #    db.session.add(new_test)
    #    db.session.commit()
    #    return 200


api.add_resource(App, "/obj/<int:id>")
api.init_app(app)

    
if __name__ == "__main__":
    app.run(debug=True, port=3000, host='127.0.0.1')







