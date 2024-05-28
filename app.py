from flask import Flask, render_template, request
import random
import redis

REDIS_URL = 'redis://default:ETw7er7MYHFCWvHIdi8c0BvfKtJKyqSD@redis-16065.c278.us-east-1-4.ec2.cloud.redislabs.com:16065'
r = redis.from_url(REDIS_URL, encoding='utf-8',decode_responses=True)

app = Flask(__name__)

@app.before_request
def check_request():
    if 'Mozilla' not in request.headers.get('User-Agent'):
        abort(403)

@app.route('/')
def index():
    videos = list(r.smembers("Reels"))
    random.shuffle(videos)
    return render_template('index.html', videos=videos)

if __name__ == '__main__':
    app.run(debug=True)
