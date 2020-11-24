from webapp import app, db
from webapp.forms import EquipmentForm
from flask import render_template
from webapp.models import EquipmentTypes
from sqlalchemy.exc import IntegrityError


@app.route('/', methods=['GET', 'POST'])
def index():
    form = EquipmentForm()
    context = {
        'title': 'K-Telecom',
        'form_title': 'Форма добавления серийных номеров',
        'form': form, }

    if form.validate_on_submit():
        type_code = form.equipment_type.data
        sn = form.serial_numbers.data

        return ''

    return render_template('index.html', **context)


@app.route('/init')
def init_db():
    equipments = [
        EquipmentTypes('TP-Link TL-WR74', 'XXAAAAAXAA'),
        EquipmentTypes('D-Link DIR-300', 'NXXAAXZXaa'),
        EquipmentTypes('D-Link DIR-300 S', 'NXXAAXZXXX'),
    ]
    try:
        for e in equipments:
            db.session.add(e)
        db.session.commit()
        return 'Done'
    except IntegrityError as err:
        return 'Записи уже добавлены'
