from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
# app.config['SECRET_KEY'] = 'hard to guess'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@127.0.0.1:3306/jswl_auto_repair'
# 设置这一项是每次请求结束后都会自动提交数据库中的变动
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)

class CustomerSurvey(db.Model):
    __tablename__ = "customer_survey"
    user_id = db.Column(db.Integer,primary_key=True)
    user_name = db.Column(db.String(20), unique=True)
    user_sex = db.Column(db.String(2), unique=True)
    user_age = db.Column(db.Integer,primary_key=True)
    user_telphone = db.Column(db.String(20), unique=True)
    user_business_address = db.Column(db.String(10), unique=True)
    user_operation = db.Column(db.String(255), unique=True)
    user_scope_of_business = db.Column(db.String(10), unique=True)
    user_is_intention = db.Column(db.String(10), unique=True)
    user_lease_use = db.Column(db.String(10), unique=True)
    user_move_date = db.Column(db.String(10), unique=True)
    user_whether_school_children = db.Column(db.String(10), unique=True)
    user_children_school_level = db.Column(db.String(10), unique=True)
    user_children_now_school = db.Column(db.String(10), unique=True)
    user_children_way = db.Column(db.String(10), unique=True)
    user_is_stay = db.Column(db.String(10), unique=True)
    user_source = db.Column(db.String(10), unique=True)
    user_remake = db.Column(db.String(10), unique=True)

    def __repr__(self):
        return '<%r>' % self.user_remake

