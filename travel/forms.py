from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms.fields.simple import StringField, PasswordField, EmailField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class RegisterForm(FlaskForm):
    image = FileField('이미지 업로드', validators=[FileAllowed(['jpg', 'jpeg', 'gif', 'png'], '이미지 파일만 업로드 가능합니다.')])
    place=StringField('여행지명', validators=[DataRequired("여행지명은 필수입력 항목입니다.")])
    location=StringField('위치', validators=[DataRequired("위치는 필수입력 항목입니다.")])
    season= StringField('계절') 
    content=TextAreaField('내용', validators=[DataRequired("설명은 필수입력 항목입니다.")])


class UserCreateForm(FlaskForm):
    userid = StringField('ID', validators=[DataRequired(), Length(min=3, max=10)])
    username = StringField('닉네임', validators=[DataRequired(), Length(min=3,max=25)])
    password1 = PasswordField('비밀번호', validators=[DataRequired(), EqualTo('password2', message='비밀번호가 일치하지 않습니다.')])
    password2 = PasswordField('비밀번호확인', validators=[DataRequired()])
    email = EmailField('이메일', validators=[DataRequired(), Email()])

class UserLoginForm(FlaskForm):
    userid = StringField('ID', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('비밀번호', validators=[DataRequired()])

