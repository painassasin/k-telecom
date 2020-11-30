from os import getenv


class Config(object):

    CSRF_ENABLED = True
    SECRET_KEY = getenv('SECRET_KEY')

    SQLALCHEMY_DATABASE_URI = (
        f"mysql+mysqlconnector://"
        f"{getenv('MYSQL_USER')}:{getenv('MYSQL_PASSWORD')}@"
        f"{getenv('SQL_HOST')}:{getenv('SQL_PORT')}/"
        f"{getenv('MYSQL_DATABASE')}")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    RE_DICT = {
        'N': '[0-9]',
        'A': '[A-Z]',
        'a': '[a-z]',
        'X': '[A-Z0-9]',
        'Z': '[-_@]'
    }
