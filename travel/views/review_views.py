
from datetime import datetime

from flask import Blueprint, flash, g, redirect, render_template, request, url_for

from travel import db
from travel.forms import ReviewForm
from travel.models import Review, Tour
from travel.views.auth_views import login_required


bp = Blueprint('review', __name__, url_prefix='/review')

@bp.route('/review/<int:tour_id>', methods=['POST'])
@login_required
def create(tour_id):
    form = ReviewForm()
    tour = Tour.query.get_or_404(tour_id)
    if form.validate_on_submit():
        content = request.form['content']
        review = Review(tour=tour, content=content, create_date=datetime.now(), user_id=g.user.id)
        db.session.add(review)
        db.session.commit()
        return redirect(url_for('sub.detail', tour_id=tour_id))
    return render_template('sub/travel_detail.html',tour=tour, form=form)

@bp.route('/modify/<int:review_id>', methods=['GET', 'POST'])
@login_required
def modify(review_id):
    review = Review.query.get_or_404(review_id)
    if g.user != review.user:
        flash('수정권한이 없습니다.')
        return redirect(url_for('sub.detail', tour_id=review.tour.id))
    if request.method == 'POST':
        form = ReviewForm()
        if form.validate_on_submit():
            form.populate_obj(review)
            review.modify_date = datetime.now()  # 수정일시 저장
            db.session.commit()
            return redirect(url_for('sub.detail', tour_id=review.tour.id))
    else:
        form = ReviewForm(obj=review)
    return render_template('review/review_form.html', form=form)

@bp.route('/delete/<int:review_id>/')
@login_required
def delete(review_id):
    review = Review.query.get_or_404(review_id)
    if g.user != review.user:
        flash('삭제 권한이 없습니다!')
        return redirect(url_for('sub.detail', tour_id=review.tour_id))
    else:
        db.session.delete(review)
        db.session.commit()
        return redirect(url_for('sub.detail', tour_id=review.tour_id))