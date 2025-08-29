from ..extensions import db


class Asset(db.Model):

    __tablename__ = 'asset'

    id = db.Column(db.Integer, primary_key=True)


    def __repr__(self):
        return f'asset id: {self.id}'