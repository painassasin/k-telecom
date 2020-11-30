from os import getenv
from dotenv import load_dotenv

load_dotenv('.env')


class Config(object):

    CSRF_ENABLED = True

    DEBUG = True

    FLASK_APP = "manage.py"

    FIXTURES_PATH = 'fixtures.json'

    SECRET_KEY = getenv('SECRET_KEY')

    DB_USER = getenv('DB_USER')
    DB_PASSWORD = getenv('DB_PASSWORD')
    DATABASE = getenv('DATABASE')

    SQLALCHEMY_DATABASE_URI = (
        f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@db/{DATABASE}")

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    RE_DICT = {
        'N': '[0-9]',
        'A': '[A-Z]',
        'a': '[a-z]',
        'X': '[A-Z0-9]',
        'Z': '[-_@]'
    }
