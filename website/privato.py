from flask import Blueprint, render_template
from website.utility import save_cookie, query

privato = Blueprint('privato', __name__)

# http://localhost:5000/privato/abc
@privato.route('/<parola>')
def index(parola):
    save_cookie(parola)
    return render_template("index.html", parola=parola)

# http://localhost:5000/privato/db
@privato.route('/db')
def db():
    save_cookie("db")
    return render_template("db.html", 
                           dati=query("visite_totali"))