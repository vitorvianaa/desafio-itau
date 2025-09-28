from flask import Blueprint, request
from app.services.user_service import UserService
from app.utils import Utils

user_bp = Blueprint('user', __name__)
user = UserService()

@user_bp.route('/', methods=['GET'])
def get_all_user():
    """
        retornar todas a última cotação desse asset
    """
    data = user.get_all_users()
    return data

@user_bp.route('/', methods=['POST'])
def create_user():
    
    user_info = request.get_json()
    if 'name' not in user_info:
        return Utils.send_response(status=400, response={}, error='the "asset" field is required in the payload')

    if 'email' not in user_info:
        return Utils.send_response(status=400, response={}, error='the "email" field is required in the payload')
    
    if 'brokerage' not in user_info:
        return Utils.send_response(status=400, response={}, error='the "brokerage" field is required in the payload')
    
    data = user.new_user(user_info)
   
    return data

@user_bp.route('/update-user/<int:user_id>/', methods=['PUT', 'PATCH'])
def update_user(user_id):

    data = user.updated_user(user_id=user_id, update_info=request.get_json())

    return data



