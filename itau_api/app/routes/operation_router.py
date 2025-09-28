from flask import Blueprint, request
from app.services.operation_service import OperationService
from app.utils import Utils

operation_bp = Blueprint('operation', __name__)
operation = OperationService()

@operation_bp.route('/', methods=['GET'])
def get_operation():

    operation_id = request.args.get('operation_id') 
    if not operation_id:
        return Utils.send_response(status=400, response={}, error='the params "operation_id" is required')
    data = operation.get_operation(operation_id=operation_id)
    return data

@operation_bp.route('/', methods=['POST'])
def create_operation():
    
    operation_info = request.get_json()
    if 'user_id' not in operation_info:
        return Utils.send_response(status=400, response={}, error='the "user_id" field is required in the payload')

    if 'asset_id' not in operation_info:
        return Utils.send_response(status=400, response={}, error='the "asset_id" field is required in the payload')
    
    if 'qtd' not in operation_info:
        return Utils.send_response(status=400, response={}, error='the "qtd" field is required in the payload')
    
    if 'unit_value' not in operation_info:
        return Utils.send_response(status=400, response={}, error='the "unit_value" field is required in the payload')
    
    if 'operation_type' not in operation_info:
        return Utils.send_response(status=400, response={}, error='the "operation_type" field is required in the payload')
    
    if 'brokerage' not in operation_info:
        return Utils.send_response(status=400, response={}, error='the "brokerage" field is required in the payload')
    
    
    
    data = operation.new_operation(operation_info=operation_info)
   
    return data




