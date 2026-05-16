# scraper/jobs_scraper.py

import requests
from bs4 import BeautifulSoup
from utils.headers import HEADERS


BASE_URL = "https://www.actuarylist.com"


def scrape_jobs():

    jobs = []

    try:
        response = requests.get(BASE_URL, headers=HEADERS, timeout=15)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        job_cards = soup.find_all("div", class_="Job_job-card-active__6V_ep")

        for card in job_cards:

            try:
                # ---------------- TITLE ----------------
                title_tag = card.find("p", class_="Job_job-card__position__ic1rc")
                title = title_tag.get_text(strip=True) if title_tag else "No Title"

                # ---------------- COMPANY ----------------
                company_tag = card.find("p", class_="Job_job-card__company__7T9qY")
                company = company_tag.get_text(strip=True) if company_tag else "Unknown"

                # ---------------- LINK ----------------
                link_tag = card.find("a", class_="Job_job-page-link__a5I5g")
                link = BASE_URL + link_tag["href"] if link_tag else BASE_URL

                # ---------------- LOCATION + COUNTRY + SALARY ----------------
                location_block = card.find("div", class_="Job_job-card__locations__x1exr")

                country = ""
                salary = ""
                locations = []

                if location_block:
                    for child in location_block.find_all(["a", "p"]):

                        text = child.get_text(strip=True)

                        if "💰" in text:
                            salary = text.replace("💰", "").strip()

                        elif "🇺🇸" in text or "🇨🇦" in text or "🇬🇧" in text:
                            country = text

                        elif "cities" in child.get("href", ""):
                            continue

                        elif text:
                            locations.append(text)

                location = ", ".join(locations) if locations else "Remote"

                # ---------------- TAGS ----------------
                tags_block = card.find("div", class_="Job_job-card__tags__zfriA")

                tags = []
                if tags_block:
                    tag_items = tags_block.find_all("a")
                    tags = [t.get_text(strip=True) for t in tag_items if t.get_text(strip=True)]

                # ---------------- DATE POSTED ----------------
                date_tag = card.find("p", class_="Job_job-card__posted-on__NCZaJ")
                date_posted = date_tag.get_text(strip=True) if date_tag else "Unknown"

                # ---------------- LOGO (BONUS FIELD) ----------------
                logo_tag = card.find("img")
                logo = logo_tag["src"] if logo_tag else None

                # ---------------- FINAL STRUCTURE ----------------
                jobs.append({
                    "category": "Job",
                    "title": title,
                    "company": company,
                    "country": country,
                    "location": location,
                    "salary": salary,
                    "job_type": "Remote" if "remote" in location.lower() else "On-site",
                    "date_posted": date_posted,
                    "tags": ", ".join(tags),
                    "link": link,
                    "logo": logo
                })

            except Exception as e:
                print("Error parsing job card:", e)
                continue

        return jobs

    except requests.exceptions.RequestException as e:
        print("Request failed:", e)
        return []

    except Exception as e:
        print("Unexpected error:", e)
        return []