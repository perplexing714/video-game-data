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
    selYear = "In " + year + ", " + rev + " was the game with the highest average review."
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
    game = request.args.get('game')
    return render_template('page4.html', game_options=games)

@app.route("/thatGraph")
def render_graph(): 
    games = get_game_options()
    game = request.args.get('game')
    graph = get_graph()
    graphdata = thing_test(game)
    return render_template('page4.html', game_options=games, data=graphdata, graph=graph)
    
def get_graph():
    graph = Markup("<div id=""chartContainer"" style=""height: 300px; width: 100%;""></div>")
    return graph 
    
def thing_test(game):
    with open('video_games.json') as game_data:
        data = json.load(game_data)
    graphdata = []
    dp1 = 0
    dp2 = 0
    dp3 = 0
    dp4 = 0
    dp5 = 0
    dp6 = 0
    dp7 = 0
    dp8 = 0
    dp9 = 0
    dp10 = 0
    dp11 = 0
    dp12 = 0
    dp13 = 0
    dp14 = 0
    dp15 = 0
    dp16 = 0
    dp17 = 0
    dp18 = 0
    dp19 = 0
    dp20 = 0
    dataNames = ["AA", "AL", "AM", "AP", "AR", "CA", "CL", "CM", "CP", "CR", "MEA", "MEL", "MEM", "MEP", "MER", "MA", "ML", "MM", "MP", "MR"]
    for c in data: 
        if c["Title"] == game:
            dp1 = {"label": dataNames[0], "y": c["Length"]["All PlayStyles"]["Average"]}
            dp2 = {"label": dataNames[1], "y": c["Length"]["All PlayStyles"]["Leisure"]}
            dp3 = {"label": dataNames[2], "y": c["Length"]["All PlayStyles"]["Median"]}
            dp4 = {"label": dataNames[3], "y": c["Length"]["All PlayStyles"]["Polled"]}
            dp5 = {"label": dataNames[4], "y": c["Length"]["All PlayStyles"]["Rushed"]}
            dp6 = {"label": dataNames[5], "y": c["Length"]["Completionists"]["Average"]}
            dp7 = {"label": dataNames[6], "y": c["Length"]["Completionists"]["Leisure"]}
            dp8 = {"label": dataNames[7], "y": c["Length"]["Completionists"]["Median"]}
            dp9 = {"label": dataNames[8], "y": c["Length"]["Completionists"]["Polled"]}
            dp10 = {"label": dataNames[9], "y": c["Length"]["Completionists"]["Rushed"]}
            dp11 = {"label": dataNames[10], "y": c["Length"]["Main + Extras"]["Average"]}
            dp12 = {"label": dataNames[11], "y": c["Length"]["Main + Extras"]["Leisure"]}
            dp13 = {"label": dataNames[12], "y": c["Length"]["Main + Extras"]["Median"]}
            dp14 = {"label": dataNames[13], "y": c["Length"]["Main + Extras"]["Polled"]}
            dp15 = {"label": dataNames[14], "y": c["Length"]["Main + Extras"]["Rushed"]}
            dp16 = {"label": dataNames[15], "y": c["Length"]["Main Story"]["Average"]}
            dp17 = {"label": dataNames[16], "y": c["Length"]["Main Story"]["Leisure"]}
            dp18 = {"label": dataNames[17], "y": c["Length"]["Main Story"]["Median"]}
            dp19 = {"label": dataNames[18], "y": c["Length"]["Main Story"]["Polled"]}
            dp20 = {"label": dataNames[19], "y": c["Length"]["Main Story"]["Rushed"]}
    graphdata = [dp1, dp2, dp3, dp4, dp5, dp6, dp7, dp8, dp9, dp10, dp11, dp12, dp13, dp14, dp15, dp16, dp17, dp18, dp19, dp20]
    return graphdata
    
if __name__=="__main__":
    app.run(debug=True)
