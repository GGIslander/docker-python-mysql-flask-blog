#from enum import unique
#from math import fabs
#from app.blueprints.qa import question_detail
from exts import db
from datetime import datetime

class EmailCpatchaModel(db.Model):
    __tablename__ = "email_captcha"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    captcha = db.Column(db.String(10), nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)

class UserModel(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(256), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(256), nullable=False)
    avatar = db.Column(db.String(256), nullable=False, default='')
    create_time = db.Column(db.DateTime, default=datetime.now)

class QuestionModel(db.Model):
    __tablename__ = "question"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uid = db.Column(db.Integer, db.ForeignKey("user.id"))
    title = db.Column(db.String(256), nullable=False)
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)

    author = db.relationship("UserModel", backref="question")

class AnswerModel(db.Model):
    __tablename__ ="answer"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text, nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey("question.id"))
    uid = db.Column(db.Integer, db.ForeignKey("user.id"))
    create_time = db.Column(db.DateTime, default=datetime.now)

    question = db.relationship("QuestionModel", backref="answers")
    author = db.relationship("UserModel", backref="answer")
