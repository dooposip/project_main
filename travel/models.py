# DB 구성하는 곳
from travel import db

#####################################################################################
# primary_key = 해당 컬럼을 기본키로 설정
#               보통 id 컬럼에 많이 사용함
#               중복, NULL 불가

# unique = 해당 컬럼 값이 테이블 안에서 유일해야함
#          이메일, 주민등록번호 같은 데이터에 주로 사용 (이메일, userid, username 에 사용 중)

# nullable = NULL 값을 허용할지 정할수 있음
#            False로 설정시 값이 들어가야함
#            비울수 없는 컬럼에서 사용해야함

# autoincrement = 정수형 컬럼에서 주로 사용, 새 레코드가 들어올 때마다 값이 자동으로 증가함
#                 주로 id컬럼에서 사용함

# ondelete='CASCADE' = 글 작성자가 탈퇴시 작성했던 글 삭제
#                      그냥 두면 오류가 발생할수 있기 때문에 삭제
#####################################################################################


# 유저모델 생성
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)      # db에 생성된 순서로 부여되는 id
    userid = db.Column(db.String(50), unique=True, nullable=False)        # user 가 회원 생성시 작성하는 로그인을 위한 id / 필수입력
    password = db.Column(db.String(200), nullable=False)                  # 비밀번호  / 필수입력
    username = db.Column(db.String(50), unique=True, nullable=False)      # 닉네임 / 필수입력
    email = db.Column(db.String(100), unique=True, nullable=False)        # 이메일 / 필수입력

# 게시판 작성 모델 생성
class Notice(db.Model):
    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)     # db에 생성된 순서로 부여되는 id
    subject = db.Column(db.String(200), nullable=False)                   # 게시글 제목 / 필수입력
    content = db.Column(db.Text(), nullable=False)                        # 게시글 내용 / 필수입력
    image_path = db.Column(db.String(200), nullable=True)                 # 이미지 첨부
    create_date = db.Column(db.DateTime(), nullable=False)                # 작성시간 / 자동생성
    modify_date = db.Column(db.DateTime(), nullable=True)                 # 수정시 수정시간 생성
    # Notice와 User을 상호 연결(참조)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'),nullable=False)
    user = db.relationship('User', backref=db.backref('notice_set'))

# 게시판 댓글 모델 생성
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)     # db에 생성된 순서로 부여되는 id
    content = db.Column(db.Text(), nullable=False)                        # 댓글 내용 / 필수입력
    create_date = db.Column(db.DateTime(), nullable=False)                # 작성시간 / 자동생성
    modify_date = db.Column(db.DateTime(), nullable=True)                 # 수정시 수정시간 생성
    # Comment와 Notice를 상호 연결(참조)
    notice_id = db.Column(db.Integer, db.ForeignKey('notice.id', ondelete='CASCADE'))
    notice = db.relationship('Notice', backref=db.backref('comment_set'))
    # Comment와 User을 상호 연결(참조)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('comment_set'))

# 여행지 모델 생성
class Tour(db.Model):
    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)     # db에 생성된 순서로 부여되는 id
    image_path = db.Column(db.String(200), nullable=False)                # 이미지 첨부 / 필수입력
    place = db.Column(db.String(150), nullable=False)                     # 관광지명 / 필수입력
    location = db.Column(db.String(200), nullable=False)                  # 위치 / 필수입력
    season = db.Column(db.String(100), nullable=False)                    # 계절 / 필수입력
    content = db.Column(db.Text(), nullable=False)                        # 여행지 설명 / 필수입력
    time = db.Column(db.String(150), nullable=False)                     # 관광지명 / 필수입력
    price = db.Column(db.String(150), nullable=False)                     # 관광지명 / 필수입력
    rating = db.Column(db.String(150), nullable=False)                     # 관광지명 / 필수입력
    level = db.Column(db.String(150), nullable=False)                     # 관광지명 / 필수입력
    

# 리뷰 모델 생성
class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)      # db에 생성된 순서로 부여되는 id
    content = db.Column(db.Text(), nullable=False)                        # 댓글 내용 / 필수입력
    create_date = db.Column(db.DateTime(), nullable=False)                # 작성시간 / 자동생성
    modify_date = db.Column(db.DateTime(), nullable=True)                 # 수정시 수정시간 생성
    # Review와 Tour를 상호 연결(참조)
    tour_id = db.Column(db.Integer, db.ForeignKey('tour.id', ondelete='CASCADE'))
    tour = db.relationship('Tour', backref=db.backref('review_set'))
    # Review와 User를 상호 연결(참조)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('review_set'))
