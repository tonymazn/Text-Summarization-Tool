# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
from core.textsummarize import get_summary
from core.algorithms import algorithms

def generate_index(text, summary, count, algorithm):
    return render_template('index.html',text=text, summary=summary, count=count, algorithms=algorithms, algorithm=algorithm)

app = Flask(__name__)
 
@app.route("/")
def index():
    return generate_index('', '', 4, algorithms.TextRank.value)


@app.route("/process", methods=['POST'])
def process():
    if request.method =='POST':
       text = request.form['text']
       count = request.form['count']
       name = request.form['algorithm']
       print('post back:')
       print(name)
       summary = get_summary(text, count, name)
       return generate_index(text, summary, count, name)

if __name__ == "__main__":
    app.run(host='0.0.0.0')


