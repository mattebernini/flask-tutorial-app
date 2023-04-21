from . import db
from .models import Visite
from sqlalchemy import text, func, case
from flask import request

def save_cookie(content):
    ip_addr = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)   
    # if ip_addr == "127.0.0.1":
    #    return
    visita = Visite(giorno=func.now(), user_agent=request.user_agent.string, ip_addr=ip_addr, content=content)
    db.session.add(visita)
    db.session.commit()

def query(sql_filename):
    with open("sql/"+sql_filename+".sql", "r") as f:
        q = f.read()
        return db.session.execute(text(q))