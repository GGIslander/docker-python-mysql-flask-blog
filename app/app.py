from atexit import register
from flask import Flask,session,g
from flask_migrate import Migrate
import config
from exts import db,mail
#from blueprints.qa import qa as qa_bp
from blueprints import qa_bp
from blueprints import user_bp
from models import UserModel

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
mail.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(qa_bp)
app.register_blueprint(user_bp)

# 请求前置钩子
@app.before_request
def before_request():
    user_id = session.get("user_id")
    if user_id:
        try:
            user = UserModel.query.get(user_id)
            #  给g绑定一个全局变量user
            setattr(g, "user", user)
            # g.user = user # 上下同意
        except:
            g.user=None

#上下文处理器            
@app.context_processor
def context_processor():
    if hasattr(g, 'user'):
        return {"user":g.user}
    else:
        return {}


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
