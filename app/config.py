HOSTNAME = '172.25.0.5'
PORT     = '3306'
DATABASE = 'test_flask'
USERNAME = 'root'
PASSWORD = 'daozhu'
DB_URI   = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8' . format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
# mysql+pymysql://root:daozhu@172.25.0.5:33060/test_flask?charset=utf8
SQLALCHEMY_DATABASE_URI = DB_URI

SECRET_KEY = "ABC123"

# Flask-Mail
MAIL_SERVER = "smtp.qq.com"
MAIL_PORT = "465"
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_DEBUG = True
MAIL_USERNAME = "1622569387@qq.com"
MAIL_PASSWORD = "hshchdbuwpjddbga"
MAIL_DEFAULT_SENDER = "1622569387@qq.com"