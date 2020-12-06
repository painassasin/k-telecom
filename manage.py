from webapp import create_app, db, cli
from config import Config
from webapp.models import EquipmentTypes, Equipments


app = create_app(Config)
cli.register(app)


@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'EquipmentTypes': EquipmentTypes,
        'Equipments': Equipments
    }

