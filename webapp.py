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
    titles = get_game_options()
    title = request.args.get('title')
    factTitle = title 
    return render_template('page2.html', game_options=titles, funFactName=factTitle)


def get_game_options():
    with open('video_games.json') as game_data:
        data = json.load(game_data)
    titles=[]
    for g in data:
        if g["Title"] not in titles:
            titles.append(g["Title"])
    options=""
    for s in titles:
        options += Markup("<option value=\"" + s + "\">" + s + "</option>") 
    return options
    
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

<<<<<<< HEAD
=======

>>>>>>> 02b5efb0097b27b069659f0b7eb9ee2789a5aaef
