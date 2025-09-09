from flask import Blueprint, jsonify, request
from app.services.asset_service import AssetService

asset_bp = Blueprint('asset', __name__)
asset = AssetService()

@asset_bp.route('/', methods=['GET', 'POST'])
def get_all_assets():
    """
        retornar todos os assets
    """

    if request.method == 'POST':
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


