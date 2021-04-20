import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()


class Cats(db.Model):
    __tablename__ = 'dogs'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    country = db.Column(db.String(100))
    price = db.Column(db.Integer)