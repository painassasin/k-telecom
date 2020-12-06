import os


class Config(object):

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret'

    # TODO: Нужно поднимать MySQL (в SQLite кажется не работают ForeignKeys)
    SQLALCHEMY_DATABASE_URI = (
            os.environ.get('DATABASE_URI') or
            'mysql+pymysql://web:12345@127.0.0.1/WebApp')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    TESTING = True
