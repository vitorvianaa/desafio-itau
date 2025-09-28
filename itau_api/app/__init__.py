from flask import Flask
from .config import DevConfig
from .extensions import db, migrate
from .routes.asset_router import asset_bp
from .routes.user_router import user_bp
from .routes.price_router import price_bp
from .routes.operation_router import operation_bp

def create_app(config_class = DevConfig):

    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)


    app.register_blueprint(asset_bp, url_prefix='/asset')
    app.register_blueprint(user_bp, url_prefix='/users' )
    app.register_blueprint(price_bp, url_prefix='/prices' )
    app.register_blueprint(operation_bp, url_prefix='/operations')

    return app

from .models import User, Asset, Operation, Position, Price