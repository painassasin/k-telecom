from flask_wtf import FlaskForm
from wtforms import SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class EquipmentForm(FlaskForm):

    equipment_type = SelectField(
        label='Тип оборудования',
    )
    serial_numbers = TextAreaField(
        label='Серийные номера',
        validators=[DataRequired('Необходимо заполнить')],
    )
    submit = SubmitField(label='Добавить')
