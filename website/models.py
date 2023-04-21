from . import db
from sqlalchemy import func

class Visite(db.Model):
    __tablename__ = "Visite"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    giorno = db.Column(db.Date)
    user_agent = db.Column(db.String, unique=False)    
    content = db.Column(db.String, unique=False)
    ip_addr = db.Column(db.String, unique=False)    