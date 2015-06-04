from flask import Flask
from redis import Redis
import os
app = Flask(__name__)
redis = Redis(host='redis', port=6379)


@app.route('/')
def hello():
    redis.incr('hits')
    response = '''Hello World!
    I have been seen %s times.
    I have been deployed %s times.'''
    return response % (redis.get('hits'), redis.get('starts'))


@app.before_first_request
def before_first_request():
    redis.incr('starts')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
