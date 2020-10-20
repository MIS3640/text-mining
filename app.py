from flask import Flask
import os
import venmo_functions

app = Flask(__name__)


# a simple page that says hello
@app.route("/hello")
def hello():
    venmo_functions.execute()
    return "Hello, World!"
