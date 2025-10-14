from datetime import datetime

from flask import Blueprint, render_template, request, redirect, url_for, g, flash

from travel import db
from travel.models import Notice

from travel.forms import QuestionForm, AnswerForm
from travel.views.auth_views import login_required

bp = Blueprint('notice', __name__, url_prefix='/notice')

@bp.route('/list/')
def _list():
    page = request.args.get('page', default=1, type=int)
    notice_list = Notice.query.order_by(Notice.create_date).paginate(page=page, per_page=10)
    return render_template('main.html', notice_list=notice_list)


@bp.route('/detail/<int:notice_id>/')
def detail(notice_id):
    form = AnswerForm()  # 질문 상세 템플릿에 폼 추가
    notice = Notice.query.get_or_404(notice_id)
    return render_template('notice/question_detail.html', notice=notice, form=form)


@bp.route('/create/', methods=['GET', 'POST'])
@login_required
def create():
    form = QuestionForm()
    image_path = None
    if request.method=='POST' and form.validate_on_submit():
        notice = Notice(subject=form.subject.data, content=form.content.data, create_date=datetime.now(), user_id=g.user.id, image_path=image_path)
        db.session.add(notice)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('notice/question_form.html', form=form)


@bp.route('/modify/<int:notice_id>/', methods=['GET', 'POST'])
@login_required
def modify(notice_id):
    notice = Notice.query.get_or_404(notice_id)
    if g.user != notice.user:
        flash('수정권한이 없습니다.')
        return redirect(url_for('notice.detail', notice_id=notice_id))
    if request.method=='POST':  # POST요청
        form = QuestionForm()
        if form.validate_on_submit():
            form.populate_obj(notice)
            notice.modify_date = datetime.now()  # 수정일시 저장
            db.session.commit()
            return redirect(url_for('notice.detail', notice_id=notice_id))
    else:  # GET요청
        form = QuestionForm(obj=notice)
    return render_template('notice/question_form.html', form=form)


@bp.route('/delete/<int:notice_id>/')
@login_required
def delete(notice_id):
    notice = Notice.query.get_or_404(notice_id)
    if g.user != notice.user:
        flash('삭제권한이 없습니다.')
        return redirect(url_for('notice.detail', notice_id=notice_id))
    db.session.delete(notice)
    db.session.commit()
    return redirect(url_for('main.index'))

