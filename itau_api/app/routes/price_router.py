from flask import Blueprint, request
from app.services.price_service import PriceService
from app.utils import Utils

price_bp = Blueprint('price', __name__)
price = PriceService()

@price_bp.route('/', methods=['GET'])
def get_price():

    price_id = request.args.get('price_id') 
    if not price_id:
        return Utils.send_response(status=400, response={}, error='the params "price_id" is required')
    data = price.get_price(price_id=price_id)
    return data

@price_bp.route('/', methods=['POST'])
def create_price():
    
    price_info = request.get_json()
    if 'asset_id' not in price_info:
        return Utils.send_response(status=400, response={}, error='the "asset_id" field is required in the payload')

    if 'unit_value' not in price_info:
        return Utils.send_response(status=400, response={}, error='the "unit_value" field is required in the payload')
    
    
    data = price.new_price(unit_value=price_info['unit_value'], asset_id=price_info['asset_id'])
   
    return data

@price_bp.route('/update-price/<int:price_id>/', methods=['PUT', 'PATCH'])
def update_price(price_id):

    price_info = request.get_json()
    
    if 'unit_value' not in price_info:
        return Utils.send_response(status=400, response={}, error='the "unit_value" field is required in the payload')
    
    data = price.updated_price(unit_value=price_info['unit_value'], price_id=price_id)

    return data



