from flask import Flask, render_template, request, redirect, send_file
#from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs
from extractors.greedJapan import extract_green_jobs
from extractors.remoteok import extract_remoteok_jobs
from file import save_to_file

app = Flask("JobScrapper")


@app.route("/")
def home():
    return render_template("index.html", name="sim")


db = {}


@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    if keyword is None:
        return redirect("/")
    if keyword in db:
        jobs = db[keyword]
    else:
        #indeed = extract_indeed_jobs(keyword)
        wwr = extract_wwr_jobs(keyword)
        greenJapan = extract_green_jobs(keyword)
        remoteok = extract_remoteok_jobs(keyword)
        jobs = wwr + greenJapan + remoteok
        db[keyword] = jobs
    return render_template("search.html", keyword=keyword, jobs=jobs)


@app.route("/export")
def export():
    keyword = request.args.get("keyword")
    if keyword is None:
        return redirect("/")
    if keyword not in db:
        return redirect(f"/search?keyword={keyword}")
    print("keyword save")
    print(db[keyword])
    save_to_file(keyword, db[keyword])
    return send_file(f"{keyword}.csv", as_attachment=True)


app.run()