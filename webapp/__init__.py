from flask import Flask
from config import DevelopmentConfig, ProductionConfig
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# Создание экземпляра приложения
app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

# # Инициализация расширений
db = SQLAlchemy(app)
db.init_app(app)
with app.app_context():
    # Импорт моделей
    from . import models
    db.create_all()
migrate = Migrate(app, db)

# Импорт вьюх
from . import views
