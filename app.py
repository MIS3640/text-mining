from flask import Flask
from flask import render_template
import os
import venmo_functions

app = Flask(__name__)


# a simple page that says hello
@app.route("/")
def display_dash():
    venmo_functions.execute()
    user = venmo_functions.get_user_info()
    common_list = venmo_functions.wc_word_list
    emoji_list = venmo_functions.wc_emoji_list
    test_list = [["foo", 4]]
    return render_template(
        "base.html", user=user, common_list=common_list, emoji_list=emoji_list
    )
