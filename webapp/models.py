from webapp import db


class EquipmentTypes(db.Model):
    __tablename__ = 'equipmentTypes'
    code = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    type_name = db.Column(db.String(100), nullable=False, unique=True)
    sn_mask = db.Column(db.String(50), nullable=False)

    def __init__(self, type_name, sn_mask):
        self.type_name = type_name
        self.sn_mask = sn_mask


class Equipments(db.Model):
    __tablename__ = 'equipments'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    type_code = db.Column(db.Integer(), db.ForeignKey('equipmentTypes.code'))
    serial_number = db.Column(db.String(50), nullable=False, unique=True)

    def __init__(self, type_code, serial_number):
        self.type_code = type_code
        self.serial_number = serial_number
