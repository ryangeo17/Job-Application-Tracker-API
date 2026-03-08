from flask import Flask
from app.db import db


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI='sqlite:///jobtracker.db',
        SQLALCHEMY_TRACK_MODIFICATIONS= False,
    )
    db.init_app(app)
    from app import models
    from app import routes

    with app.app_context():
        db.create_all()

    

    return app

app=create_app()

if __name__ == "__main__":
    app.run(debug=True)

