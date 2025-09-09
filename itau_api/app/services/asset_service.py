from app.models import Asset

def get_all_assets():

    assets = Asset.query.all()
    return assets
    
def new_asset():
    """
        add um asset
    """
    pass