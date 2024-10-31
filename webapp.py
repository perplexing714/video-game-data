from flask import Flask, request, render_template, flash
from markupsafe import Markup

import os
import json

app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template('home.html')
    
@app.route("/p2")
def render_page2():
    titles = get_game_options()
    return render_template('page2.html', game_options=titles)
    
@app.route("/showFact")
def render_fact():
    with open('video_games.json') as game_data:
        game_data = json.load(game_data)
        if "title" in request.args:      
            title = request.args.get('title')
            for titles in game_data:
                if titles["Title"] == title:
                    cons = titles["Release"]["Console"]
                    rat = titles["Release"]["Rating"]
                    yearr = titles["Release"]["Year"]
                    usp = titles["Metrics"]["Used Price"]
                    revs = titles["Metrics"]["Review Score"]
                    sales = titles["Metrics"]["Sales"]               
    factTitle = "For " + title + ", here are some fun facts:"
    uspF = "Used Price for this game: " + str(usp) + "."
    revsF = "Review Score (out of 100): " + str(revs) + "."
    salesF = "Sales (in millions): " + str(sales) + "."
    yearrF = "Year of Release: " + str(yearr) + "."
    ratF = "Game rating: " + rat + "."
    consF = "Released on what console?: " + str(cons) + "."
    titles = get_game_options()
    div1 = "Release Facts:"
    div2 = "Other:"
    return render_template('page2.html', div1=div1, div2=div2, game_options=titles, funFactName=factTitle, usp=uspF, revs=revsF, sales=salesF, yearr=yearrF, rat=ratF, cons=consF)

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

def get_year_options():
    with open('video_games.json') as game_data:
        data = json.load(game_data)
    years=[]
    for g in data:
        if g["Release"]["Year"] not in years:
            years.append(g["Release"]["Year"])
    options=""
    for f in years:
        options += Markup("<option value=\"" + str(f) + "\">" + str(f) + "</option>") 
    return options

@app.route("/p3")
def render_page3(): 
    years = get_year_options()
    return render_template('page3.html', year_options=years)
    
@app.route("/showHighestReview")
def render_fact2():
    years = get_year_options()
    year = request.args.get('year')
    rev = highest_review_score_year(year)
    selYear = "For " + year + ", " + rev + " was the game with the highest average review."
    reviewName = rev
    return render_template('page3.html', reviewName=reviewName, year_options=years, selYear=selYear)

def highest_review_score_year(year):
    with open('video_games.json') as game_data:
        data3 = json.load(game_data)
    highest = 0
    rev = "a" 
    for r in data3:
        if r["Release"]["Year"] == int(year):
            if r["Metrics"]["Review Score"] > highest: 
                highest = r["Metrics"]["Review Score"]
                rev = r["Title"]
    return rev

@app.route("/year")
def render_test(): 
    years = get_year_options()
    year = request.args.get('year')
    reviewName = year
    return render_template('page3.html', year_options=years, reviewName=reviewName)  
    
@app.route("/p4")
def render_page4():
    games = get_game_options()
    return render_template('page4.html', game_options=games)


    
if __name__=="__main__":
    app.run(debug=True)

