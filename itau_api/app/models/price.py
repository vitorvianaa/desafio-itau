from app.extensions import db
from datetime import datetime


class Price(db.Model):

    __tablename__ = 'price'

    id = db.Column(db.Integer, primary_key=True)
    asset_id = db.Column(db.Integer, db.ForeignKey('asset.id'))
    unit_value = db.Column(db.Integer, nullable=False, unique=False)
    date = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return f'price id: {self.id}'
    
    def to_dict(self):
        return {
            "id": self.id,
            "asset_id": self.asset_id,
            "unit_value": self.unit_value,
            "date": self.date
        }