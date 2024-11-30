from flask import Flask 
from app.models import db
from app.routes import main
from  dotenv import load_dotenv
import os
################################################################################################################
load_dotenv()

################################################################################################################

def create_app():
  app = Flask(__name__)
  #MYSQL configuration
  app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

  
  db.init_app(app)              # Initialize extensions
  app.register_blueprint(main)  # Register blueprints
  
  return app 
################################################################################################################

