# scraper/news_scraper.py

import requests
from bs4 import BeautifulSoup
from utils.headers import HEADERS


def scrape_news():

    url = "https://news.ycombinator.com/"

    news_data = []

    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        titles = soup.find_all("span", class_="titleline")

        for item in titles[:10]:

            anchor = item.find("a")

            title = anchor.text
            link = anchor["href"]

            news_data.append({
                "category": "News",
                "title": title,
                "source": "Hacker News",
                "link": link
            })

        return news_data

    except Exception as e:
        print("Error scraping news:", e)
        return []