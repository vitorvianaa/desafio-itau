from typing import Dict
from sqlalchemy.exc import IntegrityError
from app.utils import Utils
from app.repository.user_repository import UserRepository 

class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def get_all_users(self):
        
        """
            return all users
        """
        all_users = self.user_repository.get_all()
        if len(all_users) > 0:
            return Utils.send_response(status=200, response=all_users, message='all users found')
        elif len(all_users) < 0:
            return Utils.send_response(status=200, response=all_users, message='no users found')
        return Utils.send_response(status=500, response={}, error='internal error')
            
    def new_user(self, new_user: Dict):
        """
            add new_user
        """
        user = self.user_repository(name=new_user['name'], email=new_user['email'], brokerage=new_user['brokerage'])
        if user:
            return Utils.send_response(status=201, response=user.to_dict(), message='new user was succefully created')
        return Utils.send_response(status=500, response={}, error='internal error')

    