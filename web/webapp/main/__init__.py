from flask import Blueprint

main_bp = Blueprint('main', __name__)


def register_blueprint(app):
    from webapp.main import routes
    app.register_blueprint(main_bp)
