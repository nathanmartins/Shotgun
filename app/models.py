from app import db


class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(64), index=True, unique=True)
    results = db.Column(db.JSON(), index=False, unique=False)
    datetime = db.Column(db.DateTime(), index=False, unique=False)

    def __repr__(self):
        return '<Result {}>'.format(self.filename)
