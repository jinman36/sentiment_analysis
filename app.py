import os

import pandas as pd
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from model import model


# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/", methods=["GET", "POST"])
def index():
    """Input text message"""
    return render_template("index.html")


@app.route("/about")
def about():
    """Input text message"""
    return render_template("about.html")


@app.route("/result", methods=["POST"]) # Complete
def result():
    
    text = request.form.get("comments")
    result = model(text)
    
    # Read CSV file into DataFrame
    df = pd.read_csv('tweet_data.csv')
    max_number = df['textID'].max()
    new_row = {'textID': max_number + 1, 'tweet_text': text.strip(), 'sentiment': result}
    df.loc[len(df.index)] = new_row 
    df.to_csv('tweet_data.csv', index=False)

    
    return render_template("/result.html", result=result, text=text)
