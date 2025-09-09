from app.extensions import db


class Asset(db.Model):

    __tablename__ = 'asset'

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.Integer, nullable=False, unique=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    
    def __repr__(self):
        return f'asset id: {self.id}'