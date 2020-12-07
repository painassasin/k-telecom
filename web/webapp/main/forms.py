from flask_wtf import FlaskForm
from wtforms import SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class EquipmentForm(FlaskForm):

    equipment_type = SelectField(
        label='Тип оборудования',
        validators=[DataRequired('Необходимо заполнить')],
    )
    serial_numbers = TextAreaField(
        label='Серийные номера',
        validators=[DataRequired('Необходимо заполнить')],
        render_kw={'style': 'height:150px'}
    )
    submit = SubmitField(label='Добавить')
