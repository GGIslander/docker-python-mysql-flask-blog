from crypt import methods
import imp
from multiprocessing import context
import redis
import time
from flask import Flask, jsonify, url_for, request, redirect,render_template
import config
from apps.book import bp as book_bp
from apps.course import bp as course_bp
from apps.user import bp as user_bp
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

def get_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.3)

    

@app.route('/')
def hello():
    # DB 链接测试
    
    #return config.DB_URI;
    engine = db.get_engine()
    with engine.connect() as conn:
        result = conn.execute("select 1")
        print(result.fetchone())
    cnt = get_count()
    return 'hello world! cnt={}\n{}'.format(cnt, result.fetchone())


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
