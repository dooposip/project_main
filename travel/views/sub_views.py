from flask import Blueprint, render_template

bp = Blueprint('sub', __name__, url_prefix='/sub')

@bp.route('/detail/')
def detail():
    return render_template('sub/travel_detail.html')