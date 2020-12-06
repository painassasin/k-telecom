import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret'

    # TODO: Нужно поднимать MySQL (в SQLite кажется не работают ForeignKeys)
    SQLALCHEMY_DATABASE_URI = (
            os.environ.get('DATABASE_URI') or
            'sqlite:///' + os.path.join(basedir, 'webapp.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    TESTING = True
