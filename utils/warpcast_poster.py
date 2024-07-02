import requests
from jinja2 import Environment, FileSystemLoader
from config import WARPCAST_API_TOKEN

def render_news_template(news):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('frame_template.txt')
    return template.render(important_news=news)

def post_to_warpcast(news):
    content = render_news_template(news)
    warpcast_url = "https://api.warpcast.com/v1/frames"
    headers = {
        'Authorization': f'Bearer {WARPCAST_API_TOKEN}',
        'Content-Type': 'application/json'
    }
    payload = {
        'content': content
    }
    response = requests.post(warpcast_url, headers=headers, json=payload)
    response.raise_for_status()
