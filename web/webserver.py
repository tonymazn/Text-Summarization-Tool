# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
from core.textsummarize import get_summary

app = Flask(__name__)
 
@app.route("/")
def index():
    return render_template('index.html', originalText='', summary='', count=4)


@app.route("/process", methods=['POST'])
def process():
    if request.method=='POST':
       text = request.form['text']
       count = request.form['count']
       summary = get_summary(text, count)
       return render_template('index.html',text=text, summary=summary, count=count)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
