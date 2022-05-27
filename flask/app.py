from flask import Flask, render_template, request, redirect
from indeed import get_jobs
from exporter import save_to_file

app = Flask("JobScrapper")
db = {}


@app.route("/")
def potato():
    return render_template("potato.html")


@app.route("/report")
def report():
    word = request.args.get("word")
    if word:
        word = word.lower()
        existing_jobs = db.get(word)
        if existing_jobs:
            jobs = existing_jobs
        else:
            jobs = get_jobs(word)
            db[word] = jobs
        print(jobs)
    else:
        return redirect("/")
    return render_template(
        "report.html",
        searchingBy=word,
        resultNumber=len(jobs),
        jobs=jobs
    )


@app.route("/export")
def export():
    try:
        word = request.args.get('word')
        if not word:
            raise Exception()
        jobs = db.get(word)
        if not jobs:
            raise Exception()
        save_to_file(jobs, word)
        return f"Generate CSV for {word}"
    except:
        return redirect("/")


app.run(host='127.0.0.1')
