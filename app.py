from flask import Flask, redirect, render_template, url_for
import dbfunctions as dbf
from models import Guide

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('home'))


@app.route('/home')
def home():
    query = dbf.get_last_guide()
    last_guide = Guide(query[0], query[1], query[2], query[3], query[4])
    return render_template('index.html', last_guide=last_guide)


@app.route('/guides')
def guides():
    query = dbf.get_all_guides()
    all_guides = []
    for item in query:
        print(item)
        guide = Guide(item[0], item[1], item[2], item[3], item[4])
        all_guides.append(guide)

    return render_template('guides.html', all_guides=all_guides)


@app.route('/guide/<id>')
def guide(id):
    query = dbf.get_guide_by_id(id)
    guide = Guide(query[0], query[1], query[2], query[3], query[4])
    return render_template('guide.html', guide=guide)
