from webapp import db


class EquipmentTypes(db.Model):
    __tablename__ = 'equipment_types'
    code = db.Column(db.Integer(), primary_key=True)
    type_name = db.Column(db.String(100), nullable=False, unique=True)
    sn_mask = db.Column(db.String(50), nullable=False)
    equipment = db.relationship('Equipments', backref='type', lazy='dynamic')


class Equipments(db.Model):
    __tablename__ = 'equipments'
    id = db.Column(db.Integer(), primary_key=True)
    type_code = db.Column(db.Integer(), db.ForeignKey('equipment_types.code'))
    serial_number = db.Column(db.String(50), nullable=False, unique=True)
