from ..extensions import db

class Position(db.Model):

    __tablename__ = 'position'

    id = db.Column(db.Integer, primary_key=True)


    def __repr__(self):
        return f'position id: {self.id}'