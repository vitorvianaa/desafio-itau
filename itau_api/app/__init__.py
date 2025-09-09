from flask import Flask
from .config import DevConfig
from .extensions import db, migrate
from .routes.asset_router import asset_bp

def create_app(config_class = DevConfig):

    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)


    app.register_blueprint(asset_bp, url_prefix='/asset')

    return app

from .models import User, Asset, Operation, Position, Price