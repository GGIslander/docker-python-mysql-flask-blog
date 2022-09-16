FROM python:3.8
ADD . /code
WORKDIR /code
RUN pip install redis flask pymysql flask-sqlalchemy Flask-Mail flask_migrate wtforms email_validator
CMD ["python", "app.py"]

