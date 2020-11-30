from flask.cli import FlaskGroup
from webapp import app, db
from webapp.models import EquipmentTypes

cli = FlaskGroup(app)


@cli.command('create_tables')
def create_tables():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command('create_seed')
def create_seed():

    db.session.add_all([
        EquipmentTypes(type_name='TP-Link TL-WR74', sn_mask='XXAAAAAXAA'),
        EquipmentTypes(type_name='D-Link DIR-300', sn_mask='NXXAAXZXaa'),
        EquipmentTypes(type_name='D-Link DIR-300 S', sn_mask='NXXAAXZXXX')
    ])
    db.session.commit()


if __name__ == '__main__':
    cli()
