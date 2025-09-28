from app.models import Asset
from ..extensions import db
from typing import Dict
from app.utils import Utils
from sqlalchemy.exc import IntegrityError 

class AssetService:
    def __init__(self):
        self.__db__ = db

    def get_all_assets(self):
        
        """
            return all assets
        """

        assets = Asset.query.all()
        return assets
        
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

        return Utils.send_response(status=201, response=new_asset.to_dict(), message='new asset was succefully created.')

    def updated_asset(self):

        """
            updated new asset
        """
        pass

    def delete_asset(self):
        """
            delete asset
        """
        pass


    