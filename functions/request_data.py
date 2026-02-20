import requests
import os
import json
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

def requests_data(category, keywords):
    q = keywords if keywords else category
    url = "https://newsapi.org/v2/everything"
    params = {
        "apiKey": os.getenv("NEWSORG_API_KEY"),
        "q": q,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": 10}

    response = requests.get(url=url, params=params)
    if response.status_code != 200:
        raise Exception(f"Could not get data\nStatus code: {response.status_code}")
    data = response.json()
    if data["status"] == "error":
        raise Exception(f"Unexpected error happens in getting news")
    return data["articles"]








# {'author': 'Connie Loizos',
#  'title': 'With co-founders leaving and an IPO looming, Elon Musk turns talk to the moon', 
# 'description': 'According to The New York Times, which reports that it heard the meeting, Musk told employees that xAI needs a lunar manufacturing facility, a factory on the moon that will build AI satellites and fling them into space via a giant catapult.', 
# 'url': 'https://techcrunch.com/2026/02/10/with-co-founders-leaving-and-an-ipo-looming-elon-musk-turns-talk-to-the-moon/', 
# 'source': 'TechCrunch', 
# 'image': None, 
# 'category': 'technology', 
# 'language': 'en', 
# 'country': 'us', 
# 'published_at': '2026-02-11T05:23:26+00:00'}
