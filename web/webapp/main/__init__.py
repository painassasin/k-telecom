from flask import Blueprint

main_bp = Blueprint('main', __name__)

from webapp.main import routes
