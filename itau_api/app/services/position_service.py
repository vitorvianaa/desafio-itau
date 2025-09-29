from app.models import Position
from ..extensions import db
from sqlalchemy.exc import IntegrityError
from app.utils import Utils
from user_service import UserService
from asset_service import AssetService 

class PositionService:
    def __init__(self):
        self.__db__ = db
        self.user_service = UserService()
        self.asset_service = AssetService()
        
    def new_position(self, user_id: int, asset_id: int, qtd: int):
        """
            add position
        """
        try:
            # checar se tem um user_id
            #user = self.user_service.
            # checar se tem um asset_id e qual o preço dele
            # calcular preço medo e pl em utils
            position = Position(user_id=asset_id, asset_id=asset_id, qtd=qtd)
            self.__db__.session.add(position)
            self.__db__.session.commit()
        except IntegrityError as e:
            self.__db__.session.rollback()
            print(e)
            return Utils.send_response(status=409, response={}, error='the position is exist')

        return Utils.send_response(status=201, response=position.to_dict(), message='new position was succefully created')

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