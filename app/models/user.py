from ..extensions import db

class User(db.Model):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)


    def __repr__(self):
        return f"user_id: {self.id}"