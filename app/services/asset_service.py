from app.models import Asset

def get_all_assets():

    assets = Asset.query.all()
    return assets
    
