from flask import Flask, request, render_template, flash
from markupsafe import Markup

import os
import json

app = Flask(__name__)

@app.route("/home")
def render_main():
    return render_template('home.html')
    
@app.route("/p2")
def render_page2():
    titles = get_game_options()
    return render_template('page2.html', game_options=titles)
    
@app.route("/showFact")
def render_fact():
    titles = get_game_options()
    title = request.args.get('title')
    factTitle = "For " + title + ", here are the following stats:"
    return render_template('page2.html', game_options=titles, funFactName=factTitle)

def get_game_options():
    with open('video_games.json') as game_data:
        data = json.load(game_data)
    titles=[]
    for c in data:
        if c["Title"] not in titles:
            titles.append(c["Title"])
    options=""
    for s in titles:
        options += Markup("<option value=\"" + s + "\">" + s + "</option>") 
    return options

@app.route("/p3")
def render_page3(): 
    years = get_year_options()
    return render_template('page3.html', year_options=years)

@app.route("/year")
def render_test(): 
    years = get_year_options()
    year = request.args.get('review')
    reviewName = year
    return render_template('page3.html', year_options=years, reviewName=reviewName)
    
def get_year_options():
    with open('video_games.json') as game_data:
        data2 = json.load(game_data)
    years=[]
    for g in data2:
        if g["Release"]["Year"] not in years:
            years.append(g["Release"]["Year"])
    options=""
    for f in years:
        options += Markup("<option value=\"" + str(f) + "\">" + str(f) + "</option>") 
    return options
    
@app.route("/showHighestReview")
def render_fact2():
    years = get_year_options()
    year = request.args.get('review')
    rev = highest_review_score_year()
    reviewName = rev
    return render_template('page3.html', reviewName=reviewName)

def highest_review_score_year():
    with open('video_games.json') as game_data:
        data3 = json.load(game_data)
    year = request.args['year']
    highest = 50
    rev = "" 
    for r in data3:
        if r["Title"] == title:
            if r["Metrics"]["Review Score"] > highest: 
                highest = r["Metrics"]["Review Score"]
                rev = r["Title"]
    return rev 
"""
def county_most_under_18(state):
    with open('demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    highest=0
    county = ""
    for c in counties:
        if c["State"] == state:
            if c["Age"]["Percent Under 18 Years"] > highest:
                highest = c["Age"]["Percent Under 18 Years"]
                county = c["County"]
    return county
"""
@app.route("/p3")
def render_p3():
    return render_template('page3.html')
    
if __name__=="__main__":
    app.run(debug=True)

