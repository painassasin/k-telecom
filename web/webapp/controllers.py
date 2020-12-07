from webapp.models import Equipments
from webapp import db
from sqlalchemy.exc import IntegrityError


def validate_serial_numbers(type_code: str, serial_numbers: list) -> tuple:
    incorrect = set()
    correct = set()

    for sn in serial_numbers:
        # Если есть пустые строки - игнорировать их
        if not sn:
            continue

        e = Equipments(type_code=type_code, serial_number=sn)
        valid = e.validate()
        if not valid:
            incorrect.add(e)
        else:
            correct.add(e)

    return correct, incorrect


def insert_equipments(equipments: set) -> str:
    db.session.add_all(equipments)
    try:
        db.session.commit()
    except IntegrityError as err:
        db.session.rollback()
        return err.params['serial_number']