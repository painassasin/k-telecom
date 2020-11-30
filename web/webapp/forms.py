from flask_wtf import FlaskForm
from wtforms import SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired
from webapp.models import EquipmentTypes
from webapp.controllers import get_equipment_types


class EquipmentForm(FlaskForm):

    equipment_type = SelectField(
        label='Тип оборудования',
        validators=[DataRequired()],
        render_kw={'class': 'form-control'},
        choices=get_equipment_types(),
    )

    serial_numbers = TextAreaField(
        label='Серийные номера',
        validators=[DataRequired()],
        render_kw={'class': 'form-control',
                   'style': 'height:150px'})

    submit = SubmitField(label='Добавить',
                         render_kw={'class': 'btn btn-primary'})
