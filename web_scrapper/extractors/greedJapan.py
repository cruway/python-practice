from requests import get
from bs4 import BeautifulSoup

def stringRepalce(stringWord):
    if stringWord is None:
        return None
    else:
        return stringWord.replace(",", " ")

def get_page_count(keyword):
    base_url = "https://www.green-japan.com/search_key/01?key=vdjgfsxscaxvtfi8fejf&keyword="
    response = get(f"{base_url}{keyword}")

    if response.status_code != 200:
        print("情報取得に失敗しました。")
    else:
        soup = BeautifulSoup(response.text, 'html.parser')
        pagination = soup.find("nav", class_="pagy_nav pagination")
        if pagination is None:
            return 1
        url_link = pagination.find_all('a').pop(-2)
        return int(url_link.get_text())

def extract_green_jobs(keyword):
    pages = get_page_count(keyword)
    results = []
    base_url = "https://www.green-japan.com/search_key/01?key=vdjgfsxscaxvtfi8fejf&keyword="
    for page in range(1, pages + 1):
        response = get(f"{base_url}{keyword}&page={page}")
        if response.status_code != 200:
            print("情報取得に失敗しました。")
        else:
            soup = BeautifulSoup(response.text, "html.parser")
            job_list = soup.find("div", class_="srch-rslt")
            jobs = job_list.find_all(('div'), class_="card-info__wrapper js-card-info__wrapper", recursive=False)
            for job in jobs:
                link = job.find("a")['href']
                position = job.find("div", class_="job-offer-icon").get_text() + '/' +job.find("h3", class_="card-info__heading-area__title").get_text()
                company = job.find("h3", class_="card-info__detail-area__box__title").get_text()
                metatags = job.find("ul", class_="job-offer-meta-tags").find_all('li')
                location = ""
                i = 0
                for metatag in metatags:
                    if metatag.find("span", class_="icon-site") is not None:
                        location = metatag.get_text()
                        break
                    else:
                        i += 1
                job_data = {
                    'link': f"https://www.green-japan.com{link}",
                    'company': stringRepalce(company),
                    'location': stringRepalce(location),
                    'position': stringRepalce(position)
                }
                results.append(job_data)
    return results