from flask import Blueprint, url_for, request, redirect, render_template, flash
from werkzeug.security import generate_password_hash

from travel import db
from travel.forms import UserCreateForm

from travel.models import User

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/signup/', methods=['GET', 'POST'])
def signup():
    form = UserCreateForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(userid=form.userid.data).first()
        nick = User.query.filter_by(username=form.username.data).first()
        if not user:
            if not nick:
                user = User(userid=form.userid.data,
                            username=form.username.data,
                            password=generate_password_hash(form.password1.data),
                            email=form.email.data)
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('main.index'))
            else:
                flash('이미 존재하는 닉네임입니다.')
        else:
            flash('이미 존재하는 사용자입니다.')
    return render_template('auth/signup.html', form=form)