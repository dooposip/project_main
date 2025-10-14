import os


from flask import Blueprint, current_app, redirect, render_template, request, url_for
from werkzeug.utils import secure_filename

from travel import db
from travel.models import Tour

from travel.forms import RegisterForm

bp = Blueprint('admin', __name__, url_prefix='/admin')

@bp.route('/regist/', methods=['GET', 'POST'])
def create():
    form = RegisterForm()
    if request.method == 'POST' and form.validate_on_submit():
        # 폼에서 전송된 이미지 파일
        image_file = form.image.data
        image_path = None

        if image_file:
            # 저장 경로 : 오늘 날짜로 폴더 생성
            upload_folder = os.path.join(current_app.root_path, 'static/img', 'admin')    # 폴더 경로 지정
                                        # current_app.root_path : myproject 폴더 내 pybo폴더
            os.makedirs(upload_folder, exist_ok=True)                                   # 폴더 생성

            # 파일 저장
            filename = secure_filename(image_file.filename)
            file_path = os.path.join(upload_folder, filename)
            image_file.save(file_path)

            # DB에 저장할 경로 (db에는 파일 저장 경로만 생성 / static 기준 상대경로)
            image_path = f'img/{'admin'}/{filename}'

            # ✅ season을 다중 선택으로 받아 쉼표로 join
            seasons = request.form.get('season')

        tour = Tour(
            image_path=image_path,
            place=form.place.data,
            location=form.location.data,
            season=seasons,
            content=form.content.data,
            time=form.time.data,
            price=form.price.data,
            rating=form.rating.data,
            level=form.level.data
            )
        
        db.session.add(tour)
        db.session.commit()

        return redirect(url_for('main.index'))
    return render_template('admin/register_form.html', form=form)