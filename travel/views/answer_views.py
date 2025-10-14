from datetime import datetime

from flask import Blueprint, request, redirect, url_for, render_template, g, flash

from travel import db
from travel.forms import AnswerForm
from travel.models import Notice, Comment
from travel.views.auth_views import login_required

bp = Blueprint('comment', __name__, url_prefix='/comment')

@bp.route('/create/<int:notice_id>', methods=['POST'])
@login_required
def create(notice_id):
    form = AnswerForm()
    notice = Notice.query.get_or_404(notice_id)
    if form.validate_on_submit():
        content = request.form['content']
        comment = Comment(notice=notice, content=content, create_date=datetime.now(),
                        user_id=g.user.id)
        notice.comment_set.append(comment)
        db.session.commit()
        return redirect(url_for('notice.detail', notice_id=notice_id))
    return render_template('notice/question_detail.html', notice=notice, form=form)

@bp.route('/modify/<int:comment_id>', methods=['GET', 'POST'])
@login_required
def modify(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    if g.user != comment.user:
        flash('수정권한이 없습니다.')
        return redirect(url_for('notice.detail', notice_id=comment.notice.id))
    if request.method == 'POST':
        form = AnswerForm()
        if form.validate_on_submit():
            form.populate_obj(comment)
            comment.modify_date = datetime.now()  # 수정일시 저장
            db.session.commit()
            return redirect(url_for('notice.detail', notice_id=comment.notice.id))
    else:
        form = AnswerForm(obj=comment)
    return render_template('comment/answer_form.html', form=form)

@bp.route('/delete/<int:comment_id>')
@login_required
def delete(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    notice_id = comment.notice.id
    if g.user != comment.user:
        flash('삭제권한이 없습니다.')
    else:
        db.session.delete(comment)
        db.session.commit()
    return redirect(url_for('notice.detail', notice_id=notice_id))
