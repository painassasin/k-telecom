from webapp.controllers import insert_equipments
from flask import render_template, jsonify
from webapp.forms import EquipmentForm
from webapp import app


@app.route('/', methods=['GET', 'POST'])
def index():
    form = EquipmentForm()

    if form.validate_on_submit():
        type_code = form.equipment_type.data
        sn = form.serial_numbers.data

        result, msg = insert_equipments(type_code, sn.split('\r\n'))
        return jsonify(success=result, msg=msg)

    return render_template('index.html',
                           title='K-Telecom',
                           form_title='Форма добавления серийных номеров',
                           form=form,)
