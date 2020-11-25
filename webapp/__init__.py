from flask import Flask
from config import DevelopmentConfig
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# Создание экземпляра приложения
app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

# Инициализация расширений
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Импорт остального дерьма
from . import views, models
