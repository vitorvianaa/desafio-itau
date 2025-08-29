from ..extensions import db


class Operation(db.Model):
    __tablename__ = 'operation'


    id = db.Column(db.Integer, primary_key=True)


    def __repr__(self, value):
        return f'operation id: {self.id}'
    