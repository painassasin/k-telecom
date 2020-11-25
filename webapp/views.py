from webapp.controllers import insert_equipments, insert_equipment_types
from webapp.forms import EquipmentForm
from flask import render_template
from webapp import app
import json


@app.route('/', methods=['GET', 'POST'])
def index():
    form = EquipmentForm()

    if form.validate_on_submit():
        type_code = form.equipment_type.data
        sn = form.serial_numbers.data

        result, msg = insert_equipments(type_code, sn.split('\r\n'))
        return json.dumps({'success': result, 'msg': msg})

    return render_template('index.html',
                           title='K-Telecom',
                           form_title='Форма добавления серийных номеров',
                           form=form,)


@app.route('/init')
def init_db():
    return 'Ok' if insert_equipment_types() else 'Записи уже добавлены'


