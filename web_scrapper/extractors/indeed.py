from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup


def stringRepalce(stringWord):
    if stringWord is None:
        return None
    else:
        return stringWord.replace(",", " ").replace("\n", "").replace(
            "\t", "").lstrip().rstrip()


def get_page_count(keyword):
    print(keyword)
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    browser = webdriver.Chrome(options=options)

    browser.get(f"https://jp.indeed.com/jobs?q={keyword}")
    print(f"https://jp.indeed.com/jobs?q={keyword}")
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
    pagination = soup.find("ul", class_="pagination-list")
    if pagination is None:
        return 1
    pages = pagination.find_all("li", recursive=False)
    count = len(pages)
    if count >= 5:
        return 5
    else:
        return count


def extract_indeed_jobs(keyword):
    pages = get_page_count(keyword);
    results = []
    for page in range(pages):
        options = Options()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        browser = webdriver.Chrome(options=options)

        base_url = "https://jp.indeed.com/jobs"
        final_url = f"{base_url}?q={keyword}&start={page*10}"
        print("Requesting", final_url)
        browser.get(final_url)

        html = browser.page_source
        soup = BeautifulSoup(html, 'html.parser')
        job_list = soup.find("ul", class_="jobsearch-ResultsList")
        jobs = job_list.find_all(('li'), recursive=False)
        for job in jobs:
            zone = job.find("div", class_="mosaic-zone")
            if zone is None:
                anchor = job.select_one("h2 a")
                title = anchor['aria-label']
                link = anchor['href']
                company = job.find("span", class_="companyName")
                location = job.find("div", class_="companyLocation")
                job_data = {
                    'link': f"https://jp.indeed.com{link}",
                    'company': stringRepalce(company.string),
                    'location': stringRepalce(location.string),
                    'position': stringRepalce(title)
                }
                results.append(job_data)
    return results