import unittest
from webapp import create_app, db
from webapp.models import EquipmentTypes, Equipments
from config import TestConfig
from webapp.controllers import validate_serial_numbers


class ValidationCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

        db.session.add_all([
            EquipmentTypes(code=1, type_name='TP-Link TL-WR74', sn_mask='XXAAAAAXAA'),
            EquipmentTypes(code=2, type_name='D-Link DIR-300', sn_mask='NXXAAXZXaa'),
            EquipmentTypes(code=3, type_name='D-Link DIR-300 S', sn_mask='NXXAAXZXXX')
        ])
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_validation(self):

        equipments = [
            Equipments(type_code=1, serial_number='12ABCDE3FG'),
            Equipments(type_code=1, serial_number='ABCDEFGHIJ'),
            Equipments(type_code=2, serial_number='0ABCDE-Ghi'),
            Equipments(type_code=2, serial_number='1A2BC3_Def'),
            Equipments(type_code=3, serial_number='01ABC2@3D4'),
            Equipments(type_code=3, serial_number='9A8BC7-6DE'),
        ]

        for e in equipments:
            self.assertTrue(e.validate())

        equipments = [
            Equipments(type_code=1, serial_number='aaaaaaaaaa'),
            Equipments(type_code=2, serial_number='1111111111'),
            Equipments(type_code=3, serial_number='AAAAAAAAAA'),
        ]

        for e in equipments:
            self.assertFalse(e.validate())

    def test_validate_numbers(self):
        serial_numbers = ['12ABCDE3FG', 'ABCDEFGHIJ', '']
        correct, incorrect = validate_serial_numbers(1, serial_numbers)
        self.assertEqual(len(correct), 2)
        self.assertEqual(len(incorrect), 0)

        serial_numbers = ['aaABCDE3FG', 'ABCDEFGHIJ']
        correct, incorrect = validate_serial_numbers(1, serial_numbers)
        self.assertEqual(len(correct), 1)
        self.assertEqual(len(incorrect), 1)


if __name__ == '__main__':
    unittest.main(verbosity=2)


