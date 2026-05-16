# scraper/product_scraper.py

import requests
from bs4 import BeautifulSoup
from utils.headers import HEADERS


def scrape_products():

    products = []

    for page in range(1, 3):

        url = f"https://books.toscrape.com/catalogue/page-{page}.html"

        try:
            response = requests.get(url, headers=HEADERS)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")

            books = soup.find_all("article", class_="product_pod")

            for book in books:

                name = book.h3.a["title"]

                price = book.find("p", class_="price_color").text

                rating = book.p["class"][1]

                link = (
                    "https://books.toscrape.com/catalogue/"
                    + book.h3.a["href"]
                )

                products.append({
                    "category": "Product",
                    "name": name,
                    "price": price,
                    "rating": rating,
                    "link": link
                })

        except Exception as e:
            print("Error scraping products:", e)

    return products