# -*- coding: utf-8 -*-
import requests as r
from bs4 import BeautifulSoup

MAIN_URL = "https://stackoverflow.com"
URL = f"{MAIN_URL}/jobs/companies?tl=python"


# &pg=i


def get_last_page():
    result = r.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("div", {"class": "s-pagination"}).find_all("a")
    last_page = pagination[-2].get_text(strip=True)
    return int(last_page)


def extract_jobs_process(html):
    company = html.find("h2", {"class": "mb4"}).find("a", {"class": "s-link"})
    company_title = company.text
    company_link = company['href']
    location = html.find("div", {"class": "gsx"}).find("div", {"class": "fc-black-500"}).text
    return {"title": company_title, "link": company_link, "location": location.strip().replace(';', ',')}


def extract_jobs(last_page):
    jobs = []
    for page in range(1, last_page + 1):
        print(f"Scrapping StackOverflow Page {page}")
        result = r.get(f"{URL}&pg={page}")
        soup = BeautifulSoup(result.content, "html.parser")
        results = soup.find_all("div", {"class": "-company"})
        for a in results:
            job = extract_jobs_process(a)
            jobs.append(job)
    return jobs


def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs
