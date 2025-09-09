from app.extensions import db
from datetime import datetime


class Operation(db.Model):
    __tablename__ = 'operation'


    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    asset_id = db.Column(db.Integer, db.ForeignKey('asset.id'))
    qtd = db.Column(db.Integer, nullable=False, unique=False)
    unit_value = db.Column(db.Integer, nullable=False, unique=False)
    operation_type = db.Column(db.String(100), nullable=False, unique=False)
    brokerage = db.Column(db.Integer, nullable=False, unique=False)
    date = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return f'operation id: {self.id}'
    