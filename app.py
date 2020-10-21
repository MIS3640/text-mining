from flask import Flask
from flask import render_template
import os
import venmo_functions

app = Flask(__name__)


# a simple page that says hello
@app.route("/")
def display_dash():
    common_list = venmo_functions.execute_most_common()
    emoji_list = venmo_functions.execute_emoji_list()
    test_list = [["foo", 4]]
    return render_template("base.html", common_list=common_list, emoji_list=emoji_list)
