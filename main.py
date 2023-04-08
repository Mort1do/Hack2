import sqlite3

from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
api = Api()
db = SQLAlchemy()         
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///buildings1.3.db"
db.init_app(app)


class Objects(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    county = db.Column(db.String, nullable = False)
    district = db.Column(db.String, nullable = False)
    adress = db.Column(db.String, nullable = False)
    object_type = db.Column(db.String, nullable = False)
    object_condition = db.Column(db.String, nullable = False)
    square = db.Column(db.Integer, nullable = False)
    owner = db.Column(db.String, nullable = False)
    object_user = db.Column(db.String, nullable=False)
    object_photo = db.Column(db.LargeBinary)

    def __repr__(self):
        return f"<objects {self.id}>"


class WorkGroups(db.Model):
    group_id = db.Column(db.Integer, primary_key=True)
    organization_name = db.Column(db.String, nullable=False)
    object_id = db.Column(db.Integer, db.ForeignKey('objects.id'))
    group_type = db.Column(db.String, nullable=False)
    problems = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"<workgroups {self.group_id}>"


class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String, nullable=False)
    password = db.Column(db.Integer, nullable=False)
    work_group_type = db.Column(db.String, nullable=False)
    #objects = db.Column(db.Integer, db.ForeignKey('objects.id'))
    #work_group = db.Column(db.Integer, db.ForeignKey('workgroups.group_id'))

    def __repr__(self):
        return f"<users {self.user_id}>"


class WorkProcess(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    problem_type = db.Column(db.String, nullable=False)
    solution_type = db.Column(db.String, nullable=False)
    date_problem_appear = db.Column(db.DateTime, default=datetime.utcnow, nullable = False)
    solution_term = db.Column(db.Integer, nullable=False)
    solution_date_nominal = db.Column(db.DateTime, default=datetime.utcnow, nullable = False)
    solution_date_fact = db.Column(db.Date, nullable=False)
    object_id = db.Column(db.Integer, db.ForeignKey('objects.id'))
    work_group = db.Column(db.Integer, db.ForeignKey('workgroups.group_id'))
    document = db.Column(db.LargeBinary)


#with app.app_context():
#   db.create_all()


class App(Resource):
    def get(self, id):
        get_user = db.session.get(Users, id)
        get_obj = db.session.get(Objects, get_user.user_id)
        get_wg = db.session.get(WorkGroups, id)
        #get_wp = db.session.get(WorkProcess, id)
        #print(get_user.work_group, type(get_user.work_group))
        #get_wg = db.session.get(WorkGroups, get_user.work_group)
        #print(get_user.objects, type(get_user.objects))
        #get_obj = db.session.get(Objects, get_user.objects)
        ##print(get_user.login, get_user.password)
        ##print(get_obj.name)
        ##print(get_wp.problem_type)
        ##print(get_wg.organization_name)
        #print(get_wg.organization_name)
        print(get_obj.name)
        return {"login": get_user.login, "password": get_user.password} #, {"organization name": get_wg.organization_name}, {"object name": get_obj.name}

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







