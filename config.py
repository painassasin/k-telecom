from dotenv import load_dotenv
from os import getenv

load_dotenv('.env')


class BaseConfig(object):

    # Защита против "Cross-site Request Forgery (CSRF)"
    CSRF_ENABLED = True

    # Секретный ключ для подписи данных
    SECRET_KEY = getenv('SECRET_KEY')

    # URI используемая для подключения к базе данных
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+mysqlconnector://"
        f"{getenv('DB_USER')}:"
        f"{getenv('DB_PASSWORD')}@"
        f"{getenv('DB_HOST')}/"
        f"{getenv('DATABASE')}"
        )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Словарь соответсвия маски с регулярным выражением
    RE_DICT = {
        'N': '[0-9]',
        'A': '[A-Z]',
        'a': '[a-z]',
        'X': '[A-Z0-9]',
        'Z': '[-_@]'
    }


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
