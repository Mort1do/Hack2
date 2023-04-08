from app import db


class users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String, nullable=False)
    password = db.Column(db.Integer, nullable=False)
    work_group_type = db.Column(db.String, nullable=False)
    objects = db.Column(db.Integer, db.ForeignKey('objects.id'))
    work_group = db.Column(db.Integer, db.ForeignKey('workgroups.id'))

    def __repr__(self):
        return f"<users {self.id}>"