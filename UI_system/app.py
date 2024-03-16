# Importing Flask
from flask import Flask
from flask import render_template
import numpy
import requests

# Creating instance 
app = Flask(__name__)

# Creating routes
@app.route("/")
def index():
    return render_template("UI_system/templates/index.html")

if __name__ == "__main__":
    app.run(debug=True)