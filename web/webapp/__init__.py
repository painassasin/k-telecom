from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


# Application factory function
def create_app(class_config):

    app = Flask(__name__)
    app.config.from_object(class_config)

    db.init_app(app)
    migrate.init_app(app, db)

    from webapp import main
    main.register_blueprint(app)

    return app
