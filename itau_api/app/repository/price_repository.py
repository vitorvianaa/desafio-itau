from app.models import Price
from app.extensions import db
from sqlalchemy.exc import SQLAlchemyError
from typing import Union

class PriceRepository:
    def __init__(self):
        self.__db__ = db

    def get_by_id(self, id:int) -> Union[Price, bool]:
        try:
            price = Price.query.get(id)
            if not price:
                return False
            return price.to_dict()  
        except SQLAlchemyError as e:
            print(e)
            self.__db__.session.rollback()
            return False

    def get_all(self) -> Union[list[Price], bool]:
        try:
        
            prices = Price.query.all()
            all_prices = []
            for i in prices:
                price_transform = i.to_dict()
                all_prices.append(price_transform)
            return all_prices        
        
        except SQLAlchemyError as e:
            self.__db__.session.rollback()
            print(f"Error in get_all_prices: {e}")
            return False

    def create(self, asset_id: int, unit_value: int) -> Union[Price, bool]:
        try:
            price = Price(asset_id=asset_id, unit_value=unit_value)
            self.__db__.session.add(price)
            self.__db__.session.commit()
            return price.to_dict()
        except SQLAlchemyError as e:
            self.__db__.session.rollback()
            print(e)
            return False

    