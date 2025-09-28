from flask import Blueprint, request
from app.services.asset_service import AssetService
from app.utils import Utils

asset_bp = Blueprint('asset', __name__)
asset = AssetService()

@asset_bp.route('/', methods=['GET', 'POST'])
def get_all_assets():
    """
        retornar todos os assets
    """

    if request.method == 'POST':
        asset_info = request.get_json()
        if 'code' not in asset_info:
            return Utils.send_response(status=400, response={}, error='the "asset" field is required in the payload')

        if 'name' not in asset_info:
            return Utils.send_response(status=400, response={}, error='the "name" field is required in the payload')
        
        data = asset.new_asset(request.get_json())
    else:
        data = asset.get_all_assets()
    return data

@asset_bp.route('/<user_id>', methods=['GET'])
def get_user():
    """
        retornar todas a última cotação desse asset
    """
    pass


