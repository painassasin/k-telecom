from webapp.models import EquipmentTypes, Equipments
from sqlalchemy.exc import IntegrityError
from webapp import app, db
import re


def create_pattern(sn_mask: str) -> str:
    """
    Создает регулярное выражение для валидации номера по маске.
    :param sn_mask:
    :return:
    """
    re_dict = app.config['RE_DICT']
    re_string = ''.join([re_dict[char] for char in sn_mask])
    return f'^({re_string})$'


def valid_serial_number(sn_mask: str, serial_number: str) -> bool:
    """
    Проверяет серийный номер на соответствие маске.
    :param sn_mask:
    :param serial_number:
    :return:
    """
    pattern_string = create_pattern(sn_mask)
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

    sn_mask = get_equipment_mask(equipment_code)
    if not sn_mask:
        return False, 'Ошибка на сервере!'

    for sn in serial_numbers:
        if not valid_serial_number(sn_mask, sn):
            msg = (f'Серийный номер <b>{sn}</b> '
                   f'не соответствует маске <b>{sn_mask}</b>')
            return False, msg

    return True, ''


def get_equipment_mask(type_code: str) -> str:
    """
    Получает по идентификатору типа оборудования маску его серийного номера.
    В случае ошибок возвращает пустую строку.
    :param type_code:
    :return:
    """
    try:
        sn_mask = db.session.\
            query(EquipmentTypes.sn_mask).\
            filter(EquipmentTypes.code == int(type_code)).first()
        if sn_mask:
            return sn_mask[0]
    except Exception as err:
        print(f'{type(err)}\n{str(err)}')
    return ''


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
        db.session.add(Equipments(type_code, serial_number))
    try:
        db.session.commit()
    except IntegrityError as err:
        duplicate = err.params.get('serial_number')
        return False, f'Обнаружена дублирующая запись <b>{duplicate}</b>'
    except Exception as err:
        print(f'{type(err)}\n{str(err)}')
        return False, 'Ошибка на сервере!'

    return True, 'Серийные номера успешно добавлены!'


def insert_equipment_types() -> bool:
    """
    Вставляет дефолтные знаения типов оборудования.
    :return:
    """
    equipments = [
        EquipmentTypes('TP-Link TL-WR74', 'XXAAAAAXAA'),
        EquipmentTypes('D-Link DIR-300', 'NXXAAXZXaa'),
        EquipmentTypes('D-Link DIR-300 S', 'NXXAAXZXXX'),
    ]
    for e in equipments:
        db.session.add(e)
    try:
        db.session.commit()
    except IntegrityError as err:
        return False
    return True
