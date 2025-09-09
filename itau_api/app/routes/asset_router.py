from flask import Blueprint, jsonify, request
from app.services import asset_service

asset_bp = Blueprint('asset', __name__)

@asset_bp.route('/', methods=['GET', 'POST'])
def get_all_assets():
    """
        retornar todos os assets
    """

    if request.method == 'POST':
        data = asset_service.new_asset()
    data = asset_service.get_all_assets()
    return jsonify({"data": data})

@asset_bp.route('/<user_id>', methods=['GET'])
def get_user():
    """
        retornar todas a última cotação desse asset
    """
    pass


