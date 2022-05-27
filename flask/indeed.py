# -*- coding: utf-8 -*-
import requests as r
from bs4 import BeautifulSoup

LIMIT = 50
MAIN_URL = "https://kr.indeed.com"


def get_last_page(url):
    result = r.get(url)
    soup = BeautifulSoup(result.text, "html.parser")

    pagination = soup.find("div",  {"class": "pagination"})
    if pagination is None:
        return 1
    links = pagination.find_all('a')
    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))

    max_page = pages[-1]
    return max_page


def extract_jobs_process(html, url):
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
        "title": title,
        "company": company_name,
        "link": f"{url}&vjk={job_id}",
        "location": location
    }


def extract_jobs(last_page, url):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping Indeed Page {page + 1}")
        result = r.get(f"{url}&start={LIMIT * page}")
        soup = BeautifulSoup(result.content, "html.parser")
        results = soup.find_all("div", {"class": "job_seen_beacon"})
        for a in results:
            job = extract_jobs_process(a, url)
            jobs.append(job)
    return jobs


def get_jobs(word):
    url = f"{MAIN_URL}/취업?q={word}&limit={LIMIT}"
    max_pages = get_last_page(url)
    jobs = extract_jobs(max_pages, url)
    return jobs
