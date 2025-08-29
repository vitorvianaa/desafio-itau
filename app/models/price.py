from ..extensions import db

class Price(db.Model):

    __tablename__ = 'price'

    id = db.Column(db.Integer, primary_key=True)


    def __repr__(self):
        return f'price id: {self.id}'