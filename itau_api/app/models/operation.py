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
    
    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "asset_id": self.asset_id,
            "qtd": self.qtd,
            "unit_value": self.unit_value,
            "operation_type": self.operation_type,
            "brokerage": self.brokerage,
            "date": self.date
        }