# importing libaries
from models import create_classes
import os 
from flask import (
    Flask,
    render_templates
    jsonify,
    request, 
    redirect)

#####################################################################
# Flask Setup 
#####################################################################

app = Flask (__name__)

#####################################################################
Database Setup
#####################################################################

from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('database_URL', '')

# Removing tracking modifacations
app.config['SQLAlCHEMY_TRACKING_MODIFICATIONS'] = False

db = SQLAlchemy(app)


