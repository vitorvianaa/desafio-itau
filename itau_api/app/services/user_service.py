from app.models import User
from ..extensions import db
from typing import Dict
from sqlalchemy.exc import IntegrityError
from app.utils import Utils 

class UserService:
    def __init__(self):
        self.__db__ = db

    def get_all_users(self):
        
        """
            return all users
        """
        try:
        
            users = User.query.all()
            all_users = []
            for i in users:
                user_transform = i.to_dict()
                all_users.append(user_transform)
            return Utils.send_response(status=200, response=all_users, message='all users')
        
        except IntegrityError as e:
            self.__db__.session.rollback()
            print(f"Error in get_all_users: {e}")
            return Utils.send_response(status=500, response={}, message='Internal error')
        
    def new_user(self, new_user: Dict):
        """
            add new_user
        """
        try:
            user = User(name=new_user['name'], email=new_user['email'], brokerage=new_user['brokerage'])
            self.__db__.session.add(user)
            self.__db__.session.commit()
        except IntegrityError as e:
            self.__db__.session.rollback()
            print(e)
            return Utils.send_response(status=409, response={}, error='the user is exist')

        return Utils.send_response(status=201, response=user.to_dict(), message='new user was succefully created')

    def updated_user(self, user_id: int, update_info: dict):

        """
            updated new asset
        """
        try:
            user: User = User.query.get(user_id)
            if not user:
                return Utils.send_response(status=409, response={}, error='the user not exist')
        
            if "name" in update_info:
                user.name = update_info.get('name')
            
            if "email" in update_info:
                user.email= update_info.get('email')

            if "brokerage" in update_info:
                user.brokerage = update_info.get('brokerage')

            self.__db__.session.add(user)
            self.__db__.session.commit()
            
            return Utils.send_response(status=200, response=user.to_dict(), message='user updated successfully')
        
        except IntegrityError as e:
            self.__db__.session.rollback()
            print(e)
            return Utils.send_response(status=409, response={}, error='the user not exist')

    def delete_user(self):
        """
            delete asset (implementantion not necessary now)
        """
        pass
    