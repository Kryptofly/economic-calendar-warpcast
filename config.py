import os
from dotenv import load_dotenv

load_dotenv()

WARPCAST_API_TOKEN = os.getenv('WARPCAST_API_TOKEN')
MYFXBOOK_CALENDAR_URL = "https://www.myfxbook.com/forex-economic-calendar"
