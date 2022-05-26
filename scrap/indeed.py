# -*- coding: utf-8 -*-
import requests as r
from bs4 import BeautifulSoup

LIMIT = 50
MAIN_URL = "https://kr.indeed.com"
URL = f"{MAIN_URL}/취업?q=파이썬&limit={LIMIT}"


def get_last_page():
    result = r.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")

    pagination = soup.find("div",  {"class": "pagination"})
    links = pagination.find_all('a')
    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))

    max_page = pages[-1]
    return max_page


def extract_jobs_process(html):
    job_title = html.find_next("a", "jcs-JobTitle")
    title = job_title.string
    job_id = job_title['data-jk']
    company_info = html.find("div", "companyInfo")
    company = company_info.find("span", {"class": "companyName"})
    location = company_info.find("div", "companyLocation").string
    location = location if location is not None else ""
    company_name = ""
    company_link = ""
    if company is not None:
        company_name = company.string
        if company.find("a", "companyOverviewLink") is not None:
            company_link = MAIN_URL + company.find("a", "companyOverviewLink")['href']
    return {
        "job_id": job_id,
        "title": title,
        "job_link": f"{URL}&vjk={job_id}",
        "company": company_name,
        "company_link": company_link,
        "location": location
    }


def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping Indeed Page {page}")
        result = r.get(f"{URL}&start={LIMIT * page}")
        soup = BeautifulSoup(result.content, "html.parser")
        results = soup.find_all("div", {"class": "job_seen_beacon"})
        for a in results:
            job = extract_jobs_process(a)
            jobs.append(job)
    return jobs


def get_jobs():
    max_pages = get_last_page()
    jobs = extract_jobs(max_pages)
    return jobs
