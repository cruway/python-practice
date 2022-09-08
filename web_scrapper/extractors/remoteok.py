from requests import get
from bs4 import BeautifulSoup


def stringRepalce(stringWord):
    if stringWord is None:
        return None
    else:
        return stringWord.replace(",", " ").replace("\n", "").replace(
            "\t", "").lstrip().rstrip()


def extract_remoteok_jobs(keyword):
    header = {"User-Agent": "Kimchi"}
    base_url = f"https://remoteok.com/remote-{keyword}-jobs"
    response = get(f"{base_url}", headers=header)
    results = []
    if response.status_code != 200:
        print("情報取得に失敗しました")
    else:
        soup = BeautifulSoup(response.text, "html.parser")
        job_list = soup.find('table', id="jobsboard")
        jobs = job_list.find_all('tr', class_="job", recursive=False)
        for job in jobs:
            link = job.find("a", class_="preventLink")['href']
            company = job.find("h3", itemprop="name")
            location = job.find("div", class_="location")
            position = job.find("h2", itemprop="title")
            job_data = {
                'link': f"https://remoteok.com{link}",
                'company': stringRepalce(company.string),
                'location': stringRepalce(location.string[2:]),
                'position': stringRepalce(position.string)
            }
            results.append(job_data)
    return results