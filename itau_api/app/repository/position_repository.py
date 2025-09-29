from app.models import Position
from app.extensions import db
from sqlalchemy.exc import SQLAlchemyError
from typing import Union

class PositionRepository:
    def __init__(self):
        self.__db__ = db

    def get_by_id(self, id:int) -> Union[Position, bool]:
        try:
            postition = Position.query.get(id)
            if not postition:
                return False
            return postition.to_dict()  
        except SQLAlchemyError as e:
            print(e)
            self.__db__.session.rollback()
            return False

    def get_all(self) -> Union[list[Position], bool]:
        try:
        
            positions = Position.query.all()
            all_position = []
            for i in positions:
                position_transform = i.to_dict()
                all_position.append(position_transform)
            return all_position        
        
        except SQLAlchemyError as e:
            self.__db__.session.rollback()
            print(f"Error in get_all_positions: {e}")
            return False

    def create(self, user_id: int, asset_id: int, qtd: int, average_price: int, pl: int) -> Union[Position, bool]:
        try:
            position = Position(user_id=user_id, asset_id=asset_id, qtd=qtd, average_price=average_price, pl=pl)
            self.__db__.session.add(position)
            self.__db__.session.commit()
            return position.to_dict()
        except SQLAlchemyError as e:
            self.__db__.session.rollback()
            print(e)
            return False

    