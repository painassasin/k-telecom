from webapp.models import EquipmentTypes, Equipments
from sqlalchemy.exc import IntegrityError
from webapp import app, db
import re


def valid_serial_number(sn_mask: str, serial_number: str) -> bool:
    """
    Проверяет серийный номер на соответствие маске.
    :param sn_mask:
    :param serial_number:
    :return:
    """
    re_dict = app.config['RE_DICT']
    re_string = ''.join([re_dict[char] for char in sn_mask])
    pattern_string = f'^({re_string})$'
    pattern = re.compile(pattern_string)
    return bool(pattern.search(serial_number))


def validate_numbers(equipment_code: str, serial_numbers: list) -> tuple:
    """
    Проверяет набор серийных номеров на соответсвие маске оборудования.
    Возвращается результат проверки в формате (bool, str).
    При возникновении ошибок, первое значение будет False,
    второе значение описывает суть проблемы.
    В случае удачной проверки возвращается (True, '').
    :param equipment_code:
    :param serial_numbers:
    :return:
    """

    # Получение маски серийного номера
    sn_mask = ''
    try:
        mask = (
            db.session.query(EquipmentTypes.sn_mask).
            filter(EquipmentTypes.code == int(equipment_code)).first()
        )
        if mask:
            sn_mask = mask[0]
    except Exception as err:
        print(f'{type(err)}\n{str(err)}')
        return False, 'Ошибка на сервере!'

    # Проверка серийныйх номеров на валидность
    for sn in serial_numbers:
        if not valid_serial_number(sn_mask, sn):
            msg = (f'Серийный номер <b>{sn}</b> '
                   f'не соответствует маске <b>{sn_mask}</b>')
            return False, msg

    return True, ''


def insert_equipments(type_code: str, sns: list) -> tuple:
    """
    Сначана проверяет полученные номера на соответсвие маске.
    Если все нормально добавляет записи в таблицу.
    В результате возвращает два значения:
    - есть ли ошибка (bool)
    - сообщение (str)
    :param type_code:
    :param sns:
    :return:
    """

    valid, msg = validate_numbers(type_code, sns)

    # В случае несоответсвия маске
    if not valid:
        return False, msg

    # Если соответствует маске
    for serial_number in sns:
        e = Equipments(type_code=type_code, serial_number=serial_number)
        db.session.add(e)
    try:
        db.session.commit()
    except IntegrityError as err:
        duplicate = err.params.get('serial_number')
        return False, f'Обнаружена дублирующая запись <b>{duplicate}</b>'
    except Exception as err:
        print(f'{type(err)}\n{str(err)}')
        return False, 'Ошибка на сервере!'

    return True, 'Серийные номера успешно добавлены!'
