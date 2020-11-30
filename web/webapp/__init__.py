from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy


# Создание экземпляра приложения
app = Flask(__name__)
app.config.from_object(Config)

# Инициализация базы данных
db = SQLAlchemy(app)

# Импорт вьюх
from . import views
