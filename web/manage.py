from webapp import app, db
from flask_script import Manager
from flask_migrate import MigrateCommand
from flask_fixtures.loaders import JSONLoader
from flask_fixtures import load_fixtures

manager = Manager(app)
manager.add_command('db', MigrateCommand)


@manager.command
def load_fixture():
    fixtures = JSONLoader().load(app.config.get('FIXTURES_PATH'))
    load_fixtures(db, fixtures)


if __name__ == '__main__':
    manager.run()
