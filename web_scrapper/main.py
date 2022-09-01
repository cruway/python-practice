from requests import get
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
#from extractors.wwr import extract_jobs

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
browser = webdriver.Chrome(options=options)

browser.get("https://jp.indeed.com/jobs?q=python&limit=50")

html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')
job_list = soup.find("ul", class_="jobsearch-ResultsList")
jobs = job_list.find_all(('li'), recursive=False)
for job in jobs:
    zone = job.find("div", class_="mosaic-zone")
    if zone == None:
        print("job li")
    else:
        print("mosaic li")