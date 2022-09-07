from requests import get
from bs4 import BeautifulSoup


def extract_remoteok_jobs(keyword):
    header = {"User-Agent": "Kimchi"}
    base_url = f"https://remoteok.com/remote-{keyword}-jobs"
    response = get(f"{base_url}", headers=header)
    if response.status_code != 200:
        print("情報取得に失敗しました")
    else:
        soup = BeautifulSoup(response.text, "html.parser")
        job_list = soup.find('table', id="jobsboard")
        jobs = job_list.find_all('tr', class_="job", recursive=False)
        print(jobs)


searchKeywords = ("rust", "golang", "python", "react")

extract_remoteok_jobs("rust")
for keyword in searchKeywords:
    print(keyword)
