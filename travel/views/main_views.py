from flask import Blueprint, render_template, request

from travel.models import Tour, Notice

from travel.forms import RegisterForm

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    form = RegisterForm()
    page = request.args.get('page', default=1, type=int)
    tour_list = Tour.query.order_by(Tour.id)
    notice_list = Notice.query.order_by(Notice.id.desc()).paginate(page=page, per_page=10)
    return render_template('main.html',tour_list=tour_list, notice_list=notice_list, form=form)

