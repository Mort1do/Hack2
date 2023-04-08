from main import db

class objects(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    country = db.Column(db.String, nullable = False)
    district  = db.Column(db.String, nullable = False)
    address  = db.Column(db.String, nullable = False)
    object_type  = db.Column(db.String, nullable = False)
    object_condition  = db.Column(db.String, nullable = False)
    square  = db.Column(db.Integer, nullable = False)
    owner  = db.Column(db.String, nullable = False)
    object_user = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"<objects {self.id}>"