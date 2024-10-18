from flask import Flask, url_for, render_template, request, redirect, flash
from markupsafe import Markup

import os
import json

app = Flask(__name__)

@app.route("/")
def root(): 
    return redirect(url_for('render_main'))

@app.route("/home")
def render_main():
    return render_template('home.html')
    
@app.route("/p2")
def render_page2():
    Title = get_game_options()
    return render_template('page2.html', game_options=Title)
    
@app.route("/showFact")
def render_fact():
    Titles = get_game_options()
    Title = request.args.get('Title')
    thing = game_highest_review(Title)
    fact = "The game with the highest review score is " + Title + ", with an average rating of " + thing + "."
    return render_template('home.html', game_options=Titles, funFact=fact)


def get_game_options():
    with open('video_games.json') as game_data:
        data = json.load(game_data)
    Titles=[]
    for g in data:
        if g["Title"] not in Titles:
            Titles.append(g["Title"])
    options=""
    for s in Titles:
        options += Markup("<option value=\"" + s + "\">" + s + "</option>") 
    return options
    
def game_highest_review():
    with open('video_games.json') as game_data:
        data = json.load(game_data)
    highest=0
    thing = ""
    for c in data:
        if c["Title"] == Title:
            if c["Metrics"]["Review Score"] > highest:
                highest = c["Metrics"]["Review Score"]
                thing = c["Title"]
    return thing    
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

