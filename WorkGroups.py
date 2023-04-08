from main import db

class work_groups(db.Model):
    group_id = db.Column(db.Integer, primary_key=True)
    organization_name = db.Column(db.String, nullable=False)
    object_id = db.Column(db.Integer, db.ForeignKey('objects.id'))
    group_type = db.Column(db.String, nullable=False)
    problems = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"<work_groups {self.group_id}>"