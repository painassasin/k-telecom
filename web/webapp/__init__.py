from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Создание экземпляра приложения
app = Flask(__name__)
app.config.from_object(Config)

# Инициализация расширений
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Импорт вьюх
from . import views
