from flask import Blueprint, render_template
from website.utility import save_cookie

frontend = Blueprint('frontend', __name__)

@frontend.route('/')
def index():
    save_cookie("index")
    return render_template("index.html")
