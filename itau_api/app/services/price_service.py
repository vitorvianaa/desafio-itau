from app.models import Price
from ..extensions import db
from sqlalchemy.exc import IntegrityError
from app.utils import Utils 

class PriceService:
    def __init__(self):
        self.__db__ = db
        
    def new_price(self, unit_value: int, asset_id: int):
        """
            add price
        """
        try:
            price = Price(asset_id=asset_id, unit_value=unit_value)
            self.__db__.session.add(price)
            self.__db__.session.commit()
        except IntegrityError as e:
            self.__db__.session.rollback()
            print(e)
            return Utils.send_response(status=409, response={}, error='the price is exist')

        return Utils.send_response(status=201, response=price.to_dict(), message='new price was succefully created')

    def updated_price(self, unit_value: int, price_id: int):
        """
            updated price
        """
        try:
            new_price: Price = Price.query.get(price_id)
            
            if not new_price:
                return Utils.send_response(status=409, response={}, error='the price not exist')
            
            new_price.unit_value = unit_value
           
            self.__db__.session.add(new_price)
            self.__db__.session.commit()
            
            return Utils.send_response(status=200, response=new_price.to_dict(), message='price updated successfully')
        
        except IntegrityError as e:
            self.__db__.session.rollback()
            print(e)
            return Utils.send_response(status=409, response={}, error='the price not exist')
        
    def get_price(self, price_id: int):
        try:
            
            price: Price = Price.query.get(price_id)
            
            if not price:
                return Utils.send_response(status=409, response={}, error='the price not exist')
            
            return Utils.send_response(status=200, response=price.to_dict(), message='price found')
        
        except IntegrityError as e:
            self.__db__.session.rollback()
            print(e)
            return Utils.send_response(status=409, response={}, error='the price not exist')