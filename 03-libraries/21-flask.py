"""
Day 21 - falsk in python
Topic - first website in pyhton
Author - Uma
Date - 25-10-2026
"""

from flask import Flask

# cerate the flask application

app = Flask(__name__)

#create the home page
@app.route("/")
def home():
    return "<h1>hello, world!</h1><p>My first website using python!</p>"

#run the website
if __name__ == "__main__":
    app.run(debug=True)