from app.models import Asset
from ..extensions import db
from typing import Dict
from flask import jsonify
from sqlalchemy.exc import IntegrityError
from app.utils import Utils 

class AssetService:
    def __init__(self):
        self.__db__ = db

    def get_all_assets(self):
        
        """
            return all assets
        """
        try:
            assets = Asset.query.all()
            all_assets = []
            for i in assets:
                asset_transform = i.to_dict()
                all_assets.append(asset_transform)
            return Utils.send_response(status=200, response=all_assets, message='all assets')
        except IntegrityError as e:
            print(f"Error in get_all_assest: {e}")
            return Utils.send_response(status=500, response={}, message='Internal error')
        
    def new_asset(self, new_asset: Dict):
        """
            add new asset
        """
        try:
            new_asset = Asset(code=new_asset['code'], name=new_asset['name'])
            self.__db__.session.add(new_asset)
            self.__db__.session.commit()
        except IntegrityError as e:
            print(e)
            return Utils.send_response(status=409, response={}, error='the asset is exist')

        return Utils.send_response(status=201, response=new_asset.to_dict(), message='new asset was succefully created')

    def updated_asset(self, asset_id: int):

        """
            updated new asset (implementantion not necessary now)
        """
        pass

    def delete_asset(self):
        """
            delete asset (implementantion not necessary now)
        """
        pass
    