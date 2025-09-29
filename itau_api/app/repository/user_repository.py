from app.models import User
from app.extensions import db
from sqlalchemy.exc import SQLAlchemyError
from typing import Union

class UserRepository:
    def __init__(self):
        self.__db__ = db

    def get_by_id(self, id:int) -> Union[User, bool]:
        try:
            user = User.query.get(id)
            if not user:
                return False
            return user.to_dict()  
        except SQLAlchemyError as e:
            print(e)
            self.__db__.session.rollback()
            return False

    def get_all(self) -> Union[list[User], bool]:
        try:
        
            users = User.query.all()
            all_users = []
            for i in users:
                user_transform = i.to_dict()
                all_users.append(user_transform)
            return all_users        
        
        except SQLAlchemyError as e:
            self.__db__.session.rollback()
            print(f"Error in get_all_users: {e}")
            return False

    def create(self, name: str, email: str, brokerage: int) -> Union[User, bool]:
        try:
            user = User(name=name, email=email, brokerage=brokerage)
            self.__db__.session.add(user)
            self.__db__.session.commit()
            return user.to_dict()
        except SQLAlchemyError as e:
            self.__db__.session.rollback()
            print(e)
            return False

    