from dotenv import load_dotenv
from os import getenv

load_dotenv('.env')


class BaseConfig(object):

    # Защита против "Cross-site Request Forgery (CSRF)"
    CSRF_ENABLED = True

    # Секретный ключ для подписи данных
    SECRET_KEY = getenv('SECRET_KEY')

    # URI используемая для подключения к базе данных
    SQLALCHEMY_DATABASE_URI = getenv('DB_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


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
