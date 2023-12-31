# import necessary libraries
# from models import create_classes
import os
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, or_
from sqlalchemy.ext.automap import automap_base

import pickle

from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

engine = create_engine("sqlite:///basketball.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
print(Base.classes.keys())

nba_stadiums = Base.classes.NBAstadiums
teams = Base.classes.teams_info
ranking = Base.classes.ranking

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


# ---------------------------------------------------------
# Web site
@app.route("/")
def home():
    return render_template("index.html")