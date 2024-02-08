import os

# from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from model import model
# from werkzeug.security import check_password_hash, generate_password_hash
# from datetime import datetime
# import sqlite3

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure SQLIite - if needed
# conn = sqlite3.connect('texts.db', check_same_thread=False)
# conn.row_factory = sqlite3.Row
# db = conn.cursor()


@app.route("/", methods=["GET", "POST"])
def index():
    """Input text message"""
    return render_template("index.html")


@app.route("/about")
def about():
    """Input text message"""
    return render_template("about.html")


@app.route("/analysis", methods=["POST"]) # Complete
def analysis():
    text = request.form.get("comments")
    result = model(text)
    return render_template("/result.html", result=result, text=text)
