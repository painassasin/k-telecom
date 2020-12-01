from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import DatabaseError

# Создание экземпляра приложения
app = Flask(__name__)
app.config.from_object(Config)

# Инициализация базы данных
db = SQLAlchemy(app)
db.init_app(app)
with app.app_context():
    # Импорт моделей
    from . import models
    db.create_all()

# Импорт вьюх
from . import views
