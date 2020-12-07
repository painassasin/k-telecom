import os


class Config(object):

    SECRET_KEY = os.environ.get('SECRET_KEY')

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    RE_DICT = {
        'N': '[0-9]',
        'A': '[A-Z]',
        'a': '[a-z]',
        'X': '[A-Z0-9]',
        'Z': '[-_@]'
    }


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
