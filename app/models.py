from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
################################################################################################################
#資料庫 model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
################################################################################################################