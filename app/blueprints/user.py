from crypt import methods
from flask import Blueprint,render_template,request,url_for,redirect,jsonify,session,flash
from email.message import Message
import imp
#from urllib import request
from exts import mail,db
from flask_mail import Message
from models import EmailCpatchaModel,UserModel
import string,random
from datetime import datetime
from .forms import RegisterForm,LoginForm
from werkzeug.security import generate_password_hash,check_password_hash

bp = Blueprint("user", __name__, url_prefix="/user")

@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            user = UserModel.query.filter_by(email=email).first()
            if user and check_password_hash(user.password, password):
                session['user_id'] = user.id
                return redirect("/")
            else:
                flash("用户名密码不匹配")
                return redirect(url_for("user.login"))
        else:
            flash("用户名密码格式错误")
            return redirect(url_for("user.login"))


@bp.route("/regitster", methods=['GET', 'POST'])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        form = RegisterForm(request.form)
        if form.validate():
            email = form.email.data
            username = form.username.data
            password = generate_password_hash(form.password.data)
            user = UserModel(email=email,username=username,password=password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("user.login"))
        else:
            return redirect(url_for("user.register"))

    

@bp.route("/captcha", methods=["POST"])
def get_captcha():
    #接收参数
    email = request.form["email"]
    # 生成验证码
    str = string.ascii_letters+string.digits
    captcha = "".join(random.sample(str, 4))
    if not email:
        return jsonify({"code":400, "message":"请先传递邮箱"})

    message = Message(
        subject="邮箱测试",
        recipients=[email],
        body=f"这是一篇测试邮件,验证码{captcha}"
        )
    mail.send(message)
    # 查询邮箱是否已经注册
    captcha_model = EmailCpatchaModel.query.filter_by(email=email).first()
    if captcha_model:
        captcha_model.captcha =  captcha 
        captcha_model.create_time = datetime.now()
        db.session.commit()
    else:
        captcha_model = EmailCpatchaModel(email=email, captcha=captcha)
        db.session.add(captcha_model)
        db.session.commit()
    
    return jsonify({"code":200})

@bp.route("logout")
def logout():
    # 清除session
    session.clear()
    return redirect(url_for('user.login'))