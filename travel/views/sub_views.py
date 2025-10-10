from flask import Blueprint, render_template

from travel.forms import ReviewForm
from travel.models import Tour

bp = Blueprint('sub', __name__, url_prefix='/sub')

@bp.route('/detail/<int:tour_id>/')
def detail(tour_id):
    form = ReviewForm()
    tour = Tour.query.get_or_404(tour_id)
    return render_template('sub/travel_detail.html',tour=tour, form=form)