Dynamic Web Scraper 🚀

A Python-based CLI application that scrapes real-time data from websites including Jobs, Products, and News.
The project demonstrates real-world web scraping, data extraction, search/filtering, and data storage using Python.

📌 Features
✅ Web Scraping

Scrapes data from multiple websites using:

requests
BeautifulSoup
Supported Categories
🧑‍💼 Jobs
🛍 Products
📰 News
📂 Extracted Data
🧑‍💼 Jobs (ActuaryList)

Scrapes:

Job Title
Company Name
Country
Location
Salary
Job Type
Tags
Posted Date
Apply Link

Website Used:
ActuaryList

🛍 Products (BooksToScrape)

Scrapes:

Product Name
Price
Rating
Product Link

Website Used:
BooksToScrape

📰 News (Hacker News)

Scrapes:

News Title
Source
News Link

Website Used:
Hacker News

🔍 Search & Filter Features
Search scraped data using keywords
Filter data by category:
Job
Product
News
💾 Data Storage

The scraped data can be exported to:

JSON
CSV
Excel (.xlsx)

Saved automatically inside the data/ folder.

🧱 Project Structure
dynamic_scraper/
│
├── main.py
│
├── scraper/
│   ├── jobs_scraper.py
│   ├── product_scraper.py
│   └── news_scraper.py
│
├── utils/
│   ├── storage.py
│   ├── search_filter.py
│   └── headers.py
│
├── data/
│   ├── scraped_data.json
│   ├── scraped_data.csv
│   └── scraped_data.xlsx
│
├── requirements.txt
└── README.md
⚙️ Technologies Used
Python 3
Requests
BeautifulSoup4
Pandas
OpenPyXL
📦 Installation
1️⃣ Clone Repository
git clone https://github.com/your-username/dynamic-web-scraper.git
2️⃣ Navigate to Project
cd dynamic-web-scraper
3️⃣ Install Dependencies
pip install -r requirements.txt
▶️ Run Project
python main.py
🖥 Menu System
===== Dynamic Web Scraper =====

1. Scrape Jobs
2. Scrape Products
3. Scrape News
4. Search Data
5. Filter by Category
6. Save Data
7. Exit
📸 Sample Output
🧑‍💼 Job Example
{
  "category": "Job",
  "title": "Associate Actuary (Risk Management)",
  "company": "AIG",
  "country": "🇺🇸 USA",
  "location": "Boston MA, New York NY",
  "salary": "$115k-$145k",
  "job_type": "On-site",
  "date_posted": "20h ago",
  "tags": "Health, Pricing, Risk",
  "link": "https://www.actuarylist.com/actuarial-jobs/73674-aig"
}
🛡 Error Handling

The project includes:

Request exception handling
Timeout handling
Missing field handling
Invalid response handling
🌟 Advanced Features Implemented

✅ Modular Code Structure
✅ Pagination Support (Products)
✅ User-Agent Headers
✅ Search & Filter System
✅ JSON / CSV / Excel Export
✅ Clean Extracted Data
✅ Error Handling

📚 Requirements

Example requirements.txt

requests
beautifulsoup4
pandas
openpyxl
🎥 Deliverables
✅ Source Code
✅ JSON / CSV / Excel Data
✅ README.md
✅ GitHub Repository
✅ Screenshots
✅ Demo Video
👨‍💻 Author

Developed as part of a Python Web Scraping project.

📜 License

This project is for educational purposes only.
