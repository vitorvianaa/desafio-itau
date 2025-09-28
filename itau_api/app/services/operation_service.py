from app.models import Operation
from ..extensions import db
from typing import Dict
from sqlalchemy.exc import IntegrityError
from app.utils import Utils 

class OperationService:
    def __init__(self):
        self.__db__ = db
        
    def new_operation(self, operation_info: Dict):
        """
            add new operation
        """
        try:
            operation = Operation(user_id=operation_info['user_id'], asset_id=operation_info['asset_id'], 
                                  qtd=operation_info['qtd'],unit_value=operation_info['unit_value'], 
                                  operation_type=operation_info['operation_type'], brokerage=operation_info['brokerage'])
            
            self.__db__.session.add(operation)
            self.__db__.session.commit()
        except IntegrityError as e:
            self.__db__.session.rollback()
            print(e)
            return Utils.send_response(status=409, response={}, error='the operation is exist')

        return Utils.send_response(status=201, response=operation.to_dict(), message='new operation was succefully created')


    def get_operation(self, operation_id: int):
        try:
            operation = Operation.query.get(operation_id)

            if not operation:
                return Utils.send_response(status=404, response={}, error='operation id not found')
            
            return Utils.send_response(status=200, response=operation.to_dict(), message='operation found')
        
        except IntegrityError as e:
            print(e)
            return Utils.send_response(status=500, response={}, error='internal error')
        
