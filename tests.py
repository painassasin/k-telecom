import unittest
from webapp import create_app, db
from webapp.models import EquipmentTypes, Equipments
from config import TestConfig, Config
from sqlalchemy.exc import IntegrityError


class DatabaseRelationModelCase(unittest.TestCase):
    def setUp(self):
        # Can not test relationships via SQLite
        self.app = create_app(Config)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_foreign_key_constraint_failure(self):
        et1 = EquipmentTypes(code=1, type_name='type_a', sn_mask='a')
        et2 = EquipmentTypes(code=2, type_name='type_b', sn_mask='b')
        db.session.add_all([et1, et2])
        db.session.commit()

        e = Equipments(type_code=10, serial_number='10')
        db.session.add(e)
        with self.assertRaises(IntegrityError):
            db.session.commit()

    def test_duplicates_failure(self):
        et1 = EquipmentTypes(code=1, type_name='type_a', sn_mask='a')
        et2 = EquipmentTypes(code=2, type_name='type_b', sn_mask='b')
        db.session.add_all([et1, et2])
        db.session.commit()

        e1 = Equipments(type_code=1, serial_number='10')
        db.session.add(e1)
        db.session.commit()

        e2 = Equipments(type_code=2, serial_number='10')
        db.session.add(e2)
        with self.assertRaises(IntegrityError):
            db.session.commit()

    def test_delete_parent_rows_failure(self):
        et = EquipmentTypes(code=1, type_name='type_a', sn_mask='a')
        db.session.add(et)
        db.session.commit()

        e = Equipments(type_code=1, serial_number='10')
        db.session.add(e)
        db.session.commit()

        with self.assertRaises(IntegrityError):
            db.session.query(EquipmentTypes).delete()
            db.session.commit()


if __name__ == '__main__':
    unittest.main(verbosity=2)


