from flask import Blueprint, jsonify

asset_bp = Blueprint('asset', __name__)

@asset_bp.route('/', methods=['GET'])
def get_all_assets():
    """
        retornar todos os assets
    """
    pass

@asset_bp.route('/<user_id>', methods=['GET'])
def get_user():
    """
        retornar todas a última cotação desse asset
    """
    pass


