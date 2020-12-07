from webapp import db
from flask import current_app
import re


class EquipmentTypes(db.Model):
    __tablename__ = 'equipment_types'
    code = db.Column(db.Integer(), primary_key=True)
    type_name = db.Column(db.String(30), nullable=False, unique=True)
    sn_mask = db.Column(db.String(10), nullable=False)
    equipment = db.relationship('Equipments', backref='type', lazy='dynamic')


class Equipments(db.Model):
    __tablename__ = 'equipments'
    id = db.Column(db.Integer(), primary_key=True)
    type_code = db.Column(db.Integer(), db.ForeignKey('equipment_types.code'))
    serial_number = db.Column(db.String(10), nullable=False, unique=True)

    def validate(self) -> bool:
        """
        Проверяет серийный номер на соответствие маске
        :return:
        """
        re_dict = current_app.config['RE_DICT']
        et = EquipmentTypes.query.get(self.type_code)
        re_string = ''.join([re_dict[char] for char in et.sn_mask])
        pattern = re.compile(f'^({re_string})$')
        return bool(pattern.search(self.serial_number))
