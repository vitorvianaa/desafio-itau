from app.extensions import db

class User(db.Model):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    brokerage = db.Column(db.Integer, nullable=False, unique=False)


    def __repr__(self):
        return f"user_id: {self.id}"