from main import db
from datetime import date


class workprocess(db.Model):
    object_id = db.Column(db.Integer, db.ForeignKey('objects.id'))
    problem_type = db.Column(db.String, nullable = False)
    soultion_type = db.Column(db.String, nullable = False)
    date_problem_appear = db.Column(db.Date, default=date.utcnow, nullable = False)
    solution_term = db.Colimn(db.Integer, nullable = False)
    solution_date_nominal = db.Column(db.Date, default=date.utcnow, nullable = False)
    solution_date_fact = db.Colimn(db.Date, nullable=False)
    work_group = db.Column(db.Integer, db.ForeignKey('workgroups.id'))