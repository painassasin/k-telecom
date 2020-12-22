from webapp.main.forms import EquipmentForm
from flask import render_template, flash, redirect, url_for
from webapp.models import EquipmentTypes
from webapp.controllers import validate_serial_numbers, insert_equipments
from webapp.main import main_bp


@main_bp.route('/', methods=['GET', 'POST'])
def index():
    form = EquipmentForm()
    form.equipment_type.choices = [
        (t.code, t.type_name) for t in EquipmentTypes.query.all()]
    if form.validate_on_submit():
        et = form.equipment_type.data
        sn = form.serial_numbers.data
        correct, incorrect = validate_serial_numbers(et, sn.split('\r\n'))
        if incorrect:
            numbers = ', '.join(e.serial_number for e in incorrect)
            sn_mask = EquipmentTypes.query.get(et).sn_mask
            flash(f'Номера {numbers} не соответствуют маске {sn_mask}',
                  'danger')
        else:
            duplicates = insert_equipments(correct)
            if not duplicates:
                flash('Все номера успешно добавлены', 'success')
                return redirect(url_for('main.index'))

            flash(f'Такой номер уже существует: {duplicates}', 'danger')

    return render_template('index.html',
                           title='K-Telecom',
                           form_title='Форма добавления серийных номеров',
                           form=form)
