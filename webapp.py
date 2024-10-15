from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

<<<<<<< HEAD
@app.route("/home")
def render_main():
    return render_template('home.html')
    
if __name__=="__main__":
    app.run(debug=True)
=======
@app.route("/")
def render_main():
    return render_template('home.html')
>>>>>>> 26d2f4a45854a0d884ebd4e144fcc9911065425b
