from app.extensions import db

class Position(db.Model):

    __tablename__ = 'position'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    asset_id = db.Column(db.Integer, db.ForeignKey('asset.id'))
    qtd = db.Column(db.Integer, nullable=False, unique=False)
    average_price = db.Column(db.Numeric, nullable=False, unique=False)
    pl = db.Column(db.Numeric, nullable=False, unique=False)

    def __repr__(self):
        return f'position id: {self.id}'