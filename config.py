from dotenv import load_dotenv
from os import getenv
import json

load_dotenv('.env')


class BaseConfig(object):

    # Защита против "Cross-site Request Forgery (CSRF)"
    CSRF_ENABLED = True

    # Секретный ключ для подписи данных
    SECRET_KEY = getenv('SECRET_KEY')

    # URI используемая для подключения к базе данных
    SQLALCHEMY_DATABASE_URI = getenv('DB_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Словарь соответсвия маски с регулярным выражением
    RE_DICT = json.loads(getenv('RE_DICT'))


class DevelopmentConfig(BaseConfig):
    # Режим отладки
    DEBUG = True

    # Среда разработки
    ENV = 'development'


class ProductionConfig(BaseConfig):
    # Режим отладки
    DEBUG = False

    # Среда разработки
    ENV = 'production'
