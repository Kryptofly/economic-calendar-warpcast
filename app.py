from flask import Flask, render_template, request, redirect, url_for, flash
from fetcher.fetch_calendar import get_important_news
from utils.warpcast_poster import post_to_warpcast
import os
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)
app.secret_key = os.urandom(24)
scheduler = BackgroundScheduler()
scheduler.start()

def scheduled_post():
    news = get_important_news()
    post_to_warpcast(news)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/post_now', methods=['POST'])
def post_now():
    news = get_important_news()
    post_to_warpcast(news)
    flash('News posted to Warpcast!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Schedule the job to run every day at a specific time
    scheduler.add_job(scheduled_post, 'cron', hour=8, minute=0)
    app.run(debug=True)
