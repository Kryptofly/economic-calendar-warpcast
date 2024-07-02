import requests
from bs4 import BeautifulSoup
from config import MYFXBOOK_CALENDAR_URL

def get_important_news():
    response = requests.get(MYFXBOOK_CALENDAR_URL)
    soup = BeautifulSoup(response.content, 'html.parser')

    important_news = []
    for event in soup.select('.calendarRow'):
        impact = event.select_one('.impact').get('title', '')
        if 'High' in impact:
            time = event.select_one('.calendarTime').get_text(strip=True)
            currency = event.select_one('.calendarCurrency').get_text(strip=True)
            event_title = event.select_one('.calendarEvent').get_text(strip=True)
            important_news.append({
                'time': time,
                'currency': currency,
                'event': event_title
            })
    return important_news
