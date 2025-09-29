from app.models import Operation
from app.extensions import db
from sqlalchemy.exc import SQLAlchemyError
from typing import Union

class OperationRepository:
    def __init__(self):
        self.__db__ = db

    def get_by_id(self, id:int) -> Union[Operation, bool]:
        try:
            operation = Operation.query.get(id)
            if not operation:
                return False
            return operation.to_dict()  
        except SQLAlchemyError as e:
            print(e)
            self.__db__.session.rollback()
            return False

    def get_all(self) -> Union[list[Operation], bool]:
        try:
        
            operations = Operation.query.all()
            all_operations = []
            for i in operations:
                operation_transform = i.to_dict()
                all_operations.append(operation_transform)
            return all_operations        
        
        except SQLAlchemyError as e:
            self.__db__.session.rollback()
            print(f"Error in get_all_operations: {e}")
            return False

    def create(self, user_id: int, asset_id: int, qtd: int, unit_value: int, operation_type: int, brokerage: int) -> Union[Operation, bool]:
        try:
            operation = Operation(user_id=user_id, asset_id=asset_id, qtd=qtd, unit_value=unit_value, operation_type=operation_type, brokerage=brokerage)
            self.__db__.session.add(operation)
            self.__db__.session.commit()
            return operation.to_dict()
        except SQLAlchemyError as e:
            self.__db__.session.rollback()
            print(e)
            return False

    