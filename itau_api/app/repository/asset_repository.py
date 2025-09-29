from app.models import Asset
from app.extensions import db
from sqlalchemy.exc import SQLAlchemyError
from typing import Union

class AssetRepository:
    def __init__(self):
        self.__db__ = db

    def get_by_id(self, id:int) -> Union[Asset, bool]:
        try:
            asset = Asset.query.get(id)
            if not asset:
                return False
            return asset.to_dict()  
        except SQLAlchemyError as e:
            print(e)
            self.__db__.session.rollback()
            return False

    def get_all(self) -> Union[list[Asset], bool]:
        try:
        
            assets = Asset.query.all()
            all_assets = []
            for i in assets:
                asset_transform = i.to_dict()
                all_assets.append(asset_transform)
            return all_assets        
        
        except SQLAlchemyError as e:
            self.__db__.session.rollback()
            print(f"Error in get_all_assets: {e}")
            return False

    def create(self, code: int, name: str) -> Union[Asset, bool]:
        try:
            asset = Asset(code=code, name=name)
            self.__db__.session.add(asset)
            self.__db__.session.commit()
            return asset.to_dict()
        except SQLAlchemyError as e:
            self.__db__.session.rollback()
            print(e)
            return False

    