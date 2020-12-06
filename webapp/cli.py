from webapp import db
from webapp.models import EquipmentTypes
from sqlalchemy.exc import IntegrityError


def register(app):
    @app.cli.group()
    def fixtures():
        """Load or remove fixtures."""
        pass

    @fixtures.command()
    def load():
        """Load fixtures."""
        db.session.add_all([
            EquipmentTypes(type_name='TP-Link TL-WR74', sn_mask='XXAAAAAXAA'),
            EquipmentTypes(type_name='D-Link DIR-300', sn_mask='NXXAAXZXaa'),
            EquipmentTypes(type_name='D-Link DIR-300 S', sn_mask='NXXAAXZXXX')
        ])
        try:
            db.session.commit()
            print('Fixtures successfully loaded')
        except IntegrityError:
            db.session.rollback()
            print('Fixtures already exists')

    @fixtures.command()
    def remove():
        """Purge equipment types."""
        try:
            num_rows_deleted = db.session.query(EquipmentTypes).delete()
            db.session.commit()
        except IntegrityError:
            db.session.rollback()

