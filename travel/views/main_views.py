from flask import Blueprint

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return 'Project start22222222222222!'