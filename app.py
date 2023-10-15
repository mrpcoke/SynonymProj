#This Python Flask app connects to the DataMuse API 
#and retrieves synonmys pertaining to the word 
#that is sent to the api.
#Python App written by Paul Coke (c)2023


from flask import Flask, url_for, render_template, redirect, request
import requests
import json

app = Flask(__name__)

@app.route("/")
def index():
    return "<h2>You are on the home page</h2>"

@app.route("/getdata<myword>")
def getdata(myword):
    res = requests.get(f"https://api.datamuse.com/words?rel_syn={myword}") 
    json_resp = res.json()
    theword = {
        
        'synonyms' : json_resp
    }
    return render_template("results.html",theword=theword)


@app.route("/searchform",methods=["POST","GET"])
def form():
    if request.method == "POST":
        wrd = request.form["txtSearch"]
        return redirect(url_for("getdata",myword=wrd))
    else:
        return render_template("form.html")


if(__name__ == "__main__"):
    app.run(debug=True)


