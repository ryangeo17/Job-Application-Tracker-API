from flask import Flask
from app.db import db


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI='sqlite:///jobtracker.db',
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )
    
    # Initialize extensions
    db.init_app(app)
    
    # Import models (needed for db.create_all())
    from app import models
    
    # Register blueprints
    from app.routes import bp
    app.register_blueprint(bp)
    
    # Create database tables
    with app.app_context():
        db.create_all()
    
    return app
