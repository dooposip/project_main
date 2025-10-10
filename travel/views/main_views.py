from flask import Blueprint, render_template

from travel.models import Tour

from travel.forms import RegisterForm

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    form = RegisterForm()
    tour_list = Tour.query.order_by(Tour.id)
    return render_template('main.html',tour_list=tour_list)