from flask.cli import FlaskGroup
from webapp import app, db
from webapp.models import EquipmentTypes
from sqlalchemy.exc import IntegrityError

cli = FlaskGroup(app)


@cli.command('load_fixture')
def create_seed_data():

    db.session.add_all([
        EquipmentTypes(type_name='TP-Link TL-WR74', sn_mask='XXAAAAAXAA'),
        EquipmentTypes(type_name='D-Link DIR-300', sn_mask='NXXAAXZXaa'),
        EquipmentTypes(type_name='D-Link DIR-300 S', sn_mask='NXXAAXZXXX')
    ])
    try:
        db.session.commit()
    except IntegrityError:
        print('Fixtures already exists')


if __name__ == '__main__':
    cli()
