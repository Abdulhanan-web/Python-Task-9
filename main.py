# main.py

from scraper.jobs_scraper import scrape_jobs
from scraper.product_scraper import scrape_products
from scraper.news_scraper import scrape_news

from utils.search_filter import (
    search_data,
    filter_by_category
)

from utils.storage import (
    save_json,
    save_csv,
    save_excel
)


all_data = []


while True:

    print("\n===== Dynamic Web Scraper =====")
    print("1. Scrape Jobs")
    print("2. Scrape Products")
    print("3. Scrape News")
    print("4. Search Data")
    print("5. Filter by Category")
    print("6. Save Data")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        jobs = scrape_jobs()
        all_data.extend(jobs)

        print(f"{len(jobs)} jobs scraped.")

    elif choice == "2":

        products = scrape_products()
        all_data.extend(products)

        print(f"{len(products)} products scraped.")

    elif choice == "3":

        news = scrape_news()
        all_data.extend(news)

        print(f"{len(news)} news articles scraped.")

    elif choice == "4":

        keyword = input("Enter keyword: ")

        results = search_data(all_data, keyword)

        for item in results:
            print(item)

    elif choice == "5":

        category = input("Enter category: ")

        results = filter_by_category(all_data, category)

        for item in results:
            print(item)

    elif choice == "6":

        save_json(all_data)
        save_csv(all_data)
        save_excel(all_data)

        print("Data saved successfully.")

    elif choice == "7":

        print("Exiting program...")
        break

    else:
        print("Invalid choice.")