from datetime import datetime
from flask import render_template
from FlaskWebProject1 import app
import psycopg2
import redis
from FlaskWebProject1 import config

redis_client = redis.StrictRedis(host=config.REDIS_HOST, port=config.REDIS_PORT, decode_responses=True)

@app.route('/')
@app.route('/home')
def home():
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/db-test')
def db_test():
    try:
        conn = psycopg2.connect(
            host=config.POSTGRES_HOST,
            database=config.POSTGRES_DB,
            user=config.POSTGRES_USER,
            password=config.POSTGRES_PASSWORD
        )
        cur = conn.cursor()
        cur.execute("SELECT NOW();")
        result = cur.fetchone()
        conn.close()
        return f"Postgres Connected — Server Time: {result}"
    except Exception as e:
        return f"Postgres {str(e)}"


@app.route('/cache-test')
def cache_test():
    try:
        count = redis_client.incr("visits")
        return f"Redis Connected - Visit Count: {count}"
    except Exception as e:
        return f"Redis {str(e)}"
